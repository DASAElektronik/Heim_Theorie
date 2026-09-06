# Gamma / Q_N: Reichweite der Gleichungen und Anregungsbedingungen

Stand: 2026-09-06, Etappe 14 ab `e2f9cfe`. Unabhaengige lokale
Mathematikreview. Keine vollstaendige Resonanzsimulation, kein Fit und
keine Ergaenzung einer Gamma-Lebensdauerformel.

## 1. Grundlagen und Ergebnis

Vollstaendig gelesen wurden die bestehenden Entscheidungen
`NORM-1982-N-GAMMA-QN-BLOCKER`, `NORM-1982-SELECTION-QN-Q0-SCOPING`
und `NORM-1982-SELECTION-IF-GAMMA`, ferner die Transkriptionen
`HT-F-1982-SELECTION-N`, `HT-F-1982-SELECTION`,
`HT-F-1982-SELECTION-WVX` und `HT-F-1982-SELECTION-ALGO`.
Die Entscheidungen liegen unter
`04_reconstruction/formula_library/normalization/decisions/`,
die Transkriptionen unter `04_reconstruction/formula_library/formulas/`.
Zusaetzlich wurde die neue `GAMMA_QN_IGW_REVIEW_2026-09-06.md` gelesen.

Die neuen H004- und H013/H014-Lesungen wurden direkt mit dem
Hauptagenten sowie `book_derivation` und `alpha_versions` abgestimmt.
Es sind hier uebernommene Quellenlesungen, keine eigenen neuen
PDF-Glyphenpruefungen. Unklare Tokens wurden nicht algebraisch ergaenzt.

Ergebnis: Die spaeteren Q_N-Gleichungen beschreiben unbekannte
Aenderungsfunktionen und schraenken deren Form ein, bestimmen aber
nicht deren Werte bei gegebenem N>0. Die Wahl z=0 ist eine zusaetzliche
Naeherung. Die getrennten Regeln fuer reelle Auswahlgleichungen,
Zustandszahlen, stufenweise Anregung und Bandbreiten schliessen diese
Luecke nicht. Die alten Gamma/Q_N-Normalisierungen wurden nicht geaendert.

## 2. Was Q_N festlegt und was frei bleibt

### Unterschiedliche Quellenfassungen

Die uebergebenen klaren Gleichungen lauten:

| Quelle | Beziehung | Festgelegte Information |
| --- | --- | --- |
| H004, EDM II (114), Druck347/348, PDF353/354 | `Q(N)=Q+Z(N)`, `Q(0)=Q`, `Z(0)=0` | Grundwert und explizite Endpunktbedingung; Z(N) bleibt unbekannt. |
| H007 B37, Druck15/PDF6 | `Q(N)=Q(0)+2*z(N)` | z wird als unbekannte ganzzahlige Funktion bezeichnet. |
| H013/H014 (14c) | `Q(N)=Q(0)+2*z(N)` | Auch hier ist z in dieser Definitionspassage ganzzahlig und unbekannt. |

H004 nennt daneben einen unbekannten Ladungsverlauf und schreibt
`q_x(N) != q_x(0)=q_x`, keine additive q_x-Gleichung. Z(N) aus H004
wird nicht still mit 2z(N) identifiziert. Das waere nur unter einer
zusaetzlichen, belegten Gleichsetzung der jeweiligen Objekte eine
moegliche Notationsbruecke, keine neue Funktionsbestimmung.

Setze Q0=Q(0). Bei festem Q0 und vorgegebenem N liefert

```text
Q_N = Q0+2*z(N),       z(N) = (Q_N-Q0)/2
```

eine Beziehung zwischen zwei noch unbekannten Werten, nicht bereits
eine Auswahl ihres Werts. Fuer ganzzahliges z ist die Differenz Q_N-Q0
gerade; die Paritaet von Q_N relativ zu Q0 bleibt erhalten. Wenn die
Gleichung auch fuer N=0 angewendet wird, folgt z(0)=0. In H007 ist dies
eine algebraische Endpunktfolge, keine dort separat gedruckte Zusatzregel.

Selbst Positivitaet und Monotonie wuerden keine eindeutige Folge liefern.
Die eigenen mathematischen Zeugen

```text
z_a(N)=N,       Q_a(N)=Q0+2*N,
z_b(N)=2*N,     Q_b(N)=Q0+4*N
```

