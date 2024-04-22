import requests 
import json

def signup(email: str, password: str):
    body = {
        "email": email,
        "password": password
    }

    response = requests.post(url="http://127.0.0.1:5000/signup", json=body)
    return response.text

def login(email: str, password: str):
    body = {
        "email": email,
        "password": password,
    }

    response = requests.post(url="http://127.0.0.1:5000/login", json=body)

    return json.loads(response.text)

def test():
    print(login("whatthefuckjusthappened@gmail.com", "whatthefuck"))


if __name__ == "__main__":
    test()