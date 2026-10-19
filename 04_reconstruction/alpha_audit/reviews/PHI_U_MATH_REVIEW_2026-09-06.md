# Phi/U: explizite Abhaengigkeiten und begrenzte Vorzeichendiagnose

Stand: 2026-09-06, Etappe 13 ab `bf96741`. Unabhaengige Mathematikreview.
Keine komplette Massen- oder Lebensdauerrechnung, keine Auswahl eines
Vorzeichens durch Datenanpassung und keine Aenderung alter Normalisierungen.

## 1. Befund und gelesene Grundlagen

Die normalisierte explizite B49-Rechtsseite enthaelt weder T noch M
als Eingabe. Unter den quellenseitig angegebenen vorgelagerten
Parameterdefinitionen ist somit keine algebraische Rueckkopplung von
gemessener Lebensdauer oder Masse zur Bestimmung von phi erforderlich.
Das bedeutet NICHT, dass die eingesetzten Koeffizienten historisch
unabhaengig von Messdaten gewonnen wurden. Explizite Parameterfunktion,
Herleitungsanspruch und empirische Kalibrierung sind verschiedene Fragen.

Vollstaendig gelesen wurden:

- `NORM-1989-FPHI-B49-SCOPE.md`,
- `NORM-1989-FPHI-BUW-PRODUCT-SCOPE.md`,
- `NORM-1989-FPHI-B50-DOUBLE-MINUS-BLOCKER.md`,
- die Transkriptionen `HT-F-1989-FPHI.md` und `HT-F-1989-MASS.md`,
- der Bericht `06_docs/ETA22_ROLES_2026-09-06.md`.

Die drei Normalisierungsdateien liegen unter
`04_reconstruction/formula_library/normalization/decisions/`, die beiden
Transkriptionen unter `04_reconstruction/formula_library/formulas/`.
Ihre dokumentierte Lesung wird hier uebernommen; in dieser Etappe wurden
von mir keine neuen PDF-Glyphen eigenstaendig geprueft.

Die parallelen Quellenagenten bestaetigen als direkte Lesung zusaetzlich:
H007 B22-B31 definiert W0 ueber vorgelagerte Zustandsquantenzahlen und
Konstanten ohne sichtbares M, T oder kleines phi als Eingabe. B28 gibt
`B=3H/[k^2(2k-1)]`. Fuer H013 gilt der entsprechende lokale Aufbau ueber
(11b)-(13); B ist in (13b) durch dieselbe Relation bestimmt. Diese
Feststellung betrifft die sichtbare Abhaengigkeitskette, nicht eine
unabhaengige physikalische Herleitung ihrer Parameter.
B32-B36 sind davon getrennte Anregerbeziehungen, nicht weitere
Definitionsstufen von W0.

## 2. Eindeutig abgegrenzte B49-Struktur

Mit `r4=2^(1/4)` und den eigenen Hilfsnamen a_phi, b_phi, c_phi lautet
die bestehende normalisierte H007-Struktur:

```text
a_phi = N4*p^2/(1+p^2) * (sigma+Q_sigma)/sqrt(1+sigma^2),

b_phi = P*(P-2)^2
        * [1+kappa*(1-q)/(2*alpha*vartheta)]
        * (pi/e_base)^2 * sqrt(eta12) * (Q_m-Q_n),

c_phi = (P+1)*binom(Q,3)/alpha,

phi = a_phi*(r4-4*B*U/W0) + b_phi - c_phi.
```

`e_base` bezeichnet die in der Normalisierung verwendete Exponentialbasis,
nicht eine neu eingefuehrte elektrische Ladung. Die inverse Potenz im
kompakten BUW-Ausdruck gehoert nur zu W0. B ist die B28-Hilfsgroesse,
nicht die Baryonenziffer `k-1`. Grosses Phi aus der Massenformel bleibt
von kleinem phi getrennt.

Bei festgehaltenen anderen Groessen ist phi affin in U:

```text
phi = [a_phi*r4+b_phi-c_phi] - (4*a_phi*B/W0)*U,
d(phi)/dU = -4*a_phi*B/W0.
```

Die rechte Seite ist eine Parameterfunktion. Der Satz, eine Analyse
der Existenzzeiten liefere phi, ist fuer sich allein kein Nachweis,
dass zu jeder numerischen Auswertung gemessenes T eingesetzt werden
muesse. Umgekehrt beweist das Fehlen von T als Formelargument nicht
die Datenunabhaengigkeit ihrer Entstehung oder Koeffizientenwahl.

## 3. B50: Vorzeichenauswirkung ohne Quellenreparatur

