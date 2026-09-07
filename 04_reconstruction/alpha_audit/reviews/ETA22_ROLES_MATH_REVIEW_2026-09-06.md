# Eta22 in B47, B55 und B59: getrennte algebraische Rollen

Stand: 2026-09-06, Etappe 12 ab `94c55a0`. Unabhaengige, begrenzte
Mathematikreview. Keine komplette Massen- oder Lebensdauerrechnung,
kein Fit, keine neue physikalische Modellvariante.

## 1. Quelle, direkte Sichtpruefung und Grenze

Der PDF-Skill wurde vollstaendig gelesen. Direkt und jeweils vollstaendig
visuell geprueft wurden H007 PDF-Folios 7, 8 und 9 / Druckseiten 16, 17
und 18: B47/B48, der eta22-haltige Endterm von B55 und B59. Verwendet
wurden vorhandene Vollseitenbilder; keine Quelle wurde veraendert oder
neu exportiert.

Quelle: `01_sources/heim_primary/Erweiterte_Massenformel_Nach_Heim_1989.pdf`,
IGW-Wiedergabe mit Seitenkopf Innsbruck 2003. Das ist kein hier
nachgewiesenes Originalmanuskript von 1989. Der bestehende Quellenregister-
Hash lautet
`0E2F646D784152FB008944F58E1B8E709A416B65265D2FB75D3CC44C88FF8A40`;
in dieser Teilreview wurde kein neuer Hashlauf durchgefuehrt.

Die Reichweite des vorangehenden verschachtelten Klammerausdrucks in B55
bleibt der separaten Quellenreview vorbehalten. Hier wird nur der klar
sichtbare eta22-haltige Endterm isoliert untersucht, nicht eine bereinigte
Gesamtformel fuer b2 implementiert. Die analytische Form einer affinen
Abhaengigkeit bleibt auch bei einem zusaetzlichen festen aeusseren Faktor
bestehen; ihr Koeffizient muss diesen Faktor dann jedoch enthalten.

`B` in B55 ist die quelleneigene Groesse mit Rueckverweis auf B28.
Insbesondere wird sie hier NICHT mit der Baryonenziffer `B=k-1` aus
EDM II (101b) gleichgesetzt; fuer Delta wird kein `B=1` eingesetzt.

## 2. Der isolierte B55-Term: was wirklich verschwindet

Ersetze ausschliesslich die explizite eta22-Stelle durch einen formalen
Platzhalter t. Der sichtbare Endterm lautet

```text
L22(t) = -(5/2) H^2 binom(P,3)
         * { q[1+(pi/3)(2-q)t]B - (2-q)(1-q) }
       = A22 + c22*t,

A22 = -(5/2) H^2 binom(P,3) [qB-(2-q)(1-q)],
c22 = -(5*pi/6) H^2 binom(P,3) B q(2-q).
```

Diese Zerlegung ist eine exakte gewoehnliche algebraische Identitaet.
Der sichtbare eta22-Koeffizient ist ladungsselektiv durch `q(2-q)`:

| q | Ganzer isolierter Term L22(t) | eta22-Abhaengigkeit |
| --- | --- | --- |
| 0 | `+5 H^2 binom(P,3)` | keine |
| 1 | `-(5/2) H^2 binom(P,3) B [1+(pi/3)t]` | im Allgemeinen vorhanden |
| 2 | `-5 H^2 binom(P,3) B` | keine |

Bei q=0 und q=2 verschwindet somit der eta22-Koeffizient, NICHT allgemein
der gesamte Endterm. Ebenso verschwindet der Koeffizient fuer B=0 oder
H=0. Fuer nichtnegative ganzzahlige P mit `P<3` ist `binom(P,3)=0`,
und dann verschwindet der ganze Endterm. Diese letzte Aussage wird nicht
auf beliebige reelle P unterhalb 3 ausgedehnt.

