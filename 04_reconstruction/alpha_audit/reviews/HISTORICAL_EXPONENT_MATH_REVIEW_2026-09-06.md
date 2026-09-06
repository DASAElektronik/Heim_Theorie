# HISTORICAL_EXPONENT_MATH_REVIEW

2026-09-06, Etappe 23. Unabhaengige reine Algebrareview durch data_audit.
Die beiden vorgegebenen Lesarten werden getrennt untersucht; keine eigene
Quellen-/Glyphenentscheidung, kein Fremdprogrammlauf, keine Massenrechnung.

## 1. Exakte Differenz und Definitionsbereich

Seien Q4>0, k in {1,2} und m=n4+Q4>=0. Die beiden reellen Exponenten sind

    A=1-2*k*m/(3*Q4),
    B=(1-2*k)*m/(3*Q4).

Mit t=m/(3*Q4)>=0 folgt unmittelbar

    A-B=1-t=(2*Q4-n4)/(3*Q4).

Der Abstand ist unabhaengig von k. Er ist positiv fuer n4<2*Q4,
null fuer n4=2*Q4 und negativ fuer n4>2*Q4. Insbesondere

    A=B genau dann, wenn n4=2*Q4,
    dann A=B=1-2*k.

Die reelle Exponentialfunktion ist injektiv. Deshalb gilt dieselbe
Gleichheitsbedingung fuer exp(A) und exp(B), und ihr Quotient ist
exp((2*Q4-n4)/(3*Q4)). Dies betrifft den isolierten Exponentialterm,
nicht automatisch eine ganze Auswahlgleichung oder ihren Loesungszustand.

Die Rechnung gilt sogar fuer beliebige reelle n4,Q4 im genannten Bereich.
Rationale Werte im Code sind nur Algebrazeugen. Falls eine Quellenregel
ganzzahlige Besetzungen fordert, muss sie zusaetzlich eingehalten werden;
die unten genannten ganzzahligen Beispiele benoetigen keine Lockerung.
Aus n4+Q4>=0 folgt n4>=-Q4, nicht n4>=0.

## 2. Diskriminierende und nichtdiskriminierende Punkte

Am vorgegebenen N0-Diagnosepunkt k=Q4=1,n4=0 erhaelt man

    A=1/3, B=-1/3, A-B=2/3, exp(A)/exp(B)=exp(2/3)>1.

Es wird damit nicht behauptet, n4=0 allein definiere allgemein einen
vollstaendigen N=0-Zustand. Die uebrigen Zustandsbedingungen dieses
ausdruecklich vorgegebenen Punktes werden hier nicht neu rekonstruiert.

Ein Vergleich bei n4=2*Q4 kann die Lesarten dagegen nicht unterscheiden:
fuer k=1 ergeben beide -1, fuer k=2 beide -3. Die Funktionen sind trotzdem
nicht identisch, denn ihre Steigungen in n4 sind verschieden:

    slope(A)=-2*k/(3*Q4), slope(B)=(1-2*k)/(3*Q4).

Fuer positives ganzzahliges Q4 koennen etwa die benachbarten Testwerte
n4=2*Q4-1 und n4=2*Q4+1 gewaehlt werden. Die Abstaende betragen
dann exakt +1/(3*Q4) und -1/(3*Q4), und beide erfuellen m>=0.
Noch einfacher diskriminiert n4=0 fuer jedes Q4>0 mit Abstand 2/3.
Der erlaubte Rand n4=-Q4 liefert A=1,B=0. Diese Auswahlen sind
zielwertfreie isolierte Algebra-Pruefpunkte, keine Behauptung, alle seien
physikalisch realisierte Teilchen oder erfuellten die weiteren Zonenregeln.

Eine Uebereinstimmung im Schnittpunkt kann daher weder eine Formelidentitaet
noch den richtigen Klammerbereich belegen. Rundung, andere Summanden oder
eine gemeinsam angepasste Besetzung duerfen bei einer spaeteren numerischen
Diskriminierung nicht still mitveraendert werden.

## 3. Ausfuehrbare unabhaengige Standardbibliothekskontrolle

