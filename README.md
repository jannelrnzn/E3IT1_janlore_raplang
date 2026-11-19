# Fahrzeugverleih

Schulprojekt von Janne Lorenzen und Raphail Langer.

## Was macht das Programm?
Kunden können Fahrräder und E-Bikes mieten. Ein Mietvertrag kann mehrere Fahrzeuge haben und berechnet den Gesamtpreis.

- Fahrrad: Tagespreis × Tage
- E-Bike: (Tagespreis + 5 €) × Tage

Falsche Eingaben wie ein negativer Preis oder eine Mietdauer von 0 werden abgelehnt.

## Dateien
- `kunde.py`, `fahrzeug.py`, `fahrrad.py`, `e_bike.py`, `mietvertrag.py`: die Klassen
- `test_mietvertrag.py`: die Tests
- `docs/`: Diagramme und Screenshots

## Starten
1. Repository als ZIP herunterladen und entpacken
2. Ordner in VS Code öffnen
3. Im Terminal `pip install pytest` eingeben
4. Tests starten mit `python -m pytest -v`

Alle Tests sollten grün sein.
