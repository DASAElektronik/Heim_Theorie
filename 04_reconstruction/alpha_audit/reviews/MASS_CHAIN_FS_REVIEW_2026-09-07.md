# Herkunft und Empiriestatus von `F_S` und `phi` in der Buchfassung

Stand: 2026-09-07. Begrenzter Originalreview der Massenkette um (97),
(98d/e) und (111)--(112). Keine heutigen Messdaten, keine Neufits und keine
neue Bewertung der mehrdeutigen `f`-Stelle auf Druck 343.

## 1. Kurzergebnis

Die Buchfassung trennt drei Schritte:

1. (97) legt die Massenskalen fest, insbesondere
   `mu_+=4*mu*alpha_+` und
   `mu_S=(1-alpha_-/alpha_+)*mu_+`.
2. (98d) fuehrt `F_S` als additiven Beitrag in der Massenklammer ein.
   Druck 323 erklaert `F_S` fuer die dortige Besetzungsvariation als von
   den `n_j` unabhaengig, so dass `delta F_S=0` gilt. Damit ist `F_S` kein
   Bestimmungsstueck der aus dieser Variation gewonnenen Auswahlgleichung.
3. Druck 342 gewinnt `F_S` nach der Besetzungsauswahl aus den bereits
   zugeordneten empirischen Massen `M_emp`. Die anschliessende Form
   (111)/(111a,b) ist ausdruecklich so vorgeschlagen, dass sie 17 derart
   gewonnene Punkte trifft und fuer weitere Komponenten plausible Werte
   liefert.

Die 17 Werte sind daher Kalibrierungs-/Rekonstruktionsdaten der
`F_S`-Funktion, nicht 17 unabhaengige Vorhersagen derselben Formel. Die
Fortsetzung auf noch nicht belegte Komponenten hat in der Quelle den Status
einer mit derselben Form erzeugten Plausibilitaetsextrapolation. Druck 344
beansprucht danach zwar eine numerische Spektralfunktion fuer alle Massen;
auf den geprueften Seiten wird deren `F_S`-Anteil aber nicht unabhaengig von
den 17 Ausgangsmassen hergeleitet.

## 2. Quelle und visueller Umfang

Primärquelle:

`01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`

