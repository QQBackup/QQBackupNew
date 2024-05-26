class I18n:
    lang: str

    def __init__(self) -> None:
        # TODO: Implement i18n logic
        pass

    def get(self, key: str) -> str:
        return key

    def set_lang(self, lang: str) -> None:
        self.lang = lang


i18n = I18n()
t = i18n.get
