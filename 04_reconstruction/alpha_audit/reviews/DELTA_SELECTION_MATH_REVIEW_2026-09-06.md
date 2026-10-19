# H013-Tabellenpaar (q,k)=(2,2): bedingte Auswahlpruefung

Stand: 2026-09-06. Unabhaengige Mathematikreview, Etappe 11.
Ausgangsstand laut Auftrag: `e50cab8`. Nur diese Reviewdatei wurde
geschrieben; keine Rechner, Inputs, Snapshots oder Git-Eintraege geaendert.

## Ergebnis und Quellenstatus

Fuer das als H013-Tabellenpaar uebergebene `(q,k)=(2,2)` gilt bei
woertlicher Auswertung der Buchformeln `B_2 < x < D_2`. Das Paar erfuellt
damit die vorgelagerte F/G-Positivitaet unter der angegebenen Identifikation,
aber weder die gegensinnig gedruckte V/Q-Ungleichung noch die gedruckte
B-Schranke. Die isolierten Maxima `k_max=2, q_max=3` widersprechen diesem
Paar dagegen nicht.

Dies ist keine eigene Quellenbildpruefung. Uebernommen wurden die Lesungen
aus `CONFIGURATION_SELECTION_SOURCE_REVIEW_2026-09-06.md`, insbesondere
Zeilen 50-51 und Abschnitt "Exact inequality path and the source-internal
break", sowie die algebraische Trennung aus
`CONFIGURATION_SELECTION_MATH_REVIEW_2026-09-06.md`, Abschnitte 1-3.
Quellort ist H004, EDM II, Druckseiten 268-269 / PDF-Folios 274-275.
Es gilt die abschliessend bestaetigte Lesung `Q2=sqrt(eta)` ohne Index q;
der fruehere zwischenzeitliche Lesefehler ist keine alternative Buchfassung.

Die H013-Zuordnung `(q,k)=(2,2)` ist eine Eingabe des Hauptagenten, kein
hier eigenstaendig bestaetigtes Tabellen- oder Glyphenurteil. H013 ist im
Quellenregister als undatierter autorbezeichneter Typoskriptscan gefuehrt,
nicht als nachgewiesenes 1989-Faksimile. Ob und in welchem Sinn die
Buch-Bedingung fuer diese Tabelle gelten soll, muss daher zusaetzlich
quellenseitig begruendet werden; das folgt nicht aus der Zahlenrechnung.

## 1. Voraussetzungen und exakte Algebra

Verwendet werden mathematisches pi, positive vierte Wurzeln, positive
ganzzahlige q,k und die Buchreihenfolge `(q,k)`. Alle folgenden Groessen
sind dimensionslos. Setze

```text
eta(q,k) = [1+(4+k)q^4/pi^4]^(-1/4),
e = eta(1,0),  a = eta(q,0),  b = eta(q,k),  x = 1/b,

V1 = a*x,                 V2 = (1+sqrt(a))^2/(4e),
Q1 = a^2/sqrt(e),         Q2 = sqrt(e),
R_VQ = V1+Q1-V2-Q2.
```

`R_VQ` ist unser Hilfsresiduum, nicht Heims relatives Delta in `L*Delta=k`
und keine Bezeichnung eines Teilchenzustands. Die gedruckte B-Funktion
und die unabhaengig aus V/Q hergeleitete D-Funktion lauten

```text
B_q = (1+sqrt(a))^2/(4ea) + sqrt(e) - a/sqrt(e),
D_q = (V2+Q2-Q1)/a
    = (1+sqrt(a))^2/(4ea) + sqrt(e)/a - a/sqrt(e).

R_VQ = a*(x-D_q),
D_q-B_q = sqrt(e)*(1/a-1) > 0.
```

Hier ist `0<a<=e<1`, also sind a, B und D positiv. Insbesondere ist
das Potenzieren der positiven Schranken ordnungserhaltend. Definiere

