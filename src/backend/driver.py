from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from firebase_admin import auth

from src.backend.business import BusinessAgent
# from src.api.config import FIREBASE_API_KEY, FIREBASE_PROJECT_ID

from typing import List, Dict, Optional
from datetime import datetime, timedelta
from rich import print
from pydantic import BaseModel

import uvicorn
import pyrebase
import json

firebaseConfig = {
    "apiKey": "AIzaSyC2mBWE2hEvW4A-ApWssxQofkvNplGSPWA",
    "authDomain": "geminish-business-manage-cd958.firebaseapp.com",
    "projectId": "geminish-business-manage-cd958",
    "storageBucket": "geminish-business-manage-cd958.appspot.com",
    "messagingSenderId": "877330635552",
    "appId": "1:877330635552:web:374ccdf3783e02ded11545",
    "measurementId": "G-CJJXJ0NWF8",
    "databaseURL": ""
}


app = FastAPI()
businesses = []
pb = pyrebase.initialize_app(firebaseConfig)


class Business(BaseModel):
    id: int
    business_name: str
    created_on: datetime

# Index enpoint
@app.get("/")
def index():
    return {"message": "Hello World"}


# Signup endpoint
@app.post('/signup', include_in_schema=False)
async def signup(request: Request): 
    req = await request.json()
    email = req['email']
    password = req['password']
    if email is None or password is None:
        return HTTPException(detail={'message': 'Missing Email or Password'}, status_code=400)
    
    try:
        user = auth.create_user(email=email, password=password)
    except Exception as e:
        return HTTPException(detail={'message': 'Error creating user: ' + str(e)}, status_code=400)    


# Login endpoint
@app.post('/login', include_in_schema=False)
async def login(request: Request):
    req_json = await request.json()
    email = req_json['email']
    password = req_json['password']

    try:
        user = pb.auth().sign_in_with_email_and_password(email, password)
        jwt = user['idToken']
        return JSONResponse(content={"token": jwt}, status_code=200)
    except Exception as e:
        return HTTPException(detail={'message': 'There was an error logging in: ' + str(e)}, status_code=400)
    

# ping endpoint
@app.post("/ping", include_in_schema=False)
async def ping(request: Request):
    headers = request.headers
    jwt = headers.get('authorization')
    print(f"JWT: {jwt}")
    user = auth.verify_id_token(jwt)
    return user["uid"]


@app.post("/ping", include_in_schema=False)
async def validate(request: Request):
    headers = request.headers



@app.get("/users")
async def index():
    return {
        "users": auth.list_users()
    }



def create_driver():
    uvicorn.run("src.backend.driver:app", host="0.0.0.0", port=5000, reload=True)


if __name__ == "__main__":
    uvicorn.run("driver:app", host="0.0.0.0", port=5000, reload=True)