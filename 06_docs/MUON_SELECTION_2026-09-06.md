# H006-Myoneintrag: W, Ganzzahlauswahl und verbleibender Rest

2026-09-06, Etappe26. Ausgang `e2eaad8`, Plancheckpoint `d960144`.
Vorab benannter Folgekandidat von Etappe25, nicht nach einem Zahlentreffer
gewaehlt. Keine neue Massenrechnung oder Messdatenanpassung.

## Ergebnis

Der Quellenanschluss gelingt bedingt: H006s Eintrag x3/mu- liefert fuer
beide formalen Komponentenstellen dieselben Ladungs- und W-Eingaben.
Unter den zwoelf vorab benannten Rekonstruktionsprofilen wird jeweils
Fall(b), 0<W4<1, erreicht. K1..3=(14,9,3) bleibt gleich; die zwei
A16-Slashlesarten liefern jedoch verschiedene K4. Nach Abschneiden bleibt
in beiden Faellen ein positiver dimensionsloser Rest der Auswahlgleichung.

Damit gibt es nun nicht nur den synthetischen Befund aus Etappe25,
sondern eine konkrete Anwendung auf den benannten H006-Tabelleneintrag
unter expliziten Normalisierungen. Nicht bewiesen sind eine eindeutig
autorisierte historische Auswertung, physikalische Myonidentifikation,
eine Myonmasse oder die Unloesbarkeit aller Zonen der Theorie.

## 1. Vom Tabelleneintrag zur Eingabe

H006 Druck/PDF3, (II)/(III), nennt x3(0111)_0(-1,-1), zieht dies zu
x3(0111)_0(-1) zusammen und bezeichnet es als mu--Pseudosingulett.
Aus den Definitionen auf S.2/3 folgen:

```text
epsilon=+1, k=1, B=0, P=1, Q=1, kappa=1, C=0
I=P+1=2; in (II) x=0,1
2*qx=(P-2x)[1-kappa*Q*(2-k)]
      +epsilon[k-1-(1+kappa)*Q*(2-k)]+C = -2
```

Also q0=q1=-1 und q=1. Kontrollanschluss fuer C: alpha_P=pi,
alpha_Q=0 gibt epsilon_P=-1,epsilon_Q=+1; der Ausdruck fuer C in (I)
wird wegen P*epsilon_P+Q*epsilon_Q=0 ebenfalls null. Seite2 spricht
zunaechst von 1..I; die hier verwendete Ladungsformel und Liste auf S.3
sind ausdruecklich nullbasiert. Keine stille globale Indexgleichsetzung.

Die vier Ziffern (0111) sind Konfigurationen, keine Besetzungen n_j.
Die gleichlautende Ladungsliste allein beweist nicht, was physikalisch
zusammengezogen wird. Fuer W gibt es unter diesem Vertrag jedoch keinen
weiteren unterschiedlichen x-Eingang: beide Stellen liefern dieselbe
Rechnung, ohne sie doppelt zu gewichten.

## 2. Was von W uebrig bleibt

Mit d=eta11, aber eta weiterhin unindiziert, liefern (XVII)/(XVIII):

```text
w1=(1-Q)[...]+kappa*Q*d*A16 = d*A16
w2=(q-1)A21+(1-P)A22+choose(P,2)[...]
   +kappa(A26+q*d^2*A31)+choose(Q,3)d*A32+choose(P,3)[...]
   = A26+d^2*A31
```

Fuer k=1 erklaert die Potenzregel samt Programmform unter (XIX)
w=1+w1. Daher:

\[
W=g(1,1)(1+dA_{16}),\qquad
g=27\alpha_1+9\alpha_2+2\alpha_3+e^{-1/3}.
\]

w2 beeinflusst hier nicht den Zahlenwert von w, muss aber definiert
bleiben. Im Hauptprofil: w2=0.28435454552308406, 1+w2>0.
Vor jedem Wegfall wurden die benoetigten Nenner geprueft. Beispielsweise
wird der XVIII-A24-Nenner genau1; der A36-Nenner ist etwa0.9912045986.
Die alternative XVI-Schreibweise 1-A24 ist ebenfalls nicht singulaer,
wird aber nicht in XVIII eingesetzt. Kein Wegkuerzen von 0*undef.