Ein allfaelliger aeusserer, von t unabhaengiger Faktor in einer geklaerten
Gesamtlesung von B55 multipliziert A22 und c22 gleichermassen und hebt
diese q-Nullstellen nicht auf. Aus ihnen folgt keinerlei allgemeine
Unabhaengigkeit der Lebensdauer von eta22: B47 enthaelt eta22 weiterhin
explizit im Nenner, und andere Abhaengigkeiten werden in dieser Diagnose
absichtlich eingefroren.

## 3. Formale Weitergabe durch B48 und B47

Die Diagnose bedeutet genau Folgendes: eta, eta11, eta12, alpha, die
Quantenzahlen, M, H, B, b1, F, phi, s, W0, beta0, delta und T_N werden
festgehalten. Ersetzt werden nur die explizit als eta22 geschriebenen
Vorkommen. Insbesondere bleibt auch das generische eta_qk in B50 fest,
selbst wenn es bei `(q,k)=(2,2)` numerisch denselben Wert besitzt.
Ebenso wird eine ueber B59 veraenderte alpha nicht in phi oder beta0
zurueckgespeist. Das ist keine koharente Variation saemtlicher
quellenseitig verbundener Groessen und kein neuer freier Heim-Parameter.

Unter dieser Festlegung hat die Gesamtformel, sofern alle uebrigen
Summanden unabhaengig von t sind, die Gestalt

```text
b2(t) = A_b + c_b*t,

y(t) = F[phi + (-1)^s(1+phi)(b1+b2(t)/W0)]
     = Y0 + Y1*t,

Y0 = F[phi + (-1)^s(1+phi)(b1+A_b/W0)],
Y1 = F*(-1)^s*(1+phi)*c_b/W0.
```

Bei der Lesart von L22 als eigenstaendigem Summanden ist `c_b=c22`.
Solange die vorgelagerte Klammerfrage nicht abschliessend geklaert ist,
wird diese Gleichsetzung nur bedingt behauptet; ein aeusserer fester
Faktor waere in c_b mitzufuehren. Die Hilfsnamen A_b, c_b, Y0 und Y1
sind keine zusaetzlichen Quellenparameter.

Schreibe

```text
d0 = 1-sqrt(eta),  d1 = 1-sqrt(eta11),  d2 = 1-sqrt(eta12),
L1 = H+n+m+p+sigma,
L2 = n+abs(m)+abs(p)*beta0,

K_tau = 192*h*H*delta / [M*c^2*d0^2*d1^2*d2^2*L1*L2].
```

Dann gibt die auf Druckseite 16 tatsaechlich links stehende Differenz
aus B47 exakt

```text
T-T_N = K_tau*y(t)/t = K_tau*(Y0/t+Y1).
```

Fuer T selbst muss im Allgemeinen T_N addiert werden. Die auf derselben
Seite angegebene Sonderbedingung `T_0=0` erlaubt bei N=0 die kuerzere
Formel `T=K_tau*(Y0/t+Y1)`. Das ist keine Aussage, dass ein N=0-Zustand
unendlich lange lebt. Auch ein festgehaltenes delta=0 wuerde aus der
Differenzgleichung nur `T=T_N` liefern, nicht generell `T=0`.

Bei festen K_tau, Y0 und Y1 folgt

```text
d(T-T_N)/dt = -K_tau*Y0/t^2.
```

Die affine y-Abhaengigkeit erzeugt also einen von t unabhaengigen Anteil
K_tau*Y1; sie darf nicht mit einem rein proportionalen `1/t`-Gesetz
verwechselt werden. Fuer c_b=0 ist Y1=0 und die explizite Abhaengigkeit
rein invers, soweit der restliche Ausdruck definiert ist. Fuer Y0=0
hebt sich die t-Abhaengigkeit vollstaendig auf. Ohne Vorzeichenwissen
ueber K_tau und Y0 folgt kein allgemeines Monotoniegesetz fuer eine
physikalische Lebensdauer.

