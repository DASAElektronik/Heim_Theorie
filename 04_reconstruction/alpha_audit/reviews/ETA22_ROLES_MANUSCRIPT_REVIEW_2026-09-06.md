# `eta_22` in Lebensdauer, `b_2` und Anhang der Heim-Typoskripte

## 1. Auftrag und Ergebnis

Diese Review verfolgt gezielt die Rollen von `eta_22` im undatierten,
autorbezeichneten Typoskript H013 (`J0033`) und in der parallelen Fassung
H014 (`J0032`). Ausgangspunkt sind die in der IGW-Formelsammlung H007 als
B47 (Existenzzeit), B48 (`y`) und B55 (`b_2`) bezeichneten Strukturen. Die
Prüfung fragt nur nach den entsprechenden Autorenstellen und ihrer
Formelrolle. Sie rekonstruiert weder das gesamte Massensystem noch eine
Delta-Zwischenzustandsdynamik und datiert die beiden Scans nicht.

Das Hauptergebnis lautet:

* H013 besitzt einen zusammenhängenden Lebensdauerblock auf Druck 29-32 /
  PDF 32-35. `eta_22` tritt darin in **zwei verschiedenen Rollen** auf:
  (a) als globaler Faktor auf der linken Seite der Existenzzeitgleichung
  (21) und (b) innerhalb eines einzelnen Schlussglieds der Hilfsgröße
  `b_2` in (21f). Über (21a) geht `b_2` in `y` und damit in (21) ein.
* `b_2` ist in dieser Quelle daher primär eine Hilfsgröße der
  Existenzzeitformel, nicht eine selbständige „Massenkorrektur“. Eine
  Verbindung zur Masse besteht daneben, weil der Text aus derselben
  Lebensdaueranalyse die massenwirksame Größe `phi` in (21b) explizit
  angibt und später sagt, dass damit auch `M` nach (4) numerisch untersucht
  werden könne. Das macht den Gesamtblock gekoppelt, aber nicht `b_2`
  selbst zu einem additiven Massenterm.
* Das `eta_22`-Teilglied in `b_2` hat algebraisch einen Faktor
  `q(2-q)`. Sein `eta_22`-Anteil verschwindet deshalb bei `q=0` und `q=2`;
  zusätzlich verschwindet das ganze Schlussglied für die hier verwendeten
  nichtnegativen ganzzahligen `P<3` durch `binom(P,3)`. Dies ist eine lokale
  Formelaussage, keine Aussage über einen
  dynamischen Delta-Zwischenzustand. Der **globale** `eta_22`-Faktor in
  (21) bleibt davon unberührt.
* H014 enthält den gesamten Lebensdauer-/`b_2`-Block nicht. Seine
  Grundzustandstabelle II gibt nur Massen, nicht Existenzzeiten an. H014
  tabuliert `eta_22` trotzdem in Anhang B und verwendet es in einer eigenen
  Alpha-Internkorrektur. Das Vorkommen der Konstante im Anhang ist somit
  kein Nachweis, dass auch die Lebensdauerformeln bereits zu dieser Fassung
  gehören.

## 2. Quellenstatus und visuell geprüfter Umfang

| Kürzel | Quelle | geprüfte Seiten |
|---|---|---|
| H013 | Burkhard Heim, *Ausgewählte Ergebnisse einer einheitlichen Quantenfeldtheorie der Materie und Gravitation*, `J0033-Heim_Ausgewaehlte-Ergebnisse-b.pdf` | Druck 7 / PDF 7; Druck 29-37 / PDF 32-40; Tabelle II Druck 48 / PDF 51; Anhang B Druck 54 / PDF 57 |
| H014 | gleicher Titel und gleiche Autorenzeile, `J0032-Heim_Ausgewaehlte-Ergebnisse-a.pdf` | Druck 20-26 / PDF 22-28; Tabelle II Druck 39 / PDF 42; Anhang B Druck 41 / PDF 48 |

