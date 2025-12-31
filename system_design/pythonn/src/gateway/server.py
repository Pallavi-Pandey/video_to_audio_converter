import os,gridfs,pika,json,logging,traceback,sys
# gridfs is used to store large files in mongodb
# pika is used to connect to rabbitmq
from flask import Flask,request,Response,send_file
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util
from bson.objectid import ObjectId

# Configure logging to stdout with detailed formatting
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

server = Flask(__name__)
server.logger.setLevel(logging.DEBUG)

# Global error handler - logs full stack trace for any unhandled exception
@server.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled exception: {e}\n{traceback.format_exc()}")
    return "Internal Server Error", 500

# Log all incoming requests
@server.before_request
def log_request():
    logger.info(f"Request: {request.method} {request.path} from {request.remote_addr}")
mongo_host = os.getenv("MONGO_HOST", "mongodb")
server.config["MONGO_URI"] = f"mongodb://{mongo_host}:27017/videos"

mongo_video = PyMongo(
    server,
    uri=f"mongodb://{mongo_host}:27017/videos"
)

mongo_audio = PyMongo(
    server,
    uri=f"mongodb://{mongo_host}:27017/mp3s"
)

fs_video=gridfs.GridFS(mongo_video.db)
fs_audio=gridfs.GridFS(mongo_audio.db)

connection=pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel=connection.channel()
# this will create the queue if it does not exist
# this is synchronous queue declaration, we are not using async here because this is a simple example, in production we should use async


@server.route("/login",methods=["POST"])
def login():
    token,err= access.login(request)

    if not err:
        return token
    else:
        return err
    
@server.route("/upload",methods=["POST"])
def upload():
    access,err= validate.token(request)

    access=json.loads(access)
    if access['authz']:
        if len(request.files) > 1 or len(request.files)<1:
            return "exactly 1 file required",400
        
        for _,f in request.files.items():
            err=util.upload(f,fs_video,channel,access)
            if err:
                return err
        return "success!",200
    else:
        return "not authorized",401
    
@server.route("/download",methods=["GET"])
def download():
    access,err= validate.token(request)
    if err:
        return err
    access=json.loads(access)
    if access['authz']:
        fid_string=request.args.get("fid")
        if not fid_string:
            return "fid is required",400
        
        try:
            out=fs_audio.get(ObjectId(fid_string))
            return send_file(out,download_name=f'{fid_string}.mp3')
        except Exception as e:
            print(e)
            return "internal server error",500
        
    
    return "not authorized",401
        


if __name__ == "__main__":
    server.run(host="0.0.0.0",port=8080)