import copy
from dataclasses import dataclass
from enum import Enum
from pprint import pformat
from typing import Optional, Self, TypeVar


class ConfigType(Enum):
    YesNO = 1
    Float = 2
    Integer = 3
    String = 4
    File = 5
    Folder = 6
    FileOrFolder = 7


@dataclass
class Config:
    # maybe a validator (e.g., JSON-Schema)?
    # https://softwareengineering.stackexchange.com/questions/368235/concept-to-validate-objects-across-languages
    name: str
    type_: ConfigType
    id_: str
    alt_text: str = ""
    default: str = ""
    value: str = ""
    required: bool = True
    description: Optional[str] = None
    suggests: Optional[list[str]] = None
    internal: bool = False

    def copy(self) -> Self:
        return copy.copy(self)


StrOrNone = TypeVar("StrOrNone", str, None)


class ConfigManager:
    def __init__(self):
        self.config: dict[str, Config] = {}

    def get(self, id_: str | Config, default: StrOrNone = None) -> str | StrOrNone:
        if isinstance(id_, Config):
            id_ = id_.id_
        conf = self.config.get(id_)
        if conf:
            return conf.value
        return default
    
    def set(self, id_: str | Config, value: str) -> None:
        if isinstance(id_, Config):
            id_ = id_.id_
        self.config[id_].value = value

    def __getitem__(self, id_: str | Config) -> Config:
        if isinstance(id_, Config):
            id_ = id_.id_
        return self.config[id_]

    def may_add_config_item(self, *configs: Config) -> None:
        for config in configs:
            if config.id_ not in self.config:
                self.config[config.id_] = config.copy()
            else:
                self.config[config.id_].internal = False

    def hide_all_configs(self) -> None:
        for conf in self.config.values():
            conf.internal = True

    def __str__(self) -> str:
        return "ConfigManager: " + pformat(self.config)
