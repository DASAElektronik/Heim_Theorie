# Quellenreview: `eta_(2,2)` in der erweiterten Massenformel 1989

Datum: 2026-09-06. Enger Quellen- und Versionscheck der IGW-Ueberlieferung
H007. Ziel ist zu klaeren, was die Quelle selbst mit `eta_(2,2)` behauptet,
nicht die Buchauswahl (98a) erneut numerisch zu pruefen oder aus einem
Formelsymbol einen physisch realisierten Zustand zu konstruieren.

## Ergebnis

H007 druckt `eta_(2,2)` eindeutig, aber behauptet an keiner geprueften Stelle
ausdruecklich einen realisierten Zustand `(q,k)=(2,2)`. Der Faktor tritt auch
nicht nur in der Alpha-Korrektur auf:

- in (B47) als Faktor der allgemeinen Existenzzeitformel,
- in (B55) innerhalb des Terms `b_2`,
- in (B59) innerhalb der Definition von `1-C'=K_alpha`.

Auf der Alpha-Seite ist `eta_(2,2)` damit ein ausdruecklicher algebraischer
Input des Korrekturfaktors. Weder diese Seite noch die Einleitung gibt aber
eine Zustandsauswahl, eine neue Bedeutung von `q=2,k=2` oder eine Erklaerung,
warum gerade dieser Familienwert physikalisch in `C'` eingehen soll. Der
Richtungsbefund lautet deshalb:

```text
explizite Formelabhaengigkeit eta_(2,2)       belegt
berechenbarer Wert der eta_(q,k)-Familie      belegt
explizite Auswahl/reale Konfiguration (2,2)   nicht belegt
Uebernahme oder Aufhebung von Buch-II (98a)   nicht angegeben
```

Dies ist keine Aussage, dass eine solche Begruendung in allen erhaltenen oder
unveroeffentlichten Heim-Unterlagen fehle. Das berichtete 57-seitige
Manuskript lag diesem Review nicht als verifiziertes Faksimile vor. Der
Nachtrag in Abschnitt 7 belegt `eta_(2,2)` inzwischen auch in zwei
undatierten, Heim als Autor nennenden Typoskriptscans; er schliesst die
Herleitungs- und Zustandsluecke nicht.

## 1. Quellen- und Editionsstatus

### H007: spaetere IGW-Ueberlieferung, kein 1989-Faksimile

Lokale Quelle:
`01_sources/heim_primary/Erweiterte_Massenformel_Nach_Heim_1989.pdf`.
Sie umfasst 11 PDF-Seiten, entsprechend den gedruckten Seiten 10 bis 20, und
hat SHA-256
`0E2F646D784152FB008944F58E1B8E709A416B65265D2FB75D3CC44C88FF8A40`.
Die aktuelle, laut Quellenregister byte-identische Herausgeberkopie ist:

<https://heim-theory.com/wp-content/uploads/2026/03/F_Erweiterte_Massenformel_nach_Heim-1989.pdf>

Die Titelseite, Druck 10 / PDF 1, sagt zugleich:

- *Die erweiterte Massenformel nach Burkhard Heim (1989)*,
- "Nach einem Manuskript von Burkhard Heim",
- Forschungskreis Heimsche Theorie, IGW Innsbruck, 2002.

Der Seitenkopf traegt `Copyright IGW Innsbruck, 2003`. Die PDF-Metadaten
nennen als Titel eine Word-Datei, als Autor `Admin`, Microsoft Word/Acrobat
PDFWriter 5.0 und den Erstellungszeitpunkt 25.09.2003. Der greifbare Text ist
damit eine editorisch gesetzte Ueberlieferung von 2002/2003, die Formeln eines
berichteten Heim-Manuskripts von 1989 wiedergibt. Er ist nicht das behauptete
Originalmanuskript und kein Faksimile des nachfolgend erwaehnten 57-seitigen
Berichts.

Die Einleitung, Druck 11 / PDF 2, bestaetigt diese Trennung besonders deutlich.
Sie spricht in dritter Person ueber Heim und in erster Person Plural ueber die
spaetere Programmierung. Nach ihrer Darstellung:

1. programmierten DESY-Physiker 1982 die im Buch veroeffentlichte Formel;
2. erweiterte Heim sie und sandte 1989 einen 57-seitigen Bericht mit neuer
   Formel und Rechenergebnissen an MBB/DASA;
3. ist das damalige Programm nicht mehr auffindbar;
4. programmierte der Forschungskreis spaeter Teile neu (genannt wird
   Dr. A. Mueller);
5. seien im Manuskript in langen Gleichungen Klammern ausgelassen gewesen,
   die "nach besten Schaetzungen" korrigiert werden mussten;
6. enthalte das damalige neue Programm nur Grundzustaende und
   Neutrinomassen, nicht die Lebensdauern.

Das ist eine allgemeine Ueberlieferungswarnung. Sie identifiziert weder eine
bestimmte geschaetzte Klammer in (B58)-(B62) noch ein Alpha-Erratum. Auch
Farben oder typografische Hervorhebungen dieser Word-Fassung duerfen nicht
als sichere Schichtentrennung zwischen Heim und Herausgeber gelesen werden.
Die Formeln sind hier als von IGW berichtete Heim-Formeln nachgewiesen; ihr
unveraenderter Wortlaut im 1989-Bericht ist damit nicht bewiesen.

### H006 und der Rueckverweis `(IX)`

H007 Druck 12 / PDF 3 sagt unmittelbar vor (B8), die Konstanten
`eta_(q,k)`, `vartheta` und `eta` - mit `eta_(1,0)=eta` und
`vartheta_(1,0)=vartheta` - sowie `N_1,N_2` "lauten wie in (IX)".

Der sichtbare Bezugspunkt ist H006,
`01_sources/heim_primary/Massenformel_nach_B_Heim_1982.pdf`, ebenfalls eine
IGW-Word/PDF-Ueberlieferung von 2002/2003. Deren PDF 5, Gleichung (IX), druckt

```text
eta_qk = pi / [pi^4 + (4+k) q^4]^(1/4)
```

und daneben `N_1,N_2,N_3` bzw. `alpha_1,alpha_2,alpha_3`. Die Glyphenfolge ist
hier eindeutig `eta_qk`: erster Index `q`, zweiter Index `k`. Unter genau
diesem dokumentinternen Rueckverweis ist H007s `eta_(2,2)` daher die
Auswertung dieser Familie bei `q=2,k=2`; `eta_(1,2)` ist `q=1,k=2`.

Der Sammelverweis ist zugleich ungenau. Die eigenstaendigen Definitionen von
`eta` und `vartheta=5 eta+2 sqrt(eta)+1` stehen sichtbar auf H006 PDF 3 in
(V), nicht in (IX). `(IX)` definiert die zweistellige Familie und die
`N_i`-Anschluesse. Diese Provenienzpraezisierung bestaetigt
`NORM-1989-ALPHA-ETA-CROSSREF`; sie liefert keine neue Teilchenauswahl.

H006 ist selbst nicht still mit dem Buch gleichzusetzen: Auf PDF 3 schreibt
es im lokalen Alpha-Block `eta_kq`, auf PDF 5 dagegen `eta_qk`. Fuer H007 ist
der ausdrueckliche Rueckverweis auf `(IX)` die positive Bruecke zur
`(q,k)`-Lesart. Eine Zielwertnaehe wird zur Indexwahl nicht benoetigt.

## 2. Was der Text als Erweiterung und Motivation nennt

Die Einleitung beschreibt den 1989-Rahmen nicht als einzelne
`eta_(2,2)`-Korrektur, sondern als Erweiterung der Massenformel von 1982. Als
neue Moeglichkeiten nennt sie:

- mittlere Lebensdauern der Grundzustaende,
- Neutrinomassen,
- eine "exakte Berechnung" der Feinstrukturkonstante.

Sie kuendigt an, diejenigen Gleichungen wiederzugeben, die vom Manuskript
von 1982 abweichen. Unmittelbar folgen unter anderem:

- Division des Strukturdistributors `C` durch `k` gegenueber (I),
- geaenderter Zeithelizitaetswinkel (B1),
- geaenderte Ladungsquantenzahl (B2) anstelle von (II),
- die gegenueber (XII) anders zusammengesetzte Massenformel (B3),
- geaenderte Faktoren und Funktionen (B4)-(B46),
- das Lebensdauersystem (B47)-(B57),
- die Alpha-Kette (B58)-(B62),
- die Neutrino-Konstruktion ab (B63).

Diese Liste dokumentiert den von H007 selbst gesetzten Aenderungsrahmen. Sie
ist keine unabhaengige Herleitung dieser Formeln. Gerade die Alpha-Passage
verweist rueckwaerts auf Kapitel D und E, statt `C'` aus den vorangehenden
1989-Gleichungen herzuleiten.

Die abschliessenden Bemerkungen, Druck 20 / PDF 11, grenzen die behauptete
Erweiterung selbst ein: (B33)-(B36) seien noch nicht gut abgesichert,
`z(N)` sei unbestimmt, angeregte Spektren seien stark approximativ,
Existenzzeiten angeregter Zustaende noch nicht beschreibbar, und in (B49)/(B50)
seien frei waehlbare Parameter empirisch angepasst worden. Der Text nennt
ausserdem mehr theoretische als empirisch gefundene Anregerterme und eine
moegliche noch unbekannte Auswahlregel. Diese Aussagen betreffen vor allem
den Massen-/Anregungsblock; H007 kennzeichnet damit nicht (B59) als
Fitformel, liefert aber auch keine unabhaengige Begruendung von `eta_(2,2)`.

## 3. Die drei sichtbaren Rollen von `eta_(2,2)`

### (B47), Druck 16 / PDF 7: allgemeine Existenzzeit

In der von der Redaktion mit "nach Heim" eingeleiteten Beziehung fuer
`T-T_N` steht im Nenner sichtbar

```text
eta_(2,2) (1-sqrt(eta))^2
  (1-sqrt(eta_(1,1)))^2 (1-sqrt(eta_(1,2)))^2 .
```

Die Formel gilt dem Text nach fuer die Existenzzeit der durch (B3)
bestimmten Partikelmassen. Die Stelle nennt `eta_(2,2)` einen Faktor dieser
allgemeinen Beziehung, nicht das Label des jeweils betrachteten Teilchens.

### (B55), Druck 17 / PDF 8: Bestandteil von `b_2`

Im langen Ausdruck (B55) steht sichtbar ein Term der Form

```text
q [1 + (pi/3)(2-q) eta_(2,2)] B - (2-q)(1-q).
```

Auch hier ist `eta_(2,2)` eine feste Formelgroesse innerhalb einer allgemeinen,
anderweitig von `q` abhaengigen Funktion. Die Quelle setzt an dieser Stelle
nicht `q=2,k=2` und nennt keine entsprechende Konfiguration.

### (B59), Druck 18 / PDF 9: Alpha-Korrekturfaktor

Die Alpha-Passage beginnt:

```text
In phi und beta_(0) ist die Feinstrukturkonstante alpha enthalten.
Der in Kapitel D (Abschnitt 8) berechnete Wert ist noch mit einem
geringen Fehler behaftet. Heim gibt nun auch die genaue Formel dafuer an.
Nach Gl. 8.21/Kapitel D ist mit C -> C':
```

Es folgen sichtbar

```text
alpha sqrt(1-alpha^2) = [9 vartheta/(2 pi)^5] (1-C')       (B58)

1-C' = 1 - [(1+eta_(2,2))/(eta eta_(1,1) eta_(1,2))]
             [(1-sqrt(eta))/(1+sqrt(eta))]^2
     = K_alpha                                             (B59)
```

sowie Loesungsformel, Abkuerzung und zwei Zweige in (B60)-(B62). Damit ist
quellenklar: `eta_(2,2)` veraendert in dieser Fassung den Faktor `C'` bzw.
`K_alpha`. Als ausdrueckliche Motivation nennt die Passage nur den "geringen
Fehler" des frueheren Werts und den Ersatz `C -> C'`. Sie erklaert weder die
Herkunft des neuen Terms noch seine physikalische Bedeutung.