Beide Dokumente sind im geprüften Umfang undatierte Typoskriptscans. Aus
den Kennungen `J0032/J0033`, Uploadpfaden, Dateimetadaten, Seitenzahlen oder
dem unterschiedlichen Umfang wird keine Reihenfolge abgeleitet. Besonders
wichtig ist, dass gleiche Gleichungsnummern in beiden Fassungen nicht
notwendig dieselbe Formel bezeichnen: H013 (21) ist die
Existenzzeitbeziehung, H014 (21) dagegen bereits die Alpha-Gleichung.

## 3. Physikalische Bedeutungssetzung der Existenzzeit in H013

H013 Druck 7 / PDF 7 gibt zunächst eine qualitative Modellvorstellung. Die
zeitliche Stabilität beziehungsweise die Ausdehnung `x_4=i c t` einer
Elementarstruktur im Unterraum `R_4` bestehe nur so lange, wie ein Zustand
der internen Fluktuation periodisch wiederkehrt. Die Aufhebung dieser
Periodizität kennzeichne das zeitliche Stabilitätsintervall und bedeute den
radioaktiven Zerfall. Das ist die **physikalische Interpretation**, nicht
die algebraische Herleitung der späteren Gleichung.

H013 Druck 29 / PDF 32 präzisiert im Lebensdauerabschnitt:

* `T` ist die „zeitartige Begrenzung“ des Zustands in der Koordinate `x_4`
  des raumzeitlichen Unterraums `R_4`.
* `T_N=T(N)<=T` ist eine von `N` abhängige, noch unbekannte und ebenfalls
  zeitdimensionierte Funktion.
* Für den Grundzustand wird `T_0=0` gesetzt.

Danach heißt es, aus dem „anfangs zitierten Formalismus“ folge die
einheitliche Beziehung der Existenzzeiten (21). Auf der linken Seite steht
sichtbar

`eta_22 (1-sqrt(eta))^2 (1-sqrt(eta_11))^2`

`        (1-sqrt(eta_12))^2 (T-T_N)`.

Auf der rechten Seite stehen unter anderem `M`, `H`, die Substitution `y`,
Besetzungszahlen und der Selektor `delta(N)`. Der Text verweist für `M` auf
Gleichung (4), für `H` auf (12b) und für `delta(N)` auf (5e1). Für `N>0`
ist `delta(N)=0`, so dass (21) nur `T=T_N` ergibt. Die Quelle bezeichnet
`T_N` dann als Existenzzeit kurzlebiger Anregungen und Resonanzen.

Die Formulierung „folgt aus“ ist eine **Herleitungsbehauptung**. Auf den
geprüften Seiten wird jedoch keine vorgelagerte Rechnung gezeigt, welche
gerade den globalen Faktor `eta_22` oder seine Potenz in (21) erzwingt. Der
Autor definiert die Formel und ihre Größen und behauptet ihre Herkunft;
eine nachvollziehbare Ableitung dieses Faktors liegt hier nicht vor.

## 4. Die Kette (21) -> `y` -> `b_2`

### 4.1 `y` und die Rolle von `b_2`

Unmittelbar unter (21) definiert H013 Druck 29 / PDF 32 in (21a)

`y = F (phi + (-1)^s (1+phi) (b_1 + b_2/W_(N=0)))`.

Damit ist die Abhängigkeit eindeutig:

`b_2 -> y -> rechte Seite von (21) -> T-T_N`.

`b_2` ist also keine frei neben die Masse gesetzte Korrektur, sondern eine
von mehreren Substitutionen der Lebensdauerbeziehung. H013 Druck 30-31 /
PDF 33-34 definiert zunächst `phi`, `U`, `F`, `s`, `b_1` und schließlich
`b_2`. `b_2` ist eine lange, aus `B,H,C,k,q,P,Q`, der weiteren
Multiplettziffer und Konstanten zusammengesetzte zahlentheoretische
Funktion.

