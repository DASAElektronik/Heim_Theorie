# Quellenumfang der alpha3-Bestimmtheitspruefung

2026-09-06, Etappe19. Keine neue empirische Referenz oder Massenanpassung.

## H004: tragender Buchbeleg

Lokale Quelle: `01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`.
SHA256: `F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.
Hash erneut mit den alten Rechenchecks verifiziert. Unveraenderte Ausgabe1996;
keine neue Datierungs- oder Authentifizierungsbehauptung.

Root visuell vollstaendig gelesen: Druck271-275/PDF277-281, vorhandene
Leseansichten `tmp/pdfs/alpha3_book_origin/edm2-277.png` bis `edm2-281.png`.
Quellenagent zusaetzlich Druck270 und Abschluss(98c) Druck278, insgesamt
bereits gerenderte Druck270-278 visuell erfasst. Relevante Lesespur:

- Druck271/272: induktiver alpha3-Ansatz, f(1), zusaetzliche funktionale Bedingung.
- Druck272/273: Koeffizienten nur von k abhaengig; additive Logvariationen;
  X-Rekursion und Y-Verhaeltnis; gewaehlte Grenzen der Metronintegrale.
- Druck273/274: empirisch/induktiv motivierte untere Potentialgrenzen;
  obere H-Grenze, spekulative G-Identifikation, Sigma-Anschluss fuer C_k;
  untere Grenzkorrektur als spezielle metronische Regel, nicht neu validiert.
- Druck274/275: allgemeine Logformen und ausdruecklich frei vorgebbare,
  empirisch gewaehlte A/B-Koeffizienten; Y=xi^2 als Grenzregime.

Keine Vollwerk-Suche nach Nichtvorhandensein weiterer Randbedingungen.
Die mathematische Review benutzt diese Quellenlesung als Voraussetzung;
sie ist keine zweite neue Glyphenpruefung. Root und Quellenagent lesen
die Quelle, Root und Mathematikagent pruefen die Algebra unabhaengig.

## Eng begrenzte externe Archivpruefung

Die aktuelle [Archivseite](https://heim-theory.com/archiv/) fuehrt das Buch
als Ausgabe1996 und bietet den Link
`https://heim-theory.com/wp-content/uploads/2025/10/RH2-Elementarstrukuren_Materie_2.pdf`.
Der PDF-Abruf im Webwerkzeug scheiterte am Groessenlimit (21429782 Byte
laut Antwort). Diese verlinkte Datei wurde in dieser Etappe NICHT lokal
geladen oder gehasht; keine Bytegleichheit mit H004 behauptet. Der
Sachbefund beruht auf dem vorhandenen hashgeprueften Buchscan, nicht auf
der heutigen redaktionellen Archivbeschreibung. Keine neue Quellen-ID.
Weitere moderne Arbeiten auf der Archivseite nicht fachlich bewertet.

## Eigene Diagnosen und Geltungsgrenzen

Allgemeine Grenzformeln behandeln positive reelle Variablen bei festem k,
nicht eine bereits bewiesene Familie physikalischer q,k-Konfigurationen.
Die rationalen H/G-Anker sind kuenstlich und nicht aus Messwerten gewaehlt.
Alternative Exponenten dienen nur als Nicht-Eindeutigkeitszeugen unter
den jeweils genannten Bedingungen. Keine alternativen Teilchenloesungen,
keine globale Parameterzaehlung, kein Fit- oder Taeuschungsnachweis.

Zwei neue Reviews in `04_reconstruction/alpha_audit/reviews/`:
`ALPHA3_ASSUMPTIONS_SOURCE_REVIEW_2026-09-06.md` und
`ALPHA3_ASSUMPTIONS_MATH_REVIEW_2026-09-06.md`.
Eigene neue Tests: `tests/test_alpha3_assumptions.py`.
