# Verstaendnisbilanz: Reichweite der 26 Befundgruppen

Stand: 2026-09-06, Etappe 15 ab `bfdb806`.
Unabhaengige logische Gegenpruefung des vollstaendigen
[Befundregisters](../FINDING_REGISTER.json), keine neue Quellenedition,
Messdatenauswertung oder Gesamtbewertung der Heim-Theorie.

## 1. Pruefgrundlage und Leseschluessel

Alle Registereintraege FIND-001 bis FIND-026 wurden einschliesslich
Voraussetzungen, Gegenstandsgrenzen und Nachweisverweisen gelesen.
Ergaenzend wurden die bestehenden Berichte ALPHA_AUDIT,
CHARGE_DERIVATION, AUTHOR_RATIONALE, CYCLIC_FLOW_AND_FINDINGS,
EXPONENTIAL_CONTEXT, DELTA_SELECTION, PHI_U_BRIDGE und GAMMA_QN
gegengeprueft, jeweils vom 2026-09-06. Die bereits erarbeiteten
mathematischen Reviews dienen als weitere lokale Nachweisspur.
Quellenlesungen werden aus diesen dokumentierten Pruefungen uebernommen;
in dieser Etappe wurden keine PDF-Seiten neu interpretiert und keine
Webquellen oder Messwerte hinzugezogen.

Die folgende Einteilung ist bewusst nicht exklusiv. Ein Quellenkonflikt
kann durch lokale Algebra bewiesen sein, ein positiver Zahlenbefund
trotzdem physikalische Annahmen voraussetzen:

- **A**: bewiesene lokale Algebra innerhalb der angegebenen Praemissen.
- **Q**: Konflikt miteinander verbundener Quellenangaben, nicht schon
  Widerspruch der gesamten Theorie.
- **B**: bedingte Bedeutungspruefung oder eigenes Diagnosemodell;
  seine Objektzuordnung ist Teil der Voraussetzung.
- **O**: offene Herleitung, Bestimmung oder Identifikation im dokumentierten
  Suchumfang; kein Nachlass-weiter Nichtexistenzbeweis.
- **V**: belegter Versions-/Darstellungsunterschied, ohne Wahl einer
  richtigen Fassung oder einer ungesicherten Chronologie.
- **P**: positive Reproduktion. Die Tabelle sagt jeweils, ob nur eine
  Quellenangabe/Definition, ein formaler Anschluss oder eine Zahl
  reproduziert wurde. Das ist keine automatische physikalische Bestaetigung.

Die Kuerzel ersetzen die `kind`-Felder des Registers nicht. Insbesondere
bedeuten weder mehrere Kuerzel noch mehrere IDs mehrere unabhaengige
Experimente. Quellhashes sichern Dateigleichheit; Tests sichern gepruefte
Implementierungseigenschaften; beides entscheidet keine physikalische Wahrheit.

## 2. Vollstaendige Zuordnung

