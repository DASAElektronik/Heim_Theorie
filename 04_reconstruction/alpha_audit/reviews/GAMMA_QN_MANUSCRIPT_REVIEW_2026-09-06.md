# `Gamma`, `Q(N)`, Bandbreite und Anregung in H013/H014

## 1. Scope und Ergebnis

Diese Review verfolgt eng den Anregungsblock des undatierten,
autorbezeichneten Typoskripts H013
(`J0033-Heim_Ausgewaehlte-Ergebnisse-b.pdf`): `f(N)`, (14c)/(14d), die
Ergaenzungsseiten, die spektrale Grenze, `K_B`, `T_N` und die spaetere
numerische Anwendung. H014
(`J0032-Heim_Ausgewaehlte-Ergebnisse-a.pdf`) wird als getrennte und
ebenfalls undatierte Fassung geprueft. Dateinamen, Uploadpfade,
Seitenumfang und die Buchstaben `a/b` werden nicht chronologisch
interpretiert.

Das Ergebnis ist eindeutig begrenzt:

* H013/H014 geben mit (14c) die Form
  `Q(N)=Q(0)+2 z(N)` an. Die Funktion `z(N)` wird aber nicht bestimmt.
  H013 rechnet spaeter ausdruecklich nur mit der Approximation `z=0`, also
  `Q(N)=Q(0)=Q`. H014 bezeichnet `z` in einer spaeteren Passage fuer den
  Anregungsfall als positiv ganzzahlig, liefert aber ebenfalls keine
  Auswahlfunktion.
* (14d) ist eine Monotonie-/Auswahlbedingung fuer **stufenweise**
  Anregungen. Eine beigefuegte Ergaenzungsseite stellt klar, dass Terme,
  welche (14d) verletzen, nicht fuer nichtexistent erklaert werden,
  sondern nur in einem einzigen energetischen Vorgang, eventuell einem
  Resonanzvorgang, erreichbar sein sollen. Diese zweite Klasse wird durch
  ein unterstrichenes `N` bezeichnet.
* `K_B` wird in H013 zwar „Bandbreite“ genannt, ist dort aber eine ganze
  Zahl, welche die Anzahl moeglicher Externfeldanregungen angibt. Weder
  diese Definition noch eine andere gepruefte Autorenstelle setzt `K_B`
  mit der in H006 benannten vollen Bandbreite `Gamma` gleich.
* Eine Gleichung fuer `Gamma`, eine Funktion `F(Gamma)` oder eine
  Lebensdauer-Breiten-Beziehung erscheint im geprueften H013/H014-Block
  nicht. `T_N` bleibt fuer `N>0` nach H013 ausdruecklich unbekannt.

Damit schliesst der Autorentext die alte kombinierte
`Gamma/Q_N`-Bestimmungsluecke nicht. Er liefert eine Paritaetsform fuer
`Q(N)`, eine Zugangs-/Ordnungsregel und diskrete Anregungsgrenzen, aber
keine eindeutige Funktion `z(N)` und keine Breitenbeziehung.

## 2. Grundzustand, Anregungsordnung und `f(N)`

H013 Druck 13 / PDF 14 unterscheidet den Grundzustand `N=0` von den
natuerlichen Zahlen `N>=1`, welche moegliche Anregerstufen dieses
Grundzustandes darstellen. Auf Druck 17 / PDF 18 steht in (11)

```text
w = W_(N=0) [1 + f(N)],
```

wobei `f>0` fuer `N>0` als Anregerfunktion und `W_(N=0)` als vom
Anregungszustand unabhaengiger Faktor bezeichnet wird. H013 Druck 19 /
PDF 20 gibt dann

```text
f(N) = a N/(N+1) + b N.                                      (14)
```

Die anschliessenden Beziehungen (14a)-(14b1) bestimmen die Hilfsgroessen
`a`, `b` und `C` aus den Zustandsparametern. Direkt nach dieser Kette,
H013 Druck 20 / PDF 21, sagt der Text jedoch, diese Beziehungen seien
„vorerst noch nicht ganz gesichert“. `f(N)` ist somit eine explizite
Anregerfunktion, aber keine unabhaengig validierte oder vollstaendig
gesicherte Dynamik der Anregung.

