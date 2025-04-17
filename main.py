import yaml
import torch
import asyncio
from modules.text_processor import TextProcessor
from modules.vision_processor import VisionProcessor
from modules.audio_processor import AudioProcessor
from modules.device_control import DeviceControl
from modules.file_analyzer import FileAnalyzer
from modules.web_scraper import WebScraper
from modules.memory_manager import MemoryManager
from modules.learning_manager import LearningManager
from modules.personalization import Personalization
from modules.meta_learning import MetaLearning
from modules.scenario_modeler import ScenarioModeler
from modules.game_controller import GameController
from modules.ethics_manager import EthicsManager
from modules.code_analyzer import CodeAnalyzer
from modules.cognitive_engine import CognitiveEngine
from modules.physics_simulator import PhysicsSimulator
from modules.security_manager import SecurityManager
from modules.multimodal_engine import MultimodalEngine
from modules.folder_monitor import FolderMonitor
from modules.dialog_manager import DialogManager
from modules.api_manager import APIManager
from modules.python_interpreter import PythonInterpreter
from modules.critical_thinking import CriticalThinking
from modules.model_loader import ModelLoader
from modules.cloud_sync import CloudSync
from utils.web_interface import WebInterface

async def load_config(config_path="config.yaml"):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

async def main():
    config = await load_config()
    device = torch.device("cuda" if torch.cuda.is_available() and config["hardware"]["use_gpu"] else "cpu")
    security = SecurityManager(config["security_key"])
    memory = MemoryManager(config["memory_path"], security, config["auto_save_interval"])
    model_loader = ModelLoader(config["model_config"], device)
    learning = LearningManager(config["data_path"], memory, model_loader)
    personalization = Personalization(config["user_profile_path"])
    meta_learning = MetaLearning()
    scenario_modeler = ScenarioModeler()
    ethics_manager = EthicsManager(config["barriers_path"])
    cognitive_engine = CognitiveEngine()
    physics_simulator = PhysicsSimulator()
    multimodal_engine = MultimodalEngine()
    dialog_manager = DialogManager()
    critical_thinking = CriticalThinking()
    python_interpreter = PythonInterpreter()
    text_processor = TextProcessor(config["text_model"], device, memory, learning, personalization, ethics_manager, cognitive_engine, dialog_manager, critical_thinking, model_loader)
    vision_processor = VisionProcessor(config["vision_model"], device, model_loader)
    audio_processor = AudioProcessor(config["audio_model"], device)
    device_control = DeviceControl()
    file_analyzer = FileAnalyzer()
    web_scraper = WebScraper()
    game_controller = GameController()
    code_analyzer = CodeAnalyzer()
    folder_monitor = FolderMonitor(text_processor, file_analyzer, learning)
    api_manager = APIManager(text_processor, vision_processor, audio_processor, learning)
    cloud_sync = CloudSync(config["cloud_config"])

    if not await security.authenticate_owner():
        raise Exception("Ошибка аутентификации владельца!")

    # Запуск фоновых задач
    asyncio.create_task(folder_monitor.monitor_folders())
    asyncio.create_task(memory.auto_save())
    asyncio.create_task(cloud_sync.sync_knowledge())

    # Запуск веб-интерфейса и API
    web_interface = WebInterface(
        text_processor, vision_processor, audio_processor, device_control,
        file_analyzer, web_scraper, game_controller, code_analyzer, multimodal_engine, api_manager, python_interpreter
    )
    await web_interface.run()

if __name__ == "__main__":
    asyncio.run(main())