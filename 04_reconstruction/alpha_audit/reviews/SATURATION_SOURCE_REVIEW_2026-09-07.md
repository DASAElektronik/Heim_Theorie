# Sättigungszweig für die eigene `A(k=1)=1/5`-Zelle — Quellenreview

## Ergebnis

Unter der **eigenen** Übertragung des Etappe-35-`1/5`-Zweigs in die auf
Druck S. 341 beschriebene Sättigungsentscheidung ergibt sich für

```text
N_(3)=1,   C=alpha_3*N_(3) etwa 0.97865879,   W_5 > C
```

notwendig `N_(4)=0`. Das Ergebnis hängt nicht an der ungeklärten
Messbarkeitsschwelle der TRC-Neuner-Ausnahme:

```text
TRC(C)=0             -> N_(4)=0,
TRC(C)=1>C           -> N_(4)=TRC(C)-1=0.
```

Die zweite Zeile ist nur eine logische Prüfung der im Text genannten
bedingten Minus-eins-Regel, keine Behauptung, dass das konkrete
`C≈0.97866` eine Neunerfolge sei. Bei normalem Abschneiden ist es das
nicht und `TRC(C)=0`.

Das ist keine originale Buchrechnung für `A(k=1)=1/5`: Druck S. 341
druckt bei `k=1` die Inversion mit dem zu seinem Externterm gehörenden
Faktor 3, nicht eine `1/5`-Fassung. Die Anwendung auf den eigenen
Gegenfaktualzweig ist daher ein bedingter Entscheidungs-Test, keine
Autorenformel, keine neue Parameterwahl und keine Masse.

## Quelle und Sichtumfang

