# Fester Buchfall: keine gemeinsame Loesung im geprueften Gleichungssystem

2026-09-06, Etappe32. Ausgang e24dc86, Plancheckpoint b56a0af,
Rechner-/Testcheckpoint851f7da.
Eigener mathematischer Nachweis; keine neue Heim-Regel oder Massenrechnung.

## 1. Ergebnis und Voraussetzungen

Fuer BEIDE unveraenderten Buchprofile aus dem Eingabecheckpoint05a0bab
existiert kein nichtnegatives ganzzahliges Besetzungstupel, das gleichzeitig
die direkten ungewichteten Strukturbedingungen107/107a und die als exakte
Gleichung behandelte108 erfuellt. Gemeint ist der nichtkollabierte Zweig.

Das erweitert FIND-040: Nicht nur die bisherige Greedy-Ausgabe(14,9,13,7)
scheitert. Auch eine andere gekoppelte Besetzungswahl kann dieses feste
Gleichungssystem nicht loesen. Fuer den Ausschluss genuegen bereits die
ersten ZWEI Strukturgates; die vierte Besetzung darf sogar beliebig reell
und nichtnegativ sein. Es wird kein bestpassendes Ersatztupel gesucht.

Fest bleiben Muster3, k=P=Q=kappa=q=1, C=0, epsilon=1, qx=-1, ResonanzN=0,
Q_j=(3,3,2,1), mathematisches pi/e/xi, die Buch-eta-Indizes,98c und109b,
Y3=Y9=1. Primarprofil: kleiner positiver105-Zweig. Separates zweites Profil:
Druckalpha exakt0.007297354572. Kein H006/H010-Konstantenimport.
Der aktive Pfad bleibt W=g*(1+eta11*A16), f(0)=0.

Der Buch-Eingabevertrag bleibt [hier](../04_reconstruction/alpha_audit/book_pseudosinglet_inputs.json)
unveraendert. Dies ist KEINE Aussage ueber andere Y-Werte, alle anderen
Teilchenfaelle, eine vollstaendige metronische Dynamik oder moderne Messdaten.

## 2. Quellen und bewusst erweiterter Bereich

H004 Druck278:98e definiert G2=N2(N2+1)(2N2+1)/6 und G3=N3(N3+1)/2.
Druck321:107 fordert delta1G1>G2 und delta2G2>G3.
Druck323:delta1G1=N1^3, delta2G2=N2^2, delta3G3=N3, delta4G4=1.
Druck322/328: N_j=n_j+Q_j ganzzahlig und>=0; nichtkollabiert beta_j>=1.
N1..N4 sind in diesem Bericht Kurzzeichen fuer N_(j), nicht ResonanzN.

Die notwendige Teilmenge der Bedingungen lautet somit

```text
N1,N2,N3 in den nichtnegativen ganzen Zahlen; N4 >= 0,
N1^3 > G2(N2),             N2^2 > G3(N3),
T = a1*N1^3 + a2*N2^2 + a3*N3 + exp(-N4/3) = W.
```

T bezeichnet die dimensionslose linke Seite von108, keine Teilchenmasse.
Die gepruefte Menge ist bewusst GROESSER als der volle strikte107-Zweig:
Der dritte Gate N3>N4, die zweite107-Reihe und unbekannte obereL-Grenzen
werden fuer den Beweis nicht gebraucht. Auch N4=0 bleibt enthalten.
Die strenge Realisierungsformulierung N_(j)(vx)>0 auf323 kann nur eine
kleinere Unterklasse liefern; sie ist nicht still vorausgesetzt.

Die spaetere sigma-Gleichsetzung107b wird nicht zur Umdefinition aller
Gates gemacht. Beta=0-Kollaps, G_j->0 und n_(j-1)->n_(j-1)+1 beschreiben
einen Prozess; es wird kein nicht belegtes Kollaps-Gleichungssystem erfunden.

## 3. Vollstaendigkeit ohne willkuerliche Suchgrenze

Aus Positivitaet und dem unten zertifizierten Energiebudget folgt N1<=14.
Dann liefern G2(20)=2870>14^3=2744 und G3(27)=378>19^2=361 die Grenzen
N2<=19, N3<=26. Mit dem dritten strikten Gate folgt N4<=25.
Damit waere [0,14]x[0,19]x[0,26]x[0,25] eine vollstaendige endliche
Obermenge fuer die urspruengliche Integerfrage, kein frei gewaehlter Cutoff.

