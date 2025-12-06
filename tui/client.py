import requests

class APIClient:
    def __init__(self, base_url):
        self.session = requests.Session()
        self.base_url = base_url.rstrip("/")

    def login(self, username, password):
        url = f"{self.base_url}/api/v1/auth/login/"
        response = self.session.post(url, data={
            "username": username,
            "password": password
        })
        return response