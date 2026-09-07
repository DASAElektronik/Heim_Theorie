# POTENTIAL_PATH_MATH_REVIEW

2026-09-06, Etappe 22; unabhaengige Mathematikreview, data_audit.
Die visuell bestaetigten (98)-Formeln werden aus dem Root-Auftrag
uebernommen; keine eigene PDF-/Glyphenrecherche. Alle folgenden Aussagen
halten Radius, gemeinsamen Proportionalitaetsfaktor und den positiven
epsilon-Zweig fest. P=V_epsilon>0 ist konstant. Keine Massenrechnung.

## 1. Eine Komponentenkurve, keine vier freien Potentiale

Schreibe, nur zur Unterscheidung der normierten Komponenten,

    U(s)=V_(omega,epsilon)/P=(1+s)/2,
    R(s)=V_(rho,rho)/P=s^2,
    O(s)=V_(omega,omega)/P=(1+s)^2/4,
    D(s)=V_(delta,delta)/P=(1-s)^2.

R ist hier eine Komponente, nicht ein Radius oder relativer Sprung.
Fuer den gelockerten Abschluss 0<=s<=1 gilt exakt

    1/2<=U<=1,  0<=R<=1,  1/4<=O<=1,  0<=D<=1,
    O=U^2,  R=(2U-1)^2,  D=4*(1-U)^2,
    sqrt(R)+sqrt(D)=1,  4*O+D=2+2*R.

U,R,O sind auf diesem Intervall streng steigend, D streng fallend.
Bereits ein festgehaltener Komponentenwert legt deshalb s und alle
anderen Werte fest. Man kann auf dieser Kurve nicht nur eine der vier
Komponenten aendern und die anderen unveraendert lassen.

Im Quellenprofil ist s=(1+(4+k)*q^4/pi^4)^(-1/8). Bei festem q,k
und festem pi ist s bestimmt; bei zusaetzlich festem P gibt es in
diesen skalaren Formeln keine freie Potentialvariation. Fuer k>=1
und endliches reelles q ist s>0; s=1 entspricht q=0, s=0 nur dem
entsprechenden Grenzabschluss. Eine kontinuierliche Freigabe von s
ist keine aus der Quelle bewiesene kontinuierliche Bewegung ihrer
ganzzahligen Zustandslabels. Auch der Abschluss [0,1] ist hier eine
bewusst weiter gefasste mathematische Vergleichsmenge.

## 2. Was an einer gemeinsamen unskalierten Startkurve scheitert

ZUSAETZLICHE, nicht der Quelle unterstellte Interpretation: Beide
H-Integrationskanaele sollten gleichzeitig auf derselben unskalierten
Komponentenkurve bei einem gemeinsamen s0 beginnen. Dann verlangte
der untere A1-Wert P/2 gerade U(s0)=1/2, also s0=0. Der untere
A3-Wert P verlangte R(s0)=1, also s0=1. Es gibt kein gemeinsames s0,
selbst nicht im gelockerten Abschluss.

Auch der gesetzte obere A1-Wert alpha*U(sf)*P/3 ist bei 0<alpha<1
kein Punkt der unskalierten U-Komponentenkurve, denn

    0<alpha*U(sf)/3 <= alpha/3 < 1/2 <= U(s).

Diese Aussagen widerlegen nur die gerade hinzugefuegte Interpretation
als gleichzeitige unreskalierte Raw-Komponentenkurve. Die Quelle kann
verschiedene Endpotentiale, getrennte Integrationskanaele oder reskalierte
Potentialgroessen einsetzen. Im W-Kanal wird sogar ausdruecklich von
O zu C_k*D gewechselt; das ist schon formal nicht dieselbe rohe
Komponentenfunktion an zwei Punkten. Die algebraisch moegliche Deutung
als getrennte Kanaele liefert ihrerseits noch keinen gemeinsamen
Zeit-/Metronpfad oder eine Dynamik aus den Endwerten.

## 3. Exakte endliche Kopplung der Spruenge

Sei t der fruehere und s der aktuelle Kurvenparameter. Bei 0<s,t<1
sind alle Komponenten und Logarithmen regulaer. Fuer die auf den
aktuellen Wert normierten Rueckwaertsspruenge gilt

    r_U=(s-t)/(1+s),
    r_R=(s^2-t^2)/s^2,
    r_O=(s-t)*(2+s+t)/(1+s)^2=2*r_U-r_U^2,
    r_D=(t-s)*(2-s-t)/(1-s)^2.

Die U/O-Formeln gelten auch an beiden Randpunkten; R benoetigt fuer
den relativen Sprung s>0, fuer positive Log-Nachbarn zusaetzlich t>0.
D benoetigt s!=1 und fuer positive Log-Nachbarn zusaetzlich t!=1.
Insbesondere darf D(1)=0 nicht als positiver Log-Endpunkt behandelt
werden. Die Formeln enthalten die quadratischen Differenzterme genau,
keine still eingefuehrte Differentialnaeherung.

## 4. Gekoppelter synthetischer H-Pfad, kein Heim-Zustandsweg

