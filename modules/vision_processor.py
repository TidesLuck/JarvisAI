import torch
from diffusers import StableDiffusionPipeline
import cv2
import os
import asyncio
from datetime import datetime
import speech_recognition as sr
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

class VisionProcessor:
    def __init__(self, model_config, device, model_loader):
        self.device = device
        self.stable_diffusion = model_loader.load_model("vision", model_config["path"])
        self.recognizer = sr.Recognizer()

    async def generate_image(self, prompt):
        if self.stable_diffusion:
            image = self.stable_diffusion(prompt).images[0]
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            output_path = f"data/output/image_{timestamp}.png"
            image.save(output_path)
            return output_path
        return "Stable Diffusion не инициализирован."

    async def process_video(self, video_path, action):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_path = f"data/output/modified_video_{timestamp}.mp4"
        if action.lower().startswith("сделай короче"):
            clip = VideoFileClip(video_path)
            short_clip = clip.subclip(0, min(10, clip.duration))
            short_clip.write_videofile(output_path, codec="libx264")
            clip.close()
            return output_path
        elif action.lower().startswith("добавь субтитры"):
            clip = VideoFileClip(video_path)
            audio_path = f"data/output/temp_audio_{timestamp}.wav"
            clip.audio.write_audiofile(audio_path)
            with sr.AudioFile(audio_path) as source:
                audio = self.recognizer.record(source)
                try:
                    text = self.recognizer.recognize_google(audio)
                except:
                    text = "Не удалось распознать речь."
            subtitle = TextClip(text, fontsize=24, color="white", bg_color="black", size=clip.size)
            subtitle = subtitle.set_duration(clip.duration)
            final_clip = CompositeVideoClip([clip, subtitle.set_position(("center", "bottom"))])
            final_clip.write_videofile(output_path, codec="libx264")
            clip.close()
            final_clip.close()
            os.remove(audio_path)
            return output_path
        return "Действие не поддерживается."