from src.api.config import GEMINI_API_KEY
import google.generativeai as genai
from src.api.types import Message, Product
from rich import print, print_json
from typing import List
import time
import random


from .feedback_report import feedback_report_prompt
from .response_generate import response_generate_prompt
from .sample_feedback_emails import sample_feedback_emails_prompt
from .filter_spam import filter_spam_prompt


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
        prompt = sample_feedback_emails_prompt(self.products, self.company, 5)

        return self.execute('generator', prompt)
    
    def filter_messages(self, messages: List[Message]) -> List[Message]:
        """
        Filter spam and unrelated messages from a list of messages
        """
        prompt = filter_spam_prompt(self.products, self.company)
        filter = self.execute('analyzer', prompt)

        messages = [m for i, m in enumerate(messages) if filter[i]]

        return messages

        
        
        
