from .Message import Message


class TextMessage(Message):
    def __init__(self, text: str):
        self.text = text

    def as_text(self) -> str:
        return self.text
