import time
from rich import print, print_json
from src.api.gmail.service import GmailService
from src.api.gemini.agents import GeminiCustomerFeedbackAgent
from src.backend.business import BusinessAgent
from src.api.types import Product
'''
Test flow: all messages -> filter messages -> get report -> print report
'''
def main(business_name,products):
    agent = BusinessAgent(
        business_name=business_name,
        products=products
    )

    report = agent.get_reports()
    print(report)


if __name__ == "__main__":
    start = time.perf_counter()

    business_name = 'The Coffee House',
    products = [Product(1000,'Black Coffee', 'A coffee that is black'),
                Product(10000, 'White Coffee', 'A coffee that is white')]
    main(business_name,products)

    end = time.perf_counter()
    print(f'Finished in {end - start} seconds.')