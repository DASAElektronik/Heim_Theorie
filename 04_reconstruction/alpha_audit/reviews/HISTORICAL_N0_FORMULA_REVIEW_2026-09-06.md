# H006 gegen H010: statischer Formelvergleich fuer den Elektron-N0-Fall

Stand: 2026-09-06, Etappe 17 ab `99a2efa`.

## 1. Ergebnis in einem Satz

Bei fest gleichen Eingabekonstanten und dem bereits getrennt belegten
Elektron-Nulltupel stimmen die aktive Massenklammer, die kompakte
`K+G+H`-Auswertung und der gesamte grosse `Phi`-Ausdruck der H010-
Implementierungen algebraisch mit H006 ueberein. Zwei wertaktive
Formelabweichungen stehen jedoch in `alpha3`: H010 nimmt den Faktor
`1+sqrt(eta_qk)` aus der Potenz `2k+1` heraus und laesst im zweiten
Korrekturterm das in H006 sichtbare Wurzelzeichen vor `xi eta_qk` weg.

Diese zwei Unterschiede sind keine Rundungs- oder Konstantenfrage. Fuer
`k=P=Q=q=1`, `kappa=0`, `qx=-1`, `N=0`, `n=(0,0,0,0)` pflanzen sie sich
ueber `12*alpha3` in `G` und damit in die Masse fort. `Phi` enthaelt
`alpha3` in diesem Block nicht und wird durch diese beiden Abweichungen
nicht direkt veraendert.

Dies ist ein Versionsvergleich, kein Erratumnachweis. Weder der spaetere
Pascal-/C-Code noch die IGW-Wiedergabe H006 wird hier allein zur
autoritativen Urschrift erklaert.

## 2. Quellen, Provenienz und Pruefart

Verglichen wurden ausschliesslich statisch:

| Kennung | Datei / Fundstelle | Rolle | SHA-256 |
| --- | --- | --- | --- |
| H006 | `01_sources/heim_primary/Massenformel_nach_B_Heim_1982.pdf`, Druck/PDF 3--5, besonders (VI)--(XII) | IGW-Wiedergabe 2002/2003 eines auf 25.2.1982 datierten Textes; kein hier verifiziertes Originalfaksimile | `F74DA0DAC8496BCD01226F54D88598152D67E1C954943AF61D0EC1811F5527BE` |
| H010-Pascal | `01_sources/heim_primary_unpacked_untrusted/massformula/Pascal 0.62/GPROG 0.62c.PAS` | spaetere Transkription, Header Zeilen 1--7 | `1C1D60DC68F0EB540AA0E061896EF03559E3F57846D1E8A3AA28563694CDC59C` |
| H010-C | `01_sources/heim_primary_unpacked_untrusted/massformula/C 0.66/gprog_0.66.c` | C-Port der Transkriptionskette, Header Zeilen 1--8 und Versionsnotiz 36--39 | `29CBF3EBC197EFC8044C2C34D71AB40DD7C6F6829368A412812C7868A287B7B0` |

Die Codeheader berichten ein GPROG von H. D. Schulz/DESY und nennen
Heim-Formeln vom 17.9.1978. Danach nennen sie Transkriptionsschritte von
2001 und 2006. Das belegt die im Archiv vorliegende Ueberlieferungskette,
nicht die Unveraendertheit gegenueber einem nicht vorliegenden
Fortran-Original.

Nach vollstaendiger Lektuere des PDF-Skills wurden die vorhandenen
Vollseitenbilder von H006 Druck/PDF 3, 4 und 5 visuell gelesen. Fuer
`alpha3` wurde Druck/PDF 5 zusaetzlich bei 800 dpi gerendert:

`tmp/pdfs/historical_n0/h006-p5-alpha3-800dpi.png`.

