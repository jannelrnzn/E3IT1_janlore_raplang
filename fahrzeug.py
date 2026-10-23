class Fahrzeug:

    def __init__(self, kennzeichen: str, tagespreis: float, verfuegbar: bool = True) -> None:
        self.__kennzeichen=kennzeichen
        self.__tagespreis=tagespreis
        self.__verfuegbar=verfuegbar

    def get_kennzeichen(self) -> str:
        return self.__kennzeichen

    def get_tagespreis(self) -> float:
        return self.__tagespreis

    def ist_verfuegbar(self) -> bool:
        return self.__verfuegbar

    def vermieten(self) -> None:
        self.__verfuegbar = False

    def zurueckgeben(self) -> None:
        self.__verfuegbar = True


