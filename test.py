import requests
import json

# Base URL for the FastAPI backend
BASE_URL = "http://localhost:8000"

def get_chatbot_by_id(chatbot_id: int):
    url = f"{BASE_URL}/chatbots/{chatbot_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Chatbot Info:")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Failed to retrieve chatbot info:", response.text)

def insert_message(chat_session_id: int, content: str, sender: str):
    url = f"{BASE_URL}/messages"
    payload = {
        "chat_session_id": chat_session_id,
        "content": content,
        "sender": sender
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Message inserted successfully:")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Failed to insert message:", response.text)

if __name__ == "__main__":
    # Example call to GET endpoint
    get_chatbot_by_id(1)
    
    