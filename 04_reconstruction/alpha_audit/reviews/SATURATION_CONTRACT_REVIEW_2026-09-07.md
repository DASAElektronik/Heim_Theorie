# Vorreview der Kappenregel im z3-Sensitivitaetszweig

Stand: 2026-09-07. Rein algebraischer Definitions- und Beweisreview vor
einer neuen numerischen Auswertung. Verwendet werden die in Etappe 35
festgelegten Zellen und die bereits visuell geprueften Quellenreviews zur
Buchauswahl. Die Original-PDF wurde fuer diese Review nicht selbst neu
gelesen. Nach Sicherung des Vorvertrags meldete Root eine erneute direkte
Vollseitenpruefung von H004 Druck 321--323, 328--330 und 340--342; deren
enger Definitionsbefund zu negativen `n_j` ist in Abschnitt 7 ausdruecklich
als Root-Gegenpruefung zugeschrieben.

## 1. Ergebnis

Fuer die zwei festen `A(k=1)=1/5`-Zellen liegt nach Etappe 35 vor:

```text
(N1,N2,N3)=(14,10,1),
0<W4<1,
raw_N4=-ln(W4)/A ~= 14.345,
cap=alpha3*N3=alpha3 ~= 0.9787.
```

Damit ist `raw_N4>cap` und der bereits dokumentierte Buch-Saettigungszweig
erreicht. Unter der eng benoetigten TRC-Annahme

```text
TRC(x) ist entweder floor(x) oder ceil(x)
```

ergibt die zusammengesetzte Kappen-/Korrekturregel fuer jedes `x>=0`
exakt `floor(x)`. Da hier `0<cap<1`, folgt robust

```text
N4=0.
```

Das Ergebnis ist unabhaengig davon, ob die gedruckte Neuner-Ausnahme im
konkreten Dezimalbild als Abschneiden auf `0` oder als Promotion auf `1`
behandelt wuerde. Es ist aber nur die Ausgabe dieser Kappenregel. Sie loest
die feste Exponentialgleichung nicht: Bei `N4=0` ist der Externterm `1`,
waehrend der nach den ersten drei Schritten verbliebene Rest `W4` strikt
zwischen `0` und `1` liegt.

## 2. Quellen- und Rechenscope

Als bereits visuell abgesicherte Transkription wird aus
`BOOK_SELECTION_SOURCE_REVIEW_2026-09-06.md` und
`BOOK_SELECTION_VERSION_REVIEW_2026-09-06.md` verwendet:

```text
W5>alpha3*N3  ->  N4=TRC(alpha3*N3),

wenn zusaetzlich TRC(alpha3*N3)>alpha3*N3:
N4=TRC(alpha3*N3)-1.
```

Die Quellenreviews verorten dies auf H004 Druck 341 / PDF 347 und
bezeichnen den zweiten Schritt als lokale Beruecksichtigung von
`beta4=1` aus (107a). Diese Review bestaetigt den Wortlaut nicht durch eine
neue Bildlesung, sondern untersucht nur seine algebraische Wirkung im
bereits fixierten Fall.

Die Zahlenintervalle fuer `W4` und `alpha3` werden nicht neu berechnet.
Benutzt werden nur die bereits berichteten strikten Eigenschaften
`0<W4<1`, `0<alpha3<1` und `raw_N4>alpha3` fuer beide Alpha-Profile.

## 3. Allgemeines Kappenlemma

Definiere fuer `x>=0` die zusammengesetzte Auswahl

```text
S(x) = TRC(x)-1, falls TRC(x)>x,
       TRC(x),   sonst.
```

Angenommen sei ausschliesslich

```text
TRC(x) in {floor(x),ceil(x)}.
```

Dann gilt fuer alle `x>=0`

```text
S(x)=floor(x).
```

Beweis durch Falltrennung:

1. Ist `TRC(x)=floor(x)`, dann gilt `TRC(x)<=x`; der Abzug wird nicht
   aktiviert und `S(x)=floor(x)`.
2. Ist `TRC(x)=ceil(x)` und `x` ganzzahlig, dann ist `TRC(x)=x`; auch hier
   wird nicht abgezogen und `S(x)=x=floor(x)`.
3. Ist `TRC(x)=ceil(x)` und `x` nicht ganzzahlig, dann ist
   `TRC(x)>x`; daher

   ```text
   S(x)=ceil(x)-1=floor(x).
   ```

Die korrekte allgemeine Kurzform lautet somit

```text
S(x)=TRC(x)-1_[TRC(x)>x]=floor(x).
```

Sie darf **nicht** pauschal zu `ceil(x)-1` verkuerzt werden. Fuer jedes
ganzzahlige `x=m` waere `ceil(m)-1=m-1`, waehrend die bedingte Regel wegen
`TRC(m)=m` keinen Abzug ausloest und `S(m)=m` liefert.

Das Lemma behauptet nicht, der Buchoperator `TRC` sei allgemein entweder
floor oder ceil. Es zeigt nur: Wenn seine fuer diesen Schritt betrachteten
Moeglichkeiten auf Abschneiden oder Promotion zum naechsten Integer
beschraenkt sind, beseitigt die nachgeschaltete `>x`-Korrektur die
Mehrdeutigkeit der Ausgabe.

## 4. Anwendung auf die feste Kappe

Mit `N3=1` ist

```text
cap=alpha3*N3=alpha3.
```

Die Etappe-35-Einschluesse geben in beiden Alpha-Profilen `0<alpha3<1`.
Daher ist `floor(cap)=0`. Konkret sind nur zwei TRC-Ausgaenge unter der
Lemma-Annahme moeglich:

```text
TRC(cap)=0:  0>cap ist falsch  -> N4=0,
TRC(cap)=1:  1>cap ist wahr    -> N4=1-1=0.
```

