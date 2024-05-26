from app.chatter.Friend import Friend
from app.feature.Converter.Importer.Importer import Importer
from app.message.TextMessage import TextMessage


class QQImporter(Importer):
    def run(self):
        for exporter in self.exporters:
            exporter.before_export()

        db_path = self.process_manager.config.get("dumper_local_folder")
        qq_number = self.process_manager.config.get("qq_number")
        self.logger.debug(f"QQ number: {qq_number}, db path: {db_path}")
        friend1 = Friend("testfriend", "123456788")
        friend1.append(TextMessage("hello"))
        friend1.append(TextMessage("world"))
        friend2 = Friend("testfriend2", "123456787")
        chats = [friend1, friend2]

        for chat in chats:
            for exporter in self.exporters:
                exporter.export(chat)

        for exporter in self.exporters:
            exporter.after_export()
