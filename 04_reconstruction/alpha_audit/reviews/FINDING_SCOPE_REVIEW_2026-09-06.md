# Reichweitenreview der bisherigen Befunde

Stand: 2026-09-06. Unabhaengige logische Review fuer eine nachvollziehbare
Befundbilanz. Gelesen wurden die Berichte `ALPHA_AUDIT`,
`CHARGE_DERIVATION`, `AUTHOR_RATIONALE`, `WAVE_CLOSURE` vom 2026-09-06 sowie
`BOOK_ENERGY_ORDER_ISSUE.md` und `BOOK_LORENTZ_MATRIX_ISSUE.md`.

Diese Review prueft die logischen Folgerungen aus den dort dokumentierten
Quellenlesungen und Rechnungen. Sie wiederholt keine Glyphenkontrolle,
erhebt keine neuen Messdaten und prueft keine vollstaendige Theorie gegen
Experimente. Die vorhandenen modernen Vergleichsdaten des ersten Audits
werden fuer die folgenden internen Befunde nicht benoetigt.

## Grundregel fuer die Bilanz

Jeder Eintrag sollte getrennt angeben: Quellenfassung und Fundstelle,
gleichzeitig angenommene Aussagen, notwendige Lesekonventionen,
Nachweis, kleinste betroffene Behauptung und ausgeschlossene weitergehende
Schluesse. Ein mathematischer Widerspruch widerlegt die gleichzeitige
Gueltigkeit seines Praemissenpakets. Er identifiziert nicht automatisch
die zu korrigierende einzelne Praemisse oder den Umfang aller davon
abhaengigen physikalischen Aussagen.

Insbesondere sind diese Kategorien nicht austauschbar:

- gedruckte Zahlen, die ihre behauptete Beziehung nicht erfuellen;
- lokal unvereinbare Gleichungen/Ungleichungen einer konkreten Fassung;
- ein Widerspruch unter ausdruecklichen mathematischen Lesekonventionen;
- eine definierte, aber nicht aus frueheren Annahmen hergeleitete Setzung;
- ein innerhalb der rekonstruierten Kette noch nicht bestimmter Wert;
- eine eigene Zusatzkonstruktion und ihre bedingten Folgen;
- ein experimentelles Scheitern einer hinreichend bestimmten Modellfassung.

Die letzte Kategorie folgt aus keiner der untenstehenden Rechnungen.

## 1. Gedruckte Alpha-Paare: interner Zahlenbefund

Beleg: `06_docs/ALPHA_AUDIT_2026-09-06.md:30` und `:58`.

Fuer die Paarpruefung muessen gleichzeitig gelten:

1. Die beiden Zahlen sind die beiden positiven reellen Zweige derselben
   Gleichung `a sqrt(1-a^2)=R`, mit derselben rechten Seite R und der
   nichtnegativen reellen Quadratwurzel.
2. Die Zahlen beziehen sich auf dieselbe Modellfassung/Spezialisierung;
   ein gemeinsames Y3 gehoert entsprechend zu demselben R.
3. Die Werte und ihre direkte bzw. reziproke Bedeutung wurden korrekt
   gelesen. Die zugelassenen Druckintervalle sind die dokumentierten
   geschlossenen Halb-Letztstellenintervalle fuer Rundung zur naechsten
   Stelle; sie sind keine Messunsicherheiten.

Dann ist `a_plus^2+a_minus^2=1` notwendig. Die drei geprueften gedruckten
Paare verletzen diese Bedingung auch innerhalb ihrer Druckintervalle.
Dieses Ergebnis benoetigt weder eine Wahl von pi/eta noch Messdaten.
Eine Aenderung eines gemeinsamen Y3 kann es nicht beheben. Zweigabhaengige
rechte Seiten waeren eine andere Voraussetzung, nicht eine Reparatur
innerhalb dieser Paarpruefung.

Die beiden B62-Kehrwertpruefungen brauchen noch weniger: Jede direkte
Zahl und der ihr zugeordnete Kehrwert muessen denselben positiven Wert
bezeichnen und die dokumentierten Rundungsintervalle respektieren. Die
Intervalle fuer diese beiden Darstellungen ueberlappen nicht.

