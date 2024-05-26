from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, ClassVar, Self

from app.base.ConfigManager import Config

if TYPE_CHECKING:
    from app.base.ProcessManager import ProcessManager


class Feature(ABC):
    id_: ClassVar[str]
    feature_type: ClassVar[str]
    name: ClassVar[str]
    sequence: ClassVar[int]
    options: ClassVar[list[Config]] = []
    props: ClassVar[set[str]] = set()
    required_props: ClassVar[set[str]] = set()

    def __init__(self, process_manager: "ProcessManager") -> None:
        self.process_manager = process_manager

    @classmethod
    def meet_props_requirements(cls, props: set[str]) -> bool:
        return cls.required_props.issubset(props)

    def update_suggests(self) -> None:
        return

    def validate(self) -> bool:
        self.update_suggests()
        if any(
            not self.process_manager.config.get(option.id_)
            for option in self.options
            if option.required
        ):
            return False
        return True

    @abstractmethod
    def run(self) -> None:
        pass

    def __str__(self) -> str:
        return self.name
