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
py -3.13 scripts/validate_finding_register.py
py -3.13 -m unittest discover -s tests -q
```

Ohne lokale Fremd-PDFs `--verify-sources` weglassen. Die acht numerischen
Snapshots sind dann weiter pruefbar, die Quelldateien nicht. 98 Tests bestehen.

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