Der alte H007-Blocker bleibt bestehen. Die zwei nur diagnostisch
bezeichneten mathematischen Varianten lassen sich schreiben als

```text
U_plus  = U_base + D_U,
U_minus = U_base - D_U,

D_U = [2^Z/eta_qk^2] * (k-1)
      * [4*pi/r4] * (P-Q)*(1-q),

Delta_U = U_plus-U_minus = 2*D_U,
Delta_phi = phi(U_plus)-phi(U_minus)
          = -(4*a_phi*B/W0)*Delta_U.
```

U_base umfasst die gemeinsamen Summanden, nicht eine neue Quellenfunktion.
Insbesondere ist `2^Z` bereits Bestandteil der alten Transkription;
dieser Faktor wird hier weder neu entdeckt noch nachtraeglich eingefuegt.
Die Zeichenwahl wird nicht durch eine Programmierspracheninterpretation
des gedruckten Doppelminus oder durch bessere Rechentreffer entschieden.

Die Varianten unterscheiden sich nicht, wenn `k=1`, `P=Q` oder `q=1`.
Auch wenn Delta_U nicht null ist, verschwindet seine lokale Weitergabe
an phi bei a_phi=0 oder B=0. Beispielsweise wird a_phi fuer p=0 null,
oder fuer `sigma=-Q_sigma`, sofern ein betrachteter Zustand diesen Wert
zulaesst. Das sind bedingte algebraische Nullstellen, keine neue Liste
zulaessiger Teilchenzustande.

Diese Nullstellen duerfen nicht mit dem Verschwinden von ganz phi
verwechselt werden: b_phi und c_phi koennen weiter beitragen. Ebenso
setzt q=1 in b_phi lediglich den kappa-Zusatz auf null und laesst dessen
Klammerwert 1 stehen. Fuer ganzzahliges P=0 oder P=2 bzw. `Q_m=Q_n`
verschwindet dagegen der gesamte b_phi-Term. Bei nichtnegativen ganzen
Q<3 verschwindet der Binomialfaktor des c_phi-Terms.

Die abschliessend uebergebene Quellenlesung findet auch in H013
(21b1), Druck30/PDF33, ZWEI Minusglyphen: eine am Zeilenende hinter
P+2Q und eine vor dem 4*pi-Term der Folgezeile. Eine zwischenzeitliche
Meldung eines eindeutigen einfachen Minus wurde vom Quellenagenten nach
Nachpruefung korrigiert. Ob hier ein doppeltes mathematisches Minus oder
ein typographisch wiederholtes Fortsetzungszeichen gemeint ist, bleibt
ohne Editionsbeleg offen. Keine der beiden diagnostischen U-Varianten
wird deshalb als bestaetigte H013- oder H007-Quellenfassung ausgegeben.
Dies ist eine uebernommene Lesung, keine eigene neue Glyphenpruefung.

## 4. Bereiche, Nenner und Selektoren

Fuer die gewoehnlich-reelle lokale Algebra muessen W0, alpha, vartheta
und eta_qk ungleich null sein. Die Wurzeln verlangen die in der
Konstantenfamilie verwendeten positiven eta-Werte. Fuer reelle p und
sigma sind `1+p^2` und `sqrt(1+sigma^2)` strikt positiv; dort entsteht
kein reeller Pol.

B50 hat zusaetzlich den Nenner `3-2q`. Bei ganzzahligem q ist dieser
ungerade und niemals null. Bei einer diagnostischen Erweiterung auf
reelle q waere q=3/2 auszuschliessen; eine solche Erweiterung wird nicht
als Quellenzustandsraum benutzt. Fuer positives ganzzahliges k sind
die Nenner k und `k^2(2k-1)` in N4 und B positiv. Insbesondere gilt

```text
N4 = (4/k)*[1+q*(k-1)] > 0     fuer k>=1 ganzzahlig und q>=0.
```

W0 wird nicht allein wegen seiner Rolle als Nenner fuer alle moeglichen
Parameterwerte als positiv oder von null verschieden vorausgesagt.
Seine jeweilige Zulaessigkeit muss vor einem kompletten Rechenfall
nachgewiesen werden. Ein verschwindender Vorfaktor legitimiert keine
Auswertung von `0*(1/0)`; auch bei einer Selector-Nullstelle bleibt die
Domaene der gedruckten Ausgangsformel zu beachten. Eine stetige oder
stueckweise Erweiterung waere eine zusaetzliche explizite Entscheidung.

## 5. Gemeinsamer Eingabepfad statt erzwungenem Kreis

Fuer die untersuchten expliziten Beziehungen gilt zunaechst das
folgende gerichtete Schema; es ist kein vollstaendiger Massenalgorithmus:

