# Buch-Auswahl: unabhaengige Rest- und Bestimmtheitspruefung

2026-09-06, Etappe 29. Gewoehnliche skalare Algebra; keine Massenrechnung,
kein Y9-Fit und keine Aussage ueber eine vollstaendige metronische Loesung.
Gelesen: `06_docs/K4_W4_SELECTION_2026-09-06.md`,
`06_docs/F16_DETERMINACY_2026-09-06.md` und `00_admin/BOOK_SELECTION_PLAN.md`.
Die H004-Lesung Druck340-342/PDF346-348 stammt aus den visuellen Pruefungen
von Root/book_derivation; diese Review hat keine eigene Glyphenpruefung.
Die Buchvorschrift wird nicht still mit den H006/H015-Lesprofilen identifiziert.

## 1. Festgehaltenes Paket und Buchregel

Die vorausgehenden N1/N2-Wahlen, W3 und a=alpha3>0 bleiben fest.
Mit ganzzahligem m=N3=floor(W3/a), W3>=0 und
lambda=(2k-1)/(3Q4)>0 gilt r=W4=W3-a*m in [0,a).
Untersucht wird die zusaetzliche Lesart als exakter Loeser von
`a*N3+exp(-lambda*N4)=W3`, mit N3 ganzzahlig und N4>=0.
Die gedruckte Auswahl selbst ist von dieser Erhaltungsbehauptung zu trennen.

Fuer r>0 ist x=W5=-ln(r)/lambda. Laut uebernommener Buchlesung:

- r=0 oder x>a*m: Kappe N4=TRC(a*m); nur wenn dieser Wert a*m
  ueberschreitet, wird in diesem Maximalzweig 1 abgezogen.
- Sonst N4=TRC(x); bei negativem x beschreibt die Quelle fuer k=2
  einen Transfer aus besetztem j=3 nach j=4, mit anschliessender Rohwertkappe.
- Erster Transfer: z=x+a*m und N3_neu=m-1; verlangt werden
  0<=z<=a*(m-1) sowie N3_neu>=0. Anschliessend N4=TRC(z).

Die gedruckte Fortsetzung enthaelt eine Summe mit Index mu, aber keine
vollstaendigen Summengrenzen. Die Rekonstruktion nach h Schritten als
`S_h=sum(j=1..h,m+1-j)=h*(2*m+1-h)/2`, `z_h=x+a*S_h`, `N3=m-h`
ist daher eine explizite eigene Implementierungskonvention, keine bereinigte
Transkription. Die Quelle nennt keine erneute Logarithmierung eines neuen r.

TRC bedeutet Abschneiden, mit einer quellenbenannten Neuner-Ausnahme bis
unterhalb der Messgrenze. Eine numerisch nutzbare Schwelle ist nicht angegeben.
Eine echte Identitaet 0.999...=1 und das Heraufsetzen einer endlichen Zahl
sind mathematisch verschieden. Die folgenden Floor-Grenzen gelten nur fuer
gewoehnliches Abschneiden bzw. einen gesondert bewiesenen Integerwert.
Es wird weder eine Epsilon-Regel noch ein allgemeines ceil-minus-eins eingefuehrt.

## 2. Welche Schritte die feste Restgleichung erhalten

Fuer beliebiges ausgewaehltes j bei unveraendertem m lautet der Fehler
`E=exp(-lambda*j)-r=r*(exp(lambda*(x-j))-1)` (r>0).
Fuer j=floor(x)>=0, theta=x-j in [0,1), folgt

```text
0 <= E < exp(-lambda*j)*(1-exp(-lambda)) <= 1-exp(-lambda),
0 <= E/r < exp(lambda)-1; E=0 genau dann, wenn x ganzzahlig ist.
```

Die erste obere Schranke ist strikt, auch bei theta=0. Diese Vorzeichen-
und Fehleraussagen gelten nicht pauschal fuer eine echte Promotion j>x:
dann ist E<0. Ohne definierte Messschwelle folgt keine numerische Fehlergarantie.

Bei r=0 bleibt fuer jeden endlichen, akzeptierten N4 der Fehler exp(-lambda*N4)>0.
Bei 0<r und x>a*m liefert jeder gekappte j<=a*m<x einen strikt positiven
Fehler. Endliche Saettigung kann die Strukturkappe erfuellen, aber nicht
gleichzeitig diese unveraenderte Restgleichung loesen. Das beweist fuer r=0
nicht die Unmoeglichkeit aller anderen N3; bewiesen ist der Fehler am gewaehlten m.

