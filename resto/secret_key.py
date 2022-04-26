import json

def get_secret_key():
    with open("secrets_api.json", "r") as fd:
        data = json.load(fd)
    return data["SECRET_KEY"]