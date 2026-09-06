# Quellenprüfung zur offenen Korrelationsschließung \(C/Y_3\)

Stand: 2026-09-06

## Fragestellung und Kurzantwort

Geprüft wurde eng, ob Burkhard Heims Buch in der unmittelbaren Kette von den internen Ladungskomponenten über die Integrationskonstante \(A\) bis zur Alpha-Gleichung (105) eine **von dieser Alpha-Gleichung unabhängige** Bestimmung von \(C\), des Proportionalitätsfaktors zwischen \(C\) und \(A_1A_2\), oder des Unsicherheitsfaktors \(Y_3\) angibt.

**Befund innerhalb der unten abgegrenzten Suche:** Eine solche unabhängige Bestimmung wurde nicht gefunden. Gleichung (98) legt die internen Ladungskomponenten und für vorgegebene \(q,k\) auch \(\eta_{qk}\) fest. Die Integration auf Druckseite 299 führt \(A\) ein und stellt es anschließend als \(4A_1A_2\) dar. Dagegen bleibt die Funktion \(C(\eta_{11},\eta_{12})\) in \(W=VC\) auf Druckseite 300 unbestimmt. Der Übergang zu \(C=A_1A_2\) erfolgt auf Druckseite 301 nur über eine Proportionalitätsaussage und die modal formulierte Annahme eines Faktors 4 aufgrund von vier besetzten Konfigurationszonen. \(Y_3\) wird gerade wegen der dabei verbleibenden Unsicherheit eingeführt. Die Einführung erklärt solche \(Y_k\) allgemein als Marker für noch nicht völlig geklärte Beziehungen und setzt sie für die numerischen Ermittlungen auf 1.

Das ist eine begrenzte Nichtfund-Aussage zu der unmittelbaren Herleitung und ihren bezeichneten Querverweisen, keine Behauptung über jede Stelle aller Heim-Schriften oder des Nachlasses.

## 1. Quellen und Prüfumfang

Visuell am Scan geprüft wurden:

- Burkhard Heim, *Elementarstrukturen der Materie*, Band II, 2. unveränderte Auflage, Andreas Resch Verlag, Innsbruck 1996, ISBN 3-85382-036-0:
  - Einführung, Druckseite 1 = PDF-Seite 12;
  - Gleichung (98), Druckseite 267 = PDF-Seite 273;
  - die begrifflich verwandte Integralkette, Druckseiten 273-275 = PDF-Seiten 279-281;
  - die unmittelbare H-Atom-/Alpha-Kette, Druckseiten 298-302 = PDF-Seiten 304-308.
- Burkhard Heim, *Elementarstrukturen der Materie*, Band I, 3., veränderte Auflage, Resch Verlag, Innsbruck 1998, ISBN 3-85382-008-5, Druckseiten 247-248 = PDF-Seiten 253-254, insbesondere die in Band II bezeichneten Gleichungen (28), (28a), (29) und (29a). Die Titelseite (PDF-Seite 3) nennt ausdrücklich „3., veränderte Auflage“; das „Vorwort zur 3. Auflage“ (PDF-Seite 8) erklärt, diese Neuauflage sei um Anhang II erweitert und decke sich ansonsten mit der zweiten Auflage.
- Burkhard Heim, *Magnetfeld und Drehimpulsdichte*, auf Manuskriptseite 20 mit „Northeim den 21.12.1981“ datiertes und mit „Heim“ unterzeichnetes Manuskript, Manuskriptseiten 3-5 = PDF-Seiten 3-5, als Versionsvergleich.

Zusätzlich wurde der vorhandene Volltext von Band II zielgerichtet nach den Ausdrücken „Integrationskonstante“, „Unsicherheitsfaktor“, „Unsicherheit“, „Korrekturkomponente“, „Proportionalitätsfaktor“, \(A=4C\), \(C=A_1A_2\), \(Y_3\) und den Gleichungsnummern (29), (29a), (98), (105) durchsucht. OCR wurde nur als Suchhilfe verwendet; alle für den Befund tragenden Seiten wurden visuell gelesen.

## 2. Was die Kette tatsächlich bestimmt

### 2.1 Gleichung (98) bestimmt interne Komponenten und \(\eta_{qk}\), nicht \(C\) oder \(Y_3\)