Zulaessige Aussage: Die angegebenen Paare bzw. direkten/reziproken
Darstellungen koennen nicht alle ihre gedruckte Bedeutung und Genauigkeit
unter diesen Bedingungen besitzen. Das Problem ist teilweise im Buchscan
selbst belegt und nicht erst durch die aktuelle OCR entstanden.

Nicht zulaessig: Die Zweiggleichung habe keine Loesungen; jeder moegliche
Heim-Ansatz sei falsch; der Autor habe absichtlich getaeuscht; ein
bestimmtes historisches Rechenverfahren sei bewiesen; fuenf Beziehungen
seien fuenf unabhaengige Experimente. Die Gleichung kann korrekt loesbar
sein und dennoch mit falschen Druckwerten versehen worden sein.

Abweichungen zwischen ausgewerteten Formelversionen und gedruckten
Einzelzahlen sind gesondert zu registrieren: Sie setzen zusaetzlich die
jeweilige Index-, Konstanten- und Versionswahl voraus. Der unabhängige
Paarwiderspruch darf dadurch nicht mit einem profilabhaengigen Residuum
vermischt werden. Die spaeter geklaerte Buchindexierung macht die alte
IGW-lokale Indexvariante nicht nachtraeglich zur woertlichen IGW-Lesung.

## 2. Energieintervall: lokaler algebraischer Widerspruch

Beleg: `04_reconstruction/alpha_audit/BOOK_ENERGY_ORDER_ISSUE.md:12`.

Das minimale Praemissenpaket lautet: W,X,V sind dieselben geordneten
reellen Energiegroessen im betrachteten Fall; `W<=X<=V`; `E_k>=0`; und
`-E_k=V-W`. Daraus folgt zwingend

```text
E_k=0, W=X=V.
```

Mit dem zusaetzlichen `0<=E<=E_k` folgt auch E=0. Erst die weitere
Anforderung eines nichttrivialen positiven E_k macht das Paket
widerspruechlich. V<0, C und eine spezifische Alpha-Zahl sind fuer diesen
Minimalbeweis nicht erforderlich. Bei V ungleich null und W=VC ergibt
die Degeneration zusaetzlich C=1.

Die umgekehrt orientierte Integration ist fuer sich nicht fehlerhaft:
`integral_W^V dX=V-W` kann negativ sein. Der Konflikt liegt in ihrer
Verbindung mit der gedruckten numerischen Ordnung und positivem E_k.

Zulaessige Aussage: Diese gedruckten Aussagen tragen gemeinsam keinen
positiven Energieanteil. Derselbe Befund in der datierten Manuskriptfassung
lokalisiert eine wiederkehrende Lesung, beweist aber keine bestimmte
Entstehungsursache oder eine erst in der Buchausgabe entstandene Druckpanne.

Nicht zulaessig: Die Umkehr `V<=X<=W` sei gesicherte Autorenabsicht; die
Alpha-Zweiggleichung sei dadurch allein widerlegt; ihre Druckpaare seien
damit repariert; jede spaetere korrigierte Fassung sei ausgeschlossen.
Die dokumentierte eigene Ordnungsvariante belaesst die nachfolgend
benutzte Beziehung `E_k=-V(1-C)` und damit deren bisherige rechnerische
Weiterverwendung unveraendert. Sie liefert keine physikalische Begruendung
der Energie-, Korrelations- oder Wellenannahmen.

## 3. A-minus-Matrix: bedingter lokaler Formelwiderspruch

Beleg: `04_reconstruction/alpha_audit/BOOK_LORENTZ_MATRIX_ISSUE.md:12`.

Gleichzeitig vorausgesetzt werden der visuell gelesene Block
`[[cos psi,i sin psi],[-i sin psi,cos psi]]`, `tan psi=i beta`,
gewoehnliche analytische komplexe Trigonometrie, `i^2=-1`, gewoehnliche
Matrixtransposition und reelles `0<|beta|<1`. Dann gilt

```text
A_block A_block^T = [(1+beta^2)/(1-beta^2)] I2 != I2.
```

Damit kann die gedruckte Orthogonalitaetsbehauptung unter genau diesen
Bedingungen nicht gelten. Bei beta 3/5 lautet das volle Produkt im
angegebenen vierdimensionalen Kontext `diag(17/8,1,1,17/8)`, nicht
`(17/8) I4`. Bei beta null verschwindet der Konflikt.

