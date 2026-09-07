# Externterm und Referenzwert: bedingte Fehlerfortpflanzung

2026-09-06, Etappe33. Eigene Algebra; keine neue Quellenlesung.
Gelesen: `06_docs/COUPLED_EXISTENCE_2026-09-06.md` und
`06_docs/EXPONENTIAL_CONTEXT_2026-09-06.md`. Die Quellenbruecke von einer
korrigierten Externfunktion zur Buchgleichung bleibt offen. Keine Parameter
aus (79), keine Masse, kein Y-Fit und keine physikalische Fehlerzahl werden
neu eingesetzt. Die folgenden deltas sind eigene Fehlerbezeichnungen,
nicht Heims Differenzoperator oder ein belegter Reparaturterm.

## 1. Exakte Identitaet unter ausdruecklich festen Groessen

Fuer jedes der zwei unveraenderten Buchprofile seien a1,a2,a3 und w fest,

```text
P(N)=a1*N1^3+a2*N2^2+a3*N3, B=27*a1+9*a2+2*a3,
e(n)=exp(-n/3), w=1+d*A16>0, W=w*(B+e(1)),
R_old(N)=P(N)+e(N4)-W.
```

Nur BEDINGT werde derselbe NORMALISIERTE Externterm an beiden Stellen
ersetzt: `e(n) -> e(n)+delta(n)`, mit `delta(0)=0`. Dann gilt exakt

```text
W_new = W+w*delta(1),
R_new = R_old+delta(N4)-w*delta(1).
```

Die einseitige Rechnung `R_old+delta(N4)` laesst die Referenzaenderung weg
und beschreibt damit eine andere Annahme. Ein gemeinsamer positiver Fehler
muss den Residuen deshalb nicht auf beiden Rechenwegen dieselbe Richtung geben.
Bei N4=1 sind die beiden delta-Werte zwingend IDENTISCH:
`DeltaR=(1-w)*delta(1)`. Sie duerfen dann nicht unabhaengig variiert werden.
Bei N4=0 ist hingegen `DeltaR=-w*delta(1)`.

### Nachgetragene, mitgeteilte Quellenstruktur mit Nullreferenz

Root teilte nach Vollseitenlesung H004 Druck322/323 die Struktur
`Delta=mu_plus*(exp(-A*N4)-1)` und den ergaenzenden konstanten Beitrag
`alpha4*delta4G4=1` mit. Diese Glyphenlesung wird hier uebernommen, nicht
als eigene visuelle Quellenpruefung ausgegeben. Die Trennung von Nullpunkt0
und Geruestbesetzung Q4=1 ist fuer die bedingte Algebra wesentlich.

Fuer eine ROHE Korrektur `F(n)=e(n)+h(n)` und unveraenderte mu_plus,a_i
sowie den konstanten Beitrag1 lautet der mitgeteilte Anschluss

```text
T_new = P+1+F(N4)-F(0),
g_new = B+1+F(1)-F(0),       W_new=w*g_new,
R_new-R_old = h(N4)-w*h(1)+(w-1)*h(0).
```

Da e(0)=1, ist dies genau die vorherige Zweipunktform mit der EFFEKTIVEN
Korrektur `delta(n)=h(n)-h(0)`. Ein konstantes Roh-h verschwindet vollstaendig!
Eine nichtnullkonstante delta auf dem ganzen Bereich verletzt dagegen
delta(0)=0 und ist ein anderer Vertrag. Gleiche delta-Werte an zwei
Nichtnullargumenten sind hiervon zu unterscheiden. Auch diese normalisierte
Fortsetzung von einer unbekannten F-Funktion bleibt bedingt, keine aus
(79) bereits hergeleitete Korrekturfunktion.

Die eigene Et32-Intervallkette wurde erneut ohne Root-Import ausgefuehrt.
Fuer beide Profile ist mit `w=1+d*A16` rational zertifiziert:

```text
73.1277926806 < w < 73.1277926811.
```

Diese Einhuellung bezeichnet den festen dimensionslosen Multiplikator,
keine physikalische Fehlertoleranz. Die konkrete Kontrolle verwendete die
im eigenen Et32-Block erzeugten Intervalle `own['d']` und `own['A16']` und
pruefte die beiden strikten rationalen Ungleichungen am ganzen Produktintervall.