| Befund | Belegart und getragenes Ergebnis | Voraussetzungen und kleinste Reichweite | Abhaengigkeit / spaetere Praezisierung |
| --- | --- | --- | --- |
| FIND-001 | **A, Q:** Gedruckte Alpha-Zweigpaare erfuellen die notwendige Identitaet `a_plus^2+a_minus^2=1` auch unter Druckrundung nicht. | Beide positiven Zweige derselben Gleichung mit gemeinsamem RHS; richtige Zahlenlesung und deklariertes Rundungsmodell. Widerlegt diese Paarangaben, nicht die Loesbarkeit der Gleichung. | Von der konkreten eta-/pi-/Y3-Auswertung unabhaengig. Buchfund erweitert die Quellenlokalisierung, ist keine unabhaengige Wiederholung eines Experiments. FIND-013 repariert den Paarbefund nicht. |
| FIND-002 | **A, Q:** Direkte B62-Zahlen und zugeordnete gedruckte Kehrwerte sind unvereinbar. | Derselbe positive Wert und gewoehnlicher Kehrwert, Druckintervalle. Keine historische Fehlerursache oder richtige Zahl bestimmt. | Noch weniger Formelannahmen als FIND-001; dieselben Druckdaten erzeugen aber keine statistisch unabhaengigen Tests. Bleibt bei anderer RHS erhalten. |
| FIND-003 | **P (Rechenlauf), Q:** Die festgelegten 1982/1989-Profile liefern nicht die gedruckten Alpha-Ausgaben auf deren Druckgenauigkeit. | Explizite Formel-, Index- und pi-Version, kleiner positiver Zweig und ausreichende Praezision. Keine Aussage ueber jeden denkbaren historischen Rechenweg. | Anders als FIND-001 RHS-/normalisierungsabhaengig. FIND-013 klaert die Buchindexierung; FIND-009/022 warnen vor nachtraeglicher Fassungsfusion. Naehe ist keine Reproduktion auf alle Druckstellen. |
| FIND-004 | **A, Q:** Energieintervall und Bilanz lassen zusammen nur `E_k=0, W=X=V` zu. | Gewoehnliche reelle Ordnung, identische W,V,E_k; Konflikt erst fuer den nichttrivialen Fall `E_k>0`. | Lokaler Energieordnungsbefund, unabhaengig von der Alpha-Paarrechnung. Eigene Intervallumkehr ist kein Erratum und laesst die spaetere Alpha-Gleichung bestehen. |
| FIND-005 | **A, Q, B:** Der literal gelesene Matrixblock verletzt den Orthogonalitaetsanspruch; bei beta=3/5 steht im betroffenen Block 17/8 statt 1. | Gewoehnliche komplexe Trigonometrie, Transposition statt Adjungierung, gedrucktes `tan(psi)=i*beta`, reelles `0<abs(beta)<1`. | Die andere Buchmatrix ist ein Versions-/Kontexthinweis, keine autorisierte Reparatur. Ein korrigierter Block klaerte FIND-006/007 nicht automatisch. |
| FIND-006 | **A, B:** Bei gleicher konventioneller Masse und Kinematik sind `pc` und Bewegungsenergie T sowie `h/(mc)` und `h/p` verschieden. | Gleicher Frame, `m=gamma*m0`, `p=mv`, `0<v<c`; fuer den Wellenkonflikt zusaetzlich dieselbe Welle. | Bedeutungsdiagnose, kein pauschaler Konflikt beliebiger interner Groessen. FIND-011 begrenzt die Geschwindigkeitsfrage, schliesst aber die Teilchen-/Fluss-/Phasenidentifikation nicht. |
| FIND-007 | **P (Quellenansatz), O:** H-Kreiswelle und `lambda_H=2*pi*r_H` sind gesetzt und motiviert; ein vollstaendiges zugeordnetes H-Eigenproblem ist nicht rekonstruiert. | Aussage nur ueber den geprueften Suchumfang; Motivation, Radius, Operator, Randbedingung und Modenauswahl unterscheiden. | FIND-010/011 liefern positiven Flusskontext. FIND-012 ist kein Ersatz des fehlenden Heim-Eigenproblems und keine Widerlegung eines H-s-Zustands durch eine Ringnullmode. |
| FIND-008 | **A, P (Spezialisierung), O:** `A=4*A1*A2` ist nach Einsetzen algebraisch; `A=4*C` und Y3-Festlegung tragen eigene Begruendungslast. | Buchprofil, Bedeutungen von A/C und Endwerte fixiert. `C=A1*A2, Y3=1` ist auswertbar, nicht deshalb datenunabhaengig hergeleitet. | FIND-009 verhindert Import einer anderen Integrationsfreiheit. Eigene rho/Y3-Diagnosen aus FIND-012 sind keine entdeckten Heim-Fitparameter. Kein Fit allein aus Offenheit bewiesen. |
| FIND-009 | **V, A (bedingt):** Manuskript 1981 und Buch unterscheiden A_k-Potenzen, Y/Y3 und Begruendungswortlaut. | Visuell getrennte Fassungen; algebraischer Potenzvergleich nur bei gleicher eta-Bedeutung. | Begrenzt FIND-008 und jede numerische Uebernahme. Weder spaeterer Druck noch bessere Trefferqualitaet autorisiert eine stille Korrektur. |
| FIND-010 | **P (Definition), A:** Zyklischer Fluss und `lambda=w_f/nu` sind Quellenbegriffe; `m=a*nu` liefert nur `m*lambda=a*w_f`. | Gemeinsame konstante a,w_f und positive Frequenz. Absolute Normierung und c-Geschwindigkeit folgen nicht aus Proportionalitaet allein. | Die Quelle benennt `mc*lambda=h` selbst empirisch. FIND-011 liefert eine besondere bedingte H-Bruecke, keine Widerlegung dieses begrenzten Skalierungsarguments. |
| FIND-011 | **P (Teilbruecke), B, O:** Aus H-spezifischem w=c und allgemeinem w_f=w folgt bei gleicher Objektzuordnung w_f=c. | Identitaet von H-Wellengegenstand und strukturellem Flussaggregat zusaetzlich erforderlich; Phasengeschwindigkeit bleibt separat. | Praezisiert FIND-007/010 positiv. Weder alle Kondensationstypen noch Radius-/Kreismode sind damit bestimmt. |
| FIND-012 | **A, B:** Eigene Mittelungs-, Energie-, Ringmoden- und Phasenvarianten zeigen Konsequenzen jeweils deklarierter Zusatzannahmen. | Variablen/Operatoren sind eigene Diagnosen, kein stiller Austausch von Quelleninputs und kein Zielwertfit. | Veranschaulicht FIND-006/007/008, beweist deren physikalische Gegenmodelle aber nicht. Ganze Ringmoden einschliesslich n=0 sind Aussagen ueber den eigenen S1-Operator. |
| FIND-013 | **P (Zahl und Definition), A:** I(29a) liefert `1/alpha_prime=137.0380300128048...`, passend zur dortigen Drucknaeherung; Buch-eta_qk ist lokalisiert. | Quellenkomponenten, verschiedene Mittelungen und Buchindexkonvention vorausgesetzt. Alpha_prime nicht mit dem spaeteren Alpha-Zweig verwechseln. | Schliesst eine fruehere Rekonstruktionsluecke der Buchindizes, nicht FIND-001 oder die physikalische Mittelungsbegruendung. FIND-014 untersucht den vorausgehenden Ansatz. |
| FIND-014 | **P (Definition/Ansatz), A:** k und der moegliche Ansatz `L*Delta=k` bei L=4 verbinden die konfigurative Ladungsaenderung mit eta_qk. | Ganzzahligkeit, konkreter Ansatz und Teilchenzuordnung bleiben verschiedene Voraussetzungen; k=0 nur formaler externer Familienanschluss. | Praezisiert die Herkunft von FIND-013/019. Ist selbst kein Beweis der Quantisierung und keine Bereinigung des folgenden Auswahlknotens FIND-015/016. |
| FIND-015 | **A, Q:** Unter den gedruckten Identifikationen fordert die vorgelagerte Bedingung x<D, die V/Q-Zeile x>D, die Folgerung x<B mit B<D. | Gleiche Indizes, `Q2=sqrt(eta)` ohne q, positive eta-Werte, gewoehnliche reelle Substitution. B ist staerker als die vorgelagerte Bedingung, nicht aequivalent. | Zusammenhaengender Herleitungsknoten, keine Mehrfachzaehlung seiner Vorzeichen-/Termfolgen. FIND-017/018 liefern Kontext, aber keine gefundene Index- oder Skalenreparatur. |
| FIND-016 | **P (Auswertung), A, Q:** Gedrucktes u liefert `u_2=1.963489...`, nicht `2<u_2<3`; positive ganzzahlige Paare sind nur (1,1),(1,2),(2,1),(3,1). | Woertliche B-Funktion, mathematisches pi, strikte Schranke; keine eigene Ersetzung B durch D. Beim Buchpaar (2,2) gilt B<x<D. | Numerische B-Pruefung benoetigt FIND-015 nicht als Beweis. FIND-019 liefert den spaeter gefundenen Binnenbuch-Anwendungsanker; keine neue Fehlergruppe. Globale Maxima allein widersprechen (2,2) nicht. |
| FIND-017 | **A, B, P (Asymptotik):** Das normierte skalare Abbild von (79) reproduziert den Exponenten lambda-a samt Amplitude/Rest; H geht genau fuer a>lambda gegen null. | Festes `lambda>0,a>0,-1<b<1`, r>=0; keine Rekonstruktion des metronischen Operators. Asymptotisches Abklingen nicht mit globaler Monotonie verwechseln. | Positive Aussage neben FIND-018. Verschiedene konstante Vorfaktoren sind bei bloss proportionaler Aussage/freier Amplitude nicht fuer sich ein Quellenfehler. |
| FIND-018 | **A, B, Q (bedingt):** Positive stationaere Radien allein erzwingen im selben skalaren Abbild a>lambda nicht; ein exakter Gegenzeuge besitzt zwei positive Extrema bei a<lambda. | Gewoehnliche Ableitung, explizites skalares Abbild aus FIND-017; der Gegenzeuge liegt ausserhalb der abklingenden Teilklasse. | Kein Gegenbeispiel zu FIND-017. Metronische Extremwertregel/Randbedingung bleibt offen; gedruckte Plus-/Minusnenner nicht eigenmaechtig vereinheitlichen. |
| FIND-019 | **P (Zahl und Quellenanschluss), A:** Eta22 ist definiert, numerisch/tabellarisch reproduziert und ueber die Buch-q/k-Kette einem aufgenommenen Delta++-Grundmuster zugeordnet. | Positive vierte Wurzel und festgelegte eta-Familie; tabellierte Zuordnung nicht physikalische Zustandsvalidierung. | Staerkt FIND-016 ohne nun notwendige Fassungsbruecke. B59 ist auswertbar, aber die spezielle C_prime-Struktur folgt nicht allein aus diesem Zustand; FIND-020 bleibt. Eta22 ist kein frei waehlbarer Dezimalinput bei fester Definition. |
| FIND-020 | **P (Motiv), O:** Bindungsstrukturmotiv ist vorhanden; die spezielle B59-C_prime-Form bleibt im geprueften Material ohne ausgefuehrte Herleitung. | Autorenmotiv, IGW-Wiedergabe und redaktioneller Kenntnisstand getrennt. S005 ist kein Nachweis ueber jeden unbekannten Heim-Text. | FIND-019/021 schliessen engere Provenienz-/Rollenfragen, nicht die spezielle Dynamik. Kein gesonderter Alpha-/eta22-Fit aus dieser Luecke bewiesen. |
| FIND-021 | **P (Rollen/Autorenanschluss), A, B:** Eta22 tritt invers in B47, ladungsselektiv in B55 und affin in B59 auf; H013 belegt Lebensdauerrollen direkt. | Nur explizite eta22-Vorkommen formal variieren, alle anderen Groessen fest; definierte Nenner. Bei q=0/2 verschwindet der explizite Koeffizient, nicht der ganze B55-Endterm. | Positive Erweiterung von FIND-019/020. `T-T_N=K_tau*(Y0/t+Y1)` ist eine eigene bedingte Variation; T allein im N0-Kontext. B55-Gesamtklammer und volle M/T-Rechnung bleiben getrennt. |
| FIND-022 | **V, A (Verhaeltnisse):** H007, H014 und H013 haben unterschiedliche Alpha-Korrekturvorfaktoren und unterschiedlichen Lebensdauer-Textumfang. | Fuer Quotienten dieselbe eta-Familie; verglichen werden kleine Korrekturterme, nicht prozentuale Alpha-Aenderungen. | Begrenzt FIND-003/019/020/021. Keine Chronologie, richtige Gesamtfassung oder unveraenderte 1989-Urschrift dadurch identifiziert; keine Fusion alter Rechenprofile. |
| FIND-023 | **P (Formelbruecke), A, B, O:** Explizites phi/U-Schema speist im N0-Kontext M und y/T; gemessenes M/T ist kein Argument der lokalen phi-Rechten. | F_mass/F_time und y_W/y_time trennen, feste Restparameter/definierte Nenner. B50-Vorzeichen bleibt offen; benannte Koeffizienten sind laut Autor empirisch angepasst. | Schliesst die kleinere Frage nach dem expliziten Anschluss, nicht Dynamik/Kalibrierung oder globale Kreisfreiheit. Delta-U-Test mit P=Q kann die Vorzeichen nicht unterscheiden. FIND-021 hielt M fest, diese phi-Diagnose fuehrt den direkten M-Beitrag mit. |
| FIND-024 | **V, A (isolierter Koeffizient):** H013/H007 unterscheiden Massenklammer, ersten n-Term und phi-Selektorposition; N0-phi-Koeffizient ist lokal dennoch mu*alpha_plus. | Nur verglichene Strukturen, keine Gleichheit aller Hilfsparameter. H013-phi ist bereits selektiert; kein zusaetzliches N4 auf (21b). | Zwingende Fassungsgrenze fuer jede Verwendung von FIND-023 in einem Gesamtrechner; weder numerische Massendifferenz noch Korrekturrichtung bestimmt. |
| FIND-025 | **P (offen benannte Relation), A, O:** `Q_N=Q0+2z(N)` beschraenkt Paritaet, bestimmt aber z nicht; `F(Gamma)=0` ohne F-Gesetz bestimmt Gamma nicht. | Q0-Eingaberegel, z=0-Naeherung und N0-Endpunkt trennen. z=0 macht N>0 nicht zu N0; dann bleibt im definierten H013-Zeitausdruck T=T_N unbekannt. | Der N>0-Blocker bleibt trotz FIND-023. H014s positive-z-Prosa ist passagenspezifisch. 0.1-MeV-Angabe nicht reproduziert; gezaehltes K_B samt Energieabstand ist keine Gamma-Dynamik. |
| FIND-026 | **P (Geltungsbereich), A, O:** Positive Massenfolge in (14d) betrifft stufenweise Anregung; Ein-Prozess-Kandidaten und ausgewaehlte Resonanztafeln bleiben getrennt. | Versionsgebundene Anregungsfunktion, fuer Monotonie feste Koeffizienten und angegebene Vorzeichen. Gerichtete Ungleichung ist kein Existenz- oder Ratenbeweis. | Praezisiert einen sonst zu pauschalen Ausschluss. Repariert nicht FIND-016; bestimmt nicht z/Gamma aus FIND-025. H006-N1-Ausschluss nicht auf spaetere reelle f-Funktionen uebertragen. |