Zulaessige Aussage: Ein konkretes Praemissenpaket aus Block, Winkelrelation,
Produktkonvention und Orthogonalitaetsanspruch ist unvereinbar. Der
Nachweis erfolgt in der eigenen Quellenbasis, nicht durch blossen
Eintragsvergleich mit einer Standardmatrix in einer anderen Basis.

Nicht zulaessig: Jede Bedeutung von A-minus sei widerlegt; komplexe
Orthogonalitaet und Unitaritaet seien identisch; das Entfernen der i-Faktoren
sei ein verifiziertes Erratum; die anders kontextualisierte R6-Matrix von
p56 sei dieselbe Matrix oder eine autorisierte Korrektur. Die begrenzte
Suche nach alternativen Konventionen ist kein Nachweis ihrer Abwesenheit
in jedem unveroeffentlichten Text. Eine korrigierte Matrix wuerde auch
noch nicht die Verwendung von pc in der konkreten Energiebilanz begruenden.

## 4. Komponenten, C/Y3 und Wellenannahmen: Spezifikation versus Herleitung

Belege: `06_docs/CHARGE_DERIVATION_2026-09-06.md:63`, `:78`, `:95`, `:224`;
`06_docs/AUTHOR_RATIONALE_2026-09-06.md:64`;
`06_docs/WAVE_CLOSURE_2026-09-06.md:28` und `:187`.

Die Komponenten, gleiche Ladungsmittelung und gleiche Energiemittelung
bestimmen unter den angegebenen Definitionen eine berechenbare lokale
Alpha-prime-Naeherung. Deren erfolgreiche Reproduktion von 137,038 ist
ein positiver arithmetischer Befund. Sie beweist nicht die physikalische
Identifikation der Komponenten, Quotienten oder Mittelungen.

Entsprechend ist `A=4 A1 A2` aus der dokumentierten lokalen Integration
zu unterscheiden von der zusaetzlichen Verknuepfung `A=4C`. Beide Faktoren
vier koennen algebraisch zusammenpassen, ohne dass ihre physikalische
Zuordnung daraus erzwungen wird. Fuer einen festgelegten Buchfall Y3=1
ist die spaetere rechte Seite numerisch berechenbar. Die allgemeine
unabhaengige Festlegung bzw. Begruendung von C/Y3 bleibt eine andere Frage.

Die Begriffe "unterbestimmt" und "nicht hergeleitet" sind hier genau zu
verwenden. Eine ausdrueckliche Setzung kann eine Modellfassung numerisch
vollstaendig spezifizieren, obwohl sie nicht aus frueheren Praemissen
folgt. Fehlende Begruendung bedeutet daher nicht automatisch fehlende
Berechenbarkeit oder einen bewiesenen freien Fitparameter. Ebenso darf
eine inzwischen gefundene Buchdefinition von eta_1k nicht weiter als bei
Heim fehlende Definition bezeichnet werden.

Eigene Familien mit Mittelungsgewicht, rho, Ringmode N oder Phase zeta
zeigen die Konsequenzen geaenderter Annahmen. Sie sind keine unveraenderten
Modelle der vollstaendigen Quelle, wenn sie deren explizite Setzungen
ersetzen. Zulaessig ist etwa: Einheiten allein waehlen die gleiche
Gewichtung nicht; Periodizitaet allein waehlt N=1 nicht. Nicht zulaessig
ist daraus: Heim habe genau diese zusaetzlichen freien Parameter besessen,
oder jede dieser Ersetzungen sei eine physikalisch zulaessige Reparatur.

Die neue eigene Familie `C_eff=rho P Y3` bestimmt bei bekanntem P und
alpha_prime nur das Produkt rho Y3. Sie darf weder als Quellendefinition
von C noch als Gleichsetzung der Manuskript- und Buch-Ak ausgegeben
werden. K bleibt `alpha_prime(1-rho P Y3)`, keine reine Multiplikation
des ganzen K mit Y3.

## 5. Begriffsvergleiche und Gegenbeispiele: ihre notwendigen Bruecken

