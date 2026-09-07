# Sättigungsregel: strukturelle Auswahl und Gleichungserhalt

2026-09-07, Etappe 36. Ausgang `efb812d`, Vorvertrag `fa25c42`.
Fortsetzung des [festen A-Vergleichs](DECAY_SENSITIVITY_2026-09-06.md).

## Ergebnis

Wenden wir Heims Sättigungsvorschrift auf unseren unveränderten
`A(k=1)=1/5`-Gegenprobefall an, ergibt sich eindeutig
`N=(14,10,1,0)`. Das Tupel besteht die geprüften direkten
Strukturbedingungen. Auch die getrennte gewichtete Sigma-Größe ist
positiv. Die Sättigung hat hier also eine konkrete begrenzende Wirkung.

Sie löst aber nicht die feste exakte Skalargleichung: Der Externterm
ist nun 1 statt des benötigten Restes von etwa 0.05675. Es bleibt
`R=1-W4`, ungefähr 0.94325. Das ist keine Massenabweichung und kein
neuer unabhängiger Fehler gegenüber dem Existenzbefund aus Etappe 35.

## 1. Was die Quelle vorschreibt und was wir übertragen

H004 Druck 340-342 beschreibt die gestaffelte Auswahl. Auf Druck 341
folgt nach dem dritten Schritt der logarithmische Hilfswert. Für
`cap=a3*N3` gilt im Sättigungsfall:

```text
raw_N4 > cap:
    t = TRC(cap)
    N4 = t-1, falls t > cap
    N4 = t,   sonst.
```

TRC schneidet gewöhnlich Dezimalstellen ab; Heim nennt eine besondere
Neuner-Promotion unterhalb einer nicht numerisch festgelegten
Messbarkeitsschwelle. Das Minus 1 steht ausdrücklich unter einer
Bedingung. Es ist weder immer abzuziehen noch allgemein durch
`ceil(cap)-1` zu ersetzen.

Die gedruckte Umkehrung lautet `(2k-1)*W5=-3*Q4*ln(W4)`. Bei den
Buchparametern k=Q4=1 gehört sie zu A=1/3. Unsere schon festgelegte
Gegenprobe A=1/5 verlangt hingegen `raw_N4=-5*ln(W4)`. Die Anwendung
der gleichen Kappenentscheidung auf diesen geänderten Exponentialterm
ist unsere Übertragung, keine von Heim publizierte 1/5-Rechnung.
Die alten g/W-Werte der jeweiligen Gegenprobe bleiben dabei fest.

Der Transfer aus Zone 3 ist hier nicht ausgelöst: Der vorliegende Rest
liegt zwischen 0 und 1, der Hilfswert ist positiv, und der Buchtext
behandelt den negativen Transferzweig im k=2-Kontext. Wir ergänzen keine
neue Transfer-, Kollaps- oder Rücksprungregel.

## 2. Warum die TRC-Unklarheit hier nichts entscheidet

In beiden 1/5-Zellen ist `N3=1` und `0<cap=a3<1`. Daher:

| Für diesen Schluss betrachteter TRC-Ausgang | Bedingte Korrektur | N4 |
|---|---|---:|
| Abschneiden auf 0 | 0 ist nicht größer als cap | 0 |
| Hypothetische Promotion auf 1 | 1 ist größer als cap, daher minus 1 | 0 |

Die zweite Zeile behauptet nicht, 0.97866 sei eine Neunerfolge oder die
Promotion tatsächlich erlaubt. Sie zeigt, dass sogar diese zusätzliche
Möglichkeit das Ergebnis nicht ändern würde. Eine unbekannte Schwelle
wurde deshalb weder geschätzt noch als Epsilon programmiert.

Unser allgemeines bedingtes Lemma: Wenn `TRC(c)` für `c>=0` nur
`floor(c)` oder `ceil(c)` sein kann, dann ist
`TRC(c)-1_[TRC(c)>c]=floor(c)`. Bei ganzzahligem c wird nichts abgezogen.
Das ist eine Aussage über die zusammengesetzte Kappenregel unter der
genannten Annahme, nicht über den vollständigen Buchoperator TRC.

## 3. Alle vier unveränderten Vergleichszellen

Die zwei 1/3-Zellen bleiben gewöhnliche Kontrollfälle. Die zwei
1/5-Zellen werden ausschließlich im bereits erreichten Sättigungszweig
fortgesetzt. Zahlen sind dimensionslose, gerundete Darstellungen.

| Alpha-Profil / A | N nach Auswahl | Direkte beta2,beta3,beta4 | Separate Sigma-Größe | R=T_A-W_A |
|---|---|---|---:|---:|
| (105), Y3=1 / 1/3 | (14,9,13,7) | (2459,-10,6) | 5.722564268134031398 | 0.018486682683129778 |
| Druckalpha / 1/3 | (14,9,13,7) | (2459,-10,6) | 5.722564269105535831 | 0.018486687523355174 |
| (105), Y3=1 / 1/5 | (14,10,1,0) | (2359,99,1) | 0.978658789856463954 | 0.943249254966522970 |
| Druckalpha / 1/5 | (14,10,1,0) | (2359,99,1) | 0.978658789931195064 | 0.943249258949052267 |

Bei 1/5 bestehen alle drei direkten Bandbreiten `>=1`. Die zweite
Ordnungsreihe hat Margen `(2644,99,0)`; das Zentrum ist positiv mit
`N1^3=2744`. Die letzte Null ist der erlaubte Rand `N3=1`, nicht der
Kollapswert `beta4=0`. Die gewichtete Größe aus (107b) lautet dagegen
`sigma=a3*N3-N4=a3>0`. Ihre Positivität ist erfüllt; den ganzzahligen
Schwellwert `>=1` aus der anderen Definition darauf zu übertragen,
wäre in dieser Diagnose unzulässig. Der Quellenanschluss beider mit
beta4 bezeichneten Größen bleibt getrennt dokumentiert.

