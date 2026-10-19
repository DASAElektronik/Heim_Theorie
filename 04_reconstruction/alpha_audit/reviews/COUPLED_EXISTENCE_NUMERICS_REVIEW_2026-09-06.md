# Gekoppelte Buchbedingungen: unabhaengige Zahlen- und Beweiskontrolle

2026-09-06, Etappe32. Eigene konditionale Mathematik, keine neue Quellenlesung.
Gelesen: unveraendertes `book_pseudosinglet_inputs.json`,
`scripts/audit_book_pseudosinglet.py` und die eigene Numerikreview aus Etappe30.
Die Quellenlesung und der vor Auswertung festgelegte Vertrag werden uebernommen;
keine PDF-Glyphenpruefung oder neue Aussage zur Autorenabsicht erfolgt hier.

## 1. Praemissen und staerkerer lokaler Ausschluss

Beide bisherigen Profile bleiben getrennt: kleiner positiver (105)-Zweig
bei Y3=1 beziehungsweise Druckalpha exakt 0.007297354572. In beiden gelten
mathematisches pi/e, xi=(1+sqrt(5))/2, Y9=1 und die festen N=0-Musterparameter
des Vertrags. Die folgenden N1..N4 sind die Besetzungen N_(j), nicht der
Resonanzindex N, nicht die verschobenen n_j und keine Quellenquantenzahlwahl.

Seien a1,a2,a3>0 die vertraglichen Buchkoeffizienten, W derselbe vorgegebene
Wert wie in Etappe30 und

```text
E(N1,N2,N3,N4) = a1*N1^3 + a2*N2^2 + a3*N3 + exp(-N4/3).
N1,N2,N3 nichtnegative ganze Zahlen; N4 beliebig reell >=0.
N1^3 > G2(N2),  G2(m)=m(m+1)(2m+1)/6;
N2^2 > G3(N3),  G3(m)=m(m+1)/2.
```

Das sind nur zwei notwendige Gates des nichtkollabierten, ungewichteten
(107)/(107a)-Pakets, nicht ein vollstaendiger Zustandsvertrag. Es gilt stets
0<exp(-N4/3)<=1. Die folgenden fuenf Faelle sind erschoepfend:

| Fall | Konsequenz und Energiebeschraenkung |
|---|---|
| N1>=15 | E>=3375*a1>W. |
| N1<=13 | G2(19)=2470>2197, daher N2<=18; G3(25)=325>324, daher N3<=24. E<=2197*a1+324*a2+24*a3+1<W. |
| N1=14, N2>=10 | E>=2744*a1+100*a2>W. |
| N1=14, N2<=8 | G3(11)=66>64, daher N3<=10. E<=2744*a1+64*a2+10*a3+1<W. |
| N1=14, N2=9 | G3(13)=91>81, daher N3<=12. E<=2744*a1+81*a2+12*a3+1<W. |

Monotonie von G2/G3 fuer nichtnegative Argumente und Positivitaet der
Koeffizienten rechtfertigen alle Schranken. Eine Greedy-Regel, TRC, der dritte
Strukturgate, die zweite Differenzreihe, obere L-Grenzen und die separate
gewichtete (107b)-Kappe werden fuer diesen Ausschluss nicht benoetigt.
Insbesondere umfasst er auch nicht-greedy gewaehlte N1..N3 und reelle N4>=0.
Er beweist NICHT einen Kollapsalgorithmus oder eine Unmoeglichkeit ausserhalb
dieser festgelegten Eingaben und dieses nichtkollabierten skalaren Pakets.

## 2. Methode und kleine gemeinsame Zahlenhuellen

Der folgende selbstenthaltene Block importiert weder Root-Rechner noch Tests
oder historische Programme. Er berechnet die Kette zweimal mit Decimal
(120/160 Ausgabestellen, jeweils 20 Schutzstellen): eigenes Machin-pi,
kleiner Alpha-Zweig durch Fixpunktiteration. Davon getrennt zertifiziert er
dieselbe Kette mit Fraction-Intervallen, alternierenden Machin-Reihen,
Taylorrestschranken fuer e/exp(-1/3), ganzzahligem isqrt und ausschliesslich
nach aussen gerichteter rationaler Rundung. Die Alpha-Intervallform folgt aus
alpha^2=2*R^2/(1+sqrt(1-4*R^2)); fuer 0<R<1/2 ist dies der kleine Zweig.
Die Praezisionsuebereinstimmung ist kein Beweis; die rationalen Einschluesse
und anschliessenden rationalen Ungleichungen liefern hier die Zertifikate.

