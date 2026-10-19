# Massenkette: reine Polynom- und Skalierungsprüfung

2026-09-07, Etappe 38. Eigene bedingte Algebra, kein Fit und keine
Teilchenmassenauswertung. Nur die vom Hauptagenten übermittelten Formeln
werden geprüft; eine eigene visuelle Originallektüre wird nicht behauptet.
Nachtrag zur Zuschreibung: Beide Quellenagenten und der Hauptagent
bestätigten nach Detailprüfung auf Druck 344 beide Male `+3*Q2`.
`+2*Q2` war eine verworfene anfängliche Lesehypothese, keine Buchfassung.
Der Hauptagent bestätigte außerdem den unten benötigten M-Ausgang auf
Druck 278 und `mu_plus=4*mu*alpha_plus` in (97), Druck 253.
Der frühere [Quellenreview zur F_S-Rolle](EQ108_STATUS_DOWNSTREAM_REVIEW_2026-09-07.md)
wurde für den getrennten Ausgang `M=mu_+*(sum a_j G_j+q*r)+mu_S*F_S`
herangezogen. Insbesondere wird aus einer Umschreibung keine Herleitung
der empirischen Funktion F_S.

## 1. Notation und exakte Zerlegung

`n=(n1,...,n4)`, `Q=(Q1,...,Q4)` und `x_j=n_j+Q_j` sind voneinander zu
unterscheiden. Die in (112b) ebenfalls mit N bezeichneten Koeffizienten
heißen hier ausschließlich

```text
c1=a1, c2=2*a2/3, c3=2*a3; a4=1.
```

Sie sind keine Besetzungszahlen. Für die übermittelten (98e)-Polynome

```text
G1(x)=x1²*(1+x1)²/4,
G2(x)=x2*(2*x2²+3*x2+1)/6,
G3(x)=x3*(1+x3)/2, G4(x)=x4
```

setze als eigene Hilfsnotation

```text
P(u) = c1*u1²*(1+u1)²
     + c2*u2*(2*u2²+3*u2+1)
     + c3*u3*(1+u3) + 4*u4,
K3 = P(Q), F = P(n).
```

Der Index an `K3` kennzeichnet nur den bestätigten Term mit `3*Q2` im zweiten
Polynom, nicht Zone 3 oder eine neue Quellenvariable. Dann ist

```text
4*sum_j a_j*G_j(n+Q) = P(n+Q) = K3 + F + H,

H = 2*n1*Q1*[1+3*(n1+Q1+n1*Q1)+2*(n1²+Q1²)]*c1
  + 6*n2*Q2*(1+n2+Q2)*c2 + 2*n3*Q3*c3.
```

Die Identität folgt koeffizientenweise. Beispielsweise ist der erste
gemischte Anteil
`4*n1³*Q1+6*n1²*Q1²+4*n1*Q1³+6*n1²*Q1+6*n1*Q1²+2*n1*Q1`,
multipliziert mit c1. In Zone 4 entsteht kein gemischter Term, da G4
linear ist. Die Faktoren 4, 2/3 und 2 sind dabei notwendig.

Es handelt sich um eine Polynomidentität für beliebige reelle Argumente
und Koeffizienten. Ganzzahligkeit, positive Koeffizienten oder physikalische
Zustandszulassung werden für diese Identität nicht benötigt und dadurch
auch nicht bewiesen. Negative kleine n sind algebraisch kein Problem.

## 2. Verworfene Lesehypothese als synthetische Mutationsprobe

Es gibt laut abgeschlossener übermittelter Quellenprüfung keine zweite
gedruckte Schreibweise. Ausschließlich für eine eigene Mutationsprobe
ersetzen wir in K3 den Term `c2*Q2*(2*Q2²+3*Q2+1)` durch
`c2*Q2*(2*Q2²+2*Q2+1)` und lassen den Rest unverändert. Dieses künstliche
Polynom heiße K2. Dann exakt