```text
Zustandsquantenzahlen, Konstanten, festgelegte Koeffizienten
             -> B, U, W0, N4 und weitere Hilfsgroessen
             -> phi -> F_mass -> M -> T
                    -> y ------------> T
```

Die Abhaengigkeit von M im Nenner der Lebensdauerformel fuehrt nicht
automatisch zu M als Eingabe von phi. Beide Ausgabepfade koennen
denselben zuvor bestimmten phi-Wert benutzen, ohne einen Kreis zu
bilden. Die Auswahlgrenze M0 aus B15 und ihre Rolle bei der Bestimmung
zulaessiger Zustaende sind davon getrennt und hier nicht vollstaendig
rekonstruiert. Aus dem lokalen Schema folgt keine Kreisfreiheit des
gesamten Theorie- oder Kalibrierungsverfahrens.

Der direkte Additionsbeitrag in H007 ist nach B5/B7

```text
F_mass = F_rest + phi*delta(N),
delta(0)=1,  delta(N!=0)=0.
```

Mit der H007-Massenformel B3 folgt bei festgehaltenem Rest

```text
M = M_rest + mu*alpha_plus*phi*delta(N),
dM/dphi = mu*alpha_plus*delta(N).
```

Bei N=0 wird daraus mu*alpha_plus. Bei N>0 verschwindet dieser direkte
additive Beitrag, nicht notwendigerweise jede indirekte Abhaengigkeit
der gesamten Resonanzrechnung. Insbesondere ist dies kein Nachweis
einer vollstaendigen, geschlossenen N>0-Lebensdauerformel.

Die Versionsunterschiede bleiben erhalten: Laut direkter Quellenlesung
des Hauptagenten steht in H013 (4)
`M=mu*[(G+S+F+Phi)*alpha_plus+4q*alpha_minus]`, waehrend die alte
H007-Transkription B3 alpha_plus um die ganze Klammer einschliesslich
`4q*alpha_minus` setzt. Auch der erste n-Beitrag in F unterscheidet
sich durch einen N1-Faktor. Das wird hier nicht zu einer gemeinsamen
Gesamtformel normalisiert. Der bei N=0 isolierte Koeffizient von phi
in M ist dennoch in beiden Fassungen mu*alpha_plus.

H013 definiert in (5e) phi bereits als `N4*K*delta(N)` und gibt in
(21b) dessen fuer den Grundzustandskontext expliziten Ausdruck an,
mit N4 bereits im ersten Summanden. Es darf deshalb NICHT nochmals
der gesamte (21b)-Ausdruck mit N4 multipliziert werden. Auch wird kein
zusaetzlicher delta-Faktor still in diese gedruckte Formel eingefuegt;
die fuer N>0 benoetigte Bedeutung muss versions- und kontextgebunden
aus den entsprechenden Aussagen bestimmt werden.

Die eigenen eindeutigen Namen lauten `F_mass` fuer H007 B5 und
`F_time` fuer den Faktor in H007 B52. In H013 entsprechen dem die
verschiedenen Ausdruecke (5c) und (21c). Die zwei F werden NICHT
gleichgesetzt: F_time besitzt nicht allein wegen des gleichen
Quellenbuchstabens den phi-Anteil von F_mass. Eine Rueckkopplung,
die F_mass anstelle von F_time in B48 einsetzt, waere kuenstlich.
Sind J=`(-1)^s*(b1+b2/W0)` und die uebrigen Faktoren fest, ergibt B48

```text
y = F_time * [J+(1+J)*phi].
```

Die gemeinsame Verwendung von phi in y und M erklaert bereits, warum
T nicht allgemein einfach proportional zu phi sein muss: y ist ein
Zaehlereingang, M ein Nennereingang. Eine konkrete Zeit wird daraus in
dieser Review nicht berechnet.

Fuer N=0 und feste uebrige Eingangsgroessen kann die direkte
phi-Abhaengigkeit von M formal mitgefuehrt werden. Mit
`m_phi=mu*alpha_plus` und K_time als dem phi-unabhaengigen B47-Faktor
ohne M, aber einschliesslich F_time, ergibt sich

```text
T(phi) = K_time * [J+(1+J)*phi]/[M_rest+m_phi*phi],
dT/dphi = K_time * [(1+J)*M_rest-m_phi*J]
          /[M_rest+m_phi*phi]^2.
```

