from api.gemini.config import GEMINI_API_KEY
import google.generativeai as genai
from typing import List
import time
from rich import print, print_json
import random


def Product(id, name, description):
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

    def __init__(self, role: str = "Customer Feedback Manager", background: str = None, products: List = None, api: str = GEMINI_API_KEY, llm='gemini-1.0-pro-latest', language='English'):
        self.role = role
        self.background = background
        self.products = products
        self.language = language
        genai.configure(api_key=api)
        self.generation_config = genai.GenerationConfig(
            temperature=0.01,
            top_p=0.5,
            top_k=20,
        )
        self.llm = genai.GenerativeModel(
            llm, generation_config=self.generation_config)
        print('Google API initiated successfully.')

    def execute(self, tasks: str):
        prompt = ''

        if self.role is not None:
            prompt += f'''
You are a talented {self.role}
            '''

        if self.background is not None:
            prompt += f'''
Your background is:
                {self.background}
            '''

        prompt += f'''
Your task is to:
            {tasks}
        '''

        # print("Prompt:", prompt)
        res = self.llm.generate_content(prompt)

        return str(res.text)

    def get_feedback_report(self, messages: List[dict] = None):
        def messages_format(messages: List[dict]):
            return '\n'.join([f'Sender: {msg.get("sender", "Anonymous").get('email', "Anonymous")}\n{msg.get("body", "")}' for msg in messages if msg.get("body", "") != ""])

        if messages is not None:
            prompt = '''
Read users' feedback emails and generate reports based on the products each user mentioned from the below list of products with their description.
The reports should be formated in JSON.
Each report should have the following attributes: sender - the email address of the sender, products - a list of objects representing products that the user mentioned. For each object inside the products is a dictionary with 4 attributes: the ID of the product, the name of the product, the status of the feedback for this product (mostly positive, somewhat positive, neutral, somewhat negative, and mostly negative), and the short summary of the feedback about this product written in third person.
Here is a sample report:
{
    "reports": [
        {
            "sender": "emailofthesender1@gmail.com",
            "products": [
                {
                    "id": 1234,
                    "name": "Product 1",
                    "status": "positive",
                    "summary": "Product is great!"
                },
                {
                    "id": 5678,
                    "name": "Product 2",
                    "status": "negative",
                    "summary": "Have a lot of bugs. The color is too bright and has no dark mode"
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
                    "status": "negative",
                    "summary": "Doesn't seem working after booted up"
                },
                {
                    "id": 1357,
                    "name": "Product 7",
                    "status": "neutral",
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
            print("Prompt has", self.llm.count_tokens(prompt))
            return self.execute(prompt)
        else:
            return 'error: No text was given'
