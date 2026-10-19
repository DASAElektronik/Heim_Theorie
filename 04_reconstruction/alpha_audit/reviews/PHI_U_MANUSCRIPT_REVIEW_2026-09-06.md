# `phi/U` im H013-Typoskript: Quellenkette, Schliessungsanspruch und Grenzen

## 1. Auftrag, Quellenstatus und Kurzbefund

Diese Review untersucht eng die Seitenfolge H013 Druck 29-32 / PDF 32-35
sowie die unmittelbar benoetigten Rueckverweise. Gefragt wird, ob die aus
einer „Analyse der Existenzzeiten“ angegebene Formel fuer das kleine
`phi` den zuvor offenen Selbstkopplungsterm unabhaengig bestimmt, einen
Masse-Lebensdauer-Kreis erzeugt oder lediglich ein neues explizites
Formelschema angibt. H014 wird nur als
fassungsgetrennter Vergleich herangezogen.

H013 ist der undatierte, autorbezeichnete Typoskriptscan
`J0033-Heim_Ausgewaehlte-Ergebnisse-b.pdf`; H014 ist der ebenfalls undatierte
Scan `J0032-Heim_Ausgewaehlte-Ergebnisse-a.pdf`. Aus Dateikennung,
Uploadpfad, Umfang oder Buchstabenfolge wird keine Chronologie abgeleitet.

Der enge Befund lautet:

* H013 beansprucht ausdruecklich eine Herleitungsbruecke: Die Analyse der
  Existenzzeiten liefere das massenwirksame `phi` aus (5e) nun explizit;
  (21b)/(21b1) gestatteten damit auch die numerische Untersuchung der Masse
  nach (4).
* Die gedruckten rechten Seiten von (21b)/(21b1) enthalten weder die zu
  berechnende Masse `M` noch die Existenzzeit `T`. Zusammen mit den
  vorangehenden Zustandsdefinitionen ist daher eine Vorwaertsauswertung
  ohne algebraisches Zurueckloesen aus `M` oder `T` angegeben. Ein
  unmittelbarer Ausgabe-Kreis `M -> T -> phi -> M` ist in dieser
  dargestellten Rechenfolge nicht belegt.
* Die Quelle zeigt keine unabhaengige Dynamikherleitung des
  Selbstkopplungsterms `K`. Sie gibt `phi` durch ein teilweise empirisch
  angepasstes Formelschema an. Fuer `N=0` definiert (5e) daraus bei
  `N_4 != 0` zwar algebraisch `K=phi/N_4`; wie die umfangreiche Form (21b)
  aus einer Selbstkopplungsdynamik folgt, wird aber nicht gezeigt. Wegen
  des offenen Vorzeichens in (21b1) ist auch die eindeutige numerische
  Auswertung des gedruckten Schemas noch nicht gesichert.
* Das Vorzeichen in der `U`-Klammer ist quellenphilologisch **nicht
  entschieden**: H013 druckt am Zeilenende nach `P+2Q` ein Minus und am
  Beginn der Folgezeile vor dem `4*pi`-Term ein zweites Minus. Eine
  Ein-Minus-Fortsetzungslesart ist moeglich, aber nicht als Erratum
  ausgewiesen; eine wortwoertliche Doppelminus-Lesart bleibt ebenso als
  Diagnose zu erhalten.

## 2. Der offene Platz vor (21b)

H013 Druck 13 / PDF 14 fuehrt die Massenbeziehung (4) in der sichtbaren
Gruppierung

```text
M = mu [ (G + S + F + Phi) alpha_+ + 4 q alpha_- ].             (4)
```

ein. Das kleine `phi` ist nicht mit dem grossen `Phi` gleichzusetzen. Es
tritt am Ende von `F` in (5c) als `phi(p;sigma)` auf. Druck 13-14 / PDF
14-15 definiert anschliessend

```text
phi = N_4 K delta(N),                                           (5e)
delta(N>0) = 0,   delta(0) = 1.                                (5e1)
```

Der Text beschreibt `K` als von `p` und `sigma` abhaengigen
Selbstkopplungsterm, der wesentlich die Existenzdauer beziehungsweise die
`x_4`-Ausdehnung eines Grundzustandes bestimme, und verweist dazu bereits
auf (21b). Fuer `N=0` ist `delta=1`; fuer `N>0` bleibt das kleine `phi`
nach dieser Definition null.

