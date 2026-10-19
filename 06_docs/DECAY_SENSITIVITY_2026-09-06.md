# Gemeinsamer Vergleich von A(k=1)=1/3 und 1/5

2026-09-06, Etappe 35. Eigene Sensitivitätsprüfung, keine Korrektur Heims.

## Ergebnis vorweg

Der Wechsel von Heims Wahl `A(k=1)=1/3` zum zuvor verbliebenen Kandidaten
`1/5` ändert die gewöhnliche Vorwärtsauswahl erheblich. Aus den ersten
drei Besetzungen `(14,9,13)` werden `(14,10,1)`. Die zweite direkte
Strukturbedingung besteht dann an diesem Präfix; dafür erreicht die vierte
Zone einen Sättigungszweig, den der gewöhnliche Auswahlalgorithmus nicht
abdeckt. Wir geben dort keine erfundene vierte Besetzung aus.

Die getrennte vollständige Existenzprüfung ergibt für **beide A-Werte
und beide festen Alpha-Profile**: Keine ganzzahlige Belegung erfüllt
gleichzeitig die exakte skalare Gleichung und die direkten ungewichteten,
nichtkollabierten Strukturbedingungen. Der bloße Austausch der heuristischen
Wahl behebt diesen bedingten Konflikt also nicht. Das ist keine Widerlegung
der gesamten Theorie oder ihrer physikalischen Näherungen.

## 1. Herkunft und vorab festgelegter Vergleich

Die Quellenkette stammt aus den Etappen 30–34. H004 Druck 323–325 verbindet
Externterm und Gerüstreferenz; Druck 325 motiviert `A(k=1)=1/3` heuristisch.
Die vorherigen Teilerbedingungen lassen auch `1/5` zu. Der auf (96b)
bezogene Wert 5 ist korrekt erklärt, erzwingt aber nicht die Übertragung
auf die Sigma-Zone. Einzelheiten: [xi-Ursprung](XI_ORIGIN_2026-09-06.md)
und [Externnormierung](EXTERNAL_APPROXIMATION_2026-09-06.md).

Vor der neuen Rechnung wurden Plan und vier Vergleichszellen in Commit
`3a3ad73` festgeschrieben. Der neue
[Maschinenvertrag](../04_reconstruction/alpha_audit/decay_sensitivity_inputs.json)
hat den kanonischen SHA256
`36173ed155513a29b8b1834b32a9c1845bb96c9b1083642d1053f9d33f9ac75a`.
Er bindet den unveränderten alten Buchinput per Hash. Keine Fallauswahl
nach Resultat, keine Massenauswertung und kein nachträglicher Parameterfit.

Die beiden Alpha-Profile sind die kleine (105)-Wurzel bei `Y3=1` und das
separate gedruckte Alpha `0.007297354572`. Jeweils innerhalb eines Profils
bleiben `a1,a2,a3,eta11,A16,w,Y3,Y9,Q_j` und der Buchzustand fest. Das
bedeutet nicht, dass alle Koeffizienten zwischen den Alpha-Profilen gleich
sind. `A(k=1)` ist außerdem nicht der gleichnamige Faktor der Alpha-Kette.

Mit `Q_j=(3,3,2,1)` wird auf beiden Seiten gemeinsam geändert:

```text
E_A(n) = exp(-A*n)              E_A(0) = 1
B = 27*a1 + 9*a2 + 2*a3         g_A = B + E_A(1)
w = 1 + eta11*A16              W_A = w*g_A
P(N) = a1*N1^3 + a2*N2^2 + a3*N3
T_A(N) = P(N) + E_A(N4)         R_A(N) = T_A(N) - W_A
```

Die eigene Fragestellung ist `R_A=0` bei den festgelegten direkten Gates.
Diese exakte Skalarfrage ist von der physikalischen Genauigkeit der
Externzonenapproximation und vom Ganzzahlauswahlverfahren getrennt.

## 2. Gemeinsame Verschiebung von g und W

| Alpha-Profil | A(k=1) | g_A, gerundet | W_A, gerundet | Delta W zum eigenen 1/3-Fall |
|---|---:|---:|---:|---:|
| (105), Y3=1 | 1/3 | 38.702976719320815 | 2830.263257668096264 | 0 |
| (105), Y3=1 | 1/5 | 38.805176161825008 | 2837.736877311656731 | 7.473619643560467 |
| Druckalpha | 1/3 | 38.702976719470277 | 2830.263257664227543 | 0 |
| Druckalpha | 1/5 | 38.805176161974470 | 2837.736877307748933 | 7.473619643521390 |

Für beide Profile gilt exakt
`Delta g = exp(-1/5)-exp(-1/3)`, also ungefähr
`0.1021994425041926082443314`, und `Delta W=w*Delta g`.
Die Nullverschiebungen der Baseline werden als Identität behandelt, nicht
als Differenz zweier unabhängig gerundeter Intervalle. Alle Zahlen sind
dimensionslose Modellgrößen; Nachkommastellen sind keine Messgenauigkeit.

