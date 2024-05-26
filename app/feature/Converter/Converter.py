from app.base.ConfigManager import Config, ConfigType
from app.feature.Converter.Exporter.plaintext import PlainTextExporter
from app.feature.Converter.Importer.qq import QQImporter
from app.feature.Feature import Feature
from app.feature.FeatureManager import FeatureManager


@FeatureManager.register
class Converter(Feature):
    id_ = "Converter"
    feature_type = "i18n.converter"
    sequence = 300
    options = [Config("stub", ConfigType.String, "Stub", required=True, default="stub")]
    required_props = {"decrypted_database"}
    name = "i18n.converter"

    def run(self) -> None:
        logger = self.process_manager.process_logger.getLogger(self.__class__.id_)
        logger.info("Running Converter")
        input_type = self.process_manager.context_data.input_type
        match input_type:
            case "qq":
                logger.info("Convert source is: QQ")
                importer = QQImporter(self.process_manager)
                importer.add_exporter(PlainTextExporter(self.process_manager))
                importer.run()
            case "_":
                raise NotImplementedError(f"Input type {input_type} not implemented")
