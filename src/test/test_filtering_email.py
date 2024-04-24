import base64
from src.api.gmail.service import GmailService
from src.api.gemini.agents import Product, GeminiCustomerFeedbackAgent
from rich import print, print_json
from src.api.gemini.prompts import filter_spam_prompt
import time
from src.backend.business import BusinessAgent

def main():
    start = time.perf_counter()

    #agent = BusinessAgent(
    #    business_name = 'The Coffee House',
    #    products = ['Black Coffee', 'White Coffee']
    #)

    filter_agent = GeminiCustomerFeedbackAgent(
        business_name='The Coffee House',
        background='You are a professional at filtering messages',
        products=['Black Coffee', 'White Coffee']
    )

    gmail = GmailService(business_name = 'The Coffee House')
    messages = gmail.get_all_messages()

    i = 0
    for message in messages:
        messages[i]['body'] = message['body'][:200:]
        i += 1


    print(messages)
    promt = filter_spam_prompt(['Black Coffee', 'White Coffee'], 'The Coffee House', messages)
    print(promt)
    end = time.perf_counter()

    print(f'Finished in {end - start} seconds.')


    print('Lenght',len(messages))
    filtered_messages = filter_agent.filter_messages(messages)
    print(filtered_messages)

    #res = agent.get_reports(filtered_messages)

    end = time.perf_counter()

    #print(res)
    print(f'Finished in {end - start} seconds.')


if __name__ == "__main__":
    main()
