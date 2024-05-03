import time
from src.backend.business import BusinessAgent
from src.api.types import Product
'''
Test flow: all messages -> filter messages -> get report 
-> improvement option -> print improvement options
'''
def main(business_name,products):
    agent = BusinessAgent(
        business_name=business_name,
        products=products
    )
    options = agent.get_improvements_options()
    return options

if __name__ == "__main__":
    start = time.perf_counter()

    business_name = 'The Coffee House',
    products = [Product(1000,'Black Coffee', 'A coffee that is black'),
                Product(10000, 'White Coffee', 'A coffee that is white')]
    options = main(business_name,products)
    print(options)
    end = time.perf_counter()
    print(f'Finished in {end - start} seconds.')