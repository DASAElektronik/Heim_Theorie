# Quellenprüfung der Korrelationskette vor Gleichung (105)

Stand: 2026-09-06

## Auftrag und Quellengrundlage

Untersucht wurde ausschließlich die Herleitung in Burkhard Heim, *Elementarstrukturen der Materie*, Band II, 2. unveränderte Auflage, Andreas Resch Verlag, Innsbruck 1996, ISBN 3-85382-036-0, Druckseiten 296–302. Die Kerngrenzen des Auftrags sind Druckseiten 297–301 = PDF-Seiten 303–307; Druckseite 296 = PDF-Seite 302 wurde nur als unmittelbar notwendiger Vorlauf, Druckseite 302 = PDF-Seite 308 nur zur Kontrolle des Übergangs in (105) herangezogen.

Primärquelle: `01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`. Die Seiten 296–302 wurden aus dem Scan gerendert und visuell geprüft. Das OCR `07_outputs/extracted_text/Elementarstrukturen_der_Materie_2.txt` diente nur zum Auffinden; bei Zeichenkonflikten hat der Scan Vorrang.

## Ergebnis in Kurzform

Die Kette besteht nicht aus einer durchgehend deduktiven Rechnung. Ihr Status wechselt mehrfach:

1. Die Zuordnung der zuvor berechneten Gerüststrukturen zu Elektron und Proton wird auf Druckseite 296 anhand angenäherter Massenwerte vorgenommen; dies ist der empirisch-heuristische Einstieg.
2. Die Deutung der attraktiven \((e^-,p)\)-Korrespondenz als Wasserstoffatom mit K-Schale und der Kopplung als Feinstrukturkonstante wird auf Druckseite 297 physikalisch angenommen.
3. \(s(y)\) wird auf Druckseite 298 definiert. Der Zusammenhang
   \[
   s(\varrho)+s(\delta)=s(\omega)
   \]
   wird auf Druckseite 299 ausdrücklich als „heuristischer Zusammenhang“ bezeichnet, „der im folgenden angenommen werden soll“. Er ist kein Resultat der Definition von \(s\).
4. Unter dieser Annahme, den angegebenen Integrationsgrenzen, dem Potentialansatz und der Substitution der internen Ladungsfeldkomponenten aus (98) ist die Umformung bis \(A=4A_1A_2\) algebraisch. Dabei werden die \(A_k\) eigens so definiert, dass die exponentierte Relation diese Produktform annimmt.
5. \(C\) wird auf Druckseite 300 über \(W=VC(\eta_{11},\eta_{12})\) als dimensionsloser Korrekturfaktor des unteren Potential-/Energieniveaus eingeführt. Die Proportionalität \(C\sim A_1A_2\) ist keine Folge der Energieintegration; sie wird auf Druckseite 301 aufgrund der gemeinsamen strukturellen Deutung postuliert.
6. Der konkrete Faktor 4 wird auf Druckseite 301 aus den vier besetzten Konfigurationszonen motiviert, aber sprachlich nur als Möglichkeit eingeführt: Er „könnte … angenommen werden“. Erst damit gilt \(A=4C\) und, zusammen mit \(A=4A_1A_2\), \(C=A_1A_2\). Heim räumt unmittelbar eine Unsicherheit ein und führt dafür \(Y_3\) ein.

Wichtig für die Transkription: Das erste Argument im Scan ist die interne Komponente \(\varrho\), nicht ein lateinisches \(e\). Die Druckformel lautet somit \(s(\varrho)+s(\delta)=s(\omega)\), nicht \(s(e)+s(\delta)=s(\omega)\).

## Quellenkette mit logischem Status

### 1. Empirische Identifikation von \(e^-\) und \(p\) (Druckseite 296 / PDF-Seite 302)

Für \(k=1,q=1\) und \(k=2,q=1\) nennt Heim die berechneten Näherungswerte

\[
m_0(1,1)-\mu_sF_s=0{,}50562729\,\mathrm{MeV},
\qquad
m_0(2,1)-\mu_sF_s=938{,}2497\,\mathrm{MeV}.
\]