### 4.2 Das lokale `eta_22`-Glied in `b_2`

Am Ende von (21f), H013 Druck 31 / PDF 34, steht als letztes großes
Teilglied wort- und klammernah

`-(5/2) H^2 binom(P,3)`

` * { q [1 + (pi/3)(2-q) eta_22] B - (2-q)(1-q) }`.

Diese Stelle **verwendet** den zuvor definierten Konstantenwert `eta_22`;
sie leitet ihn weder neu her noch erklärt der anschließende Text, warum
gerade dieses Familienmitglied in `b_2` gewählt ist.

Für den `eta_22`-abhängigen Anteil allein ist der Zustandsfaktor

`binom(P,3) H^2 q(2-q) B`.

Daraus folgen ohne weitere Modellannahme:

* bei `q=0` verschwindet er durch `q`;
* bei `q=2` verschwindet er durch `(2-q)`;
* für die hier verwendeten nichtnegativen ganzzahligen `P<3` verschwindet
  das gesamte Schlussglied durch `binom(P,3)`.

Dies darf nicht zu „`eta_22` steht hier für einen realisierten
`q=2,k=2`-Zwischenzustand“ umgedeutet werden. Im Gegenteil: Der lokale
`eta_22`-Anteil dieses speziellen `b_2`-Glieds ist für die in die Formel
eingesetzte Ladungszahl `q=2` gerade algebraisch null. Eine mögliche Wirkung
des globalen `eta_22` in (21) ist eine **andere Formelrolle** und wird durch
diese Nullstelle nicht beseitigt.

Für den späteren Resonanzkontext ist `q=2` nicht nur eine externe
Rechenannahme: H013 Druck 37 / PDF 40 sagt bei der Erläuterung der Tabellen
IV bis Vb ausdrücklich: „Für die Delta-Zustände wurde q=2 verwendet.“
Damit ist die lokale Nullstelle des `eta_22`-Anteils in (21f) für diese
berichtete Delta-Tabellenauswertung quellenintern einschlägig. Sie beweist
weder die Identität eines `N>0`-Resonanzeintrags mit dem `N=0`-Grundzustand
noch eine berechenbare Delta-Lebensdauer; auf derselben Seitenfolge erklärt
H013 `T_N` für `N>0` gerade für unbekannt.

### 4.3 Klammerung am Übergang vom weiteren Multiplettterm zum `Q`-Term

Die direkte H013-Seite ist an der in H007 problematischen Stelle lesbarer.
Auf H013 Druck 31 / PDF 34 steht nach einem mit der weiteren
Multiplettziffer eingeleiteten Summanden sichtbar eine schließende
Klammerfolge vor `(k-1)` und danach ein neues `+ Q binom(P,2)(...)`. Die
visuelle Gliederung ist somit

`+ Kappa-like { ... + ... } (k-1)`

`+ Q binom(P,2) { ... }`

`-(5/2) H^2 binom(P,3) { ... eta_22 ... }`.

Das `Q binom(P,2)`-Glied steht in diesem Autorenscan nicht innerhalb der
vorherigen `Kappa`-Klammer. Dieser Befund ist eine
**Transkriptions-/Versionshilfe**, keine Erlaubnis, H007 B55 still zu
emendieren: H007 bleibt eine getrennte Herausgeberfassung und die Identität
sämtlicher übrigen Terme wurde hier nicht geprüft.

## 5. Warum der Block trotzdem mit der Masse gekoppelt ist

Unter (21a) sagt H013, eine Analyse der Existenzzeiten liefere den in (5e)
auftretenden, „massenwirksamen Anteil“ `phi` nun explizit. Gleichung (21b),
Druck 30 / PDF 33, gibt diesen Ausdruck; (21b1) bestimmt darin die
Hilfsgröße `U` mit einem `eta_(q,k)^2`-Faktor. Hier steht das
zustandsabhängige allgemeine Familienmitglied `eta_(q,k)`, nicht pauschal
der feste Wert `eta_22`.

