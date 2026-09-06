# Historische Exponenten: Typoskript und spaetere Wiedergabe

2026-09-06, Etappe 23. Ausgang `57e92f8`, Plancheckpoint `125da3a`.
Enger Nachtrag zu FIND-027; keine neue Teilchenmassenrechnung.

## Ergebnis und Zuschreibung

Der in H006 festgestellte Unterschied zwischen der allgemeinen Auswahlregel
(XIV) und dem N=0-Fall (XXVI) ist im jetzt geprueften fotografierten
Typoskript H015 nicht vorhanden. Dort steht an beiden Stellen dieselbe
gruppierte Exponentenform. Die benachbarten Wiederholungen und der
Logarithmusschritt stuetzen ebenfalls diese Form.

Das ist ein positiver Quellenanschluss: Die gruppierte Formel ist keine
von uns erfundene Reparatur. Sie ist im Heim zugeschriebenen Typoskript
belegt und auch innerhalb H006 mehrfach vorhanden. Unser Beitrag besteht
in der Gegenlesung, expliziten Normalisierung und algebraischen Kontrolle.

FIND-027 bleibt ein lokaler Darstellungswiderspruch der festgelegten
H006-Lesart. Er darf nicht ohne Weiteres Heim selbst oder dem untersuchten
Typoskript zugeschrieben werden. Ein Uebertragungs-/Satzfehler ist eine
plausible Erklaerung, aber die konkrete Entstehung ist nicht nachgewiesen.
Weder wird die Theorie dadurch bestaetigt noch ihre gesamte Herleitung
repariert. Es bleiben 34 Befundgruppen, keine neue Fehlerzaehlung.

## 1. Zwei Dokumente, nicht ein austauschbarer Text

H006 ist die IGW-Wiedergabe *Die Massenformel nach Burkhard Heim (1982)*.
Das Titelblatt nennt den Forschungskreis Heimsche Theorie, IGW Innsbruck,
2002; die laufenden Seitenkoepfe nennen 2003. Die Schlussseite traegt den
wiedergegebenen Vermerk `gez. (Heim)` und das Datum 25.2.1982. Dieses Datum
datiert die beanspruchte Vorlage, nicht die Entstehung des heutigen PDFs.

H015 ist ein heutiger Archivscan fotografierter Listings und Typoskriptseiten.
PDF39 zeigt oben die Blattzahl 4, PDF41 die 5, PDF42 die 6 und PDF43 die 7.
Die unteren Zahlen sind Fortsetzungsvermerke, nicht die Blattidentifikation.
PDF43 zeigt eine Signaturabbildung mit `(Heim)` und die Datumszeile
Northeim, 25.2.1982. Die 2026-Metadaten betreffen die Digitalisierung.

Das macht H015 fuer diese Glyphenfrage naeher am fotografierten Dokument
als die neu gesetzte H006-Wiedergabe. Es beweist keine lueckenlose
Ueberlieferungskette, forensische Echtheit oder Autorschaft jedes einzelnen
Blatts. Die roemischen Gleichungsnummern aus H006 stehen nicht auf den
geprueften H015-Typoskriptseiten. Unsere Zuordnung ist inhaltlich, nicht
eine Behauptung identischer Seitengestaltung.

## 2. Was wirklich gedruckt ist

H006 (XIV), Druck/PDF6, hat die lineare Zeichenfolge

    exp[1-2k(n4+Q4)/3Q4].

Die schon zuvor ausdruecklich festgelegte Normalisierung liest den Nenner
als 3*Q4. Sie setzt keine zusaetzliche Klammer um 1-2k. H015 zeigt dagegen
einen Bruch mit dem ganzen Zaehler 1-2k, gefolgt vom Faktor (n4+Q4).
Unsere Kurzbezeichnungen fuer die Exponenten sind deshalb

    A = 1 - 2*k*(n4+Q4)/(3*Q4),
    B = (1-2*k)*(n4+Q4)/(3*Q4).

Wichtig: A ist nicht (1-2*k*(n4+Q4))/(3*Q4). Diese andere Umklammerung
waere ebenfalls eine zusaetzliche Lesart, nicht die hier gepruefte.

| Inhalt | H015: PDF / obere Blattzahl | H006: Druck=PDF / Formel | Exponent |
|---|---|---|---|
| Allgemeine Auswahlregel | 39 / 4 | 6 / XIV | H015 B, H006 A |
| Basisanstieg bei allen n_j=0 | 39 / 4 | 6 / XV | beide (1-2k)/3 |
| N=0-Gleichung | 41 / 5 | 8 / XXVI | beide B |
| N=1-Realteil | 41 / 5 | 8 / XXVII | beide B |
| Reelle Gleichung nach Ausschluss N=1 | 41 / 5 | 8 / XXIX | beide B |
| Restgleichungen W2 und W3 | 42 / 6 | 9 / XXX und XXXI | beide B |
| Resonanzgrenze | 43 / 7 | 10 / XXXV | beide B mit L4 statt n4 |

Diese Tabelle vergleicht nur den jeweiligen Exponentialterm. Sie beweist
keine vollstaendige Gleichheit aller benachbarten Koeffizienten oder Texte.
(XXXIV) enthaelt Grenzungleichungen, nicht den hier verglichenen Exponenten.
H015 PDF40/Blatt4a ist eine Anmerkung zur Strukturpotenz und 0^0, kein
Erratum dieses Exponentialterms.

