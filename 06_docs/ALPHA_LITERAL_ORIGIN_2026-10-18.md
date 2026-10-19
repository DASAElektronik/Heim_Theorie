# Der frühe Beleg für die fest eingetragenen Kopplungswerte

2026-10-18, Etappe44, Ausgang2802434.
[Vertrag](../00_admin/ALPHA_LITERAL_ORIGIN_PLAN.md),
[Quellenumfang](../03_notes/ALPHA_LITERAL_ORIGIN_SOURCES_2026-10-18.md).

## Ergebnis

Die beiden H015-Programmvorgaben alpha^-1=137.03602725 und
beta^-1=1.00001411 stehen bereits wörtlich auf Seite6 von H011,
*Magnetfeld und Drehimpulsdichte*. Der Scan trägt auf Seite20 das Datum
21.12.1981. Dort werden die Zahlen als Ergebnisse einer theoretischen
Kopplungsgleichung angegeben, nicht als bloß übernommene Messwerte.

Damit ist ein konkreter früher Quellenvorläufer gefunden. Die bisher
offene Zahlenprovenienz ist enger eingegrenzt. Ein direkter Nachweis,
dass genau dieses Manuskript bei der Programmübertragung benutzt wurde,
liegt damit noch nicht vor. Das Manuskriptdatum ist keine forensische
Authentifizierung und die heutige Host-Dateibezeichnung keine alte Signatur.

Die Herkunftsaussage ist von der mathematischen Richtigkeit zu trennen:
**Das gedruckte Alpha-/Beta-Paar kann nicht aus derselben angegebenen
quadratischen Gleichung stammen.** Dieser interne Befund benötigt weder
moderne Messdaten noch eine Entscheidung über die eta-Definition.

## 1. Was sich gegenüber der späteren Buchfassung ändert

Beide Fassungen verwenden eine Gleichung der Form

```text
a*sqrt(1-a²) = [9*theta/(2*pi)^5]*(1-A1*A2*Y).
```

Die Koeffizienten sind jedoch verschieden. Mit z=eta_(1k):

| Quelle | Gedruckte Definition, nach A_k aufgelöst |
|---|---|
| H011 Seite4/5, (A) | (1-sqrt(z))/(z*(1+sqrt(z))) |
| H004 Druck302, (105) | sqrt(z)*(1-sqrt(z))/(1+sqrt(z)) |

Ihr Verhältnis ist z^(-3/2), nicht1. Die H011-Form passt zur dortigen
vorgeschalteten eta11*eta12*A-Gleichung. Eine bloße Gleichsetzung mit der
späteren Buchdefinition würde die Quelle verändern. Die historische
Begründung des Fassungswechsels ist hier nicht geklärt.

H011 Seite5 erwägt A=4C wegen einer frei verfügbaren Integrationskonstante
und führtY als Unsicherheitsfaktor ein; Seite6 setztY=1. Dies ist ein
belegter Rechenansatz, keine neu bewiesene physikalische Notwendigkeit.

## 2. Bedingte Vorwärtsrechnung

Die eta-Familie wird ausdrücklich über das bereits bekannte Schema
eta(q,k)=pi/[pi^4+(4+k)q^4]^(1/4) angeschlossen, hier q=1,k=1,2.
H011 nennt die beiden k-Werte und verweist auf(98); die vollständige
historische Grundtextfassung wird dadurch nicht ersetzt.

Mit der H011-Definition undY=1 ergibt die eigene Rechnung:

| pi-Profil | 1/kleiner Zweig | 1/großer Zweig |
|---|---:|---:|
| Mathematisches pi | 137.0360274220375 | 1.000026626729685 |
| H015-Literal3.1415926535 | 137.0360274025686 | 1.000026626729692 |
| H011 gedruckt / H015 fest eingetragen | 137.03602725 | 1.00001411 |

Der kleine Zweig liegt nahe beim frühen Druckwert, trifft ihn aber nicht
innerhalb einer halben letzten gedruckten Stelle: die Differenz beträgt
etwa17.20 bzw.15.26 Einheiten von1e-8. Auch hier keine exakte Reproduktion
behaupten. Historische Zwischenrundung oder ein weiterer Eingabestand
könnten untersucht werden, sind durch die Nähe allein aber nicht belegt.

