from kunde import Kunde
from fahrzeug import Fahrzeug

from datetime import date

class Mietvertrag:
    def __init__(self, vertragsnummer: int, mietbeginn: str, mietende: str, kunde: Kunde, fahrzeug: Fahrzeug) -> None:
        self.vertragsnummer=vertragsnummer
        self.mietbeginn=mietbeginn
        self.mietende=mietende
        self.kunde=kunde
        self.fahrzeug=fahrzeug

    def mietpreis(self) -> float:
        return 
    def beenden(self) -> None:
        pass