Die kleinen Klammern in H006 (XXVII)/(XXIX) wurden nach vorlaeufiger
Kleinbildunsicherheit in hochaufgeloesten Ansichten gesondert gegengelesen.
Sie sind vorhanden. In dieser begrenzten Kette weicht nur (XIV) ab.

## 3. Exakte Unterscheidung ohne Massenziel

Fuer Q4>0 und K4=n4+Q4>=0 gilt durch einfache Subtraktion

    A-B = 1-K4/(3*Q4) = (2*Q4-n4)/(3*Q4).

Damit sind beide reellen Exponenten genau dann gleich, wenn n4=2*Q4.
Die reelle Exponentialfunktion ist injektiv; dasselbe gilt fuer exp(A)
und exp(B). Ein einzelner Treffer an diesem Sonderpunkt waere daher kein
Beweis gleicher Formeln. Am bisherigen, explizit vorgegebenen N0-Pruefpunkt
k=Q4=1,n4=0 gilt dagegen exakt

    A=1/3, B=-1/3, A-B=2/3.

Der Quotient der isolierten Exponentialterme ist exp(2/3). Das ist kein
Quotient von Teilchenmassen. Allgemeiner wird bei n4=0 aus B genau der
Basisexponent (1-2k)/3; A liegt stets 2/3 darueber. Die Einbettung in den
vollstaendigen N0-Fall mit W=g ist bereits in Etappe16 dokumentiert.

Die neuen rationalen Pruefpunkte kontrollieren diese Algebra, nicht ihre
physikalische Realisierung. Der lokale Bereich n4>=-Q4 ist groesser als
n4>=0; die sonstigen Zonen- und Konfigurationsbedingungen bleiben getrennt.

## 4. Der anschliessende Rechenschritt entscheidet dieselbe Frage

H015 PDF42/Blatt6 und H006 Druck9 schreiben im Fall 0<W4<=1

    K4*(2k-1) = -3*Q4*ln(W4).

Fuer k=1 oder 2 ist dies die Umkehrung von W4=exp(B):

    K4 = -3*Q4*ln(W4)/(2k-1).

W4=exp(A) braeuchte stattdessen

    K4 = 3*Q4*(1-ln(W4))/(2k).

Setzt man die Exponenten rein algebraisch in die Quell-Logrelation ein,
verschwindet das K4-Residuum bei B identisch; bei A ist es

    (K4-3*Q4)/(2k-1).

Auch hier ist nur derselbe Sonderpunkt ununterscheidbar. Der Anschluss
stuetzt somit B ohne empirischen Massentreffer. Er autorisiert keine
stille Ersetzung anderer H006-Zeilen oder Eingaben. Insbesondere pruefen
wir nicht den gesamten stueckweisen Algorithmus: exp(A)>1 kann dessen
regulaeren Logarithmusfall verlassen. Keine neuen Besetzungen oder Massen
werden aus diesem isolierten Rueckwaertsvergleich behauptet.

## 5. Was sich am bisherigen Befund aendert

FIND-027 wird sichtbar ergaenzt, nicht geloescht und nicht als FIND-035
ein zweites Mal gezaehlt. Der H006-interne Konflikt bleibt reproduzierbar;
seine pauschale Uebertragung auf die Heim-Urschrift ist durch H015 nicht
gerechtfertigt. Die genaue Vorlage der IGW-Bearbeitung und ein autorisiertes
Erratum sind damit nicht identifiziert.

Die vorhandene N0-Rechnung nutzte bereits ausdruecklich (XV)/(XXVI) und
den Algorithmus. Sie erhaelt hier einen zusaetzlichen Quellenanschluss,
aber keine neuen Zahlen. Alle Alpha-/alpha3-/Konstantenfragen und die
fehlende physikalische Herleitung bleiben davon unberuehrt. Wir erstellen
keine vermeintlich historische Gesamtfassung aus jeweils passenden Teilen.

## 6. Nachpruefung und Fortsetzung

Zwei getrennte Quellenreviews, Root-Vollseitenkontrolle und unabhaengige
Algebrareview. Der vollstaendig gelesene Fraction-Kontrollblock wurde von
Root erneut ausgefuehrt: 42 allgemeine Paare, Sonderpunkte und symbolische
Inversenpruefungen bestanden. Sieben neue Tests, 185 insgesamt, und alle
zehn bisherigen Snapshot-/Quellchecks bestanden. Original-PDFs, alte
Rechner, Eingaben, Ergebnissnapshots und 49 Normalisierungszeilen unveraendert.
Dies sind interne Reproduktionskontrollen, kein externes Peer Review.

Die enge Exponentenfrage ist damit fuer diese zwei Dokumente beantwortet.
Naechster Arbeitsauftrag: die Verstaendnisbilanz der Etappen16-23
zusammenfuehren, insbesondere welche Auswahl-/alpha3-Teile quellenbelegt,
algebraisch angeschlossen oder weiterhin nur bedingt sind. Daraus die
naechste offene Herleitung waehlen, ohne eine neue Mischfassung zu rechnen.
H/G-Pfade nur bei konkretem neuem Kanal-/Operatorbeleg wieder aufnehmen;
die breite moderne empirische Bewertung bleibt nachgeordnet.

[Quellenumfang, Hashes und Reviewpfade](../03_notes/HISTORICAL_EXPONENT_SOURCES_2026-09-06.md).
