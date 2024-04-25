import time
from requests.auth import HTTPBasicAuth
from src.backend.business import BusinessAgent
from src.api.jira.agent_jira import Jira
from src.api.types import JiraTicket
from src.api.config import JIRA_USER_EMAIL, JIRA_USER_PASSWORD, JIRA_PRJ_URL
import json
'''
Test flow: all messages -> filter messages -> get report 
-> improvements option -> upload all option to Jira

Refer to this video to learn how to use the Jira for testing: 
https://youtu.be/oPbr8eLC4dE?si=hQKplOxCQX3N-ao4
'''
def main(url, auth, headers, key, business_name, products):
    agent = BusinessAgent(
        business_name=business_name,
        products=products
    )
    options = agent.get_improvements_options()
    for product in options:
        for option in options[product]:
            ticket = JiraTicket('ARP', option[0], option[1])
            print(ticket)
            jira = Jira(ticket, url, auth, headers)
            res = jira.upload_issue()
            print(json.dumps(json.loads(res.text), sort_keys=True, indent=4, separators=(",", ": ")))


if __name__ == "__main__":
    start = time.perf_counter()

    url = JIRA_PRJ_URL
    auth = HTTPBasicAuth(JIRA_USER_EMAIL, JIRA_USER_PASSWORD)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    key = 'ARP'
    business_name = 'The Coffee House',
    products = ['Black Coffee', 'White Coffee']
    main(url, auth, headers, key, business_name, products)

    end = time.perf_counter()
    print(f'Finished in {end - start} seconds.')