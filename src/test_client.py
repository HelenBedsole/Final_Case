import json
import requests

WEBHOOK_URL = "http://localhost:5678/webhook-test/schedule"

payload = {
    "message": "Move the project meeting to 7 pm tomorrow"
}

print("Sending test request to workflow...")
response = requests.post(WEBHOOK_URL, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", json.dumps(response.json(), indent=2))

