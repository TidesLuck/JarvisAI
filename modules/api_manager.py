from fastapi import FastAPI
import asyncio

app = FastAPI()

class APIManager:
    def __init__(self, text_processor, vision_processor, audio_processor, learning_manager):
        self.text_processor = text_processor
        self.vision_processor = vision_processor
        self.audio_processor = audio_processor
        self.learning = learning_manager

        @app.post("/api/v1/text")
        async def text_endpoint(data: dict):
            prompt = data.get("prompt", "")
            response = await self.text_processor.process(prompt)
            return {"response": response}

        @app.post("/api/v1/image")
        async def image_endpoint(data: dict):
            prompt = data.get("prompt", "")
            image_path = await self.vision_processor.generate_image(prompt)
            return {"response": f"Изображение: {image_path}"}

        @app.post("/api/v1/audio")
        async def audio_endpoint(data: dict):
            action = data.get("action", "")
            audio_path = data.get("audio_path", "")
            if action == "voice_command":
                command = await self.audio_processor.process_audio(audio_path, "голосовая команда")
                response = await self.text_processor.process(command)
                return {"response": response}
            return {"response": "Действие не поддерживается"}

        @app.post("/api/v1/code")
        async def code_endpoint(data: dict):
            code = data.get("code", "")
            result = await self.learning.python_interpreter.execute_code(code)
            return {"response": result}

    async def run(self, host="0.0.0.0", port=8080):
        import uvicorn
        await uvicorn.run(app, host=host, port=port)