SHA-256:
`F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.

Vollstaendig visuell gelesen:

- Druck 253 / PDF 259: (97), `mu_+`, `mu_S`;
- Druck 276--279 / PDF 282--285: Anschluss und (98b)--(98e);
- Druck 323 / PDF 329: `delta F_S=0` in der Besetzungsvariation;
- Druck 342--344 / PDF 348--350: empirische Extraktion, Vorschlag
  (111)/(111a,b), algebraischer Faktor 4 und (112).

Arbeitsbilder:

- `tmp/pdfs/mass_chain_fs/edm2-259.png`;
- `tmp/pdfs/mass_chain_fs/edm2-282.png` bis `edm2-285.png`;
- `tmp/pdfs/coupled_existence/edm2-329.png`;
- `tmp/pdfs/mass_chain_fs/hi-348.png`, `hi-349.png` und
  `tmp/pdfs/eq108_status/edm2-350.png`.

OCR diente nur zum Auffinden von (97). Alle tragenden Formeln und
Satzanschluesse wurden am Seitenbild gelesen.

## 3. (97): die Massenskalen

Druck 253 setzt unter anderem

```text
mu_(+/-) = 4*mu*alpha_(+/-),
mu_S  = (1-alpha_-/alpha_+)*mu_+ .                (97)
```

Die erste Zeile ist mit dem gemeinsamen `+/-`-Index gedruckt; fuer die
spaetere Umformung wird ihr Plusfall benutzt:

```text
mu_+ = 4*mu*alpha_+ .
```

`mu_S` ist damit keine von `mu_+` unabhaengige spaetere Fitskala. Ihre
algebraische Beziehung steht bereits in (97). Die Seite ordnet die Formeln
reinen Zahlen `eta` und `xi` aus (28a)/(96b) zu, leitet aber auf dieser Seite
noch keine Funktion `F_S(k,P,Q,kappa,q)` her.

## 4. (98d/e): `F_S` ist Teil des Massenansatzes

Druck 278 fasst die vorlaeufige Wirkung des Termselektors zusammen als

```text
M(c,d) = mu_+ * [
    sum_(j=1)^4 alpha_j*G_j
  + (1-alpha_-/alpha_+)*F_S
  + q*alpha_-/alpha_+
] .                                                (98d)
```

(98e) definiert anschliessend die Zonenfunktionen `G_j` aus den
Besetzungen `N_(j)` und ihren Dichtefaktoren. Fuer die vorliegende Frage ist
entscheidend: `F_S` steht in (98d) ausserhalb der Summe `sum alpha_j G_j`;
es ist weder eines der `G_j` noch eine der Besetzungen.

Der Prosatext unmittelbar nach (98e) bezeichnet die Beschreibung
ausdruecklich als noch nicht vollstaendig. Neben der Bestimmung von `F_S`
muesse erst eine Auswahlregel fuer die Konfigurationszonenbesetzungen und
ein kompletter Quantenzahlensatz gefunden werden. Die Quelle behauptet an
dieser Stelle also nicht, `F_S` sei schon deduziert.

In (98d) und (98e) kommt kein kleines Resonanz-`f` vor. Der Satz auf Druck
343, die `n_j` entstuenden nach (108) „unabhaengig von f“, kann daher nicht
durch eine dort wortgleich gedruckte Variable in (98d/e) aufgeloest werden.
Diese Review identifiziert das kleine `f` weder mit `F_S` noch mit `phi` und
verwendet den Satz nicht als Herkunftsbeleg.

## 5. Druck 323: Unabhaengigkeit nur in der definierten Variation

Druck 323 baut aus der Massenvariation und dem Externterm die
Auswahlgroesse `W` auf. Dabei werden die `n_j` einzeln variiert:

```text
delta_j N_(k) = delta_j n_k = delta_jk.
```

Die Quelle nennt `F_S` dort noch eine unbekannte Funktion. Bekannt sei nur,
dass sie in irgendeiner Form von den Quantenzahlen des betreffenden
`V6`-Punktes, auf keinen Fall aber von den `n_j` abhaenge. Fuer genau diesen
Differenzschritt setzt sie deshalb

```text
delta F_S = delta q = 0.
```

Damit verschwindet `F_S` aus der lokalen Besetzungsvariation, nicht aus der
Masse (98d). Der Satz bedeutet weder `F_S=0` noch, dass `F_S` fuer alle
verschiedenen Zustandsquantenzahlen denselben Wert habe.

Diese Druckstelle ist die direkte Grundlage fuer die Trennung von
Besetzungsauswahl und spaeterer `F_S`-Bestimmung. Das kleine `f` auf Druck
343 wird dafuer nicht benoetigt.

## 6. Druck 342: empirische Extraktion

Nach dem Exhaustionsverfahren rechnet Druck 342 zunaechst

```text
n_j = N_(j)-Q_j
```

zurueck und bestimmt damit die `G_j` in (98d/e). Fuer `N=0` betrachtet der
Text dann die 26 `V6`-Gitterpunkte und zunaechst die Groesse
`M_x-mu_S*F_S`. Er behauptet dabei `mu_S*F_S << M_x`.

Anschliessend wird `F_S` nicht aus einer neuen dynamischen Gleichung, sondern
aus den zugeordneten Messmassen geloest:

```text
mu_S*F_S = M_emp
  - mu_+*(sum_j alpha_j*G_j + q*alpha_-/alpha_+).
