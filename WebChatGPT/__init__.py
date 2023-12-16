from .main import ChatGPT

__all__ = ["ChatGPT"]

__version__ = "0.0.1"
__author__ = "Smartwa"
__repo__ = "https://github.com/Simatwa/WebChatGPT"
__info__ = "Reverse Engineered ChatGPT Web-version."

import logging

logging.basicConfig(
    format="%(levelname)s - %(message)s - (%(asctime)s) ",  # [%(module)s,%(lineno)s]",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)

getExc = lambda e: e.args[1] if len(e.args) > 1 else str(e)
