# H004 A16: Buchquelle, W-Anschluss und Herleitungsstatus

Stand: 2026-09-06. Eng begrenzte Quellenreview von Heim,
*Elementarstrukturen der Materie II* (1996-Ausgabe), lokale Datei
`01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`,
SHA-256 `F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.
OCR diente nur als Locator. Vollständig visuell geprüft wurden Druck 325--337
/ PDF 331--343; die Bildanker liegen unter `tmp/pdfs/a16_book/edm2-331.png`
bis `edm2-343.png`. Tragend für A16 sind Druck 330--336 / PDF 336--342.
Zusätzlich wurde die Y-Politik auf Druck 1 / PDF 12 in
`tmp/pdfs/a16_book/intro-012.png` visuell kontrolliert. Keine Masse, kein
Fit und keine moderne Kritik wurden untersucht.

## Ergebnis

H004 enthält die gesuchte Formel ausdrücklich. Druck 335 / PDF 341 druckt

```text
A16 = (pi e)^2 (1 + alpha/(5 eta) (1 + 6 alpha/pi)) Y9.       (109b)
```

Damit ist die im dicht gesetzten H006-Ausdruck offene Slashbindung
quellennah als `alpha/(5*eta)` belegt. H004 führt aber zugleich den
Unsicherheitsfaktor `Y9` mit. Die Quelle leitet weder diesen Faktor noch die
einzelnen Bausteine `(pi e)^2`, `1/5`, `6/pi` oder `eta^(-1)` explizit aus
einer zuvor bewiesenen Funktion ab. Ihr eigener Status ist eine heuristische,
an empirischen Grundzustandsdaten orientierte Koeffizientenermittlung.

## 1. Direkter Strukturpotenz-Anschluss

H004 Druck 325 / PDF 331 führt den Basisanstieg `g(k,q)` ein und beschreibt
`W/g=w` als Strukturpotenz. Der Text sagt, es sei *anzunehmen*, dass diese
aus zwei komponentenweise additiven Anteilen aufgebaut ist, und der Ansatz
`w=1+(2-k)w1+(k-1)w2` werde vorgeschlagen. Druck 330 / PDF 336 nennt die
Form danach ausdrücklich einen „heuristischen Ansatz“ und schreibt die
verschobene Potenzform.

Druck 331--332 / PDF 337--338 bestimmt die formale Rolle des späteren
A16-Terms:

```text
X6 = kappa*eta_qk*F16,
w1 = (1-Q) sum_(i=1)^5 Xi + Q*X6.
```

`X6` wird dort als Spinorpotenz für das Pseudosingulett bezeichnet.
Druck 334 / PDF 340 ersetzt nach dem Grenzübergang die `F_im`-Symbole durch
`A_im` und gibt in (109a) sichtbar

```text
w1 + 1 - k = (1-Q)[A11 - P(A12 + kappa*q/eta_qk*A13)
                   - binom(P,2)(A14-q/eta_qk*A15)]
              + kappa*Q*eta_qk*A16.
```

Das ist die Buchform des in H006 (XVII) wiederkehrenden A16-Beitrags.
Es belegt die gleiche **Strukturrolle**, ohne aus bloßer Symbolgleichheit
eine editionsübergreifend identische vollständige Fassung zu behaupten.

## 2. Was der Autor über die Herleitung sagt

Druck 330--331 / PDF 336--337 sagt, die Form der metronischen Funktionen
`F_im` könne „vorläufig nicht deduziert“ werden; ihre Existenz wird für die
folgende Konstruktion akzeptiert. Auf Druck 334 / PDF 340 werden nur
konstante endliche Grenzwerte angesetzt; `A=A66` wird „aus Gründen der
späteren Vereinfachung“ gesetzt.

Noch klarer sagt Druck 335 / PDF 341: Es sei bislang nicht möglich gewesen,
`F_im` explizit herzuleiten, folglich gelte dies auch für `A_im` und `A66`.
Unter Verwendung der Interpretation (101b) und empirischer Daten der
Grundzustände könne man die Koeffizienten **heuristisch numerisch** auf die
Grenzwerte `pi,e,xi` und die Kopplungskonstanten `alpha,beta` aus (105a)
zurückführen. Die einzelnen Faktoren der A16-Zeile werden dabei nicht weiter
motiviert oder separat abgeleitet.

Der Text führt deshalb laufende Unsicherheitsfaktoren `Y_k` für `k>3` ein;
in der Formel ist A16 konkret mit `Y9` versehen. Druck 336 / PDF 342 setzt
dieses Muster bei Nachbarzeilen fort, etwa mit `Y14`, `Y15` und `Y16` für
`A25`, `A26` und `A31`.

## 3. Verhältnis zu H006 und der Tabellenkonvention

H006 Druck/PDF 7 schreibt die verdichtete Formel ohne sichtbares `Y9`:

```text
A16 = (pi e)^2 [1 + alpha(1+6 alpha/pi)/5 eta].
```

H004 stützt daher genau die bereits getrennt geführte
Denominator-Produkt-Lesart, nicht die linkassoziative Sensitivitätslesart.
Es berechtigt jedoch nicht dazu, das in H004 sichtbare `Y9` still zu
streichen oder den gesamten H006-Block als vollständig hergeleitet zu
etikettieren.

Die Einleitung, Druck 1 / PDF 12, ordnet `Y_k` den „noch nicht völlig
geklärten“ mathematischen Beziehungen zu und setzt für **theoretische
numerische Daten des Tabellenanhangs** alle `Y_k=1` voraus. Dies ist weder
eine statistische Unsicherheitsverteilung noch ein allgemeiner Beleg dafür,
dass H006 oder ein späteres Listing `Y9=1` theoretisch festlegt. Ein solcher
Einsatz wäre eine offen zu kennzeichnende Spezialisierung.

## 4. Befundgrenzen

Gefunden ist eine direkte Buchkette

```text
metronische F16 (nicht explizit deduziert)
  -> Grenzwert A16
  -> kappa*Q*eta_qk*A16 in w1
  -> explizite heuristische A16-Parametrisierung mit Y9.
```

Nicht gefunden wurde auf den visuell geprüften Seiten eine Ableitung, die
gerade den Vorfaktor `(pi e)^2`, die Zahlen `5` und `6`, die
`pi`-Division, die `eta`-Potenz oder `Y9` zwingend macht. Die Seiten geben
auch keine allgemeine Regel, die `Y9` außerhalb ihres Tabellenkontexts auf
eins setzt. Diese negativen Aussagen beschränken sich auf Druck 325--337
/ PDF 331--343, nicht auf das gesamte Buch.
