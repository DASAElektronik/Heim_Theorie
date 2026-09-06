# Skripte

## Etappe 30: gebundene Buch-Pseudosingulett-Rechnung

```powershell
py -3.13 -B scripts/audit_book_pseudosinglet.py --check --verify-sources
py -3.13 -B -m unittest discover -s tests -p test_book_pseudosinglet.py -v
```

Der neue zwoelfte Ergebnischeck bindet den vorab fixierten Eingabevertrag
per Hash, prueft H004 und den eigenen80-Stellen-Snapshot. Zwei Buchprofile,
Q/alpha_i/A16/W, gewoehnlicher Auswahlzweig, direkte107-Gates und separate
107b-Diagnose; kein allgemeiner TRC-/Kollaps-/Massenloeser.
`--write` erneuert nur den neuen `book_pseudosinglet_results.json`.
17neueTests mit80/120-Vergleich,264gesamt; alle elf alten Checks erhalten.
Unabhaengige Machin-/Fixpunktrechnung120/160 und exakte Strukturpruefung
in den BOOK_PSEUDOSINGLET_NUMERICS-/STRUCTURE-Reviews imAlpha-Audit.
Bericht: `06_docs/BOOK_PSEUDOSINGLET_2026-09-06.md`.

## Etappe 29: exakte Buch-Auswahldiagnosen

`py -3.13 -B -m unittest discover -s tests -p test_book_selection.py -v`
prueft13eigene skalare Faelle: sukzessive Maxima, gemeinsame Integerausgabe
zweier Inputs, affine A-Inversion, Floor-/Kappen-/Transferreste und Gates.
Rationale Log-/Exp-Helfer aus Etappe25; keine physikalischen Buchinputs,
vollstaendigen107-Gates, allgemeine TRC-Implementierung oder Masse.
Unabhaengiger selbstenthaltener37-Pruefungen-Block in
`04_reconstruction/alpha_audit/reviews/BOOK_SELECTION_MATH_REVIEW_2026-09-06.md`.
Gesamtsuite247Tests,elfalteChecks; keine bisherigen Snapshots geaendert.
Bericht: `06_docs/BOOK_SELECTION_2026-09-06.md`.

## Etappe 28: reduzierte F16-Bestimmtheitsdiagnosen

`py -3.13 -B -m unittest discover -s tests -p test_f16_determinacy.py -v`
prueft zehn exakte Fraction-Faelle: verschiedene Grenzwerte, explizite
Restschranken, Geruestschalter und bedingte108-Inversion. Eigene skalare
Folgen, keine metronischen Loesungen, Konstantenprofile, Y9-Fits oder Massen.
Allgemeine Beweise im Bericht `06_docs/F16_DETERMINACY_2026-09-06.md`;
endliche Stichproben allein beweisen keine Konvergenz. 234Tests insgesamt,
elf alteChecks erhalten; unabhaengigerReviewblock52Faelle erneut ausgefuehrt.

## Etappe 27: exakte A16-Identitaeten und Quellenstatus

`py -3.13 -B -m unittest discover -s tests -p test_a16_origin.py -v`
prueft zehn P/L-/Y9-Identitaeten, Vorzeichen, Termrollen und K4-Schwellen.
Synthetische Fraction-Zeugen und zuvor zitierte W4-Werte; kein Fit,
keine neue Quellenrechnung oder Masse. Beide unabhaengigen Codebloecke
stehen in `reviews/A16_ALGEBRA_REVIEW_2026-09-06.md` im Alpha-Audit.
224Tests insgesamt; alle elf bisherigen Snapshots erhalten.

## Etappe 26: H006-Myoninput, W und Auswahl ohne Masse

`py -3.13 -B scripts/audit_muon_selection.py --check --verify-sources`
prueft den neuen 80-stelligen Snapshot und den festen H006-Hash.
Zwoelf vorab benannte Quellen-/Lesartprofile; keine Masseneinheit,
Messdaten oder Sollbesetzung. `--write` erneuert nur den neuen Snapshot.
`py -3.13 -B -m unittest discover -s tests -p test_muon_selection.py -v`
prueft15Faelle mit80/120-Stellenvergleich; keinIntervallzertifikat.
Gesamtsuite214Tests,elfSnapshots; alteRechner/Outputs unveraendert.
Bericht: `06_docs/MUON_SELECTION_2026-09-06.md`.

## Etappe 25: isolierte K4/W4-Restpruefung

`py -3.13 -B -m unittest discover -s tests -p test_k4_w4_selection.py -v`
prueft 14 synthetische Fraction-/Intervallfaelle einschliesslich
Gleichungsresten, Ganzzahlgrenzen und getrennten Strukturbedingungen.
Kein allgemeiner Auswahl- oder Massenrechner. Gesamtsuite: 199 Tests;
zehn alte Snapshot-/Quellchecks bleiben unveraendert.
Bericht: `06_docs/K4_W4_SELECTION_2026-09-06.md`.

