# Eta22: unabhaengige Zahlen- und Bedeutungsreview

Stand: 2026-09-06. Begrenzte mathematische Gegenpruefung von eta_22 in
der 1989-B59-Fassung; keine neue Quellbildkontrolle, keine neuen Messdaten,
kein Fit und keine Aenderung eines Rechenprofils. Quellen-/Versionsrahmen:
`CONFIGURATION_DEPENDENCY_REVIEW_2026-09-06.md`, besonders Abschnitt 5,
sowie die vorhandene Implementierung `scripts/audit_alpha.py`.

Die uebergebene Quellenlesung verortet eta_22 in B59, H007 Druck18/PDF9;
die eta-/vartheta-Rueckverweisung steht auf Druck12/PDF3. Hier wird das
bestehende Profil `1989_source_cross_reference` mit mathematischem pi
und explizit `(q,k)=(1,2)` fuer eta_12 untersucht.
Die Bezeichnung 1989 meint hier die dokumentierte IGW-Ueberlieferung,
nicht ein in dieser Review authentifiziertes Manuskriptfaksimile von 1989.

## 1. Definition, Domaene und exakte Beziehungen

Fuer die betrachteten nichtnegativen ganzen q,k gilt

```text
eta(q,k) = [1+(4+k)*q^4/pi^4]^(-1/4),
eta = eta(1,0),
eta_11 = eta(1,1), eta_12 = eta(1,2),
eta_21 = eta(2,1), eta_22 = eta(2,2).
```

Die positive vierte Wurzel ist eindeutig. Fuer q>0 gilt 0<eta(q,k)<1;
fuer q=0 ist der Faktor 1. Saemtliche hier betrachteten Groessen sind
dimensionslos. Diese mathematische Definitionsmenge ist nicht schon die
Menge physikalisch zulaessiger Konfigurationen einer bestimmten Quellfassung.

Insbesondere folgen exakt, ohne Dezimalrechnung,

```text
eta_12^(-4)-1 = 6/pi^4,
eta_22^(-4)-1 = 96/pi^4
             = 16*(eta_12^(-4)-1),

eta_22/eta_12 = [(pi^4+6)/(pi^4+96)]^(1/4).
```

Der Faktor 16 betrifft die um 1 verminderten inversen vierten Potenzen,
nicht eta_22 oder eta_12 selbst. Fuer positives pi liegt der Quotient
eta_22/eta_12 strikt zwischen 1/2 und 1. Aus den Zusatzzahlen
4,5,6,80,96 im Nenner folgt ausserdem

```text
1 > eta > eta_11 > eta_12 > eta_21 > eta_22 > 0.
```

Die gleichen beiden Indizes von eta_22 machen seinen numerischen Wert
gegen einen blossen Tausch der Indexreihenfolge invariant. Das klaert
nicht automatisch seine physikalische Bedeutung und beseitigt nicht
die unterschiedliche eta_12-Lesung anderer Quellfassungen.

## 2. Unabhaengige Zahlen

pi wurde unabhaengig vom bestehenden Gauss-Legendre-Rechner durch die
Machin-Identitaet

```text
pi = 16*atan(1/5)-4*atan(1/239)
```

und alternierende Potenzreihen berechnet. Die folgenden Werte verwenden
mathematisches pi, nicht den gedruckten kurzen pi-Wert einer anderen
Auswertungsvariante. Angezeigt werden nur so viele Stellen wie fuer den
Vergleich sinnvoll; gerechnet wurde mit 80 und 120 Stellen, jeweils
zwoelf internen Schutzstellen.

| Groesse | Wert |
|---|---:|
| eta | 0.989989640819342375373108099937 |
| eta_11 | 0.987563988106123590308672244886 |
| eta_12 | 0.985167763578005187445930281087 |
| eta_21 | 0.860807227989261570130831714773 |
| eta_22 | 0.842423846102092834039733883054 |
| eta_22/eta_12 | 0.855106995221316996119076567457 |

