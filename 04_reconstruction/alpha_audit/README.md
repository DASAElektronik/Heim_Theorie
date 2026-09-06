# Alpha-Audit

Isolierter, reproduzierbarer Konsistenztest der 1982/1989-Alpha-Bloecke in den
lokalen IGW-Wiedergaben. Python >= 3.10; nur Standardbibliothek erforderlich.

## Etappe 28: F16-Bedingungen und begrenzte Bestimmtheit (aktueller Stand)

`06_docs/F16_DETERMINACY_2026-09-06.md`: Rolle und Grenzforderung,
aber kein explizites F16-Randwertproblem in den geprueften Seiten.
Einfuehrung2-3/110d bestaetigen den offenen Herleitungsauftrag. Formel
mitfixemY9 berechenbar; eigene skalare Zeugen keine Heim-Loesungen.
(108) bestimmt A16 bedingt bei unabhaengigenT108,g,d,f; keine Fitwerte.
DreiReviews,10neueTests,234gesamt,elfalteChecks. FIND-038,38Gruppen,
nicht38Fehler. Alte Rechner/Inputs/Snapshots/49CSV erhalten.
NaechsterAuftrag Buch340-342Exhaustion getrennt vonH006/H015, keineMasse.

## Etappe 27: A16-Klammerung und heuristische Buchherkunft (vorheriger Stand)

`06_docs/A16_ORIGIN_2026-09-06.md`: H015GINIT und H004(109b) belegen
/(5eta), H004 zusaetzlich Y9 am ganzen Ausdruck. F16-Grenzwertrolle und
heuristische Koeffizientenermittlung explizit, keine vollstaendige Herleitung.
TabellenY=1 getrennt; kein neuer Fit. Drei Reviews und zehn neue exakteTests,
224gesamt,elfalteChecks bestanden. FIND-037;37Gruppen,nicht37Fehler.
Alte Rechner/Inputs/Snapshots/49CSV-Normalisierungen unveraendert.
NaechsterAuftrag F16/A16-Bestimmtheit aus konkreten Quellenbedingungen.

## Etappe 26: H006-x3/mu--Auswahl ohne Masse (vorheriger Stand)

`06_docs/MUON_SELECTION_2026-09-06.md`: Komponenten, W=g(1+d*A16),
zwoelf vorab benannte Profile und erreichten(b)-Zweig quellengebunden
geprueft. Alle K1..3=(14,9,3); A16-Slashbindung entscheidet zwischen
K4=0 und1, beide mit positivem Rest. Keine neue Masse oder Fitwahl.
`NORM-MUON-SELECTION-AUDIT.md`, neuerInput/Rechner/Snapshot, drei Reviews.
15neueTests,214gesamt,elfChecks; alle alten Rechner/Inputs/Snapshots und
49CSV-Normalisierungen erhalten. FIND-036;36Gruppen,nicht36Fehler.
NaechsterSchritt A16-Fassung/Herleitung in H015/Buch gegen explizite
spaetereH010-Klammer /(5eta). KeineAuswahl nach kleinerem Rest.

## Etappe 25: W4-Sonderfaelle und K4-Ganzzahlrest (vorheriger Stand)

`06_docs/K4_W4_SELECTION_2026-09-06.md` prueft die drei W4-Faelle und
die Ganzzahlregel gegen die gruppierte Restgleichung. H006/H015 visuell
getrennt gelesen; drei K4_W4*-Reviews. Unter festem W3/a ist die Vorschrift
nicht allgemein exaktloesend. Zaehldeutung und physikalische Erreichbarkeit
bleiben getrennt; eigene Testwerte sind keine Heim-Teilcheninputs.
FIND-035, jetzt 35 Befundgruppen; 14 neue Fraction-/Intervalltests,
199 insgesamt und zehn alte Rechen-/Quellchecks bestanden. Alte Rechner,
Inputs, Snapshots und CSV-Normalisierungen erhalten. Naechster Kandidat:
H006x3/mu-,N0, Eingabe-/Auswahlvertrag ohne Masse.