## Implementiert: Alpha-Audit (2026-09-06)

`audit_alpha.py` berechnet den isolierten 1982/1989-Konsistenz-Audit mit der
Python-Standardbibliothek. `py -3.13 scripts/audit_alpha.py --check --verify-sources`
prueft gespeicherte Ergebnisse und lokale PDF-Hashes.
`py -3.13 -m unittest discover -s tests -v` fuehrt die Tests aus.
Details: `04_reconstruction/alpha_audit/README.md`.

## Befundregister: nur Metadatenpruefung

`py -3.13 scripts/validate_finding_register.py` prueft Schema, eindeutige
Befund-IDs, bekannte Quell-IDs und sichere existierende Nachweisdateien in
`04_reconstruction/alpha_audit/FINDING_REGISTER.json`. Kein Ausfuehren der
dort vermerkten Nachprueftexte, keine Wahrheitspruefung der Befunde.
Die physikalisch-algebraischen Audits bleiben davon getrennt.

## Konfigurationsauswahl und gesamter Snapshotcheck

`audit_configuration_selection.py` trennt die drei gedruckten Aussageebenen
vor Buch(98a), rechnet u_q und dokumentiert die bedingte positive Paarmenge.
`--write` erneuert nur `05_analysis/configuration_selection_diagnostics.json`;
`--check` vergleicht ohne Schreiben. Mathematisches pi, keine Messwerte/Fits.
Vollstaendige Nachpruefung des aktuellen Rechenstands:

```powershell
py -3.13 scripts/audit_alpha.py --check --verify-sources
py -3.13 scripts/audit_alpha_book.py --check
py -3.13 scripts/audit_charge_averaging.py --check --verify-sources
py -3.13 scripts/audit_energy_kinematics.py --check --verify-sources
py -3.13 scripts/audit_lorentz_meaning.py --check --verify-sources
py -3.13 scripts/audit_wave_closure.py --check --verify-sources
py -3.13 scripts/audit_configuration_selection.py --check --verify-sources
py -3.13 scripts/audit_exponential_context.py --check --verify-sources
py -3.13 scripts/audit_n0_electron.py --check --verify-sources
py -3.13 scripts/audit_historical_n0.py --check --verify-sources
py -3.13 scripts/audit_muon_selection.py --check --verify-sources
py -3.13 scripts/validate_finding_register.py
py -3.13 -m unittest discover -s tests -q
```

Ohne lokale Fremdquellen `--verify-sources` weglassen. Die elf numerischen
Snapshots sind dann weiter pruefbar, die Quelldateien nicht. 224 Tests bestehen.

## Historische Exponenten: Quellenlesarten getrennt pruefen

`tests/test_historical_exponents.py` prueft sieben exakte algebraische
Eigenschaften der getrennten A/B-Exponenten: Abstand, Sondergleichheit,
N0-Punkt, Nachbarpunkte, lokalen Bereich und Anschluss der Logumkehrung.
Keine neuen Massen, keine Aenderung bestehender Normalisierungen.
Unabhaengiger, von Root erneut ausgefuehrter Fraction-Block:
`04_reconstruction/alpha_audit/reviews/HISTORICAL_EXPONENT_MATH_REVIEW_2026-09-06.md`.
Quellenvergleich und FIND-027-Nachtrag:
`06_docs/HISTORICAL_EXPONENTS_2026-09-06.md`.

## Gekoppelte Potentialpfade: reine exakte Diagnostik

`tests/test_potential_paths.py` ergaenzt zehn Fraction-Tests fuer die
vier normierten (98)-Paare, Grenzen einer gemeinsamen unveraenderten
Komponentenkurve, gekoppelte endliche Spruenge und synthetische H-Pfade.
Getrennte positive Hilfskanaele sind nicht widerlegt; ihre Interpolation
wird nicht als Quelldynamik ausgegeben. Keine neuen Masseneingaben.
Unabhaengiger, von Root erneut ausgefuehrter Code in
`04_reconstruction/alpha_audit/reviews/POTENTIAL_PATH_MATH_REVIEW_2026-09-06.md`.
Bericht `06_docs/POTENTIAL_PATHS_2026-09-06.md`; alte Snapshots unveraendert.

## Skalierter Schritt und bedingte H/G-Rekurrenz

`tests/test_metronic_step.py` ergaenzt zehn Tests: nichtlineare Skalierung
versus innerer Argumentshift, gemischte H/G-Gewichte, positive Rekurrenz,
ganzer Logrest, X-only-Zeugen und gleiche Endpunkte bei verschiedenen
Zwischenwerten. Synthetische Werte und zusaetzliches gemeinsames Gitter,
keine Quellen-Potentialpfade. Unabhaengiger Code:
`04_reconstruction/alpha_audit/reviews/METRONIC_STEP_MATH_REVIEW_2026-09-06.md`.
Bericht `06_docs/METRONIC_STEP_2026-09-06.md`; kein elfter Snapshot.

## Metronische Integration: exakte Operatorzeugen