Damit ist vor (21b) zwar die **Rolle** festgelegt, aber `K` noch nicht
rechnerisch bestimmt. Der offene Slot ist die Selbstkopplung, nicht ein
fehlender weiterer Faktor `N_4` oder `delta`.

Ein enger Versionshinweis verhindert die Fusion mit H007: H013 (4) druckt

```text
M = mu [(G+S+F+Phi) alpha_+ + 4 q alpha_-],
```

waehrend H007 (B3) `mu alpha_+` vor die ganze Klammer setzt. Ausserdem
traegt in H013 (5c) der erste `n`-Term sichtbar `N_1`; im entsprechenden
H007-Ausdruck (B5) fehlt dieser Faktor. Diese lokalen Differenzen legen
keine Korrekturrichtung fest, zeigen aber, dass das H013-`phi/U`-Schema
nicht in eine fassungsuebergreifend identische Gesamtmassenformel
eingesetzt werden darf.

## 3. Was H013 als Bruecke behauptet

H013 Druck 29 / PDF 32 definiert die Existenzzeit `T`, die fuer `N>0`
noch unbekannte Funktion `T_N=T(N)` und `T_0=0`. Gleichung (21) enthaelt
auf der linken Seite `T-T_N`, auf der rechten Seite dagegen unter anderem
die Masse `M`, die Hilfsgroesse `y` und `delta(N)`. Direkt darunter steht:

* `phi` sei der „massenwirksame Anteil“ aus (5e);
* eine „Analyse der Existenzzeiten“ liefere fuer (5e) nunmehr explizit den
  auf der Folgeseite gedruckten Ausdruck (21b).

H013 Druck 32 / PDF 35 formuliert den Abschlussanspruch nochmals. Nun seien
alle Bestimmungsstuecke zur numerischen Untersuchung von (21) gegeben; das
gestatte zugleich die numerische Untersuchung von (4), weil `phi` durch
(21b)/(21b1) zur Bestimmung von `M` nach (4) explizit vorliege. Der dortige
Rueckverweis nennt (5c), also die Gleichung, in der `phi` in `F` vorkommt;
die direkte Definition des kleinen `phi` steht in (5e). Beide Stellen
muessen zusammen gelesen werden.

Auf derselben Druckseite beschreibt der Autor die beabsichtigte
Auswertereihenfolge fuer `N=0`: bekannte Quantenzahlen -> `W_(N=0)` und
rechte Seite von (11) -> Besetzungen `n,m,p,sigma` -> Masse `M` und
Existenzdauer `T` mit (4)-(8f1) und (21)-(21h). Das ist eine positive
Quellenangabe fuer eine Vorwaertsauswertung, nicht nur eine von aussen
rekonstruierte Abhaengigkeitsvermutung.

## 4. Exakte Struktur von `phi` und `U`

### 4.1 `phi` in (21b), H013 Druck 30 / PDF 33

In vereinheitlichter linearer Schreibweise, aber unter Erhalt der
sichtbaren Faktoren, lautet (21b):

```text
phi = [N_4 p^2/(1+p^2)]
      [(sigma+Q_sigma)/sqrt(1+sigma^2)]
      [fourth_root(2) - 4 B U W_(N=0)^(-1)]

    + P(P-2)^2
      [1 + Kappa (1-q)/(2 vartheta alpha)]
      (pi/e)^2 sqrt(eta_(1,2)) (Q_m-Q_n)

    - alpha^(-1) (P+1) binom(Q,3).                              (21b)
```

Der Nenner im zweiten Summanden lautet sichtbar `2 vartheta alpha`; vor
`alpha` steht das auch in den parallelen Formeln verwendete
`vartheta`-Zeichen, kein Wurzelstrich. `Kappa` bezeichnet hier die weitere
Multiplettziffer; sie darf nicht mit dem Selbstkopplungssymbol `K` aus
(5e) verschmolzen werden. Der Exponent
`-1` gehoert sichtbar zu `W_(N=0)`, so dass der erste Klammerterm
`fourth_root(2) - 4 B U/W_(N=0)` ist.