H013 Druck 22 / PDF 25 legt eine wichtige Notationskonvention fest:
Fehlt bei `Q` die Angabe `Q(N)`, dann bezieht sich `Q` stets auf `N=0`.
Fuer vorgegebene Grundzustandszahlen, eine Anregungsordnung `N` und das
Vorzeichen `epsilon` soll mit (11a)-(14b1) zunaechst `w` bestimmt und
daraus per Exhaustionsverfahren `n,m,p,sigma` ermittelt werden. Diese
algorithmische Aussage ersetzt aber nicht die noch offene Wahl von
`Q(N)`.

## 3. `Q(N)` und die offene Funktion `z(N)`

H013 Druck 20 / PDF 21 bezeichnet `Q` als doppelte
Drehimpulsquantenzahl und motiviert, dass sich `Q(N=0)` bei Anregung um
gerade Zahlen aendern koenne. Gleichung (14c) lautet:

```text
Q(N) = Q(N=0) + 2 z(N).                                      (14c)
```

Unmittelbar danach wird `z(N)` eine „ganzzahlige Beziehung“ genannt und
als „noch voellig unbekannt“ bezeichnet. Die Formel sichert daher nur,
dass `Q(N)` und `Q(0)` dieselbe Paritaet haben, solange `z(N)` ganzzahlig
ist. Sie bestimmt weder den Wert noch Verlauf oder Monotonie von `z(N)`.

H013 Druck 36 / PDF 39 bestaetigt die Luecke bei der Anwendung:
`z(N)` muesste fuer `N>0` bekannt sein; da sie nicht gegeben sei, bleibe
auch `Q(N)` vorerst unbekannt. Die dort berichtete Rechnung setzt

```text
z(N) = 0 fuer alle N,
also Q(N) = Q(0) = Q,
```

als **Approximation**. Der behauptete Approximationsfehler unter
`0,1 MeV` ist eine Aussage des Manuskripts, keine in dieser Review
nachgerechnete Schranke.

H014 besitzt dieselbe Gleichung (14c) und nennt `z(N)` am unmittelbaren
Formelort ebenfalls ganzzahlig und voellig unbekannt (Druck 15 / PDF 17).
Eine spaetere H014-Passage, Druck 26 / PDF 28, sagt dagegen, von `z` sei
„nur bekannt, daß es sich um positive ganze Zahlen handelt“. Im Kontext
geht es um die noch zu untersuchenden Anregungsspektren, also `N>0`.
Quellengetreu ist daher festzuhalten:

* H013: am Formelort ganzzahlig/unbekannt; keine positive Domain genannt;
* H014: am Formelort ebenso, spaeter fuer den Anregungskontext positive
  ganze Werte, aber weiterhin keine Funktion;
* keine dieser Aussagen darf auf H007, H006 oder eine andere Fassung
  uebertragen werden.

H014 Druck 26 / PDF 28 erklaert gerade wegen der ungesicherten wahren
Feinstrukturkonstante und des Auftretens von `z(N)`, dass die
Anregungsspektren noch numerisch zu untersuchen blieben. Anders als H013
enthaelt die gepruefte H014-Fassung keinen spaeteren Resonanzblock, der
`z=0` als numerische Approximation auswertet.

## 4. Die Monotoniebedingung (14d) und zwei Arten von `N`

H013 Druck 20 / PDF 21 begruendet (14d) mit der Forderung, eine Anregung
muesse den Energieinhalt und damit die Masse erhoehen:

```text
M(N_B) - M(N_A) > 0,    N_B > N_A.                            (14d)
```

Liegen zwischen `N_A` und `N_B` Ordnungen `N_gamma` mit

```text
N_A < N_gamma < N_B,
M(N_gamma) - M(N_A) < 0,
```

so werden diese Zwischenordnungen im Haupttext durch das Energieprinzip
ausgeschlossen. In dieser ersten Form wird (14d) als Auswahlregel der
Anregungsordnung gelesen.

