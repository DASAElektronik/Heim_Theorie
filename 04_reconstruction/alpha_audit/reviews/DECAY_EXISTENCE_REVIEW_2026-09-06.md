# Gekoppelte A-Sensitivität: endliche Existenzmengen (2026-09-06)

## Auftrag, Vertrag und Ergebnis

Geprüft wurde der vorab festgelegte Vier-Zellen-Vertrag aus
`00_admin/DECAY_SENSITIVITY_PLAN.md` und
`04_reconstruction/alpha_audit/decay_sensitivity_inputs.json`:

```text
2 feste Alpha-Profile x { A(k=1)=1/3, A(k=1)=1/5 }.
E_A(n)=exp(-A n),   B=27a1+9a2+2a3,
g_A=B+E_A(1),       W_A=w*g_A.
```

`A(k=1)=1/3` ist die unveränderte Buchwahl; `1/5` ist ausschließlich die
vorab definierte eigene z3-Sensitivität. In jeder Zelle werden Externterm
und Gerüstreferenz gemeinsam geändert. Die alte `N4<=25`-Box wird nicht
übernommen: dieselbe numerische Obergrenze entsteht unten neu aus den
jeweiligen positiven Koeffizienten, `W_A` und den direkten ungewichteten
Gates.

Für die so erhaltene endliche Obermenge enthält kein zertifiziertes
Residuenintervall der exakten ganzzahligen Gleichung null. Auch in der
explizit engeren, nichtphysischen Realdiagnose des Inputs
`0<=N4<=N3-1` gibt es keinen Nullpunkt. Das ist eine bedingte
Rechen-/Vertragsaussage, weder eine Massenrechnung noch eine physikalische
Korrektur des Buchs.

## Getrennte Gleichungen und Domänen

Die geprüfte Gleichung ist für jede Zelle

```text
R_A(N)=a1*N1^3+a2*N2^2+a3*N3+E_A(N4)-W_A = 0.
```

Für den ganzzahligen Test gilt nur der im Input fixierte direkte,
ungewichtete Überbereich

```text
N1,N2,N3,N4 in Z_>=0,
N1^3 > G2(N2),  N2^2 > G3(N3),  N3 > N4.
```

`G2(m)=m(m+1)(2m+1)/6` und `G3(m)=m(m+1)/2` sind hier die aus dem
früher geprüften Buchanschluss verwendeten monotonen Gittergrößen. Die
zweite Ordnungsreihe/Zentralbedingung und die gewichtete Sigma-Aussage
`beta4=alpha3*N3-N4>0` werden **nicht** in dieses eine Prädikat
eingemischt. Sie können einen Kandidaten nur weiter einschränken; der
folgende Ausschluss benutzt sie nicht.

Die zusätzlich geforderte Realdiagnose lässt nur `N4` reell und hält
`0<=N4<=N3-1`. Sie ist eine eigene, integerzellgebundene Relaxation. Sie
ist nicht die volle reelle Fortsetzung von `N3>N4`, die `0<=N4<N3` wäre;
ein Nichtfund im hier festgelegten engeren Intervall darf nicht als
Nichtfund in diesem ausgelassenen letzten Einheitsintervall ausgegeben
werden.

## Neue endliche Obermenge

Die folgenden rationalen, nach außen gerichteten Eingaben wurden pro Zelle
aus den fest gebundenen Buchformeln zertifiziert; die gemeinsamen Schranken
sind ein Ergebnis der vier Einzelprüfungen, kein Rückgriff auf die alte
Suchbox:

```text
a1 > 249/250,   a2 > 1,   a3 > 489/500,   0 < E_A(n) <= 1,
W_A < 2840.
```

Zur Anzeige liegen die vier `W_A` ungefähr bei

| Alpha-Profil | A=1/3 | A=1/5 |
| --- | ---: | ---: |
| `book_eq105_y3_1` | 2830.2632576681 | 2837.7368773117 |
| `book_printed_alpha_sensitivity` | 2830.2632576642 | 2837.7368773077 |

Die Dezimalwerte sind nur Darstellung. Der Bereichsschluss selbst verwendet
die vorstehenden rationalen Intervallgrenzen. Aus `R_A=0`, positiver
Exponentialterm und positiven Koeffizienten folgt

```text
a1*N1^3 < W_A,
N1^3 < 2840/(249/250) = 710000/249 < 15^3.
```

Also `N1<=14`. Das erste strikte Gate und die Monotonie von `G2` liefern

```text
G2(N2) < N1^3 <= 14^3 = 2744,
G2(20)=2870 > 2744,  also N2<=19.
```

Analog gibt das zweite Gate

