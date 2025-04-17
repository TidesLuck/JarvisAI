import json
import os
import asyncio
from utils.crypto import encrypt_data, decrypt_data

class MemoryManager:
    def __init__(self, memory_path, security_manager, auto_save_interval):
        self.memory_path = memory_path
        self.security = security_manager
        self.auto_save_interval = auto_save_interval
        self.memory = {}
        if os.path.exists(memory_path):
            with open(memory_path, "r") as f:
                encrypted_data = f.read()
                decrypted_data = decrypt_data(encrypted_data, self.security.key)
                self.memory = json.loads(decrypted_data)

    async def get_context(self, prompt):
        return self.memory.get(prompt, "")

    async def save_context(self, prompt, response):
        self.memory[prompt] = response
        await self.save_to_file()

    async def clear_context(self, prompt=None):
        if prompt:
            self.memory.pop(prompt, None)
        else:
            self.memory.clear()
        await self.save_to_file()

    async def save_to_file(self):
        encrypted_data = encrypt_data(json.dumps(self.memory), self.security.key)
        with open(self.memory_path, "w") as f:
            f.write(encrypted_data)

    async def auto_save(self):
        while True:
            await self.save_to_file()
            await asyncio.sleep(self.auto_save_interval)