## 3. Was sich durch spaetere Quellen wirklich geaendert hat

Die positive Fortschreibung darf in einem Fazit nicht hinter dem
frueheren Offenheitswortlaut verschwinden:

- **Buchindexierung und Konfiguration:** FIND-013/014 beenden die Aussage,
  eta_qk sei im Buch nicht definiert. Herkunft als Ansatz und seine
  Begruendung sind andere Fragen. FIND-019 lokalisiert auch eta22;
  FIND-016 wird durch den direkten Delta-Buchanschluss konkreter,
  nicht durch ein pauschales Uebertragen der Buchauswahl auf 1989.
- **H-Welle und Normierung:** FIND-010/011 liefern mehr als nur eine
  freie Geschwindigkeitsvermutung. Die H-spezifische c-Aussage ist
  vorhanden, aber die Gleichsetzung von Flussaggregat, Elektronenwelle
  und Phase fehlt weiterhin. FIND-008 ist eine berechenbare
  Spezialisierung, nicht eine formell unberechenbare Alpha-Gleichung.
- **Frueherer F/G-Kontext:** FIND-017 bestaetigt eine bedingte Asymptotik;
  eine beliebig absorbierbare Amplitudendifferenz wurde gerade nicht
  als eigener Fehler ausgegeben. Der Kontext hebt FIND-015/016 nicht auf.
