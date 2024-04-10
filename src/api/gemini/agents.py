from api.gemini.config import GEMINI_API_KEY
import google.generativeai as genai
from typing import List
import time
from rich import print, print_json
import random


def Product(id: int, name: str, description: str):
    return {
        'id': id,
        'name': name,
        'description': description
    }


class GeminiCustomerFeedbackAgent():
    '''
    A wrapper for Google Gemini Pro LLM, using Gemini API to communicate with model.
    This wrapper is customized as a business agent, helping businesses in managing their products.
    '''

    def __init__(self, role: str = "Customer Feedback Manager", background: str = 'You have outstanding knowledge in understanding customers and product feedback.', company: str = 'Random Company', products: List = None, api: str = GEMINI_API_KEY, llm='gemini-1.0-pro-latest', language='English'):
        self.role = role
        self.background = background
        self.company = company
        self.products = products
        self.language = language
        genai.configure(api_key=api)
        self.analyze_config = genai.GenerationConfig(
            temperature=0.0,
            top_p=0.5,
            top_k=20,
        )
        self.generate_config = genai.GenerationConfig(
            temperature=0.4,
            top_p=0.9,
            top_k=20,
        )
        self.llm_analizer = genai.GenerativeModel(
            llm, generation_config=self.analyze_config)
        self.llm_generator = genai.GenerativeModel(
            llm, generation_config=self.generate_config)
        print('Gemini APIs initiated successfully.')

    def execute(self, llm_type: str = 'analyzer', tasks: str = 'Nothing', role: str = None, background: str = None):
        prompt = ''

        if role is None:
            role = self.role

        if background is None:
            background = self.background

        prompt += f'''
You are a talented {role}
            '''

        prompt += f'''
Your background is:
                {background}
            '''

        prompt += f'''
Your task is to:
            {tasks}
        '''

        # print("Prompt:", prompt)
        if llm_type is None:
            return 'No role was provided.'
        elif llm_type == 'analyzer':
            res = self.llm_analizer.generate_content(prompt)
        elif llm_type == 'generator':
            res = self.llm_generator.generate_content(prompt)
        else:
            return 'Unknown role.'

        return str(res.text)

    def get_feedback_report(self, messages: List[dict] = None):
        def messages_format(messages: List[dict]):
            return '\n'.join([f'Sender: {msg.get("sender", {}).get('email', "Anonymous")}\n{msg.get("body", "")}' for msg in messages if msg.get("body", "") != ""])

        if messages is not None:
            prompt = '''
Analyse users' feedback emails and generate reports based on the products each user mentioned from the below list of products with their description.
The reports should be formated in JSON.
Each report should have the following attributes: sender - the email address of the sender, products - a list of objects representing products that the user mentioned. For each object inside the products is a dictionary with 4 attributes: the ID of the product, the name of the product, the status of the feedback for this product (mostly positive, somewhat positive, neutral, somewhat negative, and mostly negative), and the short summary of the feedback about this product written in third person.
If the message is not related to any of the products and their description, it should have an empty products list.
Here is a sample report:
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
{self.products}
And here are the users' feedback:
{messages_format(messages)}
'''
            return self.execute('analyzer', prompt)
        else:
            return 'error: No messages were given.'

    def generate_responses(self, messages: List[dict] = None):
        def messages_format(messages: List[dict]):
            return '\n'.join([f'Sender: {msg.get("sender", {}).get('name', " Our Precious Customer")}\n{msg.get("body", "")}' for msg in messages if msg.get("body", "") != ""])
        if messages is not None:
            prompt = '''
Generate responses to the users' feedback emails based on the products each user mentioned from the below list of products with their description.
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
{self.products}
And here are the users' feedback:
{messages_format(messages)}
'''

            return self.execute('generator', prompt)
        else:
            return 'error: No messages were given.'

    def generate_sample_feedbacks(self, num_feedbacks: int = 5):
        prompt = f'''
Generate {num_feedbacks} sample feedback emails from the below list of products with their descriptions from company named '{self.company}'.
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
}
''' + f'''
Here are the products:
{self.products}
'''
        return self.execute('generator', prompt)
