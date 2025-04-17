import asyncio
import json
from modules.web_scraper import WebScraper
from modules.knowledge_clustering import KnowledgeClustering

class AutoLearner:
    def __init__(self):
        self.scraper = WebScraper()
        self.clustering = KnowledgeClustering()

    async def auto_learn(self, topic, max_urls=5):
        try:
            content = await self.scraper.search_web(topic, max_urls)
            knowledge = {"topic": topic, "content": content}
            with open(f"data/knowledge/{topic.replace(' ', '_')}.json", "w") as f:
                json.dump(knowledge, f)
            await self.clustering.cluster_knowledge(knowledge)
            return f"Learned about {topic}"
        except Exception as e:
            return f"Auto-learning error: {str(e)}"

if __name__ == "__main__":
    learner = AutoLearner()
    asyncio.run(learner.auto_learn("quantum computing"))