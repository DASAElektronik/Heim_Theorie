# Quellenvertrag: früher Konstantensatz und Tabellenfassung

2026-10-18, Etappe41. Ausgang `b2c1113`, sauberer Arbeitsbaum.
Fortsetzung von Etappe40; ein Agent, kein Mehragentenreview.

Untersucht werden der bereits archivierte fotografische H015-DESY-Scan,
H006 als spätere Darstellung und die statischen H010-Abschriften als
getrennte Überlieferungsstufen. Suche nach Konstanten, deren Zuweisungen,
gedruckten Ausgaben und Datierungs-/Programmköpfen. H004371 und H00329
bleiben der in Etappe40 festgelegte Vergleich; keine stillen Korrekturen.

OCR dient zur Navigation; tragende fotografierte Seiten vollständig
visuell prüfen. Datumsaufdruck, Archivbezeichnung und Echtheit trennen.
Originalprogramm oder Tabellenidentität nur bei tatsächlichem Beleg
behaupten. Keine Ausführung historischer Programme, Makros oder Dateien.

Zunächst Herkunftsprüfung ohne neue Massenkalibrierung oder freie
Konstantenwahl. Falls eine begrenzte Zahlendiagnose sinnvoll wird, vorab
Quelle, Formel, Inputs und Aussagegrenze ergänzen. Keine moderne Empirie.

Ausgabe: Quellenumfang und Bericht HISTORICAL_CONSTANTS_2026-10-18,
Fortschrittsdateien und neuer Befund bei substanziellem Ergebnis.
Alte Rechenprofile, Befunde und datierte PDF/Grafiken erhalten. Bestehende
Integritätsprüfung; keine Tests bloßer Textwiederholung. Die frühere
Commit-/Push-Anweisung wurde für b2c1113 erfüllt; kein erneuter Push aus
diesem Fortsetzungsauftrag abgeleitet.

## Begrenzte Diagnose, vor Auswertung festgelegt

Nach Sichtung von H015 PDF5 (GINIT1) und27 (Ausgabekopf): ausschließlich
den Initialisierungsblock nachrechnen. Die Ausgabe war vor Rechnung bekannt;
dies ist ein Reproduktionstest, kein blinder Vorhersagetest.
Feste Eingaben: PI=3.1415926535, HQ=1.0545887e-34, C=2.99792458e8,
GAM=6.6732e-11, RG=376.73037659, S0=1, FAKMEV=0.05609545e31,
XI=1.61803399, ALFA=1/137.03602725, BETA=1/1.00001411.
EBN=exp(1). EQ aus der fotografierten29-gleichen Formel;
ETA/THETA/AMU/ALFP/ALFM wie GINIT. Keine Teilchenmasse oder Matrixauswertung.

Vergleich mit den achtstelligen gedruckten Ausgaben aufPDF27 durch
halbe letzte Druckeinheit unter angenommener Rundung. Decimal60/90 als
numerische Stabilitätskontrolle; kein Emulator des IBM-FORTRAN/REAL*16.
Keine Inputs aus H004, H010 oder moderner Empirie ergänzen. Quelltoken,
Formeltranskription, Ergebnis und Rundungsannahme getrennt dokumentieren.
