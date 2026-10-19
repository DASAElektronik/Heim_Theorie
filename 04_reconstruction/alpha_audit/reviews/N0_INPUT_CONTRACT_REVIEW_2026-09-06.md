# H006 e-, N=0: Eingabevertrag und begrenzte Algebra

Stand: 2026-09-06, Etappe 16 ab `7a00e46`.
Unabhaengige Readiness-/Mathematikpruefung mit nachfolgend beauftragter
bedingter Zahlenauswertung, kein Vergleich mit einer Sollmasse.

## 1. Ergebnis und Pruefgrundlage

Ein n-Tupel allein ist noch kein vollstaendiger Eingabevertrag:
Konfiguration, nacktes Alpha, mathematische Konstanten und historische
dimensionale Konstanten muessen ebenfalls festgelegt sein. Innerhalb
der hier festgelegten H006-AUX-/MASS-Fassung sind danach keine weiteren
unbekannten Funktionen fuer die bedingte Teilsummenauswertung erforderlich.
Insbesondere sind N1,N2,N3 abgeleitete Koeffizienten, keine zusaetzlich
zu suchenden Besetzungszahlen.

Waehrend der Pruefung kam ein positiver Quellenanschluss hinzu: Der
ausdrueckliche N0-Pfad ueber (XV), (XVII)-(XIX), (XXVI) und den Algorithmus
auf Druck9 liefert fuer die vorgegebene Elektronkomponente den Nullfall
n=(0,0,0,0), sofern die getrennt ausgewiesenen Voraussetzungen gelten.
Die unten geprueften drei Konstantenprofile erfuellen dessen strikte
Greedy-Grenzen. Dies benoetigt keinen Massenzielwert oder Tabellenimport.
Es ist keine stillschweigende Harmonisierung aller gedruckten Gleichungen:
Der Exponent in (XIV) unterscheidet sich sichtbar vom expliziten N0-Pfad.

Vollstaendig gelesen: HT-F-1982-AUX, MASS, MU, ALPHA, QNUM, SELECTION
und SELECTION-WVX sowie die Entscheidungen AUX-SYMBOL-ROLES,
AUX-PHI-PRECEDENCE, MASS-MU-ALPHA-PLUS, MASS-UNDERLINED-G,
G-SYMBOL-ROLES, MU-HISTORICAL-CONSTANTS, ETA-INDEX,
ALPHA-RECONCILIATION, ALPHA-NEGATIVE-BRANCH, SELECTION-XIII-ALPHA3,
WVX-SYMBOL-FAMILIES, ALGO-INTEGER-DECIMAL-RULE, ALGO-W4-CASES und
STACKED-BINOMIAL, jeweils mit den vorhandenen NORM-Praefixen.

Nach vollstaendiger Lektuere des PDF-Skills wurden H006 Druck/PDF4,5,6,8,9
als vollstaendige Seiten selbst visuell geprueft. Die Konstanten- und
N1..N3-Lesung bestaetigte unabhaengig der Quellenagent. Die neue
kontextuelle W-Indexbruecke ueber die geprueften Seiten wird aus der
aktuellen Haupt-/Quellenagentenpruefung uebernommen; keine alte
Aliasnormalisierung wird durch diese Review heimlich geaendert.

Quelle: H006, `01_sources/heim_primary/Massenformel_nach_B_Heim_1982.pdf`,
IGW-Reproduktion mit sichtbarer Kennzeichnung Innsbruck 2003.
Keine Gleichsetzung mit einer unveraendert vorliegenden Urschrift 1982.

## 2. Aktive Eingaben und Profile

Der vorgegebene Komponentenkontext ist

```text
epsilon=+1, k=1, P=Q=1, kappa=0, C=0, x=1,
qx=-1, q=abs(qx)=1, N=0.
```

Das zugeordnete (0110) ist eine Konfigurationsschreibweise, kein n-Tupel.
Epsilon, C und x sichern hier die Komponentenidentifikation; in der
reduzierten AUX-Massensumme werden sie nicht nochmals als freie
numerische Faktoren eingefuehrt.

