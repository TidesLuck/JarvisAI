import torch
from diffusers import StableDiffusionPipeline
from config import load_config

class ImageGenerator:
    def __init__(self):
        self.config = load_config()
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "checkpoints/sd",
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        ).to(self.device)

    async def generate_image(self, prompt, output_path="data/output/generated_image.png"):
        try:
            image = self.pipe(prompt, num_inference_steps=50).images[0]
            image.save(output_path)
            return output_path
        except Exception as e:
            return f"Image generation error: {str(e)}"