N=0=>f=0 ist eine separate Aussage auf S.8, nicht das Elektronargument
kappa=0. Der allgemeine Resonanzbeitrag verschwindet fuer x3 nicht schon
fuer alle N. Verwendet wird der gruppierte XV/XXVI/XXX/XXXI-Teilpfad;
H006s abweichendes XIV bleibt als dokumentierter Versionsbefund bestehen.

## 3. Lesarten und numerischer Befund

H006 S.7/(XXIV) druckt A16 kompakt mit dem Schluss /5 eta. Die bereits
bestehende Nennerprodukt-Normalisierung ist unser Default P. L ist die
vorab benannte linkassoziative Sensitivitaet:

\[
A_{16}^{P}=(\pi e)^2\left[1+\frac{\alpha(1+6\alpha/\pi)}{5\eta}\right],
\quad
A_{16}^{L}=(\pi e)^2\left[1+\frac{\alpha(1+6\alpha/\pi)}5\eta\right].
\]

Jeweils drei alte Zahlenprofile (M/G/D) und zwei bestehende H006-
alpha3-Wurzelweiten sqrt(xi*d) bzw. sqrt(xi)*d wurden gerechnet.
Der nackte Alpha-Wert stammt in allen Zellen aus `1982_source_literal`
mit eta12=(k=1,q=2), nicht aus einer Messzahl. Vollstaendiger Vertrag:
[NORM-MUON-SELECTION-AUDIT](../04_reconstruction/alpha_audit/NORM-MUON-SELECTION-AUDIT.md).

Haupt-Zahlenprofil M (mathematisches pi/e, xi=1.61803399) und
Default-Wurzel sqrt(xi*d), gerundet:

| Groesse | A16-P: /(5eta) | A16-L: (/5)*eta |
|---|---:|---:|
| W | 2820.983346865665 | 2820.900627767596 |
| W4 nach K1..3=(14,9,3) | 0.775503922089 | 0.692784824019 |
| reelles K4=-3ln(W4) | 0.762726716645 | 1.101107481773 |
| K4 nach Abschneiden | 0 | 1 |
| n=K-(3,3,2,1) | (11,6,1,-1) | (11,6,1,0) |
| R=exp(-K4/3)-W4 | +0.224496077911 | +0.023746486554 |

Alle sechs P-Zellen liefern dasselbe K-/n-Tupel, ebenso alle sechs
L-Zellen. Konstanten- und Wurzelachse aendern diese Entscheidungen in
keiner der untersuchten Zellen. Die vollstaendigen zwoelf Zeilen stehen
in der unabhaengigen Numerikreview und alle Zwischenwerte im neuen
[Snapshot](../05_analysis/muon_selection_results.json). Es wird keine
Variante wegen ihres kleineren Rests bevorzugt.

Hauptprofil-Zwischenwerte: alpha1=0.99688127055316836,
alpha2=1.01259261378872802, alpha3=0.91521160959849895,
A16=73.03605945222875288, g=38.57608235880488516.
Die sukzessiven Restziele sind W2=85.54114046777117,
W3=3.5211387508841963 und obiges W4. Nicht mit Strukturpotenzen w1/w2
verwechseln: die gleich aehnlichen Kurzzeichen haben verschiedene Rollen.

## 4. Ganzzahlregel, Gleichung und Grenzen

Fuer r=W4 und reelles x=-3ln(r) gilt exp(-x/3)=r. Fuer j=floor(x)
und theta=x-j folgt dagegen exakt, wie in Etappe25 bewiesen:

\[
R=e^{-j/3}-r=r(e^{\theta/3}-1),\quad
0\le R<1-e^{-1/3}.
\]

Null gilt genau bei ganzzahligem x. Die hier beobachteten x liegen
nicht nahe einer Ganzzahl; der kleinste Abstand aller zwoelf Profile
betraegt etwa0.1010593. Der numerische reelle Umkehrrest geht mit hoeherer
Praezision gegen die Rechenauflosung; der Rest nach Ganzzahlauswahl bleibt
etwa0.2245 bzw.0.02374. Mehr Rechengenauigkeit ist daher kein beobachteter
Reparaturmechanismus fuer diesen Abschneideschritt.