## 2. Was die alte uniforme Luecke sichert und was nicht

Sei D die Menge mit N1,N2,N3 ganzzahlig>=0, N4 reell>=0 und den ersten
beiden ungewichteten Gates. Et32 beweist auf D
`abs(R_old)>=L`, `L=0.057144067635` (exakt rational).
NICHT gemeint sind beliebige gate-verletzende Elemente einer Integerbox.

Mit `DeltaR=delta(N4)-w*delta(1)` folgen:

- Eine uniforme Schranke `abs(DeltaR)<=E<L` auf D ist HINREICHEND fuer
  `abs(R_new)>=L-E>0`, also fuer den fortbestehenden Ausschluss.
- Eine wirkliche Nullstelle benoetigt am betreffenden Tupel exakt
  `DeltaR=-R_old`, insbesondere `abs(DeltaR)=abs(R_old)>=L`.
  Diese Groessenbedingung ist NOTWENDIG, fuer sich nicht hinreichend.
- Aus einer verfuegbaren oberen Fehlerschranke `E>=L` folgt lediglich,
  dass diese grobe Robustheitskontrolle nicht entscheidet. Daraus folgt
  weder eine Nullstelle noch die Erlaubnis, einen passenden Fehler zu waehlen.
- Bei allein bekannter nichtstrikter Luecke `abs(R_old)>=L` muss die
  allgemeine ausreichende Bedingung strikt `E<L` lauten. Bei Gleichheit
  kann ein abstrakter Grenzfall verschwinden; er muss es nicht.

Genauer sei C_N die durch eine deklarierte ZULAESSIGE Funktionsfamilie
erreichbare Menge der Werte `delta(N4)-w*delta(1)`. Robuster Ausschluss fuer
alle diese Funktionen ist genau aequivalent zu
`-R_old(N) not in C_N` fuer jedes N in D. Eine aeussere Intervallhuelle von
C_N liefert eine hinreichende Ausschlusspruefung; Einschluss von `-R_old`
in der Huelle ist ohne Erreichbarkeitsbeweis keine Loesungsaussage.

Quantorgrenze: Die Fehlerkontrolle muss auf der ganzen betrachteten Menge
gelten. Die Et32-Box, insbesondere N4<=25 im vollen Integerzweig, wurde mit
der UNVERAENDERTEN Energiegleichung hergeleitet. Nach einer Aenderung von W
darf sie nicht ungeprueft als neuer Such-/Fehlerbereich dienen. Eine nur auf
[0,25] begruendete Korrekturschranke benoetigt auch neue korrigierte
Besetzungsgrenzen; alternativ genuegt eine globale Schranke fuer N4>=0.

## 3. Vorzeichen, Intervalle und Korrelation

Bei festem w>0 und `delta(N4) in [lN,uN]`, `delta(1) in [lr,ur]` gilt

```text
DeltaR in [lN-w*ur, uN-w*lr].
```

Das ist immer eine aeussere Huelle. Sie ist als erreichbares Intervall nur
dann vollstaendig, wenn die beiden Werte innerhalb des deklarierten Modells
unabhaengig sein duerfen (insbesondere nicht automatisch bei N4=1).
Fuer ein exakt bekanntes R_old und tatsaechlich unabhaengige, frei erreichbare
Intervalle ist `-R_old` in diesem Intervall notwendig UND hinreichend fuer
eine algebraisch moegliche Nullstelle an diesem Tupel, nicht fuer einen
physikalischen Heim-Zustand oder eine aus der Quelle abgeleitete Korrektur.

Fuer N4=1 mit `delta(1) in [l,u]` ist stattdessen die skalierte Huelle
`[(1-w)*u,(1-w)*l]` exakt, da hier w>1. Weitere Korrelationen koennen die
Transportgroesse ebenfalls stark reduzieren: `delta(N4)=w*delta(1)` ergibt
DeltaR=0. Fuer gleiche Werte c an den beiden Nichtnullargumenten ergibt
sich (1-w)*c, wobei delta(0)=0 separat erhalten bleiben muss. Ein auf ALLEN
Argumenten konstantes Roh-h ergibt stattdessen genau null.