| Groesse | Rolle im konkreten Eingabevertrag |
| --- | --- |
| n1..n4 | Besetzungsparameter; nicht mit N1..N3 oder den Konfigurationsziffern verwechseln. Allgemein auch negativ erlaubt, sofern K_j=n_j+Q_j>=0; hier liefert der unten begrenzte Pfad n=0. |
| pi, e_base, xi | Aktive dimensionslose Konstanten. e_base ist die Logarithmenbasis, nicht e- oder eine elektrische Ladung. Xi bleibt in t, alpha3 und Phi aktiv. |
| alpha_bare | Kleiner positiver Zweig des H006-Profils `1982_source_literal`; ALPHA-eta12 bedeutet hier k=1,q=2. Kein gedruckter Kehrwert oder Sollalpha als Ersatz. |
| alpha_mass_plus/minus | Getrennte AUX-Koeffizienten aus (VIII), nicht die zwei Feinstrukturzweige. Der Plus-Koeffizient ist der Massenmultiplikator. |
| alpha1..3, N1..3, Q1..4 | Vollstaendig abgeleitete Koeffizienten. N1=alpha1, N2=(2/3)alpha2, N3=2alpha3; fuer k=1 ist Qj=(3,3,2,1). |
| hbar,c,gamma_grav,s0 | Historische dimensionale Eingaben fuer mu; gamma_grav ist nicht Lorentz-gamma und mu ist nicht das Myon. |
| beta, W, a_vx,b_vx,F(Gamma),Q_N | Keine numerischen Eingaben der reduzierten bedingten N0-Massensumme. W und seine Domain kommen erst bei der gesonderten Auswahlpruefung ins Spiel; unbekannte Resonanzfunktionen werden dadurch nicht bestimmt. |

Die MU-Formelkarte nennt e_base/xi nicht in ihrem Konstantenblock;
Symbolregister und H006 Druck4 nennen sie jedoch. Dies ist keine neue
freie Modellgroesse. Die Seite druckt e=2.71828183, pi=3.1415926535,
xi=1.61803399 und erwaehnt die Darstellung von xi durch (1+sqrt(5))/2
bis zur achten Dezimalstelle. Das Profil muss sagen, wie diese Angaben
numerisch verwendet werden.

Vor Kenntnis eines Massenergebnisses wurden folgende drei Profile
unterschieden und unten nur fuer Hilfsgroessen/Auswahlgrenzen geprueft:

| Profilname im Reviewcode | pi / e_base | xi |
| --- | --- | --- |
| math_pi_e_printed_xi | Mathematische Konstanten | Gedruckt 1.61803399 |
| golden_xi | Mathematische Konstanten | Eigene getrennte Sensitivitaet mit (1+sqrt(5))/2 |
| printed_all | Gedruckte Dezimalzahlen | Gedruckt 1.61803399 |

In allen drei Profilen bleiben exp und ln die mathematischen Funktionen.
Insbesondere bedeutet exp(-1/3) nicht `e_printed**(-1/3)`.
Das erste Profil darf nicht als vollstaendig dezimal-literal ausgegeben
werden. Die Profilunterschiede sind Eingabesensitivitaeten, keine
statistischen Unsicherheiten oder nach Trefferqualitaet gewaehlte Varianten.

Fuer eine spaetere Massenrechnung sind in allen drei Profilen separat
die gedruckten dimensionalen Werte hbar=1.0545887e-34 J s,
c=2.99792458e8 m/s, gamma_grav=6.6732e-11 N m^2/kg^2 und s0=1 m
vorgesehen. Die hier direkte mu-Form braucht epsilon0, mu0 und den
Wellenwiderstand nicht numerisch. c darf dabei nicht aus den gerundeten
epsilon0/mu0 nochmals als anderer Zahlenwert rekonstruiert werden.
In diesem Satz meint c selbstverstaendlich die Lichtgeschwindigkeit,
nicht das oben genannte Konfigurations-C.

## 3. Eindeutige Reduktion der Teilsummen

Verwende eigene Kurzzeichen h=eta, d=eta(k=1,q=1), s=sqrt(d),
a=alpha_bare, ap=alpha_mass_plus und am=alpha_mass_minus.
Dabei ist h keine Planck-Konstante; diese rein lokale Abkuerzung
wird im Code als `eta0` gefuehrt. Quellen-eta(1,1) und eta_qk fallen
fuer diesen konkreten Fall zusammen, ohne Indexwechsel in anderen Formeln.

Aus (VIII)/(IX) folgt exakt

```text
t  = 1-(2/3)*xi*h^2*(1-sqrt(h)),
ap = t/h^(7/3)-1,       am = t/h^(4/3)-1,
am+1 = h*(ap+1),

alpha1 = (1+s)/2,
alpha2 = 1/d,
alpha3 = 1 - a*xi^3*(1+s)^3/(3*d^3)
           - [2*sqrt(xi*d)/e_base]*[(1-s)/(1+s)]^2.
```

