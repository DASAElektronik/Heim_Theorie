# Mathematikreview der Konfigurationsauswahl (98a)

Stand: 2026-09-06. Unabhaengige algebraische und numerische Gegenpruefung
der vom Hauptagenten und Quellenreview uebergebenen Gleichungen von EDM2,
Druck268/269. Keine eigene Glyphenkontrolle, keine neuen Messdaten,
kein Fit und keine Gesamtbewertung der Theorie.

## 1. Quellenpaket und Lesestatus

Fuer positive ganze q und k seien, mit mathematischem pi,

```text
e = eta = pi/(pi^4+4)^(1/4),
a = eta_q = pi/(pi^4+4q^4)^(1/4),
b = eta_qk = pi/(pi^4+q^4(4+k))^(1/4),
V1 = a/b,
V2 = (1+sqrt(a))^2/(4e),
Q1 = a^2/sqrt(e),
Q2 = sqrt(e).
```

Dabei gelten `0<a<=e<1` und `b>0`. Alle Groessen sind dimensionslos.
q=0 ist fuer die unten verwendete u-Funktion wegen Division durch q
nicht im Definitionsbereich. Die Auswahl positiver ganzer Indizes ist
eine ausdrueckliche Voraussetzung dieser Review, kein nachgewiesener
Ausschluss jeder anderswo verwendeten Nullkonfiguration.

Nach Rueckmeldung des Hauptagenten sind drei aufeinanderfolgende Ebenen
der Quelle zu unterscheiden:

```text
I:   F2-F1+G2-G1 > 0,  F_i=V_i, G_i=Q_i;
II:  V1+Q1 > V2+Q2;
III: b^(-1) < B_q,  k < u_q,

B_q = (1+sqrt(a))^2/(4ea) + (1-a/e)*sqrt(e),
u_q = (pi/q)^4*(B_q^4-1)-4.
```

Audittrail zur Lesung: Zwischenzeitlich wurde von einem Quellenleser `Q2=sqrt(eta_q)`
vermutet. Nach erneuter hochaufgeloester Pruefung meldete der Hauptagent
Konsens von drei Lesern fuer `Q2=sqrt(eta)` ohne q. Die abweichende Lesung
wird hier als verworfene Audit-Fehlablesung behandelt, nicht als zweite
Heim-Fassung. Alle nachstehenden D-Werte beziehen sich ausschliesslich
auf das oben angegebene finale Paket.

## 2. Exakte Umformung und zwei getrennte Konflikte

Setze die eigene Residuumsgroesse `R_VQ=V1+Q1-V2-Q2`. Sie ist nicht
Heims Delta aus `L*Delta=k`. Direktes Einsetzen ergibt

```text
R_VQ = a/b + a^2/sqrt(e) - (1+sqrt(a))^2/(4e) - sqrt(e)
      = a*(b^(-1)-D_q),

D_q = (1+sqrt(a))^2/(4ea) + sqrt(e)/a - a/sqrt(e).
```

Die Differenz zur gedruckten B-Funktion ist exakt

```text
D_q-B_q = sqrt(e)*(1/a-1) > 0.
```

Der gedruckte Zusatzterm hat nach Division durch a also nicht dieselbe
Form wie der aus V/Q resultierende Term. Beide Schranken sind positiv:
B_q hat einen positiven ersten und einen nichtnegativen zweiten Term,
und D_q>B_q.

### Erster Konflikt: vorgelagerte Bedingung gegen V/Q-Zeile

Mit den mitgeteilten Identifikationen ist

```text
F2-F1+G2-G1 = -R_VQ.
```

Ebene I verlangt daher `R_VQ<0`, Ebene II dagegen `R_VQ>0`.
Die beiden strikten Aussagen koennen nicht gleichzeitig gelten.
Dieser erste Richtungsbefund benoetigt die spezielle Q2-Lesung oder
irgendeinen numerischen Indexwert nicht.

