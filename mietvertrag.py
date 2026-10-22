
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

    def get_vertragsnummer(self) -> int:
        return self.__vertragsnummer

    def get_kunde(self) -> Kunde:
        return self.__kunde

    def get_fahrzeug(self) -> Fahrzeug:
        return self.__fahrzeug

    def get_mietdauer(self) -> int:
        return self.__mietdauer
     
    def mietpreis(self) -> float:
        return self.mietdauer * self.fahrzeug.get_grundpreis()

    def starten(self) -> None:
        self.__fahrzeug.vermieten()

    def beenden(self) -> None:
        self.__fahrzeug.zurueckgeben()