E_base verschwindet also nicht schon wegen e_base^(k-1)=1: Es bleibt
im zweiten Korrekturterm von alpha3. Auch a bleibt aktiv, insbesondere
`d(alpha3)/da=-xi^3*(1+s)^3/(3*d^3)`, bei positiven xi,d ungleich null.

Setze Kj=n_j+Qj, Qj=(3,3,2,1). Aus Ausmultiplizieren der drei
Polynomanteile folgt die kompakte, aber quellenbedingt gleichwertige Summe

```text
S = K_aux+G_aux+H_aux
  = N1*K1^2*(K1+1)^2
    + N2*K2*(2*K2^2+3*K2+1)
    + N3*K3*(K3+1) + 4*K4.
```

Die gemischten H-Terme sind genau die Kreuzterme der Verschiebung.
Das bedeutet keine Gleichsetzung von K_aux und den Auswahlzahlen Kj.
Fuer n=0 gilt K_aux=H_aux=0, aber
`G_aux=144*N1+84*N2+6*N3+4` bleibt bestehen.

Die vorhandene Phi-Normalisierung liefert mit r=am/ap

```text
L = 12*s/pi*(1-a/3)*(1+4*pi*a/(h*sqrt(h)))*(1+n1/3)
    + 8*a/xi^2,
Phi_aux = (1-r)*L + 4*r.

M/mu = ap*S + (ap-am)*L + 4*am.
```

Die letzte Zeile ist zunaechst eine bedingte algebraische Teilsummenformel;
ihre spaeter beauftragte Auswertung steht in Abschnitt 7. Die Originaldomain ap!=0 bleibt
erhalten, obwohl sich der Quotient nach Multiplikation wegkuerzen laesst.

Termnullen: k-1=0, kappa=0, P-Q=0 und choose(P,2)=0 vereinfachen
F4/F5/F6/F7. Dagegen sind F3=2, F7=2*d und F9=1+n1/3 nicht generell
null. Die zwei additiven Phi-Terme bleiben ausserhalb der Produktkette.
Selbst bei n1=-3 verschwindet nur diese Produktkette, nicht automatisch
ganz Phi. Bei n=0 ist F9=1; aus N=0 folgt hier kein zusaetzliches
Wegmultiplizieren des grossen Phi. H007s kleines phi ist kein Ersatz.

Die Originalausdruecke brauchen positive h,d,xi,e_base,pi, definierte
Wurzeln, ap!=0 und die angegebenen Nenner. Fuer den vorliegenden Fall
werden k=1, Q1=3 und F6-Nenner=1 unproblematisch. Ganzzahlige n_j
haben aus der Quellenregel nur die unteren Grenzen (-3,-3,-2,-1),
nicht pauschal n_j>=0; weitere Auswahlbedingungen sind gesondert.
Bei positiven dimensionalen Konstanten reduziert die MU-Formel auf kg:
Der Kubikwurzelfaktor hat Einheit m^2/s, der Quadratwurzelfaktor
kg*s/m, der abschliessende Faktor s0^-1 die Einheit 1/m.

## 4. Nachtrag: der begrenzte algorithmische Nullfall

Unter den vorgegebenen k,P,Q,kappa,q,qx verschwinden in (XVII)/(XVIII)
alle Koeffizienten von w(1) und w(2), sofern die zugehoerigen Ausdruecke
definiert sind. Druck6 gibt selbst die Konvention fuer den uneigentlichen
Term 0^0 bzw. die verschobene Programmierform an. Letztere ergibt hier
`w=[0]^1+[1]^0=1`, nicht eine von uns erfundene 0^0-Konvention.

Domain ist kein entbehrlicher Zusatz: Im (XVIII)-Nenner ist
`1+A24*(1+qx)=1`; 3-q=2 und `8-A66^(q*(q-1))=7` bei A66>0.
Die abweichende kompakte (XVI)-Schreibweise haette 1-A24; auch dies
ist hier endlich, weil A24=2*xi^2/(3*h)>3/2 fuer xi>3/2 und h<1.
Damit wird keine Fassungsabweichung des allgemeinen w-Ausdrucks repariert.