sind fuer N>0 positiv ganzzahlig, streng wachsend, und haben denselben
Endpunkt z(0)=0. Dennoch unterscheiden sich Q_a und Q_b bei jedem N>0.
Das ist nur ein Nachweis der Unterbestimmtheit dieser Gleichung selbst,
keine Behauptung, beide Folgen erfuellten saemtliche Heim-Zustandsregeln.

### Passagenspezifische Positivitaet

Der Quellenagent hat H014 Druck26/PDF28 gezielt nachgeprueft: Dort wird
z im Anregungskontext spaeter als positive ganze Zahl beschrieben.
Diese H014-Prosaeinschraenkung steht nicht in der entsprechenden H013-
Passage und darf nicht auf H007 B37 uebertragen werden. Eine solche
Positivitaet ist mit der Endpunktfolge z(0)=0 nur als N>0-Bedingung
vereinbar; bei wortwoertlicher Ausdehnung auf alle N bestuende eine
Bereichsspannung. Die Quellen werden hier nicht entsprechend umgeschrieben.
Keine dieser Aussagen liefert eine konkrete Funktion z(N).

### z=0 ist nicht N=0

H007 Druck20/PDF11 und H013 Druck36/PDF39 bezeichnen die Wahl z=0 als
Naeherung fuer die sonst unbekannte Q(N)-Abhaengigkeit. Es folgt dann

```text
Q_N=Q0,        aber nicht N=0.
```

Bei N>0 bleiben insbesondere Anregungsargumente N und der Selektor
`delta(N)=0` erhalten. Gleicher Q-Wert erlaubt nicht, einen angeregten
Zustand als Grundzustand auszuwerten oder dessen Selbstkopplung mit
delta(0)=1 einzusetzen. Die Quelle behauptet fuer die Naeherung einen
kleinen Massenfehler; dieser wurde hier weder als Fehlergrenze bewiesen
noch empirisch nachgerechnet. T_N bleibt in den genannten spaeteren
Quellen ebenfalls unbekannt.

## 3. Reelle Auswahlgleichung ist keine Gamma-Bestimmung

H006 (XXV), Druck8/PDF8, verwendet mit reellen Koeffizienten

```text
A_N = 1-Q(2-k)(1-kappa),
f_6(N) = A_N*[a*N/(N+2)+b*sqrt(N*(N-2))].
```

Der Index im eigenen Hilfsnamen A_N kennzeichnet hier nur seinen
Anregungsgebrauch, keine neu eingefuehrte N-Abhaengigkeit: Die
Zustandsparameter werden bei dieser lokalen Betrachtung festgehalten.
Lateinisches k und griechisches kappa sind verschieden; eine anfangs
verkuerzte Agentennachricht mit zweimal k wurde korrigiert.

Fuer N=0 ist f_6=0, fuer ganzzahliges N>=2 ist die Wurzel reell. Fuer
N=1 ist die Wurzel im ueblichen komplexen Zweig i, sodass

```text
f_6(1)=A_N*(a/3+i*b).
```

Die Quelle schliesst N=1 aus der gewoehnlichen Massenterm-Aufzaehlung
aus. Bei A_N*b=0 kann dieser spezielle Ausdruck zwar seinen
Imaginaerteil verlieren; daraus folgt keine Autorisierung, N=1
gegen die gesonderte Quellenregel doch aufzunehmen. Insbesondere
bleibt die Quellen-Ausnahme A_N=0 von dieser Verfahrensgrenze getrennt.

Fuer die aufgezaehlten N=0 und N>=2 setzt die Quelle den imaginaeren
Zusatz F(Gamma)=0; fuer den getrennten N=1-Fall gibt sie
`F(Gamma)=W*A_N*b` an. Dies liefert Werte des benannten unbekannten
Ausdrucks F(Gamma), nicht dessen Funktionsgesetz, Inverse oder eine
Gamma-Zahl. Ohne weitere Annahmen folgt aus F(Gamma)=0 NICHT Gamma=0.
Als rein mathematischer Gegenzeuge hat etwa die eigene dimensionslose
Testfunktion `g(x)=(x-1)*(x-2)` zwei verschiedene positive Nullstellen.
Diese Testfunktion wird nicht als Heims F oder als Bandbreitenmodell
ausgegeben und fuehrt keine Einheit fuer Gamma ein.

Die H006-Seite fragt die Beziehung von n_j, F(Gamma), N, vollen
Bandbreiten Gamma und Q_N ausdruecklich erst an. Der spaetere
Tuplealgorithmus benutzt Q=Q0 fuer W, a, b und grosses Phi.
Das ist eine Eingabekonvention dieses Algorithmus, KEINE Gleichung,
die die unbekannten Resonanzspins Q_N mit Q0 gleichsetzt.

