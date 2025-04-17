from transformers import AutoModelForCausalLM, WhisperForConditionalGeneration, CLIPModel
import asyncio

class ExternalModels:
    def __init__(self, model_config, device):
        self.model_config = model_config
        self.device = device

    async def load_llama(self):
        model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b").to(self.device)
        return model

    async def load_whisper(self):
        model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-base").to(self.device)
        return model

    async def load_clip(self):
        model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(self.device)
        return model