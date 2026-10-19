# Die Neutrinotabelle passt zur allgemeinen Formel

2026-10-18, Einheit 53. Ausgang `d8fc5fa`.
[Vorab festgelegter Prüfvertrag](../00_admin/NEUTRINO_TABLE_PLAN.md).

Der in52 gefundene Faktor lässt sich anhand der gedruckten Tabelle
weiter eingrenzen: Die aus111 folgende Relation trifft den pi-Wert
innerhalb seiner Druckrundung. Die aus118b folgende Relation verfehlt
ihn deutlich. Das spricht für einen fehlenden Faktor2 im nichtkonstanten
pi-Term von118b. Es beweist weder die damalige Programmausführung noch
eine unabhängige Vorhersage, denn zwei Tabellenwerte gehen als Inputs ein.

## Quellen und feste Zuordnung

H004 Druck275/PDF281 und Druck376/PDF381 erneut vollständig visuell
gelesen. Auf275 ist `2*xi=1+sqrt(5)` ausdrücklich angegeben. Im Anhang
stehen beta=4,006eV, nu(e0)=5,375675keV und pi=1,441793keV.
Wir rechnen einheitlich in eV. Die Druckwerte R=2,003 und P=2,03 bleiben
unverändert; sie werden nicht benutzt, um beta nachträglich zu reparieren.

Zuordnungsannahme: Die Tabellenzeile nu(e0) bezeichnet den neutralen
e-Feldzustand aus352/118b. Dies ist keine Gleichsetzung mit einer heutigen
experimentellen Flavourmasse. Die Formeln111/118a/118b und drei Zustände
wurden in [52](NEUTRINO_BOOK_ALGEBRA_2026-10-18.md) geprüft.
Quellendatei/Hash bleiben wie in [51](NEUTRINO_BOOK_2026-10-18.md).

## Warum keine Massenskala angepasst werden muss

Mit S=mu*alpha_plus und C=4*A_v*(3-alpha)*sqrt(eta11) folgt:

```text
m_beta = S*2*B_v
m_e_field - m_beta = S*C
m_pi = m_beta + a*(m_e_field-m_beta)/(1+4*xi)
```

Die beiden vorab festgelegten Alternativen sind a=1 für118b und a=2
für111. S, A_v, B_v, alpha und eta11 müssen nicht neu berechnet oder
gewählt werden. xi ist quellenfest, kein Fitparameter. Die historische
Konstantenkalibrierung bleibt daher offen, ohne diesen Vergleich zu blockieren.

| Feste Alternative | Relationswert aus Tabellenmitten in eV | Rundungshülle in eV | Vereinbar mit gedrucktem pi-Wert? |
|---|---:|---|---|
| 118b, a=1 | 722,899370296058 | [722,898870296058;722,899870296058] | Nein |
| 111, a=2 | 1441,792740592116 | [1441,792240592116;1441,793240592116] | Ja |
| Gedrucktes pi | 1441,793 | [1441,7925;1441,7935] | Referenz |

Die Hüllen sind keine experimentellen Unsicherheiten. Primärannahme ist
Rundung auf die nächste letzte Druckstelle: alle drei verwendeten Werte
haben nach der Einheitenumrechnung eine halbe letzte Einheit von0,0005eV.
Auch die vorab bezeichnete breitere Hülle ±0,001eV ändert die Auswahl
zwischen den zwei Alternativen nicht. Kein Profil wurde nach dem Ergebnis
ausgetauscht. Die Tabellenmitte der111-Relation rundet bereits zu1441,793eV.

## Reproduzierbarkeit

[Rechner](../scripts/audit_neutrino_table.py) und
[exakte Ergebnisse](../05_analysis/neutrino_table_results.json):
`py -3.13 scripts/audit_neutrino_table.py --check`.

Die Einschließung von sqrt5 erfolgt durch eine Integerwurzel und exakte
rationale Schranken. Deren Quadrate zertifizieren die Lage, ohne sich auf
eine Gleitkomma-Rundung zu verlassen. Die Ausgabe enthält die rationalen
Intervallenden; die Dezimalzahlen oben sind gerundete Anzeigen. Monotonie
in den drei Eingaben liefert die Intervallgrenzen. Vier Tests prüfen die
xi-Schranken, sämtliche Eckpunkte, die beiden Rundungsentscheidungen und
das Herausfallen einer beliebigen gemeinsamen Skala.

FIND-059 ist eine positive Reproduktion dieser Tabellenrelation und eine
Präzisierung von FIND-058, keine weitere unabhängige Fehlerzählung.
Gesamter Teststand:389 erfolgreich. Die bisherigen Ergebnisse bleiben erhalten.

## Was daraus folgt

Eine korrigierte Lesart von118b mit8 statt4 ist durch111 und die Tabelle
gestützt. Wir führen sie als begründete Korrekturhypothese; das Original
und die gedruckte Variante bleiben dokumentiert. Ein beliebiger anderer
Fehler könnte theoretisch kompensieren, daher wird kein historischer
Rechenpfad allein aus der Zahlenübereinstimmung behauptet.

Eine absolute Neutrino-Massenreproduktion benötigt weiterhin den passenden
Konstantenvertrag. Ein experimenteller Test benötigt zusätzlich die
Messgrößenzuordnung aus49/51. Ohne neue Quellen hierfür liefert weiteres
Variieren derselben Tabellenrelation keinen Erkenntnisgewinn.