```python
from fractions import Fraction as F

def pair(k,q,n):
    assert k in (1,2) and q>0 and n+q>=0
    t=(n+q)/(3*q)
    return 1-2*k*t,(1-2*k)*t

count=0
for q in (F(1),F(3,2),F(15)):
    for n in (-q,F(0),q,2*q-q/7,2*q,2*q+q/7,3*q):
        distances=[]
        for k in (1,2):
            a,b=pair(k,q,n)
            gap=(2*q-n)/(3*q)
            assert a-b==gap and (a==b)==(n==2*q)
            assert (a>b)==(n<2*q) and (a<b)==(n>2*q)
            distances.append(a-b)
            count+=1
        assert distances[0]==distances[1]
for k in (1,2):
    for q in (F(1),F(3),F(15)):
        assert pair(k,q,2*q)==(1-2*k,1-2*k)
        for shift in (-1,1):
            a,b=pair(k,q,2*q+shift)
            assert a-b==F(-shift)/(3*q)!=0
        assert pair(k,q,-q)==(1,0)
assert pair(1,F(1),F(0))==(F(1,3),F(-1,3))
for k in (1,2):
    for q in (F(1),F(3,2),F(15)):
        for multiple in (0,1,2,3,4):
            K=multiple*q
            a,b=pair(k,q,K-q)
            inverse=lambda logarithm:-3*q*logarithm/(2*k-1)
            assert inverse(b)==K
            assert inverse(a)-K==(K-3*q)/(2*k-1)
            assert 3*q*(1-a)/(2*k)==K
print('Exact exponent pairs checked:',count)
print('N0 diagnostic: A=1/3, B=-1/3; equality only at n4=2*Q4')
print('No mass calculation, authorial correction, or foreign-code execution')
```

Am 2026-09-06 ausgefuehrt: 42 allgemeine Exponentenpaare plus die
Sonder-/Nachbarpunkt- und symbolischen Inversenpruefungen bestanden. Die sieben neuen Tests in
`tests/test_historical_exponents.py` wurden mit `python -B -m unittest
discover -s tests -p 'test_historical_exponents.py' -v` erfolgreich
ausgefuehrt. `git diff --check` ohne Befund. Nur diese neue Review und
die neue Testdatei wurden erstellt; keine bestehenden Dateien geaendert.

## 4. Anschluss an die gedruckte Logarithmusrelation

Root nennt H006 p9 und H015 p6 als Quellen der Relation
K4*(2k-1)=-3*Q4*ln(W4), K4=n4+Q4. Diese Quellenzuordnung wird
hier uebernommen, nicht neu visuell geprueft. Fuer W4>0 definiert ihre
rein reelle Umkehrung I_src(W4)=-3*Q4*ln(W4)/(2k-1). Symbolisch gilt
mit ln(exp(E))=E exakt

    I_src(exp(B))-K4=0,
    I_src(exp(A))-K4=(K4-3*Q4)/(2k-1)
                  =(n4-2*Q4)/(2k-1).

B ist also als Formel kompatibel mit dieser Logrelation. A wuerde
stattdessen K4=3*Q4*(1-ln(W4))/(2k) verlangen. Der gemeinsame
Sonderpunkt K4=3*Q4 bleibt auch im Rueckwaertsvergleich ununterscheidbar.
Bei k=Q4=1,n4=0 ergibt die isolierte Quellumkehrung aus A den Wert
-1 statt K4=1 (Residuum -2), aus B korrekt 1.

Fuer K4>=0 ist B<=0 und exp(B) liegt in (0,1]. A ist nur bei
K4>=3*Q4/(2k) nichtpositiv. Insbesondere exp(A)>1 am genannten N0-Punkt
darf nicht als unveraenderter Aufruf des regulaeren W4-Logzweigs eines
stueckweisen Algorithmus ausgegeben werden. Geprueft ist die angegebene
Logrelation, nicht der Ausgang anderer W4-Faelle, Rundungen oder einer
vollstaendigen Neuauswahl von K1,...,K4. Ein zusaetzlicher exakter Test
sichert diesen Anschluss ohne numerische Exponentialauswertung.

## 5. Reichweite

Ein spaeterer rekonstruierter Quellen- oder Ausgabebeleg kann helfen,
welche Lesart an einer konkreten Stelle benutzt wurde. Das ist weder
Autorisierung einer Aenderung anderer Quellenfassungen noch ein Beweis
physikalischer Korrektheit. Der besondere Gleichheitspunkt hebt den
formalen Unterschied nicht auf. Diese Review und die neuen exakten
Tests aendern keine bestehende Auswahlregel, Eingabe oder Rechnung.
