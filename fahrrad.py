from fahrzeug import Fahrzeug


class Fahrrad(Fahrzeug):
    def __init__(self, kennzeichen: str, tagespreis: float, verfuegbar: bool,
                 anzahl_gaenge: int) -> None:
        super().__init__(kennzeichen, tagespreis, verfuegbar)
        self.__anzahl_gaenge = anzahl_gaenge

    def get_anzahl_gaenge(self) -> int:
        return self.__anzahl_gaenge