Die Unterschiede pc/T und h/(mc) zu h/p setzen dieselben jeweiligen
Massen-, Geschwindigkeits-, Energie- und Bezugssystemdefinitionen voraus.
Mit `m=gamma m0`, `p=mv` sind pc und `T=(m-m0)c^2` verschiedene Funktionen.
Das begruendet einen Vergleich, aber noch keine Zuschreibung, der Autor
habe beide bewusst als dieselbe Groesse definiert. Fuer einen behaupteten
Wellenwiderspruch muessen zudem dieselbe Welle und dieselbe Impulsbedeutung
gemeint sein. Verschiedene Wellenkontexte koennen beide Formeln enthalten.

Der exakte Standardboost zeigt, dass gewoehnliches pc kein skalarer
Zahleninvariant ist; er widerlegt nicht die Aussage, eine Gleichung
behalte ihre Form. Das statische Kreisbeispiel widerlegt die universelle
Behauptung, ein Lorentzboost allein liefere fuer jeden Kreis L/gamma.
Es bestimmt keine rotierende oder strukturelle Heimschale, deren
Weltlinien und Gleichzeitigkeit nicht festgelegt sind.

Die eigene periodische S1-Aufgabe beweist ihr eigenes Modenspektrum.
Sie beweist weder einen Wasserstoff-Hamiltonoperator noch einen
Widerspruch des s-Grundzustands. Die gleiche-Welle-Diagnose mit
`E_tot=h nu=mc^2` und `abs(p_wave)=h/lambda=beta mc` erzwingt zeta=1/beta
nur unter diesen ausdruecklichen Identifikationen. Die daraus neu
berechneten Beta-Werte sind Folgen dieser Zusatzkonstruktion, keine
experimentell ausgeschlossenen oder bestaetigten Alpha-Vorhersagen.

Motivation durch eine bereits bekannte Naeherungsabweichung ist ein
positiver Quellenbefund, aber fuer sich weder ein Nachweis eines
ausgefuehrten Parameterfits noch einer unabhaengigen Vorhersage. Die
1981-Datierung der gefundenen Fassung stuetzt eine entsprechende
zeitliche Einordnung des Dokuments; sie beweist nicht Erstprioritaet,
lueckenlose Ueberlieferung oder die Echtheit jeder Zuschreibung.

## 6. Zyklischer Fluss: was aus den vorgegebenen Relationen folgt

Diese zusaetzliche Pruefung ist rein bedingt, ohne neue Glyphenbehauptung.
Angenommen seien fuer eine betrachtete Familie dieselben positiven
Konstanten a und w sowie positive Frequenzen nu:

```text
m(nu) = a nu,
lambda(nu) = w/nu,
w konstant.
```

Dann folgt exakt

```text
m(nu) lambda(nu) = a w.
```

Die Dimensionen sind konsistent: a hat die Einheit kg s, w hat m/s,
also a w die Einheit kg m, ebenso wie h/c. Gleiche Dimension ist aber
keine Festlegung eines Wertes. Falls a oder w zwischen den betrachteten
Zustaenden wechseln duerften, waere selbst die familienweite Konstanz
eine weitere Annahme; sie folgt hier aus den ausdruecklich gemeinsamen
Konstanten.

Eine Gegenbeispielfamilie zeigt die fehlende Normierung: Waehle beliebige
a0,w0>0 und beliebiges t>0. Dann erfuellen

```text
m_t(nu) = t a0 nu,
lambda_t(nu) = w0/nu
```

saemtliche vorstehenden Relationen, aber ihr Produkt ist `t a0 w0`.
Die Praemissen bestimmen daher nicht speziell h/c. Zyklizitaet oder
Periodizitaet liefert ohne weitere Dynamik ebenfalls keine Normierung
von a oder w.

Sogar die zusaetzliche Forderung `m lambda=h/c` wuerde nur `a w=h/c`
festlegen. Fuer jedes positive w ist `a=h/(c w)` moeglich. Insbesondere
`w=2c`, `a=h/(2c^2)` erfuellt dasselbe Produkt, ohne w=c zu setzen.
Dieses Gegenbeispiel respektiert auch eine zusaetzliche Schranke w>=c;
es behauptet keine spezielle Wasserstoffbedingung der Quelle.
Die Auswahl `w=c` und `a=h/c^2` benoetigt deshalb weitere Aussagen;
sie darf nicht allein aus der Produktformel herausgelesen werden.

