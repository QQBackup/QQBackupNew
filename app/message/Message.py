# chat/message/Message.py
from abc import ABC, abstractmethod


class Message(ABC):
    @abstractmethod
    def as_text(self) -> str:
        pass
