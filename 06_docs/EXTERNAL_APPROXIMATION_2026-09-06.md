# Externzonennaeherung: Quellenbruecke und gemeinsamer Fehlertransport

2026-09-06, Etappe 33. Ausgang `df9dff6`, Plancheckpoint `3185574`.
Vertrag: [EXTERNAL_APPROXIMATION_PLAN](../00_admin/EXTERNAL_APPROXIMATION_PLAN.md).
Quellenumfang: [Lesenotiz](../03_notes/EXTERNAL_APPROXIMATION_SOURCES_2026-09-06.md).

## Ergebnis zuerst

Heim beschreibt die Nullpunkt- und Geruestnormierung des Externterms
ausdruecklich. Es waere falsch, hier eine voellig fehlende Normierung zu
behaupten. Die spaetere Abklingkonstante `A(1)=1/3` wird auf Druck S. 325
hingegen ausdruecklich heuristisch ausgewaehlt. Eine quantitativ nachrechenbare
Uebertragung der raeumlichen Naeherung (79b)/(79c) auf die Besetzungsvariable
`N_(4)` und deren Fehler haben wir im geprueften Anschluss nicht gefunden.

Eine eigene bedingte Fehlerrechnung zeigt nun, wie eine begruendete
Aenderung auf BEIDEN Seiten von (108) wirken muesste. Sie beruecksichtigt
auch den zuvor subtrahierten Nullpunkt. Noch ist keine solche physikalische
Korrekturfunktion oder Fehlerschranke hergeleitet. Deshalb weder eine
korrigierte Besetzung noch einen naeherungsrobusten physikalischen
Ausschluss behaupten. Der bisherige bedingte Skalarbeweis bleibt bestehen.

## 1. Quellenkette und ihre Grenze

Primaerquelle ist H004, Burkhard Heim, *Elementarstrukturen der Materie II*,
lokale Ausgabe 1996. Die folgende Rekonstruktion schreibt Heims belegte
Formeln und Motivation ihm zu; Fehleridentitaeten, Tests und Robustheitssatz
weiter unten sind unsere eigene Untersuchung.

### Raeumliche Ausgangsform: Druck 175-179 / PDF 181-185

(79) enthaelt einen tensor-/feldseitigen Vorfaktor sowie Exponential- und
Klammerterme mit `lambda_(kl)`, `a`, `K=lambda*T` und `b=cos(K)`. Im
Grenzuebergang `tau -> 0` wird `lim(mu;n)=r` verwendet. Fuer grosses `r`
mit `exp(lambda*r) >> b` und `>> 1` ergibt sich die Form
`psi(r) ~ exp(-alpha*r)`, `alpha>0`, in (79b).

Die Buchnotation verwendet Zeichen mehrfach: der Abklingexponent in (79b)
ist `alpha=a-lambda`. Davor erfuellt die reelle Selektorkomponente am
Extremum `alpha=lambda_(kl)/a=A`; `A` dient dort als Quotientenabkuerzung.
Diese Extremumbedingung darf nicht mit dem spaeteren Abklingexponenten
gleichgesetzt werden. Auch `A(k)` im Besetzungsterm und die Matrixkomponente
`A16` sind davon zu unterscheiden. Die Originalzeile auf Druck 178 wurde
nach einem Notationshinweis in der Abschlussreview erneut vollseitig gelesen.

(79c) nennt fuer grosse Metronenzahlen `nu` bei `tau>0` den Anschluss
`r=r(nu)` und `delta r -> beta=const>0`. Das ist keine exakte affine
Zuordnung fuer beliebige Indizes. Insbesondere steht dort nicht `nu=N4`.

Die bereits in Etappe 9 untersuchte eigene skalare Normalisierung von (79)
besitzt eine bedingte asymptotische Restschranke. Sie wird hier nicht als
neuer Fund gezaehlt. Siehe [EXPONENTIAL_CONTEXT](EXPONENTIAL_CONTEXT_2026-09-06.md).
Ihre Anwendung auf `N4` benoetigt aber weiterhin eine Variablen-/Skalenbruecke,
Parameterbereiche und eine Verbindung der Feldamplitude zur Selektornormierung.

### Anwendung auf die Externzone: Druck 322-325 / PDF 328-331

Heim begruendet die Verwendung von (79b)/(79c) fuer die aeussere Sigma-Zone
mit der dort angenommenen sehr guten Gueltigkeit der dritten Region. Er
setzt den Verlauf `mu_+*exp(-A*N4)` an. Damit ist eine kontextuelle
Formuebertragung belegt, nicht eine ausgesprochene Gleichung `r=N4` oder
`A=alpha`.

