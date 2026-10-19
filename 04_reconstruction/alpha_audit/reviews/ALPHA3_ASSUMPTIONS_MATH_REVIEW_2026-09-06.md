# ALPHA3_ASSUMPTIONS_MATH_REVIEW

Datum: 2026-09-06. Etappe 19 ab df6934c. Unabhaengige, begrenzte
Bestimmtheitspruefung durch data_audit; keine moderne Empirie, kein Fit,
keine Auswahl von Eigenwerten oder Teilchenmassen.

## 1. Ergebnis und uebernommene Quellenlesung

**Ein festgelegtes Koeffiziententupel bestimmt die positiven Funktionen
H und G eindeutig. Der allgemeine Logansatz allein bestimmt dieses
Tupel nicht.** Positivitaet, Dimensionslosigkeit, ganzzahliges k und
blosse endliche bzw. verschwindende Grenzwerte liefern keine eindeutige
Auswahl der im Buch eingesetzten Exponenten. Ein einzelner synthetischer
Funktionsanker beseitigt diese Unterbestimmtheit ebenfalls nicht.

Gelesen wurden `ALPHA3_BOOK_ORIGIN_REVIEW_2026-09-06.md` und
`06_docs/ALPHA3_ORIGIN_2026-09-06.md`. Die folgenden Logformen und
die Quellenbeschreibung ihrer Koeffizientenwahl werden daraus sowie
aus dem konkreten Auftrag uebernommen: H004 Druck274--275, abschliessend
(98c) auf Druck278. Keine neue PDF-/Glyphenpruefung in dieser Review.
Die Quellenreview berichtet ausdruecklich eine empirisch motivierte Wahl;
hier wird deren logische Bestimmtheit untersucht, kein Optimierungs-
protokoll rekonstruiert und keine weitere Fitdurchfuehrung behauptet.

H und G heissen hier ausschliesslich die Korrekturteile von F=H+G,
nicht die KGH-Polynome der spaeteren Massensumme. Die im Buch stehende
Form ist inzwischen positiv belegt; die Frage ist deshalb nicht mehr,
ob das Exponentieren dieser Form funktioniert, sondern welche zusaetzlichen
Bedingungen ihre Koeffizienten auswaehlen.

## 2. Ansatz, reeller Definitionsbereich und gewaehltes Tupel

Fuer festes k setze

    d=s^2>0, s=sqrt(d)>0, Y=xi^2>0, xi>0,
    C=alpha*(1+s)/3, V=eta11/e,
    R=(1-s)/(1+s), Z=2^k*R^2.

C,V,Z sind hier eigene kurze Bezeichnungen fuer die Logarithmusbasen,
keine neuen Heim-Parameter. Vorausgesetzt sind alpha>0, eta11>0,
e>0 und fuer lnG ausserdem d!=1. Dann sind alle Logargumente positiv:

    ln H = A1*ln C + A2*ln Y + A3*ln d,
    ln G = B1*ln(V/d) + B2*ln Y + B3*ln d + B4*ln Z.

Die gewoehnliche reelle Exponentialfunktion ist injektiv. Fuer jedes
feste endliche reelle Koeffiziententupel folgt daher genau eine positive
Auswertung

    H=C^A1 * Y^A2 * d^A3,
    G=(V/d)^B1 * Y^B2 * d^B3 * Z^B4.

Gleichheit des Tupels ist hinreichend fuer Gleichheit der Funktionen.
Umgekehrt bestimmt aber die reine Existenz dieser Funktionen kein Tupel.
Auch bei vorab akzeptiertem A1=B1=B4=1 bleibt im abstrakten Ansatz
zunaechst die Wahl von A2,A3,B2,B3 zu begruenden.

Die Buchwahl lautet

    A=(1,(2k+1)/2,1-4k),
    B=(1,k/2,k,1).

Sie ergibt algebraisch

    H=alpha*(1+s)/3 * xi^(2k+1) * d^(1-4k),
    G=V*xi^k*2^k*d^(k-1)*R^2.

Dies ist die bereits belegte H004/H010-Form, keine neue Alternative.
Alle Basen sind dimensionslos; beliebige reelle Potenzen dieser Basen
bleiben dimensionslos. Dimensionsanalyse kann deshalb die genannten
Exponenten hier nicht bestimmen. Ganzzahligkeit von k schraenkt das
Argument einer Koeffizientenfunktion ein, erzwingt aber nicht die
vorgeschlagenen Funktionen von k. Schon A3->A3+1 und B3->B3+1
bewahren fuer jedes ganzzahlige k die Ganzzahligkeit dieser beiden
Exponenten. Die gewaehlten A2/B2 sind selbst gegebenenfalls halb-ganzzahlig.

