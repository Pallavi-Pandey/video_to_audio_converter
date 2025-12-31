import os,requests

def token(request):
    if not "Authorization" in request.headers:
        return None,("Missing credentials",401)
    token_value=request.headers["Authorization"]
    if not token_value:
        return None,("Missing credentials",401)
    response=requests.post(f"http://{os.getenv('AUTH_SVC_ADDRESS')}/validate",headers={"Authorization":token_value})

    if response.status_code ==200:
        return response.text,None
    else:
        return None,(response.text,response.status_code)