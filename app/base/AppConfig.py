# base/AppConfig.py
import tomllib


class AppConfig:
    def __init__(self):
        self.config = tomllib.load(open("config.toml", "rb"))