Ebenso kommt r_H in den Ausgangsrelationen nicht vor. Ohne zusaetzliche
Zuordnung kann sein Wert unabhaengig gewaehlt werden. Eine Relation
`lambda=2 pi r_H` benoetigt die passende geometrische Kreisform, dieselbe
Laengengroesse, Frequenz-/Umlaufbedeutung und gegebenenfalls die Auswahl
einer Wellenlaenge pro Umfang. Wenn eine Quelle lambda stattdessen als
Aggregatdurchmesser bezeichnet, ist die Verbindung zu einem H-Meridian
erst recht eigens nachzuweisen. Zyklischer interner Fluss ist nicht
automatisch dieselbe laufende Phasenwelle des gebundenen Elektrons.

Falls eine konkrete Quelle `mc lambda=h` ausdruecklich als empirischen
Quantendualismus einsetzt, ist die Normierung damit als zusaetzliche
Praemisse vorhanden. Sie darf dann weder als fehlend geleugnet noch als
aus den zwei vorstehenden Frequenzrelationen hergeleitet dargestellt
werden. Genau diese Trennung macht eine faire Befundbilanz moeglich.

## Abschliessende Empfehlung fuer das Register

Die drei lokalen Konflikte sollten als getrennte kleine Praemissenpakete
erscheinen. Die nachvollziehbare Alpha-prime-Reproduktion und inzwischen
geklaerte Buchindexierung gehoeren ebenfalls in die Bilanz. Offene
Begruendungen muessen die gepruefte Quellenabdeckung nennen; negative
Suchbefunde sind keine Nachlass-weiten Nichtexistenzbeweise.

Eigene Korrekturkandidaten sind Varianten mit Autorenstatus "Review",
nicht Quellenlesungen. Ob ein lokaler Konflikt einen bestimmten
nachfolgenden Modellanspruch trifft, verlangt eine dokumentierte
Abhaengigkeitspruefung. Ein Ziel "die ganze Theorie widerlegen" darf
diese Reichweite nicht vorwegnehmen.

Bis zu dieser Erstfassung wurde nur diese Reviewdatei erstellt. Die
anschliessend ausdruecklich beauftragte Metadatenimplementierung folgt
im nachstehenden Nachtrag; Quellen und physikalische Rechner wurden
weiterhin nicht geaendert.

## Nachtrag: Register, Bericht und Metadatenpruefung

Gegengelesen wurden die neue Datei
`04_reconstruction/alpha_audit/FINDING_REGISTER.json` mit FIND-001 bis
FIND-013 und `06_docs/CYCLIC_FLOW_AND_FINDINGS_2026-09-06.md` sowie die
zugehoerigen Quellenreviews `CYCLIC_FLOW_SOURCE_REVIEW_2026-09-06.md`
und `CORRELATION_CLOSURE_SOURCE_REVIEW_2026-09-06.md`. Die dort berichteten
Glyphenpruefungen wurden nicht durch eigene neue Bildkontrollen ersetzt.

### Ergebnis der logischen Gegenlesung

Kein offener mathematischer Reichweitendefekt in diesen Register- und
Berichtsformulierungen gefunden. Insbesondere bleiben folgende Grenzen
sichtbar:

- FIND-001/002 trennen die notwendigen Paar- bzw. Kehrwertbeziehungen von
  profilabhaengiger Formelauswertung in FIND-003. Ihre Anzahl wird nicht
  als Anzahl unabhaengiger Experimente ausgegeben.
- FIND-004 nennt den zusaetzlich vorausgesetzten nichttrivialen Fall;
  FIND-005 nennt Trigonometrie und Transposition und gibt das volle
  vierdimensionale Matrixprodukt korrekt an.
- FIND-006 ist ausdruecklich ein bedingter Bedeutungsvergleich bei
  gemeinsamen Massen-, Impuls- und Frame-Definitionen, keine automatische
  Zuschreibung gleicher physikalischer Bedeutungen an alle Quellensymbole.
- FIND-007/008 beschraenken Nichtfund-Aussagen auf die gepruefte Kette.
  Die numerisch festgelegte Buchspezialisierung wird nicht wegen fehlender
  unabhaengiger Herleitung als unberechenbar oder als bewiesener Fit
  bezeichnet.
- FIND-009 wahrt die Manuskript-/Buchtrennung. FIND-010 anerkennt den
  ausdruecklich empirischen Normierungsinput, statt ihn als verschwiegen
  oder aus der Proportionalitaet bewiesen darzustellen.