Bei an denselben kleinen Alpha-Zweig gekoppeltem beta gilt
`1-beta^2=a^2`. Der moeglich kritische A36-Nenner ist dann
`1-pi*e_base*(xi*e_base)^2*a^2` und in allen geprueften Profilen positiv.
Auch ein grober rationaler Nachweis reicht: Aus 3<pi<22/7, 0<eta<1
und 0<A1*A2<1 folgt fuer die kleine Loesung a<1/50. Mit e_base<3 und
xi<2 ist der abzuziehende Term kleiner `(22/7)*27*4/2500<1`.
Die Nullstruktur setzt somit nicht 0*(1/0) gleich null. Andere
gedruckte oder angenaeherte Beta-Werte waeren separat zu deklarieren;
nach der Reduktion steht beta nicht mehr in der aktiven Massensumme.

Setze u=exp(-1/3). Der (XV)-Basiswert ist

```text
W=g=27*alpha1+9*alpha2+2*alpha3+u.
```

Der explizite N0-Algorithmus liefert K1=3,K2=3,K3=2, wenn die
positiven Unterreste und die strikten Oberabstaende

```text
64*alpha1-W > 0,
7*alpha2-2*alpha3-u > 0,
alpha3-u > 0
```

gelten. Im Hauptprofil betragen sie etwa 25.2243189566,
4.54119376675 und 0.198680299025. Dann ist W4=u in Fall (b), und

```text
K4=-3*ln(exp(-1/3))=1,       n=K-Q=(0,0,0,0).
```

Diese letzte Ganzzahl folgt analytisch exakt aus ln(exp(x))=x.
Kein Epsilon, keine empirische Wahl und keine nachtraegliche
,99...99-Promotion ist erforderlich. Ein gerundeter Dezimalrest darf
diese bewiesene Identitaet nicht in K4=0 verfaelschen.

Die originale (XIII)-Fassung mit rechtem alpha3 erfordert bei n=0
`1<=2*alpha3<=9*alpha2<=27*alpha3`; sie ist ebenfalls erfuellt.
Die auf Druck9 anschliessenden Bedingungen
`6*alpha3<=18*alpha2` und `84*alpha2<=162*alpha1` bestehen ebenfalls.
Somit wurde alpha3 rechts nicht heimlich durch alpha1 ersetzt.
Dies zeigt das Ergebnis dieses vorgegebenen Algorithmus, nicht die
Eindeutigkeit aller denkbaren Loesungen seiner Gleichung oder die
physikalische Identifikation eines Elektrons aus ersten Prinzipien.

### Sichtbarer Exponentenunterschied, nicht still korrigiert

Druck6 (XIV) hat `exp[1-2k(n4+Q4)/(3Q4)]`, waehrend Druck8 (XXVI)
und Druck9 `exp[(1-2k)(n4+Q4)/(3Q4)]` schreiben. (XV) hat ausdruecklich
exp[(1-2k)/3] fuer n_j=0. Bei k=1,n4=0,Q4=1 ergeben die beiden
Exponentformen exp(1/3) bzw. exp(-1/3), also verschiedene Werte.
Der Nullfall erfuellt deshalb nicht zugleich die woertliche (XIV)-Zeile
mit demselben W=g; der positive Rest waere exp(1/3)-exp(-1/3).

Die positive N0-Rekonstruktion gilt nur fuer den eigens genannten
N0-/Algorithmuspfad. Weder eine historische Korrekturabsicht noch die
Konsistenz aller H006-Zeilen wird daraus abgeleitet. Alte Formeldateien
und Normalisierungen wurden nicht umgeschrieben.

## 5. Ausfuehrbare unabhaengige Kontrollen

Die folgenden Bloecke berechnen keine Masse und verwenden keinen
Sollwert. Der erste prueft symbolische Identitaeten an exakten rationalen
Zeugen, nicht reale Teilchenzustaende. Der zweite wertet nur Hilfsgroessen
und Auswahlabstaende in den drei vorher benannten Profilen aus.

