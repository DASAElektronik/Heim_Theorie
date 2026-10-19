# Mathematikreview der gewoehnlich-skalaren Abbildung von (79)

Stand: 2026-09-06. Unabhaengige Algebra, Asymptotik und numerische
Gegenpruefung der uebergebenen scalarisierten Funktion. Keine eigene
Quellbildkontrolle und keine Implementierung oder Validierung metronischer
Operatoren. Die Quelllesungen zu EDM2 Druck175-179, besonders (79)/(79a)
und Druck178, wurden vom Hauptagenten und Quellenreview uebergeben.

## 1. Explizite Voraussetzungen und Notation

Hier gelten ausschliesslich gewoehnliche reelle/komplexe Zahlen mit
kommutativen Produkten, gewoehnlicher Exponentialfunktion und Ableitung:

```text
lambda>0, a>0, -1<b<1, r>=0,
x=lambda*r, p=a/(2*lambda)>0, t=exp(-x), w=exp(x)=1/t.
```

lambda und a haben dieselbe Einheit, naemlich die inverse Einheit von r;
x, p, b und H sind dimensionslos. lambda ist hier eine Exponentialrate,
nicht die Wellenlaenge frueherer Audits. a und b sind keine der alten
eta-Konstanten. Die Scalarisierung setzt E=1 und waehlt H(0)=1; sie
behauptet keine autorisierte Ersetzung der Buchoperatoren durch Skalare.

Das untersuchte Quellenbild lautet unter diesen Zusatzannahmen

```text
H(r) = exp(x)*[(1+b)/2*(1+(exp(x)-b)^2/(1-b^2))]^(-p)
     = exp(x)*[(exp(2x)-2b*exp(x)+1)/(2*(1-b))]^(-p).
```

Die Klammer ist positiv, weil ihr Zaehler `(w-b)^2+(1-b^2)>0` ist.
Bei r=0 ist die Klammer genau 1, daher H(0)=1. Saemtliche Potenzen
bezeichnen hier den positiven reellen Zweig.

Der Bereich negativer b wird nur als zulaessiger Bereich dieser skalaren
Formel betrachtet. Er ist nicht automatisch der im Quellenkontext
gewaehlte Winkelzweig `0<K<pi/2`, der b=cos(K)>0 liefert.

## 2. Rate, Amplitude und relativer Fehler

Durch Herausziehen von exp(2x) folgt die exakte Faktorisierung

```text
H(r) = M_79 * exp((lambda-a)*r) * (1-2b*t+t^2)^(-p),
M_79 = [2*(1-b)]^p > 0.
```

Fuer festgehaltene Parameter und r gegen unendlich gilt deshalb

```text
H(r) ~ M_79*exp((lambda-a)*r),
lim log(H(r))/r = lambda-a.
```

Das Zeichen `~` bedeutet in dieser Review, dass der Quotient gegen 1
geht. Die konstante Amplitude darf unter dieser Bedeutung nicht ohne
Kommentar weggelassen werden. Fuer den logarithmischen Exponenten oder
das Vorzeichen der Wachstumsrate ist sie dagegen unerheblich.

Mit `H_lead=M_79*exp((lambda-a)*r)` ist der hier verwendete relative
Rest exakt definiert als

```text
E_rel = H/H_lead - 1
      = (1-2b*t+t^2)^(-p)-1
      = 2p*b*t + [-p+2p*(p+1)*b^2]*t^2 + O(t^3).
```

Wer den relativen Approximationsfehler andersherum als
`(H_lead-H)/H` definiert, erhaelt stattdessen
`(1-2b*t+t^2)^p-1`; diese beiden Nenner-/Vorzeichenkonventionen sind
nicht still auszutauschen.

### Spezialfall b=0, die scalarisierte (79a)

```text
H(r) = 2^p*exp((lambda-a)*r)*(1+t^2)^(-p),
E_rel = -p*t^2 + p*(p+1)/2*t^4 + O(t^6).
```

Die erste Fehlerordnung ist hier exp(-2lambda*r), nicht
exp(-lambda*r). Fuer a=2lambda folgt als exakte Kontrollidentitaet
`H(r)=sech(lambda*r)`. Diese Gleichheit betrifft nur den genannten
Spezialfall, nicht allgemeines a.

### Gueltige explizite Fehlerschranke

Setze `z=-2b*t+t^2` und `S=2*abs(b)*t+t^2`. Dann ist `abs(z)<=S`.
Fuer S<1 liefert der Mittelwertsatz fuer f(z)=(1+z)^(-p)

