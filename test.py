import requests

API_KEY = "AIzaSyDLeWrUJKNZMaNr67ttxpz_WjW9skqk-Mw"
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + API_KEY

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {"parts": [{"text": "Hello, how are you?"}]}
    ]
}

response = requests.post(url, headers=headers, json=data)
if response.ok:
    print("API call successful!")
    print("Response:", response.json())
else:
    print("Error:", response.text)