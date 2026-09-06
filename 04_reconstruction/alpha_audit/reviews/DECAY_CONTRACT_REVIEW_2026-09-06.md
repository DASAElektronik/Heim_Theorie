# Scope-Review des Vorvertrags zur A(1)-Sensitivitaet

Stand: 2026-09-06. Geprueft wurden
`00_admin/DECAY_SENSITIVITY_PLAN.md` und
`04_reconstruction/alpha_audit/decay_sensitivity_inputs.json` gegen die
bereits vorliegenden Reviews der Etappen 30--34. Es erfolgte keine neue
Originallekture und keine Ergebnisrechnung.

## 1. Gesamturteil

Der Vertrag ist in seinem Hauptvergleich tragfaehig:

- Er kreuzt die zwei bereits festgelegten Buch-Alpha-Profile mit genau zwei
  Werten des diskreten Exponentenparameters `A(k=1)`.
- `A=1/3` ist als unveraenderte Buchwahl gekennzeichnet.
- `A=1/5` ist als eigene, quellenmotivierte Sensitivitaet zum auf Druck 325
  noch zulaessigen Teilerkandidaten `z=3` gekennzeichnet, nicht als Heims
  revidierte Formel.
- Die Externfunktion wird nicht nur links bei `N4`, sondern zugleich am
  Geruestbezug in `g` und damit in `W=g*w` geaendert.
- Masse, Zielwertanpassung und ein physikalisches Fehlerbudget sind
  ausdruecklich ausgeschlossen.
- Direkte ungewichtete Strukturbedingungen, (107b), ganzzahlige Existenz,
  Vorwaertsauswahl und reelle Diagnose werden als verschiedene Fragen
  gefuehrt.

Vor der Auswertung sind jedoch drei Begrenzungen passagescharf zu
protokollieren. Eine davon betrifft die Domaene der reellen Relaxation und
ist materiell; die beiden anderen verhindern eine Ueberdehnung der
Ergebnisbezeichnung.

## 2. Basisbindung und vier vorab festgelegte Zellen

Der im Sensitivitaetsinput gespeicherte kanonische SHA-256

```text
8b320903bfe148c2956168e46c2279c1a16cd1b2b1837cb5b6efba47188affb7
```

stimmt mit der kanonischen JSON-Darstellung von
`book_pseudosinglet_inputs.json` ueberein. Damit ist die deklarierte
Ausgangsbasis technisch nachvollziehbar gebunden.

Die vier Zellen sind vor dem Ergebnis vollstaendig durch

```text
2 Alpha-Profile x 2 A(k=1)-Profile
```

bestimmt. Alle vier muessen berichtet werden. Weder Restgroesse noch
Existenz eines Tupels darf nachtraeglich ueber die Profilwahl entscheiden.

Wichtig ist die Bedeutung von `fixed`: `a_j`, `w` und `A16` bleiben beim
Vergleich `A=1/3` gegen `A=1/5` **innerhalb desselben Alpha-Profils** fest.
Sie sind nicht notwendig zwischen den beiden Alpha-Profilen numerisch
identisch; insbesondere haengen `a3`, `A16` und damit `w` vom jeweils
festgelegten Alpha-Input ab. Der Ergebnisbericht sollte deshalb paarweise
Sensitivitaeten ausweisen und `fixed` nicht als eine einzige gemeinsame
Zahl ueber alle vier Zellen formulieren.

## 3. Beidseitige A-Aenderung

Fuer den aktiven Buchzustand `k=1` gilt `Q4=1`. Daher ist die im JSON
festgelegte Kette

```text
E_A(n) = exp(-A*n),
B      = 27*a1+9*a2+2*a3,
g_A    = B+E_A(1),
W_A    = g_A*w
```

die richtige Spezialisierung der in der Quellenreview dokumentierten
beidseitigen Algebra. Eine Aenderung von `A` betrifft somit gleichzeitig

```text
T_A(N) = a1*N1^3+a2*N2^2+a3*N3+E_A(N4)
```

und den Geruestwert `g_A`, der rechts in `W_A` eingeht. Der Vertrag
vermeidet damit den zuvor benannten Fehler eines bloss einseitigen
Externtermtauschs. `E_A(0)=1` und die leere Referenz bleiben unveraendert.

`mu_+` erscheint in der dimensionslosen Gleichung nicht aktiv und ist im
Basis-JSON auch nicht als Zahlenwert enthalten. Im gegenwaertigen Vertrag
bedeutet „`mu_+` fest“ deshalb: Die gemeinsame Massenskala wird weder
geaendert noch ausgewertet. Sobald spaeter eine dimensionale Masse gebildet
wuerde, muesste ihr Wert eigens gebunden werden; dieser Schritt ist hier
ausdruecklich ausserhalb des Scopes.

## 4. Zuschreibung des Profils A=1/5

Die IDs und Rollen sind angemessen:

```text
heim_z5:         A(k=1)=1/3, unchanged_book_choice
counterfactual_z3: A(k=1)=1/5,
                   own_source_motivated_sensitivity_not_author_correction
```

Im Bericht sollte durchgehend `A(k=1)=1/5` oder „z3-Sensitivitaet“ stehen.
Die Kurzform `A1=1/5` waere unguenstig, weil `A_1` in der Alpha-Kette eine
andere Buchgroesse bezeichnet und weil sie wie eine neue Autorenformel
klingen koennte.

Die Sensitivitaet fragt nur, welche mathematische Wirkung der auf Druck 325
vor der heuristischen Wahl verbleibende Kandidat `z=3` im bereits fixierten
Buchprofil haette. Sie behauptet weder, Heim habe diese Fassung publiziert,
noch, (79b/c) oder (96b) leite `1/5` physikalisch her.