Druck 323 subtrahiert den leeren Bezugszustand:

```text
Delta = mu_+ * (exp(-A*N4) - 1)
mu_+ * W = delta M + Delta.
```

Mit `alpha4=1` und `delta4 G4=1` hebt sich der konstante Beitrag der
vierten Zone gegen die `-1` heraus. In unserer Kurznotation entsteht

```text
P(N) + exp(-A*N4) = W,
P(N) = a1*N1^3 + a2*N2^2 + a3*N3.
```

Hier und im Folgenden steht `Nj` fuer die Buchbesetzung `N_(j)`, `aj`
fuer `alpha_j`, nicht fuer die Feinstrukturkonstante. Die Gleichsetzung
ueber `mu_+` ist die im Text gewaehlte Proportionalitaetsnormierung. Sie
beweist nicht, dass der volle Vorfaktor von (79) exakt `mu_+` ist.

### Drei verschiedene Bezuege

| Bezug | Buchbedingung | Bedeutung fuer den festen Fall |
|---|---|---|
| Leerer Bezugszustand, S. 322-323 | `N_(j)=0`, also `n_j=-Q_j` | Externe Differenz `Delta(0)=0`; keine Aussage `T(0)=0` fuer die ganze Summe |
| Geruest, S. 325 | `n_j=0`, also `N_(j)=Q_j` | Referenzsumme `g`; hier `Q4=1`, nicht 0 |
| Resonanzgrundordnung, S. 326-327 | Resonanzindex `N=0`, `f(0)=0` | Nicht gleichbedeutend mit leeren Zonen oder `n_j=0` |

Druck 325 setzt

```text
B = a1*Q1^3 + a2*Q2^2 + a3*Q3
g = B + exp(-A*Q4)
W/g = w, also W = g*w.
```

Fuer das Geruest ist `w=1`. Unser vorher fixierter aktiver
Pseudosingulettfall hat dagegen `w=1+eta11*A16`, nicht `w=1`.
(108)/(108a) auf Druck 330 wiederholt diesen Anschluss.

## 2. Warum gerade A(1)=1/3?

Druck 324 trennt `A=A(k)` von `ln(xi)`. Auf Druck 325 folgt eine eigene
Konstruktion, nicht eine numerische Auswertung des raeumlichen Exponenten:

1. Fuer `k=2` wird am Geruest `exp(-A*Q4)=1/e` angenommen. Mit `Q4=15`
   folgt `A(2)=1/15`.
2. Fuer `k=1`, `Q4=1`, wird `A(1)=z/15` angesetzt, mit positivem ganzem
   `1<=z<15` und der Forderung, dass 15 durch z teilbar ist.
3. Die Teiler sind `z=1,3,5`. Die daneben geforderte strikte Ordnung
   `A(1)>A(2)` schliesst `z=1` aus; uebrig bleiben `z=3,5`.
4. Die Entscheidung fuer `z=5` wird ausdruecklich als heuristisch bezeichnet.
   Heim verknuepft sie damit, dass `xi` als Limes den Naeherungsverlauf des
   `(+7)`-Feldes nach (79b)/(79c) bestimmt habe, und zieht dann
   `(2*xi-1)^2=5` unter Verweis auf (96b) heran.
   Damit `A(1)=1/3`; zusammen schreibt Heim `3*Q4*A(k)=2*k-1`.

Der Verweis auf (96b) wurde hier auf S. 325 gelesen, nicht seine
urspruengliche Herleitung neu untersucht. Die Identitaet mit 5 erklaert die
genannte Motivation, erzwingt aber aus den aufgefuehrten Teilerbedingungen
allein keine Wahl zwischen 3 und 5.

Eine enge Wortlautauffaelligkeit bleibt: Der Ausschlusssatz fuer `z=1`
spricht von identischem `Q4*A` fuer beide k. Mit den genannten Werten waere
stattdessen `A` identisch, waehrend die Produkte `1/15` und `1` verschieden
sind. Das wird als lokale Wortlaut-/Algebradifferenz festgehalten, nicht
als autorisiertes Erratum geglaettet oder als weiterer unabhaengiger
Theoriefehler gezaehlt. Die vorangestellte strikte A-Ordnung ist separat.

Weder `A(1)=1/5` noch irgendein angepasster Wert wurde jetzt in eine
Besetzungsrechnung eingesetzt. Die alten Profile behalten `A(1)=1/3`.

## 3. Eigene bedingte Fortpflanzung: drei Punkte statt nur eines

Voraussetzungen: feste `mu_+`-Skala, `alpha4=1`, feste `aj` und `w`,
unveraenderte Nullpunkt- und Geruestbehandlung. Fuer den festen k=1-Fall
sei eine noch nicht hergeleitete dimensionslose Ersatzfunktion