### Zweiter Konflikt: V/Q-Zeile gegen gedruckte Schranke

Ebene II ist wegen a>0 aequivalent zu `b^(-1)>D_q`. Sie liefert weder
die gedruckte Richtung `<` noch den gedruckten Ausdruck B_q.
Wegen `D_q>B_q` ist sie sogar mit `b^(-1)<B_q` unvereinbar.
Auch die blosse Aenderung einer einzigen Ungleichungsrichtung wuerde
den Unterschied zwischen B_q und D_q nicht beseitigen.

Die vorgelagerte Ebene I ist dagegen aequivalent zu `b^(-1)<D_q`.
Damit ist die gedruckte B-Bedingung eine staerkere hinreichende Bedingung
fuer Ebene I, aber keine aequivalente Umformung der uebergebenen Gleichungen.
Eine zusaetzliche Auswahlbedingung, welche genau diese Verstaerkung
rechtfertigt, ist in diesem isolierten Paket nicht enthalten.

Dies identifiziert unvereinbare Praemissenpakete, aber keine gesicherte
Autorenkorrektur, historische Fehlerursache oder physikalisch richtige
Ersatzfassung.

## 3. Umrechnung der Schranken in k

Aus der eta-Definition folgt exakt

```text
b^(-4) = 1 + (q/pi)^4*(4+k).
```

Fuer eine positive Schranke X_q ist daher `b^(-1)<X_q` aequivalent zu
`k<(pi/q)^4*(X_q^4-1)-4`; bei `>` bleibt ebenfalls die Richtung erhalten.
Die vierte Potenz darf hier ohne Vorzeichenverlust genommen werden,
weil b, B_q und D_q positiv sind. Die letzte gedruckte Umformung von
B_q nach u_q ist unter diesen Voraussetzungen korrekt.

Definiere nur zur Diagnose `v_q=(pi/q)^4*(D_q^4-1)-4`. Dann lauten die
drei Ebenen, ohne sie stillschweigend miteinander zu vermischen:

| Ebene | Bedingung an den Index k |
|---|---|
| I: vorgelagerte Differenz mit F/G-Identifikation | `k<v_q` |
| II: gedruckte V/Q-Ungleichung | `k>v_q` |
| III: gedruckte B-/u-Funktion | `k<u_q` |

Es gilt `v_q>u_q`. Die Bezeichnung v_q in dieser Review ist ein eigener
Diagnosename, kein neu behauptetes Quellensymbol oder Heimparameter.

## 4. Unabhaengige Zahlenrechnung

Berechnet mit eigener, temporaer ausgefuehrter Python-Standardbibliotheks-
Arithmetik: zunaechst binaere Gleitkommazahlen, danach Decimal bei
70 bis 80 Stellen mit einem laengeren festen mathematischen pi-Praefix.
Es wurde weder ein bestehender Heim-Rechner importiert noch ein moderner
Referenzwert eingesetzt. Die folgende Tabelle ist auf 12 Nachkommastellen
gerundet; die Rechnung ist keine gesonderte Intervallarithmetik.

```text
eta = 0.989989640819342375373108099936747897202515837372404680432...
```

| q | gedruckte Funktion u_q | aus V/Q berechnete Schwelle v_q |
|---:|---:|---:|
| 1 | 2.063799031006 | 6.226877489516 |
| 2 | 1.963489198103 | 8.397876839289 |
| 3 | 1.239666657763 | 12.593522536212 |
| 4 | 0.100757928773 | 15.551725178071 |
| 5 | -0.884599369019 | 16.829706974369 |
| 6 | -1.604895797217 | 17.149100596963 |
| 7 | -2.114879715866 | 17.015728553777 |
| 8 | -2.479387483702 | 16.685846949706 |
| 9 | -2.745551088204 | 16.281584709326 |
| 10 | -2.944559334649 | 15.860420213543 |

