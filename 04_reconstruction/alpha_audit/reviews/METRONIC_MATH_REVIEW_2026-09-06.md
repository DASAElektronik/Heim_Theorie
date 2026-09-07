# METRONIC_MATH_REVIEW

Datum: 2026-09-06, Etappe 20. Unabhaengige begrenzte Mathematikreview
durch data_audit. Keine neue Empirie, kein Fit, keine Massenfortpflanzung,
keine Aussage ueber das gesamte metronische Programm.

## 1. Uebernommene Definitionen und Ergebnis

Quellenlesung uebernommen aus dem konkreten Auftrag und
`METRONIC_OPERATOR_SOURCE_REVIEW_2026-09-06.md`; keine neue PDF-Suche
oder eigene Glyphenentscheidung in dieser Review:

- H003 I103 (M2): delta F(n)=F(n)-F(n-1), ein endlicher Rueckwaertsschritt.
- H003 I104 (M2a): inklusive Summe von a bis b ergibt F(b)-F(a-1).
- H003 I109 (M7): delta_e=a_scale*delta und eine ausdruecklich
  naeherungsweise Log-/Exponentialregel im Kleinvariationsregime.
- H003 I110/PDF116 (M8): exakter dividierter Differenzenquotient,
  nicht pauschal die gewoehnliche Ableitung als Kettenfaktor.
- H004 II272--274: Ersetzung relativer Variationen durch logarithmische
  Variationen; fuer X die Rekursion X_n=X_(n-1)+X_(n-2) und der
  integrierte Quotient Y=X_(z+1)/X_(z-1).

**Die Teleskopie und der X-Quotient Y sind mit M2/M2a exakt vereinbar.
Die Logarithmus-Ersetzung ist fuer einen endlichen relativen Sprung dagegen
keine Identitaet.** Ein skalares Verkleinern des Operators reduziert den
absoluten Unterschied, aber nicht automatisch den relativen Fehler.
Grosse Fibonacci-Indizes machen die relativen Spruenge nicht klein.

Diese Aussage setzt die gewoehnliche skalare Wirkung der zitierten
Rueckwaertsdifferenz auf reelle Funktionswerte voraus. Sie ist keine
automatische Widerlegung weiterer moeglicher Operator-, Grenz- oder
Potentialannahmen in Heims Werk.

## 2. Exakte Summe, Y und unterer Endpunkt

Fuer ganzzahlige a<=b, sofern F auf a-1,...,b definiert ist,

    sum_(n=a)^b delta F(n) = F(b)-F(a-1).

Die zitierte Quelle setzt fuer ihren Integrationsfall a>=1 und b>a;
diese Bedingungen sind mit dem betrachteten grossen z vereinbar. Mit
F(n)=ln X_n und positiven X_(z-1),X_z,X_(z+1) folgt genau

    delta ln X_z + delta ln X_(z+1)
      = ln X_(z+1)-ln X_(z-1)
      = ln[X_(z+1)/X_(z-1)] = ln Y.

Es werden **zwei** Rueckwaertsdifferenzen summiert, nicht eine einzige.
Hierfuer ist weder ein Kontinuumslimes noch eine kleine relative Variation
erforderlich. Erst Y->xi^2 benoetigt die separate Rekursions-/Grenzannahme.

Soll stattdessen die Differenz F(b)-F(a) als Ergebnis stehen, beginnt
die Summe bei a+1. Auf der Ebene eines Potentialwerts bedeutet ein
solches Hochsetzen des unteren Index exakt

    V_(a+1)=V_a+delta V_(a+1),

nicht allgemein V_a+delta V_a. Beispiel V_n=n^2, a=3:
V_4=16, aber V_3+delta V_3=9+5=14. Der Quellenhinweis auf eine
Addition der Variation an der unteren Grenze ist also erst bei
geklaerter Zuordnung des Variationsindex eine konkrete Instanz von M2a.
Der allgemeine Endpunktmechanismus passt; ein blosses Pluszeichen
beweist noch keine Zuordnung jedes benannten Potentiallimits.

Feste Gewichte koennen aus der Summe gezogen werden. Bei variablen
Gewichten ist dagegen exakt

    sum_(n=a)^b w_n*delta F_n
      = w_b*F_b-w_a*F_(a-1)
        -sum_(n=a)^(b-1) (w_(n+1)-w_n)*F_n.

