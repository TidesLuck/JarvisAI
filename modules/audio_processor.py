import speech_recognition as sr
from gtts import gTTS
import os
import asyncio
from datetime import datetime

class AudioProcessor:
    def __init__(self, model_config, device):
        self.device = device
        self.recognizer = sr.Recognizer()

    async def recognize_speech(self, audio_path=None):
        if audio_path:
            with sr.AudioFile(audio_path) as source:
                audio = self.recognizer.record(source)
        else:
            with sr.Microphone() as source:
                audio = self.recognizer.listen(source)
        try:
            return self.recognizer.recognize_google(audio)
        except:
            return "Не удалось распознать речь."

    async def synthesize_speech(self, text):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = f"data/output/speech_{timestamp}.mp3"
        tts = gTTS(text=text, lang="ru")
        tts.save(output_file)
        return output_file

    async def process_audio(self, audio_path, action):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_path = f"data/output/modified_audio_{timestamp}.mp3"
        if action.lower().startswith("голосовая команда"):
            command = await self.recognize_speech(audio_path)
            return command
        with open(audio_path, "rb") as f:
            content = f.read()
        with open(output_path, "wb") as f:
            f.write(content)
        return output_path