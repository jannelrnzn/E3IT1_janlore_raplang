from fahrzeug import Fahrzeug


class E_Bike(Fahrzeug):
    def __init__(self, kennzeichen: str, tagespreis: float, verfuegbar: bool,
                 akkukapazitaet: int) -> None:
        super().__init__(kennzeichen, tagespreis, verfuegbar)
        self.__akkukapazitaet = akkukapazitaet

    def get_akkukapazitaet(self) -> int:
        return self.__akkukapazitaet
