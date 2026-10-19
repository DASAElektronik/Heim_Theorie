# Strukturbehandlung in H010: unabhaengige statische Kontrollflussreview

2026-09-06, Etappe 31, Ausgang `2ae50af`. Nur statische Quellenlekture und
eigene synthetische skalare Kontrollen; kein historisches Programm kompiliert,
importiert oder ausgefuehrt. Keine neuen Massen, Messwerte oder Konstantenprofile.
`00_admin/SOURCE_ATTRIBUTION.md` erneut vollstaendig gelesen.

## 1. Quellen und genaue Reichweite

H010 ist die vorhandene Archivkopie `01_sources/heim_primary/massformula.zip`.
Die beiden Texte bezeichnen sich als spaetere Transkriptionen/Portierungen
eines Schulz-Programms. Diese Selbstangaben sind kein unabhaengiger Beweis,
dass jede Programmzeile von Heim stammt oder eine Buchkorrektur autorisiert ist.
Pascal nennt Mueller2001 und Posdzech2006; C nennt zusaetzlich den Port
durch leovinus2006 (jeweils Kopfzeilen3-8; C-Versionsnotiz36-39).

Neu gelesene SHA-256 der unveraenderten Dateien:

| Kurzname | Lokaler Pfad | SHA-256 |
|---|---|---|
| Archiv | `01_sources/heim_primary/massformula.zip` | `8D29EAE202B9C85D3E2A19203A760E2581680D330A2C3AC601F2D73EB1E00AFE` |
| C | `01_sources/heim_primary_unpacked_untrusted/massformula/C 0.66/gprog_0.66.c` | `29CBF3EBC197EFC8044C2C34D71AB40DD7C6F6829368A412812C7868A287B7B0` |
| Pascal | `01_sources/heim_primary_unpacked_untrusted/massformula/Pascal 0.62/GPROG 0.62c.PAS` | `1C1D60DC68F0EB540AA0E061896EF03559E3F57846D1E8A3AA28563694CDC59C` |

Alle folgenden C/Pascal-Zeilen beziehen sich auf diese Dateien. GBASE,
GSTRUC, GMASS, GLIMIT und die vollstaendigen direkten Aufrufwege im
Hauptprogramm wurden gelesen. Dateiweite Suchen ergaenzten die Pruefung
aller GSTRUC-Aufrufe, K/n-Zuweisungen und moeglicher Strukturvergleiche.
C-Ausgabesammlung und Nachvergleich wurden ebenfalls auf Rueckwirkung geprueft.
Die Konstanten-/Matrixformeln werden nicht als neue Buchinputs uebernommen.

Die Programmvariablen k1..k4 sind die Gesamtbesetzungen K_j=n_j+Q_j;
sie entsprechen nicht den kleinen n_j und nicht der Resonanzvariablen n.
Negative n_j allein sind daher kein unzulaessiger Zustand. Ein negatives
K_j wuerde dagegen die vorausgesetzte nichtnegative Gesamtbesetzung verletzen.

## 2. Tatsachlicher GSTRUC-Kontrollfluss

| Schritt | C-Zeilen | Pascal-Zeilen | Statischer Befund |
|---|---|---|---|
| f(N), W1 | 898,910 | 458,464 | W1=wgx*(1+fn), jeweils aus vorgegebenen Eingaben neu berechnet. |
| K1, RestW2 | 911-923 | 465-470 | Kubikwurzel integerisiert; ein K1^3-Problem fuehrt zu Meldung, in C auch assert. |
| K2, RestW3 | 924-928 | 471-474 | Quadratwurzel integerisiert; kein Vergleich mit einem G3-Wert. |
| K3, RestW4 | 929-935 | 475-478 | Linearer Quotient integerisiert; keine K2-Ruecksetzung. |
| W4<=0 | 937-938 | 482 | K4 aus integerisiertem alpha3*K3; auch negative Rundungsreste werden so behandelt. |
| W4>0 | 939-941 | 483 | K4 aus integerisiertem Logarithmus, ohne vorgaengige obere Kappe. |
| W4>1 | 942-949 | 484-490 | Genau ein K3--, dann Addition des integerisierten alpha3*K3-NACHwerts zu bereits integerisiertem K4. |
| Ende | 953-979 | 492-512 | n4=K4-Q4, Diagnoseausgabe, normale Rueckkehr ohne kontrollflusswirksame Gueltigkeitssperre. |

Im Transfer wird W4 nicht neu berechnet. Der Code bewahrt auch nicht erst
einen reellen W5/W6 bis zum Abschluss: Er addiert zwei bereits integerisierte
Terme. Ein wiederholter Buchtransfer mit Rohwertkappe ist hier nicht vorhanden.
Es gibt weder vor K3-- ein K3>0-Gate noch danach ein K3/K4>=0-Gate.