Die fuenf Et32-Faelle haben bekannte Vorzeichen: Faelle1 und3 sind positiv,
Faelle2,4,5 negativ. Bei `R_old>=m>0` genuegt `inf DeltaR>-m`; bei
`R_old<=-m<0` genuegt `sup DeltaR<m`. Das kann wesentlich schaerfer sein
als ein Absolutbudget. Vorzeichen werden nicht aus einer unsignierten
relativen Fehlerangabe erraten.

Aus `abs(delta(N4))<=epsilon_N`, `abs(delta(1))<=epsilon_ref` folgt grob
`abs(DeltaR)<=epsilon_N+w*epsilon_ref`. Mit einer gemeinsamen unbekannten
Schranke epsilon genuegt somit `(1+w)*epsilon<L`; bei unsicher eingeschlossenem
w kann die sichere Obergrenze von w verwendet werden. KEINE solche physikalisch
begruendete epsilon-Schranke wird durch diesen algebraischen Satz geliefert.
Fuer signierte Referenzintervalle und ein w-Intervall sind alle Eckprodukte
von w*delta(1) zu beachten, statt unbesehen immer w_max einzusetzen.

Bei ROHEN Fehlerbudgets sind drei miteinander verbundene Werte zu beachten.
Fuer w>1 liefert eine unabhaengige aeussere Huelle

```text
DeltaR in [lN-w*u1+(w-1)*l0, uN-w*l1+(w-1)*u0],
abs(DeltaR) <= epsilon_N+w*epsilon_1+(w-1)*epsilon_0.
```

Beides ist ohne Korrelationswissen nur konservativ. Am Argument0 oder1
fallen Werte zusammen; bei konstantem Roh-h ist die exakte Aenderung null,
obwohl die Dreiecksgrenze positiv sein kann. Eine Schranke fuer h selbst
darf nicht unbesehen als gleich grosse Schranke fuer h(n)-h(0) benutzt werden.

## 4. Weitere Aenderungen und die offene (79)-Bruecke

Falls auch Koeffizienten und w geaendert werden, seien
`dP=sum da_j*N_j^(4-j)` und `dB=27*da1+9*da2+2*da3`. Dann ist exakt

```text
DeltaR = dP+delta(N4)-w*(dB+delta(1))
         -dw*(B+e(1)+dB+delta(1)).
```

Dies schliesst die gemischten Terme ein; sie werden nicht als vernachlaessigbar
deklariert. Veraenderte Strukturgates oder eine andere Zustaendsmenge erfordern
zusaetzlich einen neuen Bereichsnachweis. Auch ein korrigierter e-Referenzterm
ist nicht von einer behaupteten neuen Normierung unabhaengig zu behandeln.

Et9 lieferte fuer eine erklaerte skalare (79)-Abbildung einen relativen
Asymptotenrest, abhaengig von r,lambda,a,b und einer festen Normierung.
Das ist noch keine additive delta(N4)-Schranke: Es fehlen die Zuordnung
r(N4), Parameterwerte/zulassungen, Amplitude und gemeinsame Referenznormierung.
Eine gross-r-Asymptotik ist insbesondere keine uniforme Fehlerkontrolle an
allen endlichen Besetzungen inklusive Nullpunkt0 und Referenz1. Falls ERST
eine gemeinsame NORMALISIERTE
relative Darstellung `e_new(n)=e(n)*(1+rho(n))` begruendet waere, folgte
`DeltaR=e(N4)*rho(N4)-w*e(1)*rho(1)`. Diese Identitaet ersetzt die fehlende
Quellenbruecke und die benoetigten Fehlerschranken nicht; die Normierung
verlangt dann rho(0)=0. Fuer eine rohe relative Korrektur muss der
Nullpunktterm `(w-1)*h(0)` stattdessen mitgefuehrt werden.

## 5. Selbstenthaltener exakter Kontrollblock

Die Bruchwerte in den folgenden Tests sind eigene Algebrazeugen. Das Spiel-
Beispiel `v(n)=2^(-n)` ist KEINE Auswertung von exp(-n/3), kein Heim-Pfad
und kein Ersatz fuer den Buchinput. P/B/w werden fuer diese Zeugen frei als
Rechensymbole gesetzt; es wird keine Quellengleichung auf eine Zielmasse angepasst.

