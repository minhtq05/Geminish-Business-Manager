from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.exceptions import HTTPException
from firebase_admin import auth
from fastapi.middleware.cors import CORSMiddleware

from src.backend.business import BusinessAgent
from src.api.types import Product
# from src.api.config import FIREBASE_API_KEY, FIREBASE_PROJECT_ID

from typing import List, Dict, Optional
from datetime import datetime, timedelta
from rich import print
from functools import wraps


import uvicorn
import pyrebase
import json
import asyncio
import re

"""



A message should have the following format:
{
    "authorization": "token, the jwt string token of your account",
    {"the rest of the content"}
}



"""

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
origins = [
    "http://localhost:5173",  # Replace with the origin of your frontend application
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)
businesses = []
pb = pyrebase.initialize_app(firebaseConfig)



products = [
    Product(id=1234, name='Black Coffee',
            description='This is the blackest coffee we have'),
    Product(id=5678, name='White Coffee',
            description='This is the whiest coffee we have'),
]

gemini_bm = BusinessAgent("Geminish BM", products=products)


def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        headers = kwargs['request'].headers
        if headers is None:
            return {
                "message": "Error! No header given!"
            }

        jwt = headers.get('authorization', None)
        if jwt is None:
            return {
                "message": "Login required!"
            }
        user = auth.verify_id_token(jwt)
        if user.get('uid', None) is None:
            return {
                "message": "Login required!"
            }
        return await func(*args, **kwargs)
    return wrapper




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



@app.get("/feedbacks")
# @login_required
def feedbacks(request: Request):
    return {
        "messages": gemini_bm.raw_messages,
    }


@app.get("/reports")
# @login_required
def reports():
    return {
        "reports": gemini_bm.reports,
    }


@app.get("/reports/summarize")
# @login_required
async def reports_summarize():
    messages = gemini_bm.get_raw_messages()
    response = gemini_bm.get_reports_summarize(messages)
    return {
        "reports": response
    }


@app.get("/testanalyzer")
async def testanalyzer():
    return StreamingResponse(gemini_bm._gemini_agent.test_model_analyzer(), media_type='text/event-stream')