Insbesondere ist

```text
u_2 = 1.963489198102715361385288774899279758500165077172875312...
```

Die mitgeteilte Behauptung `2<u_2<3` wird von der gedruckten u-Funktion
mit diesen Definitionen nicht reproduziert. Dagegen werden `2<u_1<3`,
`1<u_3<2` und `0<u_4<1` reproduziert. Dieser Zahlenbefund ist von der
vorgelagerten V/Q-Umformung unabhaengig: Er verwendet gerade die
gedruckte B-Funktion, nicht die eigene D-Schwelle.

### Direkte Residuen als Vorwaertskontrolle

Aus den V/Q-Definitionen unmittelbar berechnet:

| (q,k) | R_VQ = V1+Q1-V2-Q2 |
|---|---:|
| (1,1) | -0.01255336320879895637 |
| (1,2) | -0.01011508800444378121 |
| (1,7) | 0.00181775171649388573 |
| (2,2) | -0.11722441235463017149 |
| (5,1) | -0.44366339495522602767 |
| (5,17) | 0.00303189383581548560 |

Damit kann etwa (1,1) gleichzeitig die gedruckte u-Bedingung und Ebene I
erfuellen, aber nicht Ebene II. (5,1) erfuellt Ebene I, obwohl es von der
gedruckten B-Bedingung ausgeschlossen wird. Diese Beispiele beweisen
nicht, dass die Quelle diese Paare nach saemtlichen weiteren Bedingungen
physikalisch zulaesst; sie testen nur die hier behauptete Umformung.

## 5. Positive ganzzahlige Paare und die Grenze q>4

Unter ausschliesslich `q,k` positiv ganzzahlig und der gedruckten
B-/u-Bedingung ist die erlaubte Menge

```text
{(1,1), (1,2), (2,1), (3,1)}.
```

Die Bedingung ist eine q-abhaengige Auswahl, kein kartesisches Produkt
separater q- und k-Bereiche. Schon `0<u_4<1` laesst fuer q=4 kein
positives ganzes k zu. Ferner wird (2,2) durch den tatsaechlich berechneten
Wert u_2 ausgeschlossen. Wenn k=0 als eigener Quellfall betrachtet wird,
muss seine Zulaessigkeit gesondert untersucht werden; sie ist nicht in
der hier beauftragten positiven Paarmenge enthalten.

### Ausschluss aller ganzen q>=5, nicht nur ein endlicher Scan

Schreibe die gedruckte Funktion als Funktion von a:

```text
F(a) = a*B(a)
     = (1+sqrt(a))^2/(4e) + a*sqrt(e) - a^2/sqrt(e).
```

a=eta_q nimmt mit q ab. Fuer q>=5 gilt `0<a<=a_5<e/2`, und

```text
F'(a) = (1+1/sqrt(a))/(4e) + sqrt(e) - 2a/sqrt(e) > 0.
```

Numerisch ist `a_5=0.44006292757453547...` und
`F(a_5)=0.94191892106626373...<1`. Der benoetigte Abstand laesst sich
auch ohne Praezisionsannahme der Dezimaltabelle grob absichern:
Aus `3.14<pi<22/7` folgen `0.98<e<1` und `0.43<a_5<0.45`.
Damit ist a_5<e/2 und wegen `sqrt(0.45)<0.671`

```text
F(a_5) < (1.671)^2/(4*0.98) + 0.45 - (0.43)^2
       = 3831433/3920000 < 1.
```

Folglich ist fuer alle q>=5 `B_q<1/eta_q`. Mit
`eta_q^(-4)=1+4(q/pi)^4` folgt daraus `u_q<0`. Damit ist die positive
ganzzahlige Paarliste vollstaendig, nicht bloss bis q=10 durchsucht.

Die Aussage "alle q>4" gilt in diesem Schluss fuer ganzzahlige q.
Fuer reelle q unmittelbar oberhalb von 4 ist u_q wegen u_4>0 und
Stetigkeit noch positiv; eine universelle reelle Lesung waere falsch.