```text
abs(E_rel) <= p*S/(1-S)^(p+1).
```

Denn entlang der Strecke zwischen 0 und z gilt
`abs(f'(v))=p*(1+v)^(-p-1)<=p*(1-S)^(-p-1)`.
Die Schranke verlangt S<1; bei S>=1 ist sie nicht anwendbar, obwohl H
selbst weiterhin definiert ist. Der analytische Beweis ist nicht schon
eine Intervallzertifizierung seiner gerundeten Decimal-Auswertung.

Die asymptotischen O-Aussagen gelten bei festen p und b. Eine uniforme
Genauigkeit beim gleichzeitigen Grenzuebergang b gegen +/-1 oder p gegen
unendlich wurde damit nicht bewiesen.

## 3. Die auf Druck178 uebergebene grosse-r-Zwischenform

Schreibe die uebergebene zweite Zwischenform getrennt als

```text
H_178(r) = exp(x)*[1/2*sqrt((1+b)/(1-b))*(exp(x)-b)^2]^(-p).
```

Sie besitzt dieselbe exponentielle Rate, aber die fuehrende Amplitude

```text
M_178 = [2*sqrt((1-b)/(1+b))]^p,
M_178/M_79 = (1-b^2)^(-p/2).
```

Der Amplitudenquotient ist fuer b ungleich null groesser als 1, bei b=0
gleich 1. Bei identischen Parametern und identischer festgehaltener
Normierung sind die beiden Funktionen daher im Allgemeinen nicht
asymptotisch aequivalent im Quotientensinn. Genauer gilt

```text
H_178/H = (1-b^2)^(-p/2)
          *[1+(1-b^2)*t^2/(1-b*t)^2]^p.
```

Fuer b=0 ist H_178 bereits genau die fuehrende Asymptote von H,
nicht die komplette Funktion H. Auch dann ist die konstante Amplitude
2^p im Allgemeinen nicht 1.

Dies ist ein bedingter Normierungs-/Amplitudenvergleich. Wenn eine Quelle
nur die exponentielle Rate meint oder eine freie Gesamtamplitude zulaesst,
ist die konstante Abweichung nicht automatisch ein physikalischer Fehler.
Aus dem Zeichen einer naeherungsweisen Beziehung darf daher weder eine
exakte Funktionsgleichheit noch ohne Kontext eine Widerlegung konstruiert
werden. In der hier festgelegten Normierung ist der Unterschied jedoch
mathematisch eindeutig und dokumentationspflichtig.

## 4. Ableitung und Extremalbedingung

Der vorgegebene reelle Selektor ist

```text
alpha_real = (1-b*t)/(1-2b*t+t^2)
           = w*(w-b)/(w^2-2b*w+1).
```

Er entspricht dem Realteil der inversen komplexen Zahl
`1-b*t+i*sqrt(1-b^2)*t`, nicht dem inversen Realteil dieser Zahl.
Nur die explizit angegebene rationale Funktion wird hier benutzt.

Die logarithmische Ableitung der skalaren Funktion ist exakt

```text
H'/H = lambda-a*alpha_real.
```

Da H>0 ist, verlangt eine stationaere Stelle `alpha_real=A=lambda/a`.
Dies ergibt

```text
(1-A)*w^2 + b*(2A-1)*w - A = 0,
```

aequivalent in t:

```text
A*t^2 + b*(1-2A)*t + A-1 = 0.
```

Eine positive Radialstelle verlangt zusaetzlich w>1 beziehungsweise
0<t<1. Reelle Loesungen einer Quadratik allein genuegen nicht. w=1
bezeichnet den Rand r=0. Dort gelten fuer jedes -1<b<1
`alpha_real=1/2` und `H'(0)/H(0)=lambda-a/2`.

### Die u/C-Umformung und der Nenner

Waehle fuer die gewoehnliche skalare Umformung

```text
sigma=sqrt(1-b^2)>0,
u=(w-b)/sigma,
C_u=b/sigma.
```

Dann gilt exakt

```text
alpha_real = u*(u+C_u)/(1+u^2),
(1-A)*u^2+C_u*u-A=0.
```

Der uebergebene Ausdruck mit Nenner `1-u^2` wuerde hingegen die andere
Quadratik `(1+A)*u^2+C_u*u-A=0` liefern und ist keine gewoehnliche
Umformung derselben rationalen Funktion. Sein Nenner wuerde zudem bei
u=1 verschwinden, waehrend die Ausgangsfunktion dort endlich bleibt.

