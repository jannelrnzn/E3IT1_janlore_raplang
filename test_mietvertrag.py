from kunde import Kunde
from fahrzeug import Fahrzeug
from mietvertrag import Mietvertrag
from fahrrad import Fahrrad
from e_bike import E-Bike

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

    def test_unterschiedliche_fahrzeugarten(self):
        kunde = Kunde("Mina Beispiel", 123)

        fahrrad = Fahrrad("F-100", 15.00, True, 21)
        e_bike = E_Bike("E-200", 30.00, True, 500)

        mietvertrag_fahrrad = Mietvertrag(1001, kunde, fahrrad, 3)
        mietvertrag_e_bike = Mietvertrag(1002, kunde, e_bike, 3)

        assert fahrrad.get_tagespreis() == 15.00
        assert fahrrad.get_anzahl_gaenge() == 21
        assert mietvertrag_fahrrad.mietpreis() == 45.00

        assert e_bike.get_tagespreis() == 30.00
        assert e_bike.get_akkukapazitaet() == 500
        assert mietvertrag_e_bike.mietpreis() == 90.00

    def test_e_bike_vermieten_und_zurueckgeben(self):
        kunde = Kunde("Max Mustermann", 456)
        e_bike = E_Bike("E-300", 25.00, True, 600)
        mietvertrag = Mietvertrag(1003, kunde, e_bike, 2)

        assert e_bike.ist_verfuegbar() is True

        mietvertrag.starten()
        assert e_bike.ist_verfuegbar() is False

        mietvertrag.beenden()
        assert e_bike.ist_verfuegbar() is True
