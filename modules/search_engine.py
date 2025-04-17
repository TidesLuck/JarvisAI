import aiohttp
import asyncio
from serpapi import GoogleSearch
from config import load_config

class SearchEngine:
    def __init__(self):
        self.config = load_config()
        self.serpapi_key = self.config["search_config"]["serpapi_key"]

    async def search(self, query):
        params = {
            "q": query,
            "api_key": self.serpapi_key,
            "num": 10
        }
        try:
            search = GoogleSearch(params)
            results = search.get_dict().get("organic_results", [])
            return [result.get("snippet", "") for result in results]
        except Exception as e:
            return [f"Search error: {str(e)}"]

    async def deep_search(self, query, max_iterations=3):
        results = await self.search(query)
        for _ in range(max_iterations - 1):
            refined_query = self.refine_query(query, results)
            new_results = await self.search(refined_query)
            results.extend(new_results)
            if self.is_sufficient(results):
                break
        return results[:10]  # Limit to top 10 results

    def refine_query(self, query, results):
        # Simple refinement: add context from results
        keywords = " ".join([r.split()[0] for r in results[:2] if r])
        return f"{query} {keywords}"

    def is_sufficient(self, results):
        # Check if results are good enough (basic heuristic)
        return len(results) >= 5 and any(len(r) > 50 for r in results)