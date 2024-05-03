from src.api.types import Message, Product
from typing import List
from src.api.gemini.formats import messages_format, sample_messages_format, products_format
import json


def feedback_report_prompt(ref_products: List[Product], messages: List[Message]) -> str:
    return '''Analyze feedback messages, read a list of products, generate a list of reports for each message, and identify the products appeared on those messages.
The reports must strictly be in JSON schema. You must strictly keep the order of the messages.
Here is the format of the list of reports:
[
    List of reports.
    {
        "sender": string - The email address of the sender,
        "products": list of dictionaries - [
            List of products appeared on this message.
            {
                "id": int - The ID of the product,
                "name": string - The name of the product,
                "status": string - The status of the feedback for this product ("mostly positive", "somewhat positive", "neutral", "somewhat negative", or "mostly negative"),
                "summary": list of strings - [
                    List of feedback sentences about this product written by the user.
                ]
            }
        ]
    }
]''' + f'''
Here is a list of products:
{products_format(ref_products)}
Here is the list of messages:
{messages_format(messages)}
'''


def filter_spam_prompt(ref_products: List[Product], ref_business_name: str, messages: List[Message]) -> str:
    return f'''Read a list of feedback messages, return a list of boolean values (True or False): True if a message is a legit feedback or False if it is unrelated to a list of products.
Your response must strictly be a list of exactly {len(messages)} boolean values separated by commas with no leading spaces.
Here is a valid response example when there are 5 messages:
False,True,False,True,True
Here is the list of messages:
{messages_format(messages)}
The company name is "{ref_business_name}"
Here is the list of products:
{products_format(ref_products)}
'''


def sample_feedback_emails_prompt(ref_products: List[Product], ref_business_name: str = None, num_feedbacks: int = 5) -> str:
    return f'''Generate {num_feedbacks} sample feedback emails mentioning random products from a list of products of a company names "{ref_business_name}".
Each message must have:
- Different ideas, feedback, tone, context, style, and reasons
- Random number of products from the list
- Random status (mostly positive, somewhat positive, neutral, somewhat negative, and mostly negative) for each product
- Random length (ranging from 100 words to 500 words)
Your response must strictly be in JSON schema.
Here is the format of the list of messages:''' + '''
[
    List of sample feedback messages
    {
        "sender": string - The email address of the sender,
        "subject": string - The subject of the message,
        "body": string - The body of the message
    }
]''' + f'''
Here is the list of products:
{products_format(ref_products)}
'''


def response_generate_prompt(ref_products: List[Product], messages: List[Message]) -> str:
    return '''Generate responses to the users' feedback emails based on the products each user mentioned from the below list of products with their description.
Use friendly tone and be as concise as possible.
Each response should be formatted in JSON and has 3 attributes: receiver - the sender of the feedback we received earlier, subject - the subject of the response, and body - the body of the feedback.
Here is a sample response:
{
    "responses": [
        {
            "receiver": "emailofthesender1@gmail.com",
            "subject": "Thank you for your feedback",
            "body": "Dear Our Precious Customer,\n\nThank you for your feedback about the black and white coffee of your shop. We appreciate your support and look forward to continuing our relationship with you.\nBest regards,\nThe Coffee House"
        }
    ]
}
Here is a list of products:
''' + f'''
{ref_products}
And here are the users' feedback:
{sample_messages_format(messages)}'''


def improvements_option(ref_products: List[Product], ref_company_name: str = None,  report: dict = None) -> str:
    return f'''Generate a list of suggestions for a list of products for company {ref_company_name} based on a feedback report.
The output must strictly be in JSON schema:''' + '''
{
    List all of the products here.
    For example:
    "name of product": "list, a [] list of improvements separated by commas. Each improvement is a list of two strings: ["summary, string, the summary of the improvement", "description, string, the description of the improvement"].
}''' + f'''
Here is a list of products:
{ref_products}
Here is the feedback report:
{report}
'''