In der mitgeteilten Quelle steht C=cot(K). Unsere Definition C_u stimmt
mit diesem C bei b=cos(K) und dem positiven sin-Zweig ueberein, insbesondere
bei `0<K<pi/2`. Ausserhalb dieses Winkelzweigs ist das Vorzeichen gesondert
zu verfolgen. C_u ist ausserdem nicht der Korrelationsfaktor C frueherer
Alpha-Audits. Diese Gegenrechnung beweist nur den Nenner und die Quadratik
unter der expliziten skalaren Substitution, keine allgemeine metronische
Operatoridentitaet oder konkrete Autorenkorrektur.

## 5. Abklingen und positive Extremstellen sind verschiedene Forderungen

Weil M_79 positiv und endlich ist, gilt auf der vereinbarten Domaene

```text
a>lambda: H(r)->0,
a=lambda: H(r)->M_79>0,
a<lambda: H(r)->infinity.
```

Somit ist a>lambda genau die Bedingung des Abklingens gegen null fuer
diese Funktion. Sie folgt nicht allgemein allein aus der Existenz
positiver Extremstellen. Wenn Abklingen eine weitere Randbedingung der
Quelle ist, ist diese gesonderte Begruendung fuer a>lambda gueltig.

### Exaktes Gegenbeispiel zur alleinigen Extremumsfolgerung

In einer beliebigen konsistenten Laengeneinheit setze

```text
lambda=1, a=10/11, b=3/5, p=5/11, A=11/10.
```

Die stationaere Quadratik reduziert sich auf

```text
5*w^2-36*w+55=0,
w=11/5 oder w=5,
r=ln(11/5) oder r=ln(5), beide positiv.
```

Beide sind echte Extrema, nicht nur tangentiale stationaere Stellen.
Mit
`d(alpha_real)/dw=(-b*w^2+2w-b)/(w^2-2b*w+1)^2`
folgt an den stationaeren Stellen exakt

```text
w=11/5: H''/H=-7/40  -> striktes Maximum,
w=5:    H''/H=7/110 -> striktes Minimum.
```

Trotzdem ist die asymptotische Rate lambda-a=1/11 positiv. Das Beispiel
liegt ausserhalb einer zusaetzlich verlangten abklingenden Modellklasse;
es widerlegt nur die Folgerung aus Extremumsexistenz allein.

Fuer b=0 laesst sich die Grenze noch enger angeben: Eine positive
Extremstelle existiert genau fuer `1/2<A<1`, also `lambda<a<2lambda`.
Dann ist `r=log(A/(1-A))/(2lambda)`. Bei a=2lambda liegt die stationaere
Stelle nur am Rand r=0; fuer a>2lambda faellt H ohne positives Extremum.
a>lambda ist daher auch keine allgemeine hinreichende Extremumsbedingung.

Der formale Wert w=b setzt alpha_real=0 und liefert `H'/H=lambda`, also
gerade keine stationaere Stelle. Fuer 0<b<1 hat er r=log(b)/lambda<0
und liegt ohnehin ausserhalb des untersuchten Radialbereichs. Fuer
b<=0 ist er kein positiver Exponentialwert.

## 6. Unabhaengige numerische Gegenrechnung

Vor Import des neuen Rechners wurden eigene Decimal-Auswertungen mit
80 und 120 Stellen durchgefuehrt. Fuer das Gegenbeispiel ergaben sich

| Stelle | r | H(r) |
|---|---:|---:|
| Maximum | 0.78845736036427016946 | 1.17154519838395894601 |
| Minimum | 1.60943791243410037460 | 1.15755791177065456864 |

Der Selektor nimmt an beiden Stellen exakt den rational nachgewiesenen
Wert 11/10 an. Die numerische logarithmische Ableitung ist entsprechend
null bis zur Arbeitsgenauigkeit. Die exakten Quadratikresiduen und
Selektorwerte wurden separat mit Fraction geprueft.

Zusaetzlich wurden bei lambda=1, a=10/11 die Faelle b=-0.6,0,0.6 und
x=5,10,20 ausgewertet: normalisierter relativer Rest, seine ersten zwei
asymptotischen Terme und logarithmische Steigung. Die groesste absolute
80/120-Differenz aller verglichenen numerischen Felder war kleiner als
`9e-80`. Amplituden und ihr Quotient wurden separat gegengerechnet.
Beispielsweise bei b=0.6:

```text
M_79 = 0.9035454309190943752561586096740110...,
M_178 = 1,
M_178/M_79 = 1.1067512111513764028697802423848092....
```

Diese Werte sind synthetische skalare Kontrollen ohne Messwertinput.
Sie bestaetigen keine physikalische Amplitudennormierung.