Da \(F_s\) unbekannt sei, schreibt er, \(m_0(1,1)\approx m_e\) und \(m_0(2,1)\approx m_p\) „gesetzt werden muß“, und identifiziert die zeitlich konstanten Gerüststrukturen mit den Grundmustern des Elektrons bei \(k=1\) und des Protons bei \(k=2\).

**Status:** empirisch gestützte, zugleich ausdrücklich heuristische Zuordnung. Die Massenähnlichkeit liefert in dieser Passage keine unabhängige Ableitung der Teilchenidentität.

### 2. Übergang zum H-Atom und zur Feinstrukturkonstante (Druckseiten 296–297 / PDF-Seiten 302–303)

Aus \(m_p\gg m_e\) folgert Heim über den „Quantendualismus“ \(\lambda_p\ll\lambda_e\) und bezieht die attraktive elektromagnetische Wechselwirkung auf das Proton. Auf Druckseite 297 wird dann behauptet, die schwache elektromagnetische Korrespondenz \((e^-,p)\) müsse zur Ausbildung einer K-Schale führen, wobei \(e^-\) den stabilen Grundzustand eines s-Terms besetze. Diese Struktur höherer Ordnung wird mit dem \(H^1_1\)-Atom identifiziert; die Kopplungskonstante der Korrespondenz „erscheint“ als Feinstrukturkonstante \(\alpha\) der H-Spektralserien.

