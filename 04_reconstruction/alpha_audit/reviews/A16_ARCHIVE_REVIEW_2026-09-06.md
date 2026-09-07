# A16 im fotografierten Archivmaterial H015

Stand: 2026-09-06. Enge visuelle Quellenpruefung; keine Programmausfuehrung,
keine Massenrechnung und keine Aenderung eines Rechenprofils.

## 1. Ergebnis

H015 enthaelt zwei positive, voneinander verschieden gesetzte Belege fuer
dieselbe lokale A16-Klammerung:

```text
A16 = (pi*e)^2 * [1 + alpha/(5*eta) * (1 + 6*alpha/pi)].
```

1. Das fotografierte FORTRAN-Listing `GINIT`, Seite 2, schreibt den Nenner
   maschinenlesbar als `(5.Q0*ETA)`.
2. Ein fotografierter Typoskriptabschnitt schreibt einen echten Bruch
   `alpha/(5 eta)` und laesst die folgende Klammer damit multiplizieren.

Damit ist die Nennerproduktlesart `/(5*eta)` fuer diese beiden H015-Stellen
belegt. Die alternative lineare Lesart `.../5*eta` wird von ihnen nicht
getragen. Der Befund ist eine lokale Quellenbruecke; er ist weder eine
Herleitung der Faktoren noch ein Editionsnachweis, dass jede mit „1982“
bezeichnete Fassung identisch war.

## 2. Quelle und Provenienzgrenze

Geprueft wurde die lokale Datei

`01_sources/heim_primary/alpha3_origin/Heim_DESY_1982_Archivscan.pdf`

mit SHA-256

`C242599F7AAF68BB8E2F3C7756A24687E86FAD879E4D0E22C00585A32403317F`.

Die PDF ist eine heutige Zusammenstellung von Fotografien. Der lokale Hash
identifiziert genau diese Kopie, authentifiziert aber weder Papier noch
Handschrift und datiert nicht die Digitalisierung auf 1982.

Im fotografierten Listing sind folgende Eigenangaben sichtbar:

- PDF 20, `GINIT PAGE 1`: Kommentarzeile `17/03/82 ... MEMBER NAME GINIT
  (HEIMS) FORTRAN`;
- PDF 20/21: Compilerkopf `SYSTEM/370 FORTRAN H EXTENDED (ENHANCED)` und
  `DATE 82.223/09.22.04`;
- der Compilerkopf nennt ausserdem `VERSION 1.3.0 (01 MAY 80)`; dies ist
  eine Versionsangabe des Compilers, kein Datum der A16-Formel.

PDF 43 zeigt am Ende eines fotografierten Typoskriptteils Blatt `- 7 -`,
`NORTHEIM den 25.2.1982` und eine Signaturabbildung mit `(Heim)`. Das stuetzt
die Datierung und Zuschreibung dieses Typoskriptteils innerhalb des Scans,
ist aber keine forensische Authentifizierung und datiert das separat
fotografierte Listing nicht automatisch auf den 25. Februar.

## 3. FORTRAN-Fundstelle

Fundort: H015 PDF 21, obere fotografierte Seite, Modul `GINIT`, Listing-
`PAGE 2`, Blockkommentar `(4-8) PARAMETERMATRIX`, ISN `0031`, physische
Quellzeile `00005308`.

Glyphengetreue lineare Transkription:

```fortran
A16=(PI*EBN)**2*(1.Q0+ALFA/(5.Q0*ETA)*(1.Q0+6.Q0*ALFA/PI))
```

Die expliziten runden Klammern entscheiden den lokalen Scope:

```text
ALFA / (5.Q0*ETA)
```

und nicht `(ALFA/5.Q0)*ETA`. `A16` ist hier der Matrixeintrag mit den
Indizes 1 und 6. Die Zeile enthaelt keinen Faktor `Y9`.

Das unmittelbar folgende Matrixlisting ist aktiver Quelltext, nicht eine
auskommentierte Alternativzeile. Daraus folgt noch keine theoretische
Begruendung fuer `5`, `6`, `(pi*e)^2` oder die gesamte Parametrisierung.

## 4. Typoskript-Fundstelle

Fundort: H015 PDF 39, fotografierter Typoskriptkoerper unter der Ueberschrift

```text
Vorschlag zur Bestimmung der Matrixelemente (Reduktion auf pi,e und xi):
```