```python
from fractions import Fraction as F
from itertools import product
Q=(3,3,2,1)
N=(F(7,8),F(5,6),F(9,7))  # eigene rationale Identitaetszeugen
def parts(n):
    n1,n2,n3,n4=n; Q1,Q2,Q3,Q4=Q; N1,N2,N3=N
    K=n1*n1*(1+n1)**2*N1+n2*(2*n2*n2+3*n2+1)*N2+n3*(1+n3)*N3+4*n4
    G=Q1*Q1*(1+Q1)**2*N1+Q2*(2*Q2*Q2+3*Q2+1)*N2+Q3*(1+Q3)*N3+4*Q4
    H=2*n1*Q1*(1+3*(n1+Q1+n1*Q1)+2*(n1*n1+Q1*Q1))*N1+6*n2*Q2*(1+n2+Q2)*N2+2*n3*Q3*N3
    K1,K2,K3,K4=(v+q for v,q in zip(n,Q))
    S=N1*K1*K1*(1+K1)**2+N2*K2*(2*K2*K2+3*K2+1)+N3*K3*(1+K3)+4*K4
    assert K+G+H==S
    return K,G,H
count=0
for n in product(*[range(-q,3) for q in Q]):
    parts(n); count+=1
K,G,H=parts((0,0,0,0))
assert K==H==0 and G==144*N[0]+84*N[1]+6*N[2]+4
for n1 in (-3,-2,0,3):
    pi=F(22,7); xi=F(5,3); eta0=F(9,16); sqrteta=F(3,4); s=F(4,5); d=s*s
    alpha=F(1,10); ap=F(2,7); am=F(1,7); ratio=am/ap
    fac=(3/(pi*s),1-ratio,F(2),1-alpha/3,F(1),F(1),2*d,1+4*pi*alpha/(eta0*sqrteta),1+F(n1,3))
    chain=F(1)
    for f in fac: chain*=f
    phi=chain+8*(1-ratio)*alpha/(xi*xi)+4*ratio
    L=12*s/pi*(1-alpha/3)*(1+4*pi*alpha/(eta0*sqrteta))*(1+F(n1,3))+8*alpha/(xi*xi)
    assert phi==(1-ratio)*L+4*ratio
    assert ap*phi==(ap-am)*L+4*am
assert F(22,7)*27*4/F(50*50)<1
print('K/G/H exact checks:',count,'; Phi exact checks:',4,'; A36 bound passed.')
```

```python
from decimal import Decimal as D, localcontext

def atan_inv(q):
    z=D(1)/q; zz=z*z; power=z; total=z; n=0
    while True:
        power=-power*zz; n+=1
        nxt=total+power/(2*n+1)
        if nxt==total: return total
        total=nxt

def check(prec,profile):
    with localcontext() as c:
        c.prec=prec+18
        pi=D('3.1415926535') if profile=='printed_all' else 16*atan_inv(5)-4*atan_inv(239)
        eb=D('2.71828183') if profile=='printed_all' else D(1).exp()
        xi=(1+D(5).sqrt())/2 if profile=='golden_xi' else D('1.61803399')
        eta=lambda k,q: pi/(pi**4+(4+k)*q**4).sqrt().sqrt()
        eta0=eta(0,1); d=eta(1,1); s=d.sqrt(); a12=eta(1,2)
        A=lambda v: v.sqrt()*(1-v.sqrt())/(1+v.sqrt())
        rhs=9*(5*eta0+2*eta0.sqrt()+1)*(1-A(d)*A(a12))/(2*pi)**5
        alpha=(2*rhs*rhs/(1+(1-4*rhs*rhs).sqrt())).sqrt()
        a1=(1+s)/2; a2=1/d
        a3=1-alpha*xi**3*(1+s)**3/(3*d**3)-2*(xi*d).sqrt()/eb*((1-s)/(1+s))**2
        t=1-D(2)/3*xi*eta0*eta0*(1-eta0.sqrt())
        amp=t/(D(7)/3*eta0.ln()).exp()-1
        amm=t/(D(4)/3*eta0.ln()).exp()-1
        u=(-D(1)/3).exp(); W=27*a1+9*a2+2*a3+u
        vals={'alpha_bare':alpha,'alpha_mass_plus':amp,'alpha_mass_minus':amm,
            'a1':a1,'a2':a2,'a3':a3,'g':W,
            'K1_upper_gap':64*a1-W,'K2_upper_gap':7*a2-2*a3-u,'K3_upper_gap':a3-u,
            'XIII_gap_1':2*a3-1,'XIII_gap_2':9*a2-2*a3,'XIII_gap_3':27*a3-9*a2,
            'zone_gap_2':18*a2-6*a3,'zone_gap_3':162*a1-84*a2,
            'A36_den':1-pi*eb*(xi*eb)**2*alpha**2}
        assert amp>0 and all(vals[k]>0 for k in vals)
        assert 0<rhs<D('.5') and 0<alpha<D('.02')
        assert abs(-3*u.ln()-1)<D(10)**(-prec-12)
        c.prec=prec
        return {k:+v for k,v in vals.items()}

res={}
for profile in ('math_pi_e_printed_xi','golden_xi','printed_all'):
    res[profile]={p:check(p,profile) for p in (80,120)}
    print(profile)
    for k,v in res[profile][80].items(): print(k,format(v,'.22g'))
with localcontext() as c:
    c.prec=150
    err=max(abs(res[pr][80][k]-res[pr][120][k]) for pr in res for k in res[pr][80])
print('MAX80_120',err)
```

