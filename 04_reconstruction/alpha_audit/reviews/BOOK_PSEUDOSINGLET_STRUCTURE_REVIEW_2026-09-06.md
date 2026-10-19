# Buch-Pseudosingulett: unabhaengiger skalarer Strukturvertrag

2026-09-06, Etappe 30, Ausgang `00180ec`. Noch keine numerische Teilchen-
oder Massenrechnung. Keine Uebernahme von H006-XIII/XXXII oder alten Rechnern.
Diese Review trennt die gedruckten Buchstufen und ihre eigene skalare Algebra;
sie vereinheitlicht keinen unklaren Anschluss durch eine eigene Quellenformel.

## 1. Quellenumfang und Methode

PDF-Skill sowie `00_admin/SOURCE_ATTRIBUTION.md` und GUARDRAILS vollstaendig
gelesen. Eigene Sichtpruefung der gesamten relevanten Seiten der lokalen H004:
Burkhard Heim, *Elementarstrukturen der Materie II*, Ausgabe 1996,
Druck278/PDF284 und Druck321-330/PDF327-336. Vollseiten wurden an vorhandenen
Renderings gelesen; keine neuen Ausschnitte, PDFs oder Quelleninhalte erzeugt.

Lokale Kopie: `01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`.
SHA-256 erneut gelesen und passend:
`F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.
Der Hash identifiziert die untersuchte Kopie, nicht die Echtheit eines Papieroriginals.

Tragende direkte Fundstellen:

| Fundstelle | Eigener visueller Befund |
|---|---|
| II278, (98d)/(98e), PDF284 | G_j sind die unten angegebenen ungewichteten Polynome; in (98d) stehen alpha_j separat vor G_j. |
| II321, (107), PDF327 | delta_j G_j > G_(j+1), delta_j G_j >= delta_(j+1) G_(j+1), j=1..3. |
| II322, PDF328 | N_(j)=n_j+Q_j sind ganzzahlig >=0; Q_j>0, negative n_j bis -Q_j moeglich. |
| II323, PDF329 | delta_j N_(k)=delta_j n_k=delta_jk; ausdruecklich delta G=(N1^3,N2^2,N3,1). In W bleiben alpha_j separate Faktoren. |
| II327/328, (107a), PDF333/334 | beta_j=delta_(j-1)G_(j-1)-G_j, j>1; ganzzahlige Bandbreiten, beta_j>=1; Kollaps bei beta_j=0 gesondert. delta_1G_1>0, -Q_j<=n_j<=L_j<infty. |
| II329, (107b), PDF335 | beta4=delta_3G_3-(n4+Q4)=alpha3*N_(3)-N_(4)>0; dies ist anders gewichtet als II323. Kontext: sigma-Anregung. |
| II327/330, (108)/(108a), PDF333/336 | f(0)=0, N>=0 als Resonanzordnung; diese N ist nicht eine der vier N_(j). |

Die folgenden Abkuerzungen N1..N4 stehen ausschliesslich fuer N_(1)..N_(4).
Sie sind weder die Resonanzordnung N noch die Verschiebungen n_j.
Die Dichtefaktoren eta_j in (98e) sind nicht eta_qk; keine Gleichsetzung erfolgt.

## 2. Ungewichtete G_j und ihre Differenzen

Aus (98e), unmittelbar und ohne einen alpha-Faktor:

```text
G1(N1) = N1^2*(N1+1)^2/4,
G2(N2) = N2*(N2+1)*(2*N2+1)/6,
G3(N3) = N3*(N3+1)/2,
G4(N4) = N4.
```

Die gewoehnliche Rueckwaertsdifferenz P(t)-P(t-1) dieser Polynome ergibt
exakt D1=N1^3, D2=N2^2, D3=N3, D4=1. Das ist hier nicht nur eine
vermutete Operatorwahl: II323 schreibt diese vier Resultate ausdruecklich hin.
Die skalare Nachrechnung prueft diese Identitaeten, nicht eine allgemeine
metronische Operatorvaliditaet. Am Nullrand ist eine Polynomfortsetzung kein
Nachweis eines physikalisch zulaessigen Schritts in negative Besetzungen.

Fuer nichtnegative ganze N_j sind G_j und D_j ganzzahlig. G1,G2,G3 sind
die Summen der Kuben, Quadrate bzw. ganzen Zahlen von 1 bis zum Argument.
Insbesondere gilt G2>=N2^2 und G3>=N3. Fuer G4>=D4=1 waere dagegen
N4>=1 noetig; diese Zwischenbegruendung gilt nicht im leeren N4=0-Fall.
Die vollstaendigen Gates unten bleiben am Nullrand dennoch wohl definiert.

## 3. Direkt auswertbare Gates aus (107)/(107a)

Der ungewichtete, nicht kollabierte Zweig hat genau folgende erste Reihe:

```text
B2 = N1^3 - N2*(N2+1)*(2*N2+1)/6 >= 1,
B3 = N2^2 - N3*(N3+1)/2           >= 1,
B4 = N3 - N4                     >= 1.
```

B2..B4 sind eigene eindeutige Variablennamen fuer die beta_j dieser
ungewichteten Stufe. Die strikten Ungleichungen aus (107) sind wegen
Ganzzahligkeit zu den jeweiligen >=1-Bedingungen aequivalent.
Die zweite Reihe aus (107) lautet explizit

```text
N1^3 >= N2^2,  N2^2 >= N3,  N3 >= 1.
```

Bei ganzzahligen N_j>=0 folgt sie bereits aus der ersten Reihe:
G2>=N2^2, G3>=N3 und N3>N4>=0 implizieren diese Aussagen. Letzteres
benutzt Ganzzahligkeit und nicht die am Nullrand ungueltige Hilfsannahme
G4>=1. Auch das Zentrumsgate D1>0, also N1>=1, folgt dann automatisch.
Ein Rechner darf die zweite Reihe dennoch separat ausgeben, um beide
gedruckten Forderungen sichtbar zu halten.

Die erste Reihe erzwingt sogar N3>=1, N2>=2 und N1>=2. Dies sind nur
notwendige Folgen des deklarierten nicht kollabierten skalaren Zweigs,
keine gefundene Teilchenbesetzung. N4 darf dabei null sein. Allgemein
bleiben N_j>=0 und n_j=N_j-Q_j>=-Q_j zu pruefen; n_j<0 ist nicht verboten.
Die oberen L_j bzw. L_N werden in diesem lokalen Abschnitt nur als endlich
gefordert, nicht als neue numerische Eingaben geliefert.

Der Kollapsfall ist kein weiterer statischer Zustand mit unveraenderten
Zahlen: II328 beschreibt bei beta_j=0 das Zusammenbrechen G_j->0 und
die Erhoehung n_(j-1)->n_(j-1)+1. Unter festen Q_j bedeutet G_j=0 auf
der nichtnegativen Domaene N_j=0. Vor-/Nachzustand muessen auseinandergehalten
werden; insbesondere darf beta_j=0 nicht unbemerkt auch am Nachzustand
mit erhoehter vorheriger Besetzung gefordert werden. Ein vollstaendiger
Kaskaden-, Neuberechnungs- oder Akzeptanzalgorithmus wird daraus hier nicht
erfunden. Werte mit B_j<1 sind nicht einfach als aktive Standardfaelle akzeptiert.

## 4. Separater Anschluss (107b): kein stiller Gewichtungswechsel

II329 druckt fuer die sigma-Bandbreite dagegen

```text
B4_sigma = alpha3*N3 - N4 > 0.
B4_sigma - B4 = (alpha3-1)*N3.
```

Der Faktor alpha3 ist in II323 gerade nicht in delta_3G_3 enthalten:
dort steht delta_3G_3=N3, und W wird aus sum_j alpha_j*delta_jG_j aufgebaut.
Eine zwischen diesen Stellen eingefuehrte Definition G_j->alpha_jG_j oder
delta_j->alpha_j*delta_j wurde auf den vollstaendig geprueften Seiten
nicht gefunden. Insbesondere folgt aus einer einzelnen spaeteren gewichteten
beta4-Zeile keine allgemeine gewichtete Fassung aller sechs (107)-Gates.

Wenn beide beta4-Definitionen gleichzeitig dieselbe Groesse am selben
Tupel mit unveraenderter Bedeutung von G und delta bezeichnen sollen, ist
ihre Gleichheit genau dann moeglich, wenn (alpha3-1)*N3=0. Im nicht
kollabierten ungewichteten Zweig N3>=1 reduziert sich das auf alpha3=1.
Dies ist ein bedingter lokaler Anschlussbefund, keine Auswahlregel, mit der
alpha3 nachtraeglich auf 1 gesetzt werden duerfte. Eine beabsichtigte
Umdefinition, Textkorrektur oder physikalische Gleichsetzung wird nicht behauptet.

Fuer eine spaetere Diagnose sind deshalb getrennte Ausgaben sinnvoll:
ungewichtete B2/B3/B4 samt beiden (107)-Reihen; daneben B4_sigma aus
(107b), dessen Positivitaet und ggf. der separat verlangte Vergleich >=1.
Die Ganzzahligkeit von B4_sigma folgt bei allgemeinem reellem alpha3
nicht aus ganzzahligen N3,N4. Daher darf >0 hier nicht allein mittels
Integerargument in >=1 umgeschrieben werden. Dies klaert auch nicht die
physikalische Anwendung der sigma-Anregungsbedingung auf jeden N=0-Fall.

Es wird kein geschlossenes, widerspruchsfreies Gesamt-Zustandspraedikat
behauptet. (108)-Rest, TRC-/Kappenregeln und die oben genannten Gates sind
getrennte Pruefpunkte; bestandenes Greedy ist kein Ersatz dieser Nachpruefung.

## 5. Eigene exakte Algebra-Zertifikate

Der folgende selbstenthaltene Standardbibliotheksblock verifiziert die vier
Polynomidentitaeten exakt durch Koeffizientenvergleich. Die zusaetzlichen
endlichen Gittertests kontrollieren Implementations- und Randlogik; sie sind
keine erschoepfende physikalische Zustandssuche und keine Teilchenrechnung.
alpha3=3/2 dient nur als eigener rationaler Zeuge der Definitionsdifferenz.

```python
from fractions import Fraction as F
from itertools import product
from math import comb