## Etappe 24: Verstaendnis- und Versionsbilanz (vorheriger Stand)

`06_docs/UNDERSTANDING_BALANCE_STAGE24_2026-09-06.md` fasst Etappen 16-23
zusammen; drei BALANCE24*-Reviews ordnen begrenzte Fassungsbruecken,
alle 34 Befundgruppen und den naechsten Einzelauftrag ein. Keine neuen IDs,
Rechner oder Profile. Zehn alte Rechen-/Quellchecks und 185 Tests bestehen;
auch Register/Normalisierungen bleiben unveraendert. Quellenanschluss,
Normalisierung, Rechnung, physikalische Herleitung und Empirie getrennt.
Naechster Schritt: H006p9-W4/K4-Faelle und Ganzzahlregel auf Erhalt der
Restgleichung und Strukturbedingungen pruefen; H015PDF42 separat daneben.
Noch kein weiterer Massenfall, keine still geaenderte Formel.

## Etappe 23: historischer Exponentenvergleich (vorheriger Stand)

`06_docs/HISTORICAL_EXPONENTS_2026-09-06.md` vergleicht die H015-Typoskript-
Exponenten mit H006. Die gruppierte Form steht in H015 durchgehend und
in H006s benachbarten Wiederholungen; nur XIV weicht in dieser Kette ab.
FIND-027 wird auf die belegte Wiedergabe eingegrenzt, nicht neu gezaehlt.
Zwei Quellenreviews, unabhaengige Algebrareview, sieben neue Tests;
185 insgesamt und zehn alte Snapshot-/Quellchecks bestanden.
Alle alten Rechenprofile erhalten. Naechster Schritt: Verstaendnisbilanz
Etappen16-23, keine erneute Massenrechnung oder stille Mischfassung.

## Etappe 22: Potentialkomponenten und getrennte Kanaele (vorheriger Stand)

`06_docs/POTENTIAL_PATHS_2026-09-06.md` grenzt die gemeinsame unveraenderte
Komponentenkurve als Zusatzlesart aus. H004s getrennte, teils gewichtete
Integrationskanaele bleiben davon unberuehrt; konkrete Zwischenpfade offen.
DreiPOTENTIAL_PATH*-Reviews und zehn neue exakte Tests,178gesamt;
zehn alte Rechen-/Quellchecks. FIND-034/34Befundgruppen, keine34Fehler.
Naechster unabhaengiger Quellenanker:H015PDF39/41 gegenH006XIV/XXVI.
Alle alten Rechner/Inputs/Snapshots und49Normalisierungen erhalten.

## Etappe 21: skalierter metronischer Schritt (vorheriger Stand)

`06_docs/METRONIC_STEP_2026-09-06.md` trennt M7s gedruckten inneren
Argumentshift von a*delta auf nichtlinearen Folgen. H004s gemischte
H/G-Gleichung ist bedingt als endliche Rekurrenz und gemeinsamer Logrest
formuliert; keine authentische Theoriereparatur oder Massenfortpflanzung.
DreiMETRONIC_STEP*-Reviews, zehn neueTests,168gesamt und zehnalteChecks.
FIND-033/33Befundgruppen, keine33Fehler. NaechsterAnker:(98)-Potentialpfade
und gemeinsame Parametrisierung bei festemk; alteRechenprofile erhalten.

## Etappe 20: metronische Integration (vorheriger Stand)

`06_docs/METRONIC_INTEGRATION_2026-09-06.md` erklaert M2a/lnY exakt
und vier Potentialquotienten bedingt. M7 ist approximativ; unter M2
macht grosses Fibonacci-z den Logaustausch nicht beliebig genau.
FIND-032/32Befundgruppen, kein berechneter Massenfehler. Drei begrenzte
Reviews und14 neue Tests mit rationalen Logintervallen;158gesamt,
zehn alte Snapshot-/Quellchecks. Delta/delta_e-Wirkung und gemeinsame
H/G-Fehlerbilanz offen; alte Rechner/Inputs/Snapshots unveraendert.