Definitionsgrenzen: t>0, W0 ungleich 0 sowie alle Nenner von B47 und
den festgehaltenen Eingangsgroessen definiert und ungleich 0; fuer die
reelle Vorzeichenlesung von `(-1)^s` wird ganzzahliges s vorausgesetzt.
Der Punkt t=0 ist durch B47 ausgeschlossen, auch wenn eine formal
vereinfachte Diagnose im Sonderfall Y0=0 einen Grenzwert besitzt.

## 4. Dimensions- und Bedeutungsgrenzen

Der gemeinsame explizite Faktor `1/eta22` in B47 ist ein dimensionsloser
Vorfaktor der dortigen Differenzformel, ohne den ladungsselektiven
Faktor q(2-q) aus B55. "Gemeinsam" bedeutet hier die Form des Ausdrucks,
nicht gleiche Lebensdauern fuer alle Teilchen und auch keine Aussage,
dass alle Spezialfaelle seiner Nenner zulaessig sind.

Unter der ausdruecklichen Voraussetzung, dass H, y, delta, L1, L2,
alle eta-Faktoren und die Quantenzahlen dimensionslos sind, traegt
allein `h/(M*c^2)` die Zeiteinheit: Wirkung geteilt durch Energie.
Das bestaetigt die bedingte Dimension des isolierten B47-Ausdrucks,
nicht die vollstaendige Einheiten- oder physikalische Validierung aller
eingesetzten Quellengroessen. Es wurden weder h, c noch M numerisch
eingesetzt und keine ganze Lebensdauer oder Masse berechnet.

B59 hat eine dritte, algebraisch andere Rolle. Mit

```text
C0 = [(1-sqrt(eta))/(1+sqrt(eta))]^2 / (eta*eta11*eta12)
```

lautet dort die reine explizite Ersetzung `C_prime(t)=C0*(1+t)` bzw.
`K_alpha(t)=1-C0*(1+t)`. Es gibt dabei keinen q(2-q)-Selektor und keinen
inversen eta22-Faktor. Dies belegt weder zwei physikalische Kanaele noch
eine Ableitung von B59 aus B47, B55 oder einer Delta-Zustandszuordnung.
Eine Variation von alpha ueber die zugehoerige Zweiggleichung wird in
dieser Review nicht durchgefuehrt.

## 5. Unabhaengige Konstantenrechnung mit 80/120 Stellen

Die definierte Familie ist
`eta(q,k)=[1+(4+k)*q^4/pi^4]^(-1/4)`. Es werden keine Messwerte oder
Tabellen-Zielwerte eingesetzt. Die vier benoetigten Konstanten stammen
ausschliesslich aus mathematischem pi und den fest vorgegebenen Indizes.

| Groesse | Unabhaengiger Wert, gerundet |
| --- | --- |
| eta22 | 0.842423846102092834039733883054 |
| 1/eta22 | 1.187050918165498614832676546798 |
| d0^2*d1^2*d2^2 | 5.427861787780533989361728629722e-14 |
| 192/(d0^2*d1^2*d2^2) | 3.537304513394937997630447180316e15 |
| 192/(eta22*d0^2*d1^2*d2^2) | 4.198960570456423443848541330555e15 |
| pi*eta22/3 | 0.882184188707731141231295035519 |
| -5*pi*eta22/6 | -2.205460471769327853078237588798 |
| C0 | 0.000006568059917072825102479037547677 |
| C_prime | 0.000012101150213842307338471516716703 |

Der grosse B47-Vorfaktor ist rein dimensionslos. Er ist noch mit
`h/(M*c^2)` und `H*y*delta/(L1*L2)` zu multiplizieren; er ist weder
eine Zeitangabe noch eine Teilchenvorhersage. Der Wert `-5*pi*eta22/6`
ist nur der numerische Faktor des eta22-Anteils nach Ausklammern von
`H^2*binom(P,3)*B*q(2-q)` aus dem isolierten B55-Term, kein kompletter
b2-Wert.

