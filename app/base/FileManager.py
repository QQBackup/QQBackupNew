from pathlib import Path
import pathlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ProcessManager import ProcessManager


class FileManager:
    current_folder = Path(".")
    assets_folder = Path("assets")
    def __init__(self, process_manager: "ProcessManager") -> None:
        self.process_manager = process_manager
        self.output_folder = Path("output") / self.process_manager.create_time
        self.output_folder.mkdir(parents=True, exist_ok=True)
        
