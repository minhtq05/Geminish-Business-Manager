import base64
from api.gmail.service import GmailService
from api.gemini.agents import Product, GeminiCustomerFeedbackAgent
from rich import print, print_json
import time


def main():
    gm_service = GmailService()

    messages = gm_service.get_messages_list()

    background = '''
You have outstanding knowledge in understanding customers and product feedback.
    '''
    products = [
        Product(id=1234, name='Black Coffee',
                description='This is the blackest coffee we have'),
        Product(id=5678, name='White Coffee',
                description='This is the whiest coffee we have'),
    ]

    feedback_agent = GeminiCustomerFeedbackAgent(
        background=background,
        products=products
    )

    start = time.perf_counter()

    res = feedback_agent.get_feedback_report(messages)

    end = time.perf_counter()

    print(res)
    print(f'Finished in {end - start} seconds.')


if __name__ == "__main__":
    main()
