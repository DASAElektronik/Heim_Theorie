# F_S: 17 Komponenten, historische Messdaten und Y41-44

2026-10-18, Etappe 39. Ausgang `442adf7`.
Fortsetzung der [Massenformelkette](MASS_CHAIN_2026-09-07.md).

## Ergebnis

Die auf H004 Druck 342 genannten 17 Ausgangspunkte lassen sich anhand von
(101a/b) nach Teilchenkomponenten rekonstruieren. Eine historische
Referenztabelle mit passenden Massen und Unsicherheiten wurde in der
offiziell archivierten PDG-Ausgabe von April 1974 gefunden. Das Buch nennt
diese Jahresquelle ausdrücklich für die empirische Koeffizientenanpassung;
eine vollständige zeilenweise Zuordnung der tatsächlich für F_S eingesetzten
Messwerte ist damit noch nicht belegt.

Die Festlegung der Y-Faktoren für den Tabellenanhang ist dagegen explizit:
Die Einführung setzt sämtliche Y_k auf 1, also auch Y41-44. Diese Annahme
markiert ungeklärte Beziehungen; sie ist weder eine unabhängige Herleitung
der Eins noch der Nachweis von vier frei optimierten Fitparametern.

## 1. Welche 17 Komponenten sind gemeint?

Druck 342 beschränkt die empirischen F_S-Punkte auf v=1 bis10, ohne e0.
Die Zuordnung steht auf Druck 291/(101b), ihre Ladungsaufteilung auf
Druck 288-289/(101a). Daraus ergibt sich die folgende eigene Nachzählung:

| v | Zugeordnete Komponenten | Anzahl im F_S-Ausgangsbestand |
|---|---|---:|
| 1 | eta | 1 |
| 2 | e-; e0 ausdrücklich ausgeschlossen | 1 |
| 3 | mu- als Pseudosingulett | 1 |
| 4 | K+, K0 | 2 |
| 5 | pi+, pi0, pi- | 3 |
| 6 | Lambda | 1 |
| 7 | Omega- | 1 |
| 8 | p, n | 2 |
| 9 | Xi0, Xi- | 2 |
| 10 | Sigma+, Sigma0, Sigma- | 3 |
| Gesamt | | 17 |

Das Pseudosingulett zählt hier einmal: Druck 288 beschreibt seine beiden
Komponenten als identisch und fasst sie entsprechend zusammen. e0 und
die jeweils vier Komponenten von v=11 und 12 gehören auf 342 zum
Extrapolationsauftrag. Damit passt auch 17 + 1 + 4 + 4 = 26 zur dort genannten
Gitterpunktzahl. Dies ist eine Rekonstruktion der Quellenzählung, keine
Prüfung der Existenz aller zugeordneten Zustände.

17 Komponenten bedeuten nicht automatisch17 unabhängige Massenangaben:
H004 Druck 372 und die historische PDG-Tabelle führen pi+ und pi- gemeinsam
als pi±. Der einschlägige Teil der Buchausgabe besitzt daher16 numerische
Masseneinträge für diese 17 Komponenten. Daraus wird weder eine Zahl
unabhängiger Fitbedingungen noch ein statistischer Freiheitsgrad abgeleitet.

## 2. Welche historische Datenquelle nennt Heim?

Die Jahresangaben müssen ihrem jeweiligen Gegenstand zugeordnet bleiben:

| H004-Stelle | Beleg | Reichweite |
|---|---|---|
| 335/(109b) | A_im und A66 heuristisch aus empirischen Grundzustandsdaten | Empirischer Ursprung der Koeffizienten; keine Einzelwertliste |
| 336, Fußnote4 | CERN-Messdaten1974, Review of Particle Properties | Unmittelbarer Kontext: empirische Resonanzmassen und f(N) |
| 339 vor 110c | Koeffizienten A41 bisA65 aus CERN-Daten1974 angepasst | Resonanzspektrum; diese A-Indizes sind nicht die Y41-44 aus 111 |
| 342 | 17 zugeordnete Messmassen zur Gewinnung von F_S | Keine Einzelwerte, Unsicherheiten oder eigene Jahresangabe |
| 355, Fußnote6 | 1974 zur Anpassung der Matrix in110d; 1976-1982 laut Autor zur Bestätigung | Autorenbericht zur Verwendung der Daten, kein von uns nachgewiesener zeitlich getrennter Vorhersagetest |

