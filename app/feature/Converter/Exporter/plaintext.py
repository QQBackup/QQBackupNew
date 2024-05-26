from pathlib import Path
from typing import TYPE_CHECKING

from app.chatter.Chatter import Chatter
from app.feature.Converter.Exporter.Exporter import Exporter

if TYPE_CHECKING:
    from app.base.ProcessManager import ProcessManager


class PlainTextExporter(Exporter):
    def export(self, chat: Chatter):
        filename = f"{chat.uid}.txt"
        filepath = self.output_folder / filename
        self.logger.debug(f"Exporting chat {chat.uid} to plain text at {filepath}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str([i.as_text() for i in chat.messages]))