Der folgende ausfuehrbare Standardbibliothekscode benutzt unabhaengig
Machins pi-Formel, positive Quadratwurzeln und zwoelf Arbeitsstellen
Rundungsreserve. Die Wurzeldifferenzen werden algebraisch rationalisiert
und zusaetzlich gegen die direkte Schreibweise kontrolliert.

```python
from decimal import Decimal as D, localcontext
from fractions import Fraction as F

def atan_inv(n):
    z = D(1)/n
    power, total, j = z, D(0), 1
    while True:
        new = total+power/j
        if new == total:
            return total
        total, power, j = new, -power*z*z, j+2

def calculate(precision):
    with localcontext() as ctx:
        ctx.prec = precision+12
        pi = 16*atan_inv(5)-4*atan_inv(239)
        def eta(q,k):
            return 1/(1+(4+k)*D(q)**4/pi**4).sqrt().sqrt()
        e, e11, e12, t = eta(1,0), eta(1,1), eta(1,2), eta(2,2)
        gaps = [(1-z)/(1+z.sqrt()) for z in (e,e11,e12)]
        product = gaps[0]**2*gaps[1]**2*gaps[2]**2
        G = D(192)/product
        c0 = ((1-e.sqrt())/(1+e.sqrt()))**2/(e*e11*e12)
        values = dict(pi=pi, eta=e, eta11=e11, eta12=e12, eta22=t,
            inverse_eta22=1/t, root_gap_product=product,
            G47_without_eta22=G, G47=G/t,
            B55_bracket_increment_q1=pi*t/3,
            B55_eta_term_coefficient=-5*pi*t/6,
            B59_C0=c0, B59_Cprime=(1+t)*c0)
        direct = D(192)/(t*(1-e.sqrt())**2*(1-e11.sqrt())**2
                        *(1-e12.sqrt())**2)
        assert abs(direct-values['G47'])/values['G47'] < D(10)**(-precision-5)
        ctx.prec = precision
        return {key:+value for key,value in values.items()}

results = {p:calculate(p) for p in (80,120)}
with localcontext() as ctx:
    ctx.prec = 140
    print('max abs:', max(abs(results[80][k]-results[120][k])
                          for k in results[80]))
    print('max scaled:', max(abs(results[80][k]-results[120][k])
        /max(D(1),abs(results[120][k])) for k in results[80]))
for p, row in results.items():
    print(p, row)

# Exact pi-independent coefficient identities of the isolated term.
assert F(-5,6)*0*(2-0) == 0
assert F(-5,6)*2*(2-2) == 0
assert F(-5,6)*1*(2-1) == F(-5,6)
assert F(-5,2)*(-2) == 5  # q=0: full term is not identically zero
assert F(-5,2)*2 == -5    # q=2: remaining factor multiplies B
```

Der Codeblock wurde aus dieser Datei ausgefuehrt. Bei den 13 Konstanten
ist der maximale skalierte 80/120-Unterschied, definiert als
`abs(diff)/max(1,abs(value120))`, kleiner als `1.89e-80`.
Der maximale absolute Unterschied ist wegen des grossen dimensionslosen
Vorfaktors kleiner als `3.99e-65`. Das sind numerische Konvergenzkontrollen,
keine Intervallzertifikate oder experimentellen Unsicherheiten.

## 6. Abschluss und verbleibende Abhaengigkeit

B47, der isolierte Endterm B55 und B59 besitzen drei unterschiedliche
explizite eta22-Abhaengigkeiten. Ihre Kombination ist unter den klaren
Einfrierannahmen formal berechenbar, ersetzt aber keine Quellenbegruendung
der gemeinsamen Konstante oder eine physikalische Dynamik.