## 3. Was der formale Grenzfall d nach 1 liefert

Diese Grenzanalyse haelt alpha,Y,eta11,e,k und alle Koeffizienten fest.
Insbesondere werden die Koeffizienten fuer diesen Absatz nicht als
unbekannte Funktionen von d variiert. Ob eine entsprechende kontinuierliche
Folge physikalisch zulaessiger q,k-Zustaende existiert, ist keine Folge
dieser rein reellen Grenzanalyse.

Fuer H ist d=1 selbst zulaessig und

    lim H = (2*alpha/3)^A1 * Y^A2.

Der Koeffizient A3 verschwindet aus dem Grenzwert. Endlichkeit und
Positivitaet dieses Grenzwertes gelten unter den genannten Voraussetzungen
fuer jedes endliche reelle A1,A2,A3, nicht nur fuer die Buchwahl.

Fuer G darf d=1 dagegen **nicht** direkt in die Logform eingesetzt werden:
R=0 und ln Z ist dort undefiniert. Eine stetige Fortsetzung wird aus dem
Grenzwert des bereits exponentierten Ausdrucks begruendet. Exakt gilt

    R^2=(d-1)^2/(1+sqrt(d))^4.

Damit, fuer beliebiges endliches reelles B4,

    G ~ V^B1 * Y^B2 * 2^((k-4)*B4) * |d-1|^(2*B4),

wobei das Verhaeltnis zur rechten Seite nach 1 geht. Es folgt:

- B4>0: G geht nach 0.
- B4=0: G geht nach V^B1*Y^B2>0.
- B4<0: G divergiert nach positiv unendlich.

Die Forderung G->0 erzwingt somit hoechstens B4>0. Ein ausdruecklich
verlangtes quadratisches Verschwinden mit endlicher nichtnulliger
Amplitude wuerde B4=1 festlegen, aber noch nicht B1,B2,B3. Blosse
beschraenkte Fortsetzbarkeit laesst sogar alle B4>=0 zu.

Staerkerer Nicht-Eindeutigkeitszeuge: Fuer beliebige feste reelle t,u
liefert A3->A3+t den Quotienten H_neu/H_alt=d^t, und B3->B3+u den
Quotienten G_neu/G_alt=d^u. Beide Quotienten gehen nach 1. Diese
Aenderungen bewahren also die vollstaendigen gerade genannten
Grenzwerte sowie bei G sogar fuehrende Potenz und Amplitude, aendern
aber fuer d!=1 im Allgemeinen die Funktionen. Fuer t=u=1 bleiben
auch die ganzzahligen Exponentenmuster erhalten.

Das ist ein Zeuge gegen Eindeutigkeit **aus diesen Bedingungen**, kein
Nachweis, dass ein solches alternatives Tupel alle weiteren metronischen,
Potential- oder Zustandsbedingungen der Theorie erfuellt.

## 4. Ein synthetischer Anker ist kein Koeffizientenbeweis

Ein bekannter positiver Einzelwert H0 an einem festgelegten Punkt
(alpha0,d0,Y0) verlangt genau

    (ln C0, ln Y0, ln d0) dot (A1,A2,A3) = ln H0.

Ist die linke Zeile nicht null, hat diese eine reelle lineare Gleichung
Rang 1: konsistente Loesungen bilden eine affine Ebene in R^3. Jede
Verschiebung deltaA orthogonal zur Zeile erhaelt den Anker. Ist A1=1
schon als eigene Zusatzbedingung gesetzt, bleibt normalerweise eine
Gerade in den beiden verbleibenden Koeffizienten. Eine Nullzeile
enthaelt noch weniger Information. Analog gibt ein separat bekannter
G-Anker hoechstens eine Gleichung in vier B-Koeffizienten.

Ein exakter rationaler Zeuge, ohne Teilchen- oder Messwertbezug, ist

    k=1, alpha0=1/2, d0=1/4, s0=1/2, Y0=4, xi0=2.

Dann ist C0=1/4 und fuer die Buchwahl H0=128. Mit beliebigem t und

    A1=1, A2=3/2+t, A3=-3+t

bleibt H0 unveraendert, weil der neue Quotient (Y0*d0)^t=1 ist.
Diese ganze Familie wahrt A1=1, positive reelle Auswertung und einen
endlichen d->1-Grenzwert. Bei ganzzahligem t bleiben A3 ganzzahlig
und A2 halb-ganzzahlig. An einem anderen synthetischen Punkt, etwa
d=1/9 bei unveraendertem Y=4, ist der Quotient dagegen (4/9)^t.
Die Funktionen sind also nicht lediglich anders notiert.

