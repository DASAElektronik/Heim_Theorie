# H006: Quellenlesung der K4/W4-Fallunterscheidung

Stand: 2026-09-06. Eng begrenzte visuelle Review von H006 Druck/PDF9 mit
dem noetigen Strukturkontext auf Druck/PDF5, 6 und 10. Keine Massenrechnung,
keine Fallreparatur und keine globale Bewertung.

## 1. Ergebnis

H006 definiert `W4` zunaechst durch einen maximalen ganzzahligen
`K3`-Schritt und teilt den nichtnegativen Rest danach in drei Faelle. Nur
Fall (b) traegt eine ausdrueckliche logarithmische Gleichung fuer zunaechst
reell bestimmtes `K4`. Anschliessend verlangt die Quelle jedoch auch fuer
`K4` Ganzzahligkeit und schreibt eine besondere Abschneideregel vor.

Die Faelle (a) und (c) sind dagegen ausdrueckliche Auswahl-/Zaehlregeln:

- Bei `W4=0` kappt die Quelle den aus dem Logarithmus divergierenden Wert
  durch `K4=alpha3*K3`.
- Bei `W4>1` wird `K3` um eins vermindert und `alpha3*K3` zu einem negativen
  `K4` addiert; die Quelle behauptet, so entstehe ein neuer nichtnegativer
  Wert.

Auf der geprueften Seite steht nicht ausdruecklich, ob im Fall (c) danach
`W4` neu berechnet wird, ob der Additionsterm den alten oder bereits
verminderten `K3` benutzt und ob die Restgleichung nach der anschliessenden
Ganzzahligmachung erneut geprueft werden soll. Diese Luecken duerfen nicht
durch stilles Pseudocode-Verhalten geschlossen werden.

## 2. Quelle und Sichtpruefung

Quelle:

`01_sources/heim_primary/Massenformel_nach_B_Heim_1982.pdf`

H006 ist die IGW-Wiedergabe 2002/2003 eines auf 25.2.1982 datierten und
Heim zugeschriebenen Textes, kein hier authentifiziertes Urschriftfaksimile.

Visuell geprueft wurden:

- Druck/PDF5: `Q_j`, `n_j` als Besetzungsparameter und Zonenrollen;
- Druck/PDF6: Anstiegsprinzip (XIII), gruppierter Basisexponent (XV);
- Druck/PDF9: komplette Auswahlfolge (XXX)--(XXXII), alle drei `W4`-Faelle
  und der Ganzzahlvermerk;
- Druck/PDF10: Strukturentitaeten, Leerraum-/Grenzbedingungen und
  (XXXIV)/(XXXV).

Tragender hochaufgeloester Seitenbeleg:
`tmp/pdfs/k4_w4_h006/h006-p9-600-09.png`.
Kontextbilder: `tmp/pdfs/n0_alias/h006-05.png`, `h006-600-06.png` und
`tmp/pdfs/historical_exponent/h006-end-10.png`.

Die PDF-Textschicht wurde nur zur Navigation benutzt. Klammern, Indizes und
die auffaellige `K`/`K4`-Stelle wurden am Bild gelesen.

## 3. Gedruckte Eingabe- und Restfolge

Der Seitenanfang begrenzt den numerischen Weg auf `N=0` oder `N>=2` und
fordert dabei `Q=Q(0)` statt der unbekannten Funktion `Q_N=Q(N)`. Zuerst
wird gesetzt:

```text
W1 = W_(nu,x) * (1+f(N)).
```

Als enger Parameterkontext gibt Seite 5 (X) `Q4=2^(s-1)-1` mit
`s=k^2+1`; Seite 6 nennt `k=1` oder `k=2` als die moeglichen Werte. Damit
ist `Q4` in diesem Quellkontext positiv. Ein allgemeiner Vorzeichensatz fuer
`alpha3` wird in der Algorithmuspassage auf Seite 9 nicht erneut formuliert;
die Maximalwahl setzt ihren geordneten Beitrag praktisch voraus.

Dann folgt eine stufenweise Maximalwahl:

1. Die maximale Kubikzahl `K1^3`, deren Produkt mit `alpha1` noch in `W1`
   enthalten ist, liefert `W2=W1-alpha1*K1^3 >= 0`.
2. Die maximale Quadratzahl `K2^2` mit demselben Restkriterium liefert
   `W3=W2-alpha2*K2^2 >= 0`.
3. In (XXXI) bleibt glyphentreu

   ```text
   (n3+Q3)*alpha3 + exp[(1-2k)(n4+Q4)/3Q4] = W3.
   ```

   Dazu wird die maximale Zahl `K3` „im Sinne“

   ```text
   W3-alpha3*K3 = W4 >= 0
   ```

   bestimmt.

