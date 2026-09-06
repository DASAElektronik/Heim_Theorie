# Was wir nach Etappe 23 von Heims Ansatz verstehen

Stand: 2026-09-06, Etappe 24. Ausgang `660d612`, Plancheckpoint `7d60d4b`.
Diese Bilanz aktualisiert die [Etappe-15-Bilanz](UNDERSTANDING_BALANCE_2026-09-06.md).
Sie betrifft den untersuchten Alpha-/Konfigurations-/Massenformel-Ausschnitt,
nicht das Gesamtwerk. Synthese vorhandener Nachweise und unveraenderter
Rechner; keine neue PDF-Lesung, Herleitungsrechnung oder empirische Bewertung.

Nachtrag Etappe 25: Die [K4/W4-Fallpruefung](K4_W4_SELECTION_2026-09-06.md)
ist abgeschlossen. Die exaktloesende Interpretation traegt nicht allgemein
unter den festgelegten positiven Eingaben; Zaehldeutung, reale Erreichbarkeit
und Teilchenmassen bleiben davon getrennt. FIND-035 ergaenzt das Register;
die folgende Bilanz mit 34 Gruppen dokumentiert weiterhin Etappe 24.

## 1. Ergebnis in einfachen Worten

Ein festgelegter Elektron-Grundzustandsfall ist inzwischen nachvollziehbar
berechenbar. Zwei zuvor unklare Programmterme sind auch im Buch
und in einem fotografierten FORTRAN-Listing belegt. Auch eine auffaellige
Exponentenabweichung laesst sich heute auf eine konkrete Wiedergabe
eingrenzen, statt sie pauschal Heim zuzuschreiben.

Damit verstehen wir mehr vom Rechenweg und von seinen Voraussetzungen.
Noch nicht erreicht ist eine vollstaendige physikalische Herleitung, die
ohne empirische Koeffizientenwahl und offene Zustands-/Operatorzuordnungen
eindeutige Teilcheneigenschaften vorhersagt. Eine Zahlenreproduktion ersetzt
diese Herleitung nicht; eine offene Herleitung ist ihrerseits kein Beweis,
dass jede daraus verwendete Endformel falsch ist.

Unser naechster Auftrag ist deshalb die **K4/W4-Ganzzahlauswahl** in H006:
Bewahren die gedruckten Sonderfall- und Ganzzahlregeln die Auswahlgleichung,
oder beschreiben sie eine Naeherungs-/Auswahlvorschrift mit zu bestimmendem
Rest? Diese Frage bleibt in dieser Bilanz ausdruecklich unbeantwortet.

## 2. Fuenf verschiedene Nachweisebenen

| Ebene | Was sie leisten muss | Erreichter Stand und Grenze |
| --- | --- | --- |
| Quelleninhalt | Formel, Begriffe, Fassung und genaue Stelle belegen | Viele lokale Definitionen und Parallelstellen gefunden; Ueberlieferung und einzelne Glyphen bleiben offen |
| Rekonstruktion | Lesart, Indizes, Definitionsbereich und Zusatzannahmen festlegen | Explizite Profile vorhanden; eine gewaehlt-normalisierte Lesart ist keine bewiesene Autorenabsicht |
| Rechnung | Aus diesen Eingaben nachvollziehbar dasselbe Ergebnis erhalten | Enger H006-N0-Fall und H010-Ausgabevergleich reproduzierbar; keine allgemeine Zustandsauswahl |
| Physikalische Herleitung | Ansatz, Koeffizienten, Operatoren und beobachtbares Objekt begruenden | Mehrere Motive und Teilbruecken rekonstruiert; wesentliche Begruendungen und Pfade offen |
| Empirische Pruefung | Vorab festgelegte Vorhersagen von Kalibrierungsdaten trennen und mit passenden Beobachtungen vergleichen | Umfassende Bewertung bewusst noch nicht durchgefuehrt |

Die 49 alten CSV-Normalisierungen bleiben unveraendert (47 `resolved`,
2 `blocked`). `resolved` bedeutet dort eine dokumentierte Lesentscheidung,
nicht, dass die Formel mathematisch konsistent, physikalisch hergeleitet
oder empirisch bestaetigt ist. Ebenso sichern Softwaretests bestimmte
Rechen-/Metadateneigenschaften, nicht die Wahrheit der Theorie.

