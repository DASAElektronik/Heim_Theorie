# Quellenkontext: Gamma, Q(N) und die Grenze der stationaeren Rechnung

Stand: 2026-09-06. Etappe14, Ausgang e2f9cfe, Plancheckpoint8655909.
Root-Lesenotiz; Manuskript-/IGW-Einzelheiten in den drei GAMMA_QN-Reviews.
Kein Anspruch einer vollstaendigen Nachlasssichtung.

## Identitaet und Pruefumfang

SHA256 dieser fuenf lokalen Quellen in dieser Etappe erneut geprueft.
Dateien relativ zu01_sources/heim_primary/:

| ID | Datei | SHA256 |
| --- | --- | --- |
| H004 | Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf | F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849 |
| H006 | Massenformel_nach_B_Heim_1982.pdf | F74DA0DAC8496BCD01226F54D88598152D67E1C954943AF61D0EC1811F5527BE |
| H007 | Erweiterte_Massenformel_Nach_Heim_1989.pdf | 0E2F646D784152FB008944F58E1B8E709A416B65265D2FB75D3CC44C88FF8A40 |
| H013 | eta22_context/J0033-Heim_Ausgewaehlte-Ergebnisse-b.pdf | 50EDCEE25B22B8E098DE27A8FC980B0EA6F887D424AB7FF2D28395D31F8F6045 |
| H014 | eta22_context/J0032-Heim_Ausgewaehlte-Ergebnisse-a.pdf | 24D143DCD97A80056CE2ABB42A39A1FC4377F540F22876D51BE3FB61E6C6BBFE |

Herkunft unter01_sources/source_register.md. H007 ausserdem mit dem
Webwerkzeug unter dem registrierten IGW-Kapitel-F-Link geoeffnet:
https://heim-theory.com/wp-content/uploads/2026/03/F_Erweiterte_Massenformel_nach_Heim-1989.pdf
Das ist historische Quellenkontrolle, keine neue empirische Bewertung.
H006 ist1982-Material in IGW-Wiedergabe2002/2003, H007 eine Redaktion
nach einem1989-Manuskript. H013/H014 bleiben undatiert; keine Reihenfolge
aus a/b, PDF-Metadaten oder2026-Uploadpfaden ableiten.

## 1. Der Autor benennt im Buch den fehlenden Schritt

Root hat jeweils die komplette relevante Seite visuell gelesen:

| H004 Druckseite | PDF-Seite | Gelesener Zusammenhang |
| --- | --- | --- |
| Einfuehrung3 |14| N0-Existenzzeitheuristik, allgemeine Bandbreiten und Spinmomente noch offen |
|327/328|333/334| Ganzzahlige Zonenbandbreite beta_j, Umstrukturierung und endliche Grenzen(107a) |
|347/348|353/354| Restanregungsenergie(113c), Spin-/Ladungsaenderung und explizites(114) |
|349/350|355/356| Nichtmonotone Massenfolge, Stufenabbrueche, Emissionsbedingung(116) |
|364/365/366|370/371/372| Kompetenzbereich/Ausblick, stationaere Einschraenkung, unbekannte Breiten und Bildungswahrscheinlichkeiten |

Arbeitsrender: tmp/pdfs/gamma_qn/edm2-*.png sowie vorhandenes
tmp/pdfs/eta22_roles/edm2-014.png. OCR nur zur Navigation verwendet.

Druck347 nennt Q(N) ausdruecklich die verdoppelte Spinquantenzahl
des angeregten Zustandes. Heim erwaegt, dass Energie nicht nur die
Zonenbesetzungen n_j, sondern auch Spin und elektrisches Ladungsfeld
aendern koennte. Welche Aenderung auftritt, ordnet er den noch zu
untersuchenden Symmetrieverhaeltnissen der Zustandsbildung zu.

Druck348 schreibt(114):

```text
Q(N)=Q+Z(N),   Q(0)=Q,   Z(0)=0,
q_x(N) != q_x(0)=q_x.
```

Direkt darunter werden die Verlaeufe Z(N) und q_x(N) als unbekannt
bezeichnet. Das Zeichen in der zweiten Zeile ist UNGLEICH, kein Plus!
OCR suggeriert eine falsche additive Ladungsregel. Die Zeile beschreibt
eine moegliche Ladungsaenderung; kein fuer N=0 zu forderndes Ungleichsein.
Grosses Z im Buch ist nicht ohne Bedeutungsabgleich gleich2z ausH007.
Auch nicht mit Z=k+P+Q+kappa aus dem phi/U-Block gleichsetzen.