Der neue Ergebnisdatensatz enthält außerdem alle vorab festgelegten
Vergleiche: unberichtigtes29a-R, unberichtigte quadratische Gleichung und
beide bereits geführten1982-Indexlesarten, jeweils mit beiden pi-Profilen.
Keiner trifft137.03602725 innerhalb der angenommenen Druckrundung.
Es wurde keinY nachgerechnet, um eine passende Zahl zu erzwingen.

## 3. Der stärkere, von dieser Brücke unabhängige Test

Für zwei verschiedene positive Lösungen a,b derselben Gleichung
a*sqrt(1-a²)=R gilt nach t=a²:

```text
t²-t+R²=0, also a²+b²=1.
```

Die gedruckten Kehrwerte137.03602725 und1.00001411 ergeben dagegen

```text
a²+b² = 1.000025031929895...
```

Selbst wenn beide gedruckten Kehrwerte um eine halbe letzte Stelle
variieren, liegt die Summe im Bereich
[1.000025021930314...,1.000025041929476...]. Die Grenzen sind im
Rechner als rationale Zahlen exakt berechnet;1 liegt sicher außerhalb.

Zum gedruckten kleinen Zweig würde als komplementärer großer Zweig
der Kehrwert1.000026626729751... gehören. Eine gemeinsame Änderung vonY
oder der rechten Seite kann die notwendige Summenidentität nicht ändern.
Das ist derselbe mathematische Fehlertyp wie in FIND-001, nun an einer
früher datierten konkreten Quelle. Keine neue unabhängige Fehlerzählung.

## 4. Bedeutung für die erfolgreiche Elektronenrechnung

Der H015-Initialisierungsblock weist die gedruckten Zahlen direkt zu und
löst(A) nicht. Die Herkunft als behauptetes Theorieergebnis ist nun
belegt; die Richtigkeit dieses Anspruchs bleibt eine eigene Prüfung.
Man darf deshalb weder pauschal von unbekannten Messwertkopien noch von
erfolgreich aus(A) hergeleiteten Programmkonstanten sprechen.

Die positive Elektronenreproduktion aus Etappe42 bleibt unverändert.
In diesem speziellen N0-Massenzweig fälltBETA nach regulärer Reduktion
weg. Deshalb prüft ein passender Elektronenwert die behauptete gemeinsame
Alpha-/Beta-Herleitung gerade nicht. Eine Reparatur der Kopplungsgleichung
oder der Theorie folgt aus dem Massentreffer nicht.

## 5. Entscheidung am Verzweigungspunkt

Die Suche nach einem frühen Zahlenbeleg war erfolgreich. Offen bleiben
die tatsächlichen Zwischenrechnungen und die Begründung der veränderten
A_k-Definition. Weitere frei gewählte Präzisions-/Y-/Indexversuche wären
ohne neue Quelle nicht geeignet, die historische Entstehung festzustellen.
Diese numerische Herkunftsspur wird deshalb an dieser Grenze geparkt.

Die nächste sachlich getrennte Spur ist die ursprüngliche F_S-/Massen-
Kalibrierung: Welche Daten und Funktionen waren vor einer behaupteten
Vorhersage bereits eingesetzt? Nur anhand dieser Herkunft lässt sich ein
unabhängiger Folgetest auswählen. Die bisherigen Resultate werden dabei
erhalten, nicht auf einen früheren Git-Stand zurückgesetzt.

## Reproduktion

[Rechner](../scripts/audit_alpha_literal_origin.py),
[Ergebnisse](../05_analysis/alpha_literal_origin_results.json),
[Tests](../tests/test_alpha_literal_origin.py).
`py -3.13 -B scripts/audit_alpha_literal_origin.py --check`.
Vier neue Tests,373 insgesamt bestanden.80/110-Stellenvergleich stabil;
unabhängige inverse-quadratische binary64-Rechnung und exakte rationale
Paargrenzen. H011-Hash bestätigt;53 Altbefunde und alle alten Profile erhalten.
FIND-054 ist Quellen-/Versionsfortschritt mit eigener Diagnose, kein
externes Peer Review oder empirisches Gesamturteil.
