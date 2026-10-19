# METRONIC_STEP_MATH_REVIEW

2026-09-06, Etappe 21; data_audit. Begrenzte skalare Mathematikreview.
Quelle/Glyphen: aus dem konkreten Root-Auftrag uebernommen, nicht neu
visuell geprueft. H003 I109 definiert delta_e=a*delta und schreibt fuer
f=exp(phi) den Ausdruck exp(phi)-exp(phi-delta_e phi). H004 II273
verwendet links delta H/H unskaliert, rechts skalierte Potentialschritte
neben dem unskalierten X-Schritt. Keine neue Massenrechnung oder Fitwahl.

## 1. Neu gegenueber Etappe 20: die konkrete nichtlineare Gleichsetzung

Setze q=delta phi=phi_n-phi_(n-1), U=exp(phi_n)>0. Dieses q ist
ein Exponentsprung, nicht Heims Ladungszahl. Unter derselben skalaren
Operatorwirkung a*delta auf allen Funktionen liefern die beiden Seiten

    L=a*U*(1-exp(-q)),   R=U*(1-exp(-a*q)).

Fuer 0<a<1 und q!=0 gilt strikt R>L. Denn h(a)=1-exp(-a*q) ist
streng konkav, h(0)=0 und h''(a)=-q^2*exp(-a*q)<0; daher h(a)>a*h(1).
Exakter Zeuge: U=4, exp(phi_(n-1))=1, a=1/2 ergibt L=3/2 und R=2.
Die Gleichsetzung eines skalierten Einheitsschritts mit dem verkleinerten
Exponentsprung ist unter diesem Praemissenpaket also keine Identitaet.
Bei a=0, a=1 oder q=0 stimmen die beiden Ausdruecke ueberein.

Fuer festes q!=0 und a->0 von oben gilt

    (R-L)/a -> U*(q-1+exp(-q)) > 0,
    (R-L)/abs(L) -> (q-1+exp(-q))/abs(1-exp(-q)) > 0.

Der absolute Unterschied verschwindet, seine relative Groesse nicht.
Bei wirklich kleinem q gilt hingegen
R-L=U*a*(1-a)*q^2/2+O(q^3). Ein kontrollierter kleiner Exponentsprung
ist eine andere Voraussetzung als allein ein kleiner Skalar a.
Dies praezisiert den Etappe-20-Befund an der konkreten M7-Zeile;
es verwirft nicht jede andere moegliche metronische Operatorinterpretation.

## 2. Neu: genaue gemischte Schrittbilanz unter expliziter Gitterannahme

NUR bedingt auf positive skalare Nachbarwerte, dasselbe Rueckwaertsgitter
und delta_e=a*delta seien r_X=delta X/X, r_i=delta V_i/V_i. Bei festem
k, a und A_i liefert die zitierte H-Gleichung

    S_H=A2*r_X+a*sum_i A_i*r_i,   i in {1,3},
    H_n/H_(n-1)=1/(1-S_H).

Diese positive Rekurrenz ist bei H_(n-1)>0 genau fuer S_H<1 definiert.
Fuer G gilt die entsprechende B-Gleichung mit ihren Potentialanteilen.
Mit E(r)=-ln(1-r)-r und allen beteiligten r<1 ist der Gesamtlogrest exakt

    delta lnH-A2*delta lnX-a*sum_i A_i*delta lnV_i
      = E(S_H)-A2*E(r_X)-a*sum_i A_i*E(r_i).

Die linke Skalierung wird also nicht still mit den rechten vereinheitlicht.
Die Gleichung enthaelt den H-Rest UND alle gewichteten Einzelreste;
Aufhebung ist moeglich. Ohne tatsächliche Potentialpfade und gesicherte
Gitterzuordnung folgt hieraus weder ein alpha3- noch ein Massenfehler.

## 3. Synthetische X-only-Zeugen und Endpunktgrenze

Halte saemtliche Potentiale konstant. Dann bleiben nur S=c*r_X und
die positive Rekurrenz; a wird in diesem Test inaktiv. Fuer den positiven
Fibonacci-Grenzschritt r=1/xi^2, xi=(1+sqrt(5))/2, ist der Logrest

    D(c)=-ln(1-c*r)-c*ln(xi),   c*r<1.

Strenge Konvexitaet von -ln(1-c*r) ergibt D<0 fuer 0<c<1,
D=0 fuer c=1 und D>0 fuer 1<c<1/r. Die hier relevanten Werte sind:

| Eigener Grenzzeuge | c | 1-c*r | D(c), gerundet |
|---|---:|---:|---:|
| G, k=1: B2=k/2 | 0.5 | 0.809016994375 | -0.0286705570294599 |
| H, k=1: A2=(2k+1)/2 | 1.5 | 0.427050983125 | 0.129034136872697 |
| H, k=2 | 2.5 | 0.0450849718747 | 1.89617674320895 |
| G, k=2 | 1 | 0.618033988750 | 0 exakt |

