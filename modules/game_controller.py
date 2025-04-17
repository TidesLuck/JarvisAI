import asyncio
import os
from datetime import datetime
from modules.unreal_bridge import UnrealBridge

class GameController:
    def __init__(self):
        self.unreal_bridge = UnrealBridge()

    async def play_game(self, game_action):
        return f"Выполнено действие в игре: {game_action}."

    async def generate_unreal_asset(self, prompt):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        if "blueprint" in prompt.lower():
            blueprint_code = await self.unreal_bridge.generate_blueprint(prompt)
            output_path = f"data/output/unreal_blueprint_{timestamp}.py"
            with open(output_path, "w") as f:
                f.write(blueprint_code)
            return output_path
        elif "mesh" in prompt.lower():
            mesh_path = await self.unreal_bridge.generate_mesh(prompt)
            return mesh_path
        else:
            output_path = f"data/output/unreal_asset_{timestamp}.py"
            code = f"# Unreal Engine Python script\n# {prompt}\nimport unreal\npass"
            with open(output_path, "w") as f:
                f.write(code)
            return output_path