## 6. Asymptotik und Reichweite der vorgelagerten Auswahl

Fuer grosse positive q gilt `a~pi/(sqrt(2)*q)`. Daraus folgen

```text
B_q ~ 1/(4e*a),
D_q ~ (1/(4e)+sqrt(e))/a,

lim u_q = 1/(64e^4)-4
        = -3.98373337610908222905...,
lim v_q = 4*(1/(4e)+sqrt(e))^4-4
        =  5.68804861972520435777....
```

Die vorgelagerte Ebene I `k<v_q` erlaubt damit fuer hinreichend grosse
ganze q weiterhin mindestens k=1 bis 5. Aus ihr allein folgt also nicht
die gedruckte q-Grenze. Die gegensaetzliche Ebene II `k>v_q` erlaubt
fuer hinreichend grosse q unter anderem jedes ganze k>=6. Beides betrifft
nur diese eine isolierte Bedingung; andere Konfigurationsgesetze koennen
eine zusaetzliche Beschraenkung vorsehen.

Die fuer die bisherige Alpha-Spezialisierung eingesetzten Paare (1,1)
und (1,2) bleiben unter der gedruckten B-Bedingung enthalten. Der neue
u_2-Befund ersetzt daher nicht automatisch eta_11 oder eta_12 in den
bisherigen sechs Rechnern. Eine Wirkung auf deren Ergebnisse waere
getrennt ueber die konkrete Abhaengigkeit von Auswahlregeln nachzuweisen.

## 7. Vorlaeufiger Abschluss

Befunde: zwei unterschiedliche algebraische Konflikte in der
uebergebenen Kette; zusaetzlich eine nicht reproduzierte Zahlenbehauptung
zu u_2. Die Umformung B_q nach u_q selbst ist unter den genannten
positiven Domaenen korrekt. Der gedruckte Ausschluss aller ganzen q>4
ist fuer diese B-Funktion bestaetigt, nicht fuer die vorgelagerte
F/G-Bedingung. Eine autorisierte Korrektur oder vollstaendige physikalische
Auswahltheorie wurde damit nicht bestimmt.

Der Abgleich mit dem vom Hauptagenten neu zu erstellenden Rechner,
Snapshot und dessen Tests stand bei dieser Erstfassung noch aus;
der folgende Nachtrag dokumentiert seine Durchfuehrung.
Nur diese eigene Reviewdatei wurde erstellt; keine kanonischen Dateien,
alten Rechner, Inputs, Ergebnis-Snapshots oder Git-Zustaende geaendert.

## 8. Nachtrag: unabhaengige Implementierungs- und Snapshotreview

Gelesen wurden vollstaendig `scripts/audit_configuration_selection.py`,
`tests/test_configuration_selection.py` und die Normalisierungsentscheidung
`NORM-CONFIGURATION-SELECTION-DIAGNOSTICS.md`. Der JSON-Snapshot wurde
zusaetzlich maschinell in seine Felder zerlegt und unabhaengig nachgerechnet.
Keine der vier Dateien wurde von dieser Review geaendert.

### Implementierte Bedeutung und Zahlen

`ratio_levels` setzt das finale Quellenpaket richtig um, insbesondere
Q2=sqrt(e). `delta_VQ` im Code bezeichnet ausschliesslich das eigene
Residuum R_VQ dieser Review, nicht das Delta von Heims `L*Delta=k`.
Die getrennten Funktionen fuer vorgelagerte, gedruckte V/Q- und gedruckte
B-/k-Bedingung bewahren die unterschiedlichen Aussagen. Die D-Schwelle
wird nicht als reparierte Quellenfassung zurueckgeschrieben.