Der restliche Block ist ebenfalls gelesen und visuell kontrolliert. (B60)
loest das reziproke Quadrat mit
`alpha_(+-)^(-2)=D'^2[1 +- sqrt(1-4/D'^2)]/2`; (B61) setzt
`D'=(2 pi)^5/(9 vartheta K_alpha)`. (B62) druckt
`alpha_(+)=0.0072973525253328589` und
`alpha_(-)=0.999985890199089`, danach separat die gerundeten Reziproken
`137,03601` und `1,0000142`. Diese Wiedergabe bestaetigt den vollstaendigen
lokalen Formelkontext, wiederholt aber bewusst nicht die bereits vorhandene
arithmetische Konsistenzpruefung der Zweige.

Die anschliessende Aussage zum negativen Zweig - wahrscheinlich starke
Wechselwirkung aus inneren Bindungen der vier Zonen - ist ausdruecklich eine
Wahrscheinlichkeitsdeutung. Der Text fuegt hinzu, Heim habe dazu keine
weiteren Untersuchungen durchgefuehrt. Sie begruendet nicht die Wahl von
`eta_(2,2)` in (B59).

## 4. Zustandsauswahl: positiv Gefundenes und offene Verbindung

### Positiv gefunden

- H007 gebraucht die zweistellige Familie in der ausdruecklichen
  `(q,k)`-Schreibweise und verweist sie auf H006 (IX).
- Dadurch ist `eta_(2,2)` formal berechenbar und seine Verwendung keine
  Erfindung des Audit-Codes.
- H007 verwendet den Faktor in drei verschiedenen Formelzusammenhaengen.
- Druck 20 / PDF 11 sagt separat, fuer Delta-Zustaende sei `q=2` verwendet
  worden. Das ist eine ausdrueckliche Verwendung einer Ladungszahl `q=2` im
  Tabellen-/Resonanzkontext.

### Nicht gefunden bzw. nicht daraus ableitbar

- Keine der drei `eta_(2,2)`-Stellen nennt ein Teilchen oder einen Zustand
  `(q,k)=(2,2)`.
- Die Delta-Bemerkung setzt nicht zugleich `k=2` und verweist weder auf
  (B47), (B55) noch (B59). Sie schliesst die Luecke daher nicht.
- H007 zitiert in dieser Kette nicht Buch II (98a), wiederholt dessen
  spekulative Potentialauswahl nicht und erklaert weder ihre Fortgeltung
  noch ihre Abaenderung.
- Der analytische Familienwert darf daher nicht mit der Existenz einer
  realisierten Konfiguration gleichgesetzt werden.
- Umgekehrt darf die getrennte Buchbedingung (98a) nicht ohne belegte
  Versionsbruecke benutzt werden, um den sichtbar gedruckten 1989-Faktor zu
  entfernen oder die gesamte 1989-Formel zu verwerfen.

Die enge Quellenantwort lautet somit: H007 kennt `eta_(2,2)` als wiederholt
verwendete Formelkonstante. Ob dies nur eine analytische Auswertung der
`eta_(q,k)`-Familie, eine geaenderte Auswahlkonvention oder die Behauptung
einer wirklichen Konfiguration sein sollte, sagt die zugaengliche
IGW-Fassung nicht.

## 5. Offener Provenienzanschluss

Das bestehende externe Quellenreview dokumentiert bereits eine spaetere
IGW-Aussage, wonach die theoretische Entwicklung der 1989-Korrektur nicht
mitgeliefert worden sei und noch in Heims Unterlagen gesucht werden muesse.
Dieser Herausgeberbefund passt zum fehlenden Herleitungsschritt in H007, ist
aber kein Beweis, dass es im Nachlass keine Begruendung gibt.

Neu im Archiv identifizierte, originalautor-bezeichnete Scankandidaten
werden vom Hauptaudit separat geprueft. Sie wurden hier weder als Beleg noch
als negativer Befund benutzt. Erst ein Seitenvergleich mit dem berichteten
57-seitigen Text koennte klaeren, ob H007s (B59) wort-/klammergetreu ist und
ob dort eine nicht uebernommene Auswahl- oder Bedeutungsbegruendung steht.

Konkrete naechste Quellenfragen:

1. Existiert in einem autorisierten Manuskript eine Herleitung von `C'`, die
   `eta_(2,2)` einer geometrischen oder konfigurationalen Groesse zuordnet?