Fuer BEIDE Profile werden insbesondere folgende gemeinsame geschlossene
Huellen geprueft (bewusst viel groeber als die interne Intervallrechnung):

| Groesse | Untere Grenze | Obere Grenze |
|---|---:|---:|
| a1 | 0.996881270553 | 0.996881270554 |
| a2 | 1.012592613788 | 1.012592613789 |
| a3 | 0.97865878985 | 0.97865878994 |
| W | 2830.263257664 | 2830.263257669 |

Alle Dezimalgrenzen in dieser Tabelle sind exakte rationale Zahlen, keine
physikalischen Unsicherheitsintervalle. Die gemeinsame Huelle vermischt die
Alpha-Definitionen nicht, sondern umfasst beide separat berechneten Profile.

```python
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from math import isqrt, factorial

SCALE = 10**60

class I:
    # Closed intervals with exact outward quantization to a rational grid.
    def __init__(self, lo, hi=None):
        lo, hi = F(lo), F(lo if hi is None else hi)
        assert lo <= hi
        self.lo = F((lo*SCALE).__floor__(), SCALE)
        self.hi = F((hi*SCALE).__ceil__(), SCALE)
    @staticmethod
    def cast(x):
        return x if isinstance(x, I) else I(x)
    def __add__(self, other):
        o = I.cast(other)
        return I(self.lo+o.lo, self.hi+o.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self, other):
        return self+-I.cast(other)
    def __rsub__(self, other):
        return I.cast(other)+-self
    def __mul__(self, other):
        o = I.cast(other)
        products = [x*y for x in (self.lo, self.hi) for y in (o.lo, o.hi)]
        return I(min(products), max(products))
    __rmul__ = __mul__
    def __truediv__(self, other):
        o = I.cast(other)
        assert not o.lo <= 0 <= o.hi
        return self*I(1/o.hi, 1/o.lo)
    def __rtruediv__(self, other):
        return I.cast(other)/self
    def __pow__(self, n):
        assert type(n) is int and n >= 0
        answer = I(1)
        for _ in range(n):
            answer = answer*self
        return answer
    def sqrt(self):
        assert self.lo >= 0
        def floor_root(x):
            return isqrt(x.numerator*SCALE*SCALE//x.denominator)
        lower, upper = floor_root(self.lo), floor_root(self.hi)
        if F(upper, SCALE)**2 != self.hi:
            upper += 1
        assert F(lower, SCALE)**2 <= self.lo <= self.hi <= F(upper, SCALE)**2
        return I(F(lower, SCALE), F(upper, SCALE))

def atan_interval(n, terms=100):
    partial = sum((F((-1)**j, (2*j+1)*n**(2*j+1))
                   for j in range(terms)), F(0))
    next_term = F((-1)**terms, (2*terms+1)*n**(2*terms+1))
    return I(min(partial, partial+next_term), max(partial, partial+next_term))

def exact_constants():
    pi = 16*atan_interval(5)-4*atan_interval(239)
    assert 3 < pi.lo < pi.hi < F(22, 7)
    # e: after n=89, all further positive-term ratios are <=1/91.
    partial = sum((F(1, factorial(n)) for n in range(90)), F(0))
    e = I(partial, partial+F(1, factorial(90))/(1-F(1, 91)))
    # exp(-1/3): alternating decreasing Taylor terms, through n=59.
    partial = sum((F((-1)**n, 3**n*factorial(n)) for n in range(60)), F(0))
    expneg = I(partial, partial+F(1, 3**60*factorial(60)))
    return pi, e, (1+I(5).sqrt())/2, expneg

def decimal_pi():
    def atan(n):
        x = D(1)/n
        term = total = x
        j = 1
        while True:
            term *= -x*x
            new = total+term/(2*j+1)
            if new == total:
                return new
            total, j = new, j+1
    return 16*atan(5)-4*atan(239)

def chain(pi, e, xi, expneg, printed):
    one = pi*0+1
    eta, d, t = (1/(one+(4+j)/pi**4).sqrt().sqrt() for j in (0, 1, 2))
    sd, st = d.sqrt(), t.sqrt()
    corr1, corr2 = sd*(1-sd)/(1+sd), st*(1-st)/(1+st)
    rhs = 9*(5*eta+2*eta.sqrt()+1)*(1-corr1*corr2)/(32*pi**5)
    if printed:
        alpha = I('0.007297354572') if isinstance(rhs, I) else D('0.007297354572')
    elif isinstance(rhs, I):
        assert 0 < rhs.lo <= rhs.hi < F(1, 2)
        alpha = (2*rhs**2/(1+(1-4*rhs**2).sqrt())).sqrt()
    else:
        alpha = rhs
        for _ in range(1000):
            nxt = rhs/(1-alpha**2).sqrt()
            if nxt == alpha:
                break
            alpha = nxt
        else:
            raise ArithmeticError('iteration did not stagnate')
    a1, a2 = (1+sd)/2, 1/d
    h = alpha*(1+sd)*xi**3/(3*d**3)
    gcor = 2*xi*d/e*((1-sd)/(1+sd))**2
    a3 = 1-h-gcor
    a16 = (pi*e)**2*(1+alpha*(1+6*alpha/pi)/(5*eta))
    base = 27*a1+9*a2+2*a3+expneg
    return dict(pi=pi, eta=eta, d=d, t=t, alpha=alpha,
                a1=a1, a2=a2, a3=a3, A16=a16, g=base, W=base*(1+d*a16))

def decimal_chain(precision, printed):
    with localcontext() as ctx:
        ctx.prec = precision+20
        values = chain(decimal_pi(), D(1).exp(), (1+D(5).sqrt())/2,
                       (-D(1)/3).exp(), printed)
        ctx.prec = precision
        return {key: +value for key, value in values.items()}

boxes = {key: (F(lo), F(hi)) for key, lo, hi in (
    ('a1', '0.996881270553', '0.996881270554'),
    ('a2', '1.012592613788', '1.012592613789'),
    ('a3', '0.97865878985', '0.97865878994'),
    ('W', '2830.263257664', '2830.263257669'))}
for printed in (False, True):
    intervals = chain(*exact_constants(), printed)
    low, high = decimal_chain(120, printed), decimal_chain(160, printed)
    assert intervals.keys() == low.keys() == high.keys()
    gaps = [abs(F(low[key])-F(high[key])) for key in high]
    assert max(gaps) < F(1, 10**112)
    for key in high:
        assert intervals[key].lo <= F(low[key]) <= intervals[key].hi
        assert intervals[key].lo <= F(high[key]) <= intervals[key].hi
    for key, (lower, upper) in boxes.items():
        assert 0 < lower <= intervals[key].lo <= intervals[key].hi <= upper
    with localcontext() as ctx:
        ctx.prec = 30
        print('printed_alpha', printed, 'fields', len(high),
              'max_120_160_gap', D(max(gaps).numerator)/D(max(gaps).denominator))
        for key in ('a1', 'a2', 'a3', 'W'):
            print(key, +high[key])

# Exact scalar inequalities from the COARSE common enclosures alone.
l1, u1 = boxes['a1']; l2, u2 = boxes['a2']
l3, u3 = boxes['a3']; lw, uw = boxes['W']
G2 = lambda n: F(n*(n+1)*(2*n+1), 6)
G3 = lambda n: F(n*(n+1), 2)
assert G2(19) == 2470 > 13**3 and G3(25) == 325 > 18**2
assert G3(11) == 66 > 8**2 and G3(13) == 91 > 9**2
margins = {
    'N1_ge15': 3375*l1-uw,
    'N1_le13': lw-(2197*u1+324*u2+24*u3+1),
    'N1_14_N2_ge10': 2744*l1+100*l2-uw,
    'N1_14_N2_le8': lw-(2744*u1+64*u2+10*u3+1),
    'N1_14_N2_9': lw-(2744*u1+81*u2+12*u3+1)}
assert min(margins.values()) > F(57, 1000)
for key, value in margins.items():
    # These fractions have finite decimals; this display is exact.
    with localcontext() as ctx:
        ctx.prec = 60
        print(key, 'certified_margin_lower', D(value.numerator)/D(value.denominator))
print('Five exhaustive cases; no mass, fit, greedy search or imported calculator.')
```

