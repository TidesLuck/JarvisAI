import os
import asyncio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FolderMonitor(FileSystemEventHandler):
    def __init__(self, text_processor, file_analyzer, learning_manager):
        self.text_processor = text_processor
        self.file_analyzer = file_analyzer
        self.learning = learning_manager
        self.folders = {
            "data/input/learn": "learn",
            "data/input/modify": "modify",
            "data/input/analyze": "analyze"
        }

    def on_created(self, event):
        if event.is_directory:
            return
        file_path = event.src_path
        for folder, action in self.folders.items():
            if file_path.startswith(folder):
                asyncio.create_task(self.process_file(file_path, action))

    async def process_file(self, file_path, action):
        if action == "learn":
            content = await self.file_analyzer.read_file(file_path)
            await self.learning.update_knowledge(content)
            await self.text_processor.dialog_manager.notify(f"Обучился на файле {file_path}!")
        elif action == "modify":
            result = await self.file_analyzer.modify_file(file_path, "auto")
            await self.text_processor.dialog_manager.notify(f"Файл изменен: {result}")
        elif action == "analyze":
            content = await self.file_analyzer.read_file(file_path)
            await self.text_processor.dialog_manager.notify(f"Анализ файла {file_path}:\n{content}")

    async def monitor_folders(self):
        observer = Observer()
        for folder in self.folders:
            observer.schedule(self, folder, recursive=False)
        observer.start()
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()