- **Lebensdauer/Masse:** FIND-021/023 belegen direkte Autorenformeln und
  den expliziten phi-Anschluss. "Kein phi-Ausdruck vorhanden" ist damit
  ueberholt. "Vollstaendig hergeleitet, unkalibriert und eindeutig
  implementierbar" waere ebenso falsch: B50, B55 und Versionsgrenzen
  bleiben; historische Anpassung ist von Laufzeitinputs zu unterscheiden.
- **Resonanzen:** FIND-026 verhindert eine globale Nichtexistenzaussage
  aus der Stufenregel. FIND-025 bleibt offen, obwohl spaetere Texte die
  unbekannte Funktion benennen. K_B besitzt in H013 sogar einen
  Energieabstand; "keinerlei Energiebezug" waere zu stark. Eine bestimmte
  volle Gamma-Breite folgt daraus dennoch nicht.

Auch unsere eigenen Lesefehler und Implementierungsfehler muessen
abgegrenzt bleiben: Die verworfene q-Lesung von Q2 in der Auswahlstelle,
eine zeitweise vermeintlich eindeutige U-Minuslesung und behobene
Ausloeschungsfehler im eigenen Exponentialrechner sind keine
zusaetzlichen Heim-Befunde.

## 4. Welche Befunde eigenstaendig tragen