2. Wird dort `(q,k)=(2,2)` als realer Zustand, nur als analytischer
   Familienwert oder als globale Konstante bezeichnet?
3. Gibt es eine ausdrueckliche Versionsaussage zur Buch-II-Auswahl (98a)?
4. Welche Klammern der IGW-Fassung stammen aus den "besten Schaetzungen"?

Bis diese Fragen quellenbelegt beantwortet sind, bleibt die konservative
Lesart: Formelabhaengigkeit ja, physische Zustandsauswahl offen.

## 6. Inspektionsgrenze und Bildnachweis

Der gesamte extrahierbare Text der 11-seitigen H007-Fassung wurde zur
Navigation gelesen. Visuell geprueft wurden ganze Seiten:

- `tmp/pdfs/eta22_version/h007-01.png` - H007 Druck 10 / PDF 1,
  Titel und IGW-Provenienz;
- `tmp/pdfs/eta22_version/h007-02.png` - Druck 11 / PDF 2,
  Einleitung, Aenderungsrahmen und Ueberlieferungswarnung;
- `tmp/pdfs/eta22_version/h007-03.png` - Druck 12 / PDF 3,
  Rueckverweis auf `(IX)`;
- `tmp/pdfs/eta22_version/h007-07.png` - Druck 16 / PDF 7, (B47);
- `tmp/pdfs/eta22_version/h007-08.png` - Druck 17 / PDF 8, (B55);
- `tmp/pdfs/eta22_version/h007-09.png` - Druck 18 / PDF 9,
  (B58)-(B62) und lokale Motivation;
- `tmp/pdfs/eta22_version/h007-11.png` - Druck 20 / PDF 11,
  Unsicherheiten, Auswahlbemerkung und `q=2` fuer Delta-Zustaende.

Fuer den Rueckverweis wurden ausserdem die bereits vorhandenen Vollseitenbilder
`07_outputs/source_check_images/1982_massenformel/page-01.png`, `page-03.png`
und `page-05.png` visuell geprueft. Sie belegen H006s eigene
IGW-Provenienz, (V) und (IX).

Nicht ausgefuehrt wurden eine erneute Berechnung der alten `u_q`-Zweige,
Alpha-Fits, Makros, fremde Programme, moderne Widerlegungssuche oder eine
vollstaendige Nachlasssuche. Geaendert wurde nur diese Review-Datei.

## 7. Nachtrag: positive Autorenprovenienz aus H013/H014

Nach Abschluss der ersten H007-Gegenlesung wurden zwei eng einschlaegige
Archivscans bereitgestellt und nur an den vom Hauptaudit lokalisierten Stellen
visuell geprueft:

| ID | Lokale Quelle | Umfang und sichtbare Selbstbezeichnung |
|---|---|---|
| H013 | `01_sources/heim_primary/eta22_context/J0033-Heim_Ausgewaehlte-Ergebnisse-b.pdf` | 61 PDF-Seiten; Titelseite: *Ausgewaehlte Ergebnisse einer einheitlichen Quantenfeldtheorie der Materie und Gravitation*, `Burkhard Heim, Northeim bei Goettingen, Germany (W)` |
| H014 | `01_sources/heim_primary/eta22_context/J0032-Heim_Ausgewaehlte-Ergebnisse-a.pdf` | 50 PDF-Seiten; gleiche Titel- und Autorenzeile |

Beide sind gescannte Typoskripte und nennen Burkhard Heim direkt als Autor.
Auf den geprueften Titel- und Tabellenseiten ist kein Abfassungs- oder
Publikationsdatum sichtbar. Die PDF-Container wurden laut Metadaten im Mai
2012 erzeugt; das datiert die Digitalisierung, nicht den Text. Die Scans sind
daher eine bessere Autorenprovenienz fuer den darin sichtbaren Konstantenblock
als die spaetere IGW-Wordfassung H007, aber kein bestaetigtes Faksimile des
berichteten 1989-Manuskripts.

### Identischer Konstantenwert in beiden Anhaengen

