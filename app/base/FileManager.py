# base/FileManager.py
import os


class FileManager:
    @staticmethod
    def get_output_dir():
        return os.path.join(os.getcwd(), "output")