Band II, Druckseite 267 fasst die internen Ladungskomponenten zusammen als

\[
e_\varrho=e_\pm\sqrt{\eta_{qk}},\qquad
2e_\omega=e_\pm(1+\sqrt{\eta_{qk}}),
\]

\[
e_\delta=e_\pm(1-\sqrt{\eta_{qk}}),\qquad
e_C=e_\pm\sqrt{\vartheta_{qk}/8},
\]

mit

\[
\vartheta_{qk}=5\eta_{qk}+2\sqrt{\eta_{qk}}+1,
\qquad
\eta_{qk}\sqrt[4]{\pi^4+q^4(4+k)}=\pi.
\tag{98}
\]

Für die später verwendeten diskreten Werte \(q=1\) sowie \(k=1,2\) ist \(\eta_{11}\) beziehungsweise \(\eta_{12}\) damit innerhalb der Quelle algebraisch gebunden. (98) enthält jedoch weder \(C\) noch \(Y_3\) und gibt auch keinen Proportionalitätsfaktor zwischen \(C\) und \(A_1A_2\) an.

### 2.2 Die logarithmische Integration bestimmt eine Beziehung für \(A\)

Band II, Druckseiten 298-299 nimmt zunächst heuristisch

\[
s(\varrho)+s(\delta)=s(\omega)
\]

an und formuliert die relativen Potentialänderungen als Differentiale von Logarithmen. Alle betrachteten Potentiale sollen von \(V_{ee}\) als unterer Integrationsgrenze ausgehen; als obere Grenzen werden die zu (98) gehörenden internen Potentiale für \(k=1\) und/oder \(k=2\) genannt.

Auf Druckseite 299 heißt es dann ausdrücklich, \(\ln A=\mathrm{const}\) sei die Integrationskonstante. Nach Einsetzen des Potentialgesetzes und der Komponenten aus (98) erhält die Buchfassung

\[
\eta_{11}^{-1/2}\eta_{12}^{-1/2}A
=4
\frac{1-\sqrt{\eta_{11}}}{1+\sqrt{\eta_{12}}}
\frac{1-\sqrt{\eta_{12}}}{1+\sqrt{\eta_{11}}}.
\tag{2.1}
\]

Mit der Definition

\[
\eta_{1k}^{-1/2}A_k(1+\sqrt{\eta_{1k}})
=1-\sqrt{\eta_{1k}}
\tag{2.2}
\]

schreibt Heim

\[
A=4A_1A_2=\mathrm{const}.
\tag{2.3}
\]

Damit liegt innerhalb der Buchfassung nicht nur die Aussage „irgendeine Konstante“ vor. Sobald (98), \(q=1\) und \(k=1,2\) sowie (2.2) eingesetzt sind, ist \(A\) durch die betreffenden \(\eta\)-Werte bestimmt:

\[
A_k=\frac{\sqrt{\eta_{1k}}(1-\sqrt{\eta_{1k}})}
{1+\sqrt{\eta_{1k}}},
\qquad A=4A_1A_2.
\tag{2.4}
\]

Diese Festlegung von \(A\) bestimmt aber noch nicht \(C\).

### 2.3 \(C\) wird als unbestimmte Verhältnisfunktion eingeführt

Band II, Druckseite 300 verlangt für die Internstrukturierungen wieder (2.3) und verknüpft sie mit dem äußeren Potential \(V\). Der entscheidende Wortlaut und die anschließende Definition lauten strukturell:

\[
W\sim A_1A_2V
\quad\text{oder}\quad
W=V\,C(\eta_{11},\eta_{12}).
\tag{2.5}
\]

Hieraus folgt

\[
-E_k=\int_W^VdX=V-W=V(1-C).
\tag{2.6}
\]

Somit ist \(C=W/V\) zwar als dimensionsloses Verhältnis und als Funktion der beiden \(\eta\)-Werte bezeichnet. Eine Formel, die diese Funktion unabhängig auswertet, wird an dieser Stelle jedoch nicht angegeben. Insbesondere folgt aus \(W\sim A_1A_2V\) nur

\[
C\sim A_1A_2,
\tag{2.7}
\]

nicht bereits \(C=A_1A_2\).

