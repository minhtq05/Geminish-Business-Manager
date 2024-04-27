from dotenv import load_dotenv
import os

load_dotenv()
FIREBASE_API_CREDENTIAL = os.getenv('FIREBASE_API_CREDENTIAL')
GMAIL_API_CREDENTIAL = os.getenv('GMAIL_API_CREDENTIAL')
GEMINI_API_CREDENTIAL = os.getenv('GEMINI_API_CREDENTIAL')