Die unabhaengige Snapshotpruefung verwendete 100-stellige Decimal-Arithmetik,
einen festen laengeren pi-Praefix und die alternative Form
`eta_qk=(1+q^4*(4+k)/pi^4)^(-1/4)`. D wurde dabei direkt als
`(V2+Q2-Q1)/a` berechnet. Insgesamt wurden 1057 numerische und boolesche
Felder kontrolliert: alle zehn Schrankenzeilen, alle 50 gespeicherten
Beispielzeilen mit ihren Entscheidungen, eta, beide asymptotischen
Grenzwerte sowie die beiden L=4-Ladungsverhaeltnisse. Die numerischen
Abweichungen lagen jeweils unter `1e-65`; alle booleschen Entscheidungen
stimmten ueberein. Es wurde kein bestehender Audit-Rechner fuer diese
unabhaengige Werteberechnung importiert.

Die Funktion `charge_change` loest nur die bedingten Beziehungen
`L*Delta=k` und `charge_ratio^4=1+Delta` auf dem positiven Wurzelzweig.
Ein anderes positives ganzes L im Helfer ist eine Diagnose, keine neue
Quellenbehauptung. Weder diese Wurzelrechnung noch die Indexauswahl
beweist die physikalische Quantisierungsannahme.

### Pruefung des rationalen Ausschlussbelegs im Code

Der Code verwendet eine andere, ebenfalls gueltige grobe Schranke als
Abschnitt 5. Aus `3<pi<22/7` folgen

```text
e^4 = pi^4/(pi^4+4) > 81/85 > (49/50)^4,
eta_5 < pi/(5*sqrt(2)) < (22/7)/(5*7/5) = 22/49 < 9/20.
```

Hier ist `sqrt(2)>7/5` durch Quadrieren positiv-rational nachgewiesen.
Setze `a_U=9/20`. Fuer jedes q>=5 gilt
`a<=eta_5<a_U<e/2`, sodass F(a,e) bei festem e in a streng waechst.
Zuerst wird deshalb a durch a_U ersetzt. Erst danach werden die
einzelnen Terme von F(a_U,e) abgeschaetzt:

```text
F(a,e) < F(a_U,e)
       < (1+84/125)^2/(4*49/50) + a_U - a_U^2
       = 470723/490000 < 1.
```

Dabei gelten `(84/125)^2>a_U`, e>49/50 und e<1. Insbesondere wird
der negative Term nicht unzulaessig fuer unbekanntes a nach oben
abgeschaetzt: Die monotone Ersetzung a->a_U erfolgt vor der getrennten
Abschaetzung. Damit ist der Codebeleg algebraisch korrekt.

Die gespeicherten booleschen Fraction-Checks pruefen die rationalen
Zahlenungleichungen. Der verbindende analytische Beweis -- Monotonie,
eta_5-Abschatzung, B<1/a und daraus u_B<0 -- wird durch die obige
Argumentation geliefert, nicht durch den Testnamen oder ein blosses
`all_checks_hold`. Der Beleg gilt fuer mathematisches pi und ganze q>=5,
nicht fuer beliebige synthetische positive pi-Argumente der Hilfsfunktionen.

Die gespeicherte Paarvollstaendigkeit ist damit nachvollziehbar:
q1..4 mit u_B<3, alle ganzen q>=5 ausgeschlossen, k positiv ganzzahlig.
Die Rechner-Schleife bis k=20 ist nicht selbst der Vollstaendigkeitsbeweis.

### Domaenen, Grenzen und Praezision

- Index-/Dimensionshelfer verlangen echte Python-Integer; bool, Float
  und Strings werden abgewiesen. Die positive Auswahl verlangt q,k>=1.
  Nur der eta-Helfer laesst die formalen Nullfaelle zu; q=0 ergibt dort
  eta=1 und wird nicht als positive Auswahlkonfiguration ausgegeben.
