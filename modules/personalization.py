import json
import os
import asyncio

class Personalization:
    def __init__(self, user_profile_path):
        self.user_profile_path = user_profile_path
        self.profile = {}
        if os.path.exists(user_profile_path):
            with open(user_profile_path, "r") as f:
                self.profile = json.load(f)

    async def get_user_style(self):
        return self.profile.get("style", "default")

    async def update_profile(self, prompt, response):
        self.profile["interactions"] = self.profile.get("interactions", []) + [{"prompt": prompt, "response": response}]
        with open(self.user_profile_path, "w") as f:
            json.dump(self.profile, f, ensure_ascii=False, indent=2)