Der Nenner muss ungleich null sein. Ohne Vorzeichenkenntnis ueber die
angegebenen festen Faktoren folgt kein allgemeines Monotoniegesetz.
Dies ist eine andere lokale Diagnose als die reine Vorkommensvariation
aus Etappe 12, die M festhielt: Hier wird ausschliesslich sein direkter
N=0-phi-Beitrag mitgefuehrt. Weder wird ein realer Massenwert eingesetzt
noch eine vollstaendige Parametervariation des Modells behauptet.

Eine Rueckkopplung oder inverse Aufgabe entstuende beispielsweise,
wenn man phi aus vorgegebenem beobachtetem T zusammen mit einer
M(phi)-Beziehung rueckbestimmte oder wenn Zustandslabels/Koeffizienten
an beobachtete M/T angepasst wuerden. Das sind zusaetzliche Arbeits-
oder Kalibrierungsschritte, keine durch B49 allein erzwungenen
Rechenpfeile. Die Quellen berichten empirisch angepasste Koeffizienten
in phi/U; welcher Messdatensatz welche Zahl festlegte und ob eine
vollstaendig unabhaengige Vorhersage verbleibt, ist hier nicht
rekonstruiert. Daraus wird kein Fit von eta22 oder der Alpha-Korrektur
abgeleitet.

## 6. Ausfuehrbare exakte Algebra-Kontrolle

Der folgende Standardbibliothekscode prueft 96 Kombinationen des
Vorzeichenselektors und die affine Weitergabe mit exakten rationalen
Zahlen. Die rationalen Platzhalter fuer bereits zusammengefasste
Koeffizienten sind KEINE Heim-Zustandsbelegung und keine numerische
Auswertung der blockierten B49/B50-Gesamtformeln. Insbesondere wird
kein Wert fuer pi, eta, eine physikalische Masse oder Lebensdauer
eingesetzt. Der Code ist eine eigene Identitaetsdiagnose, keine neue
Normalisierung oder Regression des vorhandenen Massenapparats.

```python
from fractions import Fraction as R
from math import comb

def n4(k,q):
    if type(k) is not int or k<1 or q<0:
        raise ValueError('Local test domain: k positive integer, q nonnegative')
    return R(4,k)*(1+q*(k-1))

def phi_grouped(U,constant,A,B,W0):
    if W0==0:
        raise ValueError('Original W0 denominator must remain nonzero')
    return constant-4*A*B*U/W0

# Artificial rational placeholders for grouped algebraic coefficients only.
base,scale = R(3,5),R(5,7)
constant,A,B,W0 = R(11,13),R(2,3),R(3,5),R(7,4)
cases=0
for k in (1,2):
    for q in (0,1,2,3):
        for P in (1,2,3):
            for Q in (0,1,2,3):
                selector=(k-1)*(P-Q)*(1-q)
                Uplus,Uminus=base+scale*selector,base-scale*selector
                dU=Uplus-Uminus
                dphi=(phi_grouped(Uplus,constant,A,B,W0)
                       -phi_grouped(Uminus,constant,A,B,W0))
                assert dU==2*scale*selector
                assert dphi==-4*A*B*dU/W0
                assert (dU==0)==(selector==0)
                assert n4(k,q)>0
                assert 3-2*q!=0
                cases+=1
assert n4(2,2)*R(0)**2/(1+R(0)**2)==0
assert 2*(2-2)**2==0
assert all((comb(Q,3) if Q>=3 else 0)==0 for Q in (0,1,2))
assert 3-2*R(3,2)==0
try:
    phi_grouped(R(0),constant,R(0),B,R(0))
except ValueError:
    pass
else:
    raise AssertionError('Zero numerator must not authorize undefined W0')
print('exact grouped-coefficient cases:',cases)
print('artificial example delta U:',2*scale*(-2))
print('artificial example delta phi:',-4*A*B*(2*scale*(-2))/W0)
```

Der Codeblock wurde aus dieser Datei ausgefuehrt und besteht. Ausgabe:
96 Faelle, kuenstliches Delta_U=-20/7 und zugehoeriges
Delta_phi=128/49. Diese beiden rationalen Beispiele sind keine
Quellenzahlen und keine behaupteten Teilchenwerte. Die allgemeinen
Identitaeten folgen aus der oben angegebenen exakten Algebra; die
endliche Beispielsammlung ersetzt diesen Beweis nicht.

## 7. Abschlussgrenze

Positiv geklaert sind die explizite Parameterabhaengigkeit von phi,
sein direkter Grundzustandsbeitrag zur Masse und der gemeinsame
Eingabepfad zur Lebensdauer. Nicht geklaert sind die vollstaendige
physikalische Herleitung, historische Kalibrierung, eine komplette
Zustandsauswahl oder eine kanonische Aufloesung des H007-B50-Zeichens.
Nur diese eigene Reviewdatei wurde geschrieben. Alte Rechner,
Snapshots, Inputs, Tests und Normalisierungen wurden nicht geaendert;
es wurde kein Commit erstellt.