Ein kuerzerer analytischer Beweis deckt sogar alle reellen N4>=0 ab:
stets 0<exp(-N4/3)<=1. Die folgenden fuenf Faelle sind erschoepfend.

| Fall | Notwendige Folge | Sichere Schranke fuer T |
|---|---|---|
| N1>=15 | Positive Summanden | T>=3375*a1>W |
| N1<=13 | G2(19)=2470>2197, also N2<=18; G3(25)=325>324, also N3<=24 | T<=2197*a1+324*a2+24*a3+1<W |
| N1=14,N2>=10 | Positive Summanden | T>=2744*a1+100*a2>W |
| N1=14,N2<=8 | G3(11)=66>64, also N3<=10 | T<=2744*a1+64*a2+10*a3+1<W |
| N1=14,N2=9 | G3(13)=91>81, also N3<=12 | T<=2744*a1+81*a2+12*a3+1<W |

G2 und G3 wachsen auf den nichtnegativen Integern; jeder erste verbotene
Wert schliesst auch alle groesseren aus. Fuer die Energieobergrenzen werden
nur positive Koeffizienten benutzt. Kein Fall kann T=W liefern.

## 4. Nachvollziehbare rationale Zertifikate

Der neue [Zertifikatsrechner](../scripts/audit_coupled_existence.py) berechnet
die festen Buchformeln mit ausschliesslich exakten rationalen Einschluessen:

- pi=16*atan(1/5)-4*atan(1/239), je48 alternierende Terme samt naechstem Term.
- e und exp(1/3): Taylorpolynom bis Grad64; positiver Rest hoechstens
  next_term/(1-x/66). Kehrwert liefert exp(-1/3).
- Quadratwurzeln: ganzzahliges isqrt mit nachweislich unteren/oberen Grenzen.
- Jede Intervalloperation wird nach aussen auf das rationale Gitter10^-40
  erweitert. Kein Maschinen-float oder gerundeter Messwert bildet den Beweis.
- Alpha: kleiner Zweig sqrt((1-sqrt(1-4*R^2))/2), mit zertifiziertem0<R<1/2.
  Die direkte Form verbreitert hier Intervalle, verliert aber keine Einschliessung.
- Abhaengigkeiten zwischen Koeffizienten duerfen Intervalle verbreitern,
  nicht unberechtigt verengen. Beide Profile werden getrennt eingeschlossen.

Bereits diese sehr groben, exakt rationalen gemeinsamen Huellen reichen:

```text
0.996 <= a1 <= 0.9969,
1     <= a2 <= 1.0126,
0.978 <= a3 <= 0.9787,
2830.26 <= W <= 2831.
```

Die Huellen sind bewiesene Einschliessungen, weder neue Eingaben noch
physikalische Fehlertoleranzen. Im letzten Fall ist damit

```text
T <= 0.9969*2744 + 1.0126*81 + 0.9787*12 + 1
  = 2830.2586 < 2830.26 <= W.
```

Der Abstand betraegt schon mit diesen groben Grenzen7/5000=0.0014.
Alle fuenf positiv orientierten Margen des Root-Zertifikats sind
1061/2,574999/2000,253/125,19173/1000,7/5000.

Die unabhaengige Numerikreview umschliesst beide Profile nochmals enger:

| Groesse | Exakte rationale Untergrenze | Exakte rationale Obergrenze |
|---|---:|---:|
| a1 | 0.996881270553 | 0.996881270554 |
| a2 | 1.012592613788 | 1.012592613789 |
| a3 | 0.97865878985 | 0.97865878994 |
| W | 2830.263257664 | 2830.263257669 |

Daraus folgen fuer dieselben fuenf Faelle positive Mindestabstaende von
534.211030447375,287.547288430666,6.438210107232,19.228536081928 und
0.057144067635. Insbesondere gilt fuer alle Kandidaten, die die ersten
beiden Gates erfuellen (sogar mit beliebig reellem N4>=0),
abs(T-W)>=0.057144067635>0.057. Dies gilt nicht pauschal fuer jedes
gate-verletzende Element der groesseren rechteckigen Integerbox.
Das ist keine optimierte Minimalabweichung,
kein Massenfehler und keine Erlaubnis, eine entsprechend grosse Toleranz zu setzen.