checks = 0
def check(value, label):
    global checks
    assert value, label
    checks += 1

polys = (
    (F(0), F(0), F(1, 4), F(1, 2), F(1, 4)),
    (F(0), F(1, 6), F(1, 2), F(1, 3)),
    (F(0), F(1, 2), F(1, 2)),
    (F(0), F(1)),
)
targets = ((F(0), F(0), F(0), F(1)),
           (F(0), F(0), F(1)), (F(0), F(1)), (F(1),))

def backward_coefficients(coefficients):
    out = list(coefficients)
    for power, coefficient in enumerate(coefficients):
        for degree in range(power+1):
            out[degree] -= coefficient*comb(power, degree)*(-1)**(power-degree)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)

def evaluate(coefficients, value):
    return sum((c*F(value)**j for j, c in enumerate(coefficients)), F(0))

for polynomial, target in zip(polys, targets, strict=True):
    check(backward_coefficients(polynomial) == target, 'exact polynomial identity')

for n in range(16):
    for polynomial, target in zip(polys, targets, strict=True):
        check(evaluate(polynomial, n).denominator == 1, 'integer unweighted G')
        # At n=0 this is polynomial extension, not an allowed physical step.
        check(evaluate(polynomial, n)-evaluate(polynomial, n-1)
              == evaluate(target, n), 'backward endpoint arithmetic')

