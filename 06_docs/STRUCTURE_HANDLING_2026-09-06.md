# Strukturverletzungen: keine belegte Reparatur des Buchfalls

2026-09-06, Etappe31, Ausgang `2ae50af`. Plancheckpoint `ec5e5a9`,
Buch-/Portreviews und acht eigene Tests gesichert in `0118ae9`.
Fortsetzung von [Etappe30](BOOK_PSEUDOSINGLET_2026-09-06.md).

## Ergebnis

Die gezielte Quellenpruefung liefert keine zusaetzliche Regel, welche den
bereits berechneten Buchfall N_(j)=(14,9,13,7) mit beta3=-10 repariert.
Das ist mehr als ein blosser Nichtfund eines Suchworts: Die vorhandenen
Eingriffe haben andere Ausloeser, und die gelesenen Programmzweige testen
die verletzte Bedingung nicht. Der bedingte Befund FIND-040 bleibt bestehen.

Zugleich waere die Aussage falsch, Heim habe ueberhaupt keine
Umstrukturierung vorgesehen. Das Buch beschreibt den Kollaps bei beta_j=0,
eine spezielle Zone4-Korrektur und einen begrenzten Transfer3->4.
Sie sind nicht zu einer allgemeinen Reparatur negativer Bandbreiten
zusammengesetzt. Die historischen Programme sind dazu keine identische
Implementierung und kein belegtes Autorenerratum.

Keine neue Masse, F_S-Bestimmung, Y9-Wahl oder Ersatzbesetzung wurde
berechnet. Die zwei Eingabeprofile aus05a0bab und ihr Snapshot bleiben gleich.

## 1. Was das Buch positiv vorgibt

H004, *Elementarstrukturen der Materie II*, Ausgabe1996:

| Quellenstelle Druck/PDF | Tatsaechliche Regel | Grenze ihrer Aussage |
|---|---|---|
| 321/327, (107) | Zwei Struktur-Ungleichungsreihen; auch fuer invariante Grundmuster | Kein Algorithmus zur Reparatur eines gescheiterten Kandidaten |
| 323/329 | deltaG=(N1^3,N2^2,N3,1), alpha_j stehen separat in W | Keine allgemeine gewichtete Umdefinition |
| 328/334, (107a) | Bei Erreichen beta_j=0 kollabiert Zonej zu G_j=0; vorige n-Besetzung steigt um1 | Vor-/Nachzustand unterscheiden; kein gedruckter beta_j<0-Zweig |
| 340/346 | (107) wird vor der Exhaustion ausdruecklich vorausgesetzt | Verweis allein spezifiziert keinen Ruecksprung |
| 341/347 | N1,N2,N3 sukzessiv maximal; danach Log/TRC fuer N4 | Keine explizite Pruefung der fertigen Zone2->3-Bandbreite |
| 341/347 | Zone4-Kappe; Minus1 nur bei TRC(cap)>cap | Kein Zuruecksetzen von N2/N3 wegen beta3<0 |
| 341-342/347-348 | Bei k=2,W5<0 Transfer3->4, W6-Gates und Nichtnegativitaet | Kein Sonderfall des hier gerechneten k=1,0<W4<1 |

Auf342 schliesst der Text einen analogen Transfer2->3 oder1->2
ausdruecklich aus und begruendet das mit den verschiedenen Polynomformen.
Diese Quellenbegruendung wird hier wiedergegeben, nicht als allgemeiner
mathematischer Unmoeglichkeitsbeweis jeder anderen Umverteilung ausgegeben.

Der Kollaps in107a ist ein Prozess: Ein zuvor positiver Abstand erreicht
den Rand, danach werden Besetzungen umstrukturiert. G_j=0 ist dabei der
Zusammenbruch/Reset, nicht ein zugleich unveraendert bleibender alter G_j.
Unser nach der direkten Auswahl negativer Wert -10 ist nicht dieser Rand.

Die spaetere Stelle329/PDF335 druckt tatsaechlich die Gleichsetzung
beta4=delta3G3-(n4+Q4)=alpha3*N3-N4. Der offene Punkt ist also nicht das
Fehlen einer Gleichsetzung, sondern die fehlende dazu passende Erklaerung
gegenueber delta3G3=N3 auf323. In den geprueften Anschlussseiten wird
keine allgemeine neue G/delta-Definition angegeben, die alle Gates ersetzt.

## 2. Das fotografierte FORTRAN-Listing H015

