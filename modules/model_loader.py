import torch
from transformers import AutoModel, AutoModelForCausalLM, WhisperProcessor, WhisperForConditionalGeneration, CLIPModel, CLIPProcessor
from peft import LoraConfig, get_peft_model
import asyncio

class ModelLoader:
    def __init__(self, model_config, device):
        self.model_config = model_config
        self.device = device
        self.loaded_models = {}

    def load_model(self, model_type, path, quantization=False, lora=False):
        if model_type in self.loaded_models:
            return self.loaded_models[model_type]

        if model_type == "text":
            model = AutoModelForCausalLM.from_pretrained(path).to(self.device)
            if quantization:
                model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
            if lora:
                lora_config = LoraConfig(target_modules=["q_proj", "v_proj"])
                model = get_peft_model(model, lora_config)
        elif model_type == "vision":
            model = CLIPModel.from_pretrained(path).to(self.device)
            processor = CLIPProcessor.from_pretrained(path)
            return {"model": model, "processor": processor}
        elif model_type == "audio":
            model = WhisperForConditionalGeneration.from_pretrained(path).to(self.device)
            processor = WhisperProcessor.from_pretrained(path)
            return {"model": model, "processor": processor}
        else:
            model = None

        self.loaded_models[model_type] = model
        return model

    def unload_model(self, model_type):
        if model_type in self.loaded_models:
            del self.loaded_models[model_type]
            torch.cuda.empty_cache()