Auch fuer G gibt es mit festem B1=B4=1 die Verschiebung
B2->B2+t,B3->B3+t und denselben Ankerquotienten (Y0*d0)^t.
Bei der zusaetzlichen rein synthetischen Wahl V=eta11/e=1/5 ist
G0=4/45. Das setzt keine echte eta- oder Teilchenkonfiguration ein.

Die Ankerfamilie und die Familie aus Abschnitt 3 belegen **verschiedene**
schwache Bedingungspakete. Es wird nicht behauptet, dass die Ankerfamilie
auch jede zuvor festgelegte numerische Grenzamplitude erhaelt. Ausserdem
ist ein Zahlenwert von F=H+G oder einer ganzen Masse keine separat
gegebene lineare Gleichung fuer lnH und lnG; ln(H+G) ist nicht lnH+lnG.

## 5. Welche Zusatzbedingungen Eindeutigkeit herstellen koennen

Unter einem festgelegten gemeinsamen Koeffizientenvektor liefern mehrere
Anker ein lineares System L*A=h fuer H bzw. L_G*B=g fuer G. Wenn es
konsistent ist und die jeweilige Merkmalsmatrix vollen Spaltenrang besitzt,
ist der Vektor eindeutig. Vorher festgelegte Koeffizientengleichungen
reduzieren die Zahl der noch freien Komponenten. Wiederholte, gekoppelte
oder entartete Punkte sind nicht automatisch unabhaengige Bedingungen.
Das ist keine Aufforderung, solche Anker aus Massenwerten nachzufitten.

Insbesondere kann eine **vollstaendige vorgegebene Grenzwertfunktion**
H(1,alpha,Y) fuer unabhaengig variable positive alpha und Y die
Koeffizienten A1 und A2 festlegen. Danach kann ein zusaetzlicher
Innenanker mit d0!=1 A3 bestimmen. Das ist wesentlich staerker als
die Forderung, der Grenzwert solle nur endlich oder positiv sein.
Ebenso koennen unabhaengig hergeleitete Differential-, Variations- oder
Randbedingungen Koeffizienten auswaehlen, sofern sie tatsaechlich diese
Information enthalten. Deren Gueltigkeit wird hier nicht vorweggenommen.

Die drei A- und vier B-Komponenten sind hier lediglich die Dimensionen
zweier formaler Vektoren **bei festem k**, keine gepruefte Zahl unabhaengiger
empirischer Fitparameter der ganzen Heim-Theorie. Ob Koeffizienten ueber
verschiedene k gekoppelt werden und welche Daten welche Kombination
fixieren, verlangt ein explizites Zusatzmodell bzw. Kalibrierprotokoll.

## 6. Ausfuehrbare exakte Kontrollen

Der folgende Standardbibliothekscode verwendet nur eigene rationale
Algebrazeugen. Er importiert weder Projekt-Auswerter noch historische
Programme und liest keine Massendaten. Grenzwerte folgen aus Abschnitt 3;
der Code prueft dafuer die exakt regularisierten Quotienten, nicht eine
zufaellige endliche Naeherung an d=1.

