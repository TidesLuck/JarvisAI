import requests
from bs4 import BeautifulSoup
import asyncio
import re
from modules.search_engine import SearchEngine

class WebScraper:
    def __init__(self):
        self.search_engine = SearchEngine()

    async def scrape(self, url):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            text = ""
            for tag in soup.find_all(["p", "h1", "h2", "h3", "li"]):
                text += tag.get_text() + "\n"
            return text
        except Exception as e:
            return f"Ошибка: {str(e)}"

    async def search_web(self, query):
        results = await self.search_engine.search(query)
        cleaned_text = re.sub(r"[\n\r]+", "\n", "\n".join(results))
        return cleaned_text[:2000]