Die unmittelbar beigefuegte Ergaenzung H013 Druck 20a / PDF 22 begrenzt
diese Aussage: (14d) gelte nur fuer stufenweise Anregungen. Terme, welche
(14d) nicht genuegen, seien deshalb nicht notwendig nichtexistent. Ihr
durch `N` bezeichnetes Niveau koenne nur durch einen einzigen
Anregungsprozess des Grundzustandes erreicht werden; die gesamte Energie
muesse in einem einzigen Prozess, eventuell einem Resonanzvorgang,
zugefuehrt werden.

Das Manuskript unterscheidet daraufhin typographisch:

* normales `N`: Spektrum moeglicher stufenweiser Anregungen, die (14d)
  genuegen;
* **unterstrichenes** `N`: Terme, die nicht stufenweise, sondern nur durch
  einen einzigen energetischen Vorgang entstehen koennen.

H014 Druck 15a / PDF 18 enthaelt denselben Ergaenzungstext und dieselbe
Unterstreichungskonvention. Diese Einteilung ist eine Quellenbehauptung
ueber den Zugang zu einem Niveau; sie ist weder eine Formel fuer dessen
Existenzzeit noch fuer die in H006 benannte volle Bandbreite `Gamma`.

H013 Druck 37 / PDF 40 wendet die Typographie auf die Tabellen IV-Vb an:
Die `N`-Angaben der dritten Spalte unterschieden normales und
unterstrichenes `N`; die Unterstreichung bedeute, dass der Term (14d)
nicht genuege. Die betreffenden Terme bleiben trotzdem tabelliert. Die
Tabellierung ist daher kein Beleg dafuer, dass alle Eintraege die
stufenweise Auswahlregel erfuellen.

## 5. Spektrale Grenzen und die diskrete „Bandbreite“ `K_B`

H013 Druck 21 / PDF 23 schliesst eine Massendivergenz
`M(N)->infinity`, damit auch `N->infinity`, aus und setzt fuer endliches
`N` eine obere Grenze

```text
0 <= N <= L_(N) < infinity.                                  (15)
```

`L_(N)` soll in (11) eine Maximalbesetzung aller vier Strukturzonen
kennzeichnen. Gleichung (15a) bestimmt die Anregergrenze, indem die
Maximalbesetzungen `L_(n)`, `L_(m)`, `L_(p)`, `L_(sigma)` in die linke
Seite von (11) eingesetzt und der rechten Seite

```text
W_(N=0) [1 + a L_(N)/(1+L_(N)) + b L_(N)]
```

gleichgesetzt werden. Dies ist eine endliche Grenze im diskreten
Anregungsraster, keine Breite einer Spektrallinie.

Auf derselben Seite definiert (14e)

```text
K_B = L_(sigma)(p_N) - sigma_N.                               (14e)
```

Der Haupttext nennt `K_B` eine von null verschiedene ganze Zahl und
„Bandbreite“, welche die **Zahl moeglicher Externfeldanregungen** eines
Anregungszustandes `M(N)` angibt. Die Korrekturseite H013 Druck 21a /
PDF 24 streicht die urspruengliche Nebenbedingung, `N` muesse nach (14d)
erlaubt sein, und ersetzt sie durch eine Vorzeichenregel:

* `K_B=0`: keine Moeglichkeit einer externen Anregung;
* `K_B<0`: ebenfalls keine solche Moeglichkeit; der Term strebe vor dem
  Zerfall durch Emission zunaechst das tiefste Niveau `K_B<0` an;
* nur `K_B>0`: Moeglichkeit einer externen Anregung nach (14e).

Diese korrigierte Lesart macht `K_B` zu einem diskreten
Zugaenglichkeits-/Zaehlerparameter. Der unmittelbar folgende Text gibt
fuer das aequidistante Subraster den Termabstand `4 mu alpha_+` an, der
nach Quellenangabe `9,28718 Elektronen-Kilovolt` entspricht. Angegeben ist
damit ein Energieabstand der beschriebenen `K_B`-„Feinstruktur“; er wird
jedoch weder als die in H006 benannte volle Bandbreite `Gamma`
identifiziert noch mit `T_N` verknuepft. Der Zahlenwert ist hier nur
transkribierte Quellenangabe und wurde nicht nachgerechnet.

