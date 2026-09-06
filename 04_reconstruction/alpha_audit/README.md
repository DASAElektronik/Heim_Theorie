# Alpha-Audit

Isolierter, reproduzierbarer Konsistenztest der 1982/1989-Alpha-Bloecke in den
lokalen IGW-Wiedergaben. Python >= 3.10; nur Standardbibliothek erforderlich.

## Sechste Etappe: eigene Wellen-Schliessung (aktueller Stand)

```powershell
py -3.13 scripts/audit_wave_closure.py --check --verify-sources
py -3.13 -m unittest discover -s tests -q
```

69 Tests, davon13 neue. Skalares Ring-Randwertproblem und Phase-/Impuls-
identifikation sind eigene bedingte Diagnosen, keine Heim-H-Eigenloesung.
MS/Buch-A_k und Y/Y3 getrennt; alte Rechner/Inputs/Snapshots unveraendert.
`--write` erneuert nur `05_analysis/wave_closure_diagnostics.json`.
Report: `06_docs/WAVE_CLOSURE_2026-09-06.md`. Quellhashpruefung braucht
zusaetzlich H011-Manuskript und deBroglie1929-PDF; ohne PDFs nur `--check`.

## Fuenfte Etappe: Autorenbegruendung und Invarianz

```powershell
py -3.13 scripts/audit_lorentz_meaning.py --check --verify-sources
py -3.13 -m unittest discover -s tests -q
```

56 Tests insgesamt, davon12 neue exakte Bruchrechnungen. Standardboost,
statischer Kreis und source-literale p21-Matrix strikt getrennt. Keine
Rekonstruktion einer rotierenden Heim-Schale und keine Quellenkorrektur.
`--write` erneuert nur `05_analysis/lorentz_meaning_diagnostics.json`.
Warum-/Suchbericht: `06_docs/AUTHOR_RATIONALE_2026-09-06.md`.
Die Quellenoption benoetigt auch den lokalen Einstein1905-Referenzscan;
ohne PDFs ist die Rechnung mit `--check` weiterhin reproduzierbar.

## Vierte Etappe: Energie und Wellenlaenge

```powershell
py -3.13 scripts/audit_energy_kinematics.py --check --verify-sources
py -3.13 -m unittest discover -s tests -q
```

44 Tests insgesamt, davon11 neue fuer Kinematik. Eigene Vorwaertsdiagnosen
trennen Quellen-pc, T und zwei Wellenlaengen; keine physikalische Reparatur
oder empirische Kalibrierung. Der kleine Buchzweig verwendet direkt die
in Etappe3 geklaerte Buch-qk-Bruecke, nicht eine nach Zielwert gewaehlte
IGW-Lesart. Alte IGW-Profile bleiben unveraendert. `--write` erneuert nur
`05_analysis/energy_kinematics_diagnostics.json`.
Erklaerung: `06_docs/ENERGY_KINEMATICS_2026-09-06.md`.

## Ausfuehren

Im Projektordner:

```powershell
py -3.13 scripts/audit_alpha.py --check --verify-sources
py -3.13 scripts/audit_alpha_book.py --check
py -3.13 -m unittest discover -s tests -v
```

Auf anderen Systemen `python3` statt `py -3.13` verwenden. Ohne lokale PDFs
`--verify-sources` weglassen; die Rechnung bleibt aus versionierten Eingaben
reproduzierbar, die Quellkontrolle dann nicht. Keine PDF-Dateien sind im Git.

Nach einer bewusst geprueften Eingabe-/Codeaenderung:

```powershell
py -3.13 scripts/audit_alpha.py --write --verify-sources
```

`--check` schreibt nichts und meldet abweichende gespeicherte Ergebnisse als
Fehler. `--write` erneuert `05_analysis/alpha_audit_results.json`.
`compatible=False` bezeichnet widerspruechliche Quellzahlen; erfolgreich
nachgewiesene Widersprueche sind kein Softwarefehler und kein Grund fuer
nachtraegliches Anpassen der Formel.

## Dateien und Nachvollziehbarkeit

- `inputs.json`: Quellwerte als unveraenderte Dezimalstrings, PDF-SHA256,
  Varianten, pi-Profile und separater CODATA-Referenzwert.
- `MODEL_CARD.md`: Annahmen und Grenzen.
- `reviews/`: Quellen- und Mathematikgegenpruefung.
- `../../scripts/audit_alpha.py`: Rechner (Pfad relativ zum Projekt:
  `scripts/audit_alpha.py`).
- `../../05_analysis/alpha_audit_results.json`: maschinenlesbare Ergebnisse.
- `../../06_docs/ALPHA_AUDIT_2026-09-06.md`: lesbarer Ergebnisbericht.

