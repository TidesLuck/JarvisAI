import json
import os
import asyncio

class EthicsManager:
    def __init__(self, barriers_path):
        self.barriers_path = barriers_path
        self.barriers = []
        self.security = None
        if os.path.exists(barriers_path):
            with open(barriers_path, "r") as f:
                self.barriers = json.load(f)

    async def check_barriers(self, prompt):
        for barrier in self.barriers:
            if barrier.lower() in prompt.lower():
                return True
        return False

    async def check_consequences(self, prompt, response):
        return ""

    async def add_barrier(self, barrier):
        self.barriers.append(barrier)
        with open(self.barriers_path, "w") as f:
            json.dump(self.barriers, f, ensure_ascii=False, indent=2)