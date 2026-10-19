# Positive Rekurrenz, Quotientengrenzwert und Auswahlpraemisse

2026-09-06, Etappe34. Eigene bedingte skalare Mathematik; keine eigene
Quellen-/PDF-Lesung und kein Urteil ueber metronische Operatoren. Die unten
geprueften Praemissen stammen aus dem Arbeitsauftrag; der spaetere Hinweis
auf den Kontext H004 Druck248-251 wurde durch Root mitgeteilt. Keine
Buchprofile, Tests, Normalisierungen oder anderen Dateien werden geaendert.
Keine Abklingkonstante wird in einen Teilchenrechner eingesetzt.

## 1. Exakter Verlauf bei beliebigen strikt positiven Anfangswerten

Seien x0=u>0, x1=v>0 und x_(n+2)=x_(n+1)+x_n fuer n>=0.
Mit phi=(1+sqrt(5))/2, psi=(1-sqrt(5))/2 gilt

```text
phi^2=phi+1, psi^2=psi+1, phi*psi=-1,
A=(v-psi*u)/sqrt(5)>0, B=(phi*u-v)/sqrt(5),
x_n=A*phi^n+B*psi^n.
```

Die Anfangswerte und die Rekurrenz bestaetigen diese eindeutige Loesung.
Positivitaet aller x_n folgt auch unmittelbar induktiv. Fuer den Quotienten
q_n=x_(n+1)/x_n setze c=B/A und t=psi/phi=-phi^(-2). Dann exakt

```text
x_n=A*phi^n*(1+c*t^n),
q_n-phi = -sqrt(5)*c*t^n/(1+c*t^n).
```

Der Nenner ist fuer alle n>=0 strikt positiv. Mit s=v/u>0 folgt
`c=(phi-s)/(s-psi)` und `-1<c<phi^2`. Insbesondere ist der wachsende Anteil
A nicht null; wegen |t|<1 gilt q_n->phi. Der Grenzwert haengt nicht von u/v
ab, der endliche Fehler aber schon. Eine gemeinsame Skalierung von u,v
aendert die Quotienten und c nicht.

- Fuer v=phi*u ist c=0 und jeder Quotient exakt phi.
- Sonst wechselt das Vorzeichen von q_n-phi in jedem Schritt; exakt
  `sign(q_n-phi)=-sign(c)*(-1)^n`.
- Fuer c!=0 ist der fuehrende Fehler `-sqrt(5)*c*(-phi^(-2))^n`;
  das Verhaeltnis aufeinanderfolgender absoluter Fehler tendiert zu phi^(-2).

Ein Quotientengrenzwert ist weder die Behauptung x_n->Konstante noch eine
verschwindende relative Schrittweite: Beispielsweise tendiert
`(x_(n+1)-x_n)/x_(n+1)` zu `1-1/phi>0`.

## 2. Uniforme endliche Einhuellung trotz unbekannter positiver Starts

Sei F0=0,F1=1,F_(n+1)=F_n+F_(n-1) die gewoehnliche Fibonacci-Folge.
Fuer n>=2 gilt

```text
q_n = (F_(n+1)*v+F_n*u)/(F_n*v+F_(n-1)*u).
```

Dies ist ein strikt positiver gewichteter Mittelwert der beiden Zahlen
`F_(n+1)/F_n` und `F_n/F_(n-1)`, mit Gewichten F_n*v und F_(n-1)*u.
Er liegt daher strikt zwischen ihnen. Die Cassini-Identitaet
`F_(n+1)*F_(n-1)-F_n^2=(-1)^n` liefert die exakte Intervallbreite
`1/(F_n*F_(n-1))`. Auch phi liegt strikt zwischen diesen Endpunkten:
`phi*F_n-F_(n+1)=-psi^n` wechselt sein Vorzeichen.