Ergebnis der Kontrollen: 720 exakte K/G/H-Zeugen, vier exakte
Phi-Faktorisierungen und die rationale A36-Schranke bestanden.
Je Profil wurden 16 Hilfs-/Abstandswerte bei 80/120 Stellen verglichen;
maximaler absoluter Unterschied kleiner 4.705e-79.
Im Hauptprofil sind alpha_bare=0.007296650307810962...,
ap=0.018322115073968862..., am=0.008128344940471468... und
alpha3=0.915211609598498951... . Diese Zahlen sind keine Massenwerte.
Die Dezimalpruefung ist eine Konvergenzkontrolle, keine
Intervallzertifizierung oder entsprechend genaue physikalische Vorhersage.

## 6. Reichweite und naechste Freigabe

Die konkrete Besetzung ist auf dem dokumentierten expliziten N0-Pfad
jetzt enger bestimmt als im vorigen Readiness-Stand. Das ersetzt weder
eine unabhaengige Herleitung aller AUX-Terme noch die Quellenfrage zur
abweichenden (XIV)-Zeile. Ein spaeterer Stufe-A-Rechner kann diesen
vorausgesetzten/selektierten Nullfall als eigenen, profilgebundenen
Rechenfall behandeln; Eingaben und alle Teilsummen bleiben sichtbar.
Die Fallidentifikation e- und die Wahl der Formelversion sind weiterhin
Voraussetzungen, keine daraus vorhergesagten Ergebnisse.

Keine alten Rechner, Inputs, Snapshots, Tests, Normalisierungen oder
Registereintraege wurden hier veraendert. Nur diese Review wurde
geschrieben; kein Commit. Der anschliessende ausdrueckliche Auftrag
erweiterte die Gegenpruefung um den inzwischen angelegten begrenzten
Rechner und die unabhaengige Massenauswertung im folgenden Abschnitt.

## 7. Unabhaengige Implementierungs- und Zahlengegenpruefung

Gelesen wurden der neue `scripts/audit_n0_electron.py`,
`tests/test_n0_electron.py`, `04_reconstruction/alpha_audit/n0_electron_inputs.json`
und `04_reconstruction/alpha_audit/NORM-N0-ELECTRON-AUDIT.md`.
Die neue ausdrueckliche Aliasentscheidung ist ein Nachtrag innerhalb
H006, keine eigene physikalische Identifikation verschiedener Quellen.

**Eigene Korrektur:** Bei der ersten Reduktion der dritten (XXXII)-Zeile
hatte diese Review einen falschen Polynomfaktor verwendet. Die erneute
Vollseitenansicht von Druck9 in Originalaufloesung bestaetigt
`alpha2*K2*(2*K2^2+3*K2+1)<=6*alpha1*K1^3`, also bei K2=3,K1=3
`84*alpha2<=162*alpha1`. Text und zweiter Codeblock wurden korrigiert
und nochmals ausgefuehrt. Der Hauptprofil-Abstand ist
76.43698627136012080339..., nicht der zuvor berechnete andere Ausdruck.
Dies war ein Fehler unserer Review, kein Fehler der Quelle; Root hatte
die korrekte Bedingung bereits im Rechner. Die angegebene maximale
80/120-Abweichung der 16 Diagnosefelder bleibt auch nach Korrektur gueltig.

### Getrennter Ausdruck und Ergebnis

Die Gegenrechnung importiert keine fremden Implementierungen der
Massenauswertung. Sie berechnet pi mit der Machin-Reihe und Wurzeln
mit Newton-Iteration. Fuer den Nullfall verwendet sie statt der
urspruenglichen K/G/H-Polynome

```text
G = 72*(1+sqrt(d)) + 56/d + 12*alpha3 + 4,
am = eta*(ap+1)-1,
M = mu*[ap*G+(ap-am)*L+4*am],
mu^12 = pi^7*hbar^10/(9*gamma_grav^2*c^6*s0^8).
```

Die positive zwoelfte Wurzel ist algebraisch dieselbe MU-Formel (VI),
nicht eine andere Massen-Normierung. Erst nach dieser eigenen
Auswertung werden Rechner und Snapshot zum Vergleich geladen.

| Vorher festgelegtes Profil | Unabhaengiges M in kg |
| --- | --- |
| math_pi_e_printed_xi | 9.0780174645164270975959155175409e-31 |
| golden_xi | 9.0780174666929055467614508127206e-31 |
| printed_all | 9.0780174653963532609812354595159e-31 |