## 3. Was die letzten acht Etappen beigetragen haben

| Etappe / vorhandener Nachweis | Positiver Anschluss | Was damit nicht geschlossen ist |
| --- | --- | --- |
| 16: [H006-N0-Fall](N0_ELECTRON_2026-09-06.md) | Die vorgegebene e--Komponente des x2-Multipletts liefert ueber `W=g*w`, `w=1` und die Auswahlregel bedingt `n=(0,0,0,0)`; `K4=1` ist im gruppierten (XV)/(XXVI)-N0-Pfad analytisch abgesichert | `(0110)` ist keine Besetzung; weder die Konfiguration selbst noch eine allgemeine Auswahl oder physikalische Elektronenidentifikation wird so hergeleitet |
| 17: [Historischer N0-Vergleich](HISTORICAL_N0_2026-09-06.md) | H006/H010-Unterschiede in Formel und Eingaben getrennt; archivierter H010-Ausgabewert im deklarierten Profil reproduziert | Keine historische Compilerwiederholung, keine Gleichheit aller Programmzweige und kein unabhaengiger Massentest |
| 18: [alpha3-Herkunft](ALPHA3_ORIGIN_2026-09-06.md) | H004(98c) und H015-Listing tragen die beiden charakteristischen H010-Terme; Schlussalgebra nachvollzogen | Fruehere Quellenanschluesse der Form sind belegt, nicht ihr Erstursprung, lueckenloser Ueberlieferungsweg oder eine parameterfreie Begruendung der empirisch gewaehlten A/B-Koeffizienten |
| 19: [alpha3-Annahmen](ALPHA3_ASSUMPTIONS_2026-09-06.md) | Ausdrueckliche Voraussetzungen und lokale Gegenvarianten getrennt; `C_k=2^(k-2)` folgt bedingt aus der gewaehlten Sigma-Zuordnung | Kein Nachweis von sieben unabhaengigen globalen Fitparametern, kein vollstaendiger alternativer Heim-Zustand |
| 20: [Metronische Integration](METRONIC_INTEGRATION_2026-09-06.md) | M2/M2a erklaeren die inklusive Endpunktregel und `lnY=ln[X(z+1)/X(z-1)]`; vier Potentialquotienten bedingt angeschlossen | Grosser Fibonacci-Index macht den unskalierten relativen X-Schritt nicht klein; der isolierte Logrest ist kein berechneter Massenfehler |
| 21: [Metronischer Schritt](METRONIC_STEP_2026-09-06.md) | M7 enthaelt tatsaechlich den inneren Argumentshift; skalierte Differenz und nichtlinearer innerer Shift sind unter den geprueften Annahmen unterschieden | Gemeinsames Gitter und reale H/G-/Potentialschritte fehlen; eigene endliche Rekurrenz und log-additives Modell sind keine belegte Reparatur |
| 22: [Potentialpfade](POTENTIAL_PATHS_2026-09-06.md) | Vier gekoppelte Komponenten und getrennte, teils gewichtete Quellenkanaele identifiziert | Nur unsere Zusatzlesart einer gemeinsamen unveraenderten Rohkomponentenkurve ist ausgeschlossen; Zwischenpfade und Gesamtfehler bleiben offen |
| 23: [Historische Exponenten](HISTORICAL_EXPONENTS_2026-09-06.md) | H015-Typoskript und H006-Nachbarstellen tragen den gruppierten Exponenten und seine Logumkehrung; nur H006(XIV) weicht in der geprueften Kette ab | Kein Nachweis der Fehlerentstehung, eines autorisierten Erratums oder einer vollstaendigen authentifizierten Urschrift |

Die starke Aussage lautet jeweils: *Dieser benannte Anschluss ist unter
diesen Voraussetzungen nachvollzogen.* Weder die alten H006-Zahlen noch
die H010-Zahlen werden wegen besserer Naehe zu einer Sollmasse ersetzt.

## 4. Welche Fassungen zusammenpassen -- und wie weit

Die [Fassungsreview](../04_reconstruction/alpha_audit/reviews/BALANCE24_VERSIONS_REVIEW_2026-09-06.md)
trennt H006, H010, H015-Listing, H015-Typoskript, H004 und die spaetere
logarithmische N3-Familie. Ihre wichtigsten Grenzen:

