from dataclasses import dataclass
import datetime
from typing import Any, Final, Literal, TypedDict

from app.base.ConfigManager import ConfigManager
from app.base.Logger import Logger
from app.base.Utils import get_random_chars
from app.feature.Feature import Feature
from app.feature.FeatureManager import FeatureManager

from .FileManager import FileManager


@dataclass
class ContextData:
    input_type: Literal["qq", ""] = ""
    output_type: str = ""


class ProcessManager:
    def __init__(self, config: ConfigManager):
        self.uuid = get_random_chars(4)
        self.create_time: Final[str] = datetime.datetime.now().strftime(
            "%Y-%m-%d_%H.%M.%S"
        )
        self.config = config
        self.file_manager = FileManager(self)
        self.process_logger = Logger(self)
        self.pm_logger = self.process_logger.getLogger("ProcessManager")
        self.feature_chain: list[Feature] = []
        self.context_data: ContextData = ContextData()
        self.feature_manager = FeatureManager(self)

    def __str__(self) -> str:
        return f"ProcessManager: {self.uuid} created at {self.create_time}"

    @property
    def available_props(self) -> set[str]:
        # every props from every feature
        ret = set()
        for feature in self.feature_chain:
            ret.update(feature.props)
        return ret

    @property
    def next_feature_sets(self) -> list[list[Feature]]:
        # get all sets of features
        current_props = self.available_props
        available_features = [
            i
            for i in FeatureManager.features
            if i.meet_props_requirements(current_props)
        ]
        # sort based on sequence
        feature_sets: dict[int, list[Feature]] = {}
        for feature in available_features:
            if feature.sequence not in feature_sets:
                feature_sets[feature.sequence] = []
            feature_sets[feature.sequence].append(
                self.feature_manager.get_instance(feature)
            )
        return [feature_sets[key] for key in sorted(feature_sets.keys())]

    def set_feature_chain(self, feature_set: list[Feature]) -> None:
        # detect if chain is valid (i.e. meet props) and set feature chain
        self.config.hide_all_configs()
        self.feature_chain = []
        for feature in feature_set:
            if feature.meet_props_requirements(self.available_props):
                self.feature_chain.append(feature)
            else:
                raise ValueError(
                    f"Feature {feature} cannot be added to chain, missing props"
                )
            self.config.may_add_config_item(*feature.options)

    @property
    def runnable(self) -> bool:
        return all(i.validate() for i in self.feature_chain)

    def run(self) -> None:
        if not self.runnable:
            raise ValueError("ProcessManager is not runnable")
        for feature in self.feature_chain:
            self.pm_logger.debug(f"Running {feature}")
            feature.run()
            # self.pm_logger.info(f"{feature} finished")
        self.pm_logger.info("ProcessManager finished")
