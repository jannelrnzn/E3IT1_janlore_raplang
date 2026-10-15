
from kunde import Kunde
from fahrzeug import Fahrzeug

from datetime import date

class Mietvertrag:
    def __init__(self, vertragsnummer: int, kunde: Kunde, fahrzeug: Fahrzeug, mietdauer: int) -> None:
        self.vertragsnummer = vertragsnummer
        self.kunde = kunde
        self.fahrzeug = fahrzeug
        self.mietdauer = mietdauer

    def mietpreis(self) -> float:
        return

    def beenden(self) -> None:
        pass
