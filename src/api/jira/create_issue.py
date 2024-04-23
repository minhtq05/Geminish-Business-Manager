# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from src.api.config import JIRA_USER_EMAIL, JIRA_USER_PASSWORD, JIRA_PRJ_URL
from requests.auth import HTTPBasicAuth
import json
from sample import tickets


def create_issue(payload, headers, auth):
  response = requests.request(
     "POST",
     url,
     data=payload,
     headers=headers,
     auth=auth
  )
  return response

if __name__ == "__main__":
    url = JIRA_PRJ_URL

    auth = HTTPBasicAuth(JIRA_USER_EMAIL, JIRA_USER_PASSWORD)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps(tickets)

print(json.dumps(json.loads(create_issue(payload, headers, auth).text), sort_keys=True, indent=4, separators=(",", ": ")))