import asyncio
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from modules.text_processor import TextProcessor
from modules.vision_processor import VisionProcessor
from modules.audio_processor import AudioProcessor
from modules.image_generator import ImageGenerator
from modules.auto_learn import AutoLearner
from modules.search_engine import SearchEngine
from config import load_config

app = FastAPI()
config = load_config()
text_processor = TextProcessor(config["text_model"])
vision_processor = VisionProcessor(config["vision_model"])
audio_processor = AudioProcessor()
image_generator = ImageGenerator()
auto_learner = AutoLearner()
search_engine = SearchEngine()

class TextRequest(BaseModel):
    prompt: str

class ImageRequest(BaseModel):
    prompt: str

class AudioRequest(BaseModel):
    action: str
    audio_path: str = None

class CodeRequest(BaseModel):
    code: str

@app.post("/api/v1/text")
async def process_text(request: TextRequest):
    if "поиск" in request.prompt.lower():
        results = await search_engine.deep_search(request.prompt.replace("поиск", "").strip())
        return {"response": "\n".join(results)}
    elif "учись" in request.prompt.lower():
        topic = request.prompt.replace("учись", "").strip()
        return {"response": await auto_learner.auto_learn(topic)}
    return {"response": await text_processor.process(request.prompt)}

@app.post("/api/v1/image")
async def process_image(request: ImageRequest):
    output_path = await image_generator.generate_image(request.prompt)
    return {"image_path": output_path}

@app.post("/api/v1/audio")
async def process_audio(request: AudioRequest):
    if request.action == "voice_command":
        text = await audio_processor.process_audio(request.audio_path)
        return {"text": text}
    elif request.action == "stream":
        text = await audio_processor.stream_recognition()
        return {"text": text}
    elif request.action == "synthesize":
        audio_path = await audio_processor.synthesize_speech(request.audio_path)
        return {"audio_path": audio_path}
    raise HTTPException(status_code=400, detail="Invalid audio action")

@app.post("/api/v1/code")
async def process_code(request: CodeRequest):
    # Placeholder for code execution
    return {"output": "Code executed"}

if __name__ == "__main__":
    uvicorn.run(app, host=config["web_interface"]["host"], port=config["web_interface"]["port"])