active = 0
for numbers in product(range(6), repeat=4):
    g = tuple(evaluate(poly, n) for poly, n in zip(polys, numbers, strict=True))
    d = (F(numbers[0]**3), F(numbers[1]**2), F(numbers[2]), F(1))
    beta = tuple(d[j]-g[j+1] for j in range(3))
    strict = all(d[j] > g[j+1] for j in range(3))
    check(strict == all(b >= 1 for b in beta), 'strict/integer reserve equivalence')
    if strict:
        active += 1
        check(all(d[j] >= d[j+1] for j in range(3)), 'second gate row follows')
        check(d[0] > 0, 'central gate')
        check(numbers[0] >= 2 and numbers[1] >= 2 and numbers[2] >= 1,
              'necessary lower bounds of active branch')
check(active > 0, 'nonempty synthetic scalar branch')

for n3, n4 in product(range(6), repeat=2):
    b4, sigma = F(n3-n4), F(3, 2)*n3-n4
    check(sigma-b4 == (F(3, 2)-1)*n3, 'two printed-stage expressions differ')
    check((sigma == b4) == (n3 == 0), 'equality at fixed alpha3=3/2')
check(F(3, 2)*1-1 == F(1, 2), 'positive weighted reserve need not be >=1')
check((F(3, 2)*1-1).denominator != 1, 'weighted reserve need not be integer')
print('Exact checks:', checks, '; synthetic active tuples:', active)
```

Noch keine Numerik fuer das reale Pseudosingulett oder neue Auswahlentscheidung.
Numerische Eingaben muessen durch den separaten buchinternen Vertrag festliegen;
die hier gefundene Unterscheidung wird nicht durch passende Ausgabewerte geloest.

Prueflauf: der Python-Block wurde aus dieser Review unveraendert an
`py -3.13 -B -` uebergeben; 1773 exakte Pruefungen bestanden, Exitcode 0.
Das endliche synthetische Testgitter enthaelt dabei 90 aktive Tupel; diese
Testzaehlung ist weder eine Zahl von Heim-Zustaenden noch ein Spektrumergebnis.
Die vier allgemeinen Polynomidentitaeten sind durch den separaten exakten
Koeffizientenvergleich gesichert, nicht erst durch Stichprobentests.
book_derivation bestaetigte unabhaengig die ungewichtete II278/323-Lesung
und sah im eigenen Etappe30-Umfeld ebenfalls keine explizite Umdefinition.
Nur diese neue Review wurde geschrieben; alte Artefakte blieben unangetastet.