Die nur von k abhaengigen A/B-Koeffizienten sind fuer einen festgehaltenen
k-Wert unabhaengig vom X-Summationsindex. Wird diese Bedingung nicht
eingehalten, fehlt bei einfachem Herausziehen ein Summationsterm.

## 3. Exakter logarithmischer Rest und belastbare Schranken

Seien V_n,V_(n-1)>0 und

    r_n=delta V_n/V_n=1-V_(n-1)/V_n < 1.

r darf negativ sein; aus Positivitaet folgt keine allgemeine untere
Schranke -1. Exakt gilt

    delta ln V_n = -ln(1-r_n) = r_n+E(r_n),
    E(r)=-ln(1-r)-r = r^2*integral_0^1 u/(1-r*u) du.

Damit E(r)>=0 fuer alle reellen r<1, mit Gleichheit nur fuer r=0.
Die Integralform ist auch fuer negative r korrekt. Fuer |r|<=rho<1
folgt unmittelbar

    r^2/[2*(1+rho)] <= E(r) <= r^2/[2*(1-rho)].

Insbesondere E(r)=r^2/2+O(r^3) bei r->0. Eine kleine relative Variation
ist somit eine hinreichende lokale Kontrolle der logarithmischen
Naeherung. Eine grosse Indexzahl oder ein kleiner absoluter Zahlenwert
des Potentials ist dafuer kein Ersatz.

Fuer eine endliche Summe mit reellen, moeglicherweise negativen Gewichten
w_n und einheitlichem |r_n|<=rho<1 gilt

    abs(sum w_n*(delta ln V_n-r_n))
      <= [sum abs(w_n)*r_n^2]/[2*(1-rho)].

Bei w_n>=0 liegt die Summe selbst zwischen denselben gewichteten
Quadratsummen mit Nenner 2*(1+rho) und 2*(1-rho). Gemischte
Gewichtsvorzeichen koennen Fehler aufheben; ein positives Gesamtsignal
ist dann nicht garantiert. Ueber viele Schritte muss die Summe der
Fehler kontrolliert werden, nicht nur ein einzelner Schritt.

Auch links steht bei H/G eine relative Variation. Wenn urspruenglich
r_H=sum_i A_i*r_i gilt, ist nach der Logersetzung der exakte Rest

    delta ln H - sum_i A_i*delta ln V_i
      = E(r_H)-sum_i A_i*E(r_i).

Ein isolierter nichtnulliger X-Rest beweist daher noch nicht, dass der
gesamte konkrete H/G-Rest nicht durch andere Beitraege kompensiert
wird. Dafuer waeren saemtliche relativen Potential- und H/G-Spruenge
samt Gewichten erforderlich. Es wird hier insbesondere kein Fehler
einer Teilchenmasse aus dem X-Beispiel errechnet.

## 4. M8 und M7: exakter Quotient gegen kleine Variation

Fuer eine gewoehnliche skalare Funktion f und ungleiche V_n,V_(n-1)
lautet die exakte endliche Kettenidentitaet

    delta f(V_n)
      = [(f(V_n)-f(V_(n-1)))/(V_n-V_(n-1))]*delta V_n.

Der dividierte Quotient ist nicht generell f'(V_n). Fuer den Logarithmus
ist er [1/V_n]*[-ln(1-r)/r], mit stetigem Quotientenwert 1/V_n bei r=0.
Fuer f(V)=V^2 ist er V_n+V_(n-1), nicht 2*V_n. Dies ist gerade die
Unterscheidung einer endlichen Differenz von ihrem Differentiallimes.

Nun sei delta_e=a_scale*delta als **derselbe skalare Multiplikator auf
jedem Funktionswertausdruck** interpretiert, a_scale!=0. Dann ist exakt

    delta_e ln V - delta_e V/V = a_scale*E(r),
    abs(delta_e ln V-delta_e V/V)/abs(delta_e V/V)=E(r)/abs(r)

fuer r!=0. Die relative Abweichung bleibt also unabhaengig von a_scale.
Dass delta_e V/V oder die absolute Differenz beim Skalieren gegen null
geht, begruendet nicht allein eine relative Genauigkeit der Logregel.
Entsprechend gilt fuer q=delta phi

    delta exp(phi_n)=exp(phi_n)*(1-exp(-q)),

