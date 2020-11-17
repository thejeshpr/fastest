import requests
from fastapi import Request
from fastapi import FastAPI

app = FastAPI()

@app.get("/{ip}")
def root(ip: str):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    return response.json()