## 5. Gewoehnliches floor ist nicht das vollstaendige Buch-TRC

Der Plan will eine „gewoehnliche Vorwaertsauswahl“ rechnen und verbietet
eine erfundene Promotionsschwelle. Das ist als eigene, reproduzierbare
Diagnose zulaessig. Sie darf aber nicht als vollstaendige Implementierung
des auf Druck 341 definierten `TRC` bezeichnet werden:

- Fuer gewoehnliche nichtnegative Werte wirkt `TRC` wie Abschneiden/floor.
- Das Buch nennt zusaetzlich den Sonderfall `0,99...99 -> 1` unterhalb
  einer Messbarkeitsschranke, legt dessen endliche Schwelle aber nicht fest.
- Der Vertrag erfindet diese Schwelle zu Recht nicht.

Folglich sollte das Ergebnis „ordinary-floor branch“ oder gleichwertig
heissen. Liegt ein entscheidender Wert in einer nicht zertifizierbar von
einer solchen Neunerfolge getrennten Umgebung, darf er nicht als eindeutige
Buch-TRC-Entscheidung ausgegeben werden. Exakte Integerexistenz und direkte
Gates bleiben davon unabhaengig.

Die `selection_policy` ist sonst passend begrenzt: Nur fuer
`0<W4<=1` und einen innerhalb der angegebenen Strukturgrenze liegenden
reellen Logwert wird ordinary floor verwendet. Bei `W4=0`, `W4>1`,
negativem Rest oder Ueberschreiten der Grenze wird lediglich die
Buch-Zweiggrenze gemeldet; keine Saettigung, Kappung oder Transferregel wird
hinzuerfunden.

## 6. Ganzzahlmodell, direkte Gates und (107b)

Der ganzzahlige Vertrag

```text
N1,N2,N3,N4 in Z_>=0,
N1^3>G2(N2),
N2^2>G3(N3),
N3>N4
```

entspricht dem bereits geprueften direkten ungewichteten (107)-Pfad. Die
zweite Ordnungsreihe und ihre Zentralbedingung werden getrennt geprueft.
Das verhindert, dass ein ungepruefter kombinierter Zustandspraedikat in den
Existenzsatz eingeschmuggelt wird.

Ebenso richtig ist, `beta4=alpha3*N3-N4` aus (107b) separat zu berichten.
Es darf weder das direkte Gate `N3>N4` ersetzen noch still mit ihm zu einer
einzigen Buchbedingung verschmolzen werden. Ein Ergebnis kann daher die
direkten Gates erfuellen und die Sigma-Bedingung verfehlen oder umgekehrt;
beide Status gehoeren getrennt in die Ausgabe.

## 7. Materielle Praezisierung der reellen N4-Relaxation

Das JSON setzt fuer reelles `N4`

```text
0<=N4<=N3-1.
```

Fuer ganzzahliges `N4` ist dies zu `N3>N4` aequivalent. Fuer reelles `N4`
ist es jedoch **strenger** als das direkte Gate, dessen echte reelle
Fortsetzung

```text
0<=N4<N3
```

waere. Das gegenwaertige Intervall laesst den ganzen Bereich
`N3-1<N4<N3` aus.

Vor der Auswertung gibt es daher genau zwei saubere Optionen:

1. Soll die Diagnose die reelle Relaxation des direkten Gates darstellen,
   ist die Domaene auf `0<=N4<N3` zu setzen.
2. Soll `0<=N4<=N3-1` bewusst beibehalten werden, muss sie als staerkere,
   integerzellgebundene eigene Diagnose bezeichnet werden. Ein Nichtfund
   darin ist dann kein Nichtfund fuer die volle reelle Relaxation.

Diese Praezisierung aendert weder das diskrete Modell noch die
Ganzzahlpruefung. Sie betrifft nur die Reichweite der explizit als
nichtphysikalisch bezeichneten reellen Hilfsdiagnose.

## 8. Arithmetik und endliche Suchraeume

Die geforderte Neuberechnung einer endlichen Obermenge fuer jede Zelle ist
richtig. Da sich mit `A` auch `W_A` aendert, duerfen die alten Boxgrenzen
nicht ungeprueft wiederverwendet werden. Rationale auswaerts gerundete
Intervalle duerfen Zweigzeichen, Gates und Ausschluesse zertifizieren;
hochpraezise Dezimalwerte dienen nur Anzeige und unabhaengiger Gegenprobe.

Bei einer exakten Integergleichung ist eine Toleranzsuche kein Ersatz fuer
den Existenzentscheid. Ein berichteter Minimalrest muss deshalb klar als
Diagnose neben dem exakten Existenzstatus stehen und darf weder ein Tupel
„akzeptieren“ noch ein Profil bevorzugen.

## 9. Freigabegrenze

Der Vertrag ist fuer die vier diskreten, beidseitig aktualisierten
Vergleichszellen freigegeben, sofern die Ergebnisdarstellung

- `fixed` paarweise pro Alpha-Profil versteht,
- ordinary floor nicht mit dem vollstaendigen Quellen-`TRC` gleichsetzt,
- (107b) separat haelt und
- die reelle N4-Domaene gemaess Abschnitt 7 korrigiert oder enger
  umbenennt.

Unter diesen Bedingungen untersucht Etappe 35 die Sensitivitaet einer
explizit heuristischen Buchwahl. Sie produziert weder eine neue Heim-Fassung
noch eine Massenprognose oder eine physikalisch validierte Ersatzfunktion.