Keine Datei aus H010 wurde kompiliert oder ausgefuehrt. Workbooks und
Makros wurden nicht geoeffnet oder analysiert. Es wurde kein Mess- oder
Sollmassenwert zur Auswahl einer Lesart verwendet.

## 3. Gleicher Zustandsknoten, verschiedene Komponentenindizes

H006 Druck/PDF 3 gibt fuer das Multiplett `x_2(0110)` die Komponenten
`(e_0,e-)` an. Seine Ladungsformel (II) verwendet einen bei null
beginnenden Komponentenindex `0 <= x <= P`. Im eingefrorenen H006-Profil
ist daher die Elektronkomponente `x=1` und `q_x=-1`.

H010-Pascal liest fuer dieses Multiplett `k=P=Q=1`, `kappa=0` aus
`gprogin.dat` Zeilen 12--16, laeuft aber mit `x=1..P+1` (Pascal
691--704). Seine Zeile 701 schreibt deshalb `P+2-2*x` statt H006s
`P-2*x`. H010-C speichert die Elektronkomponente explizit als
`"1110#2-10"` (C 141); seine Zeilen 1217--1230 verwenden dieselbe
einsbasige Konvention. Mit

```text
x_code = x_H006 + 1
```

sind beide Ladungsformeln identisch, und die Elektronkomponente hat im
Code `x=2`, `qx=-1`, `kq=abs(qx)=1`. Das ist eine Indexverschiebung,
keine aktive Ladungsabweichung. Das Label `(0110)` ist in keiner Fassung
das Besetzungstupel `n1..n4`.

Pascal 720--724 und C 1243--1251 setzen fuer den hier betrachteten Lauf
`N=0` und rufen danach Struktur- und Massenroutine auf. Die separate
Rundungs-/Ganzzahlpruefung gehoert nicht in diese Review; hier wird deren
bereits festgehaltener Fall

```text
k=P=Q=q=1, kappa=0, qx=-1, N=0,
Qj=(3,3,2,1), Kj=Qj, nj=(0,0,0,0)
```

als Vergleichsknoten benutzt.

## 4. AUX bis `alpha3`

### 4.1 Uebereinstimmende Formeln

H006 (VII)--(X) und H010 stimmen in folgenden Formelkoerpern ueberein:

```text
eta      = pi/(pi^4+4)^(1/4)
t        = 1-(2/3)*xi*eta^2*(1-sqrt(eta))
alpha+   = t/eta^(7/3)-1
alpha-   = t/eta^(4/3)-1
eta_qk   = pi/[pi^4+(4+k)q^4]^(1/4)
alpha1   = (1+sqrt(eta_qk))/2
alpha2   = 1/eta_qk
N1       = alpha1
N2       = (2/3)*alpha2
N3       = 2*alpha3
```

Codeanker: Pascal 106--110, 197--203, 248--254 und 368--385;
C 454--462, 607--665 und 788--810. Die Auswahlwerte `Q1..Q4` werden
ebenfalls formelgleich erzeugt. C benutzt fuer `Q3` `pow(-1,k)`, Pascal
`cos(pi*k)` mit anschliessender Ganzzahlabbildung; bei `k=1` liefern
beide den belegten Wert `Q3=2`.

Die `mu`-Form in H010-Pascal 248--249 und H010-C 659--660 ist nach
Zusammenfassen von Wurzeln und Potenzen dieselbe wie H006 (VI). Die
tatsaechlich eingesetzten Zahlenwerte sind absichtlich nicht Gegenstand
dieser Review.

### 4.2 Erste aktive `alpha3`-Abweichung: Potenzbereich

H006 (IX), Druck/PDF 5, druckt im ersten Korrekturterm:

```text
(alpha/3) * [(1+sqrt(eta_qk))*(xi/eta_qk^2)]^(2k+1)
            * eta_qk^3.
```

Pascal 383 und C 807 implementieren dagegen:

```text
(alpha/3) * (1+sqrt(eta_qk))
          * (xi/eta_qk^2)^(2k+1) * eta_qk^3.
```