## Etappe 19: alpha3-Bestimmtheit (vorheriger Stand)

`06_docs/ALPHA3_ASSUMPTIONS_2026-09-06.md` zeigt verbleibende lokale
Koeffizientenfreiheit unter expliziten Voraussetzungen. Zwei begrenzte
Reviews und elf neue Tests; 144 insgesamt, zehn alte Snapshotchecks.
FIND-031/31 Befundgruppen, keine globale Fitparameterzaehlung oder
Gesamtwiderlegung. Alle alten Rechner/Inputs/Snapshots bleiben erhalten.

## Etappe 18: alpha3-Herkunft (vorheriger Stand)

H004II275/278(98c) und H015FORTRAN/GBASE/PDF22 tragen beide H010-Terme.
Die Buchkoeffizienten sind ausdruecklich empirisch gewaehlt; die letzte
Algebra stimmt unter diesen Voraussetzungen. Drei ALPHA3*-Reviews und
`tests/test_alpha3_origin.py` sichern Quelle/Umformungen, keine neuen Massen.
Bericht `06_docs/ALPHA3_ORIGIN_2026-09-06.md`; FIND-030/30 Befundgruppen,
zehn unveraenderte Snapshotchecks und 133 Tests. Alte Profile nicht ersetzt.

## Etappe 17: historischer Vergleich (vorheriger Stand)

`historical_n0_inputs.json` und `NORM-HISTORICAL-N0-COMPARISON.md` frieren
sechs Formel-/Inputachsen vor der Rechnung ein. 64 Gegenfaktorkombinationen
plus eine alternative Wurzelreichweite, unabhaengig kontrolliert.
H010-Ausgabewert bedingt reproduziert; alpha3-Potenzklammer dominiert die
Abweichung vom H006-Ausgangspunkt. Keine Formelwahl nach Massentreffer.
Zehn Snapshotchecks und 127 Tests; FIND-029 ist eine weitere Befundgruppe,
keine neue Gesamtwiderlegung. Bericht `06_docs/HISTORICAL_N0_2026-09-06.md`.
Die alte H006-Rechnung bleibt erhalten, ihre Wurzellesart ist nachgetragen.

## Etappe 16: begrenzter H006-N0-Fall (vorheriger Stand)

`06_docs/N0_ELECTRON_2026-09-06.md` beschreibt den jetzt ausfuehrbaren
N=0-Pfad fuer die vorgegebene Elektronkomponente. Eingaben:
`n0_electron_inputs.json`, Normalisierung `NORM-N0-ELECTRON-AUDIT.md`.
Neun Snapshots, 111 Tests, 28 Befundgruppen einschliesslich positiver
Rekonstruktionen. Kein Gesamtspektrumrechner, keine moderne Massenvalidierung.
Die historischen Test-/Befundzahlen unten bleiben als Verlauf erhalten.

## Neunte Etappe: Exponentialkontext (Verlauf)

`06_docs/EXPONENTIAL_CONTEXT_2026-09-06.md` erklaert die Rueckverweise
(79)/(79a), die bedingt reproduzierte Rate, den relativen Naeherungsfehler
und die weiterhin offene F/G-Zuordnung. `audit_exponential_context.py`
ist ausdruecklich eine normalisierte skalare Diagnose, keine metronische
Operatorrekonstruktion. 98 Tests, acht reproduzierbare Snapshots;
vollstaendige Befehlsliste in `scripts/README.md`. 18 Registergruppen
einschliesslich positiver Befunde, keine Fehlerzaehlung.

## Sechste Etappe: eigene Wellen-Schliessung (Verlauf)

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