Wichtig fuer die Selektorfrage: (21b) ist bereits das **gesamte** explizite
`phi`. Es besitzt keinen aeusseren Faktor `N_4` und keinen aeusseren
`delta(N)`. `N_4` steht nur im ersten seiner drei Summanden. Deshalb darf
man (21b) bei der Einsetzung in `F_mass` aus (5c) weder nochmals insgesamt mit `N_4`
noch mit `delta` multiplizieren. Der Anschluss gilt im vom Autor
ausgewerteten Grundzustandsfall `N=0`, fuer den (5e1) ohnehin `delta=1`
setzt. Eine ungepruefte Fortsetzung von (21b) auf `N>0` wuerde dagegen die
Selektorlogik von (5e)/(5e1) verlassen.

### 4.2 `U` in (21b1) und der doppelte Minusdruck

Die sichtbare Struktur von (21b1)/(21b2) ist:

```text
U eta_(q,k)^2 = 2^Z [
    P^2 + (3/2)(P-Q) + P(1-q)
    + 4 Kappa B (1-Q)/(3-2q)
    + (k-1) (P+2Q -
             - 4 pi/fourth_root(2) (P-Q)(1-q))
],                                                               (21b1)

Z = k + Kappa + P + Q.                                           (21b2)
```

Diese Transkription bewahrt absichtlich den Zeilenumbruch der Quelle.
Zwei Minusglyphen sind sichtbar: das erste unmittelbar nach `P+2Q` am
Zeilenende, das zweite am Beginn der Folgezeile. Der Scan entscheidet
nicht, ob das erste nur eine Fortsetzungsmarke beziehungsweise eine
typographische Verdopplung ist oder ob beide algebraisch gelten sollen.
H013 autorisiert daher weder eine eindeutige Ein-Minus- noch eine
Doppelminus-Normalisierung. Insbesondere darf diese Parallelstelle nicht
als belegtes Erratum fuer H007 behandelt werden.

Unter den Formeln steht ausdruecklich, `B` werde in (21b)/(21b1) nach
(13b) ermittelt. H013 Druck 18 / PDF 19 gibt

```text
k^2 (2k-1) B = 3 H,                                             (13b)
H = Q_n + Q_m + Q_p + Q_sigma.                                  (12b)
```

Damit ist `B` hier eine zustandsabhaengige Hilfsgroesse, nicht die
empirisch eingefuehrte Baryonenziffer der Prosa auf Druck 29.

## 5. Abhaengigkeiten: kein direkter `M/T`-Ruecklauf, aber keine reine Erstdeduktion

Die auf den geprueften Seiten angegebene Rechenkette laesst sich so
trennen:

```text
diskrete Zustandszahlen und feste Konstanten
        |--> eta_(q,k), N_4, Q_i, H --> B
        |--> y_W (13e1) --> (11b)-(13e) --> W_(N=0)
        |--> (21b1)/(21b2) --> U
        '--> p,sigma und weitere Besetzungen

B, U, W_(N=0), p, sigma, ... --> (21b) phi

phi --> F_mass (5c) --> (4) M ----------------------.
  |                                                   |
  '--> y_time (21a), mit F_time (21c),                |
       W_(N=0), b_1 und b_2 ---------------------> (21) --> T
```

In den expliziten rechten Seiten von (21b), (21b1), (11b), (12b) und
(13b) steht weder ein gemessener Wert von `M` noch `T`. Die Quelle selbst
weist `W_(N=0)` in Druck 32 / PDF 35 als vor der Massen-/Lebensdauerausgabe
ermittelbar aus. In diesem engen algebraischen Sinn ist kein notwendiger
Ausgabe-Kreis belegt.

Die Schlussfolgerung ist dennoch **bedingt**:

1. (21) enthaelt bereits `M` und `T`, aber die dazwischen behauptete
   „Analyse“ wird nicht Schritt fuer Schritt gezeigt. Aus (21) allein kann
   man die umfangreiche Form (21b)/(21b1) nicht nachvollziehbar ableiten.
2. (21b) bestimmt `phi` als Formelschema und liefert keine gesonderte
   Dynamikgleichung fuer den in (5e) genannten Selbstkopplungsterm `K`.
   Fuer `N=0` und `N_4 != 0` folgt aus (5e) algebraisch `K=phi/N_4`;
   eine unabhaengige Feld- oder Kopplungsableitung dieses Werts wird damit
   nicht vorgelegt.
3. Zustandszuordnungen sind nicht durchweg theorieneutral. Schon Druck 29
   sagt, `k-1` sei mit einer „aus empirischen Gruenden eingefuehrten“
   Baryonenziffer identisch; Druck 32 setzt die bereits interpretierten
   Multiplett-Quantenzahlen voraus.
