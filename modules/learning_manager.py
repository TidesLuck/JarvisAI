import os
import json
import asyncio
from modules.web_scraper import WebScraper
from modules.file_analyzer import FileAnalyzer
from modules.scenario_modeler import ScenarioModeler
from modules.game_controller import GameController
from modules.code_analyzer import CodeAnalyzer
from modules.physics_simulator import PhysicsSimulator
from modules.cognitive_engine import CognitiveEngine
from modules.python_interpreter import PythonInterpreter
from modules.knowledge_clustering import KnowledgeClustering

class LearningManager:
    def __init__(self, data_path, memory_manager, model_loader):
        self.data_path = data_path
        self.memory = memory_manager
        self.model_loader = model_loader
        self.web_scraper = WebScraper()
        self.file_analyzer = FileAnalyzer()
        self.scenario_modeler = ScenarioModeler()
        self.game_controller = GameController()
        self.code_analyzer = CodeAnalyzer()
        self.physics_simulator = PhysicsSimulator()
        self.cognitive_engine = CognitiveEngine()
        self.python_interpreter = PythonInterpreter()
        self.clustering = KnowledgeClustering()
        self.knowledge_base = {}
        knowledge_path = os.path.join(data_path, "knowledge/knowledge.json")
        if os.path.exists(knowledge_path):
            with open(knowledge_path, "r") as f:
                self.knowledge_base = json.load(f)

    async def learn_from_web(self, url):
        content = await self.web_scraper.scrape(url)
        await self.clustering.cluster_knowledge(content)
        return content

    async def learn_from_file(self, file_path):
        content = await self.file_analyzer.read_file(file_path)
        await self.clustering.cluster_knowledge(content)
        return content

    async def update_knowledge(self, content):
        self.knowledge_base[content[:50]] = content
        with open(os.path.join(self.data_path, "knowledge/knowledge.json"), "w") as f:
            json.dump(self.knowledge_base, f, ensure_ascii=False, indent=2)
        with open(os.path.join(self.data_path, f"knowledge/{hash(content)}.txt"), "w") as f:
            f.write(content)