## 3. Durchfuehrung und Reichweite

Der unveraenderte obige Block wurde eigenstaendig via `py -3.13 -B -`
ausgefuehrt, Exitcode0. Je Profil wurden elf Decimal-Felder zwischen120/160
Stellen verglichen; alle lagen zugleich innerhalb ihrer unabhaengig erzeugten
rationalen Intervalle. Groesster Absolutabstand: 6.1970833968e-118 im primaeren
und 1.7726909427e-117 im Druckwertprofil, jeweils W. Das sind interne
Praezisionskontrollen, keine zusaetzlichen physikalischen Genauigkeitsaussagen.

Die vier kleinen gemeinsamen Boxen und die fuenf Energiemargen wurden
ausschliesslich durch exakte Fraction-Vergleiche abgesichert. Die unteren
Schranken der positiv orientierten Margen lauten, exakt dezimal dargestellt:

| Fall aus Abschnitt1 | Zertifizierte untere Energiemarge |
|---|---:|
| N1>=15 | 534.211030447375 |
| N1<=13 | 287.547288430666 |
| N1=14,N2>=10 | 6.438210107232 |
| N1=14,N2<=8 | 19.228536081928 |
| N1=14,N2=9 | 0.057144067635 |

Fuer jedes Tupel im deklarierten Paket ist somit sogar
`abs(E-W) >= 0.057144067635 > 0.057` gesichert. Diese globale algebraische
Luecke des festgelegten Pakets ist weder ein Massenresiduum noch eine
physikalische Fehleruntergrenze; sie benutzt absichtlich konservative
unabhaengige Koeffizientenhuellen und ist kein optimierter Abstand.