## 5. Aussagegrenzen und neuer konkreter Quellenanschluss

Mindestens eine Voraussetzung des festen exakten Pakets muss aufgegeben
oder anders begruendet werden, wenn eine Loesung entstehen soll. Allein
eine geschicktere Ganzzahlauswahl reicht nicht. Welche Voraussetzung
physikalisch oder historisch zu revidieren waere, entscheidet dieser Beweis nicht.

WICHTIG: H004322 bezeichnet die Herleitung des Exponentialverlaufs selbst
als Anwendung der Approximationen79b/79c im dritten Gueltigkeitsbereich.
108 ist also keine hier bewiesene exakte Vollbeschreibung metronischer Physik.
Die Zertifikate behandeln die festgelegte skalare108 als exakte Gleichung.
Das ist eine mathematisch klare Lesart, keine Wegerklaerung der Quellennaeherung.
Auch Y9=1 ist weiterhin die Tabellenannahme, keine unabhaengige Deduktion.

Bei FESTEM W/a1/a2/a3 schliesst der Beweis sogar jeden Ersatz des letzten
Summanden durch irgendeinen Wert in[0,1] aus. Eine verbesserte Externzonen-
Herleitung koennte aber zugleich den Referenzterm in g und damit W aendern.
Dann darf man nicht nur eine Seite korrigieren und den alten Ausschluss
unveraendert uebertragen. Das ist der naechste konkrete Quellenauftrag:
79b/79c ->322/323 ->g/108 auf Geltungsbereich, gemeinsame Normalisierung
und begruendete Fehlergrenzen pruefen. Kein eigener Fit oder Reparaturterm.

Die historische Frage bleibt [gesondert offen](../03_notes/HISTORICAL_OPEN_SELECTION_2026-09-06.md):
Heim benennt unvollendete F_im/110d-Grundlagenarbeit; sein Wissen um diesen
konkreten107-Konflikt oder ein ungeloster Stand bis Lebensende ist nicht belegt.

## 6. Reproduktion und Sicherung

```powershell
py -3.13 -B scripts/audit_coupled_existence.py --check --verify-sources
py -3.13 -B -m unittest discover -s tests -p test_coupled_existence.py -v
py -3.13 -B -m unittest discover -s tests -q
py -3.13 -B scripts/validate_finding_register.py
```

16 neue Tests,288 insgesamt; zwoelf bisherige Snapshotchecks bestanden.
Der neue Zertifikatscheck schreibt keine Dateien und ist kein13.Zahlensnapshot.
Tests pruefen auch alle die ersten beiden Gates erfuellenden Tripel innerhalb
der hergeleiteten endlichen Box, mit ueber[0,1] relaxiertem vierten Summanden;
kein N4- oder Restminimumsfit.

Drei interne Reviews (SOURCE/MATH/NUMERICS) wurden von Root vollstaendig
gelesen; beide selbstenthaltenen Python-Kontrollbloecke erneut erfolgreich
ausgefuehrt. Die unabhaengige Numerik verwendet eine rationalisierte
Alphaform sowie zusaetzlich Decimal-Fixpunktrechnung120/160. Letztere ist
nur Gegenkontrolle; der Nachweis stammt aus Fraction-Intervallen.
Root wiederholte zudem26 vollstaendige Intervall-Einschlussvergleiche
beider Rechenwege und143 rationale Wurzelkontrollen erfolgreich.
Die Abschlussgegenlesung praezisierte den Abstandssatz ausdruecklich auf
gate-erfuellende Kandidaten, nicht alle Elemente der groesseren Integerbox.
Interne Gegenreviews sind kein externes PeerReview.

Alle bisherigen Rechner, Eingaben, Snapshots und49CSV-Normalisierungen
bleiben unveraendert. FIND-042 ist eine Verstaerkung des bedingten Befunds,
nicht ein42.mal unabhaengig gezaehlter Fehler. Quellenumfang und Zuschreibung:
[COUPLED_EXISTENCE_SOURCES](../03_notes/COUPLED_EXISTENCE_SOURCES_2026-09-06.md).
