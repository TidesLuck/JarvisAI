import logging
import os

class Logger:
    def __init__(self, log_path="data/logs/jarvis.log"):
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        logging.basicConfig(filename=log_path, level=logging.INFO)

    def log(self, message):
        logging.info(message)