```text
K2 - K3 = -c2*Q2² = -(2/3)*a2*Q2²,
4*sum a_j*G_j - (K2+F+H) = c2*Q2².
```

Die beiden Ausdrücke stimmen als Funktionen nicht überein. Bei
`a2>0` und `Q2!=0` ist der zweite Rest strikt positiv; Gleichheit an
`Q2=0` oder `a2=0` wäre ein Sonderfall, kein Identitätsbeweis. Ein rein
synthetischer Zeuge `a2=3/2,Q2=2` gibt `K2-K3=-4`.
Das ist kein Quellenkonflikt, keine Versionsdifferenz und keine
Quellenkorrektur. Die Probe zeigt lediglich, dass die exakte Zerlegung
diese einzelne künstliche Koeffizientenänderung erkennen kann.

## 3. Bedingte Massentransformation

Unter dem ausdrücklich angegebenen Skalierungsanschluss

```text
mu_plus=4*mu*alpha_plus,
r=alpha_minus/alpha_plus, alpha_plus!=0,
mu_S=mu_plus*(1-r),
M=mu_plus*[sum a_j*G_j+(1-r)*F_S+q*r],
phi=4*(1-r)*F_S+4*q*r
```

folgt ohne weitere Näherung

```text
M = mu*alpha_plus*[4*sum a_j*G_j + phi]
  = mu*alpha_plus*[K3+F+H+phi].
```

Die angegebene phi-Definition allein ersetzt den nötigen Anschluss
`mu_S=mu_plus*(1-r)` nicht; dieser ist im übermittelten originalbestätigten
M-Ausgang enthalten. Ohne diesen Anschluss lautete der Beitrag aus
F_S zunächst `mu_S*F_S`, und die Zusammenfassung wäre nur bedingt.
Bei festem Rest erzeugte die synthetische K2-Mutation den Unterschied
`M_K2-M_K3=-mu*alpha_plus*c2*Q2²`, keine neu bestimmte Massenkorrektur.

Es wird hier keine H006- oder H013-Klammerstruktur hineingelesen.
Insbesondere steht alpha_plus in dieser Rechnung vor der ganzen Klammer;
die Identität `alpha_plus*r=alpha_minus` gilt erst zusammen mit der
angegebenen r-Definition. Für `alpha_plus=0` ist diese Quotientenschreibweise
nicht definiert. Bei `r=1` entfällt die F_S-Wirkung in diesem Vertrag und
`phi=4*q`; das ist ein algebraischer Randfall, keine physikalische Wahl.

Nur wenn alle Klammergrößen dimensionslos sind, trägt mu die Masseneinheit.
Die Umschreibung legt weder mu numerisch noch F_S, Besetzungen oder eine
Referenzmasse fest. Sie verändert auch nicht den Auswahlrest von (108).

## 4. Selbstenthaltener exakter Kontrollblock

Nur Standardbibliothek, keine Projekt- oder historischen Programmimporte.
Zuerst werden sämtliche Koeffizienten der bivariaten gemischten Polynome
verglichen; das ist der formale Identitätscheck, nicht bloß eine Stichprobe.
Anschließend folgen rationale Kontrollfälle und die künstliche K2-Mutation.
Die skalierte M-Kontrolle verwendet synthetische rationale Parameter ohne
Einheit oder Zuordnung zu realen Teilchen; ausgegeben wird nur die Prüfzahl.

