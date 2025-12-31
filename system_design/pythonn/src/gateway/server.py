import os,gridfs,pika,json,logging,traceback,sys
# gridfs is used to store large files in mongodb
# pika is used to connect to rabbitmq
from flask import Flask,request,Response
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util

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
server.config["MONGO_URI"] = os.getenv("MONGO_URI","mongodb://host.minikube.internal:27017/videos")

mongo = PyMongo(server)

fs=gridfs.GridFS(mongo.db)

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
            err=util.upload(f,fs,channel,access)
            if err:
                return err
        return "success!",200
    else:
        return "not authorized",401
    
@server.route("/download",methods=["GET"])
def download():
    pass


if __name__ == "__main__":
    server.run(host="0.0.0.0",port=8080)