Der Exponent wirkt im Code nur auf `xi/eta_qk^2`, nicht auf dessen
Produkt mit `1+sqrt(eta_qk)`. Bei `k=1` ist die Differenz sicher aktiv:
H006 enthaelt die dritte Potenz des ersten Faktors, H010 nur dessen
erste Potenz.

### 4.3 Zweite aktive `alpha3`-Abweichung: Wurzelzeichen

H006 zeigt im zweiten Korrekturterm die Glyphenfolge

```text
[eta(1,1)/(e*eta_qk)] * (2 sqrt-glyph xi eta_qk)^k
* [(1-sqrt(eta_qk))/(1+sqrt(eta_qk))]^2.
```

Die bestehende, quellgepruefte H006-Formelkarte `HT-F-1982-AUX`
normalisiert dies als `(2*sqrt(xi*eta_qk))^k`, und genau diese Lesart ist
im unveraenderten H006-N0-Profil eingefroren. Pascal 384 und C 808
schreiben dagegen eindeutig

```text
(2*xi*eta_qk)^k
```

und enthalten an dieser Stelle ueberhaupt keinen Wurzeloperator.

Wichtige Bildgrenze: Der 800-dpi-Scan zeigt zwar das Wurzelglyph sicher,
aber keinen ausreichend abgrenzenden horizontalen Wurzelstrich. Aus dem
Bild allein laesst sich daher nicht neu entscheiden, ob die historische
Setzung `sqrt(xi*eta_qk)` oder enger `sqrt(xi)*eta_qk` gemeint hat. Diese
Review aendert die bestehende H006-Normalisierung nicht. Gegen H010 ist
der Befund dennoch robust: Unter beiden H006-Lesarten fehlt im Code ein
sichtbarer Wurzeloperator und der Unterschied ist bei `k=1` wertaktiv.

### 4.4 Exakte Reduktion der beiden Fassungen

Setze fuer diesen Absatz nur

```text
d = eta_(q=1,k=1),  s=sqrt(d),  a=alpha,
R=[(1-s)/(1+s)]^2.
```

Dann reduziert die im Projekt festgehaltene H006-Lesart zu

```text
alpha3_H006 = 1
 - a*xi^3*(1+s)^3/(3*d^3)
 - (2/e)*sqrt(xi*d)*R.
```

Pascal und C reduzieren beide zu

```text
alpha3_H010 = 1
 - a*xi^3*(1+s)/(3*d^3)
 - (2/e)*xi*d*R.
```

Damit sind zwei und nur zwei aktive interne Formelabweichungen in
`alpha3` nachgewiesen. Eine moegliche engere historische Wurzellesart
wuerde im ersten Ausdruck den letzten Term durch
`-(2/e)*sqrt(xi)*d*R` ersetzen; sie wuerde ihn ebenfalls nicht zur
H010-Zeile machen.

Die Abweichung ist schon vor `GMASS` aktiv: Pascal 405--406 und C
830--831 verwenden `alpha3` in `gkq`; Pascal 474--488 und C 927--946
verwenden es in Restbildung und `K3/K4`-Bestimmung. Daher koennen sich
auch Auswahlabstaende aendern. Die unten angegebene lineare
Massendifferenz gilt ausdruecklich erst unter der hier vorgegebenen,
separat zu pruefenden Bedingung, dass beide Fassungen beim selben
Nulltupel bleiben. Diese Review ersetzt nicht die parallele
Rundungs-/Ganzzahlpruefung.