Im eigenen gemeinsamen-Gitter-Modell aus Etappe 21 setze k=1,a=1/10,
r_X=0 und S=a*(r_U-3*r_R). Dann ist H_neu/H_alt=1/(1-S).
Fuer 0<t<s<=1 gilt r_R>r_U>0, somit S<0; bei H0>0 bleibt H
positiv und nimmt ab. Hier werden U und R gemeinsam entlang derselben
Kurve veraendert, nicht als unabhaengige Potentialeingaben gewaehlt.

Die beiden rein synthetischen s-Pfade (1/2,3/4,1) und (1/2,7/8,1)
haben identische Endkomponenten. Mit H0=1 liefern sie dennoch exakt

    H_end=16800/21659  bzw.  98000/123261.

Es bleiben also trotz der Komponentenkopplung unterschiedliche endliche
Schrittprodukte. Eine als eigene Grundgleichung gesetzte Logversion
haette fuer beide H_end^10=(U_end/U_start)/(R_end/R_start)^3=1/48.
Keine dieser Rechnungen waehlt einen richtigen physikalischen Pfad aus.
Am Ende s=1 ist D=0: positiv sind hier die aktiven U/R-Komponenten
und H, nicht alle vier Komponenten. Ein G-/lnD-Pfad wird nicht getestet.

## 5. Ein ausfuehrbarer Standardbibliotheksblock

```python
from fractions import Fraction as F

def components(s):
    assert 0<=s<=1
    return (1+s)/2,s*s,(1+s)**2/4,(1-s)**2

grid=tuple(F(n,8) for n in range(9))
for s in grid:
    u,r,o,d=components(s)
    assert F(1,2)<=u<=1 and 0<=r<=1 and F(1,4)<=o<=1 and 0<=d<=1
    assert o==u*u and r==(2*u-1)**2 and d==4*(1-u)**2
    assert 4*o+d==2+2*r
    assert (u==F(1,2))==(s==0) and (r==1)==(s==1)
    assert not (u==F(1,2) and r==1)
    for alpha in (F(1,100),F(1,2),F(9,10)):
        assert 0<alpha*u/3<F(1,2)
for t,s in zip(grid,grid[1:]):
    before,after=components(t),components(s)
    assert all(after[i]>before[i] for i in range(3)) and after[3]<before[3]
for t in grid[1:-1]:
    for s in grid[1:-1]:
        old,new=components(t),components(s)
        jumps=tuple(1-v/w for v,w in zip(old,new))
        ru,rr,ro,rd=jumps
        assert ru==(s-t)/(1+s) and rr==(s*s-t*t)/(s*s)
        assert ro==(s-t)*(2+s+t)/(1+s)**2==2*ru-ru*ru
        assert rd==(t-s)*(2-s-t)/(1-s)**2

def h_path(path):
    h=F(1)
    for t,s in zip(path,path[1:]):
        assert 0<t<s<=1
        old,new=components(t),components(s)
        ru,rr=1-old[0]/new[0],1-old[1]/new[1]
        assert rr>ru>0
        S=F(1,10)*(ru-3*rr)
        assert S<0 and 1-S>0
        h/=1-S
        assert h>0
    return h
p1,p2=(F(1,2),F(3,4),F(1)),(F(1,2),F(7,8),F(1))
h1,h2=h_path(p1),h_path(p2)
assert (h1,h2)==(F(16800,21659),F(98000,123261)) and h1!=h2
assert components(p1[0])==components(p2[0])
assert components(p1[-1])==components(p2[-1])
u0,r0,_,_=components(p1[0]); uf,rf,_,df=components(p1[-1])
assert (uf/u0)/(rf/r0)**3==F(1,48)
assert h1**10!=F(1,48) and h2**10!=F(1,48)
assert df==0 and min(u0,r0,uf,rf)>0
print('Exact component identities, coupled jumps, endpoints and H paths OK')
print('H_path1',h1,'H_path2',h2,'log_model_tenth_power',F(1,48))
print('Synthetic relaxed s paths only; no particle mass or source dynamics')
```

Am 2026-09-06 mit `python -B -` erfolgreich ausgefuehrt: saemtliche
Fraction-Kontrollen bestanden; `git diff --check` ohne Befund. Keine
Dezimalnaeherung benoetigt. Nur diese neue Review wurde geschrieben.

Die universellen Aussagen sind oben algebraisch begruendet; das rationale
Gitter dient nur als unabhaengiger endlicher Gegencheck. Der neue Befund
gegenueber Etappe 21 ist die explizite Komponentenkopplung und die enge
Grenze einer gemeinsamen unskalierten Endpunktdeutung, keine pauschale
Inkonsistenz aller moeglichen Integrationskanaele oder der Heim-Theorie.

Nachtrag: `tests/test_potential_paths.py` vollstaendig gegengelesen und mit
`python -B -m unittest discover -s tests -p 'test_potential_paths.py' -v`
ausgefuehrt: alle zehn Tests erfolgreich, kein Algebrafehler gefunden.
Die q/pi-Viertpotenzinversion bleibt explizit relaxierte Algebra; die
separaten positiven Interpolationskanaele sind keine Raw-Komponenten
oder Quelldynamik. Beide gekoppelten H-Pfadwerte stimmen exakt. D(1)=0
ist ausdruecklich markiert, kein lnD/G-Schritt wird behauptet.
Nur diese eigene Review geaendert; keine Hauptdateien bearbeitet.
