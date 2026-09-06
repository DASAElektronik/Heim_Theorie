# Skripte

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
py -3.13 scripts/validate_finding_register.py
py -3.13 -m unittest discover -s tests -q
```

Ohne lokale Fremdquellen `--verify-sources` weglassen. Die zehn numerischen
Snapshots sind dann weiter pruefbar, die Quelldateien nicht. 144 Tests bestehen.

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
