# Versionsprüfung der Alpha-Schließung: Manuskript 1981 gegen Band II

Stand: 2026-09-06

## Auftrag, Quellen und Methode

Eng verglichen wurden:

- Burkhard Heim, *Magnetfeld und Drehimpulsdichte*, maschinenschriftliches, auf Manuskriptseite 20 mit „Northeim den 21.12.1981“ datiertes und mit „Heim“ unterzeichnetes Manuskript, Manuskriptseiten 3–6 = PDF-Seiten 3–6. Lokale Datei: 01_sources/heim_primary/author_rationale_search/M0042-Magnetfeld-und-Drehimpuls-B-Heim-1981.pdf.
- Burkhard Heim, *Elementarstrukturen der Materie*, Band II, 2. unveränderte Auflage, Andreas Resch Verlag, Innsbruck 1996, ISBN 3-85382-036-0, Druckseiten 297–303 = PDF-Seiten 303–309. Lokale Datei: 01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf.

Alle nachfolgend entscheidenden Potenzen, Indizes, Ungleichungen und Modalformulierungen wurden am Scan kontrolliert. OCR diente nur zum Auffinden. Es wurden keine Alpha-Fits, keine neue externe Recherche und keine Normalisierung einer Fassung auf die andere vorgenommen.

## Kurzbefund

Die Fassungen sind im Argumentationsgang eng verwandt, aber **nicht formelidentisch**. Drei Unterschiede sind für eine Rekonstruktion entscheidend:

1. Das Manuskript definiert die \(A_k\) mit einem Faktor \(\eta_{1k}^{+1}\); das Buch verwendet \(\eta_{1k}^{-1/2}\). Beide Fassungen gelangen intern zu \(A=4A_1A_2\), aber ihre \(A_k\) sind verschiedene Funktionen von \(\eta_{1k}\).
2. Das Manuskript sagt, wegen der freien Verfügbarkeit der Integrationskonstante \(A\) **könnte** \(A=4C\) unterstellt werden. Das Buch motiviert denselben Zahlenfaktor 4 neu durch vier besetzte Konfigurationszonen und sagt ebenfalls nur, er „könnte“ angenommen werden.
3. Das Manuskript führt den unindizierten Unsicherheitsfaktor \(Y\neq0\) ein; das Buch verwendet \(Y_3\). Ein quellenübergreifend gemeinsames \(Y_3\) ist daher nicht belegt.

Eine eigene Parametrisierung \(C=\rho A_1A_2\) ist als Diagnose sinnvoll, wenn \(A_1A_2\), \(\rho\) und der Unsicherheitsfaktor **je Fassung** geführt werden. In der Alpha-Schließung erscheint dann nur das Produkt \(\rho U\), wobei \(U=Y\) im Manuskript und \(U=Y_3\) im Buch ist. Aus der Schließung allein sind \(\rho\) und \(U\) nicht getrennt bestimmbar.

Der bereits bekannte Energieordnungs-Konflikt steht schon auf Manuskriptseite 4: Die Quelle schreibt \(W\leq X\leq V\), aber zugleich \(-E_k=V-W\). Für \(E_k>0\) folgt \(W>V\). Die rückwärts orientierte Integration von \(W\) nach \(V\) ist mit \(-E_k\) vereinbar; die ausgeschriebene numerische Intervallordnung ist es nicht.

## 1. Seitenzuordnung und Grad der Übereinstimmung

| Manuskript 1981 | Band II 1996 | Vergleichsbefund |
|---|---|---|
| S. 3 | Druck 298–299 | Korrespondenzvolumen und Variation interner Potentiale; das Buch formuliert und indiziert ausführlicher. |
| S. 4 | Druck 299–300 | Herleitung von \(A=4A_1A_2\), Energieprinzip, Integrationsintervalle und Übergang zum äußeren Coulombpotential; hier liegt der entscheidende \(\eta\)-Potenzunterschied. |
| S. 5 | Druck 300–302 | Lorentz-/Wellenlängenkette und Alpha-Schließung; \(A=4C\) hat eine andere Begründung, \(Y\) wird zu \(Y_3\), und die \(A_k\)-Nebenbedingung bleibt versionsverschieden. |
| S. 6 | Druck 302–303 | Setzen des jeweiligen Unsicherheitsfaktors auf 1, zweideutige Lösung und Übergang zur nächsten Wechselwirkung; numerische Ausgaben unterscheiden sich. |

„Eng verwandt“ bedeutet hier: Reihenfolge, große Teile des Wortlauts und viele Formeln stimmen strukturell überein. Es bedeutet nicht, dass ein Zeichen- oder Editionsvergleich Identität gezeigt hätte.

