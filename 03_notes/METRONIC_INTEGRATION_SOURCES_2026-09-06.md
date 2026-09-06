# Quellenumfang: metronische Integration, Etappe 20

2026-09-06. Keine neue Quelldatei importiert; H003 und H004 bleiben
getrennte Buchausgaben. Original-PDFs unveraendert, nur Leseansichten.

## Primaerdateien und Integritaet

- H003: `01_sources/heim_primary/Burkhard Heim - 1998 - Elementarstrukuren der Materie 1.pdf`
  (17,451,854 Bytes), SHA256
  `49C79028C4F5B4FEE97F0541EF1655C37755C3C3C2FD3A10DD6E72CB454DE459`.
  Ausgabe 1998; keine damit bewiesene wortgleiche Fassung von 1978/1980.
- H004: `01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`
  (21,429,782 Bytes), SHA256
  `F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.
  Ausgabe 1996, nicht still mit einem frueheren Formelblatt identifiziert.

Hashes in den bisherigen Quellpruefungen dieser Etappe erneut bestaetigt.
Abrufadressen im Quellenregister; kein neuer Bytevergleich eines Webmirrors.
Lokale PDFs, OCR und Lese-PNGs bleiben gitignoriert; Metadaten,
Eigenrechnung und begrenzte Notizen werden versioniert.

## Von Root bildlich gelesene tragende Vollseiten

| Quelle | Druck / PDF (PDF einbasiert) | Inhalt |
|---|---|---|
| H003 | 103 / 109 | M2: endliche Rueckwaertsdifferenz |
| H003 | 104 / 110 | M2a: inklusive Teleskopsumme und a-1 |
| H003 | 105 / 111 | M3a: korrigierte Produkt-/Quotientenregel |
| H003 | 109 / 115 | M7: delta_e=a*delta, explizite Naeherung |
| H003 | 110 / 116 | M8: endlicher dividierter Kettenquotient |
| H004 | 267 / 273 | (98), Ladungskomponenten und Potentialprodukt |
| H004 | 272 / 278 | Variationsgroessenordnung, X-Rekursion, Potentialstrich |
| H004 | 273 / 279 | gemischte delta/delta_e-Ansatze, z..z+1, lnY |
| H004 | 274 / 280 | Endpotentiale, Grenzkorrektur, vier Logargumente |
| H004 | 275 / 281 | A/B-Wahl, H/G-Formen und Fibonacci-Grenze |

Leseansichten: `tmp/pdfs/metronic_rules/edm1-109.png`, `-110.png`,
`-111.png`, `-115.png`, `-116.png`; H004
`tmp/pdfs/alpha3_book_origin/edm2-278.png` bis `edm2-281.png` sowie
`tmp/pdfs/correlation_chain/eq98-273.png`. II274 zusaetzlich hochaufgeloest
in `tmp/pdfs/metronic_potential/edm2-pdf280-print274.png` gegengelesen.
OCR war Suchhilfe, nicht die letzte Formelentscheidung.

## Gegenlesung und Grenzen

- `METRONIC_OPERATOR_SOURCE_REVIEW_2026-09-06.md`: book_derivation,
  H003 I102-111 und H004 II273-275. Exakte M2/M2a-Struktur von M7 trennen.
- `METRONIC_POTENTIAL_SOURCE_REVIEW_2026-09-06.md`: alpha_versions,
  vier Quotienten aus (98) und gesetzten Endpotentialen. Untergrenzenindex
  bleibt offen; rho nicht q. II274 druckt B'_1, unmittelbarer Kontext
  B1: keine lokal belegte Gleichsetzung oder bewiesene Fehlerursache.
- `METRONIC_MATH_REVIEW_2026-09-06.md`: data_audit, uebernommene
  Quellenlesung, eigenstaendige endliche Algebra und Logarithmusreihe;
  keine neue Glyphenentscheidung. Root fuehrte den Code separat aus.

Alle drei Reviews stehen unter `04_reconstruction/alpha_audit/reviews/`.
Die Wortlesung kleiner Variation liefert keine eingesetzte numerische
Fehlertoleranz. Es wird kein unbekannter Potentialpfad durch synthetische
Testwerte ersetzt. Der einzelne X-Rest ist nicht der gesamte H/G-Rest.

Eine enge externe Suche nach Metronintegral/M8 lieferte einen Mirror
desselben Band-I-Textes, keinen unabhaengigen Herleitungsbeleg. Tragende
Aussagen beruhen ausschliesslich auf den oben hashgeprueften lokalen
Primaerdateien und der ausgewiesenen eigenen Mathematik. Keine breite
Literaturrecherche, keine moderne empirische Gegenpruefung und kein
werkweiter Nichtexistenzbeweis fuer zusaetzliche Bedingungen.

Bericht: `06_docs/METRONIC_INTEGRATION_2026-09-06.md`.
