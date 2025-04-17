import requests
import asyncio

class APIConnector:
    async def call_api(self, endpoint, data):
        response = requests.post(endpoint, json=data)
        return response.json()