## 2. \(A=4A_1A_2\): in beiden Fassungen intern konsistent, aber mit verschiedenen \(A_k\)

Zur kompakten Darstellung sei

\[
x_k:=\sqrt{\eta_{1k}},\qquad k=1,2
\]

gesetzt. Diese Substitution ist nur unsere Algebrahilfe.

### 2.1 Manuskript, Seiten 4–5

Der Scan auf Manuskriptseite 4 zeigt ohne negative oder gebrochene Potenz:

\[
\eta_{11}\eta_{12}A
=4\frac{1-\sqrt{\eta_{11}}}{1+\sqrt{\eta_{12}}}
   \frac{1-\sqrt{\eta_{12}}}{1+\sqrt{\eta_{11}}}.
\tag{MS-P}
\]

Anschließend setzt das Manuskript für \(k=1\) oder \(k=2\)

\[
\eta_{1k}A_k(1+\sqrt{\eta_{1k}})
=1-\sqrt{\eta_{1k}}
\tag{MS-Ak}
\]

und erhält

\[
4A_1A_2=A=\mathrm{const}.
\]

Tatsächlich folgt aus (MS-Ak)

\[
A_k^{\rm MS}
=\frac{1-x_k}{x_k^2(1+x_k)}.
\]

Damit ist

\[
4A_1^{\rm MS}A_2^{\rm MS}
=\frac{4}{\eta_{11}\eta_{12}}
  \frac{1-x_1}{1+x_1}
  \frac{1-x_2}{1+x_2},
\]

was genau der nach \(A\) aufgelösten Manuskriptform (MS-P) entspricht. \(A=4A_1A_2\) ist innerhalb dieser Fassung also algebraisch konsistent.

Auf Manuskriptseite 5 wird dieselbe \(A_k\)-Bedingung mit dem Faktor \(\eta_{1k}^{+1}\) neben der Alpha-Schließung wiederholt.

### 2.2 Band II, Druckseiten 299 und 302

Der Buchscan zeigt auf Druckseite 299 dagegen:

\[
\eta_{11}^{-1/2}\eta_{12}^{-1/2}A
=4\frac{1-\sqrt{\eta_{11}}}{1+\sqrt{\eta_{12}}}
   \frac{1-\sqrt{\eta_{12}}}{1+\sqrt{\eta_{11}}}
\tag{B-P}
\]

und

\[
\eta_{1k}^{-1/2}A_k(1+\sqrt{\eta_{1k}})
=1-\sqrt{\eta_{1k}}.
\tag{B-Ak-299}
\]

Auch daraus schreibt Heim

\[
4A_1A_2=A=\mathrm{const}.
\]

Gleichung (105) auf Druckseite 302 gibt (B-Ak-299) äquivalent wieder als

\[
(1+\sqrt{\eta_{1k}})A_k
=(1-\sqrt{\eta_{1k}})\sqrt{\eta_{1k}}.
\tag{B-Ak-105}
\]

Somit gilt in der Buchfassung

\[
A_k^{\rm B}
=x_k\frac{1-x_k}{1+x_k},
\]

und (B-P) liefert wiederum intern konsistent \(A=4A_1^{\rm B}A_2^{\rm B}\).

### 2.3 Algebraische Konsequenz des Potenzwechsels

Wenn man nur zum Vergleich dieselben Zahlenwerte \(\eta_{1k}\) in beide gedruckten Definitionen einsetzte, ergäbe sich

\[
A_k^{\rm MS}
=\frac{A_k^{\rm B}}{\eta_{1k}^{3/2}},
\]

also

\[
A_1^{\rm MS}A_2^{\rm MS}
=\frac{A_1^{\rm B}A_2^{\rm B}}
       {(\eta_{11}\eta_{12})^{3/2}}.
\]

Das ist eine algebraische Vergleichsaussage, **keine** Behauptung, die \(\eta\)-Parameter oder \(A_k\) seien editionsübergreifend identisch gemeint. Sie zeigt aber, warum das Manuskript nicht unverändert als Recheninput der Buchgleichung verwendet werden darf: Der Potenzwechsel lässt sich nicht allein durch Umstellen derselben Gleichung erklären.

## 3. Von \(A=4A_1A_2\) zu \(A=4C\): unterschiedliche Begründungen

### 3.1 Manuskriptseite 5

Nach der gemeinsamen Vorstufe

\[
(2\pi)^5\alpha\sqrt{1-\alpha^2}=9\vartheta(1-C)
\tag{Vorstufe}
\]

