from abc import ABC, abstractmethod
from pathlib import Path
from typing import TYPE_CHECKING

from app.chatter.Chatter import Chatter

if TYPE_CHECKING:
    from app.base.ProcessManager import ProcessManager


class Exporter(ABC):
    def __init__(self, process_manager: "ProcessManager"):
        self.process_manager = process_manager
        self.output_folder = self.process_manager.file_manager.output_folder / "result"
        self.output_folder.mkdir(parents=True, exist_ok=True)
        self.logger = self.process_manager.process_logger.getLogger(
            self.__class__.__name__
        )

    def before_export(self):
        pass

    @abstractmethod
    def export(self, chat: Chatter):
        pass

    def after_export(self):
        pass