```text
G3(N3) < N2^2 <= 19^2 = 361,
G3(27)=378 > 361,  also N3<=26.
```

Schließlich folgt nur für den **ganzzahligen** Vertrag aus `N3>N4` und
`N4>=0` die frische Grenze `0<=N4<=25`. Sie ist damit keine still
wiederverwendete alte Abschneidung. Die direkte Obermenge enthält nach
Anwendung dieser drei Gates 9.231 Integerquadrupel; die zugehörige
Realdiagnose umfasst 1.239 zulässige `(N1,N2,N3)`-Tripel mit dem jeweiligen
Intervall `N4 in [0,N3-1]`.

## Zertifizierter Ausschluss in den vier Zellen

Für die Exponentialwerte wurden rationale Taylor-Einschlüsse für
`exp(A)`, anschließend Kehrwert- und Potenzintervalle für
`E_A(n)=exp(-A n)` verwendet. Jedes Kandidatresiduum wurde als
nach-außen-gerundetes rationales Intervall ausgewertet. Ein Intervall, das
null nicht enthält, entscheidet hier den Nichtgleichheitsbefund ohne eine
numerische Akzeptanztoleranz.

### Reproduzierbarer unabhängiger Kontrollweg

Der nachstehende, ausgeführte Kontrollblock importiert **nicht** den neuen
Etappe-35-Rechner und auch kein `certbook_intervals`. Er verwendet nur die
bereits vorhandene, eigenständige Bruchintervall-Hilfe
`scripts/audit_coupled_existence.py`: `Interval` (Skala `10^40` und
auswärtige Bruchrundung), `exp_positive_bounds`, `book_intervals`,
`load_inputs`, `G2`, `G3`. `book_intervals/load_inputs` binden dabei
transparent den alten kanonischen Buchinput; die zwei neuen A-Werte werden
unten ausschließlich aus dem neuen, vorab gelesenen Sensitivitätsvertrag
eingesetzt. Insbesondere ist `B` aus dem alten `g` durch Abzug seines
ursprünglichen `exp(-1/3)` rekonstruiert, nicht aus einer Root-Ausgabe
übernommen.

```python
# Run from repository root: py -3.13 -
import sys
from fractions import Fraction as F
sys.path.insert(0, "scripts")
import audit_coupled_existence as base

rows = base.book_intervals(base.load_inputs())
e13 = base.exp_positive_bounds(F(1, 3)).reciprocal()
cells = (("heim_z5", F(1, 3), e13),
         ("counterfactual_z3", F(1, 5),
          base.exp_positive_bounds(F(1, 5)).reciprocal()))

def score(interval):
    assert not (interval.lo <= 0 <= interval.hi)
    return min(abs(interval.lo), abs(interval.hi))

for row in rows:
    B = row["g"] - e13
    w = 1 + row["eta11"]*row["A16"]
    for name, A, e1 in cells:
        W = (B + e1)*w
        assert W.hi < F(2840)
        e = [base.exp_positive_bounds(A).reciprocal()**n for n in range(27)]
        integer_count = triple_count = 0
        best_integer = best_contract = best_full = None
        for N1 in range(15):
            for N2 in range(20):
                if not N1**3 > base.G2(N2):
                    continue
                for N3 in range(1, 27):
                    if not N2**2 > base.G3(N3):
                        continue
                    P = row["a1"]*N1**3 + row["a2"]*N2**2 + row["a3"]*N3
                    triple_count += 1
                    # Contract range: 0 <= N4 <= N3-1.
                    contract_lo, contract_hi = P+e[N3-1]-W, P+e[0]-W
                    assert contract_hi.hi < 0 or contract_lo.lo > 0
                    for endpoint in (contract_lo, contract_hi):
                        candidate = (score(endpoint), (N1, N2, N3), endpoint)
                        best_contract = candidate if best_contract is None or candidate[0] < best_contract[0] else best_contract
                    # Extra only: full direct real gate 0 <= N4 < N3.
                    full_limit, full_hi = P+e[N3]-W, P+e[0]-W
                    assert full_hi.hi < 0 or full_limit.lo > 0
                    for endpoint in (full_limit, full_hi):
                        candidate = (score(endpoint), (N1, N2, N3), endpoint)
                        best_full = candidate if best_full is None or candidate[0] < best_full[0] else best_full
                    for N4 in range(N3):
                        R = P+e[N4]-W
                        integer_count += 1
                        candidate = (score(R), (N1, N2, N3, N4), R)
                        best_integer = candidate if best_integer is None or candidate[0] < best_integer[0] else best_integer
        assert (integer_count, triple_count) == (9231, 1239)
        print(row["profile"], name, best_integer, best_contract, best_full)
```

