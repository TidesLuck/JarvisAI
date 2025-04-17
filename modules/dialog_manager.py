import yaml
import asyncio

class DialogManager:
    def __init__(self):
        self.config_path = "config.yaml"

    async def notify(self, message):
        print(f"JarvisAI: {message}")

    async def configure_learning(self, prompt):
        with open(self.config_path, "r") as f:
            config = yaml.safe_load(f)

        if "сколько раз думать" in prompt.lower():
            depth = int(prompt.split()[-1])
            config["learning"]["thinking_depth"] = depth
        if "рекурсивный анализ" in prompt.lower():
            recursive = int(prompt.split()[-1])
            config["learning"]["recursive_thinking"] = recursive

        with open(self.config_path, "w") as f:
            yaml.safe_dump(config, f)
        return f"thinking_depth: {config['learning']['thinking_depth']}, recursive_thinking: {config['learning']['recursive_thinking']}"