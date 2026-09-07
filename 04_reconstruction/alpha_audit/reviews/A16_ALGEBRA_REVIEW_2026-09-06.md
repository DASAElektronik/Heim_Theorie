# A16: unabhängige Algebra und bedingte Ganzzahlgrenze

2026-09-06, Etappe 27. Gegebene P-/L-Lesarten, vorhandene Ergebnisse aus
MUON_SELECTION und MUON_NUMERICS_REVIEW. Keine neue Quellenlesung,
Massenrechnung, Modellanpassung oder Änderung alter Rechenprofile.

## 1. Basis und zwei algebraische Korrekturterme

Mit den eigenen Hilfsnamen A0=(pi*e)^2 und
u_A=alpha/5+6*alpha^2/(5*pi) lauten die beiden Ausdrücke

```text
P = A0*(1+u_A/eta),
L = A0*(1+u_A*eta).
```

Bei festen pi,e,eta ist A16 exakt quadratisch in alpha:

| Rolle | P: Nennerprodukt | L: linkassoziativ |
| --- | --- | --- |
| alpha-unabhängige Basis | pi^2*e^2 | pi^2*e^2 |
| linearer Term | pi^2*e^2*alpha/(5*eta) | pi^2*e^2*eta*alpha/5 |
| quadratischer Term | 6*pi*e^2*alpha^2/(5*eta) | 6*pi*e^2*eta*alpha^2/5 |

Die Aufteilung ist eine Identität der gegebenen Formeln. Sie beweist
weder getrennte physikalische Kanäle noch die Herkunft der Zahlen 5 und 6,
der Basis oder der eta-Bindung. alpha ist hier das nackte Alpha des
festgelegten Quellenprofils, nicht alpha1/2/3 oder ein neuer Fitparameter.

eta ist durch eta^4=pi^4/(pi^4+4) festgelegt; für pi>0 gilt 0<eta<1.
Es ist nicht eta11=d und auch kein frei veränderbarer zusätzlicher Parameter.
Eine formale Variation einzelner Symbole ist von der gesamten gekoppelten
Quellenkette zu unterscheiden. Insbesondere enthält g über alpha3 weitere
Alpha-Abhängigkeit: Die volle Funktion W(alpha) ist nicht schon deshalb
quadratisch, weil A16 bei festgehaltenen übrigen Größen quadratisch ist.

## 2. Exakte P-minus-L-Differenz und Übertragung auf W

Bei identischen pi,e,alpha,eta in beiden Lesarten gilt

```text
Delta_A = P-L
        = (pi*e)^2 * alpha*(1+6*alpha/pi)/5 * (1/eta-eta)
        = pi*e^2 * alpha*(pi+6*alpha)*(1-eta^2)/(5*eta).
```

Der Basisterm hebt sich auf; lineare und quadratische Korrektur tragen
denselben eta-Faktorunterschied. Für pi>0,e>0,alpha>0 und 0<eta<1 ist
Delta_A strikt positiv und P>L>A0. Die eta-Bedingung allein genügt nicht
für dieses Vorzeichen, wenn Alpha oder andere Voraussetzungen freigelassen
werden. Bei alpha=0 oder formal eta=1 stimmen beide Lesarten überein;
eta=1 ist kein endlicher positiver pi-Wert der angegebenen eta-Definition.

Nur für die Korrekturteile gilt (P-A0)/(L-A0)=eta^(-2), sofern sie nicht
verschwinden. Dieser Quotient ist NICHT P/L; die gemeinsame Basis bleibt
in den vollständigen A16-Werten erhalten.

Bei demselben vollständigen Zahlenprofil sind d und g im P/L-Vergleich
unverändert. Aus W=g*(1+d*A16) folgt dann exakt

```text
Delta_W = W_P-W_L = g*d*Delta_A.
```

Für d>0,g>0 hat Delta_W dasselbe positive Vorzeichen. Positives g folgt
im geprüften Auswahlfall aus positiven alpha1,alpha2,alpha3 und dem
positiven Exponentialbeitrag, nicht allein aus der Definition von eta.
Die Formel ist eine Übertragung eines festgelegten Lesartenwechsels,
keine physikalische Kausalzuordnung und keine Herleitung von A16.

## 3. Was bei festen K1..3 an der K4-Grenze geschieht

Fixiere innerhalb jedes P/L-Paars dieselben alpha1..3 und
K1..3=(14,9,3), wie in Etappe 26 getrennt durch Maximalreste geprüft.
Mit S123=alpha1*14^3+alpha2*9^2+alpha3*3 ist
W4=W-S123, also Delta_W4=Delta_W. Aus dem positiven Delta_W allein
folgt nicht, dass K1..3 unverändert bleiben; diese Voraussetzung wurde
für die vorhandenen zwölf Zellen numerisch geprüft, nicht allgemein bewiesen.