Insbesondere wird nirgendwo in dieser Routine die direkte Buchbedingung
K2^2>K3*(K3+1)/2 ausgewertet. Auch die uebrigen ungewichteten (107)/(107a)-
Gates und die zweite Differenzreihe werden hier nicht als Akzeptanzbedingungen
geprueft. Das Auftreten des Dreieckspolynoms in GMASS ist eine Berechnung
des Beitrags, kein Test: C998-1000 bzw. Pascal524.

Der Zweig W4>1 ist keine Ersatzpruefung fuer K2^2>G3. Auch fuer Zone3->4
fehlen allgemeine Vergleiche K4<=alpha3*K3, alpha3*K3-K4>0 oder >=1.
Die Zuweisung bei W4<=0 ist nur eine Fallbehandlung, kein solcher Nachtest.
Der K1^3-Assert in C920 ist kein Strukturgate. Vollstaendige Endlichkeits-,
Radikanden- und Integerueberlaufguards sind nicht vorhanden; reales
Laufzeit-/Compilerverhalten bei ungueltiger Arithmetik wurde nicht getestet.

## 3. Rundung ist hier eine konkrete Implementierungsentscheidung

C63-70 aktiviert per `#if 1` ROUND=ROUND2=myround. C469-499 verwendet
epsilon=1e-7: bei negativem x wird epsilon abgezogen, sonst addiert;
anschliessend wird gegen null abgeschnitten. Die im else-Zweig genannte
Pascal-Konfiguration ist in dieser Dateifassung nicht aktiv.

Pascal465/471/475/482/483/488 verwendet dagegen `trunc(x+1e-10)`.
Die vermeintliche FORTRAN-ROUND-Routine auf112-134 steht in einem Kommentar,
nicht in einem aktiven Funktionskoerper. Fuer positive Werte sind dies
unterschiedliche Promotionsabstaende; fuer negative Werte zudem verschiedene
Richtungen. Formal etwa C(-2)=-2, Pascal(-2)=-1 unter diesen expliziten
Epsilonoperationen und exakter anschliessender Trunkierung.

Diese Mathematik illustriert die geschriebenen Operationen. Sie zertifiziert
keinen bestimmten historischen Compiler, seine Fliesskommadarstellung oder
die quellenoffene Buch-Messbarkeitsschwelle. Keine der beiden Schwellen wird
deshalb als neue autorisierte Buch-TRC-Regel uebernommen.

## 4. Meldung, Aufrufer und Fehlerpfade

Pascal setzt am Routineanfang msg='' (455), bei W4>1 unabhaengig vom
korrigierten Ergebnis msg='Resonance not allowed!' (489). Das ist kein
Abbruch. Beide Caller rufen danach GMASS auf (723/724 und742/743) und
geben Ergebnis samt msg aus (727 bzw.747). Es gibt dort keine if-msg-
Akzeptanzentscheidung und keine Rueckspruenge zur Auswahl.

C meldet denselben Fall nur bei print>1 (948-949); der Dateidefault
print=1 (50) zeigt diese Meldung nicht. Nach normaler Rueckkehr folgen
GMass und Roh-Ausgabe ebenfalls ohne Gueltigkeitspruefung (1250-1265,
1290-1309). Der Befund bedeutet nicht, dass jeder arithmetische Fehler
zurueckkehren muss: Ein aktivierter Assert oder eine Laufzeitstoerung kann
frueher abbrechen. Aber die ausdrueckliche Verbotsmeldung selbst sperrt nicht.

Die C-Sammlung addParticle (332-375) ordnet Ergebnisse nach Deskriptoren
zu, kann Duplikate auslassen und unbekannte Eintraege aus Ausgabegruenden
nicht aufnehmen. Der Nachvergleich evaluate (378-406) berechnet Ausgabedifferenzen.
Weder dort noch im Caller wird ein G_j-Gate nachgetragen oder eine neue
Besetzung erzeugt. Eine Aufnahme in die finale Tabelle ist deshalb nicht
mit struktureller Akzeptanz gleichzusetzen; umgekehrt ist ein Auslassen
wegen Deskriptor/Duplikat kein Strukturausschluss.

## 5. GLIMIT enthaelt verwandte Grenzalgebra, aber keinen Zustandsfilter

GLIMIT wird erst nach der N=0-Auswahl, GMASS und deren Ausgabe aufgerufen
(C1268-1281; Pascal730-734). Die Routine setzt lme bzw. die spaetere obere
Resonanzordnung. Fuer N>=2 ruft der Caller GSTRUC/GMASS danach ohne
individuelle Strukturkontrolle auf. Keine K_j<=L_j+Q_j-Nachpruefung steht dort.