Die Kappe des Rohwerts ist nicht durch die Kappe seines Floorwerts ersetzbar.
Ebenso folgt bei endlicher Neuner-Promotion aus x<=a*m allein nicht
TRC(x)<=a*m. Am Rand x=a*m waere eine echte Promotion bereits ein Beispiel;
die nur fuer x>a*m bzw. r=0 beschriebene beta4-Korrektur greift dort nicht.
Dies ist eine bedingte Implementierungsluecke, kein belegter numerischer
Teilchenfall und keine Behauptung, dass die Quelle eine bestimmte Schwelle nutze.

## 3. Transfer: Akzeptanz ist keine Erhaltung

Fuer r>1 erzwingt Greedy a>1. Bei jedem ganzzahligen N3<=m waere der
benoetigte Exponentialterm W3-a*N3>=r>1; bei N3>=m+1 waere er negativ.
Daher existiert bei festem W3,a ueberhaupt kein ganzzahliges N3>=0 mit
reellem N4>=0, das diese Gleichung erfuellt. Das schliesst keine geaenderte
Projektionsregel oder Aenderung vorausgehender N1/N2 aus.

Nach h>=1 Reduktionen und einem akzeptierten N4=j>=0 gilt unmittelbar

```text
E = a*(m-h)+exp(-lambda*j)-W3
  = exp(-lambda*j)-r-a*h <= 1-r-a*h < 0.
```

Diese Aussage benoetigt weder Summengrenzen noch eine TRC-Schwelle.
Bei der oben deklarierten Summenkonvention waere vor TRC sogar
`E_raw=r*(exp(-lambda*a*S_h)-1)-a*h<-a*h`, da S_h>0 fuer 1<=h<=m.
Eine Erhaltung durch blosses Reduzieren von N3 wuerde stattdessen
`exp(-lambda*N4_neu)=r+a*h>1` fordern und damit erneut N4_neu<0.

Fuer den eindeutig gelesenen ersten Schritt ist die Rohwertakzeptanz exakt
`-a*m<=x<=-a` bei m>=1; Nichtnegativitaet allein reicht nicht.
Unter der eigenen Mehrschrittkonvention lautet sie
`-a*S_h<=x<=a*(m-h-S_h)`. z_h steigt, die Kappe a*(m-h) sinkt:
Eine bereits ueberschrittene Rohwertkappe wird durch weitere solche Schritte
nicht wieder erfuellt. Bei h=m verlangt die Kappe z_h=0 exakt.

Eigene synthetische Zeugen mit k=2,Q4=15,lambda=1/15,a=2,m=4:
r=3/2 ergibt 1<z_1=8-15*ln(3/2)<2, N3_neu=3,N4=1 und Kappe 6.
Der feste Gleichungsfehler ist exp(-1/15)-7/2<0.
Bei r=21/20 liegt z_1 zwischen 7 und 8 und verletzt dieselbe Kappe.
Bei r=3/2,a=2,m=7 sind unter der eigenen Summenkonvention 1<z_2<2,
waehrend z_1<0; dieser Fall belegt nur die deklarierte Zweischrittformel
mit lambda=1/60, nicht eine ausformulierte Quellenvorschrift.

## 4. Was Ganzzahlauswahl fuer A16 leisten kann

Nach der Grenzwertapproximation und bei fixen g,d>0 ist im aktiven Kanal
W(A)=g*(1+d*A). Fuer den folgenden Greedy-Anschluss wird f=0 vorausgesetzt;
bei anderem festem f>-1 waere g durch g*(1+f) zu ersetzen. Dies ist keine
Gleichung fuer die ganze urspruengliche F16-Funktion.
Bleiben die ersten drei Greedywerte fest und ist deren Summe S123, so gilt
r(A)=g*(1+d*A)-S123. Im gewoehnlichen ungesaettigten Floorzweig N4=j:

```text
exp(-lambda*(j+1)) < r(A) <= exp(-lambda*j).
A = ((S123+r)/g-1)/d.
```

Eine nichtleere Schnittmenge dieses Intervalls mit strikten Greedy-/Kappen-
bedingungen kann viele A-Werte haben. Die eindeutige Vorwaertsausgabe fuer
gegebenes A impliziert daher keine eindeutige Rueckbestimmung von A.
Der Code zeigt zwei solche reduzierte Eingaben mit identischem Integerausgang;
die freien positiven Koeffizienten sind keine gemeinsame Heim-Parameterfamilie.
Keine vollstaendige Quellen-Strukturpruefung, Uebergangs- oder Zustandsvalidierung
wird fuer diesen Zeugen behauptet. Weitere Bedingungen koennen Werte einschraenken.

