# Skripte

## Implementiert: Alpha-Audit (2026-09-06)

`audit_alpha.py` berechnet den isolierten 1982/1989-Konsistenz-Audit mit der
Python-Standardbibliothek. `py -3.13 scripts/audit_alpha.py --check --verify-sources`
prueft gespeicherte Ergebnisse und lokale PDF-Hashes.
`py -3.13 -m unittest discover -s tests -v` fuehrt die Tests aus.
Details: `04_reconstruction/alpha_audit/README.md`.

## Fruehere Planung und Quellenimport

Hier kommen spaeter Import- und Analyse-Skripte hinein.

Geplante Skripte:

- `fetch_reference_data.ps1`: Referenzdatenquellen dokumentiert herunterladen, falls noetig.
- `extract_heim_tables.ps1`: Tabellen aus lokalen Heim-Dateien extrahieren, soweit technisch moeglich.
- `compare_masses.py`: Heim-Werte gegen PDG/NIST-Werte vergleichen.

Fuer neue Quellenimporte muessen Quellen und Dateiformate zuvor feststehen.
Der oben beschriebene eigene Alpha-Audit ist geprueft; Fremdprogramme und
Makros werden weiterhin nicht ausgefuehrt.