Der Text nennt erst spaeter ausdruecklich alle `K_j` ganzzahlig. In dieser
Ruecklesung ist `K3` deshalb die maximale nichtnegative ganze Zaehlzahl mit
nichtnegativem Rest; eine eigene `floor`-Formel druckt H006 nicht.

Die Gleichung `W4=W3-alpha3*K3` ist eine gedruckte exakte Gleichheit, kein
Naeherungszeichen. Unter der spaeter gedruckten Beziehung
`n_j=K_j-Q_j` entsprechen `K3=n3+Q3` und `K4=n4+Q4`.

## 4. Die drei gedruckten Faelle

Aus `W4>=0` listet die Quelle ohne Zwischenbereich:

```text
(a) W4=0,
(b) 0<W4<=1,
(c) W4>1.
```

### 4.1 Fall (b): reelle Logarithmusgleichung

H006 nennt (b) den allgemeinen Fall und druckt:

```text
ln W4 <= 0 und K4(2k-1) = -3Q4 ln W4.
```

Das ist eine Gleichung, nicht eine mit `approx` markierte Naeherung. Sie ist
die algebraische Umkehrung des gruppierten Exponentialrests, sofern dieser
Rest noch exakt `W4` ist, `W4>0`, `Q4` und `k` im benoetigten Bereich liegen
und `K4` vorerst reell sein darf.

Die Seite behauptet zugleich spaeter, `K_j` seien stets ganzzahlig. Weil bei
der Bestimmung von `K4` regelmaessig Dezimalstellen auftraeten, wird danach
eine gesonderte Zaehlentscheidung verlangt. Die Loggleichung und die
Integerentscheidung sind deshalb zwei Schritte; die Quelle zeigt nicht,
dass das Abschneiden die urspruengliche Exponentialgleichung exakt erhaelt.

### 4.2 Fall (c): unvollstaendig spezifizierter K3-Rueckschritt

Fuer `W4>1` druckt die Seite:

```text
ln W4 > 0 und K < 0.
```

Die Glyphe ist hier ein nacktes `K` **ohne sichtbaren Index 4**. Aus dem
unmittelbaren Kontext liegt eine Bezugnahme auf den logarithmisch ermittelten
vierten Wert nahe; quellengetreu ist `K4<0` an dieser ersten Stelle aber
nicht gedruckt.

Danach lautet die Verfahrensaussage paraphrasiert: Wegen

```text
n4+Q4 <= (n3+Q3)*alpha3
```

werde `K3` um eins vermindert und `alpha3*K3` zu `K4<0` addiert, sodass ein
neuer Wert `K4>=0` entstehe. Dies setze `K3>0` voraus. Bei `K3=0` koenne die
„Dilatation“ wegen des quadratischen Anstiegs von Zone `j=2` nicht erfolgen;
die Resonanzordnung existiere dann fuer den Zustand nicht („verbotener
Term“).

Quellenoffen bleiben drei Ablaufdetails:

- Es steht keine neue Gleichung `W4 := W3-alpha3*K3` nach `K3 := K3-1`.
- Der Additionsterm `alpha3*K3` ist nicht als alter oder neuer `K3` indiziert.
  Die Satzreihenfolge kann fuer den Nachwert sprechen, ist aber keine
  eindeutige Zuweisung.
- Weder Wiederholung/Schleife noch eine erneute Rest- oder
  Strukturpruefung wird auf dieser Seite formuliert.

Der Fall ist damit eine behauptete Auswahlvorschrift, keine vollstaendig
ausgeschriebene exakte Aktualisierung aller Variablen. Daraus folgt in dieser
Quellenreview noch kein mathematisches Fehlerurteil.

### 4.3 Fall (a): Grenzentscheidung statt Logloesung

H006 argumentiert: `W4 -> 0` fuehre zu `K4 -> infinity`; dies sei wegen
`K4<=alpha3*K3` und wegen des Ausschlusses divergierender
Selbstenergiepotentiale unmoeglich. Daher werde im Fall (a) der maximale
Wert

```text
K4 = alpha3*K3
```

berechnet.

Dies ist kein endlicher Wert, der durch Einsetzen von `W4=0` in die
Loggleichung folgt. Es ist eine von der Strukturgrenze motivierte
Zaehl-/Kappungsentscheidung. Die Quelle setzt ein Gleichheitszeichen fuer
den gewaehlten Maximalwert, zeigt aber nicht, dass dieser Wert die
Exponentialrestgleichung mit exakt `W4=0` loest oder welcher neue Rest nach
der Kappung gelten soll.

## 5. Strukturgrenze und Zaehldeutung

Die Schranke des vierten gegen den dritten Bereich ist nicht nur in der
Begruendung zu Fall (a) erwaehnt. H006 druckt als erste Ungleichung des
Anstiegsprinzips auf Seite 6 (XIII) und erneut auf Seite 9 (XXXII):

```text
n4+Q4 <= (n3+Q3)*alpha3.
```

