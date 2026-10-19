# Quellenreview: H-Kreiswelle und moeglicher Randwertschluss

Stand 2026-09-06. Begrenzte Quellenlesung dazu, ob die in EDM2 verwendete
H-Kreiswelle als Randwertproblem rekonstruiert werden kann, ohne einen
zusaetzlichen Ansatz einzufuehren. Dies ist keine eigene Ringrechnung und
keine Aussage ueber die physikalische Geltung der Annahmen.

## Ergebnis in einem Satz

EDM2 setzt die einfache Schliessung **explizit**: `lambda_H = 2 pi r_H`.
Die Quelle nennt die so charakterisierte Elektronenwelle stehend und ordnet
ihr die gesamte Kugeloberflaeche des H-Grundzustands als `s`-Niveau zu.
Sie liefert in der geprueften Kette aber keine Wellenfunktion,
Differentialgleichung, Periodizitaets-/Phasenrandbedingung oder ganzzahlige
Kreiswindung, aus der diese Schliessung abgeleitet wuerde. Daher kann man
die Ein-Wellenlaengen-Schliessung als eine **Buchannahme bzw. eingesetzte
Quantendualismus-Relation** verfolgen, nicht als bereits ausgeschriebenes
Eigenwertproblem rekonstruieren.

## Visuell kontrollierte Quellanker

| Quelle | Buchseite / PDF-Folio | Befund und Status |
|---|---:|---|
| EDM2, S. 161 / PDF 168 | 161 / 168 | Im allgemeinen Synmetronik-Kontext definiert Heim fuer einen zyklischen Kondensorfluss eine Eigenfrequenz und `lambda = w_f / eta`; anschliessend nennt er den **empirischen** Quantendualismus `m c lambda = h` und die Aequivalenz von Korpuskel- und Wellenbild. Das ist eine allgemeine Deutung, keine H-Kreis-Randbedingung. |
| EDM2, S. 256--257 / PDF 262--263 | 256--257 / 262--263 | Die Seiten behandeln kanonisch konjugierte Groessen, Selektoren und metronische Integrationen. S. 257 verwendet natuerliche ganze Zahlen fuer metronische Integrationsbereiche. Der Kontext liefert keinen Text, der diese Zahlen einer Umfangswindung der H-Elektronenwelle gleichsetzt. |
| EDM2, S. 276 / PDF 282 | 276 / 282 | Heim beschreibt den Grundzustand des H-Atoms als elektrostationaere Wechselbeziehung von Proton und Elektron, das als `s`-Term auf der K-Schale aufgefasst werde. Als Begruendung einer Strukturveraenderung sagt er dann, das Elektron duerfe im p-Feld nicht nur korpuskular, sondern **im dualen Bild als zirkulaere Elektronenwelle der Laenge** `lambda_H = 2 pi r_H` aufgefasst werden, wenn `r_H` der Radius des H-Grundzustands sei. **Explizite Setzung**, nicht an dieser Stelle hergeleitet. |
| EDM2, S. 277 / PDF 283 | 277 / 283 | Der Satz wird fortgesetzt: „Diese stehende Elektronenwelle bestimmt aber die gesamte Oberflaeche `4 pi r_H^2` dieses Grundzustandes als s-Niveau.“ Danach folgt die behauptete strukturelle Rueckwirkung. **Explizite Modellzuordnung**; keine Randbedingung oder Wellenloesung wird angegeben. |
| EDM2, S. 297 / PDF 303 | 297 / 303 | Wiederholt fuer das H-Atom: e- besetzt den stabilen Grundzustand eines `s`-Terms auf der K-Schale; die vorherige phenomenologische Annahme unveraenderter Internstruktur sei wegen Quantendualismus und `lambda_p << lambda_e` nicht haltbar, weil das Elektron als zirkulaere Elektronenwelle die ganze Oberflaeche der K-Schale bestimme. **Annahme/Modellmechanismus.** |
| EDM2, S. 300 / PDF 306 | 300 / 306 | Bezeichnet `E_k` als kinetische Energie des korpuskular aufgefassten e- im s-Niveau; dann werden R6/R3-Approximation und `v_H = c alpha` eingefuehrt. Die Seite fuegt keine Kreis- oder Phasenbedingung hinzu. |
| EDM2, S. 301 / PDF 307 | 301 / 307 | Nennt `s_H = 2 pi r_H` die Laenge eines K-Schalenmeridians. Direkt danach identifiziert Heim `m c^2` als Energiequant `h nu_H = c h / lambda_H` der zirkulaeren Elektronenwelle und schreibt: „wenn noch der Quantendualismus des e- in der Form `lambda_H = 2 pi r_H` verwendet wird“. Die Relation wird also abermals **verwendet**, nicht aus einer Eigenwertbedingung gewonnen. |

