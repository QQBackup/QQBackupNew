import logging
from typing import TYPE_CHECKING

from .FileManager import FileManager

if TYPE_CHECKING:
    from .ProcessManager import ProcessManager

format = "[%(asctime)s] %(levelname)-8s  %(message)s    (from %(name)s at %(filename)s:%(lineno)d %(funcName)s())"
formatter = logging.Formatter(format)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.DEBUG, format=format, handlers=[console_handler])


class GlobalLogger:
    logger = logging.getLogger("GlobalLogger")

    handler = logging.FileHandler(FileManager.current_folder / "global.log")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    @staticmethod
    def getLogger(child_name: str) -> logging.Logger:
        return GlobalLogger.logger.getChild(child_name)


class Logger:
    def __init__(self, process_manager: "ProcessManager") -> None:
        self.process_manager = process_manager

        self.logger = logging.getLogger(process_manager.uuid)

        handler = logging.FileHandler(
            self.process_manager.file_manager.output_folder / "process.log"
        )
        self.logger.addHandler(handler)

        self.getLogger("Logger").debug("Process logger initialized")

    def getLogger(self, child_name: str) -> logging.Logger:
        return self.logger.getChild(child_name)