H010 verwendet ausserdem aktiv eine fest eingetragene `alpha`-Zahl
(Pascal 208--215; C 618--625); die 1982-Alpha-Rekonstruktion steht nur in
auskommentierten Testbloecken (Pascal 217--245; C 627--655). H006 gibt
`alpha` zuvor durch seine Gleichung (V) vor. Dies ist eine aktive
Eingabe-/Versionsentscheidung, aber keine weitere Klammerabweichung in
`alpha3`; ihr Zahlenvergleich liegt beim parallelen Konstantenauftrag.
Entsprechendes gilt fuer die unterschiedlichen numerischen `xi`-,
`hbar`- und Gravitationskonstanten. `beta` ist im hier bereits auf
`n=0` reduzierten Massenblock nicht aktiv.

## 5. `K+G+H` gegen `kgh`

H006 (XI) schreibt drei Polynome `K`, `G`, `H`. H010-Pascal 520--524
und H010-C 988--1000 erklaeren und implementieren stattdessen den
zusammengesetzten Term `kgh`, wobei `Kj=nj+Qj` und
`Nj=(alpha1,(2/3)alpha2,2alpha3)` bereits eingesetzt sind:

```text
kgh = alpha1*K1^2*(K1+1)^2
     +(2/3)*alpha2*K2*(2*K2^2+3*K2+1)
     +2*alpha3*K3*(K3+1)+4*K4.
```

Das ist die ausmultiplizierte Identitaet `K+G+H`, keine zusaetzliche
Massenannahme. Im Nulltupel folgt mit `Kj=Qj=(3,3,2,1)`:

```text
K=H=0,
kgh=G=144*alpha1+56*alpha2+12*alpha3+4.
```

Folglich wirkt der oben gefundene `alpha3`-Unterschied bei sonst festen
Groessen exakt mit dem Koeffizienten 12 auf die dimensionslose
Massenklammer. Insbesondere ist der Koeffizient von `K4` in Pascal und C
genau 4; eine isolierte Aenderung `n4 -> n4+1` aendert vor der
Einheitenumrechnung die Masse um `4*mu*alpha+`. `Phi` enthaelt kein
`n4`.

## 6. `Phi`/`fig`: keine weitere aktive Formelabweichung

H010-Pascal 526--531 und H010-C 1002--1008 wurden Faktor fuer Faktor
gegen H006 (XI), Druck/PDF 5, sowie
`NORM-1982-AUX-PHI-PRECEDENCE` gelesen. Beide Codes erhalten die eine
Produktkette und danach die beiden additiven Terme. Insbesondere:

- der Invers-Exponent betrifft im Quelltext die volle Binomialklammer;
  der Code bildet sie als Division durch genau diese Klammer ab;
- `cos(pi*(P+Q))` ist fuer ganzzahlige `P,Q` die Codeumschreibung von
  `(-1)^(P+Q)`; hier sind beide mathematisch `+1`;
- `sqrt(eta_(1,1)*eta_qk)` entspricht wegen positiver eta-Werte dem
  gedruckten Produkt `sqrt(eta_11)*sqrt(eta_qk)`;
- `kq` ist an diesen Codezeilen H006s `q=abs(qx)`;
- `n1/q1` ist H006s `n_1/Q_1`;
- die letzten Terme `4*(1-alpha-/alpha+)*alpha*(P+Q)/xi^2` und
  `4*q*alpha-/alpha+` bleiben ausserhalb der Produktkette.

Mit `h=eta` ohne Index, `d=eta_(1,1)`, `r=alpha-/alpha+` und dem
Nulltupel reduzieren H006, Pascal und C daher formgleich zu

```text
L = 12*sqrt(d)/pi * (1-a/3)
    * (1+4*pi*a/(h*sqrt(h))) + 8*a/xi^2,

Phi = (1-r)*L + 4*r.
```

Die Nullsetzungen sind hier nachvollziehbar: `k-1=0`, `kappa=0`,
`P-Q=0`, `choose(P,2)=0` und `n1=0`. Weder die Produktkette noch ganz
`Phi` wird durch `N=0` zu null.