H007 B39 bezeichnet ferner

```text
K_B=L_sigma(p)-sigma_N
```

als ganzzahlige Anzahl moeglicher Externfeldanregungen. Diese gezaehlte
"Bandbreite" wird nicht mit H006-Gamma identifiziert. Eine endliche
Anzahl oder eine Schranke fuer N ersetzt keine Umrechnung in eine
energetische Breite. Weder Gamma=hbar/T noch Gamma=h/T oder eine
andere Lebensdauer-Normierung wurde hinzugefuegt.

## 4. Monotonie und Reihenfolge haben unterschiedliche Reichweite

### Zwei verschiedene Anregungsfunktionen

Fuer festgehaltene reelle A_N, a und b folgt aus der H006-Form fuer
ganzzahliges N>=2 exakt

```text
f_6(N+1)-f_6(N)
 = A_N * {2*a/[(N+2)*(N+3)]
          + b*(2*N-1)/[sqrt(N^2-1)+sqrt(N*(N-2))]}.
```

Beide Nenner sind in diesem Bereich positiv. Unter A_N,a,b>=0
ist die Folge nicht fallend; bei A_N>0 und mindestens einem positiven
Koeffizienten a oder b ist sie streng wachsend. Diese Vorzeichen sind
Voraussetzungen der lokalen Aussage, keine hier fuer alle
Zustandsbelegungen nachgerechnete Eigenschaft des gesamten A_rs-Apparats.

H007 B32 hat dagegen die andere Funktion

```text
f_7(N)=a*N/(N+1)+b*N,
f_7(N+1)-f_7(N)=a/[(N+1)*(N+2)]+b.
```

Auch hier reichen a,b>=0 fuer nicht fallende Werte bei N>=0. Diese
spaetere Funktion ist bei N=1 reell; der Wurzelausschluss aus H006
darf nicht in diese Fassung importiert werden. Gleiche Buchstaben
a,b beweisen keine gleichen Koeffizienten zwischen den Fassungen.
Weder eine reelle Funktion noch eine positive Zunahme ersetzt die
uebrigen Auswahlregeln fuer einen konkreten Zustand.

### Keine automatische Massenmonotonie

Nach der direkten Lesung des Hauptagenten sagt H004 Druck349/PDF355
ausdruecklich: f(N) ist monoton, M(N) hingegen nicht; es treten
Stufenabbrueche und negative Massendifferenzen auf. Schon logisch
erzwingt ein monotoner Auswahlzielwert keine monotone daraus
gebildete Masse, solange die gesamte Abbildung nicht entsprechend
nachgewiesen ist. Diskrete Belegungen und weitere Parameter duerfen
nicht durch die Monotonie von f allein ersetzt werden.

Die Manuskriptregel (14d) verlangt fuer eine stufenweise Anregung
die beiden Bedingungen

```text
N_B>N_A,       M(N_B)>M(N_A).
```

Ein dazwischenliegendes N_gamma mit `N_A<N_gamma<N_B`, aber
`M(N_gamma)<M(N_A)`, besteht diese positive Anregung vom Ausgangspunkt
N_A nicht. Das ist eine gerichtete Bedingung fuer den beschriebenen
Vorgang, kein Satz ueber die globale Monotonie aller Massenwerte.
Als eigener algebraischer Zeuge dienen die dimensionslosen Werte
`m_toy(2)=10, m_toy(3)=9, m_toy(4)=12`: 2 nach 4 erfuellt beide
Ungleichungen, 2 nach 3 nicht. Das sind keine berechneten Teilchenmassen.

Die Ergaenzungsseite der Autorenfassung grenzt den Ausschluss selbst
auf stufenweise Anregung ein und diskutiert einen einzigen energetischen
Vorgang als anderen Zugang. Die Ungleichung allein beweist weder
Nichtexistenz des ausgelassenen Terms noch die Realisierbarkeit dieses
anderen Vorgangs. Eine solche Dynamik wird hier nicht konstruiert.

## 5. Ausfuehrbare lokale Kontrollen

Der folgende Code benutzt ausschliesslich eigene mathematische Zeugen
und illustrative Koeffizienten. Er ist kein Resonanzfilter fuer echte
Quellenzustaende und keine Ergaenzung der alten Rechner.