```python
from fractions import Fraction as F
from itertools import product

checks = 0
def check(condition):
    global checks
    assert condition
    checks += 1

def residual(P, B, w, vn, vr):
    return P+vn-w*(B+vr)

def transport(w, dn, dr):
    return dn-w*dr

def signed_box(w, nbox, rbox):
    ln, un = nbox; lr, ur = rbox
    assert w > 0 and ln <= un and lr <= ur
    return ln-w*ur, un-w*lr

def samples(box):
    lo, hi = box
    return (lo, (lo+hi)/2, hi)

# Exact identity at independent formal input slots (not exp evaluations).
for P, B, w, vn, vr, dn, dr in product(
        (F(1), F(3, 2)), (F(2), F(1, 3)), (F(2), F(73)),
        (F(1, 4), F(2, 3)), (F(1, 2),),
        (F(-1, 10), F(1, 5)), (F(-1, 20), F(1, 10))):
    old = residual(P, B, w, vn, vr)
    new = residual(P, B, w, vn+dn, vr+dr)
    check(new-old == transport(w, dn, dr))

# Toy v(n)=2**(-n), n=2, reference=1. Preserve the separate value v(0)=1.
# Equal normalized changes at n=1,2, but delta(0)=0, act differently.
P, B, w, vn, vr = F(2), F(1), F(2), F(1, 4), F(1, 2)
old = residual(P, B, w, vn, vr)
c = F(1, 4)
check(old == -F(3, 4))
check(old+c == -F(1, 2))             # Only the left side changed.
check(residual(P, B, w, vn+c, vr+c) == -1)  # Shared function changed.
check(transport(w, F(1, 5), F(1, 10)) == 0)
check(transport(w, -F(1, 5), -F(1, 10)) == 0)

# Raw corrections require normalization at argument zero.
v0 = F(1)
for hn, h1, h0 in product((F(-1, 10), F(1, 5)), repeat=3):
    new = P+1+(vn+hn)-(v0+h0)-w*(B+1+(vr+h1)-(v0+h0))
    raw_change = hn-w*h1+(w-1)*h0
    check(new-old == raw_change)
    check(raw_change == transport(w, hn-h0, h1-h0))
for common_offset in (F(-1, 3), F(0), F(2)):
    new = P+1+(vn+common_offset)-(v0+common_offset) \
          -w*(B+1+(vr+common_offset)-(v0+common_offset))
    check(new == old)
check(transport(w, F(0), c) == -w*c)  # N4=0, delta(0)=0.

# Signed rectangles: endpoint image and interior containment.
for nbox, rbox in product(((F(-1, 5), F(1, 10)), (F(1, 10), F(1, 5))),
                          ((F(-1, 10), F(1, 20)), (F(1, 20), F(1, 10)))):
    lo, hi = signed_box(w, nbox, rbox)
    images = [transport(w, dn, dr) for dn, dr in product(samples(nbox), samples(rbox))]
    check(min(images) == lo and max(images) == hi)
    check(all(lo <= value <= hi for value in images))

# Shared argument N4=1: not two independent correction values.
eps = F(1, 10)
for same_error in (-eps, F(0), eps):
    check(transport(w, same_error, same_error) == (1-w)*same_error)
    check(abs(transport(w, same_error, same_error)) <= abs(1-w)*eps)
check(abs(1-w)*eps < (1+w)*eps)
# Triangle bound is attainable for independent, oppositely signed values.
check(transport(w, eps, -eps) == (1+w)*eps)

# Equality of an abstract gap and its error budget can allow cancellation.
toy_gap = F(1, 10)
check(toy_gap+transport(w, -toy_gap, F(0)) == 0)
# Large budget does not itself imply a root: direction matters.
check(abs(transport(w, F(1), F(1))) > abs(old))
check(old+transport(w, F(1), F(1)) != 0)

# w interval with signed reference errors: all four product corners.
wbox, rbox, nbox = (F(2), F(3)), (F(-2), F(-1)), (F(0), F(1))
products = [wv*rv for wv, rv in product(wbox, rbox)]
lo, hi = nbox[0]-max(products), nbox[1]-min(products)
for wv, nv, rv in product(samples(wbox), samples(nbox), samples(rbox)):
    check(lo <= transport(wv, nv, rv) <= hi)

# General formula including changes of both polynomial coefficients and w.
for dP, dB, dw, dn, dr in product((F(-1, 4), F(1, 3)), repeat=5):
    new = residual(P+dP, B+dB, w+dw, vn+dn, vr+dr)
    exact_change = dP+dn-w*(dB+dr)-dw*(B+vr+dB+dr)
    check(new-old == exact_change)

# Purely logical robust-gap statement; these are NOT sourced error budgets.
L = F('0.057144067635')
for R in (-2*L, -L, L, 3*L):
    for change in (-L/2, F(0), L/2):
        check(abs(R+change) >= L-L/2 > 0)
print(checks, 'exact algebra controls; no physical epsilon, mass or fitted term.')
```

