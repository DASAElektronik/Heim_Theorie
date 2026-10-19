# Gleichung (108) nach TRC/Kappe und der nachfolgende `F_S`-Block

Stand: 2026-09-07. Eng begrenzter Originalreview ohne neue Massen- oder
Empirieauswertung. Geprueft wurde, welchen Status die Buchquelle der Gleichung
(108) nach ihrer diskreten Exhaustionsvorschrift gibt und ob der anschliessende
`F_S`-Block eine Projektions- oder Restregel bereitstellt.

## 1. Ergebnis

Die Buchquelle schreibt (108) als Gleichheit und behandelt die daraus
gewonnenen Besetzungen als Resultat ihres Exhaustionsverfahrens. Auf den
geprueften Seiten wird aber **keine** eigene Regel angegeben, die nach einer
`TRC`-, Kappen- oder Transferentscheidung

- den verbleibenden Gleichungsrest benennt,
- ihn auf andere Terme verteilt,
- eine Toleranz fuer (108) festlegt oder
- die Gleichheit mit den schliesslich ganzzahligen `N_(j)` nochmals prueft.

Die Messbarkeitsschranke auf Druck 341 qualifiziert nur den besonderen
`0,99...99`-Fall des Operators `TRC`. Sie ist nicht als allgemeine
Resttoleranz fuer (108) formuliert.

Der anschliessende `F_S`-Block repariert einen solchen Rest ebenfalls nicht
ausdruecklich. Druck 342 bestimmt `F_S` zunaechst empirisch aus zugeordneten
Massen und sucht danach eine passende Funktion der diskreten
Protosimplexkennzahlen. Bereits Druck 323 setzt fuer die Variation der
Besetzungszahlen `delta F_S=0`, weil `F_S` zwar von Quantenzahlen, aber nicht
von den `n_j` abhaengen soll. `F_S` ist damit im dargestellten Quellengang ein
nachgeschalteter Massenterm, keine ausgewiesene Projektionsvariable von (108).

Der quellennahe Status lautet daher nicht „(108) ist nach `TRC` widerlegt“,
aber auch nicht „die Quelle beweist den exakten Gleichungserhalt“. Belegt ist
eine als Auswahlgleichung gesetzte (108) plus eine diskrete Auswahlvorschrift;
eine ausdrueckliche post-diskrete Restbehandlung fehlt im geprueften Umfang.

## 2. Quelle und Sichtumfang

Primärquelle:

`01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`

SHA-256:
`F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.

Vollstaendig visuell gelesen:

- Druck 340--347 / PDF 346--353;
- konkreter Rueckanker Druck 323 / PDF 329, weil dort die Rolle von `F_S`
  waehrend der Besetzungsvariation festgelegt wird.

Arbeitsbilder:

- `tmp/pdfs/eq108_status/edm2-346.png` bis `edm2-353.png`;
- `tmp/pdfs/coupled_existence/edm2-329.png` fuer Druck 323.

Nach diesen acht fortlaufenden Seiten und dem einen sachlich notwendigen
Rueckanker wurde die Suche beendet. Der Befund ist deshalb kein werkweiter
Nichtexistenzbeweis fuer jede denkbare Projektionsdeutung.

## 3. Der von der Quelle gesetzte Gleichungsstatus

Druck 340 setzt zunaechst

```text
W1 = W*(1+f)
```

und schreibt die Auswahlbeziehung ohne Naeherungszeichen:

```text
alpha1*N1^3 + alpha2*N2^2 + alpha3*N3
  + exp[-(2k-1)*N4/(3Q4)] = W1.                 (108 im Anschluss)