Die Gleichung mit den inversen vierten Potenzen ist analytisch exakt.
Ihr etwa `9e-91` grosses Residuum in der 80-plus-12-Stellen-Rechnung
ist lediglich Rundungsrest, kein Quellen- oder Modellfehler.

## 3. B59-Faktoren und die rein algebraische Zerlegung

Fuer die festgehaltene 1989-Fassung seien

```text
S = [(1-sqrt(eta))/(1+sqrt(eta))]^2,
P_den = eta*eta_11*eta_12,
C0 = S/P_den,
C_prime = (1+eta_22)*C0,
K_alpha = 1-C_prime.
```

Das hier quellennahe K_alpha ist der dimensionslose Korrekturfaktor
1-C_prime. Es ist nicht das frueher fuer die Energiebilanz verwendete
K=alpha_prime*(1-C). Ebenso sind C_prime und C0 nicht der ungestrichene
Korrelationsfaktor oder die sonstigen C-Symbole anderer Quellkontexte.

| Groesse | Wert |
|---|---:|
| S | 0.000006326204016092086731851842725 |
| P_den | 0.963176964882420586279623017712 |
| (1+eta_22)/P_den | 1.91286120129233565362118344507 |
| C0 | 0.000006568059917072825102479037548 |
| eta_22*C0 | 0.000005533090296769482235992479169 |
| C_prime | 0.000012101150213842307338471516717 |
| K_alpha | 0.999987898849786157692661528483 |

Es gilt unmittelbar

```text
C_prime = C0 + eta_22*C0.
```

Der Anteil des zweiten Summanden an dieser gewaehlten Darstellung ist

```text
(eta_22*C0)/C_prime = eta_22/(1+eta_22)
                  = 0.457236725351964556000163918575....
```

Das sind etwa 45.7237 Prozent dieses algebraischen Korrekturkoeffizienten,
nicht ein Anteil an Alpha, einer Masse, einer Energie oder einer
physikalischen Wahrscheinlichkeit. Aus der Distributivitaet folgen keine
zwei physikalischen Kanaele, keine unabhaengigen Prozesse und keine
Autoreninterpretation der Summanden.

### Sensitivitaet mit klarer Festhaltebedingung

Ersetzt man nur eta_22 formal durch einen unabhaengigen Platzhalter z und
haelt eta,eta_11,eta_12 fest, so ist

```text
C_prime(z) = C0*(1+z),
dC_prime/dz = C0.
```

Bei z=eta_22 kann dies als partielle Sensitivitaet
`partial C_prime/partial eta_22=C0` geschrieben werden. Es ist kein
Nachweis, dass eta_22 im Quellenmodell frei veraenderbar waere: Im hier
festgelegten Profil sind alle eta-Faktoren durch dieselbe Definition
und mathematisches pi bestimmt. Eine totale Ableitung bei Aenderung von
pi oder anderen gemeinsamen Grundlagen enthaelt weitere Terme.
Es wurde keine solche Parameteraenderung, Zielwertinversion oder
Unsicherheitsanpassung vorgenommen.

## 4. Getrennter Vergleich mit dem A1*A2-Produkt

Nur fuer den ausdruecklich festgehaltenen Buchindexfall seien

```text
A1 = sqrt(eta_11)*(1-sqrt(eta_11))/(1+sqrt(eta_11)),
A2 = sqrt(eta_12)*(1-sqrt(eta_12))/(1+sqrt(eta_12)),
P_Buch = A1*A2.
```

Dies ist die A1*A2-Struktur der aelteren Alpha-Gleichung mit der geklaerten
Buchreihenfolge (q,k). Sie wird hier nicht nachtraeglich zur woertlichen
Lesung von IGW1982(V) erklaert. Dessen source-literal-Profil verwendet
fuer den als eta_12 beschrifteten Faktor die andere Indexzuordnung.
Keines der bestehenden Profil-IDs oder ihrer historischen Auditstatus
wird umbenannt oder korrigiert.

Die Zahlen des festgelegten Vergleichs lauten

