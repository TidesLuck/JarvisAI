from web3 import Web3
import asyncio

class Blockchain:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

    async def interact(self, contract_address, action):
        return f"Взаимодействие с блокчейном: {action}."