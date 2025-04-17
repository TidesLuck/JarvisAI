from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import asyncio
import os

app = FastAPI()

class WebInterface:
    def __init__(self, text_processor, vision_processor, audio_processor, device_control, file_analyzer, web_scraper, game_controller, code_analyzer, multimodal_engine, api_manager, python_interpreter):
        self.text_processor = text_processor
        self.vision_processor = vision_processor
        self.audio_processor = audio_processor
        self.device_control = device_control
        self.file_analyzer = file_analyzer
        self.web_scraper = web_scraper
        self.game_controller = game_controller
        self.code_analyzer = code_analyzer
        self.multimodal_engine = multimodal_engine
        self.api_manager = api_manager
        self.python_interpreter = python_interpreter

        # Монтируем папку с фронтендом
        app.mount("/static", StaticFiles(directory="frontend"), name="static")

        @app.get("/")
        async def root():
            return {"message": "JarvisAI Dashboard. Access UI at /static/index.html"}

        @app.get("/status")
        async def get_status():
            return {
                "tasks": len(asyncio.all_tasks()),
                "memory_usage": os.path.getsize("data/memory.json") / 1024,  # KB
                "knowledge_files": len(os.listdir("data/knowledge")),
            }

        @app.post("/execute")
        async def execute_command(data: dict):
            prompt = data.get("prompt", "")
            response = await self.text_processor.process(prompt)
            return {"response": response}

    async def run(self, host="0.0.0.0", port=8000):
        import uvicorn
        asyncio.create_task(self.api_manager.run())
        await uvicorn.run(app, host=host, port=port)