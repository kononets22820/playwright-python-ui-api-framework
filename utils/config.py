import os

ENV = os.getenv("ENV", "dev").lower()

URLS = {
    "dev": "https://the-internet.herokuapp.com",
    # placeholders to show structure (you can change later)
    "qa": "https://the-internet.herokuapp.com",
    "prod": "https://the-internet.herokuapp.com",
}

BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
API_BASE_URL = os.getenv("API_BASE_URL", "https://httpbin.org")