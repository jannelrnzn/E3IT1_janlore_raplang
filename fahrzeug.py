class Fahrzeug:

    def __init__(self, kennzeichen: str, grundpreis: float, verfuegbar: bool) -> None:
        self.__kennzeichen=kennzeichen
        self.__grundpreis=grundpreis
        self.__verfuegbar=verfuegbar

    def get_kennzeichen(self) -> str:
        return self.__kennzeichen

    def get_grundpreis(self) -> float:
        return self.__grundpreis

    def ist_verfuegbar(self) -> bool:
        return self.__verfuegbar

    def vermieten(self) -> None:
        self.__verfuegbar = False

    def zurueckgeben(self) -> None:
        self.__verfuegbar = True


