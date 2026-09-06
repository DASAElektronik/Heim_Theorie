# TODO

## Aktueller Einstieg (2026-09-06)

- [x] Isolierten Alpha-Audit 1982/1989 implementieren, testen und gegenlesen.
- [x] Gedruckte Zweig-/Kehrwertangaben unter Rundung pruefen; Bericht erstellt.
- [x] Buch (105) eng gegenpruefen; Y3=1-Spezialisierung dokumentieren.
- [x] Buchherleitung von eta/A_k/Y3 begrenzt verfolgen; offene Schritte markieren.
- [x] 1989 B58-B62 mit oeffentlichen Fassungen/Errata begrenzt abgleichen.
- [x] Y3-/Praezisionsdiagnose implementieren, unabhaengig pruefen und sichern.
- [x] eta-Buchdefinition und Ladungsmittelung/Korrelationsschluss lokal ausarbeiten.
- [x] Buch-Indexbruecke an(98) auffinden, ohne IGW(V) still zu korrigieren.
- [x] Neuen Energieordnungs-Konflikt quellenseitig und algebraisch gegenpruefen.
- [x] Energie-/Masse-/Wellenlaengenbegriffe vor(105) begrenzt zurueckverfolgen.
- [x] pc/T und h/(mc)/h/p getrennt rechnen, Quellen-/Mathematikreviews sichern.
- [x] A_--Quellenanker, invariante Form versus Skalar und exakte Boostdiagnose.
- [x] Heims eigene Motivation fuer Alpha-Korrektur/Kreiswelle lokalisieren.
- [x] p21-Matrixdruck getrennt von p56-Kontext algebraisch gegenpruefen.
- [ ] Operative Energie-/Arbeitszuordnung im vollstaendigen Quellenmodell.
- [ ] H-Wellenproblem mit Randbedingungen, Kreisform und Wellenzuordnung.
- [ ] Manuskript1981 p5: A=4C/freie Integrationskonstante/Y getrennt mit Buch/Y3 vergleichen.
- [ ] Fruehere Ausgabe/Erratum zum p21-Matrixdruck suchen, falls zugaenglich.
- [ ] Physikalische Begruendung L*Delta=k, Auswahl(98a), historischer Rechenweg.
- [ ] Danach fehlende Massenabhaengigkeiten sowie B50 und Gamma/Q_N bearbeiten.
- [ ] Verstaendnisbilanz vor breiter Recherche nach neueren Widerlegungen.

Aktuelle Nutzerreihenfolge: erst verstehen/rekonstruieren, dann externe
physikalische Bewertung. Eigene begruendete Verbesserungen sind erwuenscht;
siehe `UNDERSTANDING_ROADMAP.md` und die Alpha-Erweiterungskandidaten.

Massgeblicher Wiedereinstieg: `RESUME.md`. Die folgenden Phasenlisten sind
die urspruengliche Projektplanung und nicht der aktuelle Detailstatus.

## Phase 1: Quellenbasis

- [ ] Vollstaendige Quellenliste aus `01_sources/source_register.md` pruefen.
- [ ] Entscheiden, welche PDFs lokal gesichert werden sollen.
- [ ] Bibliographische Metadaten fuer Heim-Hauptwerke erfassen.
- [ ] Quellen nach Typ markieren: Primaerquelle, Uebersetzung, Sekundaerquelle, spaetere Erweiterung, Kritik.
- [ ] Lizenz-/Copyright-Status fuer lokale Kopien dokumentieren.

## Phase 2: Zielmodell

- [ ] Eingrenzen: zuerst Massenformel, nicht Gesamttheorie.
- [ ] Tabelle der zu vergleichenden Teilchen definieren.
- [ ] Heims behauptete Vorhersagewerte erfassen.
- [ ] Heutige PDG/NIST-Werte mit Unsicherheiten erfassen.
- [ ] Freie Parameter der Rekonstruktion zaehlen.

## Phase 3: Rekonstruktion

- [ ] Formelbibliothek in `04_reconstruction/formula_library/` gegen PDF-Bilder pruefen.
- [ ] Fuer jede Formel aus `formula_catalog.csv` mindestens eine Einzelformel-Datei anlegen.
- [ ] Alle Symbole aus `symbols/symbol_register.csv` disambiguieren.
- [ ] `04_reconstruction/PARAMETER_BOOK.md` mit konkreten Quellenstellen fuellen.
- [ ] Erste Model Card fuer `model_1982_from_text` anlegen.
- [ ] Notation aus Heim-Quellen in moderne Symbole uebersetzen.
- [ ] Formelketten fuer Elektron, Myon, Tau, Proton, Neutron identifizieren.
- [ ] Minimalen Rechenweg als Pseudocode formulieren.
- [ ] Erste Implementierung in `04_reconstruction/mass_formula/` anlegen.
- [ ] Rechenergebnisse gegen Originaltabellen vergleichen.

## Phase 4: Bewertung

- [ ] Abweichungen zu heutigen Referenzdaten berechnen.
- [ ] Pruefen, welche Werte echte Vorhersagen waren und welche schon bekannt waren.
- [ ] Sensitivitaet gegen Parameterwahl untersuchen.
- [ ] Konflikte mit Standardmodell, QFT, Lorentz-Invarianz und bekannten Symmetrien sammeln.
- [ ] Zwischenbericht in `06_docs/` schreiben.
