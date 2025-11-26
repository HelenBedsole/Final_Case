import requests
import json

WEBHOOK_URL = "http://localhost:5678/webhook-test/start"

def send_request(message: str):
    payload = {"message": message}
    
    print(f"📨 Sending: {message}")
    response = requests.post(WEBHOOK_URL, json=payload)
    
    try:
        data = response.json()
    except ValueError:
        data = response.text

    print("🔽 Response:")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    print("\n=== TEST 1: Create an event ===")
    send_request("Create a study group on Friday at 4 PM for 1 hour at the library.")

    print("\n=== TEST 2: Update an event ===")
    send_request("Move the project meeting to 7 PM tomorrow.")

    print("\n=== TEST 3: Delete an event ===")
    send_request("Delete the robotics meeting next week.")
