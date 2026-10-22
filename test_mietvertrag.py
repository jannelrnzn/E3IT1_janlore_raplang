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

    def test_fahrzeugstatus_wird_kontrolliert_geandert(self):
        kunde = Kunde("Mina Beispiel", 123)
        fahrzeug = Fahrzeug("AB-CD 123", 30.00, True)
        mietvertrag = Mietvertrag(1001, kunde, fahrzeug, 3)

        assert fahrzeug.ist_verfuegbar() is True
        assert mietvertrag.mietpreis() == 90.00

        mietvertrag.starten()
        assert fahrzeug.ist_verfuegbar() is False

        mietvertrag.beenden()
        assert fahrzeug.ist_verfuegbar() is True

    def test_fahrzeug_vermieten_und_zurueckgeben(self):
        fahrzeug = Fahrzeug("SHA-JL 151", 45.00)

        assert fahrzeug.ist_verfuegbar() is True

        fahrzeug.vermieten()
        assert fahrzeug.ist_verfuegbar() is False

        fahrzeug.zurueckgeben()
        assert fahrzeug.ist_verfuegbar() is True
        
