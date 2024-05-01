from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.exceptions import HTTPException
from firebase_admin import auth

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
This is the main driver of your backend server, which means that driver.py will be the only code file that you will need to run in order to initalize all the database, api services, and servers.

It is an all-in-one system that will be used to deploy your backend server.

The main structure of the driver is as follows:
    - app: our FastAPI application for routing and request handling
    - businesses: a list of all the businesses running in the system. However, at the moment, it will only run a single business, which is our demo business "Geminish Business Manager" or "Geminish BM".
    - the BusinessAgent class is the main wrapper of all the databases and services needed for a business. You only need to call it with 2 parameters: business_name: str and products: a list of products the business has. 
    - Our server has 4 routes:
        * /index: the index route, which will be used to test if the server is up and running
        * /feedbacks: the route for getting all the feedbacks from the customers
        * /reports: the route for getting all the reports after analyzing the feedbacks
        * /reports/summarize: the route for summarizing the reports into a total summary of all feedbacks

        
Other than that, you don't have to worry about anything else.

"""


app = FastAPI()  # our main FastAPI application
businesses = []  # a list of all the businesses
# firebaseConfig = {} # Replace with real firebase config later
# pb = pyrebase.initialize_app(firebaseConfig)


allow_all = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_all,
    allow_credentials=True,
    allow_methods=allow_all,
    allow_headers=allow_all
)


products = [
    Product(id=1234, name='Black Coffee',
            description='This is the blackest coffee we have'),
    Product(id=5678, name='White Coffee',
            description='This is the whiest coffee we have'),
]  # a list of all the products

# initializing the business
gemini_bm = BusinessAgent("Geminish BM", products=products)


# def login_required(func):
#     @wraps(func)
#     async def wrapper(*args, **kwargs):
#         headers = kwargs['request'].headers
#         if headers is None:
#             return {
#                 "message": "Error! No header given!"
#             }

#         jwt = headers.get('authorization', None)
#         if jwt is None:
#             return {
#                 "message": "Login required!"
#             }
#         user = auth.verify_id_token(jwt)
#         if user.get('uid', None) is None:
#             return {
#                 "message": "Login required!"
#             }
#         return await func(*args, **kwargs)
#     return wrapper


def decorator(func):
    """
    Just a decorator for all the routes while logging them
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        print('-' * 60)
        return func(*args, **kwargs)
    return wrapper


# Index enpoint
@app.get("/")
@decorator
def index():
    """
    This is the index route, which will be used to test if the server is up and running
    This route will later return more information but it will do nothing for now.
    """
    return {"message": "Hello World"}


# # Signup endpoint
# @app.post('/signup', include_in_schema=False)
# @decorator
# async def signup(request: Request):
#     req = await request.json()
#     email = req['email']
#     password = req['password']
#     if email is None or password is None:
#         return HTTPException(detail={'message': 'Missing Email or Password'}, status_code=400)

#     try:
#         user = auth.create_user(email=email, password=password)
#     except Exception as e:
#         return HTTPException(detail={'message': 'Error creating user: ' + str(e)}, status_code=400)


# # Login endpoint
# @app.post('/login', include_in_schema=False)
# @decorator
# async def login(request: Request):
#     req_json = await request.json()
#     email = req_json['email']
#     password = req_json['password']

#     try:
#         user = pb.auth().sign_in_with_email_and_password(email, password)
#         jwt = user['idToken']
#         return JSONResponse(content={"token": jwt}, status_code=200)
#     except Exception as e:
#         return HTTPException(detail={'message': 'There was an error logging in: ' + str(e)}, status_code=400)


# # ping endpoint
# @app.post("/ping", include_in_schema=False)
# @decorator
# async def ping(request: Request):
#     headers = request.headers
#     jwt = headers.get('authorization')
#     print(f"JWT: {jwt}")
#     user = auth.verify_id_token(jwt)
#     return user["uid"]


@app.get("/feedbacks")
@decorator
# @login_required
def feedbacks():
    """
    This is the route to get all the feedbacks
    This route will only return the feedbacks of the "Geminish BM" business for now
    """
    output = gemini_bm.get_raw_messages()
    return output


@app.get("/reports")
@decorator
# @login_required
def reports():
    """
    This is the route to get all the reports
    This route will only return the reports of the "Geminish BM" business for now
    """
    return gemini_bm.get_reports()


@app.get("/jira")
async def push_issues_to_web(project_key):
    """
        This is the route to get all the jira ticket
        This route will only return the jira ticket from the report for now
    """
    return {
        "tickets": gemini_bm.get_all_issue(project_key)
    }


@app.post("/jira/upload")
async def push_issues_to_jira(request: Request):
    data = await request.json()
    output = gemini_bm.upload_issue(data)
    return output


# @app.get("/reports/summarize")
# @decorator
# # @login_required
# def reports_summarize():
#     messages = gemini_bm.get_raw_messages()
#     response = gemini_bm.get_reports_summarize(messages)
#     return {
#         response
#     }


# @app.get("/testanalyzer")
# @decorator
# async def testanalyzer():
#     return StreamingResponse(gemini_bm._gemini_agent.test_model_analyzer(), media_type='text/event-stream')
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)