4. Die Buchstaben `y` und `F` werden im Scan in verschiedenen lokalen
   Rollen wiederverwendet: `y_W` in (13e)/(13e1) gehoert zur Konstruktion
   von `W_(N=0)`, waehrend `y_time` in (21a) die Substitution der
   Existenzzeitformel ist; entsprechend ist `F_mass` aus (5c) vom
   `F_time` aus (21c) zu trennen. Nimmt man diese gleich gedruckten
   Buchstaben ohne lokale Bereichstrennung als jeweils dieselbe Variable,
   entsteht eine Scheinkopplung. Die explizite Auswertereihenfolge auf
   Druck 32 behandelt `W_(N=0)` jedoch als bereits aus der frueheren Kette
   bestimmbar. Die Indizes `_W`, `_time` und `_mass` sind nur
   Analysebezeichnungen dieser Review, nicht Quellensymbole.

Der angemessene Status ist daher: **explizites Vorwaertsformelschema bei
vorgegebenen Zustandsdaten**, dessen eindeutige Auswertung noch von der
Vorzeichenklaerung in (21b1) abhaengt, und **keine gezeigte,
datenunabhaengige Dynamikherleitung der Selbstkopplung**.

## 6. Empirische Eingaben und ausdrueckliche Vorlaeufigkeit

H013 Druck 37 / PDF 40 nennt innerhalb der Verbindung
(21b)/(21b1) gewisse „frei verfuegbare Konstanten“ in den Formen

```text
fourth_root(2),  (pi/e)^2,  4 pi fourth_root(1/2)
```

und sagt, sie seien an empirische Gegebenheiten angepasst worden. Die
kleine `4` ist jeweils der Wurzelindex. Der dritte Ausdruck ist der
Zahlenfaktor, der in (21b1) als `4*pi/fourth_root(2)` erscheint. Die
fertigen Formeln sind also aus festen Zahlen auswertbar; ihre Wahl ist
nach dem eigenen Text aber nicht rein datenunabhaengig deduziert. Die
Passage nennt weder das Fitverfahren noch den verwendeten Datensatz oder
die Zahl statistisch unabhaengiger Anpassungen. Daraus darf insbesondere
nicht pauschal gefolgert werden, jede andere Konstante des Blocks sei frei
gefittet.

Die Seiten Druck 36-37 / PDF 39-40 begrenzen den Anspruch weiter:

* `z(N)`, daraus `Q(N)`, und die Existenzzeiten `T_N` fuer `N>0` seien noch
  unbekannt; die Resonanzmassen seien daher nur approximativ.
* Die Klaerung dieser offenen Fragen und der magnetischen Momente koenne
  rueckwirkende Korrekturen der Beziehungen (14a)-(14b1) zur Folge haben.
* Eine spaetere Beschreibung der Wirkungsquerschnitte koenne
  Korrekturglieder sowohl im grossen `Phi` aus (5d) als auch im kleinen
  `phi` aus (21b) nach sich ziehen.

Das belegt unmittelbar die vom Autor selbst vorgesehene
Fortschreibbarkeit der Formeln. Es belegt weder, dass diese spaetere
Korrektur tatsaechlich ausgearbeitet wurde, noch dass alle vorhandenen
Unklarheiten dadurch automatisch behoben waeren.

## 7. Fassungsvergleich zu H014, ohne Chronologie

H014 besitzt dieselbe fruehe Struktur `phi=N_4 K delta(N)` und beschreibt
`K` ebenfalls als Selbstkopplungsterm mit Bezug auf die Existenzdauer. Im
gezielt geprueften Anschluss Druck 20-26 / PDF 22-28 folgt jedoch kein dem
H013-Block (21)-(21h) entsprechender Lebensdauer-/`phi/U`-Abschnitt.
Druck 24 / PDF 26 geht zur numerischen Bestimmung und Tabelle der Massen
ueber; seine Tabelle II enthaelt Massen, aber keine Lebensdauern.

H014 ist damit eine positive Vergleichsstelle fuer den fruehen offenen
Selbstkopplungsslot, aber keine zweite Ueberlieferung von H013 (21b)/(21b1).
Dass H013 die spaetere explizite Formel besitzt und H014 nicht, ist ein
Fassungsunterschied; eine zeitliche Reihenfolge oder Herkunft der
Ergaenzung folgt daraus nicht.

## 8. Ergebnis nach Statusarten

### Direkt belegt