Beide Strukturbedingungssaetze wurden getrennt ausgewertet:
XIII mit der gedruckten rechten alpha3*K1^3, XXXII mit seiner eigenen
alpha1-Grenze. Saemtliche Abstaende sind strikt positiv in den
Dezimalauswertungen; kleinster Abstand etwa1.7456348. Kein beobachteter
Gleichheitsrand liefert hier einen Anlass, die auf S.10 beschriebene
Zonenuebertragung einzufuegen. Damit ist keine allgemeine Dynamik bewiesen.
Auch n4=-1 ist im Quellenbereich n4>=-Q4 erlaubt, kein negativer
Strukturzaehlwert: K4=n4+Q4=0.

Dieser Rest ist weder ein relativer Massenfehler noch eine gemessene
Abweichung. Die Zaehldeutung kann eine diskrete Auswahlvorschrift
motivieren; sie ist nicht automatisch eine exakte Loesung der gedruckten
Gleichung. Eine benoetigte Ersatzrelation oder Fehlerabschaetzung muesste
separat hergeleitet werden, nicht von uns still ergaenzt.

## 5. Gegenpruefung und Speicherung

- Komponentenreview, W-Quellenreview und unabhaengige Numerikreview in
  `04_reconstruction/alpha_audit/reviews/MUON_*_2026-09-06.md`.
- Root las die tragenden Vollseiten und alle Reviewableitungen selbst.
  Der unabhaengige Code verwendet Machin-pi, inverse Viertelwurzeln,
  eigene Alpha-Fixpunktiteration und algebraisch reduzierte A26/alpha3.
  Kein bestehender Massenevaluator oder fremdes Programm wurde benutzt.
- Root fuehrte den unabhaengigen Reviewcode erneut aus: 120/160 Stellen,
  648 Feldvergleiche, groesster absoluter Unterschied <1.703e-115.
  Vergleich mit Root-Code: 252 gemeinsame skalare Felder,
  groesster absoluter Unterschied <1e-115; alle K-/n-Tupel gleich.
- Root-Tests vergleichen 80/120 Stellen, numerische Felder absolut
  <1e-70 verschieden, alle K-/n-Tupel stabil. Das ist kein vollstaendiger
  Intervallbeweis fuer die transzendenten Eingaben und keine physikalische
  Unsicherheitsrechnung. Der Status bleibt explizit bedingt.
- 15 neue Tests, 214 insgesamt; elf Snapshotchecks einschliesslich der
  zehn alten samt jeweiliger Quellpruefung bestanden. Register separat
  geprueft. Alte Rechner, Inputs, Snapshots und 49 CSV-Normalisierungen
  bleiben erhalten. Die alte Elektron-N0-Identitaet K4=1 wird nicht beruehrt.

Nachrechnen:

```powershell
py -3.13 -B scripts/audit_muon_selection.py --check --verify-sources
py -3.13 -B -m unittest discover -s tests -p test_muon_selection.py -v
py -3.13 -B scripts/validate_finding_register.py
```

FIND-036 ist eine bedingte Rekonstruktions-/Auswahlbefundgruppe;
36 Gruppen bedeuten weder36 Fehler noch36 unabhaengige Experimente.
Heims Quellenideen bleiben ihm zugeschrieben. Die Normalisierung,
Sensitivitaetsmatrix, Restrechnung und Software sind unsere Arbeit.
Interne Agentenreviews ersetzen kein externes Peer Review.

## 6. Naechster begrenzter Auftrag

A16 quellenhistorisch klaeren, bevor aus einer Besetzung eine Masse
berechnet wird: Die statisch gegengelesenen H010-Pascal/C-Zeilen
291/705 setzen explizit /(5*eta). Das belegt einen spaeteren Rechenweg,
keine autorisierte Korrektur der H006-Wiedergabe. Jetzt soll die zugehoerige
fotografierte H015-A-Matrix/GVALUES-Stelle und gegebenenfalls ein
Buch-/Herleitungsanker gesucht werden. Beide Ergebnisse dieser Etappe
bleiben erhalten, unabhaengig davon, welche historische Lesart besser
belegt wird. Kein Wechsel zur Lesart mit dem kleineren Rest.

Quelle, genaue Seiten und begrenzter Suchstand:
[MUON_SELECTION_SOURCES](../03_notes/MUON_SELECTION_SOURCES_2026-09-06.md).
