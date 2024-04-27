from src.api.types import Message, Product
from typing import List
from src.api.gemini.formats import messages_format, sample_messages_format, products_format
import json


def feedback_report_prompt(ref_products: List[Product], messages: List[Message]) -> str:
    return '''Analyse users' feedback emails, generate a list of reports for feedback that matches the list of products with descriptions using this JSON schema:
[
    List of the reports for each feedback email with JSON schema as below:
    {
        "sender": "string, email of the sender",
        "products": [
            List of the products that the user mentioned with JSON schema as below:
            {
                "id": "string, id of the product",
                "name": "string, Name of product",
                "status": "string, status of the feedback (mostly positive, somewhat positive, neutral, somewhat negative, and mostly negative)",
                "summary": [
                    List of the exact feedback sentences with format as below:
                    "string, feedback sentence",
                ]
            }
        ]
    }
]
    
If a message doesn't relate to any of the products and descriptions, return an empty products list. ''' + f'''
Here is the list of products:
{products_format(ref_products)}
Here is the list of users' feedback:
{messages_format(messages)}
You must not change the order of the messages
'''


def filter_spam_prompt(ref_products: List[Product], ref_company: str, messages: List[Message]) -> str:
    return f'''Analyze emails, generate a list of booleans (True,False) indicating if each email is a legit feedback or not related to the below list of products including their descriptions.
You must strictly response with a string of boolean values separated by commas with no leading spaces.

Here is the list of products of company '{ref_company}' and their detailed descriptions:
{ref_products}
Here are the messages:

{messages_format(messages)}

End of messages.
I have {len(messages)}, you must response with exactly {len(messages)} boolean values.'''


def sample_feedback_emails_prompt(ref_products: List[Product], ref_company_name: str = None, num_feedbacks: int = 5) -> str:
    return f'''Generate {num_feedbacks} sample feedback emails from the below list of products with their descriptions from company named '{ref_company_name}'.
Each feedback email has to mention a random number of products from the list (don't nessarily mention all of them) with random status (mostly positive, somewhat positive, neutral, somewhat negative, and mostly negative), and random reason for those status. Most importantly, each message has to have idea, feedback, tone, context, style, and reasons.
Your responses need to be a single JSON object and messages body should be formatted as strings. Here are two feedback examples generated for a company A selling products B and C:
''' + '''
{
    "messages": [
        {
            "sender": "emailofthesender1@gmail.com",
            "subject": "Disappointed with [Product B] Performance",
            "body": Dear Company A,\n\nI am writing to express my disappointment with the recent purchase of your [Product B]. I bought it specifically for [reason for purchase], but unfortunately, it has fallen short of my expectations in several ways.\n\nHere are the main issues I've encountered:\n\n[Specific problem 1 with Product B]: This has made it [explain how the problem affects usage].\n\n[Specific problem 2 with Product B]: I was particularly surprised by this, as [explain your expectation based on product description or reviews].\n\nOverall, the performance of [Product B] has been frustrating and hasn't lived up to the claims advertised. While [Product C] (which I also purchased) has been working well, I'm hesitant to recommend Company A based on this experience.\n\nI would appreciate it if you could look into these issues and potentially offer a solution. Perhaps a replacement or a store credit for [Product B] would be a fair resolution.\n\nThank you for your time and attention to this matter.\n\nSincerely,\nRandom User
        },
        {
            "sender": "emailofthesender2@gmail.com",
            "subject": "Delighted with [Product C]!",
            "body": "Dear Company A,\n\nI'm writing to express my sincere satisfaction with your [Product C]. I recently purchased it for [reason for purchase], and it has been an absolute game-changer!\n\nHere's what I particularly love about it:\n\n[Specific positive aspect 1 of Product C]: This has made [explain how the aspect improves your experience].\n\n[Specific positive aspect 2 of Product C]: I wasn't expecting this feature, but it's a delightful surprise and adds a lot of value.\n\nOverall, [Product C] has exceeded my expectations and has become an essential part of [how you use the product]. The quality and functionality are top-notch, and I would highly recommend it to anyone looking for [what the product helps with].\n\nThank you for creating such an impressive product. I look forward to exploring what else Company A has to offer in the future.\n\nSincerely,\nRandom User"
        }
    ]
}''' + f'''
Here are the products:
{ref_products}'''


def response_generate_prompt(ref_products: List[Product], messages: List[Message]) -> str:
    return '''Generate responses to the users' feedback emails based on the products each user mentioned from the below list of products with their description.
Use friendly tone and be as concise as possible.
Each response should be formated in JSON and has 3 attributes: receiver - the sender of the feedback we received earlier, subject - the subject of the response, and body - the body of the feedback.
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





# Each report stricly have 5 attributes: sender: sender's email address, products: list of products user mentioned. Each products is a dictionary with 4 attributes: products' ID, product's name, status of feedback for this product (mostly positive, somewhat positive, neutral, somewhat negative, and mostly negative), and a list of feedback sentences summarized.

#  "sender": "emailofthesender1@gmail.com",
#         "products": [
#             {
#                 "id": "id of the product",
#                 "name": "Name of product 1",
#                 "status": "status of the feedback",
#                 "summary": []
#             },
#             {
#                 "id": "idoftheproduct2",
#                 "name": "Name of product 2",
#                 "status": "status of the feedback",
#                 "summary": [
#                     "feedback sentence 1",
#                     "feedback sentence 2",
#                     "feedback sentence 3",
#                     "feedback sentence 4"
#                 ]
#             },
#         ]
#     }