```text
Phi(x) = exp(-x/3) + h(x).
```

`Phi` ist unsere Notation, weder Heims Strukturfunktion `F_im` noch seine
Resonanzfunktion. Bewahrt man die gedruckte Subtraktion am Nullpunkt, gilt

```text
T_Phi = P + 1 + Phi(N4) - Phi(0)
g_Phi = B + 1 + Phi(1)  - Phi(0)
W_Phi = w*g_Phi
R     = T-W

R_neu - R_alt = h(N4) - w*h(1) + (w-1)*h(0).
```

Das ist eine exakte algebraische Identitaet innerhalb unserer bedingten
Erweiterung. Sie ist keine Behauptung, dass Heim eine beliebige solche
Funktion zuliesse. Der Nullpunktterm darf nur entfallen, wenn `h(0)=0`
oder bereits mit der normalisierten Korrektur gerechnet wird:

```text
delta(x) = h(x)-h(0), delta(0)=0
R_neu-R_alt = delta(N4)-w*delta(1).
```

Konsequenzen:

- Eine ueberall konstante ROHE Aenderung `h=c` hebt sich exakt heraus.
  Eine ueberall konstante nichtnullige `delta` waere mit `delta(0)=0`
  unvereinbar. Gleiche effektive Fehler an zwei verschiedenen positiven
  Argumenten sind dagegen moeglich und wirken dort mit `(1-w)*delta`.
- Bei `N4=0` ist die Aenderung `-w*delta(1)`; bei `N4=1` ist sie
  `(1-w)*delta(1)`. Derselbe Funktionswert darf nicht zweimal unabhaengig
  variiert werden. Der Rechner fasst gleiche Argumente zuerst zusammen.
- Intervallhuellen unabhaengiger Punktfehler sind aeussere Schranken;
  sie beweisen nicht, dass eine erlaubte Feldfunktion alle Eckwerte erreicht.
- Eine Aenderung nur links bei festgehaltenem `g/W` untersucht einen
  anderen Vertrag und kann sogar eine andere Aenderungsrichtung ergeben.

Fuer beide unveraenderten Buchprofile ist rational zertifiziert:

```text
73.1277926806 < w < 73.1277926811.
```

Dies ist ein dimensionsloser algebraischer Multiplikator, kein gemessener
Fehler oder allgemein gueltiger Verstaerkungsfaktor: Korrelationen koennen
Beitraege aufheben. Root bestaetigte das Intervall ausserdem mit der
unabhaengigen Fraction-Kette der Etappe-32-Numerikreview.

### Falls weitere Eingaben mitgeandert werden

Fuer effektive, nullpunktnormierte `delta`, `g_alt=B+exp(-1/3)` und
`dP=sum(da_j*N_j^(4-j))`, `dB=27*da1+9*da2+2*da3` gilt allgemeiner:

```text
dR = dP + delta(N4) - w*(dB+delta(1))
     - dw*(g_alt+dB+delta(1)).
```

Gemischte Terme sind enthalten. Diese Erweiterung wurde nur synthetisch
geprueft; weder `aj` noch `w`, `A16`, `Y9` oder die Massenskala wurden
in den Buchprofilen veraendert.

## 4. Was wuerde den alten Ausschluss robust machen?

Der eigene Beweis aus [Etappe 32](COUPLED_EXISTENCE_2026-09-06.md) liefert
fuer beide festen Profile auf der gesamten Menge D mit nichtnegativen
ganzzahligen `N1,N2,N3`, reellem `N4>=0` und den ersten zwei direkten
ungewichteten Strukturgates:

```text
|R_alt| >= L, L = 0.057144067635.
```

Die Gates und der nichtkollabierte Vertrag sind wesentlich. Dies ist
keine Aussage fuer jedes Tupel in einem beliebigen Suchrechteck.

Eine nachgewiesene UNIFORME Schranke auf D

```text
|delta(N4)-w*delta(1)| <= E < L
```

wuerde per Dreiecksungleichung `|R_neu|>=L-E>0` ergeben. Bei einzelnen
effektiven Fehlergrenzen ist `E=eps_N+w*eps_1` eine ausreichende aeussere
Schranke. Fuer rohe Fehler und hier `w>1` lautet sie dagegen
`E=eps_N+w*eps_1+(w-1)*eps_0`. Funktionale Korrelationen oder gerichtete
Fehlerintervalle koennen schaerfere Kriterien liefern.

