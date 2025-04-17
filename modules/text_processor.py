import torch
import asyncio
from models.text_model import TextModel
from utils.tokenizer import Tokenizer
from sentence_transformers import SentenceTransformer
import random
import json
import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document

class TextProcessor:
    def __init__(self, model_config, device, memory_manager, learning_manager, personalization, ethics_manager, cognitive_engine, dialog_manager, critical_thinking, model_loader):
        self.tokenizer = Tokenizer(model_config["tokenizer"])
        self.model = model_loader.load_model("text", model_config["path"], quantization=model_config["quantization"], lora=model_config["lora"])
        self.device = device
        self.memory = memory_manager
        self.learning = learning_manager
        self.personalization = personalization
        self.ethics_manager = ethics_manager
        self.cognitive_engine = cognitive_engine
        self.dialog_manager = dialog_manager
        self.critical_thinking = critical_thinking
        self.sentiment_analyzer = SentenceTransformer("all-MiniLM-L6-v2")
        self.rag_store = Chroma(embedding_function=HuggingFaceEmbeddings(), persist_directory="data/knowledge/rag")

    async def initialize_rag(self):
        if os.path.exists("data/knowledge"):
            for file in os.listdir("data/knowledge"):
                if file.endswith(".txt"):
                    content = await self.learning.file_analyzer.read_file(f"data/knowledge/{file}")
                    self.rag_store.add_documents([Document(page_content=content, metadata={"source": file})])

    async def analyze_sentiment(self, prompt):
        embedding = self.sentiment_analyzer.encode(prompt)
        return "neutral"

    async def generate_solutions(self, prompt, depth=1, max_solutions=5):
        solutions = []
        input_ids = self.tokenizer.encode(prompt).to(self.device)
        user_style = await self.personalization.get_user_style()
        prompt = f"{user_style}\n{prompt}"

        if await self.ethics_manager.check_barriers(prompt):
            return [{"text": "Действие запрещено вашими барьерами!", "score": 1.0}]

        rag_results = self.rag_store.similarity_search(prompt, k=3)
        rag_context = "\n".join([doc.page_content for doc in rag_results])
        enhanced_prompt = f"{rag_context}\n{await self.cognitive_engine.enhance_prompt(prompt)}"

        for _ in range(max_solutions):
            output = self.model.generate(input_ids, max_length=100)
            solution = self.tokenizer.decode(output)
            if not await self.ethics_manager.check_barriers(solution):
                solutions.append({"text": solution, "score": random.random()})

        if depth > 1:
            sub_solutions = []
            for solution in solutions:
                sub_prompt = f"Анализируй: {solution['text']}. Найди улучшения."
                for _ in range(3):
                    output = self.model.generate(self.tokenizer.encode(sub_prompt).to(self.device), max_length=100)
                    sub_solution = self.tokenizer.decode(output)
                    if not await self.ethics_manager.check_barriers(sub_solution):
                        sub_solutions.append({"text": sub_solution, "parent": solution["text"], "score": random.random()})
            solutions.extend(sub_solutions)

        verified_solutions = []
        for sol in solutions:
            if await self.critical_thinking.verify_solution(sol["text"], prompt):
                verified_solutions.append(sol)

        verified_solutions.sort(key=lambda x: x["score"], reverse=True)
        return verified_solutions[:3]

    async def process(self, prompt):
        if not await self.ethics_manager.security.authenticate_owner():
            return "Ошибка: только владелец может давать команды!"

        sentiment = await self.analyze_sentiment(prompt)
        response_prefix = "" if sentiment == "neutral" else f"Похоже, ты {sentiment}! "
        context = await self.memory.get_context(prompt)
        if context:
            prompt = f"{context}\n{prompt}"

        if prompt.lower().startswith("учись"):
            content = prompt.replace("учись", "", 1).strip()
            if content.startswith("http"):
                web_content = await self.learning.learn_from_web(content)
                await self.learning.update_knowledge(web_content)
                self.rag_store.add_documents([Document(page_content=web_content, metadata={"source": content})])
                return f"{response_prefix}Обучился на сайте {content}!"
            elif os.path.exists(content):
                file_content = await self.learning.learn_from_file(content)
                await self.learning.update_knowledge(file_content)
                self.rag_store.add_documents([Document(page_content=file_content, metadata={"source": content})])
                return f"{response_prefix}Обучился на файле {content}!"
            else:
                return f"{response_prefix}Укажи ссылку или путь к файлу!"

        if prompt.lower().startswith("измени"):
            parts = prompt.replace("измени", "", 1).strip().split()
            if len(parts) < 2:
                return f"{response_prefix}Укажи файл и что изменить!"
            file_path, action = parts[0], " ".join(parts[1:])
            if os.path.exists(file_path):
                result = await self.learning.file_analyzer.modify_file(file_path, action)
                return f"{response_prefix}Файл изменен: {result}"
            else:
                return f"{response_prefix}Файл {file_path} не найден!"

        if prompt.lower().startswith("настрой обучение"):
            new_settings = await self.dialog_manager.configure_learning(prompt)
            return f"{response_prefix}Настройки обучения обновлены: {new_settings}"

        if prompt.lower().startswith("запустить код"):
            code = prompt.replace("запустить код", "", 1).strip()
            result = await self.learning.python_interpreter.execute_code(code)
            return f"{response_prefix}Результат кода:\n{result}"

        if prompt.lower().startswith("поиск"):
            query = prompt.replace("поиск", "", 1).strip()
            results = await self.learning.web_scraper.search_web(query)
            return f"{response_prefix}Результаты поиска:\n{results}"

        solutions = await self.generate_solutions(prompt, depth=3, max_solutions=3)
        response = f"{response_prefix}JarvisAI нашел следующие решения:\n"
        for i, sol in enumerate(solutions):
            response += f"{i+1}. {sol['text']} (вероятность: {sol['score']:.2f})\n"

        warnings = await self.ethics_manager.check_consequences(prompt, response)
        if warnings:
            response += f"\nПредупреждения:\n{warnings}"

        await self.memory.save_context(prompt, response)
        await self.learning.update_knowledge(f"Вопрос: {prompt}\nОтвет: {response}")
        await self.personalization.update_profile(prompt, response)
        return response