```

Der vorausgehende Satz sagt, mit (108)--(110d) koennten fuer jeden
`V6`-Punkt die Groessen `W`, `a` und `b` numerisch bestimmt werden. Das ist
der von der Quelle beanspruchte konstruktive Rahmen. Es ist noch keine
separate Aussage darueber, ob jede nachfolgende Ganzzahlprojektion die
angezeigte reelle Gleichheit exakt erhaelt.

Fuer die ersten drei Zonen definiert Druck 340/341 ein gestuftes
Exhaustionsverfahren:

```text
alpha1*N1^3 <= W1,       W2 = W1-alpha1*N1^3,
alpha2*N2^2 <= W2,       W3 = W2-alpha2*N2^2,
alpha3*N3   <= W3,       W4 = W3-alpha3*N3.
```

Die Ungleichungen und Restdefinitionen sind exakt gedruckt. Die Auswahl der
maximalen ganzen `N1,N2,N3` ist jedoch bereits eine diskrete
Zaehentscheidung, keine stetige Umkehrung aller vier Summanden zugleich.

## 4. Logarithmische Umkehrung und diskrete Auswahl sind zwei Schritte

Druck 341 definiert vor der Ganzzahlwahl den reellen Zwischenwert `W5`:

```text
(2k-1)*W5 = -3*Q4*ln(W4).
```

Nur im regulaeren Fall waere die unbeschnittene reelle Umkehrung genau auf
den Exponentialterm abgestimmt. Danach setzt die Quelle je nach Zweig

```text
N4 = TRC(W5)
```

oder bei `W4=0` beziehungsweise `W5>alpha3*N3` eine gekappte
Maximalbesetzung aus `TRC(alpha3*N3)`, gegebenenfalls vermindert um eins zur
Beruecksichtigung von `beta4=1` aus (107a).

Fuer den bei `k=2` moeglichen negativen `W5` beschreibt Druck 341/342 einen
Transfer aus Zone 3, bildet `W6` und setzt anschliessend `N4=TRC(W6)`. Diese
Regeln bestimmen eine zulaessig gedachte ganzzahlige Besetzung. Die Seiten
fuehren aber kein Symbol fuer

```text
W1-[alpha1*N1^3+alpha2*N2^2+alpha3*N3+exp(...)]
```

ein und geben keine nachgeschaltete Kompensation dieses Ausdrucks an.

Das ist die enge Quellenluecke: Nicht die diskrete Vorschrift fehlt, sondern
eine ausdrueckliche Bruecke von ihrer ganzzahligen Ausgabe zur erneut exakt
erfuellten Ausgangsgleichung.

## 5. Was die Messbarkeitsschranke qualifiziert

Die Definition von `TRC` auf Druck 341 verlangt grundsaetzlich Abschneiden
statt Aufrunden. Nur eine Neunerfolge in `0,99...99`, die bis unter eine
Messbarkeitsschranke reicht, soll als `1` behandelt werden; als normales
Beispiel steht `TRC(e)=2`.

Aus diesem Wortlaut folgt nur eine besondere Dezimalentscheidung fuer den
Integeroperator. Nicht gedruckt sind:

- ein Zahlenwert der Messbarkeitsschranke;
- ein Fehlerintervall fuer (108);
- eine Regel „Rest kleiner als Messbarkeitsschranke gilt als null“;
- eine Fehlerfortpflanzung vom `TRC`-Argument auf die linke Seite von (108).

Eine solche Toleranzdeutung waere daher eine Rekonstruktion, keine auf diesen
Seiten ausgesprochene Quellenregel.

## 6. Rueckrechnung und `F_S`: getrennte Ebenen

Druck 342 erklaert nach Abschluss der Exhaustion:

```text
n_j = N_(j)-Q_j.
```

Mit diesen `n_j` werden die `G_j` in (98d)/(98e) ermittelt. Erst danach
wechselt der Text zur numerischen Bestimmung von `M_x-mu_S*F_S` fuer die
`N=0`-Gitterpunkte.

Die Quelle sagt ausdruecklich, `F_S` koenne zunaechst empirisch aus den
vorliegenden Messmassen `M_emp` gewonnen werden. Sie stellt dazu sinngemaess

```text
mu_S*F_S = M_emp-mu_+*(sum_j alpha_j*G_j + q*alpha_-/alpha_+)
```

auf. Da solche Werte nur fuer 17 Komponenten vorlaegen, sei eine Funktion
`F_S(k,P,Q,kappa,q)` zu suchen, welche diese Messpunkte trifft und fuer die
noch nicht belegten Komponenten plausible Werte liefert. Druck 342/343
schlaegt dafuer Hilfsfunktionen und Konstanten vor; die Form habe sich als
besonders guenstig erwiesen.

Das ist eine klar bezeichnete empirische Anpassungsaufgabe innerhalb der
Massenformel. Es ist keine Anweisung,

```text
F_S := Rest von (108)
```

zu setzen oder `F_S` beim Exhaustionsschritt zu veraendern.

Der sachlich direkte Rueckanker steht auf Druck 323. Dort soll `F_S` zwar in
irgendeiner Form von den Quantenzahlen des `V6`-Punktes abhaengen, aber auf
keinen Fall von den `n_j`. Fuer die verwendete Variation folgt deshalb

```text
delta F_S = delta q = 0.
```

Gerade dadurch verschwindet `F_S` aus der lokalen Besetzungsgleichung, aus
der spaeter (108) hervorgeht. Diese Aussage gilt fuer die dort definierte
Variation; sie ist keine Behauptung, `F_S` sei im gesamten Massenspektrum
numerisch null.

Druck 343 sagt zusaetzlich, die `n_j` entstuenden nach (108) durch die
Exhaustionsmethode unabhaengig von dem dort klein gedruckten `f`. Die Seite
fuehrt in (111) zugleich `phi` ein, identifiziert aber weder dieses `f` mit
`F_S` oder `phi`, noch erklaert sie den Rueckverweis an dieser Stelle neu.
Moeglicherweise betrifft der Satz die Formunabhaengigkeit des Algorithmus
gegenueber der Resonanzfunktion; das wurde im gesetzten Seitenumfang nicht
weiter aufgeloest. Er wird deshalb hier **nicht** als Beleg fuer die
`F_S`-Unabhaengigkeit verwendet. Diese stuetzt sich allein auf die
Variationsaussage von Druck 323 und die nachgeschaltete empirische Rolle von
`F_S` auf Druck 342.

## 7. Druck 344--347 fuehrt zu einer anderen Fragestellung

Druck 344 fasst die Massenterme zu einer Spektralfunktion `M(N)` in (112)
zusammen und behauptet eine numerische Ermittlung der ponderablen Massen mit
dem Umfeld (108)--(111b). Danach wechselt der Text zu den oberen Grenzen der
Resonanzspektren.

Druck 345/346 ist in diesem Grenzabschnitt ausdruecklich heuristischer:

- Maximalanstiege werden nur als in der Groessenordnung vergleichbar
  beschrieben (`ungefaehr`);
- ein Zusammenhang mit einem Faktor `S` wird erwartet;
- der Faktor muesse von Symmetriekennzahlen abhaengen;
- mehrere aus beobachteten Massen gebildete Verhaeltnisse werden wiederum
  nur naeherungsweise als kleine ganze Zahlen gelesen;
- daraus entstehen (113) und die Maximalbesetzungen (113a).

Diese Motivations- und Anpassungssprache darf nicht rueckwirkend als Beweis
des exakten Gleichungserhalts von (108) etikettiert werden.

Druck 346 setzt fuer die Grenzbesetzungen mit (113b) erneut eine formal
exakte Gleichheit derselben kubisch-quadratisch-linear-exponentiellen Form.
Druck 347 sagt, `M_L` werde aus `L_N` durch das Exhaustionsverfahren, `M_max`
aber aus den `L_j` nach (113)/(113a) bestimmt. Die Seite diskutiert dann
positive Restbandbreiten bis zum Maximalniveau sowie noch unbekannte
Spin-/Ladungsanregungen. Sie formuliert weder fuer (108) noch fuer (113b)
eine Projektionstoleranz oder Restkorrektur nach `TRC`.

## 8. Statusmatrix der Aussagen

| Gegenstand | Quellenstatus im geprueften Umfang | Nicht daraus abzuleiten |
|---|---|---|
| (108) | als Gleichheit gedruckt und als Auswahlprinzip verwendet | mathematischer Beweis exakter Erfuellbarkeit fuer jede Eingabe |
| `W2,W3,W4` | exakte Restdefinitionen nach maximaler ganzzahliger Auswahl | bereits vollstaendige Loesung des Exponentialglieds |
| `W5` | exakte reelle logarithmische Umkehrung bei zulaessigem `W4` | Ganzzahligkeit von `W5` |
| `TRC`/Kappe | ausdrueckliche diskrete Auswahl-/Saettigungsregel | allgemeine Projektions- oder Residualnorm |
| Messbarkeit | Sonderqualifikation der Neunerfolge bei `TRC` | Toleranzband fuer die Gesamtgleichung |
| `F_S` | empirisch bestimmbarer, quantenzahlabhaengiger Massenterm | Restvariable oder Korrektor der Besetzungsgleichung |
| (113)/(113a) | heuristisch motivierte Maximalbesetzungsbeziehung | rueckwirkende Reparatur eines Restes in (108) |
| (113b) | erneut als Gleichheit gesetzte Grenzbeziehung | post-`TRC` Gleichheitssicherung |

## 9. Belastbare Schlussformulierung

Quellenfest ist folgende abgestufte Aussage:

1. Heim setzt (108) als Gleichheit und leitet daraus ein diskretes
   Exhaustionsverfahren zur Bestimmung der `N_(j)` ab.
2. Das Verfahren enthaelt ausdrueckliche Restgroessen, logarithmische
   Umkehrung, `TRC`, Kappung und einen Transferzweig.
3. Fuer die schliesslich ganzzahligen Ergebnisse wird auf Druck 340--347
   keine gesonderte Projektion, Toleranz oder Restkompensation angegeben.
4. `F_S` ist nach Druck 323 von dieser Besetzungsvariation getrennt; Druck
   342 richtet seine Bestimmung empirisch auf den Massenterm, und Druck 343
   setzt den vorgeschlagenen Funktionsaufbau fort.
5. Ob eine nicht ausgesprochene Interpretation die diskrete Auswahl nur als
   Naeherung meint, bleibt offen; sie darf weder als Quellenbeweis noch als
   Autorenfehlerursache ausgegeben werden.

Damit ist ein konkret berechneter post-diskreter Rest eine legitime
Rekonstruktionsdiagnose. Er ist aber von der Quellenbehauptung, der
physikalischen Interpretation und der spaeteren empirischen `F_S`-Anpassung
sauber getrennt zu dokumentieren.