H013 Druck 32 / PDF 35 erklärt anschließend ausdrücklich, durch (21b) und
(21b1) liege die Funktion `phi` aus (5c) zur Bestimmung von `M` nach (4)
ebenfalls explizit vor. Mit (4)-(8f1) und (21)-(21h) könnten Masse `M` und
Existenzdauer `T` der `N=0`-Komponenten numerisch ermittelt werden.

Die saubere Rollenverteilung ist daher:

* `b_2` wirkt über `y` unmittelbar in die Existenzzeitgleichung (21);
* `phi` ist der ausdrücklich als massenwirksam bezeichnete Anteil und die
  Brücke desselben Analyseblocks zurück zur Masse;
* daraus folgt eine gekoppelte Massen-/Lebensdauerkonstruktion, aber keine
  Gleichsetzung `b_2 = Massenkorrektur`.

H013 Druck 33 / PDF 36 sagt später, die mit der korrigierten
Feinstrukturkonstante berechneten Massen **und** Existenzzeiten seien in
Tabelle II zusammengestellt. Auch dies macht beide Ausgaben von gemeinsamen
Konstanten abhängig; es ändert die unmittelbare algebraische Rolle von
`b_2` nicht.

## 6. Grenzen, empirische Eingaben und numerische Behauptungen in H013

Die Quelle begrenzt ihren Geltungsanspruch an mehreren Stellen selbst:

1. H013 Druck 36 / PDF 39 sagt, das System für `N>0` sei noch unsicher;
   `z(N)` und daher `Q(N)` seien unbekannt. Auch die Existenzzeiten `T_N`
   solcher Zustände könnten „noch nicht beschrieben werden“.
2. Die dort tabulierten Resonanzmassen seien nur stark approximativ. Die
   Aussage, der Approximationsfehler bei `z=0` bleibe unter `0,1 MeV`, ist
   eine Quellenbehauptung und wurde hier nicht nachgerechnet.
3. H013 Druck 37 / PDF 40 nennt in (21b)/(21b1) gewisse frei verfügbare
   Konstanten - `fourth_root(2)`, `(pi/e)^2` und
   `4 pi fourth_root(1/2)` - ausdrücklich als an empirische Gegebenheiten
   angepasst. Die führende `4` in `fourth_root(2)` ist der Wurzelindex,
   kein zusätzlicher Multiplikationsfaktor.
4. H013 Druck 37 / PDF 40 dokumentiert für die approximierten
   Delta-Resonanztabellen ausdrücklich die Einsetzung `q=2`. Dies ist eine
   positive Quellenangabe zur dortigen Rechenkonvention, keine Aussage über
   die Identität der einzelnen `N=0`- und `N>0`-Zustände.
5. Tabelle II, Druck 48 / PDF 51, trägt die Überschrift „Theoretische
   Massen und Existenzzeiten der Elementarteilchen N=0“ und gibt
   numerische Lebensdauern aus. Das belegt die Anwendung des Formelblocks,
   nicht dessen unabhängige empirische Bestätigung.

Damit enthält H013 Definitionen, eine Herleitungsbehauptung und numerische
Anwendungsbehauptungen, aber zugleich unbekannte Funktionen und angepasste
Konstanten. Diese Statusarten dürfen nicht zu einer lückenlosen Ableitung
zusammengezogen werden.

## 7. H014: derselbe Konstantenname ohne Lebensdauerblock

H014 weicht an genau dieser Stelle substanziell ab:

* Druck 20-23 / PDF 22-25 behandelt Multiplettstrukturen und ihre
  Identifikation.
* Druck 24 / PDF 26 geht unmittelbar zur numerischen Massenbestimmung der
  `N=0`-Grundzustände und zu Tabelle II über. Eine Definition von `T`, `y`,
  `b_1` oder `b_2` erscheint in der geprüften Verbindung nicht.
