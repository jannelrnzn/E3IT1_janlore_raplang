from kunde import Kunde
from fahrzeug import Fahrzeug
from mietvertrag import Mietvertrag

import pytest
import sys
import os

class TestMietpreis:
    def test_mietpreis_berechnen_vorgabe(self):
        kunde = Kunde("Mina Beispiel", 123)
        fahrzeug = Fahrzeug("AB-CD 123", 30.00, True)

        mietvertrag = Mietvertrag(1001, kunde, fahrzeug, 3)

        assert mietvertrag.mietpreis() == 90.00

    def test_mietpreis_berechnen_eigener(self):
        kunde = Kunde("Raphail", 169)
        fahrzeug = Fahrzeug("SHA RL 44", 50.00, True)

        mietvertrag = Mietvertrag(1001, kunde, fahrzeug, 4)

        assert mietvertrag.mietpreis() == 200