1. H013 definiert das kleine `phi` zuerst als selektierten,
   massenwirksamen Selbstkopplungsanteil und verweist auf die spaetere
   Existenzzeitanalyse.
2. (21b)/(21b1) geben `phi` und `U` als Formeln ohne `M`- oder `T`-Wert auf
   ihren rechten Seiten an; Druck 32 behauptet damit die numerische
   Bestimmbarkeit von Masse und Lebensdauer fuer `N=0`.
3. `N_4` steht in (21b) nur im ersten Summanden; `delta(N)` steht dort
   nicht. (21b) darf nicht nochmals global mit `N_4 delta(N)` multipliziert
   werden.
4. H013 druckt in (21b1) zwei Minuszeichen ueber den Zeilenumbruch.
5. Drei Zahlenformen des `phi/U`-Blocks werden vom Autor ausdruecklich als
   empirisch angepasst bezeichnet.
6. Die Quelle erklaert Teile der Resonanz- und Wirkungsquerschnittskette
   fuer offen beziehungsweise spaeter korrekturbeduerftig.

### Nur bedingt oder nicht belegt

1. Belegt ist ein **explizites Formelschema** fuer den frueheren
   `phi`-Slot; eine eindeutige numerische Auswertung bleibt wegen des
   offenen Vorzeichens in (21b1) fassungsabhaengig. Nicht belegt ist eine
   nachvollziehbare Dynamikherleitung des Selbstkopplungsterms `K` aus
   vorgelagerten Grundgleichungen.
2. Ein unmittelbarer algebraischer Kreis ueber ausgegebene `M`/`T` ist in
   der dargestellten Vorwaertskette nicht vorhanden; statistische
   Unabhaengigkeit von den zur Konstantenwahl oder Zustandsidentifikation
   verwendeten empirischen Daten ist damit nicht gezeigt.
3. Das doppelte Minus in (21b1) entscheidet keine ausführbare
   Vorzeichenfassung und kein H007-Erratum.
4. Der `N=0`-Anschluss autorisiert keine `N>0`-Lebensdauer- oder
   Zwischenzustandsdynamik.
5. Aus dem Unterschied H013/H014 folgt keine gesicherte Redaktions- oder
   Werkchronologie.

## 9. Visuelle Pruefspur und Suchgrenze

Besonders tragende Vollseitenbilder:

* `tmp/pdfs/eta22_context/j0033-render-14.png` - H013 Druck 13 / PDF 14,
  (4), (5c), (5e);
* `tmp/pdfs/eta22_context/j0033-render-15.png` - H013 Druck 14 / PDF 15,
  Selbstkopplungsbedeutung von `K` und Selektor (5e1);
* `tmp/pdfs/eta22_roles/j0033-hi-32.png` - H013 Druck 29 / PDF 32,
  Existenzzeitgleichung und Ankuendigung der expliziten `phi`-Form;
* `tmp/pdfs/eta22_roles/j0033-hi-33.png` sowie
  `j0033-phi-800-33.png` - H013 Druck 30 / PDF 33, (21b)-(21b2),
  Produktumfang und doppeltes Minus;
* `tmp/pdfs/phi_u/phi-denominator.png` - 400-dpi-Detail aus H013
  Druck 30 / PDF 33, Nenner `2 vartheta alpha` in (21b);
* `tmp/pdfs/eta22_roles/j0033-35.png` - H013 Druck 32 / PDF 35,
  behauptete Schliessung und Auswertereihenfolge;
* `tmp/pdfs/eta22_roles/j0033-limit-39.png` und
  `j0033-limit-40.png` - H013 Druck 36-37 / PDF 39-40,
  unbekannte Groessen, empirische Anpassung und moegliche Korrekturen;
* `tmp/pdfs/eta22_roles/j0032-26.png` - H014 Druck 24 / PDF 26,
  Uebergang zur Massenauswertung ohne entsprechenden Lebensdauerblock.

Ergaenzend wurden H013 Druck 17-18 / PDF 18-19 fuer `W_(N=0)`, `H` und `B`
sowie H014 Druck 13-15 und 20-26 visuell geprueft. Die Suche war auf diese
unmittelbare Definitions- und Anschlusskette beschraenkt. Es wurde weder
die gesamte Massenformel erneut auditiert noch ein Fit gerechnet, eine
neuere physikalische Widerlegung gesucht oder eine nicht belegte
Manuskriptchronologie konstruiert.