**Starke lokale Algebra ist nicht von der vollstaendigen physikalischen
Herleitung abhaengig.** FIND-001/002 benoetigen keine Auswahl einer
passenden RHS. FIND-004 hat ein anderes, enges Praemissenpaket.
FIND-005 traegt unter seinen expliziten Matrixkonventionen. Neue
Motivationsquellen allein koennen diese lokalen Unvereinbarkeiten nicht
aufheben; ein neuer Textbeleg kann aber ihre historische Einordnung
oder die richtige Lesart praezisieren.

**Getrennte Pruefungen koennen demselben Herleitungsknoten angehoeren.**
FIND-015 betrifft den Umformungsweg, FIND-016 die Auswertung der
gedruckten B-Funktion. Letztere ist auch ohne Annahme der Richtigkeit
dieses Wegs nachrechenbar. Der Delta-Anschluss aus FIND-019 ist eine
konkrete Anwendung, keine zusaetzliche unabhaengige Fehlerstatistik.
Dass (2,2) die vorgelagerte Positivitaet erfuellt, ist wesentliche
Entlastung dieser einen Stufe, keine Entlastung der gedruckten B-Zeile.

**Modell-/Bedeutungsdiagnosen bleiben bedingt.** FIND-006/012/018
brauchen die explizite Objekt- oder Skalarabbildung. Sie koennen nicht
allein die physikalische Gueltigkeit eines anderen, noch unvollstaendig
rekonstruierten Modells entscheiden. FIND-017 und FIND-018 sind deshalb
keine sich widersprechenden Resultate. Offenheiten FIND-007/008/020/025
sind weder arithmetische Fehler noch Nachweise beliebiger Fitfreiheit.

