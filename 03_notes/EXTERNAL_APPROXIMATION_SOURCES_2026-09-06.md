# Quellenumfang: Externzonennaeherung, Etappe 33

2026-09-06. Primaerquelle H004: Burkhard Heim,
*Elementarstrukturen der Materie 2*, lokale Ausgabe 1996.

Datei: `01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`

SHA256: `F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`

## Neu gepruefte Vollseiten

Root las in dieser Etappe die kompletten gerenderten Originalseiten:

| Druckseite | Physische PDF-Seite (1-basiert) | Pruefzweck |
|---|---|---|
| 175-177 | 181-183 | (79), Feld-/Selektorpraefaktor, Parameter, Ausgangsform |
| 178-179 | 184-185 | (79b)/(79c), grosse-r-Annahmen, tau-/nu-Grenzen, verschiedene alpha-Rollen |
| 322-323 | 328-329 | Leerer Bezug, N_(j), Anwendung der Approximation, mu_+, Delta und W-Normierung |
| 324-325 | 330-331 | A(k), Geruest/g/w, heuristische Entscheidung z=5 statt z=3 |
| 326-327 | 332-333 | Resonanzgrundordnung und f(0), Abgrenzung gegen n_j=0 |
| 328-330 | 334-336 | Anschluss an Strukturbedingungen, (108)/(108a) |

Root-Renderpfade (lokale abgeleitete Hilfsdateien, keine neuen Quellen):
`tmp/pdfs/exponential_context/edm2-181.png` bis `edm2-185.png`;
`tmp/pdfs/book_selection_source/edm2-328.png` bis `edm2-336.png`.

Die Quellenreview las 175-179 und 322-324 eigenstaendig; die
Normierungsreview 322-330, 178-179 und zusaetzlich 277-278 / PDF 283-284.
Diese letzteren beiden Seiten wurden von Root hier nicht erneut gelesen;
ihre Eingabedefinitionen sind im frueheren Buchvertrag bereits geprueft.
(96b) wurde in dieser Etappe nur als auf S. 325 verwendeter Rueckverweis
erfasst, nicht an seiner urspruenglichen Stelle neu visuell geprueft.
Druck 178 wurde von Root nach einem Abschlussreviewhinweis nochmals
vollseitig gelesen: `alpha=lambda_(kl)/a=A` am Extremum, spaeter
Abklingexponent `alpha=a-lambda`. Die getrennten Rollen sind im Bericht
explizit; kein Notationshinweis ersetzt den Blick auf die Originalzeile.

## Positive Belege und enger Nichtfund

- Belegt: explizite Verwendung der (79b)/(79c)-Form in der aeusseren Zone;
  `Delta=mu_+*(exp(-A*N4)-1)`, Wahl `mu_+*W=delta M+Delta`;
  `alpha4=delta4G4=1`, Geruestsumme g und W/g=w.
- Belegt: A(2)=1/15 nach Geruestansatz, Teilerkandidaten z=1,3,5 und
  ausdruecklich heuristische Wahl z=5. Druck 325 verbindet xi mit dem
  Grenzverlauf der (+7)-Feldnaeherung (79b)/(79c) und nennt
  (2xi-1)^2=5/(96b); dieser gedruckte Zusammenhang ist noch kein neuer
  quantitativer Nachweis der benoetigten Fehlerbruecke.
- Wortlautabweichung: der z=1-Ausschlusssatz nennt identisches Q4*A,
  waehrend nach seinen Werten nur A identisch waere. Strikte A-Ordnung
  separat belegt; kein autorisiertes Erratum angenommen.
- Nicht gefunden im genannten Umfang: quantitatives r-/nu-zu-N4-Gesetz,
  Uebertragung des vollen Feldpraefaktors/der Parameter und ein numerisches
  Fehlerbudget fuer Nullpunkt, Geruest und Besetzung gemeinsam.

Die eigene skalare Restschranke der Etappe 9 wurde vorab abgeglichen
(`EXPONENTIAL_CONTEXT` und damalige Quellenreview). Sie ist keine neue
Entdeckung und keine bereits geschlossene physikalische N4-Fehlerschranke.

Ein Abrufversuch des bekannten PDF-Spiegels
`https://heim-theory.com/wp-content/uploads/2025/10/RH2-Elementarstrukuren_Materie_2.pdf`
lieferte lediglich die Werkzeuggrenze fuer die 21.429.782-Byte-Datei.
Dessen Inhalt wurde dadurch nicht unabhaengig online bestaetigt. Keine
neue Quelle importiert, keine Originaldatei veraendert und keine breite
Recherche nach neueren Widerlegungen vorgenommen.

## Zuschreibung und Eigenanteil

Quellenform, Referenzbildung und heuristischer A-Ansatz sind Heims
veroeffentlichte Arbeit. Die generische Ersatzfunktion Phi, Dreipunkt-
Fehleridentitaet, Robustheitsbedingung, synthetischen Zeugen und rationale
Kontrollsoftware stammen aus unserer Untersuchung. Sie sind keine
behauptete Rekonstruktion fehlender metronischer Dynamik.

Die bisher hashgebundenen Buchinputs und 49 CSV-Normalisierungszeilen
bleiben unveraendert. Kein moderner Referenzwert, keine neue Masse, kein
Y9-/A-/Restfit. Kein Urteil ueber den gesamten Lebensendstand des Autors.

Bericht: [EXTERNAL_APPROXIMATION](../06_docs/EXTERNAL_APPROXIMATION_2026-09-06.md).
Interne Reviews unter `04_reconstruction/alpha_audit/reviews/`:

- `EXTERNAL_APPROXIMATION_SOURCE_REVIEW_2026-09-06.md`
- `EXTERNAL_NORMALIZATION_REVIEW_2026-09-06.md`
- `EXTERNAL_ERROR_TRANSPORT_REVIEW_2026-09-06.md`