Im mittleren Fall 0<r=W4<=1 und bei lambda=1/3 lautet der reelle Wert
x=-3*ln(r). Die Ganzzahlbereiche sind exakt

```text
floor(x)=0  genau für  exp(-1/3) < r <= 1,
floor(x)=1  genau für  exp(-2/3) < r <= exp(-1/3).
```

Die untere r-Grenze ist jeweils offen, die obere geschlossen. Bei
r=exp(-1/3) gilt x=1 und K4=1; bei r=exp(-2/3) bereits K4=2.
Die Exponentialschwellen sind mathematische Funktionen, kein Potenzieren
eines gegebenenfalls gerundeten e-Eingangs aus einem Zahlenprofil.

Die bereits dokumentierten P-Werte r≈0.77550 bis 0.77552 liegen oberhalb
der ersten Schwelle ≈0.71653; die L-Werte r≈0.69278 bis 0.69280 liegen
zwischen den beiden Schwellen. Das erklärt die vorhandene Auswahl
K4_P=0 gegenüber K4_L=1 ohne neue Massenrechnung. Das größere P-A16 erhöht
bei festem Restabzug W4, senkt also -3*ln(W4). Beide nach floor verbleibenden
Gleichungsreste sind weiterhin positiv; unterschiedliche Reste sind kein
Kriterium für historische Autorschaft oder die richtige Editionslesart.

## 4. Ausführbare unabhängige Fraction-Kontrolle

Die rationalen Symbole im ersten Teil prüfen die algebraischen Identitäten
auf synthetischen Eingaben. p ist dort kein behaupteter rationaler Wert
von pi; frei gewähltes eta bildet keine gemeinsame Heim-Konfiguration.
Der zweite Teil liest ausschließlich die zwölf schon veröffentlichten,
gerundeten W4-Werte dieser Arbeit. Die Exp-Schwellen werden rational
eingeschlossen, nicht durch einen alten Rechner importiert. Damit werden
die zitierten Zahlen gegen exakte Schwellenintervalle geprüft, NICHT die
gesamte vorangehende transzendente Quellenrechnung intervallzertifiziert.

```python
from fractions import Fraction as F
from itertools import product


def readings(p, eb, alpha, eta):
    base = (p*eb)**2
    correction = alpha*(1+6*alpha/p)/5
    return base*(1+correction/eta), base*(1+correction*eta), base


count = 0
for p, eb, alpha, eta, d, g in product(
        (F(3), F(22, 7)), (F(2), F(11, 4)),
        (F(1, 100), F(1, 10)), (F(1, 2), F(4, 5), F(99, 100)),
        (F(3, 4), F(1)), (F(1), F(7))):
    P, L, base = readings(p, eb, alpha, eta)
    linear, quadratic = p*p*eb*eb*alpha/5, 6*p*eb*eb*alpha*alpha/5
    assert P == base+(linear+quadratic)/eta
    assert L == base+(linear+quadratic)*eta
    delta = p*eb*eb*alpha*(p+6*alpha)*(1-eta*eta)/(5*eta)
    assert P-L == delta > 0 and P > L > base
    assert (P-base)/(L-base) == 1/(eta*eta)
    assert P/L != 1/(eta*eta)
    WP, WL = g*(1+d*P), g*(1+d*L)
    assert WP-WL == g*d*delta
    arbitrary_same_subtraction = F(19, 7)
    assert (WP-arbitrary_same_subtraction)-(WL-arbitrary_same_subtraction) == g*d*delta
    eta_fourth_from_p = p**4/(p**4+4)
    assert 0 < eta_fourth_from_p < 1
    count += 1
assert count == 96
assert readings(F(3), F(2), F(0), F(4, 5))[:2] == (F(36), F(36))
P, L, _ = readings(F(3), F(2), F(1, 10), F(1))
assert P == L
P, L, _ = readings(F(3), F(2), F(-1, 4), F(4, 5))
assert P < L  # eta in (0,1) alone does not imply the positive-alpha result.


def exp_negative_bounds(x, terms=24):
    # x>=0: sum exp(x) through n, geometric upper bound on the positive tail.
    x = F(x)
    assert 0 <= x < terms+2
    term = total = F(1)
    for j in range(1, terms+1):
        term *= x/j
        total += term
    next_term = term*x/(terms+1)
    upper = total+next_term/(1-x/(terms+2))
    return 1/upper, 1/total


lo1, hi1 = exp_negative_bounds(F(1, 3))
lo2, hi2 = exp_negative_bounds(F(2, 3))
assert F("0.7165") < lo1 <= hi1 < F("0.7166")
assert F("0.5134") < lo2 <= hi2 < F("0.5135")
quoted_pairs = [
    ("0.7755039220886995", "0.6927848240193449"),
    ("0.7755120560046683", "0.6927929576918099"),
    ("0.7755039502393991", "0.6927848521692018"),
    ("0.7755120841553648", "0.6927929858416636"),
    ("0.7755069136887019", "0.6927878155092382"),
    ("0.7755150476046777", "0.6927959491817101"),
]
for p_text, l_text in quoted_pairs:
    rP, rL = F(p_text), F(l_text)
    assert hi1 < rP <= 1          # K4=0 for these quoted numerical values.
    assert hi2 < rL < lo1         # K4=1; no endpoint or epsilon promotion.
    assert rP-rL > 0
print("OK:", count, "exact synthetic identities;",
      len(quoted_pairs)*2, "previously quoted W4 values against rational exp bounds")
```

