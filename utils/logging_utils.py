from datetime import datetime
from utils.config import LOG_LEVEL


def log(message, level="INFO"):
    levels = ["DEBUG", "INFO", "ERROR"]
    if level not in levels:
        level = "INFO"
    if levels.index(level) >= levels.index(LOG_LEVEL):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}")
