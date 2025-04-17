import asyncio
from sentence_transformers import SentenceTransformer
import numpy as np

class CriticalThinking:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    async def verify_solution(self, solution, prompt):
        solution_emb = self.model.encode(solution)
        prompt_emb = self.model.encode(prompt)
        similarity = np.dot(solution_emb, prompt_emb) / (np.linalg.norm(solution_emb) * np.linalg.norm(prompt_emb))
        return similarity > 0.7