Aus dieser Review ausgeführt mit py -3.13 -B: Exitcode 0; 96 exakte
synthetische Identitätsprüfungen und alle zwölf zitierten W4-Werte bestanden.
Keine bestehenden Rechner, Tests oder Eingaben wurden geändert.

Die Algebra benötigt kein passendes K4 oder Massenziel als Auswahlhilfe.
Ein historischer Beleg für P oder L muss aus der Quelle stammen; weder
die Faktorisierung noch die unterschiedliche Ganzzahlentscheidung ersetzt
ihn. Ein solcher Beleg würde seinerseits noch nicht die physikalische
Herleitung oder die vollständige Gleichungserhaltung bestätigen.

## 5. Getrennter Nachtrag: Buchform mit Y9

Neue Quellenmitteilung von Root und book_derivation, nicht eigene Glyphenprüfung:
H004 Druck335/PDF341 gibt A16_book=P*Y9. Y9 multipliziert den GANZEN
P-Ausdruck, also Basis, linearen und quadratischen Term gemeinsam; nicht
nur den Alpha-Korrekturteil. Der dortige Herleitungs-/Heuristikkontext
wird in der Quellenreview geprüft und durch die folgende Algebra nicht ersetzt.

Für eine rein formale Ersetzung dieses expliziten Y9-Vorkommens und bei
festgehaltenen g,d sowie aP=P gilt

```text
A16_book(Y9) = aP*Y9,
W(Y9) = g*(1+d*aP*Y9),
W(Y9)-W(1) = g*d*aP*(Y9-1).
```

W ist in diesem eingefrorenen Vergleich affin in Y9. Falls g,d,aP positiv
sind, ist die Steigung g*d*aP positiv. Andere mögliche Abhängigkeiten der
vollständigen Buchkette sind hier weder eingesetzt noch ausgeschlossen.
Insbesondere wird kein gesamter Buch-Auswahlalgorithmus mit H006 identifiziert.

Die symbolische Spezialisierung Y9=1 ergibt A16_book=P und erklärt damit
die lokale Formgleichheit. Sie beweist weder Y9=1 aus einer Dynamik noch
die Gleichheit aller übrigen Buch-/H006-Größen. Quellenbenannte Unsicherheit
von Y9 ist kein statistisches Fehlerintervall. Diese Diagnose autorisiert
keinen freien Fit, keinen neuen Y9-Wert und keine Optimierung auf K4 oder Masse.
Y9 wird auch nicht mit den früheren Korrelationsfaktoren Y3 gleichgesetzt.

```python
from fractions import Fraction as F

checks = 0
for g, d, aP in ((F(1), F(3, 4), F(5)),
                 (F(7, 3), F(4, 5), F(9, 2)),
                 (F(2), F(1), F(1, 3))):
    W1 = g*(1+d*aP)
    for y in (F(0), F(1), F(3, 2), F(2)):
        # Synthetic algebra witnesses, not admissible source values for Y9.
        W = g*(1+d*aP*y)
        assert W-W1 == g*d*aP*(y-1)
        assert aP*F(1) == aP
        if y == 0:
            assert W == g
        if y > 1:
            assert W > W1
        checks += 1
print("OK:", checks, "exact affine-Y9 identities; no fitted/source Y9 chosen")
```

Dieser zweite eigene Block wurde separat ausgeführt: zwölf exakte
Identitätsprüfungen bestanden, Exitcode 0. Alte Profile bleiben unverändert.