H004: Burkhard Heim, *Elementarstrukturen der Materie 2*, zweite
unveränderte Auflage (1996), SHA-256
`F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.

Vollseitig visuell geprüft:

| Druckseite / PDF | Relevanz | Render |
| --- | --- | --- |
| 328 / 334 | (107a), nichtkollabierter Zweig und Kollaps-/Anhebungsregel | `tmp/pdfs/a16_book/edm2-334.png` |
| 329 / 335 | gewichtete Sigma-Bandbreite (107b) | `tmp/pdfs/a16_book/edm2-335.png` |
| 330 / 336 | (108), gedruckter Externterm, `g(k,q)`, `W=g*w` | `tmp/pdfs/a16_book/edm2-336.png` |
| 340–342 / 346–348 | Exhaustion, TRC, Sättigung und nur-k=2-Transfer | `tmp/pdfs/f16_constraints/edm2-346.png` bis `edm2-348.png` |

Die hochaufgelöste Detailansicht von Druck 341 wurde zusätzlich geprüft:
`tmp/pdfs/f16_constraints/selection-detail-347.png`. OCR wurde lediglich
als Locator benutzt. Keine weitere Buchsuche, Rechnerauswertung oder
Dateiänderung außerhalb dieses Reviews erfolgte.

## Gedruckte Regelkette

### 1. Direkte und gewichtete Strukturgrößen bleiben getrennt

Druck S. 328, (107a), enthält für `j>1` den aktiven Zweig

```text
beta_j = delta_(j-1)G_(j-1)-G_j >= 1
```

und daneben den Kollapszweig `beta_j=0, G_j=0` mit Anhebung in Zone
`j-1`. Für `j=4` ist in der früheren, ungewichteten Auspackung dieses
Zweigs `beta_4=N_(3)-N_(4)`; die Sättigungsstelle auf S. 341 verweist
ausdrücklich auf **dieses** `beta_4=1 aus (107a)`.

Davon getrennt druckt S. 329, (107b), für die Sigma-Anregung

```text
beta_4 = alpha_3*N_(3)-N_(4) > 0.
```

Sie ist keine stillschweigende Umdefinition der (107a)-Größe. Nach dem
unten bedingten Ergebnis `N_(3)=1,N_(4)=0` wären daher beide Aussagen
getrennt wahr: ungewichtet `beta_4=1`, gewichtet `alpha_3>0`. Es folgt
nicht `alpha_3=1`.

### 2. Buchregel auf Druck 341

Nach Exhaustion der ersten drei Zonen wird `W_4` gebildet. Der Text nennt
zunächst die Fälle `0<=W_4<=1` und `1<W_4<(alpha_3N_(3))_max` (den
zweiten im Text speziell mit `k=2`, `alpha_3>1`). Er definiert `TRC` als
Abschneiden der Dezimalstellen; nur eine Folge `0.99...99` bis unter eine
nicht weiter numerisch festgelegte Messbarkeitsschwelle werde zu 1
behandelt.

Für die Bestimmung von `N_(4)` wird anschließend gedruckt

```text
(2k-1) W_5 = -3 Q_4 ln(W_4).
```

Bei Divergenz `W_5 -> infinity` für `W_4=0` **oder** bei
`W_5>alpha_3N_(3)` schreibt der Text die Maximalbesetzung als

```text
N_(4) = TRC(alpha_3*N_(3)).
```

Erst danach folgt die konditionale Ergänzung:

```text
Falls TRC(alpha_3*N_(3)) > alpha_3*N_(3),
ist wegen beta_4=1 aus (107a)
N_(4) = TRC(alpha_3*N_(3)) - 1.
```

Falls dagegen `W_5<=alpha_3*N_(3)`, gilt `N_(4)=TRC(W_5)`. Die
Minus-eins-Regel ist also nicht eine allgemeine Abrundungsregel, sondern
an die explizit gedruckte strikte Vergleichsbedingung gebunden.

### 3. Einsetzen nur als eigene Etappe-35-Anwendung

Der Vorvertrag für die eigene Sensitivität liefert in jeder `1/5`-Zelle
den ersten Dreierpräfix `N_(1),N_(2),N_(3)=(14,10,1)` und den unveränderten
profilabhängigen Wert `alpha_3≈0.97865879`. Somit liegt die Kapazität

```text
C=alpha_3*N_(3) in (0,1).
```

Die eigene Inversion des gegenfaktualen Externterms
`E(n)=exp(-n/5)` verlangt `W_5=-5 ln(W_4)` und liefert ungefähr `14.345`;
sie liegt deutlich über `C`. Dies ist nur die algebraisch konsistente
Fortsetzung der **eigenen** `1/5`-Definition, nicht der auf S. 341
gedruckte Ausdruck.

S. 341 selbst ergäbe bei bloßem Einsetzen desselben eigenen Restwerts in
seine gedruckte `k=1,Q_4=1`-Relation `W_5=-3 ln(W_4)`, ebenfalls einen
positiven Wert über `C`. Dies zeigt nur, dass beide Rechenwege dieselbe
Sättigungsseite `W_5>C` erreichen; es legitimiert nicht, die gedruckte
Faktor-3-Relation als Buchformel für `A=1/5` umzuschreiben.

Aus `W_5>C` folgt damit nach der gedruckten Entscheidungsfolge
`N_(4)=TRC(C)`, mit der oben gesondert geprüften möglichen Minus-eins-
Korrektur. Weil `0<C<1`, ist das Resultat in beiden TRC-Fällen `N_(4)=0`.
Die Sättigungsentscheidung ist in diesem engen Schluss deshalb robuster
als eine Auswahl, die vom genauen `W_5`-Wert oder einer unbekannten
Neuner-Schwelle abhinge.

## Grenzen

- Der Transfer von `j=3` nach `j=4` auf S. 341 wird dort nur im Kontext
  `k=2` und `W_5<0` eingeführt. Er ist für den aktiven `k=1`-Zweig keine
  hier verfügbare Ersatzregel.
- Die Quelle stellt die Exhaustionslogik im Rahmen von (108) und einer
  vollständigen numerischen Bestimmung von `W,a,b` für einen V6-Punkt dar.
  Etappe 35 ersetzt diese Gesamtbestimmung nicht; sie verwendet nur den
  festgelegten skalarisierten Vergleichsvertrag.
- Das Ergebnis `N_(4)=0` sagt nicht, dass die exakte skalare Gleichung
  `R_A=0` erfüllt ist. Die vorherige Existenzprüfung bleibt separat und
  hat für den gesamten direkten Gate-Überbereich keinen Nullpunkt
  gefunden.
- Keine Behauptung wird über andere A-/Y-Werte, Kollapsdynamik,
  eine vollständige historische TRC-Implementierung, physikalische
  Zustandsrealität oder eine Autorenkorrektur getroffen.