Im Hauptprofil ergeben sich ausserdem

```text
mu       = 2.2590218742148826835518017235781e-31 kg,
G_aux    = 215.23862864700700097393097184836,
Phi_aux  = 4.0898222465431541334055693743294,
M_G      = 8.9087394815204765315709592173155e-31 kg,
M_Phi    = 1.6927798299595056602495630022547e-32 kg.
```

Dies sind Ausgaben des festgelegten historischen Formelfalls, keine
Eingaben aus beobachteten Teilchenmassen. Keine Umrechnung mit modernen
Konstanten, kein Messwertresiduum und keine passende Variantenwahl.

```python
from decimal import Decimal as D, localcontext
from pathlib import Path
import json
import sys
sys.path.insert(0,str(Path('scripts').resolve()))
import audit_n0_electron as candidate  # nur spaeterer Vergleich

def atan_inv(q):
    z=D(1)/q; power=z; total=z; j=0
    while True:
        power=-power*z*z; j+=1
        nxt=total+power/(2*j+1)
        if nxt==total: return total
        total=nxt

def root(x,n):
    assert x>0 and n>0
    y=D(10)**(x.adjusted()//n); old=None
    while True:
        nxt=((n-1)*y+x/y**(n-1))/n
        if nxt==y or nxt==old: return min(y,nxt)
        old,y=y,nxt

def independent(profile,precision):
    with localcontext() as c:
        c.prec=precision+24
        pi=D('3.1415926535') if profile=='printed_all' else 16*atan_inv(5)-4*atan_inv(239)
        eb=D('2.71828183') if profile=='printed_all' else D(1).exp()
        xi=(1+D(5).sqrt())/2 if profile=='golden_xi' else D('1.61803399')
        eta=lambda k,q: pi/root(pi**4+(4+k)*q**4,4)
        eta0=eta(0,1); d=eta(1,1); s=d.sqrt(); d12=eta(1,2)
        A=lambda x: x.sqrt()*(1-x.sqrt())/(1+x.sqrt())
        R=9*(5*eta0+2*eta0.sqrt()+1)*(1-A(d)*A(d12))/(2*pi)**5
        aa=(2*R*R/(1+(1-4*R*R).sqrt())).sqrt()
        t=1-D(2)/3*xi*eta0*eta0*(1-eta0.sqrt())
        h13=root(eta0,3)
        ap=t/(eta0*eta0*h13)-1
        am=eta0*(ap+1)-1
        a3=1-aa*xi**3*(1+s)**3/(3*d**3)-2*(xi*d).sqrt()/eb*((1-s)/(1+s))**2
        G=72*(1+s)+56/d+12*a3+4
        L=12*s/pi*(1-aa/3)*(1+4*pi*aa/(eta0*eta0.sqrt()))+8*aa/(xi*xi)
        Phi=((ap-am)*L+4*am)/ap
        hb=D('1.0545887e-34'); cc=D('2.99792458e8'); gg=D('6.6732e-11'); s0=D(1)
        mu=root(pi**7*hb**10/(9*gg**2*cc**6*s0**8),12)
        M=mu*(ap*G+(ap-am)*L+4*am)
        vals={'alpha':aa,'alpha_mass_plus':ap,'alpha_mass_minus':am,'a3':a3,
              'G_aux':G,'Phi_aux':Phi,'mu_kg':mu,'mass_kg':M,
              'G_contribution_kg':mu*ap*G,'Phi_contribution_kg':mu*((ap-am)*L+4*am)}
        c.prec=precision
        return {k:+v for k,v in vals.items()}

names=('math_pi_e_printed_xi','golden_xi','printed_all')
refs={pr:{p:independent(pr,p) for p in (80,120)} for pr in names}
fields=lambda r:{'alpha':D(r['alpha']),'alpha_mass_plus':D(r['alpha_mass_plus']),
    'alpha_mass_minus':D(r['alpha_mass_minus']),'a3':D(r['selection_coefficients'][2]),
    'G_aux':D(r['mass_terms']['G_aux']),'Phi_aux':D(r['mass_terms']['Phi_aux']),
    'mu_kg':D(r['mu_kg']),'mass_kg':D(r['mass_kg']),
    'G_contribution_kg':D(r['contribution_kg']['G']),'Phi_contribution_kg':D(r['contribution_kg']['Phi'])}
with localcontext() as c:
    c.prec=160
    conv=max(abs(refs[pr][80][k]-refs[pr][120][k])/abs(refs[pr][120][k]) for pr in names for k in refs[pr][80])
    errors=[]
    for prec in (80,120):
        actual=candidate.build_report(prec)
        for pr,row in zip(names,actual['profiles']):
            for k,v in fields(row).items():
                errors.append(abs(v-refs[pr][prec][k])/abs(refs[pr][prec][k]))
    snapshot=json.loads(candidate.OUTPUT.read_text(encoding='utf-8'))
    snap=max(abs(v-refs[pr][80][k])/abs(refs[pr][80][k]) for pr,row in zip(names,snapshot['profiles']) for k,v in fields(row).items())
    assert conv<D('1e-78') and max(errors)<D('1e-75') and snap<D('1e-75')
print('Independent80/120 max relative:',conv)
print('Script 60 field comparisons max relative:',max(errors))
print('Snapshot 30 field comparisons max relative:',snap)
for pr in names:
    print(pr)
    for k in ('G_aux','Phi_aux','mu_kg','mass_kg','G_contribution_kg','Phi_contribution_kg'):
        print(k,format(refs[pr][120][k],'.32g'))
```