### 2.4 Druckseite 301 schließt die Proportionalität durch eine Annahme

Nach der kinematischen Zwischenkette erhält Heim

\[
(2\pi)^5\alpha\sqrt{1-\alpha^2}=9\vartheta(1-C).
\tag{2.8}
\]

Er argumentiert anschließend:

- Wegen \(C\sim A_1A_2\) und \(A=4A_1A_2\) müsse \(A\sim C\) bestehen.
- \(C\) sei der Korrekturbeitrag eines strukturellen Elements beziehungsweise einer besetzten Konfigurationszone.
- Da bei den betrachteten Einheitsstrukturen alle \(j\leq4\) Konfigurationszonen besetzt seien, **könnte** für den Proportionalitätsfaktor der Wert 4 angenommen werden.

Erst auf dieser Grundlage schreibt die Quelle

\[
A=4C
\quad\Longleftrightarrow\quad
C=A_1A_2.
\tag{2.9}
\]

Der Text kennzeichnet den Wert 4 durch „könnte ... angenommen werden“ selbst als modal. Die Zonenanzahl liefert eine anschauliche Zählmotivation, aber keine zusätzliche Gleichung für \(W\), \(C\) oder einen Proportionalitätsfaktor, mit der (2.9) unabhängig kontrolliert würde.

### 2.5 \(Y_3\) dokumentiert die verbleibende Unsicherheit

Unmittelbar nach (2.9) sagt Druckseite 301, dabei trete eine Unsicherheit auf, der durch \(Y_3\) Rechnung getragen werden könne. Gleichung (105) auf Druckseite 302 lautet dann

\[
(2\pi)^5\alpha\sqrt{1-\alpha^2}
=9\vartheta(1-A_1A_2Y_3),
\tag{105a}
\]

zusammen mit

\[
(1+\sqrt{\eta_{1k}})A_k
=(1-\sqrt{\eta_{1k}})\sqrt{\eta_{1k}},
\qquad \alpha>0.
\tag{105b}
\]

Die Einführung, Druckseite 1, bestimmt den Status der \(Y_k\) ausdrücklich: Sie seien in den mathematischen Beziehungen angebracht, „die noch nicht völlig geklärt sind“. Für die theoretischen numerischen Daten des Tabellenanhangs sei für alle \(Y_k=1\) **unterstellt** worden. Entsprechend setzt Druckseite 302 für die numerische Lösung von (105) \(Y_3=1\).

Eine Herleitung oder Messvorschrift für \(Y_3\) wird in dieser unmittelbaren Kette nicht gegeben. \(Y_3=1\) ist nach dem Wortlaut der Quelle eine unterstellte Rechenwahl, keine unabhängige Bestimmung.

Das bedeutet nicht, dass die Buchfassung numerisch unberechenbar wäre: Mit der Spezialisierung \(C=A_1A_2\) und \(Y_3=1\) ist ihre Gleichung (105) geschlossen und Heim wertet sie auf Druckseite 302 aus. Offen ist die unabhängige Herleitung dieser Spezialisierung, nicht ihre rechnerische Verwendbarkeit.

## 3. Mathematischer Status der Integrationskonstante

Hier sind drei Aussagen zu trennen.

### 3.1 Eine Integrationskonstante entsteht vor der Randwertfestlegung

Beim Integrieren einer Differentialbeziehung von Logarithmen kann grundsätzlich eine additive Konstante \(\ln A\) auftreten. Solange keine Normierung oder kein Randwert angegeben ist, bleibt sie frei.

### 3.2 Bei vollständig vorgegebenen Endwerten ist ihr Wert nicht mehr frei

Werden dagegen die unteren und oberen Potentialwerte tatsächlich als feste Integrationsgrenzen behandelt, dann ist die Differenz der Logarithmen ein bestimmter Wert. Eine zuvor eingeführte Integrationskonstante muss dann durch diese Rand- oder Kompatibilitätsbedingungen festgelegt werden. In Heims eigener Weiterrechnung übernehmen (98), \(q=1\), \(k=1,2\) und die Definitionen (2.2) genau diese bindende Rolle: Sie führen zu (2.4).