Der noch zu klaerende Klammerumfang der gesamten B55-Fassung wird nicht
durch diese Teilrechnung entschieden. Keine vollstaendige b2-Funktion,
kein Lebensdauerrechner und kein alternativer Modellinput wurden erstellt.
Nur diese eigene Reviewdatei wurde geschrieben; die acht alten Rechner,
Inputs, Snapshots, Tests und Git-Eintraege wurden nicht veraendert.

## 7. Nachtrag: abweichender Korrekturterm in H014 (21a)

Die neu bezeichnete Vollseite H014, J0032, Druck26/PDF28 wurde nach
erneuter vollstaendiger Lektuere des PDF-Skills selbst visuell gelesen.
Quelle: `01_sources/heim_primary/eta22_context/J0032-Heim_Ausgewaehlte-Ergebnisse-a.pdf`.
Die Gleichung (21a) hat eta11 innerhalb des quadrierten Nenners:

```text
K_alpha,H014 = 1-(1+eta22)*[(1-sqrt(eta))/(eta11*(1+sqrt(eta)))]^2.
```

Definiere nur zum Vergleich `C_H014=1-K_alpha,H014`; H014 bezeichnet
diesen Ausdruck an der Stelle nicht selbst als C_prime. Bei gleicher
positiver eta-Familie und mit `S=[(1-sqrt(eta))/(1+sqrt(eta))]^2` gilt

```text
C_H014 = (1+eta22)*S/eta11^2,
C_H007 = (1+eta22)*S/(eta*eta11*eta12),

C_H014/C_H007 = eta*eta12/eta11.
```

Das ist nicht dieselbe Nennerstruktur. Wegen `0<eta12<eta11` und
`0<eta<1` ist der Quotient strikt kleiner als 1. Unabhaengige Werte:

```text
C_H014/C_H007 = 0.987587530689280083882445034776030410...,
C_H014       = 0.000011950945058188577948373252442059757...,
C_H014-C_H007 = -1.50205155653729390098264274643377285e-7.
```

Der Unterschied betraegt etwa -1.241246931 Prozent des kleinen
Korrekturterms C_H007, NICHT -1.241246931 Prozent von alpha. Keine
Alpha-Zweige oder neuen Alpha-Ausgaben wurden hier berechnet. Die
explizite eta22-Rolle bleibt in beiden Ausdruecken proportional zu
`1+eta22`; der Versionsunterschied betrifft den uebrigen Vorfaktor.
Der gemeinsame eta22-Faktor macht die Gesamtformeln nicht identisch.

Der folgende Nachtrag ist nach dem Python-Codeblock aus Abschnitt 5
ausfuehrbar und verwendet dessen unabhaengige Funktion `atan_inv`:

```python
def compare_versions(precision):
    with localcontext() as ctx:
        ctx.prec = precision+12
        pi = 16*atan_inv(5)-4*atan_inv(239)
        def eta(q,k):
            return 1/(1+(4+k)*D(q)**4/pi**4).sqrt().sqrt()
        e,e11,e12,t = eta(1,0),eta(1,1),eta(1,2),eta(2,2)
        S = ((1-e.sqrt())/(1+e.sqrt()))**2
        c7, c14 = (1+t)*S/(e*e11*e12), (1+t)*S/e11**2
        ratio = e*e12/e11
        assert abs(c14/c7-ratio) < D(10)**(-precision-7)
        assert 0<c14<c7 and 0<ratio<e<1
        values = dict(C_H007=c7, C_H014=c14, ratio=ratio,
                      relative_change=ratio-1, absolute_change=c14-c7)
        ctx.prec = precision
        return {key:+value for key,value in values.items()}

versions = {p:compare_versions(p) for p in (80,120)}
with localcontext() as ctx:
    ctx.prec = 140
    print('version max abs 80/120:', max(abs(versions[80][k]-versions[120][k])
                                       for k in versions[80]))
print(versions[120])
```