```

Dies ist die direkte Umstellung von (98d), nachdem die Besetzungen und der
restliche Massenanteil eingesetzt sind. Der empirische Input steht auf der
linken Seite der Herkunftskette: Ohne `M_emp` ergibt diese Gleichung an
dieser Stelle keinen Zahlenwert fuer `F_S`.

Die Quelle grenzt die Datenlage selbst ein:

- empirische `M_emp` und daraus gewonnene `F_S` laegen nur fuer Komponenten
  der Multipletts `v=1` bis `v=10` vor;
- die Komponente `e_0` in `v=2` werde ausgeschlossen;
- insgesamt seien dies 17 Messpunkte fuer `F_S`;
- gesucht werde ein Verlauf `F_S(k,P,Q,kappa,q)`, der diese 17 Punkte trifft
  und zugleich plausible Werte fuer `e_0`, `v=11` und `v=12` liefert.

Die gepruefte Passage listet die 17 Einzelwerte nicht tabellarisch auf.
Ihre Zahl und Rollenverteilung werden daher als Quellenangabe dokumentiert,
nicht als in dieser Review unabhaengig nachgezaehlter Datensatz.

## 7. Vorgeschlagene Form und die Faktoren `Y_41` bis `Y_44`

Druck 342 sagt, die gesuchte Funktion sei mit zwei Konstanten und vier
Hilfsfunktionen moeglich; die Verlaeufe sollen vorgeschlagen werden. Druck
343 beginnt mit der Aussage, die Formen haetten sich als besonders guenstig
erwiesen, wenn gesetzt werde:

```text
4*(1-alpha_-/alpha_+)*F_S
  = A_v*F_1*F_q*F_kappa/F_2 + B_v*(P+Q).
```

Zur Zusammenfassung mit dem Ladungsterm definiert die Quelle dann

```text
phi = A_v*F_1*F_q*F_kappa/F_2
    + B_v*(P+Q)
    + 4*q*alpha_-/alpha_+.                         (111)
```

Die Hilfsfunktionen in (111a) sind glyphentreu nach ihrer Struktur:

```text
F_1 = P*(P+Q)*(-1)^(P+Q)*(2-k+eta^3*(k-1)),

F_2 = 1 + 4*(xi/k)*binom(P,2)*(xi/6)^q*Y_41,

F_q*sqrt(eta_qk)
    = (3-alpha + (pi/2)*(k-1)*3^(2-q/2))
      *(2*sqrt(eta_11*eta_qk) + q*eta^2*(k-1)*Y_42),

F_kappa = 1 + (2*k*kappa/(3*eta^2))*xi
              *{1+pi*xi^2*(P-Q)*(pi-5*q/4)}*Y_43.  (111a)
```

Die zwei anschliessenden Konstantenbeziehungen lauten:

```text
beta*pi*A_v = (1-alpha_-/alpha_+)
  *{(pi/3)^2 + (eta/eta_11)^2*alpha/(3*xi)},

