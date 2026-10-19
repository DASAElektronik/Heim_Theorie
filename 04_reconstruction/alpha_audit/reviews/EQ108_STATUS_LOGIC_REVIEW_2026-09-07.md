# (108): Gleichungsstatus, Näherung und diskrete Auswahl

2026-09-07, Etappe 37. Unabhängige interne Logikabgrenzung; kein neuer
Fehlerbefund, keine neue Numerik und kein Urteil über die gesamte Theorie.

## 1. Grundlage und Zuschreibung

Vollständig gegengelesen wurden die bestehenden Berichte
[Buchauswahl](../../../06_docs/BOOK_SELECTION_2026-09-06.md),
[Externnäherung](../../../06_docs/EXTERNAL_APPROXIMATION_2026-09-06.md) und
[Sättigung](../../../06_docs/SATURATION_2026-09-07.md).
Die Quellenangaben darin werden übernommen, nicht hier erneut visuell geprüft.
Ergänzend gelesen: der Abschnitt zur Vorwärtsrichtung in
[BOOK_SELECTION_SOURCE_REVIEW](BOOK_SELECTION_SOURCE_REVIEW_2026-09-06.md)
und die dort ausdrücklich ausgesparte empirische Bestimmung von `F_S`.
Die Angabe `delta F_S=0` auf H004 Druck 323 wird zunächst als vom
Hauptagenten übermittelte Quellenprämisse behandelt. Die lokale Aussage
darüber gilt unter der unten ausdrücklich angegebenen Variationsrichtung.

## 2. Drei verschiedene Prüfgegenstände

| Ebene | Präzise Frage | Reichweite des vorhandenen Nachweises |
|---|---|---|
| Quellenansatz | Welche Relation wird aus welchen Ansätzen, Grenzwerten und Normierungen gewonnen? | Die skalare Form von (108) ist rekonstruiert; dadurch ist sie noch kein exakt gültiges metronisches oder physikalisches Feldgesetz. |
| Näherungsgüte | Wie nahe liegt diese skalare Beschreibung am bezeichneten Gegenstand, auf welcher Menge und in welcher Norm? | Dafür braucht es eine quantitative, zur konkreten Anwendung passende Fehlerkontrolle. Ein einzelner algebraischer Rest liefert sie nicht. |
| Algorithmuserhaltung | Erfüllt die diskrete Ausgabe dieselbe feste skalare Relation exakt? | Hier lässt sich `R=0` prüfen oder `R!=0` zertifizieren, ohne die physikalische Güte der Näherung bereits zu entscheiden. |

Eine aus Näherungsansätzen gewonnene Gleichung kann innerhalb des daraus
gebildeten Modells exakt auferlegt werden. Die angenäherte Herkunft
macht einen internen Gleichungsrest nicht automatisch bedeutungslos.
Umgekehrt ist eine gedruckte Gleichheit allein kein Beweis dafür, dass
jedes spätere diskrete Auswahlverfahren sie erhalten soll oder erhält.
Das ist eine zusätzliche Quellen- und Verfahrensfrage.

## 3. Was ein nicht verschwindender Rest genau besagt

Im festen N=0-Vertrag sei, mit unveränderten Koeffizienten und Eingaben,

```text
T_A(N) = a1*N1^3 + a2*N2^2 + a3*N3 + exp(-A*N4),
W_A = w*(27*a1 + 9*a2 + 2*a3 + exp(-A)),
R_A(N) = T_A(N) - W_A.
```

Hier bezeichnet `T_A` die dimensionslose Hilfssumme, keine Lebensdauer.
Die Resonanzordnung N=0 ist außerdem nicht das leere Besetzungstupel.

Ein zertifiziertes `R_A(N_out)!=0` beweist: **Diese Ausgabe löst diese
unveränderte skalare Gleichung nicht exakt.** Ein Gegenbeispiel reicht,
um die universale Zusatzbehauptung zu verwerfen, dass das betreffende
Verfahren sie bei allen zugelassenen Eingaben exakt löse. Nötig bleiben
dabei die ausdrücklich benannten Eingabe-, Zweig- und Zulassungsannahmen.

Daraus folgt für sich genommen weder das Fehlen jedes anderen Tupels
noch die Unmöglichkeit eines anderen Modells, eines begründeten
Näherungsverfahrens oder einer physikalischen Realisierung. Ebenso wenig
folgen ein Massenfehler, dessen experimentelle Größe oder eine Rangliste
der A-Werte. Ein globaler Ausschluss ist ein separater Bereichsbeweis.

Die vorhandenen lokalen Algebraresultate sind damit vereinbar:

- Beim gewöhnlichen Abschneiden von `x=-ln(r)/A` auf `j=floor(x)` ist
  `R=exp(-A*j)-r>=0`; exakt null ist er nur bei ganzzahligem x.
- Im untersuchten Sättigungsfall führt die übertragene Kappenregel zu
  `N4=0`, daher `R=1-r>0`. Die direkten geprüften Strukturgates können
  zugleich bestehen. Das ist kein vollständiger physikalischer Zulassungsbeweis.
- Die Transferdiagnose aus Etappe 29 betrifft wiederum ihren eigenen
  festgehaltenen Restvertrag. Sie ist keine vollständige Rekonstruktion
  aller mehrschrittigen Quellenregeln.

Die Übertragung der Sättigung auf A=1/5 bleibt eine eigene bedingte
Diagnose, keine im Buch publizierte A=1/5-Auswertung.

Insbesondere gilt die globale Untergrenze aus Etappe 32 nur auf ihrer
gate-admissiblen Menge D. Die gewöhnliche Ausgabe mit negativem direktem
`beta3` gehört nicht zu D. Ihr kleinerer Rest widerlegt die globale
Untergrenze deshalb nicht. Strukturgates und Gleichungsrest sind zwei
getrennte Prüfungen, nicht gegeneinander austauschbare Kriterien.