* H014 Tabelle II, Druck 39 / PDF 42, heißt „Theoretische Massen der
  Elementarteilchen N=0“ und besitzt nur Spalten für theoretische und
  empirische Masse. Anders als H013 Tabelle II hat sie keine
  Lebensdauerspalte.

Dies ist nicht bloß ein fehlendes Scanblatt, sondern eine konsistente
inhaltliche Fassung ohne den H013-Lebensdauerblock: Prosa, Gleichungsfolge
und Ergebnistabelle gehen direkt über die Masse weiter.

Trotzdem enthält H014 `eta_22` an zwei positiven Stellen:

1. H014 Anhang B, Druck 41 / PDF 48, tabuliert unter den zu (2a), (2b),
   (7a), (7b), (4a) gehörigen Konstanten `eta_22=0,84242385`.
2. H014 Druck 26 / PDF 28 setzt in seiner Alpha-Internkorrektur (21a)

   `K_alpha = 1 - (1+eta_22)`

   `          * [(1-sqrt(eta))/(eta_11(1+sqrt(eta)))]^2`.

Diese H014-Form ist weder mit H013 (22a) noch mit H007 B59 ungeprüft
gleichzusetzen. Insbesondere steht hier `eta_11` innerhalb des quadrierten
Nenners; H013 Druck 33 / PDF 36 druckt stattdessen

`K_alpha = 1 - [(1+eta_22)/(eta eta_11 eta_12)]`

`          * [(1-sqrt(eta))/(1+sqrt(eta))]^2 * 3/(pi eta)`  (22a).

Schon die beiden undatierten Autorenfassungen besitzen also verschiedene
Alpha-Ausdrucksstrukturen und verschiedene Gleichungsnummern.

## 8. Anhang B: Definition/Numerik, keine Rollenherleitung

H013 Anhang B, Druck 54 / PDF 57, und H014 Anhang B, Druck 41 / PDF 48,
drucken übereinstimmend die Werte

`eta = 0,98998964`, `eta_11 = 0,98756399`,
`eta_12 = 0,98516776`, `eta_22 = 0,84242385`.

Die Tabellenüberschrift verweist auf die nummerierten Gleichungen (2a),
(2b), (7a), (7b), (4a). H013 Gleichung (7a), Druck 14 / PDF 15, definiert
die Familie `eta_(q,k)`; Einsetzen von `(q,k)=(2,2)` bestimmt daher den
tabulierten Zahlenwert. Der Anhang belegt:

* die Definition und numerische Auswertung des Familienmitglieds;
* die Stabilität dieses Zahlenwerts in beiden undatierten Fassungen.

Er belegt dagegen nicht:

* eine Herleitung des globalen Auftretens in der Existenzzeitgleichung;
* eine Herleitung des speziellen Auftretens im Schlussglied von `b_2`;
* eine gemeinsame Redaktionschronologie von H013, H014 und H007.

Die Gleichungsnummern über der Tabelle bezeichnen die Erzeugung bzw.
Numerierung der Konstanten, nicht eine vollständige Liste aller späteren
Verwendungsstellen.

## 9. Abhängigkeitskarte und begrenzter Vergleich zu H007

Die direkt belegte H013-Kette lautet:

`(7a) Definition eta_(q,k) -> eta_22 als (2,2)-Wert`

`              |`

`              +-> (21) globaler Existenzzeitfaktor`

`              +-> (21f) lokaler b_2-Term`

`                          -> (21a) y`

`                          -> (21) T-T_N`

`Lebensdaueranalyse -> (21b) massenwirksames phi -> (4) M`.

Diese Topologie entspricht strukturell der H007-Folge B47 (`T`), B48
(`y`) und B55 (`b_2`). Der Autorenscan H013 ist insbesondere für die
Gliederung des langen `b_2`-Ausdrucks eine positive Vergleichsstelle. Er
ist aber kein Nachweis, dass H007 wort- und formelidentisch aus genau diesem
Scan gesetzt wurde. Wegen der nicht gesicherten Versionsrelation darf H013
nur als Parallelüberlieferung, nicht als stilles Erratum für H007 verwendet
werden.