## 7. Implementierungsreview: Erstbefund und gemeldete Randfehler

Vollstaendig gelesen wurden der neue Rechner
`scripts/audit_exponential_context.py` und seine zunaechst zehn Tests
in `tests/test_exponential_context.py`. Die vorgesehenen normalen
Beispielwerte, der Mittelwertsatz-Beleg, die Faktorisierung, die Rate,
der Amplitudenquotient und das exakte Gegenbeispiel waren algebraisch
richtig implementiert. Der erste Lauf von `--check --verify-sources`
bestaetigte Snapshot und H004-Hash; zehn Tests bestanden.

Zusaetzliche unabhaengige Randtests fanden folgende reale Defekte,
obwohl die normalen Snapshotbeispiele davon nicht betroffen waren:

1. Bei 80 Stellen und einem direkt aus einem String konstruierten
   `b=0.999...` mit 100 Neunen, sowie beim negativen Pendant, rundete
   `1-b*b` zu null. Der Amplitudenquotient wurde Infinity, obwohl sein
   wahrer Wert endlich etwa `7.071067811865475e49` ist (lambda=1,a=2).
   Der Hauptagent ersetzte den Ausdruck durch `(1-b)*(1+b)`.
2. Beim positiven gleichen Endpunkt und r=0 rundete b*t zu 1. Der
   Selektor wurde 0 statt 1/2, die logarithmische Steigung 1 statt 0.
   Der Hauptagent faktorisierte den Zaehler als `(1-t)+(1-b)*t`.
3. Ein weiterer Test mit demselben positiven b und r=`1e-100` zeigte
   verbleibenden Genauigkeitsverlust: exp(-x) rundete bei 80 Stellen zu
   1, somit wurde auch 1-t null. Nach den ersten zwei Korrekturen lieferte
   die Funktion dann Selektor 1/2 und Steigung 0; bei 220 Stellen ergibt
   sich Selektor nahe 1 und Steigung nahe -1. Der kleine Verlust in
   1-t wird durch den kleinen Nenner stark verstaerkt. Gemeldet wurde
   eine stabile Berechnung von `1-exp(-x)` bzw. eine explizite Ablehnung
   unaufgeloester Faelle.

Die drei Faelle wurden vor jeder Hauptdateiaenderung dem Hauptagenten
mit konkretem Reproduktionsbeispiel gemeldet. Von dieser Review wurden
keine Codepatches vorgenommen. Beim vorstehenden Zwischenstand war die
abschliessende Kontrolle noch offen; ihr Ergebnis folgt im Nachtrag.

## 8. Abschluss: Korrekturen, Snapshot und Berichtsgegenlesung

Der Hauptagent hat den dritten Fehler durch eine eigene stabile
Berechnung von `1-exp(-x)` behoben. Der interne Helfer wertet fuer
0<=x<=0.1 die alternierende Reihe

```text
x-x^2/2!+x^3/3!-...
```

bis zur Decimal-Stagnation aus; oberhalb 0.1 wird die direkte Differenz
verwendet. Die kleine Differenz wird nun in Zaehler und Nenner des
Selektors eingesetzt. Die Reihe aendert keine Quellenparameter oder
mathematische Funktion, sondern beseitigt vermeidbaren Verlust relativer
Genauigkeit in der gewoehnlichen numerischen Auswertung. Auch ihre
Auswertung wird nicht als zertifizierte Intervallarithmetik ausgegeben.

Vollstaendig erneut gelesen wurden der geaenderte Rechner und seine
zwoelf Tests; ferner `NORM-EXPONENTIAL-CONTEXT-DIAGNOSTICS.md` und
`06_docs/EXPONENTIAL_CONTEXT_2026-09-06.md`. Der neue Normalisierungs-
und Berichtstext trennt die skalare Abbildung, die gewaehlte Amplitude,
die asymptotische Rate und die offene Operator-/F/G-Zuordnung angemessen.
Insbesondere wird die konstante Amplitudendifferenz nicht als weiterer
Fehler gezaehlt, wenn die Quelle nur eine proportionale Naeherung mit
freier Amplitude beansprucht. Der Extremumsbefund bleibt bedingt und
wird nicht als Widerlegung des Abklingens bei a>lambda ausgegeben.

### Unabhaengiger Snapshotabgleich