**Versions- und Positivbefunde sind eigenstaendige Sicherungen.**
FIND-009/022/024 bleiben wichtig, selbst wenn jede Fassung fuer sich
korrekt waere. FIND-013/017/019 sowie die Quellen-/Formelanschluesse
zeigen, was bereits reproduziert ist. Sie bestaetigen weder jede
Voraussetzung noch beheben sie andere Aussagen durch blosse Nachbarschaft.

Eine Gesamtrefutation wuerde zusaetzlich nachweisen muessen, dass ein
betroffener Schritt fuer eine eindeutig bestimmte Theorieversion
unverzichtbar ist, nicht als lokaler Editionsfehler isoliert werden kann
und ihre physikalische Behauptung traegt. Dieser globale
Abhaengigkeitsnachweis ist hier nicht geleistet.

## 5. Minimale Pflichten vor einem oeffentlichen Fazit

Ein enges Fazit zu den lokalen Befunden ist schon moeglich; es muss
nicht auf die Fertigstellung eines gesamten Massenrechners warten.
Dafuer genuegen aber weder die Zahl der Registereintraege noch ein
gruener Testlauf. Mindestens erforderlich sind:

1. **Gegenstand einfrieren:** Gepruefte Ausgaben/Textzeugen, Datierungs-
   und Ueberlieferungsgrenzen, konkrete Seiten und normalisierte
   Zeichen nennen. Autorentext, Redaktion und eigene Diagnosen trennen;
   keine Mischung gleich benannter Parameter verschiedener Fassungen.