Der unveraenderte obige Block wurde mit `py -3.13 -B -` eigenstaendig
ausgefuehrt: 179 exakte Bruchkontrollen bestanden, Exitcode0. Er importiert
keinen Projekt-Rechner oder Testhelfer. Die Identitaeten, Vorzeichenhuellen,
Nullpunkt-/Referenzkorrelationen und die Rolle der strikten Robustheitsgrenze
sind damit zusaetzlich an den deklarierten synthetischen Werten geprueft.
Der Zahlwiederholung fuer w lag dagegen ausdruecklich die schon dokumentierte
eigene Et32-Intervallkette zugrunde, kein erfundener synthetischer Buchparameter.

Die Funktionalform und Fehlerschranke einer wirklichen Externkorrektur sind
damit nicht rekonstruiert. Ohne diese Quellenbruecke wird weder der alte
bedingte Ausschluss aufgehoben noch seine physikalische Robustheit bewiesen.
Nur diese neue eigene Review wurde geschrieben; alte Rechner, Profile,
Snapshots, Tests, Normalisierungen und Register wurden nicht geaendert.

## 6. Begrenzte Code- und Testgegenreview

`scripts/audit_external_error_transport.py` und
`tests/test_external_error_transport.py` vollstaendig gelesen. Die rohe
Gewichtszerlegung summiert Koeffizienten auf identischen Argumenten vor der
Auswertung; Nullgewichte werden entfernt. Dadurch sind insbesondere n=0,
n=Referenz und w=1 korrekt. Die Punktintervallbilder verwenden fuer positive
und negative Gewichte die richtigen Endpunkte, auch bei 0<w<1. Andere
funktionale Korrelationen werden ausdruecklich nicht als frei erreichbar
ausgegeben. Die effektive Zweipunktfunktion verlangt delta(0)=0 als externe
Vertragsbedingung; sie besitzt selbst keinen Argumentparameter, mit dem sie
diese Bedingung ueberpruefen koennte.

Die erweiterte `joint_change`-Form enthaelt die d_w*d_B- und d_w*delta_ref-
Terme korrekt; g_old muss hierbei die alte normalisierte Referenzsumme sein.
`robust_gap` liefert bei Budget>=L bewusst kein Urteil und behauptet keine
Nullstelle. `fixed_book_factors` prueft nur die unveraenderten zwei Profile,
ihre alte Luecke und w-Einschluesse, nicht eine physikalische Fehlerschranke.

Selbst ausgefuehrt, beide erfolgreich:

```text
py -3.13 -B scripts/audit_external_error_transport.py --check
py -3.13 -B -m unittest discover -s tests -p test_external_error_transport.py -v
  16 Tests bestanden, Exitcode0.
```

Keine materiellen Algebrafehler gefunden. Die Tests unterscheiden rohe und
normalisierte Fehler, belegen die Null-/Referenzkorrelation und enthalten
einen ausdruecklich synthetischen Zeugen fuer die fehlende Folgerung von
lokaler auf globale Fehlerkontrolle. Der neue Teilertest ist mathematisch
korrekt unter seinen eigenen Praemissen 0<z<15, z teilt15 und z/15>1/15;
er laesst z=3,5 uebrig. Eine eigene neue Glyphen- oder Vollstaendigkeitspruefung
der dazugehoerigen Quellenannahmen erfolgte in dieser Codegegenreview nicht.

Ein Vertragswortlaut in der CLI-Ausgabe wurde Root zur Praezisierung gemeldet:
Direkt nach der rohen h-Formel nennt die Ausgabe das Zweipunktbudget ohne
ausdruecklichen Bezug auf normalisierte delta=h-h(0). Das Rechenergebnis
ist korrekt; der Text sollte die Budgetart benennen, damit er nicht als
unvollstaendige rohe Dreipunktfehlerschranke gelesen wird. Root-Dateien
wurden auch fuer diese Meldung nicht geaendert.