schreibt Heim sinngemäß und im entscheidenden Modalwort eindeutig:

- \(C\sim A_1A_2\);
- wegen der „freien Verfügbarkeit“ der Integrationskonstante \(A\) in \(4A_1A_2=A\) **könnte** \(A=4C\), also \(C=A_1A_2\), unterstellt werden;
- dabei trete eine Unsicherheit auf, der durch den Faktor \(Y\) als Unsicherheitsfaktor, \(Y\neq0\), Rechnung getragen werden könne.

Die Manuskript-Schließung lautet daraufhin

\[
(2\pi)^5\alpha\sqrt{1-\alpha^2}
=9\vartheta(1-A_1A_2Y),
\tag{MS-A}
\]

zusammen mit (MS-Ak) und \(\alpha>0\). Der Scan bezeichnet die Gleichung als (A).

**Status:** Die Freiheit einer Integrationskonstante zeigt nicht aus sich heraus, dass ihr Wert physikalisch \(4C\) sein muss. Heim kennzeichnet diesen Schritt selbst modal als mögliche Unterstellung und führt unmittelbar danach einen Unsicherheitsfaktor ein.

### 3.2 Band II, Druckseite 301

Das Buch übernimmt die Vorstufe, erweitert aber die Begründung:

- Aus \(C\sim A_1A_2\) und der Darstellung \(A=4A_1A_2\) müsse auch \(A\sim C\) gelten.
- \(C\) wird als Korrekturkomponente von (29a), \(A_1A_2\) als strukturelle Abweichung der Ladungsfelder bei der H-Korrespondenz gedeutet.
- Weil \(C\) nur den Korrekturbeitrag eines Strukturelements beziehungsweise einer besetzten Konfigurationszone liefere und bei den betrachteten Einheitsstrukturen alle \(j\leq4\) Zonen besetzt seien, **könnte** für den Proportionalitätsfaktor der Wert 4 angenommen werden.
- Daraus werden \(A=4C\) beziehungsweise \(C=A_1A_2\) geschrieben; die verbleibende Unsicherheit wird mit \(Y_3\) berücksichtigt.

Die Buch-Schließung (105) auf Druckseite 302 lautet

\[
(2\pi)^5\alpha\sqrt{1-\alpha^2}
=9\vartheta(1-A_1A_2Y_3),
\tag{B-105}
\]

zusammen mit (B-Ak-105) und \(\alpha>0\).

**Versionsbefund:** Das numerische Ergebnis \(A=4C\) ist gleich geschrieben, seine Begründung aber nicht. Das Manuskript beruft sich auf die freie Verfügbarkeit von \(A\); das Buch führt eine Zählannahme von vier besetzten Zonen ein. Beide Texte bleiben mit „könnte“ modal. Keine der Fassungen beweist, dass andere Proportionalitätsfaktoren ausgeschlossen sind.

## 4. \(Y\) gegen \(Y_3\) und die sichtbaren Folgeunterschiede

Das Manuskript verwendet auf Seite 5 den unindizierten Faktor \(Y\neq0\) und setzt auf Seite 6 für die dortige numerische Diskussion \(Y=1\). Das Buch verwendet auf Druckseiten 301–302 \(Y_3\), verweist dabei auf seine Vorbemerkung und setzt anschließend \(Y_3=1\).

Schon deshalb dürfen (MS-A) und (B-105) nicht als identische Gleichungsversionen katalogisiert werden. Hinzu kommt die unterschiedliche \(A_k\)-Definition. Sichtbar verschieden sind auch die von den Quellen selbst anschließend gedruckten Ausgaben:

| Größe | Manuskript S. 6 | Band II Druck 302 |
|---|---:|---:|
| \(\alpha_{(+)}^{-1}\) | \(137{,}03602725\) | \(137{,}03596147\) |
| \(\alpha_{(-)}^{-1}\) | \(1{,}00001411\) | \(1{,}00001363\) |
| \(\alpha_{(+)}\) | \(0{,}007297351069\) | \(0{,}007297354572\) |
| \(\alpha_{(-)}=\beta\) | \(0{,}99998589\) | \(0{,}99998637\) |

Diese Tabelle gibt nur die visuell gelesenen Quellenausgaben wieder. Sie ist keine Neuberechnung, kein Fit und kein Genauigkeitsvergleich.

## 5. Eigene Diagnoseparametrisierung \(C=\rho A_1A_2\)

### 5.1 Sinnvolle Form