## 8. Nachtrag: vorzeichenblinder Delta-Kontexttest und Quotientenidentitaet

Das bereits quellenseitig zugeordnete Kontexttupel
`k=2, P=3, Q=3, kappa=0, q=2` ist keine vollstaendige Festlegung
aller Zonenquantenzahlen oder eines physikalisch validierten Zustands.
Es reicht aber fuer diesen einzelnen U-Ausdruck: Wegen P=Q ist der
umstrittene Term null, und wegen kappa=0 faellt auch der B-haltige
Summand weg. Bei q=2 ist sein Nenner `3-2q=-1` regulaer. Somit gilt

```text
Z = k+P+Q+kappa = 8,
U_plus = U_minus
       = 2^8 * [3^2+0+3*(1-2)+0+(2-1)*(3+2*3)]/eta22^2
       = 3840/eta22^2
       = 3840*sqrt(1+96/pi^4).
```

Der unabhaengige Wert lautet

```text
U_Kontext = 5410.905148099404631131279413983334368736....
```

Dieser Test unterscheidet die zwei Vorzeichen NICHT. Ein Treffer an
diesem Tupel koennte deshalb kein Vorzeichenproblem von B50 aufloesen.
Ohne die uebrigen Hilfs- und Zonenparameter, insbesondere W0, wurde
daraus keine phi-, Massen- oder Lebensdauerzahl fuer Delta berechnet.

```python
from decimal import Decimal as D, localcontext

def atan_inv(n):
    z=D(1)/n
    power,total,j=z,D(0),1
    while True:
        new=total+power/j
        if new==total:
            return total
        total,power,j=new,-power*z*z,j+2

def delta_u(precision):
    with localcontext() as ctx:
        ctx.prec=precision+12
        pi=16*atan_inv(5)-4*atan_inv(239)
        eta22=1/(1+D(96)/pi**4).sqrt().sqrt()
        value=3840/eta22**2
        alternate=3840*(1+D(96)/pi**4).sqrt()
        assert abs(value-alternate)<D(10)**(-precision-5)
        ctx.prec=precision
        return {'eta22':+eta22,'U_context':+value}

rows={p:delta_u(p) for p in (80,120)}
with localcontext() as ctx:
    ctx.prec=140
    print('Delta-U max abs 80/120:',max(abs(rows[80][k]-rows[120][k])
                                      for k in rows[80]))
print(rows[120])
```

Der maximale absolute 80/120-Unterschied der beiden Groessen betraegt
weniger als `4.77e-77`. Die Zahl stammt nur aus mathematischem pi und
dem vorgegebenen Tupel; kein Messwert wurde importiert. Dies ist keine
Intervallzertifizierung.

Eine unabhaengige exakte Kontrolle der Quotientenstruktur aus Abschnitt 5
ist moeglich, ohne eine Masse oder Zeit numerisch auszuweisen. Fuer
`f(x)=K*[J+(1+J)*x]/[A+m*x]` gilt bei beiden Nennern ungleich null:

```text
f(v)-f(u) = K*[(1+J)*A-m*J]*(v-u)/[(A+m*u)*(A+m*v)].
```

Der folgende dritte Codeblock verwendet ausschliesslich kuenstliche
rationale Koeffizienten; A ist hier ein formaler Koeffizient, KEIN
eingesetzter physikalischer M_rest-Wert. R stammt aus Abschnitt 6.

```python
quotient_cases=0
for K,J,A,m in ((R(2,3),R(1,4),R(5,2),R(3,7)),
                (R(1),R(-2),R(4),R(1)),
                (R(1),R(1),R(1),R(2))):
    def f(x):
        if A+m*x==0:
            raise ValueError('Undefined quotient')
        return K*(J+(1+J)*x)/(A+m*x)
    for u,v in ((R(0),R(1)),(R(1,3),R(4,3))):
        expected=K*((1+J)*A-m*J)*(v-u)/((A+m*u)*(A+m*v))
        assert f(v)-f(u)==expected
        quotient_cases+=1
print('exact artificial quotient cases:',quotient_cases)
```

Alle drei Codebloecke wurden gemeinsam aus dieser Review ausgefuehrt:
96 Selektor-/Weitergabefaelle, der 80/120-Konstantenvergleich und sechs
exakte Quotientendifferenzen bestehen. Es wurde weiterhin nur diese
Reviewdatei geaendert, kein alter Rechner oder kanonischer Input.
