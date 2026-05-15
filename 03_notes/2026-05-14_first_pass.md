# First Pass: Heim-Massenformel

Datum: 2026-05-14

## Was lokal erzeugt wurde

- PDF-Textauszuege in `07_outputs/extracted_text/`.
- ZIP-/XLSM-Strukturlisten in `07_outputs/archive_listing/`.
- Statischer XLSM-Export in `07_outputs/xlsm_static_export/`.

## Heim-Dateien mit konkreten Masseninformationen

- `Basic_thoughts_1976.txt`: Addendum `Particle Masses` enthaelt eine Tabelle `B. Heim` vs. `Rev.Mod.Phys. 48, April 1976`.
- `Massenformel_nach_B_Heim_1982.txt`: enthaelt Formelsystem, Quantenzahlen, Naturkonstanten und Auswahlregeln, aber im ersten Pass keine fertige moderne Vergleichstabelle.
- `Erweiterte_Massenformel_Nach_Heim_1989.txt`: enthaelt 1989b-Formelerweiterung und wichtige Warnstellen:
  - einige Klammern wurden laut IGW nach besten Schaetzungen korrigiert;
  - Programm enthaelt zunaechst Grundzustaende und Neutrinomassen, nicht Lebensdauern;
  - fuer Resonanzen sind `z(N)` und `Q(N)` unvollstaendig;
  - in einem Term wurden frei waehlbare Parameter empirisch angepasst.
- `Heim_1989_Massenformel_0.4.xlsm`: statisch exportiert; sheet `Vergleich` enthaelt berechnete vs. empirische Werte, nutzt aber u.a. CODATA 2014 und Wiki-Vergleiche.
- `Elementarstrukturen_der_Materie_2.txt`: Tabellenanhang enthaelt Grundmuster-Massen, Resonanzspektren sowie moegliche Werte fuer W- und Z-Terme. Der Tau-Lepton-Status ist im OCR unklar; es erscheint ein tau-aehnlicher Zustand um 1783.430 MeV als mu-Resonanz.
- `massformula/C 0.66/output_plus_neutrino.txt`: sekundarer Implementierungsoutput mit 20 Referenzmassen und 5 Neutrino-Werten. Dieses Output ist fuer Reproduktionsarbeit wertvoll, aber wegen spaeterer Codeaenderungen und Referenzdaten nicht als Primaerbeleg zu werten.

## Sicherheitsnotiz

Die Dateien `Heim_1989_Massenformel_0.4.xlsm`, `massformula.zip` und `massformula89.zip` wurden nicht ausgefuehrt. Die XLSM wurde nur mit `openpyxl` gelesen, ZIPs nur gelistet.

Die ZIPs wurden anschliessend in `01_sources/heim_primary_unpacked_untrusted/` entpackt, aber Inhalte wurden nicht ausgefuehrt. Der Zweck ist statische Analyse von Quelltexten, Outputs und Tabellen.

## Erste methodische Konsequenz

Die Spreadsheet-Werte sind nuetzlich fuer eine Tabellenreproduktion, aber nicht als primaerer Beleg fuer Heims originale Formel. Fuer jede Formelzeile brauchen wir spaeter eine Textstelle in Heim/naher Quelle.

## Sofort sichtbare Befunde

- Die bekannten leichten Grundzustaende liegen in den Heim-nahen Tabellen teilweise grob bei den damaligen Werten, aber nicht innerhalb heutiger Messunsicherheiten.
- Die moeglichen W-Werte im Tabellenanhang liegen ca. 0.55 Prozent ueber dem heutigen PDG-Wert.
- Die moeglichen Z-Werte liegen ca. 1.88 Prozent ueber dem heutigen PDG-Wert.
- Fuer diese Bewertung ist noch offen, ob die Werte echte historische Vorhersagen, Ex-post-Zuordnungen oder branch-sensitive Tabellenwerte sind.
