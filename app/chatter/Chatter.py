from abc import ABC, abstractmethod
from typing import Iterable

from app.message.Message import Message


class Chatter(ABC):
    messages: list[Message]

    def __init__(self, name: str, uid: str) -> None:
        self.name = name
        self.uid = uid
        self.messages = []

    def append(self, message: Message) -> None:
        self.messages.append(message)

    def extend(self, messages: Iterable[Message]) -> None:
        self.messages.extend(messages)
