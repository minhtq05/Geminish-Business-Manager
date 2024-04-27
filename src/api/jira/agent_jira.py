# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import time
from typing import List
from src.api.config import JIRA_USER_GMAIL, JIRA_USER_PASSWORD, JIRA_PRJ_URL
from requests.auth import HTTPBasicAuth
from src.api.jira.sample import ticket1
from src.api.types import JiraTicket
import json

'''
Refer to this video to learn how to use the Jira for testing: 
https://youtu.be/oPbr8eLC4dE?si=hQKplOxCQX3N-ao4
'''
class Jira():
    def __init__(self,
                 url: str = JIRA_PRJ_URL,
                 auth: str = HTTPBasicAuth(JIRA_USER_GMAIL, JIRA_USER_PASSWORD),
                 headers: str = {"Accept": "application/json","Content-Type": "application/json"}
                 ):
        self.url = url
        self.headers = headers
        self.auth = auth
    def upload_issue(self, payload = None):
      response = requests.request(
         "POST",
         url = self.url,
         data = json.dumps(payload),
         headers= self.headers,
         auth = self.auth
      )
      return response
    def option_to_jira(self,key: str, product: str, option_list: List) -> List:
        ticket_list = []
        for i in range(len(option_list) - 1):
            summary = option_list[i]
            description = option_list[i + 1]
            ticket_list.append(JiraTicket(key, product, summary, description))
        return ticket_list
    def add_custom_jira_ticket(self,key: str, product: str, summary: str, description: str):
        return JiraTicket(key, product, summary, description)

if __name__ == "__main__":
    start = time.perf_counter()

    payload = ticket1

    jira = Jira(payload)
    res = jira.upload_issue(payload)
    print(json.dumps(json.loads(res.text), sort_keys=True, indent=4, separators=(",", ": ")))

    end = time.perf_counter()
    print(f'Finished in {end - start} seconds.')