Die Ausführung ergab in jeder der vier Zellen die oben tabellierten
nullfreien Integerintervalle, nullfreie Endintervalle im Vertragsbereich
und nullfreie Endintervalle im zusätzlichen vollen Realbereich. Die
ausgegebenen Bruchobjekte sind der reproduzierbare Zertifikatsgegenstand;
gerundete Dezimalzahlen im Haupttext dienen nur der Lesbarkeit.

| Alpha-Profil | A(k=1) | kleinster zertifizierter Abstand von 0 | Zeuge des kleinsten Abstands |
| --- | ---: | ---: | --- |
| `book_eq105_y3_1` | 1/3 | > 0.0571440750 | `(14,9,12,0)` |
| `book_printed_alpha_sensitivity` | 1/3 | > 0.0571440702 | `(14,9,12,0)` |
| `book_eq105_y3_1` | 1/5 | > 0.9432492549 | `(14,10,1,0)` |
| `book_printed_alpha_sensitivity` | 1/5 | > 0.9432492589 | `(14,10,1,0)` |

Dies sind diagnostische Minimalabstände innerhalb der vorab festgelegten
vier Zellen, keine Güte- oder Auswahlmetrik. Insbesondere wird nicht aus
dem größeren Abstand ein bevorzugter `A`-Wert abgeleitet.

Für die Realdiagnose ist bei festem `(N1,N2,N3)` die Funktion

```text
N4 -> a1*N1^3+a2*N2^2+a3*N3+exp(-A*N4)-W_A
```

bei `A>0` streng fallend. Daher genügt die Prüfung der beiden Grenzen
`N4=0` und `N4=N3-1`; keines der 1.239 Tripel besitzt ein einschließendes
Vorzeichenintervall. Die im Integerfall oben genannten unteren Abstände
sind zugleich die kleinsten Randabstände dieser engeren Realdiagnose.

### Zusätzliche mathematische Stärkung: volle direkte Realgrenze

Ohne den Eingabevertrag zu ändern, wurde zusätzlich die tatsächlich direkte
reelle Fortsetzung des dritten Gates betrachtet:

```text
0 <= N4 < N3.
```

Für jedes der gleichen 1.239 Tripel wurde wegen der strengen Monotonie der
Funktionswert bei `N4=0` und sein linksseitiger Grenzwert bei
`N4↑N3` geprüft. Der zweite Wert ist rechnerisch
`P(N1,N2,N3)+exp(-A*N3)-W_A`; er ist ein Grenzwert, nicht ein zugelassener
zusätzlicher Integer- oder Realpunkt. Kein Tripel hat zwischen beiden
zertifizierten Endwerten einen Vorzeichenwechsel oder einen Endwert, dessen
Intervall null enthält. Damit existiert auch in diesem größeren offenen
Intervall kein reeller Nullpunkt.

Die kleinsten zertifizierten Endabstände betragen dabei für `A=1/3` weiter
mehr als `0.0571440702` (am Wert `N4=0` bei `(14,9,12)`); für `A=1/5`
mehr als `0.7619800080` (am Grenzwert `N4↑1` bei `(14,10,1)`). Diese
Zusatzprüfung ist eine eigene analytische Verstärkung des direkten Gates,
keine Änderung der vertraglich gespeicherten engeren Realdiagnose und keine
physikalische Behauptung.

## Reichweite und offene Grenzen

- Der Nachweis betrifft die gemeinsame Formeländerung `E_A` und `g_A/W_A`
  bei sonst festem jeweiligem Alpha-Profil. Ein nur links geänderter
  Externterm wäre ein anderer, hier nicht getesteter Vertrag.
- Die vier Zustandsräume sind absichtlich Übermengen bezüglich der nicht
  verwendeten zweiten Reihe und (107b). Daraus folgt ein Ausschluss für
  deren Schnittmenge, aber keine Deutung dieser Bedingungen als identisch.
- Die vertragliche Realdiagnose ist wegen ihres Eingabeintervalls enger als
  die volle `0<=N4<N3`-Relaxation und keine physikalische Zustandsmenge.
  Die vorstehende Zusatzprüfung deckt die volle direkte Realgrenze nur als
  eigene mathematische Verstärkung ab.
- Die Rechnung liefert keine aus (79b)/(79c) abgeleitete Fehlerfunktion,
  keine Wahl zwischen den A-Profilen und keine Aussage über Masse,
  Messwerte oder eine autorisierte Buchkorrektur.

Nur diese neue Reviewdatei wurde erzeugt; alte Rechner, Eingaben,
Normalisierungen, Snapshots und Register blieben unverändert.
