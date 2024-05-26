"""
读取并解密数据库，同时调用Exporter输出
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from app.base.ProcessManager import ProcessManager
from app.feature.Converter.Exporter.Exporter import Exporter


class Importer(ABC):

    def __init__(self, process_manager: "ProcessManager"):
        self.process_manager = process_manager
        self.exporters: list[Exporter] = []
        self.logger = self.process_manager.process_logger.getLogger(
            self.__class__.__name__
        )

    def add_exporter(self, *exporters: Exporter) -> None:
        self.exporters.extend([i for i in exporters if i not in self.exporters])
        return None

    @abstractmethod
    def run(self) -> None:
        pass