Mit den festen Gerüstwerten `Q=(3,3,2,1)` folgt `n=N-Q=(11,7,-1,-1)`.
Das ist nicht allein wegen der negativen kleinen Besetzungen verboten:
H004 Druck 322 erlaubt diese ausdrücklich bei `N_j>=0`, und (107a) auf
Druck 328 nennt `n_j>=-Q_j`. Die letzte Komponente erreicht hier genau
ihr Minimum. Nicht alle N_j sind null; wir setzen das Tupel nicht mit
dem vollständig leeren Referenzzustand gleich. Ebenso beweisen diese
lokalen Bedingungen weder sämtliche L_j-Grenzen noch physikalische
Realisierung oder eine vollständige Zulassung im gesamten Heim-Modell.

## 4. Der verbleibende Rest ist analytisch gesichert

Bei unverändertem Präfix definiert
`W4=W_A-(a1*N1^3+a2*N2^2+a3*N3)` den benötigten Externbeitrag. Deshalb
gilt nach dem gewählten N4 genau

```text
R = a1*N1^3+a2*N2^2+a3*N3+exp(-A*N4)-W_A
  = exp(-A*N4)-W4.
```

Für die gesättigte Ausgabe N4=0 folgt `R=1-W4>0`. Das ist nicht nur
eine fast identische Dezimalrechnung: Rationale auswärts gerundete
Intervalle sichern in beiden 1/5-Profilen `R>0.9432492549`. Beide
Auswertungswege werden getrennt gerechnet und ihre Einschlüsse geprüft.

Der Befund passt zum bereits vollständigen Existenznachweis aus Etappe
35. Dort war auch dieses Tupel schon enthalten. Neu ist hier die
quellengebundene Herleitung, dass gerade die Sättigungsvorschrift es
auswählt. Der größere Rest ist keine physikalische Rangliste für A und
keine nachträgliche Begründung, doch lieber den anderen Wert zu wählen.

Die Begrenzung bleibt wesentlich: Externzone und Koeffizienten werden
im Buch über Näherungsansätze gewonnen. Unsere exakt untersuchte
Skalarrelation ist nicht automatisch ein exaktes Feldgesetz. Eine
begründete diskrete Projektion oder eine quantitative Resttoleranz ist
mit diesem Rechenschritt weder nachgewiesen noch widerlegt. Insbesondere
wurde aus dem Rest kein empirisches Fehlerbudget oder Massenfehler gemacht.

## 5. Nachvollziehbarkeit und Weiterarbeit

Der [Vorvertrag](../00_admin/SATURATION_PLAN.md) wurde mit `fa25c42`
vor der neuen numerischen Auswertung gesichert. Der neue
[Input](../04_reconstruction/alpha_audit/saturation_inputs.json) trägt
den kanonischen SHA256
`902f775de16e96628825c7ebab93881e58cae1a334f2f1a4710b7528eec98f98`.
Die alten Eingaben, Rechner, Snapshots und 49 Normalisierungs-CSV-Zeilen
bleiben unverändert. Ein neuer [Diagnoseaufsatz](../scripts/audit_saturation.py)
und [11 Tests](../tests/test_saturation.py) prüfen die eng begrenzte Fortsetzung.

Root las H004 Druck 321-323, 328-330 und 340-342 vollständig visuell;
Details und Zuschreibung im [Quellenumfang](../03_notes/SATURATION_SOURCES_2026-09-07.md).
Interne Gegenprüfungen:
[Quelle](../04_reconstruction/alpha_audit/reviews/SATURATION_SOURCE_REVIEW_2026-09-07.md),
[Vertrag/Algebra](../04_reconstruction/alpha_audit/reviews/SATURATION_CONTRACT_REVIEW_2026-09-07.md),
[Numerik](../04_reconstruction/alpha_audit/reviews/SATURATION_NUMERICS_REVIEW_2026-09-07.md).
Diese ersetzen kein externes Peer Review.

Die Numerikreview nutzt ihre eigene Machin-/Taylor-/Fraction-Kette aus
Etappe 35, ohne Import unseres Rechners. Root führte den dort per Hash
gebundenen Vorblock und den neuen Anschlussblock erneut aus: 42 neue
Decimal-Felder bei 120/160 Stellen und 14 rationale Rest-/Sigma-Hüllen
bestanden. Die Feldzahlen zählen teilweise abhängige Größen, keine
unabhängigen Experimente. Die separate Codegegenprüfung fand keinen
materiellen Fehler; Quelle und Schlussfolgerungen wurden gegengelesen.

```powershell
py -3.13 -B scripts/audit_saturation.py --check --verify-sources
py -3.13 -B -m unittest discover -s tests -q
py -3.13 -B scripts/validate_finding_register.py
```

Abschlussprüfungen: 342 Tests bestanden, darunter 11 neue. Alle zwölf
alten Snapshotchecks und vier bisherigen Zertifikatschecks (gekoppelte
Existenz, Externtransport, xi-Rekurrenz, A-Sensitivität) bestanden ebenfalls;
neuer Sättigungscheck, H004-Hash und Registermetadaten sind geprüft.

FIND-046 führt diese eigene Anschlussdiagnose. 46 Befundgruppen sind
keine 46 unabhängigen Fehler. Der nächste begrenzte Auftrag ist eine
Quellenbilanz zum Status von (108) gegenüber der anschließenden diskreten
Auswahl: Gibt es eine ausdrücklich begründete Projektions- oder Restregel?
Keine neue A-/Y-/Massenwahl und keine Zuschreibung unbelegter Autorenabsichten.
