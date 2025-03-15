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

def get_guest_by_id(guest_id: int):
    url = f"{BASE_URL}/guests/{guest_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Guest Info:")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Failed to retrieve guest info:", response.text)


def get_chatbot_by_user(clerk_user_id: str):
    url = f"{BASE_URL}/chatbotbyuser/{clerk_user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print("chatbot Info:")
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

def insert_guest(name: str, email: str):
    url = f"{BASE_URL}/guest/"
    payload = {
        "name": name,
        "email": email
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Guest inserted successfully:")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Failed to insert guest:", response.text)


def insert_chat_sessions(chatbot_id: int, guest_id: int):
    url = f"{BASE_URL}/chat_sessions"
    payload = {
        "chatbot_id": chatbot_id,
        "guest_id": guest_id
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("chat session inserted successfully:")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Failed to insert chat session:",response.text)

if __name__ == "__main__":
    # Example call to GET endpoint
    insert_message(1, "Hello", "ai")
    insert_guest("John Doe", "johndoe@gmail.com")
    insert_chat_sessions(1, 1)