2. **Jede Schlussfolgerung mit ihrem Praemissenpaket zeigen:**
   Rundungsintervalle von Messunsicherheit, Transposition von
   Adjungierung, Skalarabbildung von metronischem Operator und N0 von
   N>0 unterscheiden. Angeben, welche Aussage genau widerlegt,
   reproduziert oder nur noch nicht hergeleitet ist.
3. **Positive Fortschreibung und Abhaengigkeiten erhalten:** Die
   Praezisierungen aus Abschnitt 3 gemeinsam mit den negativen Befunden
   berichten. Keine Summe von IDs/Agentenlesungen als Beweisstaerke
   ausgeben. Eigene Fehler offen von Quellenbefunden unterscheiden.
4. **Reproduktion separat sichern:** Rechenprofile, Inputstrings,
   Softwarestand, Praezision, Tests und Quellhashpruefung dokumentieren.
   Numerische Konvergenz ist keine Intervallgarantie; der
   Registervalidator prueft nur Metadaten. Agentengegenlesungen sind
   keine externe wissenschaftliche Begutachtung.
5. **Vor einem empirischen Anspruch einen eigenen Pruefplan vorlegen:**
   Feste Version, vollstaendige Inputs/Zustandsauswahl, bekannte
   Kalibrierung und alle Kandidaten statt nur passender Tabellenzeilen
   festlegen. Der Lehrfall N=0 benoetigt nicht automatisch ein N>0-
   Gamma-Modul, umgekehrt validiert ein solcher Lehrfall keine
   Resonanzen. Ein vollstaendiger M/T-Fall braucht seine eigenen
   geklaerten Vorzeichen, Selektoren, Nenner und Abhaengigkeiten.
6. **Korrekturen nur belegt oder als eigene Variante behandeln:**
   B durch D, pc durch T, eine Alpha-Fassung durch eine andere oder
   ein U-Vorzeichen nach Trefferqualitaet zu ersetzen ist keine
   wortgetreue Rekonstruktion. Offene Punkte nur mit konkret neuer
   Evidenz wieder oeffnen; Suchumfang nicht zum Nachlass-Gesamturteil
   aufblasen.

Kurzfazit: Ein nachvollziehbarer Teil der Rechen- und Quellenstruktur
ist erschlossen, einige lokale Angaben sind unter expliziten
Voraussetzungen unvereinbar, und mehrere physikalische Verbindungen
bleiben offen. Das ist eine belastbare begrenzte Verstaendnisbilanz,
kein Score fuer oder gegen die gesamte Theorie.

## 6. Pruefstatus dieser Review

Nur diese Reviewdatei wurde neu angelegt. Keine alten Rechner, Inputs,
Snapshots, Tests, Normalisierungen oder Registereintraege wurden
geaendert; keine neue numerische Physikrechnung und kein Commit.
Die ID-Abdeckung wurde gegen das Register geprueft: alle 26 IDs stehen
genau einmal als Tabellenzeile, keine fehlt oder ist zusaetzlich.
`git diff --check` blieb ohne Beanstandung. Dies ist eine redaktionelle
Vollstaendigkeitskontrolle, keine erneute Wahrheitspruefung aller
Quellenbefunde.