```text
A1 = 0.00310897254432996057870897804339...,
A2 = 0.00370800735463179605121631913148...,
P_Buch = 0.0000115280930597238214052306081859...,

C_prime-P_Buch = 0.000000573057154118485933240908530762...,
C_prime/P_Buch = 1.04970962249780924885497675136....
```

Die relative Differenz von etwa 4.971 Prozent betrifft nur die beiden
kleinen Korrekturkoeffizienten, nicht eine entsprechende Aenderung des
Alpha-Werts. Eine Gleichheit der Formeln oder physikalischen Mechanismen
folgt daraus ebenso wenig wie eine Verbesserung gegen einen Messwert.

Zum reinen API-Abgleich wurde noch der gemeinsame Vorfaktor
`alpha_prime=9*(5eta+2sqrt(eta)+1)/(2pi)^5` benutzt. Die rechten Seiten
der beiden festgelegten Gleichungen sind

```text
rhs_1989 = alpha_prime*(1-C_prime)
         = 0.00729715611612592092893687701231...,
rhs_Buch = alpha_prime*(1-P_Buch)
         = 0.00729716029786404183551702379250....
```

Es wurden keine Zweige geloest, keine inversen Zielwerte eingesetzt und
keine experimentellen Referenzen fuer diesen Vergleich importiert.

## 5. eta22 ist berechenbar; Zustandszulaessigkeit ist eine andere Aussage

Die einzelne nachgerechnete Buch-Bedingung k<u_q liefert bei positiven
ganzen q,k die Menge `{(1,1),(1,2),(2,1),(3,1)}`. Das Paar (2,2) liegt
nicht in dieser Menge. Die mathematische eta-Funktion ist an (2,2)
trotzdem definiert. Eine Einschraenkung einer Zustandsmenge macht eine
ausserhalb ausgewertete analytische Funktion nicht automatisch undefiniert.

Aus dem Auftreten von eta_22 in B59 allein folgt weder, dass die
1989-Fassung einen realisierten Zustand (2,2) beansprucht, noch dass
sie lediglich einen unphysikalischen Hilfswert meint. Beides waere eine
zusaetzliche Bedeutungszuschreibung. Ein Konflikt mit der Buchauswahl
braeuchte zugleich eine belegte Uebernahme genau dieser Auswahlregel in
die 1989-Fassung und die entsprechende reale Zustandsbedeutung des Faktors.
Diese beiden Bruecken werden hier nicht vorausgesetzt oder bewiesen.

Die neue Rechnung bestaetigt die eindeutig definierte numerische
Abhaengigkeit des festgelegten B59-Profils. Sie loest weder den
u_2-Zahlenbefund noch die Indexkollision der 1982-Ueberlieferung, und sie
ist kein Ersatz fuer einen Quellenbeleg zur Bedeutung von eta_22.

## 6. Kurzer reproduzierbarer Standardbibliothekscode

Auszufuehren aus dem Projektroot als eigener temporaerer Python-Aufruf,
beispielsweise ohne Bytecode-Ausgabe. Der Code schreibt keine Dateien.
Die ersten Funktionen sind vom bestehenden Rechner unabhaengig;
erst der letzte Block importiert gezielt dessen reine Formel-API.

