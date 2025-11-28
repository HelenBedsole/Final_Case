import json
import requests

WEBHOOK_URL = "http://localhost:5678/webhook-test/start"

payload = {
    "message": "Schedule a Google Developers Group meeting for 4pm tomorrow in Shannon Library"
}

print("Sending test request to workflow...")
response = requests.post(WEBHOOK_URL, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", json.dumps(response.json(), indent=2))