`tests/test_metronic_integration.py` prueft14 neue Faelle: inklusive
Teleskopie, indizierte Untergrenze, korrigierte Produkt-/Quotientenregel,
endliche Kettenregel, Logfehlergrenzen, signierte Gewichte, Skalierung,
Fibonacci-Zeugen und die vier bedingten Potentialquotienten. Fraction-
Logintervalle mit expliziter Restschranke; keine Teilchen-Schrittweiten,
neuen Massen oder Fits. Der eigenstaendige Code in
`04_reconstruction/alpha_audit/reviews/METRONIC_MATH_REVIEW_2026-09-06.md`
wurde separat von Root ausgefuehrt (13Felder80/120Stellen). Alte Rechner,
Inputs und Snapshots bleiben unveraendert.

## Alpha3: lokale Bestimmtheitszeugen

`tests/test_alpha3_assumptions.py` enthaelt elf neue exakte Tests fuer
Koeffizientenverschiebungen, stetige Grenzfortsetzungen, synthetische
Anker und bedingte Eindeutigkeit. Keine neuen Teilchenmassen oder Fits.
Der unabhaengige ausfuehrbare Reviewblock in
`04_reconstruction/alpha_audit/reviews/ALPHA3_ASSUMPTIONS_MATH_REVIEW_2026-09-06.md`
prueft dieselbe Fragestellung ohne Import des Root-Testcodes.

## Alpha3: letzte Buchalgebra, kein neuer Massenrechner

`tests/test_alpha3_origin.py` prueft sechs elementare Zusammenhaenge mit
exakten rationalen Beispielwerten. Empirisch gewaehlte Buchkoeffizienten
werden vorausgesetzt; keine Validierung metronischer Integration oder
physikalischer Vorhersagen. Kein elfter Snapshot und kein Fremdprogrammlauf.

## H006/H010: getrennte N0-Vergleichsprofile

`audit_historical_n0.py` rechnet 64 vorab festgelegte Formel-/Inputkombinationen
plus eine alternative H006-Wurzelreichweite. Reelle Hochpraezisionsrechnung,
kein Pascal-/C-Binary-Replay. Historischer Ausgabewert dient nur zum Vergleich
nach der Berechnung; eigene mathematische K4-Zertifizierung statt Code-Offsets.
`--write` erneuert ausschliesslich `05_analysis/historical_n0_results.json`.
16 neue Tests und unabhaengige 65-Zellen-Gegenrechnung. Bericht:
`06_docs/HISTORICAL_N0_2026-09-06.md`. Alle alten Rechner bleiben unveraendert.

## H006: begrenzter N0-Elektronfall

`audit_n0_electron.py` verwendet ausschliesslich die festgelegte
H006-Konfiguration x2/e-, N=0, den expliziten XXVI-/Algorithmuspfad und
historische dimensionale Konstanten. Drei vorab deklarierte reine
Zahlenprofile, keine Zielmasse und kein gemessenes Alpha als Input.
Die alte v/nu-Lesung wird durch eine dokumentierte H006-Indexbruecke
korrigiert; XIV bleibt als abweichende Exponentenlesart sichtbar.
K4=1 folgt in diesem Fall aus einer exakten Identitaet, nicht aus Epsilon-Rundung.
`--write` erzeugt nur `05_analysis/n0_electron_results.json`; `--check`
vergleicht ohne Schreiben. Keine allgemeine Teilchen-/Resonanz-Enumeration.
13 neue Tests und unabhaengige Zahlenanker; Bericht `06_docs/N0_ELECTRON_2026-09-06.md`.

## Bedingtes skalares Exponentialabbild

`audit_exponential_context.py` berechnet die explizite E=1-Abbildung von
EDM2(79) mit H(0)=1, Asymptote, relativen Rest und ein exaktes skalares
Extremumsgegenbeispiel. Keine Rekonstruktion metronischer Operatoren oder
der F/G-Zuordnung; nur synthetische Parameter. `--write` erneuert nur
`05_analysis/exponential_context_diagnostics.json`. `--check` schreibt nichts.
12 neue Tests, einschliesslich separat nachgerechneter Endpunktrandfaelle;
Bericht `06_docs/EXPONENTIAL_CONTEXT_2026-09-06.md`.

## Fruehere Planung und Quellenimport

Hier kommen spaeter Import- und Analyse-Skripte hinein.

Geplante Skripte:

- `fetch_reference_data.ps1`: Referenzdatenquellen dokumentiert herunterladen, falls noetig.
- `extract_heim_tables.ps1`: Tabellen aus lokalen Heim-Dateien extrahieren, soweit technisch moeglich.
- `compare_masses.py`: Heim-Werte gegen PDG/NIST-Werte vergleichen.

Fuer neue Quellenimporte muessen Quellen und Dateiformate zuvor feststehen.
Der oben beschriebene eigene Alpha-Audit ist geprueft; Fremdprogramme und
Makros werden weiterhin nicht ausgefuehrt.