## 3. Vorwärtsauswahl und erreichte Zweiggrenze

Die ersten drei Schritte maximieren jeweils die noch finanzierbare ganze
Besetzung. Der gewöhnliche vierte Schritt ist nur bei positivem `W4<=1`
und `raw_N4<=a3*N3` zugelassen, mit `raw_N4=-ln(W4)/A`.
Dies ist unsere eingeschränkte Diagnose, keine vollständige Implementierung
der historischen TRC-, Sättigungs- und Transferregeln.

| Profil / A | N1,N2,N3 | Rest W4 | Reeller Rohwert N4 | Kappe a3*N3 | Ausgabe |
|---|---|---:|---:|---:|---|
| (105) / 1/3 | (14,9,13) | 0.0784852851812753 | 7.63453236505430 | 12.7225642681340 | N4=7 |
| Druck / 1/3 | (14,9,13) | 0.0784852803410499 | 7.63453255006575 | 12.7225642691055 | N4=7 |
| (105) / 1/5 | (14,10,1) | 0.0567507450334770 | 14.3454324718180 | 0.978658789856464 | Sättigung erforderlich |
| Druck / 1/5 | (14,10,1) | 0.0567507410509477 | 14.3454328226970 | 0.978658789931195 | Sättigung erforderlich |

Bei `1/3` reproduzieren beide Profile `(14,9,13,7)` und die direkten
Bandbreiten `(2459,-10,6)`: Die zweite Bedingung scheitert an `81>91`.
Die Reste `R_A` sind ungefähr `0.0184866826831298` bzw.
`0.0184866875233552`, also nicht null. Die separat ausgewertete gewichtete
107b-Größe `a3*N3-N4` ist etwa `5.7225642681340` bzw. `5.7225642691055`.
Ihr positives Vorzeichen beseitigt den anderen Strukturkonflikt nicht.

Bei `1/5` bestehen die ersten beiden direkten Gates am Präfix mit Margen
`(2359,99)`. Die zweite Reihenfolge hat Margen `(2644,99,0)`, das Zentrum
ist `2744`. Das ist keine gültige Vollstruktur: Der Rohwert über 14
überschreitet die Kappe unter 1. Es wird weder auf 14 abgeschnitten noch
auf die Kappe gesetzt; keine ausgewählte `N4`-, `R_A`- oder 107b-Ausgabe.

Der Unterschied ist nachvollziehbar: Die Änderung von `g` wird durch `w`
auf `W` übertragen. Die neue zweite Besetzung 10 verbraucht so viel des
Budgets, dass für die dritte nur 1 bleibt. Damit sinkt deren Kappe stark,
während die langsamere Exponentialabnahme einen größeren vierten Rohwert
verlangt. Das ist ein diskreter Zweigwechsel, keine kleine Rundungskorrektur.

## 4. Vollständiger bedingter Ausschluss

Die Existenzprüfung hängt nicht von dieser Vorwärtsauswahl ab. Geprüft
werden nichtnegative ganze `N_j` mit den direkten Bedingungen

```text
N1^3 > G2(N2),   G2(n) = n*(n+1)*(2*n+1)/6
N2^2 > G3(N3),   G3(n) = n*(n+1)/2
N3 > N4.
```

Die zweite Reihe `N1^3>=N2^2>=N3>=1` und das positive Zentrum werden
zusätzlich geprüft; im betreffenden Integerbereich folgen sie bereits
aus den strikten Gates. Die spätere gewichtete 107b-Bedingung wird nicht
mit ihnen vermischt. Zusätzliche Bedingungen könnten keine fehlende
Lösung erzeugen.

Die Endlichkeit wird für jede neue Zelle frisch begründet, nicht aus der
alten Rechnung übernommen. Die rationalen Inputintervalle sichern
`a1>249/250`, `a2>1`, `a3>489/500` und `W_A<2840`. Wegen des positiven
Externterms gilt für jede exakte Lösung:

```text
N1^3 < 2840/(249/250) < 15^3    => N1<=14
G2(20)=2870 > 14^3=2744         => N2<=19
G3(27)=378 > 19^2=361           => N3<=26
N4 < N3, ganzzahlig             => N4<=25.
```

Die Box enthält je Zelle **1239 strukturell zulässige Dreierpräfixe** und
**9231 zulässige ganzzahlige Viererbelegungen**. Für festes Präfix nimmt
`R_A` mit `N4` streng ab. Zertifizierte Endpunkte schließen deshalb ganze
Bereiche auf einmal aus. Kein geprüfter Bereich enthält null; keine
nachträglich gewählte numerische Toleranz wird verwendet. Oberhalb der
N1-Box ist die positive Budgetüberschreitung ebenfalls zertifiziert.