In der gelieferten H014-PDF folgt auf Druck 15a / PDF 18 unmittelbar
Druck 17 / PDF 19; eine Druckseite 16 ist im Scan nicht vorhanden. Daher
kann H014 an der korrespondierenden Stelle weder als zweite positive
Ueberlieferung noch als Gegenbeleg fuer (14e) verwendet werden. Ob die
Seite in dieser Fassung fehlte oder nur im bereitgestellten Scan fehlt,
bleibt offen.

## 6. `T_N` schliesst keine Breitenbeziehung

H013 Druck 29 / PDF 32 fuehrt `T_N=T(N)<=T` als eine von `N` abhaengige,
noch unbekannte und ebenfalls zeitdimensionierte Funktion ein; fuer den
Grundzustand wird `T_0=0` gesetzt. In (21) bewirkt fuer `N>0` der Selektor
`delta(N)=0`, dass lediglich `T=T_N` folgt. Der Text nennt `T_N` damit
die Existenzzeit kurzlebiger Anregungen und Resonanzen.

H013 Druck 36 / PDF 39 sagt jedoch ausdruecklich, die Existenzzeiten
solcher Zustaende `N`, also `T_N`, koennten noch nicht beschrieben werden;
Druck 37 / PDF 40 nennt `z(N)` und `T_N` weiterhin unbekannt. Die
Bezeichnung einer unbekannten Groesse als Existenzzeit ist keine
Bestimmung ihrer Werte und keine Ableitung einer Linienbreite.

H014 enthaelt in der geprueften Fassung keinen entsprechenden
Lebensdauerblock. Sein Anregungsansatz (14) und die Bedingung (14d) liefern
daher ebenfalls keinen `T_N`- oder Breitenanschluss.

## 7. `Gamma`: negativer, aber abgegrenzter Befund

Auf den vollstaendig visuell geprueften H013/H014-Seiten um (14)-(16),
den Ergaenzungsseiten, der H013-Lebensdauerkette und dem spaeteren
Anwendungs-/Grenzenabschnitt erscheint keine Groesse `Gamma`. Eine
Stichwortsuche diente nur der Seitennavigation: Beide PDFs sind
bildbasierte Scans ohne hinreichende Textschicht, so dass ein leerer
Suchtreffer kein dokumentweiter Negativbeweis ist. Tragend ist allein die
visuelle Pruefung der abgegrenzten Anschlusskette.

Das kleine griechische `gamma` erscheint an anderen Stellen als laufender
Index von Multiplettstrukturen (`x_gamma`) beziehungsweise in
Teilchenbezeichnungen. Es ist nicht als die in H006 benannte volle Bandbreite
definiert. Ebenso darf die deutsche Bezeichnung „Bandbreite“ fuer die
ganze Zahl `K_B` nicht allein aufgrund des Wortes mit `Gamma`
identifiziert werden.

Dieser Negativbefund gilt nur fuer die abgegrenzten Autorenfassungen und
die durchsuchte Definitionskette. Er ist keine Behauptung, dass im
gesamten Nachlass keine andere Gamma-Formel existiert.

## 8. Numerische Anwendung: Approximation und Auswahl aus Kandidaten

H013 Druck 36-37 / PDF 39-40 bezeichnet die Rechnung fuer `N>0` selbst
als unsicher und die Massenwerte als stark approximativ. Neben dem
unbekannten `z(N)` und `T_N` seien auch die Beziehungen (14a)-(14b1) noch
nicht sicher. Trotz `z(N)=0` gebe es wesentlich mehr theoretische
Anregerterme als empirisch gefundene Resonanzen.

Der Text sagt anschliessend, aus der relativ grossen Zahl numerisch
bestimmter moeglicher Zustaende seien diejenigen ausgewaehlt worden,
welche die empirischen Resonanzmassen offensichtlich verhaeltnismaessig
gut wiedergeben. Die Tabellen IV-Vb sind daher nach eigener Darstellung
eine ausgewaehlte Teilmenge unter einer `z=0`-Approximation, keine
erschoepfende Blindvorhersage aller Resonanzzustaende. Unterstrichene
`N`-Eintraege verletzen zudem (14d), bleiben aber wegen der
Ein-Prozess-Deutung im Tabellenbestand.

