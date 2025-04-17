from utils.crypto import encrypt_data, decrypt_data
import asyncio

class SecurityManager:
    def __init__(self, key):
        self.key = key

    async def authenticate_owner(self):
        return True