und der Vergleich mit exp(phi_n)*q hat beim blossen Skalieren beider
Seiten ebenfalls einen von a_scale unabhaengigen relativen Fehler.
Das q ist hier ausschliesslich ein Hilfsname fuer den Exponentsprung,
nicht Heims Ladungszahl.

Anders ist ein wirklich kleiner Argumentversatz h in einer glatten
positiven Funktion V(x): Delta_h V(x)=V(x)-V(x-h). Bei beschraenkten
lokalen Ableitungen und V(x)>0 wird r_h=Delta_h V/V=O(h), und

    Delta_h ln V-Delta_h V/V
      = (h^2/2)*(V'(x)/V(x))^2+O(h^3).

Hier verbessert sich auch die relative Genauigkeit, soweit der fuehrende
Term nicht entartet. Delta_h ist aber im Allgemeinen nicht h*delta_1.
Beispiel V(x)=2^x: Delta_h V/V=1-2^(-h), waehrend h*delta_1 V/V=h/2;
Delta_h ln V=h*ln2. Ebenso waere ein Ersetzen des frueheren Werts durch
V_n-a_scale*delta V_n eine neue Zwischenschrittdefinition, nicht allein
die Wirkung des skalaren Operators a_scale*delta auf ln V.

Die Diagnose betrifft somit die Verbindung der woertlichen skalaren
M2-/M7-Lesung mit einer relativen Naeherungsbehauptung. Sie erklaert
M7 nicht pauschal fuer im gesamten Werk widerspruechlich: Eine echte
Schrittverkleinerung, abhaengige Datenfamilie oder andere praezisierte
Operatorinterpretation waere gesondert zu pruefen.

## 5. Fibonacci-Grenze: grosse Indizes genuegen nicht

Fuer die reelle Rekursion X_n=X_(n-1)+X_(n-2) mit strikt positiven
Anfangswerten und dem positiven wachsenden Anteil gilt

    phi=(1+sqrt5)/2,  X_n/X_(n-1) -> phi.

Bei positiven Anfangswerten ist der Koeffizient dieses wachsenden Zweigs
positiv; der zweite charakteristische Zweig -1/phi faellt relativ ab.
Damit

    delta X_n/X_n = X_(n-2)/X_n -> 1/phi^2=1-1/phi,
    delta ln X_n -> ln phi.

Der erste Grenzwert ist weder null noch gleich dem zweiten. Fuer das
inklusive Zweischrittintervall z..z+1 gilt

    Y_z=X_(z+1)/X_(z-1) -> phi^2,
    sum_(n=z)^(z+1) delta ln X_n = ln Y_z -> 2*ln phi,
    sum_(n=z)^(z+1) delta X_n/X_n -> 2/phi^2.

Die Differenz geht nach 2*[ln phi-1/phi^2]>0. Dies widerlegt die
Behauptung, **allein** ein wachsendes z mache die unskalierte
Logersetzung fuer diese Fibonacci-Schritte exakt oder relativ beliebig
genau. Es ist kein Ersatz fuer die noch fehlenden tatsaechlichen
Potentialverlaeufe oder eine Berechnung des gesamten H/G-Fehlers.

## 6. Ausfuehrbarer eigener Standardbibliothekscheck

Keine historischen Programme, Projekt-Auswerter, Massendaten oder neuen
physikalischen Eingaben. Fraction prueft die endliche Algebra; eine eigene
Logarithmusreihe und Decimal.ln dienen als voneinander verschieden
ausgewertete numerische Gegenchecks. Die gewaehlten rationalen V-Werte
und a_scale sind synthetische Operatorzeugen.

```python
from fractions import Fraction as F
from decimal import Decimal as D, localcontext, getcontext

# Inclusive backward telescoping, logarithmic ratio in product form,
# and exact summation by parts with nonconstant weights.
values=[F(n*n+1) for n in range(12)]
weights=[F(2*n+3,7) for n in range(12)]
for a in range(1,9):
    for b in range(a+1,11):
        delta=sum(values[n]-values[n-1] for n in range(a,b+1))
        assert delta==values[b]-values[a-1]
        assert sum(values[n]-values[n-1] for n in range(a+1,b+1))==values[b]-values[a]
        product=F(1)
        for n in range(a,b+1):
            product*=values[n]/values[n-1]
        assert product==values[b]/values[a-1]
        weighted=sum(weights[n]*(values[n]-values[n-1]) for n in range(a,b+1))
        parts=weights[b]*values[b]-weights[a]*values[a-1]
        parts-=sum((weights[n+1]-weights[n])*values[n] for n in range(a,b))
        assert weighted==parts
assert 4**2!=3**2+(3**2-2**2)
assert 4**2==3**2+(4**2-3**2)
for new,old in ((F(4),F(3)),(F(2),F(5)),(F(8,3),F(2,7))):
    assert new*new-old*old==(new+old)*(new-old)
    assert (new*new-old*old)-2*new*(new-old)==-(new-old)**2

def log_series(x):
    assert x>0
    t=(x-1)/(x+1)
    term=t
    total=t
    for j in range(1,10000):
        term*=t*t
        new=total+term/(2*j+1)
        if new==total:
            return 2*total
        total=new
    raise ArithmeticError('Log series did not converge')

def sqrt5_newton():
    x=D(2)
    for _ in range(1000):
        y=(x+5/x)/2
        if abs(y-x)<=abs(y)*D(10)**(-getcontext().prec+5):
            return y
        x=y
    raise ArithmeticError('Square-root iteration did not converge')

def numerical(precision):
    with localcontext() as ctx:
        ctx.prec=precision+20
        phi=(1+sqrt5_newton())/2
        lp=log_series(phi)
        assert abs(lp-phi.ln())<D(10)**(-precision-10)
        r=1-1/phi
        error=lp-r
        assert error>0
        rho=D('0.75')
        jumps=[D('-0.75'),D('-0.5'),D('-0.01'),D(0),D('0.01'),D('0.5'),rho]
        errs=[]
        for q in jumps:
            e=-log_series(1-q)-q
            assert e>=0
            assert q*q/(2*(1+rho))<=e<=q*q/(2*(1-rho))
            errs.append(e)
        w=[D(v) for v in (1,-2,3,-4,5,-6,7)]
        actual=sum(weight*e for weight,e in zip(w,errs))
        bound=sum(abs(weight)*q*q for weight,q in zip(w,jumps))/(2*(1-rho))
        assert abs(actual)<=bound

        # Exact unit-step values Vnew=2, Vold=1; scalar scaling cancels
        # from the relative discrepancy.  Not a small argument shift.
        log2=log_series(D(2))
        unit_jump=D(1)/2
        for scale in (D(1),D('0.01'),D('1e-30')):
            scaled_error=scale*(log2-unit_jump)
            relative=abs(scaled_error)/abs(scale*unit_jump)
            assert abs(relative-(2*log2-1))<D(10)**(-precision-10)
        h=D('0.001')
        true_jump=1-(-h*log2).exp()
        true_log=h*log2
        assert true_jump!=h/2
        assert 0<(true_log-true_jump)/true_jump<(2*log2-1)

        # Positive exact Fibonacci integers: X0=X1=1.  Index 1000 is
        # merely a convergence witness, not a physical metron scale.
        X=[1,1]
        for n in range(2,1002):
            X.append(X[-1]+X[-2])
        z=1000
        quot=F(X[z+1],X[z-1])
        exact_r=[F(X[n]-X[n-1],X[n]) for n in (z,z+1)]
        ratio=lambda v:D(v.numerator)/D(v.denominator)
        lnY=log_series(ratio(quot))
        logsum=sum(log_series(D(X[n])/D(X[n-1])) for n in (z,z+1))
        relsum=sum(ratio(v) for v in exact_r)
        tol=D(10)**(-precision-10)
        assert abs(logsum-lnY)<tol
        assert abs(lnY-2*lp)<tol
        assert abs(relsum-2*r)<tol
        fields=dict(phi=phi,relative_jump=r,log_jump=lp,single_gap=error,
                    relative_error_against_ratio=error/r,Y_limit=phi*phi,
                    two_relative_steps=2*r,ln_Y_limit=2*lp,two_step_gap=2*error,
                    fibonacci1000_relative_sum=relsum,fibonacci1000_lnY=lnY,
                    scalar_unit_step_relative_error=2*log2-1,
                    true_shift_relative_error=(true_log-true_jump)/true_jump)
        with localcontext() as rounded:
            rounded.prec=precision
            return {key:+value for key,value in fields.items()}

low,high=numerical(80),numerical(120)
with localcontext() as ctx:
    ctx.prec=140
    worst=max(abs(low[k]-high[k])/abs(high[k]) for k in high)
    assert worst<D('1e-78')
    print('Compared fields:',len(high),'80/120 max_relative_error',format(worst,'.12E'))
    for key,value in high.items():
        print(key,format(value,'.45g'))
print('Exact telescoping/product/secant, weighted bounds and scaling checks OK')
print('No physical mass propagation or historical programme execution')
```

Ausgefuehrt am 2026-09-06 mit `python -B -`: alle Fraction-Identitaeten,
Logreihen-/Decimal-Gegenchecks, Restschranken und Skalierungszeugen
erfolgreich. Die 13 ausgegebenen Felder stimmen bei 80/120 Stellen
relativ besser als 3.073e-80 ueberein (gemessen
3.072074353802e-80). `git diff --check` ohne Befund.

| Reine Fibonacci-Grenzgroesse | Hier gerundeter Wert |
|---|---:|
| Relativer Einzelschritt 1/phi^2 | 0.381966011250105151795413165634 |
| Logarithmischer Einzelschritt ln phi | 0.481211825059603447497758913424 |
| Zweischrittsumme der relativen Spruenge | 0.763932022500210303590826331269 |
| lnY im selben Grenzfall | 0.962423650119206894995517826849 |
| Zweischrittluecke | 0.198491627618996591404691495580 |

Die relative Einzelschritt-Abweichung bezogen auf 1/phi^2 ist
0.259828913794410219858429911325; dies ist eine normierte Differenz
der zwei genannten Operatorausdruecke, **keine** relative Unsicherheit
einer Heim-Masse. Die reine positive Integerfolge X0=X1=1 bei z=1000
wurde als eigener Konvergenzzeuge geprueft, nicht als Quellenwert eines
physikalischen Metronindex. Der echte kleine Shift h=0.001 im separaten
Beispiel V=2^x ergibt dagegen etwa 0.000346613628 als relativen Rest;
der skalierte Einheitsschritt hat unabhaengig von a_scale etwa
0.386294361120. Auch diese Zahlen sind ausschliesslich Operatorzeugen.

Nur diese eigene Review wurde von data_audit geschrieben. Keine
Quellen, Hauptdateien, Rechner, Eingaben, Tests oder Snapshots geaendert.

## 7. Schlussgrenze

Die belastbare positive Folgerung ist die exakte M2a-Endpunktstruktur
einschliesslich lnY. Die belastbare bedingte Warnung betrifft den Uebergang
von relativen endlichen Differenzen zu logarithmischen Differenzen ohne
eine gepruefte Kleinheits- bzw. Fehlerbedingung. Die Fibonacci-Rekursion
liefert fuer ihre eigenen unskalierten Spruenge gerade keinen solchen
Kleinheitsnachweis bei z->unendlich.

Ein weitergehender Widerspruch von M7 selbst, der gesamten H/G-Gleichung
oder der Theorie erfordert mehr: praezise Operatorwirkung, eventuelle
Verkleinerung des Argumentgitters, konkrete Potentialwerte samt relativen
Spruengen und ihre gemeinsame Fehlerbilanz. Nichts davon wird hier durch
synthetische Werte ersetzt oder aus einer passenden Masse erschlossen.

## 8. Gegenlesung der Root-Tests

`tests/test_metronic_integration.py` vollstaendig gelesen und mit
`python -B -m unittest discover -s tests -p 'test_metronic_integration.py' -v`
ausgefuehrt: alle 14 neuen Tests erfolgreich, kein Algebrafehler gefunden.
Die rationale Logarithmus-Einschliessung hat den korrekten geometrischen
Rest nach 40 atanh-Reihentermen; die Reziprok-Transformation fuer
Argumente kleiner 1 dreht die Intervallgrenzen korrekt um. Auch
Produkt-/Quotientenregel, vorzeichenabhaengige Intervallgewichtung und
die vier Potentialverhaeltnisse stimmen unter den explizit fixierten
gemeinsamen Faktoren. Letztere pruefen keine unabhaengige Begruendung
gleicher Radien oder vorgeschlagener Potentialgrenzen. Die endlichen
Fibonacci-Tests sind Konvergenzzeugen zur getrennt hergeleiteten Grenze,
keine allgemeine metronische Gueltigkeitspruefung. M8-Locator oben auf
I110/PDF116 praezisiert; ausser dieser eigenen Review nichts geaendert.
