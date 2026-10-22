class Kunde:

    def __init__(self, name: str, kundennummer: int) -> None:
        self.__name = name
        self.__kundennummer = kundennummer

    def get_name(self) -> str:
        return self.__name

    def get_kundennummer(self) -> int:
        return self.__kundennummer