## 10. Gesicherte Befunde und offene Fragen

### Gesichert

1. `eta_22` ist in H013 globaler Faktor von (21) und lokaler Bestandteil
   eines `b_2`-Glieds in (21f).
2. `b_2` geht über `y` in die Existenzzeitformel ein.
3. Die Verbindung zur Masse läuft ausdrücklich über das aus der
   Lebensdaueranalyse gewonnene `phi`, nicht über eine Definition von
   `b_2` als Massenterm.
4. Der lokale `eta_22`-Anteil in `b_2` ist proportional zu `q(2-q)` und
   verschwindet daher bei `q=0` und `q=2`; H013 gibt für seine
   Delta-Resonanztabellen ausdrücklich die Verwendung von `q=2` an.
5. H013 kann `T_N` für `N>0` nach eigener Aussage nicht beschreiben und
   enthält empirisch angepasste Konstanten.
6. H014 enthält `eta_22`, aber nicht den H013-Lebensdauer-/`b_2`-Block.

### Offen / nicht behaupten

1. Warum `eta_22` gerade global in (21) und gerade lokal in (21f) gewählt
   wird, wird in den geprüften Seiten nicht hergeleitet.
2. Aus dem Symbol darf kein virtueller oder realer Delta-Zwischenzustand
   konstruiert werden.
3. Die lokale Nullstelle des `b_2`-Anteils beseitigt nicht den separaten
   globalen `eta_22`-Faktor in (21).
4. H013, H014 und H007 dürfen weder chronologisch noch algebraisch als eine
   einzige unveränderte Formelversion behandelt werden.
5. Die Quellenbehauptungen zur numerischen Übereinstimmung wurden hier
   nicht geprüft.

## 11. Visuelle Prüfspur und Suchgrenze

Für die unmittelbare Gegenlesung sind besonders wichtig:

* `tmp/pdfs/eta22_roles/j0033-hi-32.png` - H013 Druck 29 / PDF 32,
  Definition von `T,T_N`, (21) und (21a);
* `tmp/pdfs/eta22_roles/j0033-hi-33.png` - H013 Druck 30 / PDF 33,
  (21b)-(21e);
* `tmp/pdfs/eta22_roles/j0033-hi-34.png` - H013 Druck 31 / PDF 34,
  vollständiges (21f) mit `eta_22` und sichtbarer Klammergliederung;
* `tmp/pdfs/eta22_roles/j0033-limit-39.png` und
  `j0033-limit-40.png` - H013 Druck 36-37 / PDF 39-40,
  unbekannte `T_N`/`z(N)` und empirisch angepasste Konstanten;
* `tmp/pdfs/eta22_roles/j0032-26.png` - H014 Druck 24 / PDF 26,
  direkter Übergang zur reinen Massenauswertung;
* `tmp/pdfs/eta22_roles/j0032-28.png` - H014 Druck 26 / PDF 28,
  fassungseigene Alpha-Internkorrektur.

Ergänzend wurden die Vollseitenbilder
`tmp/pdfs/eta22_context/j0033-57.png` und `j0032-48.png` für Anhang B sowie
`delta-j0033-51.png` und `delta-j0032-42.png` für die unterschiedlichen
Tabellen II visuell geprüft.

Die Suche war auf die Seitenfolge um Existenzzeit, `y`, `b_2`, die
unmittelbaren Statuswarnungen, Tabelle II und die `eta_22`-Konstantentabelle
begrenzt. Nicht durchsucht wurden sämtliche Nachlassbestände, nicht
rekonstruiert wurden alle Summanden von (21f), und nicht geprüft wurden
moderne Messwerte oder die gesamte H007-Satzgeschichte. Negative Befunde
gelten nur innerhalb dieser abgegrenzten Autorenfassungen und Seitenketten.
