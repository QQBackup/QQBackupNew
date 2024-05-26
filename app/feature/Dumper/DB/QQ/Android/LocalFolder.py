from pathlib import Path
from app.base.ConfigManager import Config, ConfigType
from app.feature.Dumper.Dumper import Dumper
from app.feature.FeatureManager import FeatureManager


def extract_qq_number_from_db(db_path: str | Path) -> str:
    name = Path(db_path).name.removesuffix(".db").removeprefix("slowtable_")
    if not name.isdigit():
        return ""
    return name


def extract_possible_qq_numbers_from_path(path: str | Path) -> list[str]:
    path = Path(path)
    ret = []
    if path.is_dir():
        ret = [
            extract_qq_number_from_db(db) for db in path.glob("*.db") if db.is_file()
        ]
    if path.is_file():
        ret = [extract_qq_number_from_db(path)]
    return list(filter(None, ret))


@FeatureManager.register
class LocalFolderDumper(Dumper):
    id_ = "Dumper.LocalFolder"
    name = "i18n.localfolder"
    options = [
        Config(
            id_="dumper_local_folder",
            name="local_folder",
            type_=ConfigType.FileOrFolder,
            description="i18n.str.Local folder to store the dump",
            default="",
            required=True,
        ),
        Config(
            id_="qq_number",
            name="qq-number",
            type_=ConfigType.String,
            description="i18n.str.QQ_number",
            default="",
            required=True,
        ),
    ]
    props = {"decrypted_database", "QQ", "Android"}

    def update_suggests(self) -> None:
        super().update_suggests()
        conf = self.process_manager.config.get("dumper_local_folder", "")
        if conf != "" and (conf_path := Path(conf)).exists():
            self.process_manager.config["qq_number"].suggests = (
                extract_possible_qq_numbers_from_path(conf_path)
            )

    def validate(self) -> bool:
        if not super().validate():
            return False
        return True

    def run(self):
        super().run()
        # set input_type
        self.process_manager.context_data.input_type = "qq"