Physische PDF23 enthaelt GSTRUC mit beiden gedruckten Routineseiten.
Die Auswahl berechnet IK1,IK2,IK3 aus Wurzeln/Quotient und IQINT. Es gibt
keinen aktuellen Vergleich IK2^2>IK3*(IK3+1)/2 und keine Ruecksetzung von
IK2. Nach der Zone4-Auswahl werden die kleinen IN_j=IK_j-IQ_j ausgegeben.
Die IQINT-Funktion wird nicht still zur Buch-TRC-Messbarkeitsschwelle erklaert.

Der Sonderzweig zeigt einen zusaetzlichen lokalen Datenflussbefund:

```text
W4>1: Sprung direkt zu Label3
      IK3 := IK3-1
      IK4 := IK4 + IQINT(ALF3*QFLOAT(IK3))
```

Der Sprung ueberspringt die vorherigen aktuellen IK4-Zuweisungen aus
Logarithmus bzw. Nullrestkappe. Die Addition liest deshalb den in COMMON
liegenden IK4-Bestand, ohne ihn in diesem Aufruf zuvor festzulegen.
Das belegt eine Abhaengigkeit vom Vorbestand dieses Zweigs, nicht einen
bestimmten Zahlenwert, zufaellige Speicherbits oder tatsaechlichen Laufabbruch.
Dieser Sonderzweig wird vom Buchfall aus Etappe30 nicht erreicht.

Der direkte Caller auf physischer PDF4 ruft bei ISN0059/00005600 GSTRUC
und unmittelbar bei ISN0060/00005700 GMASS(AM) auf, danach folgt die Ausgabe.
MAIN ist ueber die Fotos PDF18/4/19 verteilt; die Resonanzbegrenzung liegt
im N=1-Sprungpfad, nicht als Akzeptanztest nach jeder GSTRUC-Rueckkehr.
GMASS aufPDF24 verwendet die gelieferten Werte ohne solchen Strukturfilter.
Die gesehene AusgabeseitePDF14 bestaetigt das Tabellenformat, nicht die
Korrektheit aller historischen Werte oder ihre Identitaet mit Buchprofilen.

Der Scan zeigt verschiedene Datumsangaben und fotografierte Zusammenstellungen.
Eine Scan-/Dateifassung beweist weder vollstaendige Ueberlieferung noch
Autorenabsicht. Die Routine wird als H015-Listing, nicht pauschal als jede
historische Heim-/Schulz-Fassung behandelt.

## 3. Spaetere Pascal- und C-Fassungen H010

Statisch geprueft: Pascal0.62c GSTRUC452-512 und C0.66 GStruc894-979,
direkte Caller, GMASS und GLIMIT; C zusaetzlich Ausgabesammlung/Nachvergleich.
Genaue Pfade/Hashes stehen im [Quellenumfang](../03_notes/STRUCTURE_HANDLING_SOURCES_2026-09-06.md).

- Beide Routinen integerisieren IK1..IK3 direkt. Ein aktueller107/107a-Test
  und eine strukturbedingte Ruecksetzung von K2 oder K1 fehlen dort.
- Bei W4>0 wird der Logarithmus zuerst integerisiert. Fuer W4>1 folgt
  genau ein K3-- und die Addition des integerisierten alpha3*K3-NACHwerts.
  Das unterscheidet sich sowohl vom H015-Sprung vor der IK4-Zuweisung als
  auch vom Buch: Dort steht im ersten reellen W6-Schritt der alte N3-Wert.
- Es fehlen die allgemeine Rohwertkappe und eine wiederholte Transferfolge
  mit Buch-Gates. W4 wird nach K3-- nicht neu berechnet.
- Die Meldung `Resonance not allowed!` ist kein kontrollflusswirksamer Ausschluss.
  Pascal489 setzt msg; Caller723/724 und742/743 rechnen trotzdem weiter
  und drucken msg mit. C948-949 meldet nur bei print>1; Dateidefault print=1.
  Caller1250/1251 und1290/1291 rufen danach ohne Statuspruefung GMass auf.
- C hat einen K1^3-Assert; dieser ist keine107-Pruefung. Eine normale
  Rueckkehr wird fuer ungueltige Laufzeitarithmetik nicht garantiert.
  Die Verbotsmeldung selbst verhindert die Weiterverarbeitung jedoch nicht.

Die Portierer beschreiben den alten W4>1-Fehler und ihre Aenderungen in
Kommentaren/Readmes. Das ist als Bearbeiterangabe zu kennzeichnen. Die
sichtbare neue Zuweisungsreihenfolge bestaetigt die lokale Aenderung,
aber nicht eine umfassend korrekte Implementierung der Buchtheorie.

