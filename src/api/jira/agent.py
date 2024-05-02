# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import time
from typing import List
from requests import Response

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
                 headers=None
                 ):
        if headers is None:
            headers = {"Accept": "application/json", "Content-Type": "application/json"}
        self.url = url
        self.headers = headers
        self.auth = auth

    def upload_issue(self, payload=None) -> Response:
        """
        Upload Jira ticket to Jira as a Task
        payload: a single Jira Ticket object
        return Response
        """
        response = requests.request(
            "POST",
            url=self.url,
            data=json.dumps(payload),
            headers=self.headers,
            auth=self.auth
        )
        return response

    def option_to_jira(self, key: str, product: str, option_list: List) -> List:
        """
        :param key: the project key
        :param product: list of company products
        :param option_list: list of improvement option for each product
               each option has a summary and description: [summary, description]
        :return:
        """
        ticket_list = []
        if option_list is None or option_list == {}:
            return ticket_list

        for i in range(len(option_list)):
            option = option_list[i]
            summary = option[0]
            description = option[1]
            ticket_list.append(JiraTicket(key, product, summary, description))
        return ticket_list



if __name__ == "__main__":
    start = time.perf_counter()

    payload = ticket1

    jira = Jira(payload)
    res = jira.upload_issue(payload)
    print(json.dumps(json.loads(res.text), sort_keys=True, indent=4, separators=(",", ": ")))

    end = time.perf_counter()
    print(f'Finished in {end - start} seconds.')
