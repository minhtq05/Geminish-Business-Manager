import time
from requests.auth import HTTPBasicAuth
from src.backend.business import BusinessAgent
from src.api.jira.agent_jira import Jira
from src.api.config import JIRA_USER_GMAIL, JIRA_USER_PASSWORD, JIRA_PRJ_URL
import json
'''
Test flow: all messages -> filter messages -> get report 
-> improvements option -> upload all option to Jira

Refer to this video to learn how to use the Jira for testing: 
https://youtu.be/oPbr8eLC4dE?si=hQKplOxCQX3N-ao4
'''
def main(business_name, products, key):
    agent = BusinessAgent(
        business_name=business_name,
        products=products
    )
    agent.upload_issue(key)


if __name__ == "__main__":
    start = time.perf_counter()
    key = 'ARP'
    business_name = 'The Coffee House',
    products = ['Black Coffee', 'White Coffee']

    main(business_name, products, key)

    end = time.perf_counter()
    print(f'Finished in {end - start} seconds.')