Es waere trotzdem falsch, pauschal keinerlei Strukturalgebra in GLIMIT zu
behaupten. C1046-1065 und Pascal562-581 konstruieren Grenzkandidaten.
Mit eigenen Abkuerzungen M_j=L_j+Q_j entsprechen die reellen Ausgangsformen
vor ihrer jeweiligen Integerisierung den GEWICHTETEN Randgleichungen

```text
alpha2*G2(M2) = alpha1*M1^3,
alpha3*G3(M3) = alpha2*M2^2,
M4 = alpha3*M3.
```

Der erste Schritt L1 benutzt das zuvor berechnete kgh+fig (C1044/Pascal560).
Aus L_j konstruiert GLIMIT eine skalare Grenze fuer f(N) und lme
(C1071-1099/Pascal586-603); das ist keine Reparatur des aktuellen Tupels.
Gewichtete Grenzgleichungen an L sind nicht die ungewichtete lokale
(107)-Pruefung an K. Ebenso ist die berechnete globale Resonanzgrenze kein
Beweis, dass jedes darunter ausgegebene Tupel die lokalen Gates erfuellt.

Selbst ein gueltiges oberes Tupel wuerde dazu nicht genuegen: Der eigene
exakte Zeuge U=(5,4,3,2) hat ungewichtete Bandbreiten (95,10,1), aber das
komponentenweise kleinere K=(4,2,3,2) hat (59,-2,1). Sinkt die vorherige
Zone bei gleichbleibend grosser Folgezone, kann ein Gate verletzt werden.
Dies ist eine allgemeine skalare Gegenkontrolle, keine Aussage, dass GLIMIT
diese beiden konkreten Tupel in einem historischen Programmlauf erzeugt.

## 6. Eigene begrenzte Kontrollfluss-Zeugen

Der selbstenthaltene Fraction-Block bildet nur die benoetigten arithmetischen
Faelle nach. Kein importierter Quelltext und keine Vollsimulation. Logwerte
werden durch rationale atanh-Reihenintervalle mit expliziter Restschranke
integerisiert; alle benutzten Intervalle liegen eindeutig in derselben Zelle.
Die synthetischen Koeffizienten und W-Werte sind keine Heim-/Teilcheninputs.

```python
from fractions import Fraction as F

checks = 0
def check(condition, label):
    global checks
    assert condition, label
    checks += 1

def policy(x, language):
    x = F(x)
    if language == 'C':
        eps = F(1, 10**7)
        return int(x-eps if x < 0 else x+eps)
    assert language == 'Pascal'
    return int(x+F(1, 10**10))

def log_bounds(value, terms=48):
    value = F(value)
    assert value > 0
    t = (value-1)/(value+1)
    total = 2*sum((t**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    tail = 2*abs(t)**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    return (total, total+tail) if t >= 0 else (total-tail, total)

def last_stage(m, a, rest, lam, language):
    # Deliberately no extra positivity/cap/rejection gate absent from this path.
    m, a, rest, lam = int(m), F(a), F(rest), F(lam)
    assert m >= 0 and a > 0 and lam > 0
    warning_case = False
    if rest <= 0:
        k4 = policy(a*m, language)
    else:
        lo, hi = log_bounds(rest)
        xlo, xhi = -hi/lam, -lo/lam
        lower, upper = policy(xlo, language), policy(xhi, language)
        check(lower == upper, 'certified integerized log cell')
        k4 = lower
        if rest > 1:
            m -= 1
            k4 += policy(a*m, language)
            warning_case = True
    return m, k4, warning_case

def beta_unweighted(tup):
    a, b, c, d = tup
    return (F(a**3)-F(b*(b+1)*(2*b+1), 6),
            F(b*b)-F(c*(c+1), 2), F(c-d))

for language in ('C', 'Pascal'):
    # Root's fresh synthetic example; no book-profile replay.
    remaining, numbers = F(145, 2), []
    for power in (3, 2, 1):
        m = 0
        while (m+1)**power <= remaining:
            m += 1
        # Positive-root rounding is away from either printed epsilon threshold.
        check((F(m+1)-F(1, 10**7))**power > remaining,
              'root remains below next-integer promotion threshold')
        remaining -= m**power
        numbers.append(m)
    check(tuple(numbers) == (4, 2, 4) and remaining == F(1, 2), 'first-three toy')
    m, k4, warning = last_stage(4, 1, remaining, F(1, 3), language)
    check((m, k4, warning) == (4, 2, False), 'ordinary path, no warning')
    check(beta_unweighted((4, 2, m, k4)) == (59, -6, 2), 'unweighted gate fails')
    check(k4 < m, 'even last-zone cap would pass this toy')

    m, k4, warning = last_stage(1, 1, F(1, 2), F(1, 3), language)
    check((m, k4, warning) == (1, 2, False), 'ordinary branch lacks upper cap')
    check(k4 > m, 'weighted cap violated at a=1 without warning')

    m, k4, warning = last_stage(1, 2, F(3, 2), F(1, 3), language)
    check((m, k4, warning) == (0, -1, True), 'transfer can leave negative total K4')

    check(last_stage(1, 1, 0, F(1, 3), language) == (1, 1, False),
          'zero-rest assignment does not handle zero beta collapse')
    w3 = 1-F(1, 10**11)
    promoted = policy(w3, language)
    check(promoted == 1 and w3-promoted < 0, 'promotion can make negative W4')
    check(last_stage(promoted, 1, w3-promoted, F(1, 3), language)
          == (1, 1, False), 'negative rounding rest enters <=0 case')

check(policy(-2, 'C') == -2 and policy(-2, 'Pascal') == -1,
      'negative integer epsilon rules differ')
upper, lower = (5, 4, 3, 2), (4, 2, 3, 2)
check(all(a <= b for a, b in zip(lower, upper)), 'componentwise smaller')
check(beta_unweighted(upper) == (95, 10, 1), 'valid upper tuple')
check(beta_unweighted(lower) == (59, -2, 1), 'invalid lower tuple')
print('Exact synthetic control checks:', checks)
```