## 4. Welche zusätzlichen Verträge die Beurteilung ändern würden

Die folgenden Möglichkeiten sind logische Alternativen, keine hier
belegten Quellenregeln und keine Vorschläge zur nachträglichen Anpassung.

| Zusätzlicher Vertrag | Was zusätzlich festzulegen oder zu beweisen wäre |
|---|---|
| Zulässiger Rest `R in J` | Unabhängige Herkunft, Vorzeichen, Skala/Norm, Parameter- und Zustandsbereich des Intervalls J; ferner die Beziehung zum physikalisch angenäherten Gegenstand. Ein nach Besichtigung von R gewähltes J erklärt R nicht. |
| Diskrete Projektion | Welches kontinuierliche Objekt auf welche diskrete Menge abgebildet wird, welche Gates und Zielgröße gelten, wie Mehrdeutigkeit behandelt wird und welche Restgarantie besteht. Ferner: Ist (108) Vorstufe oder auch Bedingung nach der Projektion? |
| Geändertes W oder geänderte Koeffizienten | Eine unabhängige Änderungsregel samt Eingaberolle, Referenznormalisierung und erneuter Konsistenzprüfung. Das ist ein anderer Vertrag, keine exakte Lösung der unveränderten Rechnung. |

Eine Abschneide- oder Kappenregel definiert bereits einen Auswahlschritt;
das beweist weder dessen Erhaltung von (108) noch eine metrische
Projektions- oder physikalische Fehlergarantie. Die exakte Rücksetzung
`W_neu=T_A(N_out)` würde die Gleichheit algebraisch herstellen, wäre ohne
zusätzliche Begründung aber lediglich eine Änderung der zuvor festen
rechten Seite. Wegen `W=g*w` ist sie nicht unabhängig von deren Aufbau.
Hier wird keine solche Rücksetzung vorgenommen.

Auch eine korrigierte Externfunktion muss beidseitig konsistent behandelt
werden. Unter dem in Etappe 33 deklarierten unveränderten Vertrag gilt
für rohe Korrektur h und den dortigen A=1/3-Fall

```text
R_neu - R_alt = h(N4) - w*h(1) + (w-1)*h(0).
```

Gleiche Argumente sind derselbe Funktionswert; ein konstanter roher
Offset hebt sich auf. Nur links einen Rest zu addieren untersuchte
einen anderen Vertrag. Das ist keine Herleitung einer erlaubten h-Funktion.

Liegt auf D ein alter Abstand `|R_alt|>=L` vor, reicht ein **uniformes**
Fehlerbudget `|R_neu-R_alt|<=E<L` zur Erhaltung des Ausschlusses.
Ein tatsächlicher neuer Nullpunkt erfordert dagegen
`R_neu-R_alt=-R_alt`. Die notwendige Größe `>=L` allein ist nicht
hinreichend; auch eine äußere Hülle mit `E>=L` beweist keinen Nullpunkt.
Eine alte energieabhängige endliche Suchgrenze darf für eine geänderte
Relation nicht ohne erneuten Bereichsnachweis übernommen werden.

## 5. Kann F_S den Rest durch eine Massenanpassung beseitigen?

Seien s die festgehaltenen äußeren Zustandsparameter und n die Besetzungen,
in deren Richtung die betreffende Differenzoperation wirkt. Wird `F_S(s)`
in dieser Operation als besetzungsunabhängiger additiver Beitrag behandelt,
gilt schlicht `delta_n F_S(s)=0`. Das behauptet weder `F_S=0` noch eine
globale Konstanz über verschiedene s. Es ist keine Verwechslung mit
`F_im`, `F16` oder der Resonanzfunktion f.

Unter dieser Prämisse kann eine Änderung von `F_S(s)` absolute Massenwerte
ändern, nicht aber die betreffende Massendifferenz und die daraus
gebildete feste skalare (108). Eine nach gemessenen Massen bestimmte
additive Konstante beseitigt also den hier geprüften Rest nicht.
Ein verbesserter Massentabellenwert wäre kein Nachweis des Gleichungserhalts.

Dies verbietet empirische Kalibrierung nicht generell. Sie wäre als solche
zu deklarieren und nicht als unabhängige Vorhersage derselben Massenwerte
zu zählen. Als Reparatur von (108) ist sie unter der genannten
Differenzprämisse schlicht unwirksam.

Falls F_S doch mit n variiert, die Operation auch s verändert oder eine
Anpassung zugleich `a_j`, `g`, `w` beziehungsweise die Normierung ändert,
gilt das einfache Aufhebungsargument nicht unverändert. Dann müssten
diese Abhängigkeiten und die Ableitung von (108) neu nachgewiesen werden;
sie dürfen nicht stillschweigend hinzugenommen werden. Eine entsprechende
Rückkopplung wird mit diesem Review weder behauptet noch ausgeschlossen.

## 6. Minimales Fazit

Der gesicherte Befund heißt: **kein exakter Gleichungserhalt im bezeichneten
festen skalaren Auswahlvertrag**, nicht „alle Näherungen sind widerlegt“.
Ein öffentliches Fazit muss Herkunft der Relation, tatsächliche
Auswahlvorschrift, geprüfte Zustandsmenge und etwaige Restgarantie getrennt
benennen. Die offene Quelle einer Projektions- oder Fehlerregel bleibt
offen; logisch denkbare Zusätze ersetzen sie nicht.

Keine neue Zahl, kein neuer Test und kein neuer Korrekturterm wurden
eingeführt. Dieses Review ordnet vorhandene Belege ein und zählt sie
nicht als weiteren unabhängigen Fehler.
