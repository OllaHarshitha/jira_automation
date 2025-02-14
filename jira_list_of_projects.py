import requests
from requests.auth import HTTPBasicAuth
import json

# API Endpoint
url = "https://mail-team-iznn07u5.atlassian.net/rest/api/3/project"

# Authentication
auth = HTTPBasicAuth("holla@mail.bradley.edu", "ATATT3xFfGF0t8XOtq42WWutM2tKc9wcFo91aObUQN-4-CGdIIKaRJm5_cc7_Y9S6pYr9wbnUa3Pt4oVJhT04NWOANNdjXBdCCJsU-cQODo-osXPeaeUB1TN0XLI_oggdUM2mBGjDNFCFJrD9Q0H2GwoVMkgnCNI3KS_mJeZf10sX33JvaIGCDc=0D1A2108")

# Headers
headers = {"Accept": "application/json"}

# API Request
response = requests.get(url, headers=headers, auth=auth)

# Print Status Code
print("Status Code:", response.status_code)

# Print Raw Response Text
print("Raw Response:", response.text)  # This will help us debug

# Try Parsing JSON
try:
    response_json = response.json()
    print(json.dumps(response_json, indent=4, separators=(",", ": ")))
except json.JSONDecodeError:
    print("Error: Response is not in JSON format.")

output=json.loads(response.text)
name=output[0]["name"]
print(name)