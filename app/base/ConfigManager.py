# base/ConfigManager.py
class ConfigManager:
    def __init__(self):
        self.config = {}

    def set_config(self, key, value):
        self.config[key] = value