Deshalb darf „\(A\) ist eine Integrationskonstante“ mathematisch nicht mit „\(A\) kann nach Festlegung der Endwerte noch beliebig gewählt werden“ gleichgesetzt werden. Entweder bleiben Rand- beziehungsweise Normierungsdaten offen; dann ist \(A\) frei. Oder die Endwerte und (2.2) gelten; dann ist \(A\) festgelegt. Beides gleichzeitig liefert keine zusätzliche Freiheit zur Wahl einer physikalisch gewünschten Relation.

### 3.3 Die Identifikation mit \(C\) ist eine weitere physikalische Annahme

Selbst ein fest bestimmtes \(A\) besitzt nicht allein wegen seines Ursprungs als Integrationskonstante eine physikalisch festgelegte Beziehung zu dem später eingeführten Verhältnis \(C=W/V\). Aus

\[
A=4A_1A_2,
\qquad C\sim A_1A_2
\]

folgt allgemein nur

\[
C=\rho A_1A_2=\frac{\rho}{4}A
\tag{3.1}
\]

mit einem zunächst unbestimmten Proportionalitätsfaktor \(\rho\). Die Buchannahme \(A=4C\) ist der Spezialfall \(\rho=1\). Weder der mathematische Begriff „Integrationskonstante“ noch (98) erzwingt \(\rho=1\).

## 4. Welche Rolle \(Y_3\) algebraisch spielen kann

Setzt man die offene Proportionalität transparent als (3.1) an, lautet die Vorstufe (2.8)

\[
(2\pi)^5\alpha\sqrt{1-\alpha^2}
=9\vartheta(1-\rho A_1A_2).
\tag{4.1}
\]

Die gedruckte Gleichung (105a) enthält stattdessen \(A_1A_2Y_3\). Algebraisch kann \(Y_3\) daher genau die Rolle eines effektiven, noch unsicheren Proportionalitätsfaktors übernehmen:

\[
\rho_{\mathrm{eff}}=Y_3.
\tag{4.2}
\]

Dies ist eine Interpretation der Form von (105), keine von Heim separat gedruckte Definition \(Y_3:=\rho\). Sie stimmt aber mit seinem unmittelbaren Text überein, wonach \(Y_3\) der Unsicherheit beim angenommenen Proportionalitätsfaktor Rechnung trägt.

Wesentlich ist: (105) enthält nur das Produkt \(A_1A_2Y_3\). Ohne eine weitere unabhängige Beziehung kann (105) nicht zugleich \(\alpha\) und \(Y_3\) bestimmen. Setzt man \(Y_3=1\), wird die Gleichung lösbar für \(\alpha\), aber die Proportionalitätsannahme wird damit eingesetzt, nicht unabhängig geprüft.

## 5. Status der bezeichneten Querverweise

### 5.1 Band I, Gleichungen (28) bis (29a)

Band I, Druckseiten 247-248 bezeichnet bereits das Potentialgesetz (28) als „spekulativer Art“ und entwickelt daraus die Ladungskomponenten (28a). Gleichung (29) gibt anschließend eine theoretische Beziehung für das messbare elementare Ladungsfeld an. Die Substitution in die dort so genannte quantenelektrodynamische Beziehung \(e_\pm^2\sim\alpha\) führt zur vorläufigen Näherung

\[
(2\pi)^5\alpha'=9\vartheta.
\tag{29a}
\]

