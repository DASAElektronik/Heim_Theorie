# Quellenumfang: Massenformelkette (98d/e) bis (112)

2026-09-07, Etappe38. [Bericht](../06_docs/MASS_CHAIN_2026-09-07.md).
Keine neue Primärquelle importiert, kein Original geändert.

H004: Burkhard Heim, *Elementarstrukturen der Materie 2*, Ausgabe1996.
Lokale Datei:
`01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`.
SHA-256 erneut am2026-09-07 geprüft:
`F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.
Der Hash belegt Dateiintegrität, keine historische Authentifizierung.

## Root: vollständig visuell gelesene Seiten

| Druck / physische PDF-Seite | Geprüfter Inhalt | Arbeitsbilder |
|---|---|---|
| 253 /259 | (97), mu-Skalen, additiver Massenansatz und Kontext | `tmp/pdfs/book_pseudosinglet_input/edm2-259.png` |
| 276-278 /282-284 | Alpha-/Strukturkontext,98b-Besetzungen,98c-Koeffizienten,98d/e-Masse, explizite Unvollständigkeit danach | `tmp/pdfs/alpha3_book_origin/edm2-282.png` bis `edm2-284.png` |
| 323 /329 | F_S unabhängig von der betrachteten n-Variation | `tmp/pdfs/book_selection_source/edm2-329.png` |
| 342-344 /348-350 | empirische F_S-Extraktion und17 Punkte,111 und Hilfsfunktionen, K/F/H-Zerlegung,112, anschließende Spektrumsgrenzenfrage | `tmp/pdfs/eq108_status/edm2-348.png` bis `edm2-350.png`; zusätzlich `tmp/pdfs/mass_chain/edm2-350.png` |

Das sind acht vollständig gelesene Seiten. Die zunächst grob verortete
(97) wurde per OCR gezielt auf253 gefunden und am ganzen Original gelesen.
Druck323 wurde als konkreter F_S-Rückanker nochmals geprüft. Root las
in dieser Etappe nicht zusätzlich275/279; diese Seiten gehören zur
weiteren Sicht der Quellenagenten, nicht zu Roots Umfang.

Nach der Vollsicht wurden zwei eigene Detailrenderings ausgewertet:
`tmp/pdfs/mass_chain/root-k-detail.png` (344/112a) und
`tmp/pdfs/mass_chain/root-b-detail.png` (342/B_v). Beide dienen nur zur
Glyphenabsicherung. Die vollständigen Seiten und Satzanschlüsse blieben
maßgeblich. PNGs sind ignorierte interne Arbeitskopien, keine neue PDF
oder zur Veröffentlichung bereitgestellten Abbildungen.

## Zwei verworfene Lesehypothesen

1. Root vermutete zunächst im unteren K-Term auf344 einen Faktor2 statt3.
   Zwei Quellenagenten und Roots eigener hochaufgelöster Ausschnitt
   bestätigten jedoch beide K-Zeilen mit `3*Q2`. Der Plan hält den
   ursprünglichen Verdacht historisch fest; er ist kein Fehlerbefund.
2. Ein erster interner F_S-Review las auf342 bei B_v einen Exponenten
   `kappa-2`. Roots Detailbild zeigt eindeutig nur `-2`. Der Review
   wurde nach Gegenprüfung korrigiert; keine Versionsdifferenz oder
   neue Relation `Y44=xi^kappa` wird daraus abgeleitet.

Damit beeinflusste der PDF-Skill die Schlussfolgerung materiell: Die
vollständige Seitenkontrolle mit gezielten Vergrößerungen verhinderte,
Leseartefakte als Quellenfehler festzuhalten. Die Originale wurden nicht
durch OCR-Zeichenfolgen oder algebraische Erwartungen ersetzt.

## Interne Arbeitsteilung

- `book_derivation`: eigene Vollsicht253,275-279,342-344, Transkription
  und Algebraanschluss; lokale Nachprüfung der B_v-Ziffer.
- `alpha_versions`: eigene Vollsicht253,276-279,323,342-344;
  F_S-Provenienz, Hilfsfunktionen/Y-Faktoren und Empiriestatus.
- `data_audit`: transparente Algebra aus übermittelten Formeln,
  ohne behauptete eigene Originalsicht; selbstenthaltener exakter Block.

Root las alle drei neuen Reviews, prüfte tragende Originalformeln selbst
und führte den Algebrablock erneut aus. Der neue Testcode prüft dieselben
Identitäten über Polynom-Multiplikation plus synthetische rationale Fälle.
Kein externer Gutachter und keine unabhängige experimentelle Bestätigung.

Heim zuzuschreiben sind97/98/111/112, die Zerlegung und der empirische
Funktionsansatz. Eigener Anteil: Notationsentflechtung, expliziter
Identitätsvergleich, synthetische Kontrollfälle und Quellenstatusbilanz.
Nicht geprüft sind tatsächliche17 Massendaten, vollständige metronische
Deduktion, neue Teilchenwerte, alle Editionen oder heutige Messdaten.