Umgekehrt kann ein unabhaengig festes vollstaendiges Tupel zusammen mit
einer verlangten exakten Gleichheit A bestimmen: Fuer den dimensionslosen
linken Ausdruck T108, nicht die Lebensdauer T, folgt bedingt
`A=[T108/(g*(1+f))-1]/d`, sofern f!=-1. Ganzzahligkeit, Approximation und
exakte Gleichheit sind unterschiedliche Anforderungen. Die durch W(A)
erst erzeugten N_(j) machen T108 nicht schon zu einer unabhaengigen Eingabe.
Eine vorab festgelegte heuristische A16-Formel bleibt numerisch berechenbar;
diese Review behauptet weder einen global freien Parameter noch dessen Herleitung.

## 5. Eigene ausfuehrbare Zertifikate

Nur Python-Standardbibliothek, keine Rechner-/Quellenprogrammimporte.
Logarithmen werden durch die rationale atanh-Reihe mit gerichteter Restschranke,
negative Exponentialwerte durch Kehrwerte rationaler Taylorintervalle begrenzt.
Die Assertions, nicht die optionalen Dezimaldarstellungen, entscheiden die Faelle.

```python
from fractions import Fraction as F
from decimal import Decimal, localcontext

checks = 0
def check(condition, label):
    global checks
    assert condition, label
    checks += 1

def log_bounds(v, terms=48):
    v = F(v)
    assert v > 0
    t = (v-1)/(v+1)
    value = 2*sum((t**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    tail = 2*abs(t)**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    return (value, value+tail) if t >= 0 else (value-tail, value)

def exp_negative_bounds(v, terms=48):
    v = F(v)
    assert 0 <= v < terms+2
    term = total = F(1)
    for j in range(1, terms+1):
        term *= v/j
        total += term
    upper = total + term*v/F(terms+1)/(1-v/F(terms+2))
    return 1/upper, 1/total

def raw_bounds(r, lam):
    assert lam > 0
    lo, hi = log_bounds(r)
    return -hi/lam, -lo/lam

def exhaust(w, coefficient, power):
    assert w >= 0 and coefficient > 0 and power >= 1
    n = 0
    while coefficient*(n+1)**power <= w:
        n += 1
    return n, w-coefficient*n**power

# Normal floor; no finite-nine promotion is used.
lo, hi = raw_bounds(F(3, 4), F(1, 3))
check(0 < lo <= hi < 1, 'normal raw lies strictly in (0,1)')
check(1-F(3, 4) == F(1, 4), 'exact floor residual')
e_lo, e_hi = exp_negative_bounds(F(1, 3))
check(e_hi < F(3, 4), 'strict absolute residual bound')
check(F(1, 3) < 1/e_hi-1, 'strict relative residual bound')

# Positive-r cap and zero-r cap, at fixed selected m.
lo, hi = raw_bounds(F(1, 2), F(1, 3))
check(lo > 2, 'raw exceeds a*m=2')
cap_lo, cap_hi = exp_negative_bounds(F(2, 3))
check(cap_lo > F(1, 2), 'positive-r capped residual strictly positive')
check(cap_lo > 0, 'zero-r finite capped residual strictly positive')

# Book first transfer; all inputs below are synthetic.
a, m, lam, r = F(2), 4, F(1, 15), F(3, 2)
check(exhaust(a*m+r, a, 1) == (m, r), 'greedy transfer remainder')
x_lo, x_hi = raw_bounds(r, lam)
z_lo, z_hi = x_lo+a*m, x_hi+a*m
check(1 < z_lo <= z_hi < 2, 'first transfer floor is 1')
check(0 <= z_lo and z_hi <= a*(m-1), 'raw cap holds')
check(-a*m < x_lo and x_hi < -a, 'equivalent first-step gate')
e_lo, e_hi = exp_negative_bounds(lam)
check(e_hi-r-a < 0, 'accepted transfer residual is negative')
check(e_hi-r-a <= 1-r-a, 'universal nonnegative-N4 bound')
bad_lo, bad_hi = raw_bounds(F(21, 20), lam)
check(7 < bad_lo+a*m <= bad_hi+a*m < 8, 'raw cap failure witness')
check(bad_lo+a*m > a*(m-1), 'nonnegative does not imply capped')

# Optional explicit convention for repeated transfer, not printed bounds.
m, lam = 7, F(1, 60)
x_lo, x_hi = raw_bounds(F(3, 2), lam)
check(x_hi+a*m < 0, 'first step still negative')
for h in range(1, m+1):
    s = sum((F(m+1-j) for j in range(1, h+1)), F(0))
    check(s == F(h*(2*m+1-h), 2), 'triangular convention identity')
z_lo, z_hi = x_lo+26, x_hi+26
check(1 < z_lo <= z_hi < 2, 'second step raw lies in (1,2)')
check(z_hi < a*(m-2), 'second step raw cap holds')

# Two accepted reduced forward inputs, not a full Heim state.
outputs = []
for r in (F(3, 4), F(4, 5)):
    w = F(33)+r
    n1, w2 = exhaust(w, F(1), 3)
    n2, w3 = exhaust(w2, F(1), 2)
    n3, remainder = exhaust(w3, F(1), 1)
    lo, hi = raw_bounds(remainder, F(1, 3))
    check((n1, n2, n3) == (3, 2, 2), 'same first-three greedy output')
    check(remainder == r, 'same declared affine remainder')
    check(0 < lo <= hi < 1 < n3, 'floor zero and raw cap interior')
    outputs.append((n1, n2, n3, 0))
check(outputs[0] == outputs[1], 'integer output not injective on W')
check(F(33)+F(3, 4) != F(33)+F(4, 5), 'distinct W inputs')
for g, d in ((F(1), F(1)), (F(2), F(1, 2))):
    aa = [((F(33)+r)/g-1)/d for r in (F(3, 4), F(4, 5))]
    check(aa[0] != aa[1], 'distinct A under fixed positive affine map')
    check(all(g*(1+d*v) > 0 for v in aa), 'forward domains')
print('Exact rational certificate checks:', checks)
with localcontext() as ctx:
    ctx.prec = 35
    print('First-transfer z interval:',
          *(Decimal(v.numerator)/Decimal(v.denominator)
            for v in (raw_bounds(F(3, 2), F(1, 15))[0]+8,
                      raw_bounds(F(3, 2), F(1, 15))[1]+8)))
```