Der folgende Buchabsatz reduziert die im Massenalgorithmus benutzten
Grundmustergroessen auf k,P,epsilon und fuegt die N-abhaengigen
Besetzungen zur Stratonmatrix hinzu. Diese Reduktion bestimmt nicht die
unmittelbar zuvor ausdruecklich unbekannt gelassenen Verlaeufe. Eine
Berechnung mit Grundmusterparametern ist von der Vorhersage aller
Eigenschaften eines tatsaechlich angeregten Teilchens zu unterscheiden.

## 2. Warum Heim trotzdem Massen berechnen wollte

Einfuehrung3 nennt den stationaeren Zustand eines dynamischen
Gleichgewichts und eine heuristische Existenzzeitbeziehung nur fuer N=0.
Eine einheitliche Beziehung fuer volle Bandbreiten und magnetische
Spinmomente setzt nach dem Autor Kenntnis von Q(N) voraus und bleibt
einer spaeteren Untersuchung vorbehalten.

Druck365 wiederholt diese Grenze am Ende des Buches: Die Massenbeziehung
(112) gilt im stationaeren Ansatz mit konstantem Realteil der
Ausgangsbeziehung. Eine entsprechende allgemeine Bandbreitenbeziehung
und die Abhaengigkeiten(114) fehlen noch. Erst danach soll die
Beschreibung von Spinmomenten/Wechselwirkungen versucht werden.

Eigene Einordnung: Eine stationaere interne Rechnung kann einen
Massenwert liefern, ohne bereits die zeitabhaengige Entstehung und
den Zerfall desselben Zustandes zu bestimmen. Das erklaert die
Arbeitsteilung des Ansatzes; es beweist weder seine Richtigkeit noch
die spaetere Loesbarkeit. Stationaer ist hier kein Beleg fuer eine
unendliche Lebensdauer. Die Quelle beansprucht selbst keinen solchen
Schluss fuer ihre gesamte N=0-Klasse.

Druck365/366 spricht auch ueber mehr berechenbare Massenterme als
damals beobachtete Teilchen und vermutet unterschiedliche
Bildungswahrscheinlichkeiten. Das ist eine Autorenhypothese, kein
bereits berechneter Nachweis- oder Produktionsmechanismus. Die
historischen Quark-/Praeonenbehauptungen auf diesen Vollseiten wurden
hier nicht empirisch geprueft und werden nicht als heutige Tatsachen
uebernommen.

## 3. Verschiedene Bedeutungen von Bandbreite und Zeit

Druck327/328 definiert beta_j als ganze Zahl verfuegbarer
Zonenanregungsstufen. Bei Ausschoepfung beschreibt(107a) einen
Besetzungszusammenbruch und eine Erhoehung der inneren Zone. Druck347
verwendet verbliebene beta_j>0 fuer eine noch moegliche Restenergie
(M_max-M_L)c^2. Weder Zahl noch Restenergie sind dort als die volle
Bandbreite Gamma ausH006 definiert.

Ebenso ist H007(B39) K_B eine ganze Zahl moeglicher Externfeldanregungen.
Die Gleichheit beta_j=K_B=Gamma waere eine unbelegte Gleichsetzung
verschiedener Groessen. Anzahl, maximale Resonanzordnung, Energieabstand
und spektrale Breite benoetigen jeweils ihre eigene Objekt-/Einheitenbruecke.

Druck349 stellt ausserdem ausdruecklich klar: f(N) steigt an, M(N)
nicht allgemein. M beschreibt stueckweise ansteigende Aeste mit
Stufenabbruechen. Druck350(116) diskutiert eine dabei moegliche
Photonenemission; keine allgemeine Lebensdauerformel. Das dortige T
ist die Dauer des Resonanzprozesses, waehrend M(N) entsteht, nicht
automatisch T_N aus dem spaeteren Existenzzeitabschnitt.

## 4. Gegenlesung der IGW-Seiten

Root hat H006 PDF8/9/10 und H007 PDF5/6/11 vollstaendig visuell
gegengelesen. H006(XXV) hat sqrt(N(N-2)) und N+2, H007(B32)
hingegen f(N)=a*N/(N+1)+b*N. Der pauschale N1-Ausschluss des alten
Algorithmus darf nicht ohne Quellenbeleg in die andere Funktion
uebertragen werden. H006 nennt auch den Sonderfall eines verschwindenden
Vorfaktors; Radikandenkomplexitaet allein ist keine fuer jedes Tupel
bewiesene Ausschlussherleitung.

