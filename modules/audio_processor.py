import asyncio
import speech_recognition as sr
import pyttsx3
import whisper
from config import load_config

class AudioProcessor:
    def __init__(self):
        self.config = load_config()
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()
        self.whisper_model = whisper.load_model(self.config["audio_model"]["path"])
        self.dialog_context = []

    async def process_audio(self, audio_path):
        try:
            result = self.whisper_model.transcribe(audio_path)
            text = result["text"]
            self.dialog_context.append({"user": text})
            return text
        except Exception as e:
            return f"Audio processing error: {str(e)}"

    async def stream_recognition(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                self.dialog_context.append({"user": text})
                return text
            except sr.UnknownValueError:
                return "Could not understand audio"
            except sr.RequestError as e:
                return f"Speech recognition error: {str(e)}"

    async def synthesize_speech(self, text):
        self.dialog_context.append({"ai": text})
        self.tts_engine.save_to_file(text, "data/output/response.wav")
        self.tts_engine.runAndWait()
        return "data/output/response.wav"

    def get_dialog_context(self):
        return self.dialog_context[-5:]  # Keep last 5 exchanges