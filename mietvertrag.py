from kunde import Kunde
from fahrzeug import Fahrzeug


class Mietvertrag:

    def __init__(self, vertragsnummer: int, kunde: Kunde, fahrzeug: Fahrzeug,
                 mietdauer: int, mietbeginn: str = "", mietende: str = "") -> None:
        self.__vertragsnummer = vertragsnummer
        self.__kunde = kunde
        self.__fahrzeuge = [fahrzeug]
        self.__mietdauer = mietdauer
        self.__mietbeginn = mietbeginn
        self.__mietende = mietende

    def get_vertragsnummer(self) -> int:
        return self.__vertragsnummer

    def get_kunde(self) -> Kunde:
        return self.__kunde

    def get_fahrzeuge(self) -> list:
        return self.__fahrzeuge

    def get_mietdauer(self) -> int:
        return self.__mietdauer

    def hinzufuegen_fahrzeug(self, fahrzeug: Fahrzeug) -> None:
        self.__fahrzeuge.append(fahrzeug)

    def gesamtpreis(self) -> float:
        summe = 0.0
        for fahrzeug in self.__fahrzeuge:
            summe = summe + fahrzeug.mietpreis(self.__mietdauer)
        return summe

    def starten(self) -> None:
        for fahrzeug in self.__fahrzeuge:
            fahrzeug.vermieten()

    def beenden(self) -> None:
        for fahrzeug in self.__fahrzeuge:
            fahrzeug.zurueckgeben()