- H006 und H010 sind am festgelegten N0-Knoten in mehreren Rechenbloecken
  algebraisch anschliessbar, besitzen aber zwei aktive alpha3-Unterschiede
  und unterschiedliche Eingabeprofile. H006s Radikandweite bleibt offen.
- H004(98c), H010 und H015-Listing stimmen in den zwei untersuchten
  alpha3-Termformen ueberein. Das vereinheitlicht weder Programme noch
  Konstanten, Rundung oder Auswahlregeln.
- H015-Listing und H015-Typoskript sind verschiedene Belegarten in derselben
  heutigen PDF. Sichtbare historische Datumsangaben sind keine
  forensische Authentifizierung; Digitalisierungsdaten sind keine Werkdaten.
- H007/H013/H014 verbinden ihre logarithmische `N3`-Form mit `2*alpha3=N3`.
  Dies erklaert nicht rueckwirkend die alte H006/H004/H010-Formel und
  begruendet keine Chronologie der undatierten Manuskripte.

Es liegt keine vollstaendige gemeinsame "1982-Fassung" vor. Auch die
Symbole sind rollengebunden: nacktes `alpha`, Strukturkoeffizient `alpha3`
und Massenfaktoren `alpha+/-` sind unterschiedliche Groessen. Ebenso sind
H/G-Korrekturfunktionen der Buchableitung nicht automatisch die gleichnamigen
Hilfsterme der Massenrechnung.

## 5. Welche frueheren Kurzurteile ueberholt sind

Die historischen Berichte bleiben als Verlauf erhalten. Als heutiges Fazit
waeren folgende Aussagen falsch oder zu stark:

- **"Die nu/x-Bruecke und Besetzung fehlen auch im Elektron-N0-Fall."**
  Unsere eigene v/nu-Fehllesung wurde korrigiert; der enge Basisfall ist
  geschlossen. Das behauptet keine allgemeine Loesung der Auswahlregel.
- **"Die H010-alpha3-Terme haben keinen belegten frueheren Quellenanschluss."** Buch und
  fotografiertes Listing tragen die Form. Offen bleibt deren physikalische
  Bestimmtheit und das genaue empirische Anpassungsverfahren.
- **"Das z-1 in lnY ist ein Fehler" oder "M7 besitzt keinen inneren Shift".**
  Die Endpunktregel bzw. der gedruckte Ausdruck erklaeren beides. Die
  Genauigkeit und gemeinsame Anwendung der Operatoren bleiben eigene Fragen.
- **"Alle Potentiale laufen laut Heim auf derselben Rohkurve."** Gerade
  diese zusaetzliche Identifikation ist nicht quellenbelegt. Die Quelle
  verwendet getrennte, teils gewichtete Kanaele.
- **"FIND-027 beweist einen Fehler in Heims urspruenglicher Formel."**
  Belegt bleibt die lokale H006-Abweichung; das gepruefte H015-Typoskript
  enthaelt sie nicht. Die konkrete Uebertragungsursache ist offen.

Alle 34 Registergruppen sind in der [Befundreview](../04_reconstruction/alpha_audit/reviews/BALANCE24_FINDINGS_REVIEW_2026-09-06.md)
genau einmal eingeordnet. Sie umfassen positive Rekonstruktionen,
Versionsunterschiede, offene Begruendungen und lokale bzw. bedingte
Konflikte. Sie sind weder 34 Fehler noch 34 unabhaengige Experimente.
Diese Synthese fuegt keine Befund-ID hinzu und aendert das Register nicht.

Fortbestehende groessere Luecken sind insbesondere der H-Wellen-/
Normierungsabschluss, die konkrete eta22-Alpha-Korrektur, Kalibrierung,
Gamma/Q_N/T_N und allgemeine Kandidatenauswahl sowie die gemeinsame
Operator-/Potentialpfadzuordnung. Der berechenbare N0-Sonderfall hebt sie
nicht auf. Die vollstaendige Zuordnung mit Einzelbelegen steht in der Review.

## 6. Der naechste begrenzte Auftrag