Die bibliographische Spur führt zu *Review of Particle Properties*,
Particle Data Group, Physics Letters 50B, Nr. 1, April 1974. Der
[offizielle Publikationsnachweis](https://pdg.lbl.gov/2025/list_of_RPP_publications.html)
und der [Archivscan](https://pdg.lbl.gov/rpp-archive/files/Physics-Letters-B-1974-v50.pdf)
sind als M006 verzeichnet. Die Ausgabe passt zur im Buch benannten
Jahresquelle. Dass genau ihre zusammenfassenden Tabellenwerte in jedem
F_S-Schritt benutzt wurden, bleibt eine gesonderte Provenienzfrage.

## 3. Historische Referenzwerte, noch kein freigegebener Eingabedatensatz

Transkription aus M006, Stable Particle Table, Druck 1-3/PDF 20-22.
Einheit wie gedruckt: MeV. ±-Angaben sind die veröffentlichten Fehler,
keine harten Schranken. S kennzeichnet die gedruckte Fehlerskalierung;
laut Fußnote auf Druck 5 ist sie bereits berücksichtigt. Ein Strich
bedeutet nur: kein S an dieser Massenangabe gedruckt.

| v | Komponente | PDG1974 Masse ± Fehler | S | Druckseite |
|---|---|---:|---:|---:|
| 1 | eta | 548.8 ±0.6 | 1.4 | 2 |
| 2 | e- | 0.5110034 ±0.0000014 | - | 1 |
| 3 | mu- | 105.65948 ±0.00035 | - | 1 |
| 4 | K+ | 493.707 ±0.037 | - | 2 |
| 4 | K0 | 497.70 ±0.13 | 1.1 | 2 |
| 5 | pi+ | 139.5688 ±0.0064 | - | 1 |
| 5 | pi0 | 134.9645 ±0.0074 | - | 1 |
| 5 | pi- | derselbe pi±-Eintrag wie oben | - | 1 |
| 6 | Lambda | 1115.60 ±0.05 | 1.2 | 3 |
| 7 | Omega- | 1672.2 ±0.4 | - | 3 |
| 8 | p | 938.2796 ±0.0027 | - | 3 |
| 8 | n | 939.5731 ±0.0027 | - | 3 |
| 9 | Xi0 | 1314.9 ±0.6 | - | 3 |
| 9 | Xi- | 1321.29 ±0.14 | - | 3 |
| 10 | Sigma+ | 1189.37 ±0.06 | 1.8 | 3 |
| 10 | Sigma0 | 1192.48 ±0.08 | - | 3 |
| 10 | Sigma- | 1197.35 ±0.06 | - | 3 |

Quelle: [PDG1974, offizieller Scan](https://pdg.lbl.gov/rpp-archive/files/Physics-Letters-B-1974-v50.pdf).
Die Ladungszuordnung der Tabelle ist unsere Verbindung zu H004/101b;
M006 selbst verwendet teils Sammelbezeichnungen wie e, mu und K±.
Diese Referenzwerte werden nicht in einen bestehenden Rechner importiert.
Die experimentellen Einzelpublikationen hinter den PDG-Zusammenfassungen
sind noch nicht bis auf jeden Messwert verfolgt.

## 4. Warum der Buchanhang die F_S-Eingaben nicht ersetzt

H004 Druck 371 kennzeichnet die folgenden Werte als theoretische Daten.
Auf 372 stehen berechnete Grundmassen zusammen mit den Besetzungen n1..n4.
Die weiteren Seiten 373-376 behandeln Resonanzen und weitere theoretische
Zuordnungen. Der vollständig gelesene Anhang enthält keine als solche
ausgewiesene Liste der 17 extrahierten F_S-Werte samt ursprünglichen
Messmassen, Unsicherheiten und Einzelnachweisen.

Der Vermerk auf 371 nennt außerdem eine Korrektur dimensionaler Konstanten
mithilfe von (29) und der Elektronenform von (112), mit Rückverweis auf
den Text nach(115). Wie diese Korrektur genau durchgeführt wurde und
welche empirischen Eingaben sie bindet, ist hier nicht rekonstruiert.
Sie darf in einem späteren Rechenvertrag nicht still durch heutige
Konstanten ersetzt werden. Die auf derselben Seite berichtete numerische
Kontrolle durch H.D.Schulz am26.7.1982 ist ein Quellenbericht über eine
Rechnung, keine zusätzliche Messung der 17 Grundmassen.

Das Impressum nennt Manuskripteinreichung 20.3.1981, Copyright 1984 und
Gesamtherstellung 1996. Diese Daten datieren nicht automatisch jeden
Formel- oder Tabellenstand. Insbesondere wird aus dem Einreichungsdatum
kein Beweis, dass jede im späteren Druck enthaltene Aussage schon1981
feststand.

## 5. Was ist für Y41-44 tatsächlich festgelegt?

Die Einführung auf Druck 1 erklärt allgemein, dass Y_k ungeklärte
mathematische Beziehungen markieren, und setzt für die theoretischen
Tabellenwerte alle Y_k=1. Druck 342 gibt die F_S-Hilfsformen zunächst
ohne diese vier Symbole an; Druck 343 versieht sie in111a/b mit den Y.
Einsetzen von Y41=Y42=Y43=Y44=1 stellt lokal die vorgeschlagenen Formen
wieder her. Es handelt sich um die dokumentierte Buchannahme.

| Faktor | Stelle in111a/b | Festlegung im Tabellenanhang |
|---|---|---|
| Y41 | Zusatzterm von F2 | 1 |
| Y42 | q*eta^2*(k-1)-Beitrag in Fq | 1 |
| Y43 | Zusatzterm von F_kappa | 1 |
| Y44 | Multiplikator in xi^2*B_v | 1 |

Damit ist die numerische Annahme für diesen Tabellenstand geklärt.
Ungeklärt bleibt ihre physikalische Deduktion. Die Einführung auf 2-3
bezeichnet die strukturelle Ableitung der betreffenden Funktionen
ausdrücklich als offenen Auftrag und ordnet109 bis111 heuristisch ein.
335 erläutert denselben Status für die vorgelagerten Koeffizienten.

Es wurde kein Optimierungsprotokoll, keine Kovarianzmatrix und keine
quantitative Unsicherheitsverteilung für Y41-44 im genannten Umfang
gefunden. Vier Symbole sind deshalb nicht gleichbedeutend mit vier
nachgewiesenen freien Fitparametern. Umgekehrt beseitigt Y=1 die
empirische Auswahl der Funktionsform auf 342 nicht. Eine feste Zahl in
der Endform sagt noch nichts über den Entstehungsweg dieser Endform.

## 6. Bilanz und nächste konkrete Frage

Belegt sind jetzt die Komponentenliste und ihre Zählung, die lokale
Y=1-Tabellenannahme sowie eine passende historische PDG-Referenztabelle.
Weiter offen sind die ursprüngliche F_S-Arbeitsliste, die genaue
Koeffizienten-/Konstantenfassung bei ihrer Gewinnung und die Auswahl
der gemeinsamen Hilfsfunktionen. FIND-049 fasst diesen Provenienzstand
zusammen; es ist keine zusätzliche Fehlerzählung.

Der nächste begrenzte Auftrag ist die **Quellenprüfung der
Konstantenkorrektur nach(115) und ihres Elektronenankers**, einschließlich
des Anschlusses an den Vermerk auf 371. Parallel zur späteren Quellenarbeit
bleibt nach einer historischen F_S-Arbeitstabelle zu suchen. Erst mit
gebundenen damaligen Eingaben wäre eine numerische Rückgewinnung der
F_S-Punkte sinnvoll; die PDG-Tabelle allein schließt diesen Vertrag nicht.

Diese Etappe berechnet keine Teilchenmasse, passt keine Parameter an und
prüft keine modernen Messdaten. Quellenkontrolle durch einen Agenten,
kein unabhängiges Mehragentenreview oder externes Peer Review.
[Quellenumfang und Dateihashes](../03_notes/FS_PROVENANCE_SOURCES_2026-10-18.md).

Technischer Abschluss: Alle 354 bestehenden Tests und der Registervalidator
bestanden. Die 48 alten Befunde sind inhaltlich unverändert. Git-Diffprüfung
und lokale Links der neuen Dokumente geprüft. Softwaretests bestätigen
die technische Integrität, nicht die Quelleninterpretation.