- Die Verhaeltnisfunktion verlangt positive endliche Decimal-Werte und
  `0<a<=e<=1`. Ihr formaler Rand a=e=1 ist algebraisch erlaubt, liefert
  D-B=0 und gehoert nicht zum nichttrivialen Buchfall e<1.
- Die vierte Potenz im Schwellenhelfer wird nur fuer positive Schranken
  verwendet; damit ist die benoetigte Monotonie gegeben.
- `strict_compare` verweigert sowohl Gleichheit als auch zu nahe Werte
  mit ArithmeticError. Es ist kein vollstaendiger dreifacher Vergleich
  mit Rueckgabe 0 und keine zertifizierte Intervallarithmetik. Die
  Verweigerung exakter Gleichheit entspricht seinem dokumentierten
  konservativen API-Verhalten und ist im Test explizit erwartet.
- Das Praezisionsfenster 40..200 wird geprueft. Zusaetzlich zu den
  bestehenden 80/120-Tests wurden 39 und 201 erfolgreich abgewiesen,
  40 und 200 akzeptiert. Paarmenge und Intervallentscheidungen stimmen
  an beiden erlaubten Enden ueberein; die groesste absolute 40/200-
  Differenz der 50 geprueften Schrankenfelder war etwa `2.693e-37`.
- Bei 40 Stellen wurden auch mathematisch ungleiche Werte mit 70
  zusaetzlichen Nachkommastellen nahe 2 konservativ abgewiesen. Eine
  ausreichend getrennte Differenz wurde richtig entschieden.

Kein falscher Grenzentscheid wurde im vorgesehenen Bereich gefunden.
Decimal-Operationen runden intern; eine Aussage "keine Rundung" sollte
deshalb nur das Fehlen einer zusaetzlichen Rundung auf Ausgabestellen
vor der Entscheidung bezeichnen. Diese kleine redaktionelle Praezisierung
wurde dem Hauptagenten gemeldet.

### Tests, Grenzen der Testaussage und Abschluss

```text
python -B scripts/audit_configuration_selection.py --check --verify-sources
  EDM2-Hash bestaetigt; Snapshot stimmt mit Neuberechnung ueberein.
python -B -m unittest discover -s tests -p test_configuration_selection.py -v
  9 Tests bestanden.
python -B -m unittest discover -s tests -q
  86 Tests bestanden.
```

Die Tests enthalten eine exakt rationale synthetische V/Q-Identitaet,
welche die verworfene Q2-Lesung unterscheiden wuerde, ein unabhaengiges
u_2-Zahlenziel, unterschiedliche Beispiele der drei Aussageebenen,
die Paarmenge, Konvergenz und den rationalen Ausschlussbeleg. Sie testen
nicht die physikalische Begruendung der Auswahl. Als kleine nichtblockierende
Verstaerkung wurden die oben ad hoc erfolgreich geprueften genauen
Praezisionsraender und ungleichen Nahgrenzen fuer dauerhafte Tests empfohlen.

Abschluss des Implementierungsabgleichs: kein offener Code-, Zahlen- oder
algebraischer Belegdefekt im geprueften neuen Rechner gefunden. Die lokalen
Quellenwidersprueche und die nicht reproduzierte u_2-Behauptung bleiben
inhaltliche Befunde, nicht durch eine heimliche Codekorrektur beseitigt.
Eine Buchauswahlregel darf auch nicht ohne gesonderte Quellenbruecke auf
die Formelueberlieferung von 1989 oder deren eta_22 uebertragen werden.
Nur diese eigene Reviewdatei wurde ergaenzt; keine Codepatches oder Commits.

## 9. Nachtrag: abschliessende Berichts- und Registergegenlesung

Vollstaendig gegengelesen wurden
`06_docs/CONFIGURATION_SELECTION_2026-09-06.md`,
`04_reconstruction/alpha_audit/CONFIGURATION_DEPENDENCIES.md` sowie die
neuen Registereintraege FIND-014 bis FIND-016. Die zwischenzeitlich
ergaenzten Praezisions- und Nahgrenztests wurden ebenfalls gelesen und
erneut ausgefuehrt.