Die [unabhaengige Auswahlreview](../04_reconstruction/alpha_audit/reviews/BALANCE24_NEXT_STEP_REVIEW_2026-09-06.md)
empfiehlt eine **H006-interne K4/W4-Fallpruefung ohne Massenrechnung**.
Der vorhandene [N0-Rechner](../scripts/audit_n0_electron.py) verlangt die
ersten drei Basiswerte `(3,3,2)` und `0<W4<=1`; `K4=1` wird in diesem
Sonderfall analytisch bestaetigt. Er implementiert keinen allgemeinen
Solver der drei W4-Faelle. Die bisherigen Normalisierungen
[W4-Faelle](../04_reconstruction/formula_library/normalization/decisions/NORM-1982-ALGO-W4-CASES.md)
und [Ganzzahlregel](../04_reconstruction/formula_library/normalization/decisions/NORM-1982-ALGO-INTEGER-DECIMAL-RULE.md)
dokumentieren Lesarten/Pseudocode, keinen vollstaendigen Erhaltungsnachweis.

Der Folgeauftrag hat vier Teile:

1. H006 Druck/PDF9 erneut **mit dieser neuen Frage** visuell pruefen:
   `W4=0`, `0<W4<=1`, `W4>1`, Ganzzahl-/Dezimalregel, K3-Aenderung und
   `n4=K4-Q4`. H015 PDF42/Blatt6 separat vergleichen; keine Texte verschmelzen.
2. Fuer jeden Zweig Definitionsbereich, Eingaben, Reihenfolge und Resultat
   festhalten. Mehrdeutige Vor-/Nachschrittlesarten sichtbar getrennt halten.
3. Die gruppierte Restgleichung vor und nach Ganzzahl-/Sonderfallschritt
   pruefen. Exakte oder zertifizierte Grenzzeugen verwenden; einen
   Nachkommarest nicht durch frei gewaehltes Epsilon zum Integer erklaeren.
4. Gleichungserhalt, Rest und Strukturbedingungen getrennt berichten.
   Eine mathematische Testeingabe ist noch kein quellenbelegter Teilchenfall.

Abschluss ist eine Falltabelle mit Quellenregel, algebraischem Anschluss,
Zusatzannahmen und Folgen fuer K4/n4. Ein offener oder widerspruechlicher
Zweig ist ein zulaessiges Ergebnis; er wird nicht durch eine Ersatzregel
oder einen Massentreffer geschlossen. Noch keine neue Teilchenmasse,
Resonanzrechnung oder Ausfuehrung historischer Fremdprogramme.

Vor einem zweiten quellengebundenen N0-Fall muessen ausserdem Fassung und
Teilpfad, Komponentenidentifikation, `W_(nu,x)`, Konstantenprofil und der
benoetigte Auswahlzweig festliegen. Allgemeine N>0-Faelle brauchen weiterhin
die offene Dynamikbruecke. H/G-Pfade werden erst bei einem neuen konkreten
Kanal-/Operatorbeleg wieder aufgenommen; die jetzige Bilanz liefert keinen.

## 7. Nachweis, Zuschreibung und Sicherung

Heims belegte Grundideen bleiben ihm zugeschrieben; spaetere Beitraege,
unsere Normalisierungen, Rechnungen und moegliche Erweiterungen werden
nach [SOURCE_ATTRIBUTION](../00_admin/SOURCE_ATTRIBUTION.md) getrennt.
Die drei Agentenreviews sind interne Gegenpruefungen, kein externes Peer Review.
Neue Primaerquellenbefunde werden mit dieser Synthese nicht beansprucht.

Abschlusskontrollen: zehn alte Snapshot-/Quellchecks, 185 vorhandene Tests,
Registervalidierung sowie vollstaendige Zuordnung der 34 Tabellen-IDs.
Alte Rechner, Eingaben, Tests, Snapshots, Register und Normalisierungen
bleiben unveraendert. Es gibt weder neue Messdaten noch eine aktualisierte
Masse oder ein neues Gesamturteil zur Theorie.

Der [Wiedereinstieg](../00_admin/RESUME.md) und die
[Arbeitsfolge](../00_admin/UNDERSTANDING_ROADMAP.md) halten diesen Stand und
den einzelnen Folgeauftrag fest. Breite moderne Empiriepruefung bleibt
eine eigene, spaetere Phase mit vorher festgelegtem Modell- und Datenvertrag.