Mit der auf Seite 9 angegebenen Rueckbeziehung `n_j=K_j-Q_j` wird daraus

```text
K4 <= alpha3*K3.
```

Seite 10 erklaert `n_j+Q_j>=0` als ganzzahlig, weil dieser Ausdruck die
Anzahl von Strukturentitaeten sei. Als Leerraumbedingung nennt sie
`n_j=-Q_j`; endliche Intervalle reichen von `-Q_j` bis zu den Grenzwerten
`L_j`. Beim Erreichen einer Zonengleichheit beschreibt sie den Anstieg
„von Aussen nach Innen“ als Ruecksetzung in Zone `j` und Erhoehung in
`j-1` um eine Einheit.

Das ist die quelleninterne physikalische Motivation fuer Nichtnegativitaet,
Ganzzahligkeit und Strukturgrenze. Es ist keine unabhaengige mathematische
Herleitung, dass jede der drei operativen `W4`-Regeln diese Bedingungen und
zugleich die Restgleichung erhaelt.

## 6. Der Ganzzahlvermerk

Nach den drei Faellen setzt H006 allgemein:

```text
n_j = K_j-Q_j,
K_j >= 0, also n_j >= -Q_j.
```

Der anschliessende hervorgehobene Vermerk beansprucht:

- `K_j` seien stets ganzzahlig;
- bei `K4` traeten dennoch regelmaessig Dezimalstellen auf;
- bei einer Dezimalfolge `,99...99` sei die Identitaet `,99...99=1` zu
  verwenden;
- jede davon verschiedene Dezimalfolge duerfe nicht aufgerundet werden;
  die Dezimalstellen seien abzuschneiden, weil `K_j` Anzahlen von
  Strukturentitaeten seien.

Die Quelle gibt keine endliche Stellenzahl, Toleranz oder numerische
Erkennungsregel fuer `,99...99` an. Die `0.999...=1`-Aussage ist eine exakte
Grenzidentitaet; ihre Umsetzung bei endlicher Rechnerdarstellung bleibt
offen. Das sonstige Abschneiden ist eine diskrete Auswahlentscheidung,
keine als Naeherung gekennzeichnete Gleichung und kein Beweis, dass der
abgeschnittene Wert den vorherigen reellen Logarithmusrest exakt erhaelt.

Seite 10 wiederholt fuer die Grenzwerte `L_j` und `L`, dass nicht
aufgerundet, sondern abgeschnitten werden solle. `L`/`L_j` sind dort
Resonanzgrenzen und duerfen nicht allein wegen derselben Rundungsprosa mit
dem lokalen `K4`-Zwischenschritt gleichgesetzt werden.

## 7. Quellenstatus der einzelnen Aussagen

| Aussage | Status in H006 |
|---|---|
| `W4=W3-alpha3*K3>=0` nach maximalem `K3` | explizite exakte Restdefinition |
| drei Bereiche (a)--(c) | explizite Fallaufteilung fuer den nichtnegativen Rest |
| Loggleichung in (b) | explizite Gleichheit fuer reelles `K4`; keine gedruckte Naeherung |
| Ganzzahligkeit/Abschneiden | explizite physisch motivierte Zaehlentscheidung |
| Gleichungserhalt nach Abschneiden | nicht gezeigt |
| `K3--` und Addition in (c) | explizite Prosaoperation, aber Vor-/Nachwert und Restupdate offen |
| `K4=alpha3*K3` in (a) | explizite maximale Kappungsentscheidung, keine Loesung von `ln(0)` |
| `K4<=alpha3*K3` | explizit in (a) und aus (XIII)/(XXXII) unter `K_j=n_j+Q_j` |
| Schleife oder erneute Validierung fuer (a)/(c) | nicht angegeben |

## 8. Enger Schluss

H006 bietet mehr als eine lose Naeherung: Die Greedy-Reste und die
Loggleichung in (b) sind mit Gleichheitszeichen gesetzt. Der Uebergang von
dem reellen Logwert zur ganzzahligen Strukturzahl sowie die Sonderfaelle
(a)/(c) sind jedoch zusaetzliche Zaehl-/Auswahlentscheidungen. Die Quelle
behauptet ihre physikalische Zulassigkeit, schreibt aber auf den geprueften
Seiten keinen vollstaendigen Nachweis der Gleichungserhaltung aus.

Der naechste algebraische Test darf deshalb exakt zwischen

1. dem vor dem Sonderfall definierten Rest `W4`,
2. einem reellen logarithmischen `K4`,
3. dem ganzzahlig ausgewaehlten `K4`, und
4. einem gegebenenfalls veraenderten `K3`

unterscheiden. Er darf fehlende Aktualisierungen nicht als Quelltext
ausgeben und einen gefundenen Rest nicht ohne weitere Quelle zu einem
globalen Fehler der Massenformel verallgemeinern.