Die logische Hauptlinie ist korrekt begrenzt: FIND-014 erhaelt einen
positiven Quellen-/Begriffsbeleg, ohne die Ganzzahligkeit als Beweis des
L*Delta-Ansatzes auszugeben. FIND-015 fasst den lokalen Herleitungsknoten
zusammen und unterscheidet die drei Bedingungen. FIND-016 registriert
die von dieser Umformung unabhaengige u_2-Zahlenabweichung und die vier
Paare unter der einzelnen gedruckten B-Bedingung, nicht einen vollstaendigen
physikalischen Zustandskatalog.

Die Vollstaendigkeit der Paarliste ist im Bericht mit dem analytischen
Monotonieschritt und der rationalen Schranke begruendet. Die getrennten
Maxima q_max=3 und k_max=2 werden nicht als kartesisches Produkt ausgegeben.
Die Buch-Alpha-Paare (1,1) und (1,2) bleiben in dieser Liste; das ist weder
eine Loesung aller frueheren H-Probleme noch ein Grund, neue Zahlen in die
alten Profile einzusetzen. Die 1989-Verwendung von eta_22 bleibt eine
separate Versions-/Bedeutungsfrage: Ein Formelfaktor ist nicht allein
eine Behauptung eines realisierten Zustands mit denselben Auswahlgesetzen.

Zwei kleine, aber inhaltlich sinnvolle Schlussredaktionen wurden dem
Hauptagenten gemeldet:

1. In der Zusammenhangskarte steht bei C/Y3 die Kurzform `C=P/Y3=1`.
   Sie sollte eindeutig `C=P und Y3=1` mit `P=A1*A2` lauten; ein Slash
   darf hier nicht eine neue inverse Y3-Abhaengigkeit nahelegen.
2. Aus `Delta=(epsilon_prime/epsilon)^4-1` und `Delta=k/4` folgt fuer
   reelle Ladungsverhaeltnisse zunaechst der Betrag
   `abs(epsilon_prime/epsilon)=(1+k/4)^(1/4)`. Die im Bericht angegebene
   positive Wurzel fuer den Quotienten selbst benoetigt die positive
   Zweig-/Vorzeichenwahl. Diese ist fuer den Rechner explizit und sollte
   auch an der Formel im Bericht kurz genannt werden.

Diese beiden Hinweise betreffen keine Zahlenaenderung im geprueften
Rechner. Die zusaetzlichen Tests pruefen jetzt dauerhaft 39/201 als
unzulaessig, 40/200 als zulaessig sowie einen ungleichen Nahwert bei
80 Stellen, der durch den Abstandsschutz abgewiesen werden muss.
Der Normalisierungswortlaut unterscheidet nun richtig zwischen interner
Decimal-Rundung und keiner zusaetzlichen Rundung auf Ausgabestellen.

Erneute Ergebnisse: 9 Konfigurationstests und 86 Tests insgesamt bestanden;
Snapshot und H004-Quellhash bestaetigt; das erweiterte Befundregister
besteht die reine Metadatenintegritaetspruefung. Letzteres prueft nicht
die Wahrheit seiner Aussagen. Abgesehen von den beiden gemeldeten
Schlussredaktionen kein weiterer Algebra- oder Reichweitendefekt gefunden.
Nur diese eigene Reviewdatei ergaenzt; keine anderen Dateien oder Commits.

Nachtrag Hauptagent zum Abschluss: Beide oben genannten Schlussredaktionen
sind umgesetzt: C=P und Y3=1 ist eindeutig ausgeschrieben, und die positive
Quotienten-/Betragswahl steht nun im Bericht, in der Normalisierung und im
Rechnerdocstring. Der Reviewer hat diese Aenderungen abschliessend bestaetigt.
