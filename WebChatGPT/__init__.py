from .main import ChatGPT
from importlib import metadata

__all__ = ["ChatGPT"]

try:
    __version__ = metadata.version("webchatgpt")
except metadata.PackageNotFoundError:
    __version__ = "0.0.0"
__author__ = "Smartwa"
__repo__ = "https://github.com/Simatwa/WebChatGPT"
__info__ = "Reverse Engineering of ChatGPT Web-version."