```text
u_B(q) = (pi/q)^4*(B_q^4-1)-4,
u_D(q) = (pi/q)^4*(D_q^4-1)-4.
```

Die drei Aussagen bleiben getrennt:

| Ebene | Praemissen/Aussage | Exakt aequivalent |
| --- | --- | --- |
| I | `F2-F1+G2-G1>0` zusammen mit `F_i=V_i, G_i=Q_i` | `-R_VQ>0`, also `x<D_q`, also `k<u_D(q)` |
| II | gedruckt `V1+Q1>V2+Q2` | `R_VQ>0`, also `x>D_q`, also `k>u_D(q)` |
| III | gedruckt `x<B_q` | `k<u_B(q)` |

I und II sind unter dieser Identifikation gegensaetzlich. Wegen `B_q<D_q`
impliziert III die Ebene I, waehrend die Umkehrung nicht gilt. II und III
sind unvereinbar. D und u_D sind diagnostische Umformungen, keine Auswahl
einer vermeintlich beabsichtigten Quellenkorrektur.

## 2. Unabhaengige Werte fuer (2,2)

Die folgenden Werte sind gerundete Ausgaben der 120-stelligen Rechnung:

| Groesse | Wert |
| --- | --- |
| e | 0.989989640819342375373108099937 |
| a = eta(2,0) | 0.881389504645664020958643426116 |
| b = eta(2,2) | 0.842423846102092834039733883054 |
| x | 1.187050918165498614832676546798 |
| B_2 | 1.186153558964637102879869715696 |
| D_2 | 1.320050473681827004970859999611 |
| u_B(2) | 1.963489198102715361385288774899 |
| u_D(2) | 8.397876839288775631793930569225 |

Die fuer die Entscheidungen relevanten Abstaende sind

```text
x-B_2  =  0.000897359200861511952806831102105676151404...,
x-D_2  = -0.132999555516328390138183452813270508893684...,
u_B(2)-2 = -0.036510801897284638614711225100720241499835...,
R_VQ   = -0.117224412354630171485396918524872977183141....
```

Damit ist I wahr (`-R_VQ>0`), II falsch und III falsch. Die gedruckte
Intervallbehauptung `2<u_2<3` waere mit k=2 vereinbar, ist aber fuer die
woertliche B-Funktion gerade nicht reproduzierbar. Das vorliegende Paar
zeigt ausserdem konkret, weshalb aus der Erfuellung von I nicht III folgt.

## 3. Reproduktion und Gegencheck

Der folgende Standardbibliothekscode berechnet pi unabhaengig ueber
Machins Formel und die Arkustangensreihe. Der vorhandene Rechner verwendet
stattdessen den Gauss-Legendre-Algorithmus. Die Wurzelfunktion wird hier
in normierter Form ausgewertet und D unmittelbar aus V2, Q2 und Q1
gebildet. Die zusaetzlichen 12 Arbeitsstellen sind Rundungsreserve,
keine zertifizierte Intervallarithmetik.

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
        def eta(q, k):
            return 1/(1+D(q)**4*(4+k)/pi**4).sqrt().sqrt()
        e, a, b = eta(1,0), eta(2,0), eta(2,2)
        x = 1/b
        V1, V2 = a*x, (1+a.sqrt())**2/(4*e)
        Q1, Q2 = a*a/e.sqrt(), e.sqrt()
        B = (1+a.sqrt())**2/(4*e*a)+(1-a/e)*e.sqrt()
        DD = (V2+Q2-Q1)/a
        R = V1+Q1-V2-Q2
        ub, ud = [(pi/2)**4*(z**4-1)-4 for z in (B,DD)]
        assert abs(R-a*(x-DD)) < D(10)**(-precision-7)
        assert abs(DD-B-e.sqrt()*(1/a-1)) < D(10)**(-precision-7)
        assert -R > 0 and R < 0 and B < x < DD and ub < 2 < ud
        values = dict(pi=pi, eta=e, eta_q=a, eta_qk=b, x=x,
            V1=V1, V2=V2, Q1=Q1, Q2=Q2, B_printed=B, D_from_VQ=DD,
            delta_VQ=R, u_B=ub, u_D=ud, x_minus_B=x-B, x_minus_D=x-DD,
            u_B_minus_2=ub-2, upstream=-R, D_minus_B=DD-B)
        ctx.prec = precision
        return {key:+value for key,value in values.items()}