Die Zertifikate sichern nur die erklaerten skalaren Eigenschaften. Insbesondere
sind keine realen Teilcheninputs, unbekannten Messschwellen, kompletten
Buch-Strukturgates oder deren physikalische Begruendung damit bewiesen.

Ausgefuehrt: der unveraenderte Python-Block dieser Review via `py -3.13 -B -`
bestand mit 37 rationalen Pruefungen und Exitcode 0. Das zertifizierte Intervall
fuer den ersten Transfer ergibt gerundet z=1.9180233783775342703298032680347630;
die Integerentscheidung stammt aus den rationalen Grenzen, nicht dieser Anzeige.

## 6. Begrenzte Gegenreview der Root-Tests

`tests/test_book_selection.py` wurde vollstaendig gelesen und mit
`py -3.13 -B -m unittest discover -s tests -p test_book_selection.py -v`
ausgefuehrt: alle 13 Tests bestanden, Exitcode 0. Keine materiellen Algebrafehler
in den getesteten Faellen gefunden. Die rationalen Log-/Exp-Hilfsfunktionen
werden aus den Etappe25-Tests importiert; das ist kein historischer Programmlauf
und keine weitere unabhaengige Zertifikatsimplementierung. Der obige eigene
Block ist dagegen selbstenthalten und importiert diese Helfer nicht.

Die Testzeugen W=151/4 bzw. 189/5 verwenden andere synthetische Koeffizienten
(1,2,1) als der eigene reduzierte Zeuge; beide Root-Faelle liefern (3,2,2,0).
Die Tests behaupten nur die explizit gepruefte beta4-Bedingung, keine komplette
107/107a-Zulaessigkeit. Am ganzzahligen Saettigungsrand mit beta4=0 wird kein
physikalisch erreichbarer Teilchenzustand behauptet; die Kollapsausnahme bleibt
getrennt. Mehrschrittsumme und Floor sind deklarierte Rechenlesarten.
Kleiner Helper-Rand: `transfer_addition` prueft Schranken, nicht ausdruecklich
die Ganzzahligkeit von Transferzahl und N3; alle verwendeten Faelle sind
ganzzahlig. Dies ist keine Produktions-API oder vollstaendige TRC-Implementierung.

Neu gegenueber Etappe25 sind die direkt gelesene Buch-Rohwertkappe, der
explizite erste Transferschritt und die nun abgegrenzten offenen
Implementierungsdetails der Fortsetzung. Die Restgleichungsargumente sind verwandt, keine zusaetzliche
unabhaengige Fehlerzaehlung. Gegenueber Etappe28 ist der Vorwaerts-/Rueckschluss
nun an einer deklarierten diskreten Auswahl demonstriert, nicht global bewiesen.