```python
from decimal import Decimal as D, localcontext

def atan_inv(n):
    z = D(1)/n
    power, total, j = z, D(0), 1
    while True:
        new = total + power/j
        if new == total:
            return total
        total, power, j = new, -power*z*z, j+2

def calculate(precision):
    with localcontext() as ctx:
        ctx.prec = precision+12
        pi = 16*atan_inv(5)-4*atan_inv(239)
        eta = lambda q, k: 1/(1+(4+k)*D(q)**4/pi**4).sqrt().sqrt()
        e, e11, e12, e21, e22 = (eta(q,k) for q,k in
                               ((1,0),(1,1),(1,2),(2,1),(2,2)))
        theta = 5*e+2*e.sqrt()+1
        S = (1-e)**2/(1+e.sqrt())**4
        C0 = S/(e*e11*e12)
        Cp = C0*(1+e22)
        A = lambda z: z.sqrt()*(1-z)/(1+z.sqrt())**2
        a1, a2 = A(e11), A(e12)
        base = 9*theta/(2*pi)**5
        result = dict(pi=pi, eta=e, vartheta=theta, eta11=e11,
            eta12=e12, eta21=e21, eta22=e22, ratio=e22/e12, S=S,
            prefactor=(1+e22)/(e*e11*e12), C0=C0, summand=e22*C0,
            C_prime=Cp, K_alpha=1-Cp, share=e22/(1+e22),
            A1=a1, A2=a2, P_book=a1*a2, rhs=base*(1-Cp),
            rhs_book=base*(1-a1*a2), Cprime_gap=Cp-a1*a2,
            Cprime_ratio=Cp/(a1*a2))
        ctx.prec = precision
        return {key: +value for key,value in result.items()}

low, high = calculate(80), calculate(120)
with localcontext() as ctx:
    ctx.prec = 140
    assert max(abs(low[k]-high[k]) for k in low) < D('1e-78')
for key,value in low.items():
    print(key, value)

import sys
sys.path.insert(0, 'scripts')
import audit_alpha as api
for precision in (80,120):
    own = calculate(precision)
    with localcontext() as ctx:
        ctx.prec = precision
        pi = api.mathematical_pi()
        old89 = api.equation_rhs(pi,
            dict(equation='1989', eta12_k=2, eta12_q=1))
        old82 = api.equation_rhs(pi,
            dict(equation='1982', eta12_k=2, eta12_q=1))
        errors = [abs(old89[k]-own[k]) for k in old89]
        errors += [abs(old82[k]-own[k]) for k in ('A1','A2')]
        errors += [abs(old82['A1']*old82['A2']-own['P_book']),
                   abs(old82['rhs']-own['rhs_book'])]
        assert max(errors) < D(10)**(10-precision)
        print(precision, len(errors), max(errors))
```

Die Umformungen in S und A rationalisieren `1-sqrt(eta)` und sind
algebraisch identisch, aber nicht einfach kopierte Aufrufketten des
bestehenden Rechners. Auch die pi-Algorithmen sind verschieden.

## 7. Ergebnis der Gegenpruefung

Die unabhaengige 80/120-Rechnung aller berechneten Faktoren einschliesslich
des Korrekturquotienten stimmte mit groesster absoluter Differenz kleiner
als `4.2e-80` ueberein. Im alten API wurden je Praezision zwoelf Felder
kontrolliert: acht 1989-Zwischengroessen/rechte Seite und vier A1/A2-
Vergleichswerte. Groesste absolute Abweichungen waren `4e-80` bei
80 Stellen und `1e-119` bei 120 Stellen; die verwendeten Toleranzen
waren `1e-70` beziehungsweise `1e-110`.
Der in Abschnitt 6 abgedruckte Code wurde anschliessend selbst unveraendert
aus dem Markdown-Codeblock ausgefuehrt und bestaetigte diese API-Abstaende.

Nur `equation_rhs` und der mathematische pi-Helfer des alten Rechners
wurden aufgerufen, nicht dessen Reportbuilder oder Vergleichsdatenteil.
Keine modernen Messwerte, Zweigloesungen, Zielwertinversionen oder
Parameterfits wurden verwendet. Kein neuer Rechner und kein neuer
Snapshot wurden angelegt; alle acht alten Rechner, Inputs und Snapshots
blieben durch diesen Auftrag unveraendert. Nur diese eigene Reviewdatei
wurde geschrieben; kein Commit.

Abschluss: Die angegebenen mathematischen eta22- und B59-Abhaengigkeiten
sind reproduziert. Kein Zahlen- oder Algebrafehler in dem festgelegten
1989-Profil gefunden. Die physikalische/konfigurationelle Bedeutung von
eta22 bleibt die ausdruecklich getrennte Quellenfrage.