Somit gilt fuer ALLE strikt positiven Startpaare und n>=2 die uniforme
Schranke `abs(q_n-phi)<1/(F_n*F_(n-1))`, die gegen null geht. Diese
anfangswertunabhaengige Einhuellung ist nicht mit der individuellen exakten
Fehleramplitude c zu verwechseln. Bei n=0 und n=1 sind die Quotienten
ueber alle positiven Startpaare noch unbeschraenkt (v/u bzw.1+u/v).
Der Index n dieser Rechnung wird keiner physikalischen Besetzung zugeordnet.

## 3. Goldene Identitaet und Teilerwahl sind verschiedene Aussagen

Aus phi folgt genau `(2*phi-1)^2=5`. Die davon zunaechst getrennten
Bedingungen `z ganzzahlig, z teilt15, 1<z<15` ergeben aber `z in {3,5}`.
Die gleichzeitige Belegung phi=(1+sqrt(5))/2 und z=3 erfuellt SAEMTLICHE
dieser Praemissen einschliesslich der goldenen Identitaet. Sie ist daher
ein elementarer logischer Gegenzeuge zur behaupteten Folgerung z=5.

Erst eine weitere Gleichsetzung `z=(2*phi-1)^2` schliesst z=3 aus. Ob ein
Autor eine solche Zusatzregel oder andere Auswahlbedingungen begruendet,
ist eine getrennte Quellenfrage. Weder die Rekurrenz noch ihre Konvergenz
allein setzt z in Beziehung zu dieser Identitaet. Es wird kein A-Profil
variiert und kein Kandidat durch einen Massen- oder Restvergleich ausgewaehlt.

## 4. Exponentialasymptotik allein erzwingt die Rekurrenz nicht

Fuer die hier EIGENS erklaerte gewoehnliche Rueckwaertsdifferenz
`Delta=I-S`, `S*x_n=x_(n-1)`, ist fuer n>=2 exakt

```text
(Delta^2-3*Delta+I)x_n = -x_n+x_(n-1)+x_(n-2).
```

Die positive eigene Folge x_n=2^n hat mit beliebigem ell>0 und
alpha=ln(2)/ell exakt `x_n=exp(alpha*r_n)`, `r_n=n*ell` und
`Delta r_n=ell>0`. Trotzdem ist der Selektorausdruck `-2^(n-2)`, nicht0.
Damit erzwingen Exponentialasymptotik und ein positiver konstanter
Raumschritt ALLEIN die Fibonacci-Rekurrenz nicht. Dieser reduzierte Zeuge
ist keine metronische Gegenloesung, kein Modell eines Teilchens und keine
Behauptung, alle sonstigen Quellenannahmen zu erfuellen.

Wenn dagegen die Rekurrenz UND eine multiplikative Asymptotik
`x_n/(C*exp(alpha*r_n))->1` mit C>0, konstantem alpha>0 und
`r_(n+1)-r_n->beta>0` gelten, folgt bedingt `exp(alpha*beta)=phi`, also
`alpha*beta=ln(phi)`. Hierzu muss die Bedeutung der Asymptotik die
benannte Quotientenfolgerung erlauben; blosse grobe Wachstumsordnung oder
ein logarithmischer Mittelwert reichen ohne Zusatzkontrolle nicht.
Diese Folgerung liefert weder einen Wert fuer alpha oder beta einzeln noch
`A_sigma=1/3` oder eine Identifikation von n,r_n mit N4.

## 5. Selbstenthaltener exakter Kontrollblock

Das Paar (a,b) steht exakt fuer a+b*sqrt(5), mit rationalen Komponenten.
Vorzeichen werden durch rationale Quadrate entschieden, nicht mit float.
Die endlichen Tests ergaenzen die obigen allgemeinen Beweise.