Damit gibt es im geprueften `Phi`-Formelkoerper keinen dritten
Klammer-, Faktor- oder Vorzeichenunterschied. Tatsaechliche Zahlen von
H006 und H010 koennen wegen ihrer verschiedenen aktiven Eingaben
trotzdem abweichen; das ist getrennt vom Formelkoerper zu berichten.

## 7. Endformel und Ausgabeschicht

H006 (XII) lautet normalisiert

```text
M_kg = mu*alpha+*(K+G+H+Phi).
```

Pascal 545--546 und C 1025--1027 rechnen aktiv

```text
am = amu*fakMeV*alfp*(kgh+fig).
```

Nach `kgh=K+G+H`, `fig=Phi`, `amu=mu` und `alfp=alpha+` ist der
Massenkoerper identisch. `fakMeV` ist die anschliessende Umrechnung von
kg nach `MeV/c^2`, wie die Codeausgabe selbst ausweist, nicht ein
weiterer Term der H006-Massenklammer. Fuer einen Vergleich in kg muss
dieser Ausgabefaktor entfernt bzw. die Einheit explizit umgerechnet
werden.

Unter fest gleichen Eingaben und fest gleichem Nulltupel ist die rein
durch die normalisierten `alpha3`-Formeln verursachte Differenz daher

```text
M_H010,kg - M_H006,kg
 = 12*mu*alpha+*(alpha3_H010-alpha3_H006).
```

Das ist eine Abhaengigkeitsformel, keine hier vorgenommene alternative
Massenrechnung.

H010-C berechnet zusaetzlich `fik`/`am_field` (C 1010--1027). Dieser
C-spezifische Diagnose-/Neutrinopfad geht nicht in `am` der
Elektronkomponente ein. Der entsprechende `fik`-Block ist in Pascal
533--535 auskommentiert und hat dort zudem einen anderen Faktor. Diese
Portdifferenz ist fuer die hier betrachtete Elektronmasse inaktiv.
Auch der C-Kommentar 988--990 zu einer 1989er Klammer aendert die
aktive 1982-Zeile 1026 nicht.

## 8. Vollstaendigkeitsgrenze und Schlussfolgerung

Innerhalb des angeforderten, bereits festgelegten N0-Knotens wurden
alle werttragenden Bausteine der Massenrechnung geprueft:

| Baustein | H006 gegen H010 bei gleichen Eingaben |
| --- | --- |
| `mu` | algebraisch gleich |
| `eta`, `t`, `alpha+/-`, `eta_qk`, `alpha1/2`, `Qj` | Formelkoerper gleich |
| `alpha3`, Korrekturterm 1 | aktiv verschieden: Potenzbereich |
| `alpha3`, Korrekturterm 2 | aktiv verschieden: Wurzelzeichen fehlt in H010; genaue historische Radikandgrenze im Scan offen |
| `K+G+H` / `kgh` | algebraische Kompaktidentitaet |
| `Phi` / `fig` | im geprueften N0-Profil formgleich |
| Massenklammer | formgleich; `alpha3`-Differenz wirkt ueber `12*alpha3` |
| Ausgabe | H010 multipliziert mit `fakMeV`; reine Einheitenumrechnung |

Nicht Teil dieser Review sind die numerischen Konstantenabweichungen,
die C-/Pascal-Rundungsvarianten, der allgemeine Resonanzalgorithmus und
andere Teilchen. Insbesondere wird nicht behauptet, dass ein gleiches
`alpha3` automatisch dasselbe `n` fuer beliebige Eingaben erzeugt.

Das bestehende H006-Literalprofil und sein berichtetes Ergebnis
`9.078017464516...e-31 kg` bleiben unveraendert. Es wurde weder durch
eine H010-Formel ersetzt noch auf einen beobachteten Wert getrimmt.
Eine spaetere Vergleichsrechnung muss die beiden `alpha3`-Aenderungen
als benannte, gemeinsam und einzeln schaltbare Versionsdifferenzen
behandeln; sie darf sie nicht als stilles Erratum uebernehmen.