Die beiden Quellen beginnen vor dem strittigen Proportionalitätsschritt mit (Vorstufe). Für eine transparente eigene Diagnose kann deshalb je Fassung \(s\) gesetzt werden:

\[
P_s:=A_{1,s}A_{2,s},
\qquad
C_s:=\rho_sP_s.
\tag{D1}
\]

Dabei steht \(s={\rm MS}\) für die Manuskriptdefinition (MS-Ak) und \(s={\rm B}\) für die Buchdefinition (B-Ak-105). Aus \(A_s=4P_s\) folgt, sofern \(\rho_s\neq0\),

\[
A_s=\frac{4}{\rho_s}C_s.
\]

Die in beiden Quellen erwogene Setzung \(A=4C\) ist also der Spezialfall

\[
\rho_s=1.
\]

Diese Schreibweise isoliert gerade den nicht hergeleiteten Proportionalitätsschritt, ohne ihn auf 1 festzulegen.

### 5.2 Einbeziehung des Unsicherheitsfaktors

Die Quellen schreiben nicht ausdrücklich eine neue Definition \(C=A_1A_2Y\) beziehungsweise \(C=A_1A_2Y_3\), sondern führen den jeweiligen Unsicherheitsfaktor direkt in der Schließung ein. Als **eigene effektive Parametrisierung** kann man schreiben

\[
C_{\mathrm{eff},s}:=\rho_sU_sP_s,
\qquad
U_{\rm MS}:=Y,
\qquad
U_{\rm B}:=Y_3,
\tag{D2}
\]

und damit

\[
(2\pi)^5\alpha\sqrt{1-\alpha^2}
=9\vartheta\left(1-\rho_sU_sP_s\right).
\tag{D3}
\]

Das ist algebraisch sinnvoll und macht drei Entscheidungen sichtbar:

1. welche \(A_k\)-Version und damit welches \(P_s\) verwendet wird;
2. welcher Proportionalitätsfaktor \(\rho_s\) zwischen \(C\) und \(P_s\) angenommen wird;
3. welcher quellenspezifische Unsicherheitsfaktor \(U_s\) gilt.

In (D3) erscheint allerdings nur

\[
\chi_s:=\rho_sU_s.
\]

Die Alpha-Schließung allein kann \(\rho_s\) und \(U_s\) daher nicht getrennt identifizieren. Ohne einen zusätzlichen, quellenunabhängigen Zusammenhang wäre ein Versuch, beide zugleich aus derselben Alpha-Zahl zu bestimmen, unterdeterminiert.

### 5.3 Warum ein gemeinsames \(\rho Y_3\) für beide Quellen nicht quellengetreu wäre

Für die **Buchfassung** ist \(\rho_{\rm B}Y_3\) eine brauchbare eigene Diagnosegröße. Für das Manuskript müsste dieselbe Rolle aber \(\rho_{\rm MS}Y\) übernehmen. Ein versionsübergreifend gemeinsames \(\rho Y_3\) würde mindestens zwei unbelegte Identitäten voraussetzen:

- \(Y=Y_3\);
- \(P_{\rm MS}=P_{\rm B}\) trotz verschiedener \(\eta\)-Potenzen in den \(A_k\)-Definitionen.

Darum sollte eine gemeinsame Implementierung höchstens das neutrale Schema \(\rho_sU_sP_s\) teilen. Die konkreten Definitionen bleiben pro Quelle getrennt.

## 6. Energieordnungs-Konflikt bereits im Manuskript

### 6.1 Visueller Befund Manuskriptseite 4

Das Manuskript schreibt klar:

\[
X+E=\mathrm{const},
\qquad dX=-dE,
\]

und für die Intervalle

\[
W\leq X\leq V,
\qquad 0\leq E\leq E_k.
\tag{MS-I}
\]

Unmittelbar danach stehen \(W=VC(\eta_{11},\eta_{12})\) und

\[
-E_k=\int_W^V dX=V-W=V(1-C).
\tag{MS-E}
\]

Für das äußere Proton-Elektron-Feld gilt auf derselben Seite

\[
4\pi\varepsilon_0 yV=-e_-^2,
\]

also bei \(y>0\) insbesondere \(V<0\).

### 6.2 Enge algebraische Konsequenz

Schon aus (MS-E) folgt

\[
W=V+E_k.
\]

Für \(E_k>0\) ist daher \(W>V\), für \(E_k=0\) gilt \(W=V\). Dies widerspricht der in (MS-I) ausgeschriebenen Ordnung \(W\leq X\leq V\), außer im trivialen Gleichheitsfall.

