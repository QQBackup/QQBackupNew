from typing import TYPE_CHECKING
from app.base.Logger import GlobalLogger
from app.feature.Feature import Feature

if TYPE_CHECKING:
    from app.base.ProcessManager import ProcessManager


logger = GlobalLogger.getLogger(__name__)


class FeatureManager:
    features: list[type[Feature]] = []

    @classmethod
    def register(cls, feature: type[Feature]) -> type[Feature]:
        cls.features.append(feature)
        # logger.debug(f"Feature {feature} registered")
        return feature

    def __init__(self, process_manager: "ProcessManager"):
        self.process_manager = process_manager
        self.feature_instances: list[Feature] = [
            i(process_manager) for i in self.features
        ]

    def get_instance(self, feature: type[Feature]) -> Feature:
        return next(i for i in self.feature_instances if isinstance(i, feature))