```python
from fractions import Fraction as F

def H(k,s,xi,alpha,t=0,anchor_shift=False):
    d=s*s
    # t alone shifts A3; anchor_shift also shifts A2 by t.
    y_power=2*k+1+(2*t if anchor_shift else 0)
    return alpha*(1+s)/3*xi**y_power*d**(1-4*k+t)

def G(k,s,xi,V,u=0,anchor_shift=False):
    d=s*s
    assert s>0 and s!=1 and xi>0 and V>0
    r=(1-s)/(1+s)
    y_power=k+(2*u if anchor_shift else 0)
    return V*xi**y_power*F(2)**k*d**(k-1+u)*r*r

checks=0
for k in (1,2,3,4):
    for s in (F(1,3),F(1,2),F(3,2)):
        d=s*s
        xi,alpha,V=F(2),F(1,2),F(1,5)
        assert ((1-s)/(1+s))**2==(d-1)**2/(1+s)**4
        for shift in (-2,-1,0,1,2):
            assert H(k,s,xi,alpha,shift)/H(k,s,xi,alpha)==d**shift
            assert G(k,s,xi,V,shift)/G(k,s,xi,V)==d**shift
            h_limit=2*alpha/3*xi**(2*k+1)
            assert H(k,s,xi,alpha,shift)/h_limit==(1+s)/2*d**(1-4*k+shift)
            g_lead=V*xi**k*F(2)**(k-4)
            assert G(k,s,xi,V,shift)/(g_lead*(d-1)**2)==16*d**(k-1+shift)/(1+s)**4
            # Continuous extensions of these regularized ratios at s=1.
            assert (1+F(1))/2*F(1)**(1-4*k+shift)==1
            assert 16*F(1)**(k-1+shift)/(1+F(1))**4==1
            checks+=6

s0,xi0,alpha0,V0=F(1,2),F(2),F(1,2),F(1,5)
assert H(1,s0,xi0,alpha0)==128
assert G(1,s0,xi0,V0)==F(4,45)
for shift in (-2,-1,0,1,2):
    assert H(1,s0,xi0,alpha0,shift,True)==128
    assert G(1,s0,xi0,V0,shift,True)==F(4,45)
    s=F(1,3)
    assert H(1,s,xi0,alpha0,shift,True)/H(1,s,xi0,alpha0)==F(4,9)**shift
    assert G(1,s,xi0,V0,shift,True)/G(1,s,xi0,V0)==F(4,9)**shift
    checks+=4

# At the H anchor: log-feature vector = log(4)*(-1,1,-1).
# A1 remains fixed, while deltaA=(0,t,t) is in its kernel.
feature=(F(-1),F(1),F(-1))
for shift in range(-4,5):
    delta=(F(0),F(shift),F(shift))
    assert sum(a*b for a,b in zip(feature,delta))==0
    checks+=1
print('Exact checks counted:',checks)
print('H_anchor=128; G_anchor=4/45; alternative functions differ away from anchor')
print('No mass fit, eigenvalue selection, or metronic operator validation')
```

Am 2026-09-06 mit `python -B -` erfolgreich ausgefuehrt: 389 im Code
gezaehlte exakte Fraction-Pruefungen bestanden, dazu die vorangestellten
Basisidentitaeten; `git diff --check` ohne Befund. Nur diese neue Review
wurde von data_audit geschrieben. Keine alten Rechner, Inputs, Snapshots,
Tests, Normalisierungen oder Quellen wurden veraendert.

## 7. Reichweite fuer das weitere Quellenurteil

Zulaessig ist: Die konkrete H004-Koeffizientenwahl ist eine hinreichende
Spezialisierung des Logansatzes; die hier geprueften allgemeinen
Minimalbedingungen machen sie noch nicht mathematisch eindeutig.
Der Autorenhinweis auf empirische Anpassung bleibt eine separate positive
Quellenaussage. Ein Fitfehler, eine optimale Zielfunktion oder eine Zahl
unabhaengiger Kalibrierparameter wurde daraus nicht errechnet.

Nicht zulaessig waere: Die eigenen Tupel seien alternative vollstaendige
Heim-Loesungen, saemtliche moeglichen Quellenbedingungen seien widerlegt,
die Buchform sei deshalb falsch oder die gesamte Theorie widerlegt.
Vor einem staerkeren Eindeutigkeitsurteil waeren die angeblich tragenden
Zusatzbedingungen einzeln anzugeben und ihre unabhaengige Information
ueber A/B zu pruefen. Die hier gewaehlten rationalen Anker ersetzen diese
Quellenarbeit nicht.

## 8. Gegenlesung der unabhaengig erstellten Root-Tests

`tests/test_alpha3_assumptions.py` vollstaendig gelesen und mit
`python -B -m unittest discover -s tests -p 'test_alpha3_assumptions.py' -v`
ausgefuehrt: alle 10 Tests erfolgreich. Kein Algebrafehler gefunden.
Die zusaetzlichen Werte H=405/16 gegen H_neu=45 bei d=4/9 stimmen,
ebenso die Determinante -1 der zwei unabhaengigen logarithmischen
A2/A3-Bedingungen. Die H/G-Randtests sind deutlich als Fortsetzungen
des exponentierten Ausdrucks beschriftet; der G-Test prueft den
regularisierten quadratischen Kofaktor und setzt nicht ln(0) ein.

Der Ladungsfaktor-Test q=0 ist eine reine Multiplikatoridentitaet bei
endlichem H+G und kuenstlich festgehaltenem d. Ebenso bleiben beim
synthetischen Vergleich von q=1 und q=2 die uebrigen Groessen fest. Das ist keine
gemeinsame Auswertung von q und d=eta(q,k) als physikalische
Quellenkonfiguration. Diese kleine Reichweitenpraezisierung wurde an
Root gemeldet; sie ist kein Rechenfehler der als synthetisch erklaerten
Tests. Keine Hauptdatei wurde von data_audit geaendert.