Die Unmoeglichkeit betrifft gleichzeitig die unveraenderte skalare Gleichung
E=W und die zwei benannten ungewichteten nichtkollabierten Gates. Sie ist
keine Aussage ueber die Existenz des Myons, alle Heim-Eingaben, die
metronische Operatorstruktur oder einen unbekannten dynamischen Kollapspfad.
Insbesondere werden weder Quelle (107b) und (107a) verschmolzen noch A16,
Y9 oder W zur Herstellung eines Treffers geaendert.

## 4. Begrenzte Gegenreview des neuen Zertifikatsrechners

`scripts/audit_coupled_existence.py` vollstaendig gelesen. Keine materiellen
Fehler gefunden. Addition/Subtraktion, vier Eckprodukte, Kehrwert ausserhalb
von Null, nichtnegative Integerpotenzen und isqrt halten Einschliessung ein;
die Rundung auf das 40-Dezimalstellen-Gitter geht an beiden Enden nach aussen.
Wiederholte Intervallmultiplikation darf Abhaengigkeiten verbreitern, verletzt
aber keine Einschliessung. Die alternierenden atan-Teilsummen und der positive
exp-Rest `next_term/(1-x/(terms+2))` sind auf den bewachten Bereichen korrekt.
Die Kehrwertbildung aus exp(1/3) umschliesst exp(-1/3).

Der Root-Rechner verwendet fuer alpha die direkte kleine Quadratwurzelform,
dieser Review die rationalisierte Form und im Decimal-Gegenweg eine Iteration.
Die direkte Form ist bei kleinen Werten ausloeschungsanfaelliger, bleibt hier
aber durch exakte Intervalle korrekt eingeschlossen und hinreichend schmal.
Die ungewichteten Gatefolgen und die fuenf Energiezweige sind algebraisch
vollstaendig fuer den deklarierten Bereich. Die beiden zusaetzlichen globalen
Schwellen fuer N2<=19 beziehungsweise N3<=26 sind ebenfalls korrekt, fuer den
obigen Fuenffallbeweis aber nicht erforderlich.

Die unveraenderten Buchformeln/Indizes und beide Alpha-Profile stimmen mit
dem festgelegten Vertrag ueberein. `certify()` bindet die Eingaben ueber den
kanonischen SHA256-Vergleich in `load_inputs()`; `book_intervals(inputs)` ist
fuer sich ein interner, nicht erneut digest-validierender Rechenhelfer. Daraus
wird keine generische API-Zusage fuer fremde Eingabevertraege abgeleitet.

Selbst ausgefuehrt, Exitcode0:

```text
py -3.13 -B scripts/audit_coupled_existence.py --check --verify-sources
  H004-Hash bestaetigt; beide Profile und alle fuenf Faelle zertifiziert.
  Grobe gemeinsame letzte Marge: 7/5000.
```

Danach wurde der eigene Block erneut ausgefuehrt und fuer einen separaten
Kreuztest ausschliesslich der neue eigene Root-Rechner importiert. Fuer alle
13 gemeinsamen Groessen je Profil (pi,e,xi,eta,eta11,eta12,alpha,A16,g,a1,a2,a3,W)
liegt das gesamte engere eigene Fraction-Intervall innerhalb des Root-
Intervalls: 26 exakte Einschlussvergleiche bestanden. Dies ist kein Vergleich
bloss gerundeter Mittelpunktwerte. Der unabhaengige Rechenweg oben bleibt
ohne diesen Root-Import selbstenthalten.

Zusaetzlich fuer alle 143 rationalen Werte n/d mit n=0..10, d=1..13 den
Root-isqrt-Pfad geprueft: `lo^2 <= n/d <= hi^2` immer exakt erfuellt. Diese
endlichen Zusatzkontrollen ergaenzen die analytische Codegegenlesung, ersetzen
keinen allgemeinen Beweis der Bibliothek und emulieren keine Quellenprogramme.
Root-Tests waren zum Zeitpunkt dieses Checks noch nicht vorhanden.