Beide Codebloecke wurden zusammen ausgefuehrt; der maximale absolute
80/120-Unterschied der fuenf neuen Groessen ist kleiner als `4.50e-81`.
Das ist ein lokaler Versionsvergleich, keine Auswahl einer richtigen
Fassung, keine Chronologie von H014 und H007 und keine Korrektur
bestehender Model Cards oder Rechner. Die H013-Alphaformel wurde in
diesem Nachtrag nicht beurteilt. Nur diese Review wurde ergaenzt.

## 8. Zweiter Versionsnachtrag: H013 (22a) mit zusaetzlichem Faktor

Nach erneuter vollstaendiger Lektuere des PDF-Skills wurde nun auch
H013, J0033, Druck33/PDF36 vollstaendig visuell gelesen.
Quelle: `01_sources/heim_primary/eta22_context/J0033-Heim_Ausgewaehlte-Ergebnisse-b.pdf`.
In (22a) ist rechts ausserhalb des quadrierten Wurzelquotienten der
zusaetzliche Faktor `3/(pi*eta)` erkennbar. Mit demselben S wie oben
und der eigenen Vergleichsdefinition `C_H013=1-K_alpha,H013` folgt

```text
C_H013 = [(1+eta22)/(eta*eta11*eta12)]*S*3/(pi*eta),
C_H013/C_H007 = 3/(pi*eta).
```

Diese Identitaet gilt unter denselben positiven eta-Familiendefinitionen
wie in Abschnitt 7. Die drei gelesenen Ausdruecke H013, H014 und H007
sind damit nicht wortgleich. Der explizite Faktor `1+eta22` ist ihnen
gemeinsam; ihre unterschiedlichen uebrigen Vorfaktoren bleiben getrennt.
Die Existenz dieser Unterschiede entscheidet weder ihre zeitliche
Reihenfolge noch die Absicht einer Aenderung oder die physikalisch
richtige Fassung.

```text
C_H013/C_H007 = 0.964585505926149121052721642061784146...,
C_H013 = 0.000011672594101307409648721761364544357...,
C_H013-C_H007 = -4.28556112534897689749755352158778084e-7.
```

Das entspricht etwa -3.541449407 Prozent des kleinen H007-Korrekturterms,
nicht derselben relativen Aenderung von alpha. Die auf der H013-Seite
ebenfalls gedruckten Alpha-Zweigzahlen wurden weder als Eingaben benutzt
noch hier nachgerechnet.

Dieser dritte Codeblock verwendet `calculate` aus Abschnitt 5. Seine
zusaetzlichen Arbeitsstellen werden vor dem abschliessenden Runden
beibehalten:

```python
def compare_h013(precision):
    base = calculate(precision+12)
    with localcontext() as ctx:
        ctx.prec = precision+12
        ratio = 3/(base['pi']*base['eta'])
        c7 = base['B59_Cprime']
        c13 = c7*ratio
        assert 0<ratio<1 and 0<c13<c7
        values = dict(ratio=ratio, C_H013=c13,
                      absolute_change=c13-c7, relative_change=ratio-1)
        ctx.prec = precision
        return {key:+value for key,value in values.items()}

h013 = {p:compare_h013(p) for p in (80,120)}
with localcontext() as ctx:
    ctx.prec = 140
    print('H013 max abs 80/120:', max(abs(h013[80][k]-h013[120][k])
                                     for k in h013[80]))
print(h013[120])
```

Alle drei Codebloecke wurden gemeinsam ausgefuehrt. Bei den vier neuen
Groessen liegt der maximale absolute 80/120-Unterschied unter `6.57e-82`.
Es wurden keine Alpha-Zweige, neuen Modelle oder physikalischen
Lebensdauern berechnet und keine bestehenden Rechner, Inputs oder
Snapshots geaendert. Dieser Nachtrag ergaenzt nur die eigene Review.
