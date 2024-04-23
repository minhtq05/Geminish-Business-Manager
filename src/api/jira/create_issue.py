# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
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
    url = "https://geminish-business-manager.atlassian.net/rest/api/2/issue"

    auth = HTTPBasicAuth("geminishbm@gmail.com", "ATATT3xFfGF0mq9KHefJcCvFNvuHkt8nrw_L1Dnc3Gq34nlcXByE0wArtfpNbVfBcB22ZF1sxSd7KCTnTDtXHx1qvlhGetP6V3GMtTBPzWdLYud56fGd3HGg2CabE9g1B2jxJvdOI5SR1WRr4FFYFYqAnN85tndMaE7byfbHVlbivg7QwlRCowM=F36FEB38")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps(tickets)

print(json.dumps(json.loads(create_issue(payload, headers, auth).text), sort_keys=True, indent=4, separators=(",", ": ")))