Die Gleichung (98b) auf S. 277 enthaelt ausserdem ein Symbol `s = k^2 + 1`
im Zusammenhang mit den dortigen Struktur-/Koeffizientenformeln. Die
geprueften Seiten sagen jedoch nicht ausdruecklich, dass dieses `s` die
Bedeutung des sprachlichen `s`-Terms bzw. `s`-Niveaus oder einer Kreiswindung
hat. Eine solche Identifikation waere daher nicht quellengedeckt.

## Was die Quellenkette traegt

1. **Geometrische Schliessung:** Die Gleichheit von Wellenlaenge und dem
   Umfang eines Kreises mit Radius `r_H` steht zweimal gedruckt (S. 276 und
   S. 301). Fuer die konkrete Algebra der Alpha-Passage darf sie daher als
   explizite Heim-Annahme/Relation eingesetzt werden.
2. **Stehend/Kugeloberflaeche:** S. 277 verbindet diese Welle mit der
   gesamten Oberflaeche `4 pi r_H^2`, nicht nur mit einer parametrisierten
   Kreislinie. Das ist eine Besonderheit der Quellensprache; sie liefert
   nicht von sich aus eine Standard-Ringmode.
3. **Korpuskel-Welle:** S. 161 liefert eine allgemeine, vom Autor als
   empirisch benannte Quantendualismus-Relation `m c lambda = h`; S. 301
   verbindet im konkreten H-Schritt `m c^2` mit `h nu_H = c h / lambda_H`.
   Diese beiden Befunde erklaeren, warum Wellenlaenge und Energie in der
   Rechnung zugleich auftreten.

## Was nicht als hergeleitet gelten darf

In der gezielt geprueften H-Kette gibt es keinen ausgeschriebenen

- Operator bzw. keine Wellengleichung fuer die H-Elektronenwelle;
- Ansatz fuer eine Wellenfunktion auf Kreis oder Kugel;
- Randwert `psi(phi + 2 pi) = psi(phi)` oder vergleichbare Phasenbedingung;
- ganzzahlige Windungszahl/Modeszahl und keine Auswahlregel `n = 1`;
- Herleitung, warum die als „stehend“ bezeichnete Welle gleichzeitig die
  gesamte Kugeloberflaeche als s-Niveau bestimmen soll.

Das Wort `s` ersetzt diese fehlenden Schritte nicht. Eine spaetere eigene
Ringdiagnose kann folglich nur sichtbar als externe Konsequenz eines
zusaetzlich formulierten Randwertproblems auftreten; sie ist keine
Wiederholung einer von Heim hier ausformulierten Eigenloesung.

## Begrenztes Suchprotokoll und negative Befunde

Als Suchhilfe wurde der lokale Volltext von EDM2 nach den konkreten
Begriffen `Elektronenwelle`, `zirkulaere Elektronenwelle`, `K-Schale`,
`Quantendualismus`, `s-Term`, `s-Niveau`, `stehende Welle`, `Kreiswelle`,
`Wellenfunktion`, `Wellengleichung`, `Eigenwertgleichung`, `Windung`,
`Wellenzahl`, `Kreisumfang`, `Umfang` und `Randbedingung` durchsucht.

- `Elektronenwelle` verweist im Register nur auf S. 276 und S. 297; die
  beiden direkten Textstellen wurden visuell kontrolliert.
- Die Volltextsuche hat keine Treffer fuer `Wellenfunktion`, `Windung`,
  `Wellenzahl`, `Kreisumfang` oder `Kreiswelle`; fuer `s-Term`, `s-Niveau`
  und `stehende Welle` liefert das OCR wegen Schrifterkennung keine
  verlaesslichen Treffer. Die entscheidenden Saetze sind deshalb am PDF
  geprueft.
- `Wellengleichung` und `Eigenwertgleichung` kommen an anderen Stellen des
  Bands vor (u.a. allgemeine elektromagnetische bzw. Dirac-nahe
  Approximationen), jedoch nicht als eine im gezielten H-Abschnitt
  ausgesprochene Kreis-/Kugel-Randwertgleichung. Das ist ein begrenzter
  Fund- und Suchbefund, kein Beweis, dass eine solche Behandlung nirgends
  in allen unveroeffentlichten Materialien existiert.

Visuell gepruefte Render: `tmp/pdfs/wave_closure/edm2-282.png`,
`-283.png`, `-303.png` bis `-307.png`; Kontext fuer Quantendualismus:
`-167.png`, `-168.png`; unmittelbarer Strukturkontext: `-262.png`,
`-263.png`, `-279.png` bis `-281.png`.