Diese Gleichungen liefern den Ladungs- und Näherungsanker, den Band II auf Druckseite 301 verwendet. Sie enthalten aber weder \(C\) noch \(Y_3\) und normieren den Faktor in (3.1) nicht. Band I, Druckseite 248 sagt vielmehr, die Ursache der Abweichung von \(\alpha'\) könne dort „vorerst noch nicht ermittelt werden“ und werde erst mit Methoden aus Band II behandelt.

### 5.2 Die frühere \(Y\)-Integralkette auf Band-II-Druckseiten 273-275

Auf Druckseite 273 erscheint ebenfalls ein Symbol \(Y\), jedoch mit ausdrücklicher Definition

\[
Y=\frac{X(z+1)}{X(z-1)}.
\]

Der Text warnt sogar, diese Kürzung nicht mit einem dort anders gesetzten Vektorsymbol zu verwechseln. Auf Druckseite 275 wird das Verhältnis aus einem Limes einer Folge bestimmt. Dieses \(Y\) gehört zur Grenzschicht \(j=3\to4\) in der Ermittlung der Funktionen \(H\) und \(G\). Es ist nicht als \(Y_3\) der Alpha-Gleichung (105) ausgewiesen und liefert keine Beziehung für \(C\). Eine Gleichsetzung wäre ohne weiteren Quellentext nicht gerechtfertigt.

### 5.3 Manuskript 1981 als Versionsvergleich

Das Manuskript folgt auf Seiten 3-5 demselben Grundgang von den internen Potentialvariationen über \(A=4A_1A_2\), \(W=VC\) und die Alpha-Vorstufe. Es verwendet jedoch eine andere \(\eta\)-Potenz in der \(A_k\)-Definition und später den unindizierten Unsicherheitsfaktor \(Y\neq0\); deshalb sind die Formeln nicht ohne weiteres editionsidentisch.

Für die hier untersuchte Schließungsfrage ist sein Wortlaut besonders deutlich: Wegen der „freien Verfügbarkeit“ der Integrationskonstante \(A\) **könnte** \(A=4C\), also \(C=A_1A_2\), unterstellt werden. Eine unabhängige Randbedingung für \(C\) folgt darauf nicht; stattdessen wird sofort der Unsicherheitsfaktor \(Y\) eingeführt. Das Manuskript macht die offene Setzung damit sichtbarer, schließt sie aber ebenfalls nicht.

## 6. Suchgrenze und belastbarer Nichtfund

Die Prüfung umfasste die vollständige unmittelbare Kette Band II, Druckseiten 298-302, die dort ausdrücklich verwendete Gleichung (98), die allgemeine Erklärung der \(Y_k\) in der Einführung, die bezeichneten Band-I-Anker (28) bis (29a), die ähnlich aussehende, aber sachlich andere \(Y\)-Kette auf Band-II-Druckseiten 273-275 sowie die Manuskriptversion 1981, Seiten 3-5. Ergänzend wurde der lokale Volltext von Band II mit den in Abschnitt 1 genannten Zielbegriffen durchsucht.

Nicht systematisch geprüft wurden sämtliche anderen Symbolvorkommen in beiden Bänden, ungenannte spätere Publikationen, Nachlassblätter oder externe Kommentarliteratur. OCR kann mathematische Indizes übersehen; deshalb lautet der Befund ausdrücklich nicht „nirgendwo bei Heim“, sondern:

> In der unmittelbaren Herleitung, ihren benannten Querverweisen und der gezielten Volltextsuche wurde keine unabhängige Bestimmung von \(C\), \(\rho\) oder \(Y_3\) gefunden, welche den Übergang \(C\sim A_1A_2\to C=A_1A_2\) schließt.

## 7. Schlussfolgerung für eine Rekonstruktion

Quellengetreu sind drei Ebenen getrennt zu führen:

1. **Bestimmt:** (98) bindet \(\eta_{11},\eta_{12}\); die Buchdefinitionen binden daraus \(A_1,A_2\) und \(A=4A_1A_2\).
2. **Nur proportional beschrieben:** \(C=W/V\sim A_1A_2\), ohne unabhängig angegebene Funktion \(C(\eta_{11},\eta_{12})\).
3. **Unterstellt beziehungsweise als unsicher markiert:** Faktor 4 in \(A=4C\), entsprechend \(C=A_1A_2\), und für die numerische Auswertung \(Y_3=1\).

Eine publizierbare Rekonstruktion darf daher \(C=A_1A_2\) und \(Y_3=1\) als Heims ausdrücklich modal beziehungsweise als Unsicherheitsfaktor gekennzeichnete Schließungsannahmen verwenden. Sie sollte sie aber nicht als aus der Eigenschaft „Integrationskonstante“ oder aus (98) bewiesene Identitäten ausgeben. Eine eigene verallgemeinerte Fassung mit \(C=\rho A_1A_2\) macht die offene Stelle sichtbar; in der Alpha-Gleichung ist dann nur das effektive Produkt \(\rho A_1A_2\) beziehungsweise in der Buchnotation \(A_1A_2Y_3\) bestimmt.