```python
from fractions import Fraction as Q
from itertools import product
from math import comb

checks = 0

def same(left, right):
    global checks
    assert left == right, (left, right)
    checks += 1

# Each pair (i,j) denotes the coefficient of n**i * Qref**j.
def mixed(coeff):
    out = {}
    for degree, value in coeff.items():
        for i in range(1, degree):
            out[i, degree-i] = value * comb(degree, i)
    return {power: value for power, value in out.items() if value}

same(mixed({2: 1, 3: 2, 4: 1}),
     {(1,1): 2, (1,2): 6, (2,1): 6,
      (1,3): 4, (2,2): 6, (3,1): 4})
same(mixed({1: 1, 2: 3, 3: 2}),
     {(1,1): 6, (1,2): 6, (2,1): 6})
same(mixed({1: 1, 2: 1}), {(1,1): 2})
same(mixed({1: 4}), {})

def weights(a):
    return a[0], Q(2,3)*a[1], 2*a[2]

def pure(u, a, middle=3):
    u1,u2,u3,u4 = u
    c1,c2,c3 = weights(a)
    return (c1*u1*u1*(1+u1)**2
            +c2*u2*(2*u2*u2+middle*u2+1)
            +c3*u3*(1+u3)+4*u4)

def cross(n, qref, a):
    n1,n2,n3,_ = n
    v1,v2,v3,_ = qref
    c1,c2,c3 = weights(a)
    return (2*n1*v1*(1+3*(n1+v1+n1*v1)+2*(n1*n1+v1*v1))*c1
            +6*n2*v2*(1+n2+v2)*c2+2*n3*v3*c3)

def source_sum(x, a):
    u,v,w,z = x
    return (a[0]*u*u*(1+u)**2/4
            +a[1]*v*(2*v*v+3*v+1)/6
            +a[2]*w*(1+w)/2+z)

coefficients = [tuple(map(Q, a)) for a in
                [(1,1,1), (Q(2,7),Q(3,2),Q(5,3)), (0,0,0)]]
occupations = [tuple(map(Q, n)) for n in
               [(0,0,0,0), (1,2,3,4), (-1,0,-2,-1),
                (Q(1,2),Q(-2,3),Q(3,5),Q(7,4))]]
references = [tuple(map(Q, v)) for v in
              [(0,0,0,0), (1,2,3,1), (Q(2,3),Q(3,4),1,Q(1,2))]]

for a,n,qref in product(coefficients, occupations, references):
    x = tuple(u+v for u,v in zip(n,qref))
    s = source_sum(x, a)
    k3, k2 = pure(qref,a), pure(qref,a,2)
    f, h = pure(n,a), cross(n,qref,a)
    defect = weights(a)[1]*qref[1]**2
    same(4*s, k3+f+h)
    same(k2-k3, -defect)
    same(4*s-(k2+f+h), defect)
    for mu,ap,am,fs,charge in product(
            [Q(2,3)], [Q(3,2),Q(-1,2)], [Q(1,5),Q(3,2)],
            [Q(0),Q(7,9)], [Q(-1),Q(0),Q(2)]):
        r = am/ap
        mu_plus = 4*mu*ap
        mu_s = mu_plus*(1-r)
        phi = 4*(1-r)*fs+4*charge*r
        original = mu_plus*(s+charge*r)+mu_s*fs
        transformed = mu*ap*(k3+f+h+phi)
        same(original, transformed)
        same(mu*ap*(k2+f+h+phi)-transformed, -mu*ap*defect)

same(pure((Q(0),Q(2),Q(0),Q(0)), (Q(1),Q(3,2),Q(1)), 2)
     -pure((Q(0),Q(2),Q(0),Q(0)), (Q(1),Q(3,2),Q(1))), -4)
print('Exact coefficient/identity checks:', checks)
```

Ausgeführt durch Extraktion genau dieses Blocks nach `py -3.13 -B -`:
Exitcode 0, `Exact coefficient/identity checks: 1841`. Die Prüfzahl enthält
abhängige Identitätskontrollen, keine unabhängigen Experimente. Der Block
schreibt keine Dateien und benutzt keine Massendaten.

## Ergebnisgrenze

Die bestätigte H-Zerlegung und die mu/phi-Transformation tragen unter den
übermittelten Quellenansätzen exakt algebraisch. Die anfängliche
Q2-Leseunsicherheit ist positiv geklärt, kein neuer Quellenfehler gefunden.
Die künstliche Mutation gehört nur zur Kontrollmethode. Die bestätigte
Identität validiert keine Zustandsauswahl, bestimmt F_S nicht und
repariert (108) nicht. Kalibrierung bleibt von dieser Algebra getrennt.