Normalisierungen stehen in `../formula_library/normalization/decisions/`:
`NORM-ALPHA-AUDIT-SCOPE`, `NORM-1989-ALPHA-ETA-CROSSREF` und die dort
referenzierten bereits bestehenden Entscheidungen.

## Testumfang

Bekanntes Loesungspaar 0.6/0.8, doppelte Wurzel, ungueltiger Definitionsbereich,
sehr kleine Wurzeln, unabhaengige pi-Ziffern, Erhalt von Dezimalstellen,
nach aussen gerundete Intervallgrenzen, gedruckte Zweig-/Kehrwertwidersprueche,
80/120-Stellen-Konvergenz und keine Rueckwirkung geaenderter Messwerte auf
die Formel. Bei extrem kleinen R kann die grosse Wurzel auf 1 gerundet
werden; dieser Test beansprucht keine relative Genauigkeit ihrer verlorenen
kleinen Ergaenzung. Die hier geprueften Quellenwerte liegen fern davon.

## Zweite Etappe: Buchstruktur und Y3

`scripts/audit_alpha_book.py` rechnet Y3 aus expliziten Zielwerten zurueck
und untersucht numerische Ausloeschung. Das ist Diagnose/Kalibrierung, keine
Vorhersage. Buch-(105)-Struktur und bestehende IGW1982-eta-Profile werden
offen kombiniert; die Indexherleitung allein aus dem Buch bleibt unvollstaendig.
`--write` erneuert nur `05_analysis/alpha_book_diagnostics.json`.

Zum Abschluss der zweiten Etappe 23 Tests: 13 fuer den ersten Audit, 10 fuer die Diagnose, inklusive
unabhaengigem einfachen Inversionsfall, Extremum bei sqrt(2), Intervallen,
80/120-Stellen-Konvergenz und Regressionen aus der Mathematikreview.
Die Inversionshelfer verweigern Eingaben, deren Quadrat/Subtraktion nicht
exakt in die aktuelle Decimal-Praezision passt; Kontextpraezision erhoehen.

Bericht: `06_docs/BOOK_TRACE_2026-09-06.md`.
Eigene Varianten: `EXTENSION_CANDIDATES.md`.

## Dritte Etappe: Ladungsmittelung

```powershell
py -3.13 scripts/audit_charge_averaging.py --check --verify-sources
```

Rekonstruktion der vorlaeufigen BandI-Alpha-Naeherung plus ungefittete
Gewichtungsdiagnose. Keine modernen Referenzen und keine Y3-Kopplung.
Snapshot: `05_analysis/charge_averaging_diagnostics.json`; mit `--write`
bewusst erneuerbar. Zehn neue Tests, nun33 insgesamt.
Erklaerung: `06_docs/CHARGE_DERIVATION_2026-09-06.md`.
Quelle BandI erhaelt einen eigenen Hashcheck; alte Inputs/Snapshots bleiben
unveraendert. Buch-Indexbruecke jetzt geklaert, Energieordnungsfrage getrennt.

## Siebte Etappe: Befundregister und Tragweite

`FINDING_REGISTER.json` sammelt13 Befundgruppen mit Quellen, Voraussetzungen,
Reichweite, nicht belegten Schlussfolgerungen, Nachweisen und naechsten Checks.
Es ist keine Liste von13 Fehlern und kein vollstaendiger Theorie-Audit.
Positive Reproduktionen, Quellenbruecken und eigene Diagnosen sind enthalten.

```powershell
py -3.13 scripts/validate_finding_register.py
py -3.13 -m unittest discover -s tests -q
```

Der neue Validator prueft nur Metadatenintegritaet; die sechs vorhandenen
Rechner und Snapshots sind unveraendert. Quellen-/Ergebnisbilanz:
`06_docs/CYCLIC_FLOW_AND_FINDINGS_2026-09-06.md`.

## Achte Etappe: Konfigurationsauswahl (98a)

Neuer isolierter Rechner `scripts/audit_configuration_selection.py` mit
Snapshot, 9 neuen Tests und unabhaengiger Review. Alle 7 Snapshotchecks und
86 Tests bestehen; die alten 6 Rechner sind unveraendert. Neues Register:
16 Befundgruppen, einschliesslich positiver Begriffsbruecke, keine 16 Fehler.
`CONFIGURATION_DEPENDENCIES.md` verknuepft Definitionen, Annahmen, Folgen und
konkrete erneute Pruefanlaesse. Bericht `06_docs/CONFIGURATION_SELECTION_2026-09-06.md`.