```python
from fractions import Fraction as F

def Q(a=0, b=0):
    return F(a), F(b)
def add(x, y):
    return Q(x[0]+y[0], x[1]+y[1])
def neg(x):
    return Q(-x[0], -x[1])
def sub(x, y):
    return add(x, neg(y))
def mul(x, y):
    a, b = x; c, d = y
    return Q(a*c+5*b*d, a*d+b*c)
def div(x, y):
    a, b = y
    norm = a*a-5*b*b
    assert norm != 0
    return mul(x, Q(a/norm, -b/norm))
def power(x, n):
    assert type(n) is int and n >= 0
    result = Q(1)
    for _ in range(n):
        result = mul(result, x)
    return result
def sign(x):
    a, b = x
    sg = lambda r: (r > 0)-(r < 0)
    if b == 0:
        return sg(a)
    if a == 0 or a*b > 0:
        return sg(b)
    return sg(a*a-5*b*b) if a > 0 else sg(5*b*b-a*a)

checks = 0
def check(condition):
    global checks
    assert condition
    checks += 1

one, phi, psi, root5 = Q(1), Q(F(1, 2), F(1, 2)), Q(F(1, 2), -F(1, 2)), Q(0, 1)
for root in (phi, psi):
    check(power(root, 2) == add(root, one))
check(mul(phi, psi) == Q(-1))
t = div(psi, phi)
check(t == neg(div(one, power(phi, 2))))

fib = [0, 1]
for _ in range(15):
    fib.append(fib[-1]+fib[-2])
for u, v in ((F(1), F(1)), (F(1), F(2)), (F(2), F(1)), (F(1, 10), F(13))):
    A = div(sub(Q(v), mul(psi, Q(u))), root5)
    B = div(sub(mul(phi, Q(u)), Q(v)), root5)
    c = div(B, A)
    check(sign(A) > 0)
    check(sign(add(c, one)) > 0 and sign(sub(power(phi, 2), c)) > 0)
    sequence = [u, v]
    for _ in range(13):
        sequence.append(sequence[-1]+sequence[-2])
    for n in range(13):
        check(add(mul(A, power(phi, n)), mul(B, power(psi, n))) == Q(sequence[n]))
        denominator = add(one, mul(c, power(t, n)))
        check(sign(denominator) > 0)
        error = sub(Q(sequence[n+1]/sequence[n]), phi)
        exact_error = div(neg(mul(root5, mul(c, power(t, n)))), denominator)
        check(error == exact_error)
        check(sign(error) == -sign(c)*(-1)**n)
        if n >= 2:
            ends = (F(fib[n+1], fib[n]), F(fib[n], fib[n-1]))
            lo, hi = min(ends), max(ends)
            quotient = sequence[n+1]/sequence[n]
            check(lo < quotient < hi)
            check(sign(sub(phi, Q(lo))) > 0 and sign(sub(Q(hi), phi)) > 0)
            check(hi-lo == F(1, fib[n]*fib[n-1]))
            check(fib[n+1]*fib[n-1]-fib[n]**2 == (-1)**n)
            check(sub(mul(phi, Q(fib[n])), Q(fib[n+1])) == neg(power(psi, n)))

# Special irrational initial ratio: pure growing mode, no quotient error.
sequence = [one, phi]
for _ in range(8):
    sequence.append(add(sequence[-1], sequence[-2]))
for n in range(9):
    check(div(sequence[n+1], sequence[n]) == phi)

identity = power(sub(mul(Q(2), phi), one), 2)
check(identity == Q(5))
candidates = [z for z in range(2, 15) if 15 % z == 0]
check(candidates == [3, 5])
for z in candidates:
    check(identity == Q(5) and 1 < z < 15 and 15 % z == 0)
check([z for z in candidates if Q(z) == identity] == [5])

# Ordinary backward difference, not a metronic operator evaluation.
for n in range(2, 15):
    x, prev, prev2 = F(2**n), F(2**(n-1)), F(2**(n-2))
    delta = x-prev
    delta2 = x-2*prev+prev2
    selector = delta2-3*delta+x
    check(selector == -x+prev+prev2 == -F(2**(n-2)))
    check(selector != 0)
print(checks, 'exact recurrence/algebra controls; no source solution or mass claim.')
```