Diese Quellenangaben duerfen nicht in eine neue Datenpruefung umgedeutet
werden; die behauptete Uebereinstimmung und Fehlergroesse wurden hier
nicht nachgerechnet.

## 9. Abhaengigkeitskarte und Schlussantwort

Die in H013 tatsaechlich belegte Kette lautet:

```text
N=0: Grundzustand, Q=Q(0)
          |
N>=1: Anregungsordnung --> f(N)=aN/(N+1)+bN --> W=W0[1+f(N)]
          |
          +--> Q(N)=Q(0)+2z(N)       z(N) unbekannt
          |          |
          |          '--> in der Rechnung nur Approximation z=0
          |
          +--> (14d) Monotonietest fuer stufenweisen Zugang
          |          '--> Verletzer als unterstrichenes N,
          |               nur Ein-Prozess-Zugang behauptet
          |
          +--> L_(N), K_B: diskrete Grenzen/Anregungsmoeglichkeiten
          |
          '--> T_N: als Existenzzeit benannt, aber unbekannt

Gamma oder F(Gamma): keine Anschlussgleichung im geprueften Block
```

Die alte `Q_N`-Luecke wird also nur parametrisiert, nicht geloest:
`Q(N)-Q(0)` ist gerade, aber `z(N)` bleibt frei. Die Gamma-Luecke bleibt
vollstaendig offen. Weder `K_B` noch `L_(N)`, `f(N)` oder `T_N` liefert in
diesen Seiten die fehlende volle Breite.

## 10. Visuelle Pruefspur und Suchgrenze

Tragende Vollseitenbilder:

* `tmp/pdfs/eta22_context/j0033-render-20.png` - H013 Druck 19 / PDF 20,
  `f(N)` und (14a)-(14b1);
* `tmp/pdfs/eta22_context/j0033-render-21.png` - H013 Druck 20 / PDF 21,
  (14c), unbekanntes `z(N)` und (14d);
* `tmp/pdfs/eta22_context/j0033-render-22.png` - H013 Druck 20a / PDF 22,
  Ein-Prozess-Ergaenzung und normales/unterstrichenes `N`;
* `tmp/pdfs/eta22_roles/j0033-23.png` und `j0033-24.png` - H013 Druck
  21/21a / PDF 23/24, `K_B`, (15)/(15a) und Korrektur;
* `tmp/pdfs/eta22_roles/j0033-25.png` - H013 Druck 22 / PDF 25,
  Konvention `Q` ohne `(N)` und Exhaustionsverfahren;
* `tmp/pdfs/eta22_roles/j0033-hi-32.png` - H013 Druck 29 / PDF 32,
  Definition und Rolle von `T_N`;
* `tmp/pdfs/eta22_roles/j0033-limit-39.png` und
  `j0033-limit-40.png` - H013 Druck 36-37 / PDF 39-40,
  `z=0`-Approximation, unbekannte `Q(N)`/`T_N`, Kandidatenauswahl und
  Unterstreichungskonvention;
* `tmp/pdfs/eta22_roles/j0032-phi-context-15.png` und
  `j0032-phi-context-16.png` - H014 Druck 15/15a / PDF 17/18,
  (14c)/(14d) und Ein-Prozess-Ergaenzung;
* `tmp/pdfs/eta22_roles/j0032-28.png` - H014 Druck 26 / PDF 28,
  positive Ganzzahligkeit von `z` im Anregungskontext und fortbestehender
  Untersuchungsbedarf.

Die Untersuchung war auf die unmittelbare Anregungs-, Auswahl-, Grenzen-
und Lebensdauerkette begrenzt. Es wurden keine Resonanzwerte neu
gerechnet, keine moderne Vergleichsliteratur gesucht und keine
Gamma-Lebensdauer-Beziehung aus externer Physik in den Autorentext
eingesetzt.