- FIND-011 erhaelt den neuen positiven Quellenbefund: Aus `w_f=w` und
  H-spezifischem `w=c` folgt `w_f=c`, wenn wirklich dasselbe Flussobjekt
  gemeint ist. Die Objektidentifikation und insbesondere eine Bedeutung
  als Phasengeschwindigkeit bleiben offen. Weder das Quellen-w noch
  seine Schranke werden mit dem Teilchen-v_H gleichgesetzt.
- FIND-012 kennzeichnet eigene Diagnosen; FIND-013 erhaelt positive
  Arithmetik und die inzwischen gefundene Buchindexdefinition. Der
  Bericht grenzt Agentengegenpruefungen von externer wissenschaftlicher
  Begutachtung ab.

Das Gegenbeispiel im Abschnitt 6 wurde auf `w=2c`, `a=h/(2c^2)` umgestellt.
Es erfuellt `aw=h/c` und die zusaetzliche allgemeine Schranke `w>=c`.
Es ist weiterhin nur ein Gegenbeispiel zur Folgerung aus den isolierten
Proportionalitaeten, nicht zur zusaetzlichen H-Stabilitaetsvoraussetzung.
Der neue Bericht formuliert dieselbe Einschraenkung ausdruecklich.

### Implementierter Metadatenvalidator

Auf gesonderten Auftrag wurden ausschliesslich
`scripts/validate_finding_register.py` und `tests/test_finding_register.py`
zusaetzlich zu dieser eigenen Reviewdatei erstellt. Die Implementierung
verwendet nur die Python-Standardbibliothek und liest feste Registerpfade.
Ihre `reproduction`-Felder und Evidenzdateien werden nicht ausgefuehrt.

Geprueft werden das exakte Objekt-/Zeilenschema, Schema-Version 1 ohne
boolesche Ersatzwerte, echte ISO-Kalenderdaten, nichtleere Text-/Listenfelder,
eindeutige formatierte Befund-IDs, erlaubte Kategorien sowie Quell-IDs aus
der ersten Spalte des vorhandenen Quellenregisters. Doppelte JSON-Schluessel
werden beim Einlesen abgelehnt, nicht still ueberschrieben.

Evidenzpfade duerfen nicht absolut sein und weder `..`-Komponenten,
Backslashes, Doppelpunkte noch NUL enthalten. Nach Pfadauflosung muessen
sie innerhalb des aufgeloesten Repository-Roots liegen und existierende
Dateien sein. Der Root-Ausbruchstest simuliert einen extern aufgeloesten
Link ohne Betriebssystem-Symlinkberechtigungen; ein realer Windows-Junction-
Integrationstest wurde nicht durchgefuehrt. Dies ist keine allgemeine
Sicherheitsgarantie fuer gleichzeitig von anderen Prozessen veraenderte
Dateisysteme. Die Funktion prueft zum Laufzeitpunkt Metadaten und liest
keinen behaupteten wissenschaftlichen Nachweis aus den Evidenzinhalten.

Die CLI sagt in Erfolg und Fehlerfall ausdruecklich, dass es keine
Wahrheitspruefung ist. Sie prueft insbesondere weder Quellenzitate noch
Algebra, Seitenangaben, Hashes oder die inhaltliche Gueltigkeit der Claims.
Diese Aspekte bleiben Gegenstand der getrennten Fach-/Quellenreviews.

### Ausgefuehrte Pruefungen

```text
python -B scripts/validate_finding_register.py
  OK: Metadatenintegritaet bestaetigt; keine Wahrheitspruefung der Befunde.
python -B -m unittest discover -s tests -p test_finding_register.py -v
  8 Tests bestanden, einschliesslich realem Register und Negativfixtures.
python -B -m unittest discover -s tests -q
  77 Tests bestanden.
git diff --check
  keine Ausgabe, Exitcode 0.
```

Die acht Metadatentests wurden zusammen mit diesem neuen Validator
geschrieben; sie sind keine unabhaengige zweite Implementierung seiner
Pruefregeln. Die logische Gegenlesung des vom Hauptagenten erstellten
Registers und Berichts ist davon getrennt. Keine anderen Dateien durch
diesen Reviewauftrag geaendert, keine Commits oder Quellkorrekturen.
