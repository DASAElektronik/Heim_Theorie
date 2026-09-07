# Historische Exponenten: Quellen- und Kontrollumfang

2026-09-06, Etappe 23. Ausgang `57e92f8`, Plan `125da3a`.
Keine neue Quelle importiert, keine Quell-PDF geaendert.

## H006: IGW-Wiedergabe

- Titel: Die Massenformel nach Burkhard Heim (1982).
- Verantwortungsangabe des Titelblatts: Forschungskreis Heimsche Theorie,
  IGW Innsbruck, 2002; Seitenkoepfe 2003. Schluss: gez. (Heim), 25.2.1982.
- Lokal: `01_sources/heim_primary/Massenformel_nach_B_Heim_1982.pdf`.
- Fundstelle: https://burkhardheim.de/assets/Massenformel_nach_B_Heim_1982.pdf
- SHA256 erneut geprueft:
  `F74DA0DAC8496BCD01226F54D88598152D67E1C954943AF61D0EC1811F5527BE`.
- Root: Vollseiten Druck/PDF1,6,8,9,10. XIV ungruppiert; XV,XXVI,
  XXVII,XXIX,XXX,XXXI,XXXV gruppiert. XXXIV ist kein Exponentialterm.
- Arbeitsbilder: `tmp/pdfs/n0_alias/h006-01.png`, `-06.png`, `-08.png`,
  `-09.png`; `tmp/pdfs/historical_exponent/h006-p8-600.png`,
  `h006-end-10.png`. Root zusaetzlich direkter Poppler-Detailrender
  `h006-p8-repeat-detail.png` fuer die kleinen XXVII/XXIX-Klammern.
  Poppler meldet fehlenden Display-Font Symbol; die entscheidenden
  lateinischen Klammern sind sichtbar. Keine unklare Glyphe aus OCR ergaenzt.

## H015: fotografierter Typoskriptausschnitt

- Archivtitel: 1982 Heim DESY sortiert OCR; 43 PDF-Seiten.
- Lokal: `01_sources/heim_primary/alpha3_origin/Heim_DESY_1982_Archivscan.pdf`.
- Fundstelle: https://burkhardheim.de/media/f/c57c27a0-3692-5fae-920d-5ba89ad58349
- SHA256 erneut geprueft:
  `C242599F7AAF68BB8E2F3C7756A24687E86FAD879E4D0E22C00585A32403317F`.
- Root: Vollseiten PDF39/Blatt4, PDF41/Blatt5, PDF42/Blatt6, PDF43/Blatt7.
  Quellenagent zusaetzlich PDF40/Blatt4a (Anmerkung zur Strukturpotenz).
- Bilder: `tmp/pdfs/alpha3_origin/desy-39.png`, `-41.png`, `-42.png`,
  `-43.png`; Agent zusaetzlich `-40.png`. Keine automatische Ableitung
  der Blattnummer aus der PDF-Position; untere Ziffern sind Fortsetzungsvermerke.
- Auf Blatt7 Datum25.2.1982, Signaturabbildung, (Heim), Verteiler.
  Heutige OCR-/PDF-Metadaten datieren die Digitalisierung, keine
  forensische Echtheitspruefung und kein Programm-Replay.
- Keine roemischen H006-Formelnummern auf diesen Typoskriptseiten.
  Nur der relevante Exponent und sein Anschluss werden verglichen,
  nicht die Gleichheit des vollstaendigen Dokuments behauptet.

## Unabhaengige Kontrollen und Suchgrenzen

Reviews in `04_reconstruction/alpha_audit/reviews/`:

- `HISTORICAL_EXPONENT_ARCHIVE_REVIEW_2026-09-06.md`;
- `HISTORICAL_EXPONENT_REPRINT_REVIEW_2026-09-06.md`;
- `HISTORICAL_EXPONENT_MATH_REVIEW_2026-09-06.md`.

Eine vorlaeufige H006-XIV-Umklammerung in einer Agentennachricht wurde
an der Originalzeichenfolge korrigiert. Root-Kleinbildunsicherheit bei
XXVII/XXIX wurde durch hohe Aufloesung geklaert: beide sind gruppiert.
Beides ist vor dem Befundnachtrag bereinigt, keine neue Quellenvariante.

Websuche nach Massenformel_nach_B_Heim_1982/Korrekturen und 1982 Heim DESY
bestaetigt den bereits bekannten Medienarchiveintrag
https://burkhardheim.de/media . Kein neues Erratum daraus gewonnen.
Allgemeine Medien-/Sekundaerberichte zu Massentreffern nicht verwendet.
Kein Kontakt mit Herausgebern, kein neuer Fremdprogrammlauf.

Root hat den gesamten unabhaengigen Python-Codeblock gelesen und erneut
ausgefuehrt. Sieben neue Fraction-Tests, 185 Gesamttests und zehn alte
Snapshot-/Quellchecks bestanden; Registerpruefung ist nur Metadatenkontrolle.