| Profil / A | Gesicherte Untergrenze für abs(R_A), abwärts gerundet |
|---|---:|
| (105) / 1/3 | 0.057144075037 |
| Druck / 1/3 | 0.057144070272 |
| (105) / 1/5 | 0.943249254966 |
| Druck / 1/5 | 0.943249258949 |

Diese Grenzen gelten auf der strukturell zulässigen Domain, nicht für
die strukturell unzulässige Vorwärtsausgabe des 1/3-Falls. Sie sind
algebraische Ausschlussmargen, keine Massenfehler oder Rangliste
physikalischer Güte.

### Getrennte reelle Diagnosen

Der Vorvertrag deklarierte nur die enge Relaxation `0<=N4<=N3-1`, während
`N1,N2,N3` ganz bleiben. Auch sie ist in allen vier Zellen ausgeschlossen.
Die Vertragsreview machte ausdrücklich darauf aufmerksam, dass dieser
Bereich für reelle Zahlen enger als der direkte Gate `0<=N4<N3` ist.

Daraufhin wurde **zusätzlich**, nicht als vorab deklarierte Rechnung,
der größere offene Bereich analytisch geprüft. Monotonie und der
linksseitige Grenzwert `N4` gegen `N3` genügen; `N4=N3` ist selbst nicht
zugelassen. Auch hier kein Nullpunkt. Für `1/5` bleibt in beiden Profilen
ein Abstand größer als `0.7619800080`; für `1/3` gelten die obigen Grenzen.
Der ursprüngliche Inputvertrag blieb unverändert.

Das erweitert ausdrücklich nicht auf beliebiges reelles `N4>=0` ohne
dritten Gate: Bei `1/5` würde bereits der isolierte Rohwert am neuen
Präfix eine solche weitergehende Ausschlussbehauptung widerlegen.

## 5. Nachprüfbarkeit und Grenzen

[Rechner](../scripts/audit_decay_sensitivity.py),
[15 neue Tests](../tests/test_decay_sensitivity.py) und drei interne Reviews:
[Numerik](../04_reconstruction/alpha_audit/reviews/DECAY_NUMERICS_REVIEW_2026-09-06.md),
[Existenz](../04_reconstruction/alpha_audit/reviews/DECAY_EXISTENCE_REVIEW_2026-09-06.md),
[Vertrag](../04_reconstruction/alpha_audit/reviews/DECAY_CONTRACT_REVIEW_2026-09-06.md).

Der Rechner nutzt auswärts gerundete rationale Intervalle auf dem alten
10^-40-Gitter. Exponentialargumente werden vor Taylor-Einschluss reduziert;
die Zweigentscheidung benötigt keinen gerundeten Logarithmus. Decimalwerte
sind nur Darstellung und Kreuztest, nicht der Ausschlussbeweis.

Der Numerikagent entwickelte eine eigene Machin-/Wurzel-/Taylor-Kette ohne
Import unserer Rechner: 120/160-Stellen-Läufe, 110 verglichene Ausgabefelder
und 76 rationale Einschlüsse; zusätzlich eigene gekoppelte Endpunktprüfung.
Die Existenzreview prüft separat sämtliche 9231 Integerzustände, verwendet
aber transparent die alte Intervall-/Inputhilfe. Sie ist daher keine zweite
vollständig unabhängige Inputimplementierung. Root hat die ausführbaren
Blöcke wiederholt. Die Codegegenreview bestätigt Zweiggrenzen, Box und
Intervallrichtungen. Das sind interne Prüfungen, kein externes Peer Review.

```powershell
py -3.13 -B scripts/audit_decay_sensitivity.py --check --verify-sources
py -3.13 -B -m unittest discover -s tests -q
py -3.13 -B scripts/validate_finding_register.py
```

Abschluss: 331 Tests insgesamt; zwölf bisherige Ergebnischecks sowie
Existenz-, Externtransport- und Rekurrenzzertifikate unverändert bestanden.
Alte Inputs, Rechner, Snapshots und 49 Normalisierungs-CSV-Zeilen erhalten.
FIND-045 ist ein Anschlussbefund zu FIND-040/042–044: 45 Befundgruppen
sind ausdrücklich nicht 45 unabhängige Fehler.

Kein Ergebnis hier entscheidet über andere A- oder Y-Werte, Kollapszweige,
die gesamte Feldtheorie, reale Massen oder Heims Kenntnisstand am Lebensende.
Die quantitative physikalische Fehlerbrücke der Externzonenapproximation
bleibt offen. Genauere Hardware schließt eine solche Herleitungslücke nicht.

Nächster begrenzter Auftrag: Die bereits belegten Buch-Sättigungsregeln
auf den nun erreichten 1/5-Zweig beziehen, ihren Definitionsbereich und
den Gleichungserhalt getrennt prüfen. Kein freier Ersatzalgorithmus und
keine Suche nach einem besser passenden A-Wert.