Rundungsregeln sind ebenfalls verschieden: Pascal benutzt trunc(x+1e-10),
C myround mit einem Vorzeichen-abhaengigen Offset1e-7 vor trunc. In exakter
reeller Lesung etwa Pascal(-2)=-1, C(-2)=-2. Das ist keine Emulation eines
historischen Compilers und keine neue Buch-TRC-Konvention.

## 4. Warum die Resonanzgrenzen nicht genuegen

GLIMIT ist nicht frei von verwandter Strukturalgebra. C1046-1065 bzw.
Pascal562-581 konstruieren gewichtete Randkandidaten. Fuer die reellen
M_j-Kandidaten vor der jeweiligen Integerisierung der L_j+Q_j gilt:

\[
\alpha_2G_2(M_2)=\alpha_1M_1^3,\quad
\alpha_3G_3(M_3)=\alpha_2M_2^2,\quad M_4=\alpha_3M_3.
\]

Danach wird eine skalare Resonanzgrenze bestimmt. Diese Konstruktion an
den oberen L-Werten ist weder eine Pruefung der ungewichteten Buch-Gates
am aktuellen K-Tupel noch eine Reparatur desselben. In H010 wird bereits
der N=0-Wert vor GLIMIT berechnet und ausgegeben.

Selbst gueltige obere Grenzen allein garantieren keine lokale Gueltigkeit.
Ein eigener exakter Zeuge im positiven Integerbereich ist:

| Tupel | Direkte Bandbreiten beta2,beta3,beta4 | Zweite107-Reihe |
|---|---|---|
| U=(5,4,3,2) | (95,10,1) | bestanden |
| K=(4,2,3,2), komponentenweise K<=U | (59,-2,1) | bestanden |

K liegt innerhalb der Komponentengrenzen und verletzt dennoch die erste
107-Reihe. Das ist ein eigener mathematischer Gegenbeleg gegen die
Rechteck-Schlussfolgerung, keine Behauptung ueber einen realen GLIMIT-Lauf.

## 5. Eigene Kontrollen und Aussagegrenzen

Acht neue [Tests](../tests/test_structure_handling.py) enthalten weitere
synthetische, von den Quellenkonstanten getrennte Diagnosen:

- W1=145/2, alpha=(1,1,1), lambda=1/3 ergibt gestaffelt(4,2,4),W4=1/2
  und N4=2. Die Rohwertkappe besteht; beta=(59,-6,2) verletzt trotzdem107.
- Positive Restwahl allein garantiert keine Zone4-Kappe.
- Negative Logwerte: Trunkierung gegen null ist nicht floor.
- Transferzeuge alpha3=2,altesN3=4,W4=3/2,lambda=1/15: der Buch-Erstschritt
  ergibt nach Abschneiden N4=1, die beiden Port-Lesregeln N4=0.
  Kein vollstaendiger Teilchenzustand oder allgemeiner Transferloeser.

Logarithmen der synthetischen Zeugen werden mit rationalen Reihen und
expliziten Restschranken eingeschlossen. Der unabhaengige Reviewblock mit
36 exakten Kontrollen wurde von Root erneut ausgefuehrt. Die Tests beweisen
nicht den statischen Nichtfund; dazu dienen die gelesenen Anweisungen.
Drei interne Reviews sind keine externe Begutachtung.

Die bisherigen264 Tests bleiben erhalten; mit acht neuen sind es272.
Zwoelf bestehende Ergebnischecks pruefen die unveraenderten Rechnungen.
Keine neuen Quellprogramme ausgefuehrt, Quellen veraendert, Massen bestimmt
oder Y-Faktoren angepasst. Die49CSV-Normalisierungen bleiben erhalten.

## 6. Naechster Einzelauftrag

Eine ausdruecklich eigene **gekoppelte Existenzpruefung** bei den unveraenderten
Buchinputs vorbereiten: Gibt es ueberhaupt ein nichtnegatives ganzzahliges
Tupel, das gleichzeitig die direkten Strukturbedingungen und108 erfuellt?

Dafuer zuerst aus Positivitaet und Strukturbedingungen einen vollstaendigen
endlichen Suchbereich ableiten, kollabierte/aktive Zonen trennen und die
transzendenten Eingaben mit begruendeten Schranken behandeln. Exakte108,
Ganzzahl-/TRC-Auswahl und ein tolerierter Rest sind verschiedene Auftraege;
keine Toleranz nach dem Ergebnis waehlen. Unabhaengige Gegenpruefung.
Keine Ersatzbesetzung nach kleinster Abweichung, keine Masse/F_S/Y9-Suche.

Dieser Folgeschritt waere unsere Diagnose des festen Gleichungssystems,
nicht ein nachtraeglich Heim zugeschriebener Auswahlalgorithmus.
