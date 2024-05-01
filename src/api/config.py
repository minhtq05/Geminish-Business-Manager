from dotenv import load_dotenv
import os

load_dotenv() # take environment variables from .env. The environmental variables became available in the current system


# os.getenv(key, default = None) returns value of environmental variable key as a string
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY') 
FIREBASE_API_CREDENTIAL = os.getenv('FIREBASE_API_CREDENTIAL')
FIREBASE_API_KEY = os.getenv('FIREBASE_API_KEY')
FIREBASE_PROJECT_ID = os.getenv('FIREBASE_PROJECT_ID')
GMAIL_API_CREDENTIAL = os.getenv('GMAIL_API_CREDENTIAL')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_API_KEY_BACKUP = os.getenv('GEMINI_API_KEY_BACKUP')
JIRA_USER_GMAIL = os.getenv('JIRA_USER_GMAIL')
JIRA_USER_PASSWORD = os.getenv('JIRA_USER_PASSWORD')
JIRA_PRJ_URL = os.getenv('JIRA_PRJ_URL')