xi^2*B_v = alpha*(1-alpha_-/alpha_+)^2*Y_44.        (111b)
```

Damit sind die Rollen der vier `Y`-Faktoren lokal klar verteilt:

| Faktor | gedruckte Stelle |
|---|---|
| `Y_41` | Zusatzterm von `F_2` |
| `Y_42` | `q*eta^2*(k-1)`-Term im zweiten Faktor von `F_q` |
| `Y_43` | Korrekturterm von `F_kappa` |
| `Y_44` | Beziehung fuer `B_v` in (111b) |

Auf Druck 342 stehen unmittelbar vor (111) zunaechst dieselben
Hilfsfunktionen ohne `Y_41` bis `Y_43`. Dort erscheint ausserdem

```text
B_v = (1-alpha_-/alpha_+)^2*alpha*xi^(-2).
```

Der hochaufgeloeste Detailausschnitt zeigt im Exponenten eindeutig nur
`-2`; das zuvor in kleinerer Ansicht vermeintlich gelesene `kappa` ist nicht
gedruckt. Damit ist diese Grundform genau der Spezialfall `Y_44=1` von
(111b), keine zweite `B_v`-Fassung und keine lokale Formeldiskrepanz.

Die Seiten fuehren `Y_41`--`Y_44` in (111a/b) als zusaetzliche Faktoren ein,
geben in dem geprueften Dreiseitenblock aber keine Zahlenwerte an. Daraus
folgt **nicht**, dass vier voneinander unabhaengige freie Fitparameter
vorliegen. Der umliegende, bereits dokumentierte Buchkontext bezeichnet
solche `Y_k` als Unsicherheitsfaktoren; ihre konkrete Bindung ist eine eigene
Provenienzfrage, nicht durch blosses Auftreten in (111a/b) entschieden.

## 8. Woher der Faktor 4 und `phi` kommen

Der Faktor 4 ist in der geprueften Kette algebraisch nachvollziehbar und
nicht ein neuer Fitparameter. Aus (97) gilt

```text
mu_+ = 4*mu*alpha_+.
```

Setzt man dies in (98d) ein, folgt

```text
M = mu*alpha_+ * 4*[
    sum_j alpha_j*G_j
  + (1-alpha_-/alpha_+)*F_S
  + q*alpha_-/alpha_+
] .
```

Druck 343 definiert die letzten beiden vervierfachten Summanden gemeinsam
als `phi` und spaltet `4*sum alpha_j G_j` in einen zeitlich konstanten
Geruestanteil `K`, einen von `n_j` abhaengigen Anteil `F` und einen
gemischten Anteil `H`. Druck 344 schreibt daraus

```text
M(N) = mu*alpha_+*(K+F+H+phi).                     (112)
```

Der Uebergang von (98d) zu (112) ist insoweit eine algebraische Umgruppierung
mit den neu definierten Symbolen. Er verwandelt die empirische Herkunft des
in `phi` enthaltenen `F_S`-Anteils nicht in eine unabhaengige Deduktion.

Als separate Glyphenkontrolle liest diese Review in beiden auf Druck 344
gedruckten `K`-Darstellungen, oben im Satzanschluss und unten in (112a), den
zweiten Geruestterm gleich:

```text
N_2*Q_2*(2*Q_2^2 + 3*Q_2 + 1).
```

Es wurde an keiner der beiden Stellen `2*Q_2` als mittlerer Summand gelesen.

## 9. Behauptung, Rekonstruktion und Vorhersage sauber getrennt

### Von der Quelle definiert oder algebraisch umgestellt

- die Skalenrelationen in (97);
- `F_S` als additiver Massenbeitrag in (98d);
- die empirische Umstellung fuer `mu_S*F_S` auf Druck 342;
- die Definition von `phi` und die Zerlegung zu (112).

### Von der Quelle empirisch vorgeschlagen oder mit Unsicherheit versehen

- die 17 aus `M_emp` gewonnenen `F_S`-Werte;
- die Forderung, dass die vorgeschlagene Funktion diese Punkte trifft;
- die als besonders guenstig bezeichneten Hilfsfunktionen und Konstanten;
- die in (111a/b) auftretenden `Y_41`--`Y_44` als Unsicherheitsfaktoren;
  ihr Auftreten allein belegt keine vier unabhaengigen Fitfreiheiten.

### Von der Quelle als weiterer Anspruch formuliert

- plausible Werte fuer `e_0`, `v=11` und `v=12` aus derselben Funktion;
- auf Druck 344 die Moeglichkeit, mit (112) und dem Umfeld (108)--(111b)
  alle ponderablen Massen `M(N)` numerisch zu bestimmen.

Diese beiden Anschlussansprueche sind nicht dasselbe wie eine unabhaengige
Vorhersage der 17 Kalibrierungspunkte. Ob die extrapolierten Werte spaeter
experimentell bestaetigt wurden, wurde hier bewusst nicht untersucht.

## 10. Begrenzte offene Punkte

Im gesetzten Umfang bleibt offen:

- welche konkreten 17 Zahlenwerte und Messquellen eingesetzt wurden;
- wie `Y_41`--`Y_44` zahlenmaessig festgelegt wurden;
- worauf das kleine `f` im Satz auf Druck 343 genau rueckverweist.

Diese offenen Provenienzpunkte erlauben weder eine freie Neuanpassung noch
die Behauptung, `F_S` sei bedeutungslos. Der engste quellenfeste Schluss ist:
`F_S` bleibt ein wirksamer Bestandteil der Massenformel, wird aber fuer die
bekannten Komponenten aus denselben empirischen Massen extrahiert, die seine
vorgeschlagene Funktionsform treffen soll. Seine Rolle in der
Besetzungsauswahl ist durch `delta F_S=0` getrennt.