results = {p:calculate(p) for p in (80,120)}
with localcontext() as ctx:
    ctx.prec = 140
    print('max abs 80/120:', max(abs(results[80][k]-results[120][k])
                                for k in results[80]))
for p, row in results.items():
    print(p, row)
```

Dieser Codeblock wurde als eigener Code ausgefuehrt. Der maximale absolute
80/120-Unterschied seiner 19 Werte ist kleiner als `3.50e-80`.
Die analytischen Identitaeten sind exakt; die numerischen Vorzeichen
wurden hochpraezise gegengeprueft, nicht mit Intervallarithmetik zertifiziert.

Zusaetzlich wurde `configuration(core.mathematical_pi(), q=2, k=2)` aus
`scripts/audit_configuration_selection.py` bei jeweils 80 und 120 Stellen
read-only aufgerufen. Je 13 gemeinsame numerische Felder wurden verglichen;
die maximalen absoluten Differenzen betragen `1.0e-78` bzw. `2.9e-118`.
Die 13 entsprechenden Felder des unveraenderten alten Snapshots weichen
von der unabhaengigen 80-stelligen Rechnung hoechstens um `1.0e-78` ab.
Alle fuenf Entscheidungsfelder der API und des Snapshots stimmen mit den
oben getrennt hergeleiteten Entscheidungen ueberein:

```text
upstream_positive_condition = true
printed_VQ_inequality = false
printed_eta_inequality = false
printed_k_bound = false
derived_upstream_k_bound = true
```

Ferner erfolgreich ausgefuehrt:
`python -B scripts/audit_configuration_selection.py --check --verify-sources`.
Der alte Snapshot stimmt weiterhin bytegetreu mit der eigenen Ausgabe des
alten Rechners ueberein; der konfigurierte H004-Quellhash ist unveraendert.
Keine Messwerte, Zielwertinversionen oder neuen Modellinputs wurden benutzt.

## 4. Logische Reichweite fuer das H013-Tabellenpaar

Ein quellenuebergreifender Konflikt erfordert zugleich die korrekte
H013-Paarlesung, die gleiche q/k-Bedeutung, die gleiche eta-Funktion und
die zusaetzliche Geltung der woertlichen strikten B-Bedingung fuer diese
Tabellenkonfiguration. Unter diesem Praemissenpaket ist das Paar mit
`k<u_B(q)` unvereinbar. Eine isolierte Mitgliedschaft in einer Tabelle
beweist dieses gesamte Praemissenpaket nicht.

Die Grenzen `q<=3, k<=2` aus den globalen Maxima sind lediglich
Einzelgrenzen; sie sind nicht mit der detaillierten Paarbedingung
`k<u_B(q)` gleichzusetzen. (2,2) erfuellt beide Einzelgrenzen. Ausserdem
bleibt eta(2,2) mathematisch definiert, auch wenn eine separat angesetzte
Auswahlbedingung dieses Paar ausschliesst.

Es wurde weder ein beabsichtigter Druckfehler ausgewaehlt noch ein
physikalisch zulaessiger oder unzulaessiger Zustand nachgewiesen. Die
bedingte F/G-Positivitaet allein ist keine vollstaendige Auswahltheorie.
Insbesondere waere die Aussage falsch, (2,2) scheitere an allen drei
hier untersuchten Bedingungen oder schon an den beiden globalen Maxima.