Es muss fuer diesen Schluss weder entschieden werden, wie viele Neunen die
Quelle fuer eine Promotion verlangt, noch ob die berichtete Kappe diese
undefinierte Schwelle erreicht. Ein allgemeiner TRC-Algorithmus folgt
daraus nicht.

## 5. Strukturdiagnosen bei N=(14,10,1,0)

Die ungewichteten Bandbreiten aus (107)/(107a) sind

```text
beta2 = 14^3-G2(10) = 2359,
beta3 = 10^2-G3(1)  = 99,
beta4 = 1-0          = 1.
```

Alle drei erfuellen den nicht kollabierten (107a)-Schwellwert `>=1`.
Die separat auszugebenden Margen der zweiten (107)-Reihe sind

```text
14^3-10^2 = 2644,
10^2-1    = 99,
1-1       = 0.
```

Die letzte Null bedeutet hier, dass die Forderung `N3>=1` genau am Rand
erfuellt ist; sie ist nicht `beta4=0` und kein Kollapsbefund.

Die spaetere, gewichtete Sigma-Groesse (107b) ist davon zu trennen:

```text
beta4_sigma=alpha3*N3-N4=alpha3.
```

Wegen `0<alpha3<1` erfuellt sie die in (107b) gedruckte Positivitaet
`>0`, aber nicht einen hypothetisch darauf uebertragenen Schwellwert
`>=1`. Ein solcher Integer-Schwellwert darf nicht aus (107a) importiert
werden, weil `alpha3` reell ist und die Quellenreviews die gewichtete
(107b)-Definition gerade von der ungewichteten Bandbreite trennen.

## 6. Gleichungserhalt bleibt eine eigene Frage

Nach den ersten drei Vorwaertsschritten ist definitionsgemaess

```text
W4 = W-[a1*N1^3+a2*N2^2+a3*N3].
```

Die feste Gleichung (108) waere nach Einsetzen von `N4` genau dann erfuellt,
wenn

```text
exp(-A*N4)=W4.
```

Fuer `N4=0` ist die linke Seite `1`. Da im festen Zweig `0<W4<1`, gilt

```text
R = 1-W4 > 0.
```

Die Sattigungsregel erzeugt also eine strukturell begrenzte ganzzahlige
Ausgabe, nicht die exakte logarithmische Umkehrung des Restes. Das ist ein
algebraischer Status des festgelegten Modells, keine Masse, kein
physikalischer Fehler und keine Aussage, die Buchregel sei sinnlos.

## 7. Rueckrechnung zu n_j und ihre Grenze

Mit den buchinternen Geruestwerten

```text
(Q1,Q2,Q3,Q4)=(3,3,2,1)
```

liefert `n_j=N_j-Q_j`

```text
n=(11,7,-1,-1).
```

Die bereits geprueften Definitionsseiten erlauben allgemein
`N_j=n_j+Q_j>=0`, also `n_j>=-Q_j`. Root bestaetigte dies nach Sicherung
des Vorvertrags erneut durch direkte Vollseitensicht: Druck 322 erlaube
`n_j<0` ausdruecklich bei `N_j>=0`, Druck 328 nenne als Untergrenze
`-Q_j`. Das Tupel verletzt diese Grenze nicht: `n3=-1>=-2`,
`n4=-1=-Q4`. Negative `n_j` duerfen deshalb nicht als negative `N_j` oder
allein wegen ihres Vorzeichens als verbotene Besetzung bezeichnet werden.

Umgekehrt beweist diese untere Definitionsgrenze noch nicht, dass jedes
solche `n` einen physikalisch realisierten Pseudosingulettzustand darstellt.
Insbesondere ist `N4=0` nur die leere vierte Komponente; nicht alle `N_j`
sind null, also ist das Gesamttupel nicht der auf Druck 322 bezeichnete
vollstaendig leere `R3`-Bezug.

## 8. Engster naechster Originalauftrag

Fuer die algebraische Ausgabe `N4=0` ist keine weitere Quelle noetig. Eine
erneute Originallekture wird erst fuer weitergehende Bedeutungsansprueche
erforderlich. Der engste sinnvolle Umfang waere:

1. H004 Druck 341 / PDF 347 samt Satzanschluss auf 342 erneut visuell
   pruefen: genauer Geltungsbereich der Saettigungsregel, der bedingten
   `beta4=1`-Korrektur und der anschliessenden Rueckrechnung `n=N-Q`.
2. H004 Druck 328--329 / PDF 334--335 gegenlesen: Ist die auf 341 genannte
   `beta4=1`-Korrektur ausschliesslich die ungewichtete (107a)-Bandbreite,
   waehrend (107b) fuer die Sigma-Anregung nur `>0` verlangt? Die vorhandenen
   Reviews sprechen dafuer, der lokale Symbolanschluss bleibt aber
   erklaerungsbeduerftig.
3. Nur falls aus `n3=n4=-1` eine weitergehende physikalische Zulassungs-
   oder Realisierungsaussage folgen soll, den konkreten Pseudosingulett-/
   Sigma-Kontext weiter pruefen. Die negative Zahl ist nach Roots erneuter
   Vollsicht von Druck 322 und 328 fuer sich kein Verbot; die allgemeine
   Schranke `n_j>=-Q_j` allein beweist aber auch keine Realisierung.

Nicht erforderlich ist eine neue A-, Y-, Massen- oder Restwertsuche. Der
naechste Rechenschritt kann auf dem vorab bestimmten `N4=0` lediglich den
Gleichungsrest und die getrennten Strukturdefinitionen ausweisen; eine
weitere Sattigungs- oder Transferregel darf nicht erfunden werden.
