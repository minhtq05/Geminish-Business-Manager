from src.api.config import GEMINI_API_KEY
import google.generativeai as genai
from src.api.types import Message, Product
# from rich import print, print_json
from typing import List
import time
import random
import json
import re


from src.api.gemini.prompts import feedback_report_prompt, response_generate_prompt, sample_feedback_emails_prompt, filter_spam_prompt


_safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]


class GeminiCustomerFeedbackAgent():
    '''
    A wrapper for Google Gemini Pro LLM, using Gemini API to communicate with model.
    This wrapper is customized as a business agent, helping businesses in managing their products.
    '''

    def __init__(self, role: str = "Customer Feedback Manager",
                 background: str = 'You have outstanding knowledge in understanding customers and product feedback.',
                 business_name: str = 'Random Business',
                 products: List = None,
                 api: str = GEMINI_API_KEY,
                 llm: str = 'gemini-1.5-pro-latest',
                 language: str = 'English'):
        self.role = role
        self.background = background
        self.business_name = business_name
        self.products = products
        self.language = language
        genai.configure(api_key=api)
        self.analyze_config = genai.GenerationConfig(
            temperature=0.1,
            top_p=0.5,
            top_k=20,
        )
        self.generate_config = genai.GenerationConfig(
            temperature=0.7,
            top_p=0.9,
            top_k=20,
        )
        self.llm_analizer = genai.GenerativeModel(
            llm, generation_config=self.analyze_config)
        self.llm_generator = genai.GenerativeModel(
            llm, generation_config=self.generate_config)
        
        print('Gemini APIs initiated successfully.')


    # def initialize_required(func):
    #     def wrapper(self, *args, **kwargs):
    #         if not self.is_initialized:
    #             raise ValueError("Business is not initialized!")
    #         return func(self, *args, **kwargs)
    #     return wrapper

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
            res = self.llm_analizer.generate_content(prompt, safety_settings=_safety_settings)
            if hasattr(res, 'text'):
                return res.text
                # return json_clean(res.text)
        elif llm_type == 'generator':
            res = self.llm_generator.generate_content(prompt, safety_settings=_safety_settings)
            return res.text
        else:
            return 'Unknown role.'            
        
        return "Something went wrong!"
    

    def get_feedback_report(self, messages: List[Message] = None):
        if messages is not None:
            prompt = feedback_report_prompt(self.products, messages)
            return self.execute('analyzer', prompt)
        else:
            return 'error: No messages were given.'

    def generate_responses(self, messages: List[Message] = None) -> str:
        if messages is not None:
            prompt = response_generate_prompt(self.products, messages)
            return self.execute('generator', prompt)
        else:
            return 'error: No messages were given.'

    def generate_sample_feedback_messages(self, num_feedbacks: int = 5) -> str:
        """
        Generate sample feedback messages and later prompt the users to reply to those messages and learn their styles and tones.
        """
        prompt = sample_feedback_emails_prompt(self.products, self.business_name, 5)

        return self.execute('generator', prompt)
    
    def filter_messages(self, messages: List[Message]) -> List[Message]:
        """
        Filter spam and unrelated messages from a list of messages
        """
        unempty_message = []
        for i, message in enumerate(messages):
            if message.get("body", "") == "":
                continue
            unempty_message.append(message)
        messages = unempty_message
        prompt = filter_spam_prompt(self.products, self.business_name, messages)
        filter = self.execute('analyzer', prompt)
        filter = filter.strip().split(',')
        filter = [True if x == "True" else False for x in filter]
        messages = [m for i, m in enumerate(messages) if filter[i]]
        return messages

    async def test_model_analyzer(self):
        response = await self.llm_analizer.generate_content_async('''
Give me a list of 10 breakfasts that are healthy with JSON schema separated by commas:
{}"name":"string, name of the meal", "description": "string, a short description of the meal", "calories": "int, number of calories in the meal", "serving_size": "float, size of the serving in grams"}
''', safety_settings=_safety_settings, stream=True)
        async for chunk in response:
            yield chunk.text
        
        
        
