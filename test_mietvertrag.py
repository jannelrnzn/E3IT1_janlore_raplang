from kunde import Kunde
from mietvertrag import Mietvertrag
from fahrrad import Fahrrad
from e_bike import E_Bike


class TestMietpreis:
    def test_mietpreis_berechnen_vorgabe(self):
        kunde = Kunde("Mina Beispiel", 123)
        fahrzeug = Fahrrad("AB-CD 123", 30.00, True, 21)

        mietvertrag = Mietvertrag(1001, kunde, fahrzeug, 3)

        assert mietvertrag.gesamtpreis() == 90.00

    def test_mietpreis_berechnen_eigener(self):
        kunde = Kunde("Raphail", 69)
        fahrzeug = Fahrrad("SHA RL 44", 50.00, True, 21)

        mietvertrag = Mietvertrag(1001, kunde, fahrzeug, 4)

        assert mietvertrag.gesamtpreis() == 200

    def test_fahrzeugstatus_wird_kontrolliert_geaendert(self):
        kunde = Kunde("Mina Beispiel", 123)
        fahrzeug = Fahrrad("AB-CD 123", 30.00, True, 21)
        mietvertrag = Mietvertrag(1001, kunde, fahrzeug, 3)

        assert fahrzeug.ist_verfuegbar() is True
        assert mietvertrag.gesamtpreis() == 90.00

        mietvertrag.starten()
        assert fahrzeug.ist_verfuegbar() is False

        mietvertrag.beenden()
        assert fahrzeug.ist_verfuegbar() is True

    def test_fahrzeug_vermieten_und_zurueckgeben(self):
        fahrzeug = Fahrrad("SHA-JL 21", 45.00, True, 21)

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
        assert mietvertrag_fahrrad.gesamtpreis() == 45.00

        assert e_bike.get_tagespreis() == 30.00
        assert e_bike.get_akkukapazitaet() == 500
        assert mietvertrag_e_bike.gesamtpreis() == 105.00

    def test_e_bike_vermieten_und_zurueckgeben(self):
        kunde = Kunde("Max Mustermann", 456)
        e_bike = E_Bike("E-300", 25.00, True, 600)
        mietvertrag = Mietvertrag(1003, kunde, e_bike, 2)

        assert e_bike.ist_verfuegbar() is True

        mietvertrag.starten()
        assert e_bike.ist_verfuegbar() is False

        mietvertrag.beenden()
        assert e_bike.ist_verfuegbar() is True

    def test_fahrzeuge_berechnen_unterschiedliche_mietpreise(self):
        kunde = Kunde("Mina Beispiel", 123)

        fahrrad = Fahrrad("F-100", 15.00, True, 21)
        e_bike = E_Bike("E-200", 30.00, True, 500)

        mietvertrag = Mietvertrag(1001, kunde, fahrrad, 3)
        mietvertrag.hinzufuegen_fahrzeug(e_bike)

        assert mietvertrag.gesamtpreis() == 150.00

    def test_mehrere_fahrzeuge_starten_und_beenden(self):
        kunde = Kunde("Raphail Langer", 456)

        fahrrad = Fahrrad("F-200", 10.00, True, 7)
        e_bike = E_Bike("E-400", 20.00, True, 400)

        mietvertrag = Mietvertrag(1004, kunde, fahrrad, 2)
        mietvertrag.hinzufuegen_fahrzeug(e_bike)

        assert mietvertrag.gesamtpreis() == 70.00

        mietvertrag.starten()
        assert fahrrad.ist_verfuegbar() is False
        assert e_bike.ist_verfuegbar() is False

        mietvertrag.beenden()
        assert fahrrad.ist_verfuegbar() is True
        assert e_bike.ist_verfuegbar() is True