Alle 18 regulären Zeilen und drei asymptotischen Kontrollzeilen des
Snapshots wurden mit eigener 140-stelliger Decimal-Arithmetik nachgerechnet.
H wurde dabei direkt aus der urspruenglichen Klammer
`(1+b)/2*(1+(w-b)^2/(1-b^2))` gebildet, der Selektor unabhaengig in w
und die Druck178-Amplitude aus ihrem eigenen Vorfaktor.

Geprueft wurden je Zeile genau diese 13 Felder:

```text
x, p, H, leading_amplitude, leading_profile,
H_over_leading_minus_one, relative_error_absolute_bound,
bound_condition_s, real_selector, logarithmic_slope,
asymptotic_slope, decays_at_infinity,
p178_over_p79_leading_amplitude.
```

Das sind 273 numerische, boolesche beziehungsweise bei unzulaessiger
Schrankenbedingung nullwertige Feldvergleiche. Alle Entscheidungen und
Nullwerte stimmten; die groesste absolute Abweichung der numerischen
Felder war kleiner als `2.4e-79` (Prueftoleranz `1e-70`). Die drei
gerundeten Beispielreste im Bericht stimmen ebenfalls.

Das exakte Gegenbeispiel wurde gesondert mit Fraction kontrolliert:
Wurzeln 11/5 und 5, beide Quadratikresiduen null, logarithmische Steigungen
an w=1,3,6 gleich `6/11`, `-1/44`, `19/1639` sowie asymptotische Rate
`1/11`. Zusammen mit den zwei stationaeren Wurzeln und dem positiven
Nenner bestaetigen die Vorzeichen ein Maximum gefolgt von einem Minimum.

### Nachweis der behobenen Randfaelle

Zusaetzlich wurden die beiden direkt aus 100 Neunen gebildeten b-Werte
`+0.999...` und `-0.999...` bei lambda=1, a=2 und den vier Radien
`0`, `1e-100`, `1e-80`, `1e-50` getestet. Referenz war jeweils eine
direkte Auswertung der urspruenglichen Funktion und des urspruenglichen
Selektors bei 260 Stellen, nicht der neue Klein-x-Helfer.

Bei 80 Arbeitsstellen wurden H, Selektor, logarithmische Steigung und
Amplitudenquotient verglichen, insgesamt 32 Feldvergleiche. Alle Werte
waren endlich. Der groesste Fehler geteilt durch
`max(1,abs(Referenzwert))` war kleiner als `3.4e-78`, gegen die gewaehlte
Toleranz `1e-70`. Die Skalierung ist wichtig, weil einzelne Selektoren
in dieser steifen Randregion groesser als `1e49` werden.

Insbesondere werden jetzt am positiven Endpunkt bei r=0 Selektor 1/2
und Steigung 0 geliefert, bei r=`1e-100` Selektor nahe 1 und Steigung
nahe -1. Der zuvor unendliche Amplitudenquotient bleibt endlich. Die
drei konkret gemeldeten Ausloeschungsdefekte sind damit nachgeprueft
behoben. Es waren Defekte unseres Rechners, keine Befunde gegen Heim.

Die dauerhaften Tests enthalten beide langen b-Eingaben, die r=0-
Identitaeten, den kleinen positiven Radius gegen eine direkte
220-stellige Referenz und den Klein-x-Helfer beiderseits der Schwelle
0.1. Domaenenfehler, Praezision 39/201 versus 40/200 und der b=0-
Spezialfall bleiben erfasst.

### Ausgefuehrte Abschlusspruefungen

```text
python -B scripts/audit_exponential_context.py --check --verify-sources
  Snapshot stimmt; H004-Quellhash bestaetigt.
python -B -m unittest discover -s tests -p test_exponential_context.py -v
  12 Tests bestanden.
python -B -m unittest discover -s tests -q
  98 Tests bestanden.
```

Der vorhandene Snapshot blieb durch die Randkorrekturen unveraendert.
Die alten sieben Rechner wurden durch diese Review weder veraendert
noch als Gegenstand einer neuen Gesamtvalidierung behandelt. Der
Hauptagent wurde auf noch alte Test-/Defektzaehler in seiner laufenden
Berichtsredaktion hingewiesen; inhaltlich wurde kein weiterer
Reichweitendefekt gefunden.

Abschluss: Kein offener beobachteter Code- oder Algebrafehler in den
geprueften Faellen. Dies ist keine Garantie beliebiger extremer Parameter,
keine Intervallzertifizierung und kein metronischer Operatorbeweis.
Nur diese eigene Reviewdatei wurde geschrieben und ergaenzt; keine
Hauptdateipatches, neuen Messdaten, externen Widerlegungsrecherchen oder
Commits durch diesen Reviewauftrag.