```python
from decimal import Decimal as D, localcontext
from fractions import Fraction as R

# Witness families only, not source-assigned resonance quantum numbers.
Q0=3
for N in (0,2,3,4,5):
    QA,QB=Q0+2*N,Q0+4*N
    assert (QA-Q0)%2==0 and (QB-Q0)%2==0
    assert (QA==QB)==(N==0)
    delta=1 if N==0 else 0
    Q_zero_approx=Q0+2*0
    assert Q_zero_approx==Q0 and (delta==1)==(N==0)
assert all(Q0+2*(N+1)>Q0+2*N for N in range(5))
assert all(Q0+4*(N+1)>Q0+4*N for N in range(5))

def own_zero_function(x):
    return (x-R(1))*(x-R(2))
assert own_zero_function(R(1))==own_zero_function(R(2))==0
assert R(1)!=R(2) and R(1)>0 and R(2)>0

def f6_real(N,A,a,b):
    if type(N) is not int or N<0 or N==1:
        raise ValueError('Local H006 enumeration: N=0 or integer N>=2')
    n=D(N)
    return A*(a*n/(n+2)+b*(n*(n-2)).sqrt())

def monotone_check(precision):
    with localcontext() as ctx:
        ctx.prec=precision+12
        A,a,b=D(1),D(2),D(3)  # illustrative, not Heim component coefficients
        values={N:f6_real(N,A,a,b) for N in (0,*range(2,11))}
        assert values[0]==0 and values[2]==A*a/2
        for N in range(2,10):
            n=D(N)
            increment=A*(2*a/((n+2)*(n+3))
                +b*(2*n-1)/((n*n-1).sqrt()+(n*(n-2)).sqrt()))
            assert values[N+1]>values[N]
            assert abs(values[N+1]-values[N]-increment)<D(10)**(-precision-7)
        assert all(f6_real(N,D(0),a,b)==0 for N in (0,2,3))
        ctx.prec=precision
        return {N:+value for N,value in values.items()}

results={p:monotone_check(p) for p in (80,120)}
with localcontext() as ctx:
    ctx.prec=140
    error=max(abs(results[80][N]-results[120][N]) for N in results[80])
print('H006 illustrative fields:',len(results[80]),'80/120 max abs:',error)
try:
    f6_real(1,D(1),D(2),D(3))
except ValueError:
    pass
else:
    raise AssertionError('H006 N=1 silently admitted')

def f7(N,a,b):
    if type(N) is not int or N<0:
        raise ValueError('Nonnegative integer N required')
    return a*R(N,N+1)+b*N

a,b=R(2),R(3)
for N in range(10):
    assert f7(N+1,a,b)-f7(N,a,b)==a/R((N+1)*(N+2))+b
    assert f7(N+1,a,b)>f7(N,a,b)
assert f7(0,a,b)==0 and f7(1,a,b)==a/2+b

# Artificial ordering values, not physical masses or a resonance simulation.
m_toy={2:R(10),3:R(9),4:R(12)}
def positive_step(A,B):
    return B>A and m_toy[B]>m_toy[A]
assert positive_step(2,4) and not positive_step(2,3)
assert 2<3<4 and m_toy[3]<m_toy[2]
assert positive_step(3,4)
print('Witness families, selectors, both increments and ordering checks passed.')
```

Der Codeblock wurde aus dieser Datei ausgefuehrt. Die zehn illustrativen
f_6-Werte stimmen bei 80/120 Stellen mit maximalem absoluten Unterschied
kleiner `4.71e-79` ueberein. Die rationalen Zeugen und Zuwachsidentitaeten
bestehen ebenfalls. Endliche Beispiele ersetzen nicht die angegebenen
allgemeinen algebraischen Beweise; der Decimal-Vergleich ist keine
Intervallzertifizierung und keine physikalische Fehlergrenze.

## 6. Abschlussgrenze

Die Quelle liefert Formen fuer Anregung und unbekannte Spinverschiebung,
Bereichs- und Reihenfolgebedingungen sowie eine deklarierte Naeherung.
Damit sind weder z(N)/Z(N) noch F(Gamma) invertierbar bestimmt. Reelle
Tupleaufzaehlung, endliche Resonanzgrenzen und ein gezaehltes K_B sind
keine fehlende Gamma-/Lebensdauer-Dynamik. Der alte Gamma/Q_N-Blocker
bleibt unangetastet. Nur diese eigene Reviewdatei wurde erstellt;
keine alten Rechner, Inputs, Snapshots, Tests oder Normalisierungen
wurden veraendert und kein Commit ausgefuehrt.