H014 Anhang B, Druck 41 / PDF 48, und H013 Anhang B, Druck 54 / PDF 57,
beginnen mit derselben Erklaerung: Die mit `#` versehenen nummerierten
Gleichungen wuerden nach Gleichungsnummern tabelliert. In der anschliessenden
Konstantentabelle stehen jeweils sichtbar und in derselben Reihenfolge:

```text
eta         = 0,98998964
eta_(1,1)   = 0,98756399
eta_(1,2)   = 0,98516776
eta_(2,2)   = 0,84242385
```

Rechts daneben werden weitere, entsprechend indizierte Zahlen tabelliert;
darunter stehen `alpha_+` und `alpha_-`. Fuer den jetzigen Befund ist nur die
linke, eindeutig beschriftete `eta`-Spalte erforderlich. Die Tabelle ist ein
positiver Beleg, dass `eta_(2,2)` samt genau diesem Zahlenwert in einem Heim
zugeschriebenen Autoren-Typoskript als numerische Konstante vorgesehen war.
Sie ist also nicht erst als Rechenhelfer des heutigen Audits entstanden und
auch nicht nur in H007s B59-Zeile ueberliefert.

Die Tabelle bezeichnet `eta_(2,2)` jedoch nicht als Teilchen, Grundzustand
oder realisierte Konfiguration. Auf der Seite steht weder eine Auswahlregel
noch die H007-Gleichung (B59). Der Befund belegt deshalb nicht:

- dass der Tabellenwert aus einer physischen Realisierung `(q,k)=(2,2)`
  gewonnen wurde;
- dass er die Buch-II-Auswahl (98a) aufhebt oder ersetzt;
- dass H007s konkrete Alpha-Korrektur `C -> C'` oder deren Herleitung in
  diesen Scans enthalten ist;
- dass einer der beiden Scans das Original oder eine bestimmte Vorstufe des
  1989-Berichts ist.

### Konkreter Versionshinweis, keine Chronologie

H013 Druck 10 / PDF 11 enthaelt bei den mit `#` markierten Definitionen die
Fussnote:

```text
Bei # s. Anhang B S. 41
```

Im selben H013-Scan beginnt Anhang B tatsaechlich erst auf Druck 54 / PDF 57.
Anhang B beginnt dagegen in H014 genau auf Druck 41 / PDF 48. Zusammen mit
dem in beiden Fassungen gleich aufgebauten Konstantenblock ist dies ein
konkreter Text-/Versionsbezug zwischen den Scans: Eine Seitenreferenz auf 41
passt zur Paginierung von H014, waehrend sie in H013 nicht aktualisiert ist.

Daraus folgt ohne weitere Editionsbelege weder, dass H014 zwingend frueher
geschrieben wurde, noch wer welche Fassung redigierte oder ob beide direkt
vom selben Original abstammen. Der Befund erlaubt eine Versionsbeziehung,
keine bewiesene Redaktionschronologie.

### Aktualisierte enge Bilanz

```text
eta_(2,2) als Heim zugeschriebene numerische Konstante   jetzt positiv belegt
eta_(2,2) in H007 B47/B55/B59                            positiv belegt
Herleitung des H007-Korrekturfaktors B59                 weiterhin offen
realisierter Zustand (q,k)=(2,2)                         weiterhin offen
1989-Originalfaksimile / sichere Chronologie             weiterhin offen
```

Visuell gepruefte Vollseitenbilder fuer diesen Nachtrag:

- `tmp/pdfs/eta22_context/j0032-01.png` - H014 Titelseite;
- `tmp/pdfs/eta22_context/j0032-48.png` - H014 Druck 41 / PDF 48,
  Anhang-B-Tabelle;
- `tmp/pdfs/eta22_context/j0033-01.png` - H013 Titelseite;
- `tmp/pdfs/eta22_context/j0033-11.png` - H013 Druck 10 / PDF 11,
  Fussnote `Anhang B S. 41`;
- `tmp/pdfs/eta22_context/j0033-57.png` - H013 Druck 54 / PDF 57,
  Anhang-B-Tabelle.

Es erfolgte keine darueber hinausgehende Dokument-, Nachlass- oder
Literatursuche und keine erneute numerische Rekonstruktion der Formel.