Diese Zeugen zeigen mathematisch, warum die gelesenen Operationen allein
keinen vollstaendigen Strukturfilter ergeben. Sie sind keine Behauptung,
dass ein bestimmter ueberlieferter Binarlauf diese Eingaben benutzt hat.
Die fehlende Caller-Sperre ist ein separater statischer Befund der gelesenen
Anweisungen, keine durch ein erfundenes Rueckgabeflag simulierte Tatsache.

## 7. Enges Ergebnis

In diesen beiden H010-Fassungen wurde kein versteckter aktueller
ungewichteter (107)/(107a)-Filter und kein strukturbedingter Ruecksprung
zu K2 oder K1 gefunden. Der einzige ausdrueckliche K3-Rueckschritt haengt
an W4>1, nicht an der in Etappe30 verletzten Zone2->3-Bedingung.
GLIMIT liefert verwandte gewichtete Grenzkonstruktionen, aber keinen
solchen nachtraeglichen Test. Die Verbotsmeldung selbst stoppt den Caller nicht.

Das klaert die vorliegenden Portierungen, nicht das gesamte historische
Schulz-/Heim-Programm und nicht die Autorenabsicht der Buchfassung.
Weder diese Routinen noch ihre Schwellen werden in den Buchvertrag
kopiert. Kein neuer gekoppelter Solver, keine Ersatzbesetzung und keine
Aenderung des bisherigen bedingten Pseudosingulett-Befunds wurden erzeugt.

## 8. Ausfuehrung und begrenzte Testgegenreview

Der eigene unveraenderte Python-Block aus Abschnitt6 wurde via
`py -3.13 -B -` ausgefuehrt: 36 exakte synthetische Kontrollen bestanden,
Exitcode 0. Keine historischen Quelltexte oder Programmdateien wurden
dabei importiert oder ausgefuehrt.

`tests/test_structure_handling.py` wurde anschliessend vollstaendig gelesen
und mit `py -3.13 -B -m unittest discover -s tests -p test_structure_handling.py -v`
ausgefuehrt: alle acht Tests bestanden, Exitcode 0. Keine materiellen
Algebra- oder Reichweitenfehler gefunden. Die Tests importieren vorhandene
eigene rationale Log-/Greedy-Helfer, keine historischen Programme.

Insbesondere sind die exakte-reelle Offsetdiagnose und historische
Laufzeitwirkung ausdruecklich getrennt. Der positive Besetzungsbereich des
kleinen Gatehelpers ist deklariert und keine Einschraenkung der gesamten
Buchdomaene. Der Transfervergleich ergibt fuer seinen synthetischen Fall
den Buch-Erstwert 1, aber die beiden Port-Leswerte 0; er behauptet weder
Autorenkorrektur noch physikalisch gueltigen Teilchenzustand. Die fehlenden
Caller-Sperren werden nicht durch diese Zahlentests bewiesen, sondern durch
die oben belegte statische Kontrollflusslekture.

Nur die eigene neue Reviewdatei wurde geschrieben. Root-Tests, historische
Quellen, alte Rechner, Eingaben und Snapshots blieben unveraendert.