Der unveraenderte obige Block wurde eigenstaendig via `py -3.13 -B -`
ausgefuehrt: 480 exakte Kontrollen bestanden, Exitcode0. Er importiert nur
die Standardbibliotheks-Fraction-Klasse, keine Projekt- oder Quellenprogramme.
Geprueft wurden charakteristische Identitaeten, Binet- und Fehlerform fuer
vier positive rationale Startpaare, endliche uniforme Quotientenhuellen,
der exakt goldene Startquotient, die beiden Teilerbelegungen und der
Exponentialgegenzeuge. Die allgemeinen Aussagen fuer alle positiven reellen
Starts beruhen auf den oben gegebenen algebraischen Beweisen, nicht auf
einer Hochrechnung aus diesen endlich vielen Tests.

Nur diese eigene neue Review wurde geschrieben. Keine Quellenformel wurde
korrigiert, keine neue Besetzung berechnet und kein physikalischer
Ursprungs- oder Auswahlbeweis aus den Zahlenidentitaeten abgeleitet.

## 6. Begrenzte Codegegenreview und achtstellige Rundungszelle

`scripts/audit_xi_recurrence.py` und `tests/test_xi_recurrence.py` vollstaendig
gelesen. Keine materiellen Rechen- oder Aussagefehler gefunden. Die
Quotientenindexierung, Rekurrenz, Cassini-Breiten, verschachtelten Huellen
und die Selektorgegenprobe stimmen mit der eigenen Herleitung ueberein.
Der Rechner akzeptiert nur exakte int/Fraction-Werte; die Tests behandeln
rationale Beispielstarts, waehrend der Beweis in Abschnitt2 alle positiven
reellen Starts abdeckt. Die algebraischen Teiler- und Fuenferidentitaetstests
behaupten keine neue physikalische Auswahlregel.

Selbst ausgefuehrt, jeweils Exitcode0:

```text
py -3.13 -B scripts/audit_xi_recurrence.py --check
py -3.13 -B -m unittest discover -s tests -p test_xi_recurrence.py -v
  12 Tests bestanden.
```

Die neue konkrete Aussage wurde zusaetzlich mit einer separat aufgebauten
Fibonacci-Liste und Fraction-Arithmetik OHNE Root-Import geprueft:

```text
q22=x23/x22,
17711/10946 < q22 < 28657/17711.
Untere Rundungszellgrenze: 1.618033985;
obere Rundungszellgrenze:  1.618033995.
```

Die exakten Abstaende der aeusseren Huelle von den Zellgrenzen sind

| Vergleich | Exakter strikt positiver Abstand |
|---|---:|
| 17711/10946 minus untere Zellgrenze | 19/1094600000000 |
| Obere Zellgrenze minus 28657/17711 | 17089/3542200000000 |

Insbesondere die erste Differenz ist klein (etwa1.74e-11), aber exakt
positiv, nicht durch eine ungepruefte Dezimalapproximation entschieden.
Alle q22 fuer strikt positive Anfangswerte und auch phi runden daher auf
acht Nachkommastellen zu1.61803399. Gemeint ist Rundung zum naechsten Wert,
NICHT Abschneiden; die strikte Lage vermeidet jede Bindungsfallkonvention.

Die obere q21-Huellengrenze10946/6765 liegt hingegen um
`953/270600000000` oberhalb der oberen Rundungszellgrenze. Somit reicht
diese uniforme Huelle bei n21 noch nicht aus. Das Ergebnis betrifft
ausschliesslich unseren Folgenindex und eine mathematische Rundungszelle,
keine Identifikation einer physischen Besetzung oder Feldfehlertoleranz.
Auch fuer diesen Nachtrag wurden keine Root-Dateien geaendert.