H006 PDF8 fragt selbst nach Gamma/Q_N; PDF9 verwendet ausdruecklich
Q(0) fuer die numerische Enumeration. H007(B37) gibt nur die
ganzzahlige Verschiebung2z(N) an. PDF11 bezeichnet z=0 und die daraus
folgende GleichheitQ(N)=Q(0) als Naeherung. Die dort behauptete
Genauigkeit unter0.1MeV wird durch diese Aussage allein nicht
reproduziert oder als allgemeine Fehlerschranke zertifiziert.

Die beiden bestehenden Normalisierungsentscheidungen bleiben erhalten:
NORM-1982-N-003 blocked; NORM-1982-N-004 resolved mit engem Q0-Scope.
F(Gamma)=0 ergibt ohne F-Definition/Inversion weder Gamma=0 noch eine
unendliche Lebensdauer. Einzelheiten und unabhaengige Diagnose folgen
in GAMMA_QN_MATH_REVIEW_2026-09-06.md.

## 5. Autorenmanuskripte: Ergaenzung, Energieabstand und Tabellenauswahl

Root hat ferner H013 PDF21/22/23/24/25/32/39/40 sowieH014 PDF17/18/19/28
vollstaendig gegengelesen. H014 PDF20/21 wurden als angrenzender
Quantenzahlenkontext gelesen, liefern keine Gamma-Schliessung.

- H01320/PDF21: (14c) unbekanntesz, (14d) positive Massendifferenz.
- H01320a/PDF22: ausdrueckliche Ergaenzung beschraenkt(14d) auf
  stufenweise Anregung; unterstrichenesN fuer Ein-Prozess-Anregung.
  Die behauptete Erreichbarkeit ist keine berechnete Uebergangsrate.
- H01321/PDF23: K_B(14e) und endliche Grenze(15)/(15a). Wichtig:
  Der Text gibt einen aequidistanten Termabstand4*mu*alpha_plus,
  laut Quelle9.28718keV, an. Nicht behaupten, es fehle jeder Energiebezug!
  Dieser Termabstand ist aber keine Definition der vollenGamma-Breite.
- H01321a/PDF24: Korrektur hebt die vorherige(14d)-Nebenbedingung
  beiK_B auf; nurK_B>0 erlaubt externe Anregung, beiK_B<=0 keine.
- H01322/PDF25 undH01417/PDF19: Fehlt die MarkierungQ(N), meintQ
  den Grundzustand. Diese Symbolkonvention loestz nicht.
- H01329/PDF32: (21) reduziert sich beiN>0 durchdelta=0 aufT=T_N;
  T_N ist noch unbekannt. Keine vollstaendige Existenzzeitrechnung.
- H01336/37/PDF39/40: z=0-Approximation, Unsicherheiten weiterer
  Anregerparameter und unbekannteT_N. Aus einer grossen Kandidatenmenge
  wurden fuer TabellenIV-Vb empirisch gut passende Massenterme gewaehlt.
  Das ist eine Autorenbeschreibung der Auswahl, kein von uns erhobener
  quantitativer Treffer-/Fehlerbefund. UnterstricheneN bleiben tabelliert.
- H01415/15a/PDF17/18: gleiche Form(14c) und gleiche Ergaenzung zu(14d).
  H01426/PDF28 nennt im Anregungskontext positive ganzez, aber keine
  Bestimmungsfunktion. N>0-Kontext wahren; kein neuer Endpunktfehler
  aus einer unnoetigen Uebertragung aufN=0.

Der gelieferte H014-Scan springt vonDruck15a/PDF18 zuDruck17/PDF19.
Die korrespondierendeDruck16 fehlt; das erlaubt keinen sicheren
Vergleich des dort vermutetenK_B-Blocks. Fehlende Scan-Seite ist
nicht gleich fehlende Gleichung im urspruenglichen Manuskript.

## 6. Unabhaengige Kontrolle

Root hat den Pythonblock ausGAMMA_QN_MATH_REVIEW separat ausgefuehrt:
freie Spinfolgen, zwei positive Nullstellen der eigenen Testfunktion,
delta-Scope, beide Zuwachsformeln und eine kuenstliche Massenreihenfolge.
Zehn illustrativef6-Werte bei80/120Stellen: max.abs.Abweichung
4.708707092979954...e-79. Keine echten Resonanzmassen, kein Fit,
keine Intervallzertifizierung oder physikalische Fehlergrenze.

Acht bestehende Rechen-/Snapshotpruefungen samt verfuegbaren Quellhash-
Checks und98 Softwaretests bestanden. Register-/Abschlussstand siehe
Bericht undRESUME. Alte Rechner/Inputs/Normalisierungen unveraendert.