Wichtig fuer die Umkehrung: Ein tatsaechlicher neuer Nullpunkt braucht
`dR=-R_alt`, also `|dR|>=L`; das ist nur notwendig. Eine OBERE Fehlerschranke
`E>=L` beweist weder eine ausreichend grosse wirkliche Aenderung noch einen
Nullpunkt. Unser Test ist dann lediglich unentschieden.

Auch die alte endliche Obermenge `N4<=25` darf nicht ungeprueft fuer die
korrigierte Suche benutzt werden: Sie wurde mit der ALTEN Gleichung und
ihrem W hergeleitet. Eine lokale Fehlerkontrolle nur auf `[0,25]` genuegt
ohne neue Bereichsherleitung nicht. Globale Kontrolle fuer `N4>=0` waere
hinreichend; alternativ ist ein neuer Bereichsausschluss zu beweisen.

## 5. Was fuer einen physikalischen Fehlerrahmen noch fehlt

Im hier geprueften Quellenanschluss fehlen fuer die konkrete Rechnung:

1. Die nachpruefbare Zuordnung von `r` beziehungsweise `nu` zu `N4`,
   einschliesslich ihrer Skala und ihres Geltungsbereichs.
2. Die zugehoerigen Feldparameter und die Uebertragung des vollstaendigen
   Vorfaktors zur gewaehlten `mu_+`-Normierung.
3. Ein Fehlernachweis nicht nur an der gesuchten Besetzung, sondern auch
   am leeren Bezug und am Geruest; gegebenenfalls eine gesondert begruendete
   Referenznormierung ausserhalb der raeumlichen Asymptotik.
4. Der Nachweis, welche anderen Koeffizienten bei dieser Revision fest
   bleiben duerfen und ob die direkte Struktur-/Kollapsbehandlung gilt.

Eine qualitative Gueteaussage oder beliebig hohe Rechengenauigkeit ersetzt
diese Voraussetzungen nicht. Dies ist ein lokaler Anschlussbefund, kein
Nachweis, dass das ganze Werk oder spaetere Arbeiten diese Fragen nie loesen.
Auch Heims Kenntnis oder Bearbeitungsstand bis zu seinem Lebensende folgt
daraus nicht; die historische Notiz bleibt unveraendert offen.

## 6. Reproduktion und Sicherung

```powershell
py -3.13 -B scripts/audit_external_error_transport.py --check
py -3.13 -B scripts/audit_coupled_existence.py --check --verify-sources
py -3.13 -B -m unittest discover -s tests -q
py -3.13 -B scripts/validate_finding_register.py
```

16 neue exakte Tests, 304 insgesamt bestanden. Alle 12 bestehenden
Ergebnissnapshots stimmen weiterhin mit frischer Rechnung ueberein;
Quellhash und alter Existenznachweis wurden erneut geprueft. Alte Massen
werden dabei nur als Regression wiederholt, keine neue Massenrechnung
oder neue Parametersuche eingefuehrt. Neuer Rechner schreibt keine Dateien.

Drei interne Agentenreviews: Quellenform, Normierung, Fehleralgebra. Root
las die tragenden Originalvollseiten und alle Reviews, wiederholte den
selbstenthaltenen 179-Fraction-Kontrollblock und die unabhaengige alte
Intervallkette einschliesslich beider w-Einschluesse. Nach Codegegenreview
wurde der CLI-Wortlaut fuer rohe versus normalisierte Fehler praezisiert.
Interne Gegenpruefung ist kein externes Peer Review; Tests allein sind
keine physikalische Validierung. FIND-043 ist eine zusammenhaengende
Befundgruppe, nicht ein weiterer unabhaengig gezaehlter Theoriefehler.

## 7. Naechster begrenzter Auftrag

Die Quellenmotivation fuer `z=5` hat jetzt einen konkreten Rueckverweis:
(96b). Dessen Begruendung und Bezug zur Sigma-Zone gezielt pruefen. Falls
dadurch keine zusaetzliche Auswahlbedingung entsteht, waere eine VORHER
festgeschriebene Sensitivitaetsdiagnose der beiden bereits gedruckten
Kandidaten `A(1)=1/5` und `1/3` sinnvoll. Dabei Externterm UND `g/W`
gemeinsam aendern, die alten Profile erhalten, neue Bereichsgrenzen beweisen
und keine Auswahl nach Rest oder Masse treffen.

Das waere eine eigene Robustheitsfrage, keine hergeleitete Feldkorrektur
und kein Heim-Erratum. In dieser Etappe wurden diese Alternativen nicht
ausgerechnet. Eine echte (79)-Fehlerfortpflanzung erst bei neuer belastbarer
Variablen-/Parameterbruecke wieder aufnehmen.