Eigene 80/120-Konvergenz: maximaler relativer Unterschied <2.943e-80.
Gegen den Rechner wurden 60 Felder verglichen, gegen den 80-stelligen
Snapshot 30 Felder; jeweils maximaler relativer Unterschied <6.927e-78.
Die drei Review-Codebloecke wurden aus dieser Datei ausgefuehrt.

### Code-/Testbefund und Grenzen

- G, Phi, alpha3, mu und M entsprechen fuer die drei eingefrorenen Profile
  der unabhaengigen Rechnung und den geprueften lokalen Faktoren.
- XIII bleibt mit alpha3 am rechten Ende erhalten. XXXII verwendet im
  Rechner die richtige letzte Differenz 162*alpha1-84*alpha2.
- Der Polynomhelfer akzeptiert die erlaubten negativen Besetzungen;
  der Elektronpfad erzwingt nicht pauschal n_j>=0 fuer andere Zustaende.
- Domainkontrollen erfolgen vor der Nullstrukturreduktion. Das K4=1-
  Zertifikat ist auf W=g und K1..3=Q1..3 beschraenkt, keine generische
  Gleitkomma-Aufrundungsregel. Der rohe Dezimalwert und sein moeglich
  falscher Floor bleiben diagnostisch sichtbar.
- `python -B scripts/audit_n0_electron.py --check --verify-sources`
  bestand; die 12 zum Pruefzeitpunkt vorhandenen Tests bestanden.
  Kein beobachteter Rechenfehler im abgegrenzten Pfad.
- Empfohlen ist ein zusaetzlicher Regressionstest gegen die hier
  unabhaengig berechneten mu/G/Phi-Werte. Reine Eigenkonsistenz und
  80/120-Konvergenz wuerden einen gemeinsamen Vorfaktorfehler nicht
  sicher erkennen. Die Anker sind eigene Rechenergebnisse, keine
  experimentellen Zielwerte.
- Die Scriptformulierung "No empirical inputs" ist weiter als die
  tatsaechliche Grenze: Historische dimensionale Naturkonstanten sind
  vorgegeben. Praeziser ist "keine Teilchenmassenziele oder neuen
  experimentellen Vergleichseingaben". Dieser Wortlauthinweis wurde
  Root gemeldet; hier erfolgte kein Codeeingriff.

Abschliessender Follow-up: Root hat den unabhaengigen Zahlenankertest
fuer mu/G/Phi/M ergaenzt und den Scriptwortlaut auf "No particle-mass
targets" eingegrenzt. Beides wurde erneut gelesen; der Test verwendet
die eigenen Rechenanker, keine Messwerte. Neuer Lauf: 13 Tests OK sowie
Snapshot-/H006-Hashcheck OK. Alle drei Codebloecke dieser Review wurden
aus der Datei erfolgreich ausgefuehrt; `git diff --check` blieb ohne
Beanstandung. Keine beobachtete offene Rechenbeanstandung fuer die
drei eingefrorenen Profile; keine allgemeine Parameterraumgarantie.

Das positive Rechnergebnis hebt weder den lokalen XIV/XXVI-Unterschied
noch die Voraussetzungen, historischen Kalibrierungsfragen oder offenen
N>0-Beziehungen auf. Es ist nun ein reproduzierter, bedingter H006-N0-
Formelfall mit dokumentiertem Auswahlpfad, keine Gesamtvalidierung.