Im Bild sind die Folioangaben `- 4 -` und `- 5 -` zugleich sichtbar. Ob
dies durch ueberlagerte Blaetter, die Aufnahmeordnung oder eine andere
physische Anordnung entstand, wird hier nicht entschieden. Fuer den
Formelbeleg wird daher PDF 39 und der sichtbare Formelkoerper angegeben,
nicht pauschal „Typoskriptseite 4“ oder „Seite 5“ behauptet.

Die A16-Zeile lautet normalisiert, aber ohne algebraische Umformung:

```text
A_16 = (pi e)^2 (1 + alpha/(5 eta) (1 + 6 alpha/pi)).
```

Der Bruchstrich umfasst sichtbar `5 eta`. Der Ausdruck steht in einer als
„Vorschlag“ bezeichneten Liste von Matrixelementen. Das ist eine direkte
Formelfestlegung, keine auf dieser Seite ausgefuehrte Ableitung ihres
Zahlenaufbaus.

## 5. Welche eta-Groesse ist belegt?

Beide H015-Stellen verwenden das **unindizierte** `eta` beziehungsweise
`ETA`. Weder die Listingzeile noch die Typoskriptzeile schreibt `eta_qk`,
`eta_11` oder einen anderen Index. Insbesondere darf das `ETA` in A16 nicht
allein wegen anderer Programmteile durch `ETAQK` ersetzt werden.

Auf PDF 20 fuehrt die sichtbare `COMMON`-Deklaration `ETA` ebenfalls als
einzelne Konstante. Die anschliessenden Zuweisungen auf `GINIT PAGE 1` sind
im Foto durch Hand/Schatten und den Bildausschnitt teilweise verdeckt; eine
eigenstaendige H015-Zuweisung fuer `ETA` wurde deshalb nicht glyphensicher
abgelesen.

Als getrennte statische Vergleichsquelle definieren die vorhandenen H010-
Transkriptionen dasselbe unindizierte Symbol explizit:

```text
eta = pi / sqrt(sqrt(4 + pi^4)).
```

Fundstellen: H010 Pascal 0.62c, Zeile 200, und H010 C 0.66, Zeile 610.
Ihre A16-Zeilen 291 beziehungsweise 705 verwenden ebenfalls
`alpha/(5*eta)`. Diese Uebereinstimmung ist ein positiver Formvergleich,
aber kein Ersatz fuer die im Foto verdeckte H015-ETA-Zuweisung und kein
Beweis einer lueckenlosen Portierungs- oder Editionsgeschichte.

## 6. Abgrenzung zu H006 und spaeteren Fassungen

H006 Druck/PDF 7, (XXIV), druckt die A16-Zeile kompakt mit der linearen
Zeichenfolge `/5 eta`, ohne eine so explizite Nennerklammer wie H015. H015
belegt daher eine historische Rechenlesart fuer die lokale Formel, aber
nicht die Ursache der abweichend offenen Drucksetzung und kein autorisiertes
Erratum zu H006.

Eine Buchfassung kann zusaetzliche Faktoren oder Unsicherheitsparameter
fuehren. Solche Zusatzelemente duerfen nicht stillschweigend in das
H015-Listing importiert werden; insbesondere zeigt die gepruefte H015-
A16-Zuweisung kein `Y9`.

## 7. Such- und Aussagegrenze

Visuell tragend geprueft wurden H015 PDF 20, 21, 39 und 43. PDF 20/21
decken den sichtbaren `GINIT`-Anfang und den gesamten A16-Matrixblock ab;
PDF 39 liefert die Typoskriptform, PDF 43 den Schluss-/Datierungskontext.
Keine OCR-Leerstelle wird als Negativbeweis benutzt.

Arbeitsbilder:

- `tmp/pdfs/a16_archive/h015-p21-ginit-a16-detail.jpg`
- `tmp/pdfs/alpha3_desy/desy-21.png`
- `tmp/pdfs/a16_archive/h015-p39-a16-typescript-detail.jpg`
- `tmp/pdfs/alpha3_origin/desy-39.png`
- `tmp/pdfs/alpha3_origin/desy-43.png`

Nicht belegt sind damit eine vollstaendige Herleitung von A16, die genaue
Redaktionschronologie aller fotografierten Blaetter, die Vollstaendigkeit
des Archivs oder eine gemeinsame Gesamtfassung von H006, H010 und H015.
Das engste belastbare Resultat lautet: **H015 setzt A16 zweimal mit dem
Nennerprodukt `5*eta` und einem unindizierten eta; die sichtbaren Stellen
erklaeren diese Wahl nicht weiter.**
