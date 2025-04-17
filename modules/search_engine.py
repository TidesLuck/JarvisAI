import requests
import asyncio
import os

class SearchEngine:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_KEY", "your_serpapi_key")

    async def search(self, query):
        try:
            response = requests.get(
                "https://serpapi.com/search",
                params={"q": query, "api_key": self.api_key}
            )
            response.raise_for_status()
            results = response.json().get("organic_results", [])
            return [result.get("snippet", "") for result in results]
        except Exception as e:
            return [f"Ошибка поиска: {str(e)}"]