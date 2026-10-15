
from kunde import Kunde
from fahrzeug import Fahrzeug

from datetime import date

class Mietvertrag:
    def __init__(self, vertragsnummer: int, kunde: Kunde, fahrzeug: Fahrzeug, mietdauer: int, mietbeginn: str = "", mietende: str = "") -> None:
        self.vertragsnummer = vertragsnummer
        self.kunde = kunde
        self.fahrzeug = fahrzeug
        self.mietdauer = mietdauer  
        self.mietbeginn = mietbeginn    # erstmal optional
        self.mietende = mietende        # erstmal optional

    def mietpreis(self) -> float:
        return self.mietdauer * self.fahrzeug.grundpreis

    def beenden(self) -> None:
        pass