Die frühere Näherung (29a) wird zugleich als numerisch fehlerhaft bezeichnet. Heim führt die Abweichung darauf zurück, dass (29a) phänomenologisch \(e_-^2\sim\alpha'\) verwendet und die Änderung der internen Strukturierung von Elektron und Proton bei der Bindung nicht berücksichtigt habe.

**Status:** physikalische Modellannahme/Identifikation. Hier wird noch keine neue Gleichung für \(\alpha\) deduziert.

### 3. Strukturelle Korrespondenz und Definition von \(s(y)\) (Druckseite 298 / PDF-Seite 304)

Heim beschreibt Elektron und Proton zunächst durch partielle Korrelationsstrukturen und reduziert außerhalb des sphärischen Korrespondenzvolumens die wechselseitige Korrespondenz auf eine verkürzte Strukturform. Diese soll das H-Atom als „dynamisch stabiles Korrespondenzgefüge“ beschreiben.

Für \(y\in\{\varrho,\omega,\delta\}\) bezeichnet \(V'(y,\varepsilon)\) das interne Potential zwischen \(e_y\) und dem nicht reduzierten Ladungsfeld \(\varepsilon_\pm\) für \(k=1\), während \(V'''(y,\varepsilon)\) das entsprechende Potential für \(k=2\) bezeichnet. Die relative Änderungssumme wird definiert als

\[
s(y)=\frac{\partial V'(y,\varepsilon)}{V'(y,\varepsilon)}
     +\frac{\partial V'''(y,\varepsilon)}{V'''(y,\varepsilon)}.
\]

Im Druck steht für die Division jeweils ein Doppelpunkt:

\[
s(y)=(\partial V'(y,\varepsilon)):V'(y,\varepsilon)
 +(\partial V'''(y,\varepsilon)):V'''(y,\varepsilon).
\]

**Status:** Definition. Aus ihr allein folgt keine Beziehung zwischen den drei \(s(y)\).

### 4. Der Ansatz \(s(\varrho)+s(\delta)=s(\omega)\) (Druckseite 299 / PDF-Seite 305)

Der Scantext lautet sinngemäß und statusentscheidend: Die \(s(y)\) „können“ im Korrespondenzfall zwischen \(e^-\) und \(p\) in dem „heuristischen Zusammenhang“

\[
s(\varrho)+s(\delta)=s(\omega)
\]

stehen, „der im folgenden angenommen werden soll“. Umgestellt wird daraus

\[
-s(\varrho)=s(\delta)-s(\omega).
\]

Heim ergänzt, der Änderungsoperator \(\partial\) bezeichne eine Änderung in der Größenordnung \(\sqrt{\tau}\), und schreibt die Beziehung als Summe von relativen Potentialänderungen beziehungsweise logarithmischen Änderungen aus. Dieser Operator ist von der internen Komponente mit dem Index \(\delta\) zu unterscheiden.

**Status:** explizite heuristische Annahme; die anschließende Umstellung und die Darstellung als Logarithmen sind Algebra.

### 5. Integration, Substitution aus (98) und Entstehung von \(A=4A_1A_2\) (Druckseite 299 / PDF-Seite 305)

Die auf Druckseite 299 ausdrücklich herangezogene Gleichung (98) steht auf Druckseite 267 / PDF-Seite 273. Ihr hier relevanter Teil definiert die drei internen Ladungsfeldkomponenten als

\[
e_\varrho=\varepsilon_\pm\sqrt{\eta_{qk}},
\qquad
2e_\omega=\varepsilon_\pm\bigl(1+\sqrt{\eta_{qk}}\bigr),
\qquad
e_\delta=\varepsilon_\pm\bigl(1-\sqrt{\eta_{qk}}\bigr).
\tag{98, Auszug}
\]

Für die hier betrachteten geladenen Terme ist \(q=1\), während \(k=1\) und \(k=2\) Elektron beziehungsweise Proton kennzeichnen. Damit gilt je \(k\)

\[
\frac{e_\delta}{e_\omega}
=2\frac{1-\sqrt{\eta_{1k}}}{1+\sqrt{\eta_{1k}}}.
\]

Der Zahlenfaktor 4 in der späteren potenzierten Relation stammt somit bereits algebraisch aus den beiden Faktoren 2 für \(k=1\) und \(k=2\), also aus der Definition \(2e_\omega=\ldots\) in (98). Er ist an dieser Stelle noch nicht die spätere Zählannahme „vier Konfigurationszonen“.

Alle Potentiale sollen von \(V_{\varepsilon\varepsilon}\) als unterer Integrationsgrenze ausgehen, mit

\[
4\pi\varepsilon_0 f(r)V_{\varepsilon\varepsilon}=\varepsilon_\pm^{2},
\]

während die oberen Grenzen die internen Potentiale \(V_{\varepsilon\varrho}\), \(V_{\varepsilon\delta}\) und \(V_{\varepsilon\omega}\) für \(k=1\) und/oder \(k=2\) sind. Mit \(\ln A=\mathrm{const}\) als Integrationskonstante gibt der Text die integrierte Logarithmusrelation

\[
-\ln\!\bigl(V'_\varrho V'''_\varrho\bigr)+2\ln V_{\varepsilon\varepsilon}+\ln A
=\ln V'_{\varepsilon\delta}-\ln V'''_{\varepsilon\omega}
 +\ln V'''_{\varepsilon\delta}-\ln V'_{\varepsilon\omega}
\]

an. Nach dem Potentialansatz \(f(r)V_{(l)}\sim e_{(l)}e_{(l)}\) und der Substitution der internen Ladungsfeldkomponenten gemäß (98) folgt nach Potenzierung:

\[
\eta_{11}^{-1/2}\eta_{12}^{-1/2}A
=4\left(\frac{1-\sqrt{\eta_{11}}}{1+\sqrt{\eta_{12}}}\right)
  \left(\frac{1-\sqrt{\eta_{12}}}{1+\sqrt{\eta_{11}}}\right).
\]

Anschließend definiert Heim für \(k=1,2\)

\[
\eta_{1k}^{-1/2}A_k\bigl(1+\sqrt{\eta_{1k}}\bigr)
=1-\sqrt{\eta_{1k}}.
\]

Diese Definition ist äquivalent zu

\[
A_k=\sqrt{\eta_{1k}}\,
\frac{1-\sqrt{\eta_{1k}}}{1+\sqrt{\eta_{1k}}}.
\]

Das Produkt beider Definitionen verwandelt die potenzierte Relation unmittelbar in

\[
4A_1A_2=A=\mathrm{const}.
\]

**Status:** Die Produktgleichung ist algebraisch korrekt **bedingt durch** (i) den heuristischen \(s\)-Ansatz, (ii) die Integrationsgrenzen, (iii) den Potentialansatz, (iv) die aus (98) eingesetzten internen Komponenten und (v) die Definition der beiden \(A_k\). Der Faktor 4 steht bereits in der nach (98) potenzierten Relation; er wird hier noch nicht mit den vier Konfigurationszonen begründet. Die Herleitung der \(\eta_{1k}\) selbst gehört nicht zu dieser Korrelationspassage.

### 6. Einführung von \(C\) über das Energieprinzip (Druckseiten 299–300 / PDF-Seiten 305–306)

Das H-Atom wird als System höherer Ordnung mit potentiellem Anteil \(X\) und kinetischem Anteil \(E\) behandelt. Heim setzt

\[
X+E=\mathrm{const},\qquad d(X+E)=0,\qquad dX=-dE,
\]

mit den Intervallen \(W\leq X\leq V\) und \(0\leq E\leq E_k\); die Ruhemassen von Proton und Elektron sollen nicht in dieses Energieprinzip eingehen.

Die interne Strukturierung müsse \(4A_1A_2=A=\mathrm{const}\) genügen und mit

\[
4\pi\varepsilon_0 f(y)V=e_+e_-=-e_-^2
\]

verknüpft sein. Daraus setzt Heim zunächst nur proportional

\[
W\sim A_1A_2V
\]

und führt dann die neue Funktion beziehungsweise den Faktor \(C\) ein:

\[
W=V\,C(\eta_{11},\eta_{12}).
\]

Die Integration wird als

\[
-E_k=\int_W^V dX=V-W=V(1-C)
\]

geschrieben. Für das externe Feld setzt Heim \(f(y)=y\), die Distanz zwischen \(p\) und \(e^-\), und erhält

\[
e_-^2(1-C)=4\pi\varepsilon_0yE_k.
\]

**Status:** Das Energieerhaltungsprinzip und die Wahl der Integrationsintervalle sind physikalische Annahmen; \(C=W/V\) ist eine Definition. Bereits \(W\sim A_1A_2V\) ist eine Modell-Proportionalität. Die Integration erzeugt den Faktor \(1-C\), bestimmt aber weder \(C=A_1A_2\) noch dessen Proportionalitätsfaktor.

#### Quelleninterner Vorzeichen- und Ordnungsbefund

Die erneute Sichtprüfung beseitigt die OCR-/Transkriptionsfrage: Auf Druckseite 299 stehen eindeutig

\[
W\leq X\leq V,
\qquad
0\leq E\leq E_k.
\]

Auf Druckseite 300 sind ebenso eindeutig das führende Minuszeichen, die Integrationsrichtung von \(W\) nach \(V\) und die Gleichung

\[
-E_k=\int_W^VdX=V-W=V(1-C)
\]

gedruckt. Diese Angaben sind bereits untereinander nicht vorzeichenverträglich: Aus \(W\leq V\) folgt \(V-W\geq0\), aus \(E_k\geq0\) dagegen \(-E_k\leq0\). Eine Gleichheit wäre nur im trivialen Grenzfall \(E_k=0\) und \(V=W\) möglich, während der Text anschließend \(v_H=c\alpha>0\) und damit \(E_k>0\) verwendet.

Zusätzlich setzt dieselbe Druckseite für das äußere Feld

\[
4\pi\varepsilon_0yV=-e_-^2.
\]

Bei der im Text verwendeten positiven Distanz \(y\) ist daher \(V<0\). Aus (98) folgt für \(q=1\), \(k=1,2\) jeweils \(0<\eta_{1k}<1\); mit der Definition der \(A_k\) sind daher \(A_1,A_2>0\). Zusammen mit der späteren Wahl \(C=A_1A_2\), der Angabe \(A_1A_2\ll1\) und \(Y_3=1\) auf Druckseite 302 gilt im verwendeten Rechengang \(0<C<1\). Dann ergibt \(W=VC\) aber \(W>V\), also gerade die umgekehrte Ordnung zur gedruckten Angabe \(W\leq X\leq V\).

**Befund:** Es handelt sich um einen echten lokalen Konflikt im Primärdruck, nicht um einen OCR- oder Transkriptionsfehler. Innerhalb der geprüften Passage wird nicht entschieden, ob die Ungleichungsrichtung, das Minus vor \(E_k\), die Integrationsorientierung oder eine Vorzeichenkonvention für die Energien zu korrigieren wäre. Das ist als offene Quellenfrage zu führen; eine stillschweigende Reparatur wäre spekulativ.

### 7. Verbindung von \(C\) mit \(\alpha\) (Druckseiten 300–301 / PDF-Seiten 306–307)

Für das Korrespondenzsystem wird die \(R_6\)-Metrik pseudoeuklidisch approximiert und Lorentzinvarianz angesetzt. Aus der dynamischen Stabilität des H-Atoms, zeitlich konstanten zusätzlichen Koordinaten und der Vernachlässigung des gravitativen Anteils folgert Heim die Reduktion auf den relevanten Lorentzfaktor. Die Geschwindigkeit des korpuskulär aufgefassten Elektrons im K-Schalen-Grundzustand wird dann identifiziert durch

\[
v_H=c\alpha>0.
\]

Für einen K-Schalenmeridian \(s_H=2\pi r_H\) wird eine Lorentzverkürzung angesetzt:

\[
s=2\pi y=s_H\sqrt{1-\alpha^2},
\qquad
y=r_H\sqrt{1-\alpha^2}.
\]

Mit Impuls \(mv_H\) und „invarianter Transversalmasse“ verwendet Heim

\[
E_k=mv_Hc=\alpha mc^2,
\]

und erhält

\[
e_-^2(1-C)
=4\pi\varepsilon_0r_H\alpha\sqrt{1-\alpha^2}\,mc^2.
\]

Danach identifiziert Heim die Ruheenergie mit dem Energiequant einer „zirkulären Elektronenwelle“ und setzt

\[
mc^2=h\nu_H=\frac{ch}{\lambda_H},
\quad
\lambda_H=2\pi r_H,
\quad
\varepsilon_0cR_-=1,
\quad
R_-=\sqrt{\mu_0/\varepsilon_0}
\]

ein. Dabei sind \(mc^2=h\nu_H=ch/\lambda_H\) in dieser Anwendung und insbesondere \(\lambda_H=2\pi r_H\) source-interne Modellidentifikationen; die Quelle bezeichnet Letzteres als „Quantendualismus des \(e^-\)“. Davon zu unterscheiden sind die elektromagnetischen Identitäten \(\varepsilon_0cR_-=1\) und \(R_-=\sqrt{\mu_0/\varepsilon_0}\). Aus dem gesamten Einsetzungspaket folgt

\[
e_-^2(1-C)
=4\pi\alpha\sqrt{1-\alpha^2}\,\frac{\hbar}{R_-}
\]

folgt. Durch Substitution der früheren Aussage (29) schreibt Heim schließlich

\[
(2\pi)^5\alpha\sqrt{1-\alpha^2}=9\vartheta(1-C).
\]

**Status:** Die letzten Umformungen sind Algebra nach Einsetzen der genannten Relationen. Die Identifikationen \(v_H/c=\alpha\), \(E_k=mv_Hc\), \(mc^2=ch/\lambda_H\) für die zirkuläre Elektronenwelle und \(\lambda_H=2\pi r_H\), ebenso die K-Schalen-Geometrie und Lorentzverkürzung, sind physikalische Inputs des Quellenmodells und keine rein algebraischen oder pauschal „standardmäßigen“ Schritte. Gleichung (29) wird an dieser Stelle übernommen und nicht neu hergeleitet.

### 8. Von \(C\sim A_1A_2\) zu \(C=A_1A_2\) und \(Y_3\) (Druckseite 301 / PDF-Seite 307)

Heim schreibt zunächst

\[
C\sim A_1A_2
\]

und folgert aus der Darstellbarkeit von \(A\) durch \(4A_1A_2=A\), es müsse auch \(A\sim C\) gelten. Als qualitative Begründung heißt es: \(C\) sei eine Korrekturkomponente von (29a), während \(A_1A_2\) die strukturelle Abweichung der Ladungsfelder von Elektron und Proton bei der H-Korrespondenz beschreibe. \(C\) liefere aber nur den Korrekturbeitrag eines strukturellen Elements, also einer besetzten Konfigurationszone.

Da Elektron und Proton als Einheitsstrukturen \(N=1\), \(n_j=0\) behandelt werden und alle \(j\leq4\) Konfigurationszonen mit \(Q_j>0\) besetzt seien, lautet die entscheidende Passage: Für den Proportionalitätsfaktor **„könnte“** der Wert 4 angenommen werden. Daraus setzt Heim

\[
A=4C,
\]

und kombiniert dies mit \(A=4A_1A_2\) zu

\[
C=A_1A_2.
\]

Unmittelbar danach heißt es jedoch, hierbei trete eine Unsicherheit auf, der durch \(Y_3\) Rechnung getragen werden könne. Auf Druckseite 302 / PDF-Seite 308 geht deshalb nicht \(C=A_1A_2\), sondern effektiv

\[
C=A_1A_2Y_3
\]

in Gleichung (105) ein:

\[
(2\pi)^5\alpha\sqrt{1-\alpha^2}
=9\vartheta\bigl(1-A_1A_2Y_3\bigr),
\]

\[
(1+\sqrt{\eta_{1k}})A_k
=(1-\sqrt{\eta_{1k}})\sqrt{\eta_{1k}},
\qquad \alpha>0.
\tag{105}
\]

**Status:** \(C\sim A_1A_2\) ist eine qualitative Modellidentifikation; der Faktor 4 beziehungsweise \(A=4C\) ist eine ausdrücklich als möglich formulierte Zählannahme. \(Y_3\) markiert im Primärtext selbst die verbleibende Unsicherheit dieser Gleichsetzung.

## Trennung nach Begründungstyp

| Schritt | Definition | Algebra | Physikalische/heuristische Annahme | Empirischer Input |
|---|---:|---:|---:|---:|
| \(s(y)\) als Summe relativer Potentialänderungen | ja | – | – | – |
| \(s(\varrho)+s(\delta)=s(\omega)\) | – | – | ja, ausdrücklich „heuristisch“ und „angenommen“ | – |
| Integration und Potenzierung | – | ja, bedingt | Integrationsgrenzen und Potentialansatz | – |
| Definition der \(A_k\) | ja | – | – | – |
| \(A=4A_1A_2\) | – | ja, nach Definition und Vorannahmen | die Vorannahmen bleiben erforderlich | – |
| \(C=W/V\) | ja | – | \(W\sim A_1A_2V\) wird angenommen | – |
| H-Atom als \((e^-,p)\)-Korrespondenz | – | – | ja | Teilchenzuordnung über angenäherte \(m_e,m_p\) |
| \(v_H=c\alpha\), \(E_k=mv_Hc\), Wellen- und K-Schalenmodell | teils Identifikation | nachfolgende Umformungen | ja | EM-Konstanten; die Wellen-/Geometriezuordnungen sind Modellinputs |
| \(C\sim A_1A_2\) | – | – | ja | – |
| Faktor 4: \(A=4C\) | – | – | ja, Zählannahme aus vier Zonen | – |
| \(C=A_1A_2\) | – | ja, aber nur nach der Faktor-4-Annahme | ja, mittelbar | – |
| \(C=A_1A_2Y_3\) in (105) | Parametrisierung der Unsicherheit | Einsetzung | ja | \(Y_3\) in dieser Passage nicht unabhängig bestimmt |

## Belastbare Schlussfolgerung für die Rekonstruktion

Die Quelle rechtfertigt folgende abgestufte Aussage:

- \(A=4A_1A_2\) ist die algebraische Kurzform der integrierten, nach (98) substituierten Potentialrelation, nachdem \(A_1\) und \(A_2\) passend definiert wurden.
- \(C\) stammt aus einer anderen Ebene der Argumentation, nämlich aus \(W=VC\) im Energieansatz des H-Korrespondenzsystems.
- Die Brücke zwischen beiden Ebenen ist zunächst nur \(C\sim A_1A_2\); ihr Proportionalitätsfaktor wird nicht aus der Potential- oder Energiegleichung berechnet.
- Die Wahl des Faktors 4 beruht auf der Zählung von vier besetzten Konfigurationszonen und wird vom Autor ausdrücklich nur als Annahme formuliert. Daher ist \(C=A_1A_2\) keine voraussetzungsfreie Folgerung.
- Die Unsicherheit dieser Brücke wird im Original nicht verborgen, sondern unmittelbar durch den Zusatzfaktor \(Y_3\) parametrisiert. Gleichung (105) enthält daher \(A_1A_2Y_3\).

Es wurde keine neuere physikalische Kritik oder Widerlegungsrecherche vorgenommen; der Bericht rekonstruiert ausschließlich den Begründungsstatus im genannten Primärtext.