Fuer k=2 liegt der H-Koeffizient unter 1/r=xi^2=2.61803398875... .
Die grosse H-Grenzantwort ist eine Eigenschaft dieses synthetischen
X-only-Modells, kein rekonstruierter Heim-Pfad und keine Instabilitaets-
oder Fehlerbehauptung fuer reale Teilchen. Nichtkonstante Potentiale
koennen sowohl S als auch den gemeinsamen Logrest aendern.

Ein zweiter Zeuge haelt X konstant und nur einen Potentialanteil aktiv,
a=1/2,A1=1,H0=1. Beide positiven Pfade V=(1,2,4) und V=(1,3,4)
haben dieselben Endpunkte. Die exakte Rekurrenz liefert jedoch
H2=16/9 bzw.12/7; der reine Log-Endpunktausdruck waere jeweils sqrt(4)=2.
Endpunkte allein ersetzen daher nicht die Bilanz der relativen Schritte.
Auch diese Pfade sind frei gewaehlte Algebrazeugen, keine Quellenwerte.

## 4. Ein ausfuehrbarer Standardbibliotheksblock

```python
from fractions import Fraction as F
from decimal import Decimal as D, localcontext

left=F(1,2)*(4-1)
right=F(4)-F(2)  # exp((ln4)/2)=2
assert (left,right)==(F(3,2),F(2)) and right>left
def path(v):
    h=F(1)
    for old,new in zip(v,v[1:]):
        s=F(1,2)*(1-F(old,new))
        assert s<1
        h/=1-s
    return h
assert path((1,2,4))==F(16,9)
assert path((1,3,4))==F(12,7)
assert path((1,2,4))!=path((1,3,4))

def run(precision):
    with localcontext() as ctx:
        ctx.prec=precision+20
        xi=(1+D(5).sqrt())/2
        r=1-1/xi
        q=D(4).ln()
        out={'r':r,'critical_c':1/r}
        for c in (D('0.5'),D(1),D('1.5'),D('2.5')):
            s=c*r
            assert 0<s<1
            gap=-(1-s).ln()-c*xi.ln()
            e=lambda v:-(1-v).ln()-v
            assert abs(gap-(e(s)-c*e(r)))<D(10)**(-precision-10)
            if c!=1:
                assert (gap>0)==(c>1)
            else:
                assert abs(gap)<D(10)**(-precision-10)
            out[f'margin_{c}']=1-s
            if c!=1: out[f'gap_{c}']=gap
        for jump in (q,-q):
            for a in (D('0.5'),D('0.01'),D('1e-20')):
                l=a*4*(1-(-jump).exp())
                rr=4*(1-(-a*jump).exp())
                assert rr>l
        a=D('1e-30')
        l=a*4*(1-(-q).exp())
        rr=4*(1-(-a*q).exp())
        limit=(q-1+(-q).exp())/abs(1-(-q).exp())
        assert abs((rr-l)/abs(l)-limit)<D('1e-28')
        out['small_a_relative_limit']=limit
        with localcontext() as rounded:
            rounded.prec=precision
            return {key:+value for key,value in out.items()}
lo,hi=run(80),run(120)
with localcontext() as ctx:
    ctx.prec=140
    worst=max(abs(lo[k]-hi[k])/abs(hi[k]) for k in hi)
    assert worst<D('1e-78')
    print('fields',len(hi),'80/120 max_relative_error',format(worst,'.12E'))
    for key,value in hi.items(): print(key,format(value,'.40g'))
print('Exact step/path witnesses OK; no historical or mass code executed')
```

Am 2026-09-06 erfolgreich ausgefuehrt: exakte Fraction-Zeugen und zehn
Felder bei 80/120 Stellen; maximale relative Abweichung 2.550612081569e-80.
`git diff --check` ohne Befund. Nur diese eigene Review wurde geschrieben.

Die algebraischen Zeichen- und Grenzaussagen folgen aus den oben
angegebenen Voraussetzungen; numerische Tests allein beweisen keinen
allgemeinen Operator- oder Quellenbefund. Die Folgerung bleibt lokal:
Woertliches a*delta und verkleinerter nichtlinearer Argumentsprung sind
verschieden, und die gemischte Gleichung braucht ihre ganze Schrittbilanz.

Nachtrag: `tests/test_metronic_step.py` vollstaendig gegengelesen und mit
`python -B -m unittest discover -s tests -p 'test_metronic_step.py' -v`
ausgefuehrt: alle zehn Tests erfolgreich, kein Algebrafehler gefunden.
Der gemischte k=2-Test ergibt mit synthetischem r_X=2/5 und den dort
festgelegten Potentialen S_H=1.01075>1: nur fuer diesen kuenstlichen
Schritt gibt es keine positive H-Rekurrenz. Er widerlegt keinen echten
Heim-Pfad; der getrennte Fibonacci-X-only-Grenzzeuge hat dagegen S_H<1.
Die Intervallgewichtung und exakte Ausloeschung der linearen Terme im
gemischten Resttest sind korrekt. Keine anderen Dateien geaendert.
