# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import time
from src.api.config import JIRA_USER_EMAIL, JIRA_USER_PASSWORD, JIRA_PRJ_URL
from requests.auth import HTTPBasicAuth
from src.api.jira.sample import tickets
import json

'''
Refer to this video to learn how to use the Jira for testing: 
https://youtu.be/oPbr8eLC4dE?si=hQKplOxCQX3N-ao4
'''
class Jira():
    def __init__(self, payload, url, auth, headers):
        self.payload = json.dumps(payload)
        self.url = url
        self.headers = headers
        self.auth = auth
    def upload_issue(self):
      response = requests.request(
         "POST",
         url = self.url,
         data = self.payload,
         headers= self.headers,
         auth = self.auth
      )
      return response

if __name__ == "__main__":
    start = time.perf_counter()

    url = JIRA_PRJ_URL
    auth = HTTPBasicAuth(JIRA_USER_EMAIL, JIRA_USER_PASSWORD)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = json.dumps(tickets)

    jira = Jira(payload, url, headers, auth)
    res = jira.upload_issue()
    print(json.dumps(json.loads(res.text), sort_keys=True, indent=4, separators=(",", ": ")))

    end = time.perf_counter()
    print(f'Finished in {end - start} seconds.')