from src.api.types import Message, Product
from typing import List
from src.format import sample_messages_format, messages_format

def feedback_report_prompt(ref_products: List[Product], messages: List[Message]) -> str:
    return '''Analyse users' feedback emails and generate reports based on the products each user mentioned from the below list of products with their description.
The reports must be formated in JSON. The report must not have /n or anything like that 
Each report should have the following attributes: sender - the email address of the sender, products - a list of objects representing products that the user mentioned. For each object inside the products is a dictionary with 4 attributes: the ID of the product, the name of the product, the status of the feedback for this product (mostly positive, somewhat positive, neutral, somewhat negative, and mostly negative), and the short summary of the feedback about this product written in third person.
If the message is not related to any of the products and their description, it should have an empty products list.
Here is a sample report, the report must look like this:
{
    "reports": [
        {
            "sender": "emailofthesender1@gmail.com",
            "products": [
                {
                    "id": 1234,
                    "name": "Product 1",
                    "status": "mostly positive",
                    "summary": "Product is great!"
                },
                {
                    "id": 5678,
                    "name": "Product 2",
                    "status": "mostly negative",
                    "summary": "Have a lot of bugs. The color is too bright and has no dark mode."
                },
                {
                    "id": 1357,
                    "name": "Product 3",
                    "status": "neutral",
                    "summary": "The documentation is hard to read. However, still readable and can be improved."
                }
            ]
        },
        {
            "sender": "emailofthesender2@gmail.com",
            "products": [
                {
                    "id": 5678,
                    "name": "Product 3",
                    "status": "somewhatnegative",
                    "summary": "Doesn't seem working after booted up"
                },
                {
                    "id": 1357,
                    "name": "Product 7",
                    "status": "somewhat negative",
                    "summary": "Didn't run after hours of booting up"
                }
            ]
        }
    ]
}
''' + f'''
Here is a list of products:
{ref_products}
And here are the users' feedback:
{messages_format(messages)}
'''


def filter_spam_prompt(ref_products: List[Product], ref_company: str, messages: List[Message]) -> str:
    return f'''True if a message is a legit feedback and False if it is a spam email or an unrelated message.
A feedback body or subject must include company name: {ref_company} and products: {ref_products} 
Strictly be a string of boolean values (True or False) separated by commas with no leading spaces.
Number of boolean values must be equal to {len(messages)}
Here is a response example:

False,True,False,True,True

Here are the messages:
{messages_format(messages)}'''


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