Die Integrationsgleichung selbst ist nicht notwendig widersprüchlich: Ein Integral von der numerisch größeren Grenze \(W\) zur kleineren Grenze \(V\) ist negativ und kann \(-E_k\) ergeben. Lokal problematisch ist die gleichzeitig gedruckte Intervallordnung. Eine naheliegende, aber nicht von der Quelle bestätigte Korrekturhypothese wäre daher

\[
V\leq X\leq W
\]

anstelle von \(W\leq X\leq V\). Dies bleibt ausdrücklich eine editorische Diagnose, kein stillschweigend eingesetzter Quellentext.

### 6.3 Vergleich mit Band II

Band II übernimmt auf Druckseiten 299–300 dieselben Bestandteile:

\[
W\leq X\leq V,
\qquad 0\leq E\leq E_k,
\qquad
-E_k=\int_W^VdX=V-W=V(1-C),
\]

sowie das negative äußere Coulombpotential. Der Konflikt wurde damit nicht erst beim Buchsatz 1996 eingeführt; er ist bereits im datierten Manuskript von 1981 sichtbar. Ob er schon in einer noch früheren Vorlage stand oder bewusst als orientiertes Intervall mit unpassender Ungleichungsnotation gemeint war, lässt der enge Quellenvergleich offen.

Die nachfolgende Umformung

\[
e_-^2(1-C)=4\pi\varepsilon_0yE_k
\]

ist mit \(V<0\) und (MS-E) algebraisch verträglich. Der lokale Ordnungsbefund allein widerlegt daher nicht die gesamte nachfolgende Schließung; er markiert eine konkret prüfbare Vorzeichen-/Intervallstelle.

## 7. Belastbare Trennung für weitere Rekonstruktionen

### Manuskriptfassung 1981

\[
\eta_{1k}A_k(1+\sqrt{\eta_{1k}})=1-\sqrt{\eta_{1k}},
\]

\[
A=4A_1A_2,
\qquad
A=4C\ \text{„könnte ... unterstellt werden“},
\]

\[
(2\pi)^5\alpha\sqrt{1-\alpha^2}
=9\vartheta(1-A_1A_2Y),
\qquad Y\neq0.
\]

### Buchfassung 1996

\[
\eta_{1k}^{-1/2}A_k(1+\sqrt{\eta_{1k}})=1-\sqrt{\eta_{1k}},
\]

äquivalent in (105):

\[
(1+\sqrt{\eta_{1k}})A_k
=(1-\sqrt{\eta_{1k}})\sqrt{\eta_{1k}},
\]

\[
A=4A_1A_2,
\qquad
A=4C\ \text{als mögliche Vier-Zonen-Annahme},
\]

\[
(2\pi)^5\alpha\sqrt{1-\alpha^2}
=9\vartheta(1-A_1A_2Y_3).
\]

### Eigene Diagnose, nicht Heim-Zitat

\[
P_s=A_{1,s}A_{2,s},
\qquad
C_s=\rho_sP_s,
\qquad
C_{\mathrm{eff},s}=\rho_sU_sP_s,
\]

mit \(U_{\rm MS}=Y\) und \(U_{\rm B}=Y_3\). Dieses Schema ist geeignet, die Proportionalitätsannahme und den Unsicherheitsfaktor sichtbar zu machen. Es rechtfertigt weder die Gleichsetzung der beiden \(A_k\)-Versionen noch die getrennte Bestimmung von \(\rho_s\) und \(U_s\) aus der Alpha-Schließung.

## Schlussfolgerung

Der Manuskriptfund schließt eine historische Lücke, aber keine algebraische Versionslücke. Er zeigt, dass die H-Schließung spätestens 1981 vorlag und dass Heim \(A=4C\) damals mit der Freiheit der Integrationskonstante verband. Die Buchfassung ersetzt diese Begründung durch eine angenommene Vier-Zonen-Zählung und ändert zugleich \(Y\to Y_3\) sowie, besonders folgenreich, die \(\eta\)-Potenzen der \(A_k\)-Definition.

Für eine publizierbare Rekonstruktion müssen deshalb mindestens zwei Quellprofile erhalten bleiben. Die neutrale Parametrisierung \(\rho_sU_sP_s\) ist als eigene Diagnose vertretbar, solange ihr Status offengelegt und nicht als bei Heim gedruckte Formel ausgegeben wird. Der Energieordnungs-Konflikt sollte als bereits 1981 belegte lokale Intervall-/Vorzeichenfrage geführt werden, nicht als stillschweigend reparierter Eingang der kanonischen Rechnung.
