# coding: utf-8
from pathlib import Path

# change DEBUG to False if you want to compile the code to exe
DEBUG = "__compiled__" not in globals()


YEAR = 2024
AUTHOR = "Zhan Han"
VERSION = "v1.4"
APP_NAME = "piji"
HELP_URL = "https://blog.arshdelight.com"
REPO_URL = "https://baidu.com"
FEEDBACK_URL = "https://baidu.com"
DOC_URL = "https://blog.arshdelight.com"

CONFIG_FOLDER = Path('AppData').absolute()
CONFIG_FILE = CONFIG_FOLDER / "config.json"
