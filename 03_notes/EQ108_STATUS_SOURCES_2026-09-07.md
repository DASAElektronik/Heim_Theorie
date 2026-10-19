# Quellenumfang: Status von (108) und anschließende Ganzzahlauswahl

2026-09-07, Etappe 37. Keine neue Primärquelle importiert; keine
Originaldatei bearbeitet. [Ergebnisbericht](../06_docs/EQ108_STATUS_2026-09-07.md).

H004: Burkhard Heim, *Elementarstrukturen der Materie 2*, vorliegende
Ausgabe 1996. Lokale Datei:
`01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`.

SHA-256 am 2026-09-07 erneut geprüft:
`F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.
Der Hash belegt Dateiintegrität, keine historische Authentifizierung.

## Tatsächliche vollständige Originallektüre durch Root

| Druck / physische PDF-Seiten | Zusammenhang | Interne Arbeitsbilder |
|---|---|---|
| 322-330 / 328-336 | Näherung der Externzone, Proportionalität und Normierung, delta F_S=0, A-Heuristik, Resonanzanschluss,107a/b,108 | `tmp/pdfs/book_selection_source/edm2-328.png` bis `edm2-336.png` |
| 331-335 / 337-341 | F_im, Grenzwerte, Messbarkeitsbehauptung, A_im/A66, Y-Faktoren | `tmp/pdfs/a16_book/edm2-337.png` bis `edm2-341.png` |
| 340-342 / 346-348 | Anschluss110d, formale Gleichung, Exhaustion/TRC/Kappe/Transfer, empirischer F_S-Beginn | `tmp/pdfs/f16_constraints/edm2-346.png` bis `edm2-348.png` |
| 343-347 / 349-353 | F_S-Funktionsvorschlag/phi,112-Masse, heuristische Resonanzgrenzen113 bis113c | `tmp/pdfs/eq108_status/edm2-349.png` bis `edm2-353.png` |

Root hat alle 22 Seiten vollständig visuell gelesen; Druck 323 und342
wurden für die F_S-Abgrenzung zusätzlich erneut betrachtet. Druck321
wurde in dieser Etappe nur vom Quellenagenten erneut gelesen und ist
nicht in Roots neuem 22-Seiten-Umfang enthalten. Druck336-339 war kein
neuer Sichtumfang. Frühere Befunde dort werden nicht als neue Lektüre
ausgegeben.

Der PDF-Skill führte zur Kontrolle vollständiger Seiten samt Satzanschlüssen.
Vorhandene Renderings wurden wiederverwendet; der Downstream-Agent
renderte346-353 für seinen Review. Die PNGs sind ignorierte interne
Arbeitsbilder, keine neue PDF-Ausgabe und keine veröffentlichten
Abbildungen. OCR aus `tmp/pdfs/exponential_context/edm2.txt` diente
nur als Locator und wurde nicht als Formelautorität verwendet.

## Fundstellenbilanz

- S.322: Externverlauf unter der Näherungszuordnung zu79b/c.
- S.323: Delta-Normierung; `~` mit ausdrücklich folgendem
  Proportionalitätsfaktor, nicht als Toleranz gelesen; `delta F_S=0`
  in der Besetzungsvariation; normierte Gleichheit.
- S.324-325: heuristische Bestimmung des Abklingparameters und `W=g*w`.
- S.327/330: Resonanzfunktion `1+f(N)` und formale Gleichheit108;
  unbekannte Bestimmungsstücke bleiben eigens bezeichnet.
- S.331-335: nicht explizit deduzierte F_im und Grenzwertkoeffizienten;
  S.334 Messbarkeitsaussage nur für die Grenzwertsubstitution bei
  korrekt bestimmten Koeffizienten; S.335 heuristische empirische
  Reduktion und Y-Unsicherheitsfaktoren.
- S.340-342: festgelegte diskrete Vorschrift, aber keine ausgewiesene
  Bilanz/Toleranz des endgültigen108-Restes oder entsprechende W-Änderung.
  S.341 Messbarkeitsbezug betrifft die TRC-Neuner-Ausnahme.
- S.342-344: F_S aus Messmassen,17 verfügbare Punkte laut Quelle,
  vorgeschlagener Funktionsverlauf und Zusammenfassung112.
- S.345-347: heuristischer Grenzansatz,113b erneut mit Gleichheitszeichen;
  keine hier gefundene nachträgliche Restgarantie für108.

Insbesondere ist die vorhandene diskrete Auswahl nicht mit einer
bewiesenen metrischen Projektion oder Fehlerschranke gleichzusetzen.
Auch das Vorhandensein der internen Restgrößen W2-4 wird nicht bestritten.
Der Nichtfund betrifft den Anschluss der endgültigen Integerausgabe.

## Interne Gegenprüfungen und Zuschreibung

- `book_derivation`: vollständige Sicht Druck321-335, Einführung/Näherung.
- `alpha_versions`: vollständige Sicht Druck340-347 plus Rückanker323;
  eigener Review nach Rückfrage zum mehrdeutigen kleinen f auf343
  präzisiert. Dieses f wird nicht mit F_S/phi identifiziert und trägt
  keinen Teil des F_S-Aufhebungsarguments.
- `data_audit`: vorhandene Berichte und logische Reichweite; keine neue
  Originalsicht behauptet. Die übermittelte323-Prämisse ist im Review
  als solche gekennzeichnet und von Root am Original bestätigt.

Root las alle drei Reviews. Die zwei Quellenagenten und der Logikreview
sind interne Arbeitsteilung, kein unabhängiges externes Peer Review.

Heim zuzuschreiben sind Gleichung, Näherungsansätze, Normierung,
Auswahlalgorithmus und empirischer F_S-Vorschlag. Unser Beitrag ist die
Trennung ihrer Geltungsansprüche und der bedingte Schluss: Bei festem
Zustand und unverändertem restlichem Vertrag kann ein in der Variation
verschwindender additiver F_S-Term den108-Rest nicht korrigieren.

Nicht untersucht: volle physikalische Fehlerfortpflanzung, neue
Massenwerte, heutiger Messdatenvergleich, weitere Editionen oder Heims
Wissensstand am Lebensende. Die fehlende ausdrückliche Restbrücke ist
ein Nichtfund nur im dokumentierten Anschluss, keine Gesamtwiderlegung.
