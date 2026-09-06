# Wiedereinstieg

Aktualisiert: 2026-09-06.

## Aktuell: achte Etappe abgeschlossen

Ausgangscommit2b46b5d; Plan3abd70c und Rechner-/Quellencheckpoint033617d
erfolgreich gepusht. Abschlusscommit-Nachricht:
`Complete configuration audit and context-first research handoff`.
Nutzer bestaetigt Gesamtzusammenhang vor Gesamturteil: spaetere Quellen
koennen Luecken schliessen, unsere Lesarten bleiben korrigierbar. Plan
`CONFIGURATION_SELECTION_PLAN.md` erledigt. Keine moderne Widerlegungs-
literatur/Hardware und keine neue externe Publikation in dieser Etappe.

Rechner `scripts/audit_configuration_selection.py`, Snapshot
`05_analysis/configuration_selection_diagnostics.json`, Bericht
`06_docs/CONFIGURATION_SELECTION_2026-09-06.md` und Karte
`04_reconstruction/alpha_audit/CONFIGURATION_DEPENDENCIES.md` liegen vor.
Die Karte nennt offene Verbindungen und konkrete erneute Pruefanlaesse.
Drei Reviews CONFIGURATION_SELECTION_SOURCE, CONFIGURATION_DEPENDENCY und
CONFIGURATION_SELECTION_MATH (jeweils2026-09-06) abgeschlossen. Keine
laufenden Agenten zum Fortsetzen erforderlich.

- I244/PDF250: q>=0 explizit ganzzahlig. II263/264: k>=1 ganzzahlig,
  Konfigurationszahl; L*Delta=k auf II265 als moeglicher Ansatz. Delta ist
  relative Ladungs-Viertpotenzaenderung, L=4. Ladungsquotient positiv bzw. Betrag.
- II268/269: Literal Q2=sqrt(eta) OHNE q durch 3 Leser/hochaufgeloeste Bilder
  bestaetigt. Zwischenzeitliche q-Fehllesung verworfen, keine Modellvariante.
- Mit a=eta_q,e=eta,x=1/eta_qk und R=V1+Q1-V2-Q2 gilt R=a*(x-D).
  D=(1+sqrt(a))^2/(4ea)+(1/a-a/e)*sqrt(e), B gleich aber1 statt1/a.
  D-B=sqrt(e)*(1/a-1)>0. Vorgelagerte Positivitaet verlangt x<D; gedruckte
  VQ-Zeile x>D; gedruckte eta-Folgerung x<B. Lokaler Knoten, keine eindeutige Reparatur.
- Gedrucktes u_q=(pi/q)^4*(B^4-1)-4 ergibt u2=1.963489... statt 2..3.
  Vier B-Paare (1,1),(1,2),(2,1),(3,1); globale Maxima k2/q3 bleiben.
  Ganze q>=5 analytisch/rational ausgeschlossen, nicht nur Scan bis10.
- Buch-Alpha-Paare (1,1)/(1,2) bleiben. 1989 B59 druckt eta22 tatsaechlich,
  aber ein Faktor ist nicht automatisch ein realisierter Zustand und die
  Buchregel gilt nicht ungeprueft fuer diese Version. Anwendbarkeitsfrage gesichert.
- Sieben Snapshots samt Quellchecks reproduziert; alte 6 Rechner/Inputs/Snapshots
  unveraendert. 86 Tests (77 vorher+9 neu). 1057 Felder unabhaengig gegengerechnet.
  Decimal40-200, Konvergenz80/120; Abstandsschutz ist keine Intervallzertifizierung.
- Befundregister16 Gruppen (keine Fehlerzaehlung); NORM48:46 resolved,2 alte Blocker.
  Formelkatalog weiter 2 isolierte ALPHA-Audits, kein Massenrechner.

Naechster konkreter Zusammenhang: Rueckverweise (79)/(79a) ausII269,
Exponentialnaeherung und Bedeutung von F/G samt Gueltigkeitsbereich und
Potentialidentifikation. Pruefen, ob hier zusaetzliche Bedingungen bzw.
andere Definitionen den lokalen Knoten erklaeren; nicht einfach Vorzeichen
oder B durch D ersetzen.1989eta22 als getrennte Versionsfrage mitfuehren.
Danach Massenabhaengigkeiten B50/Gamma-Q_N und Verstaendnisbilanz.
H-Wellen-/Arbeits-/C-Y3-Fragen bleiben auf der Zusammenhangskarte, keine
erneute ungezielte Suche ohne neue Querverbindung.

```powershell
py -3.13 scripts/audit_configuration_selection.py --check --verify-sources
py -3.13 scripts/validate_finding_register.py
py -3.13 -m unittest discover -s tests -q
```

Die sieben Snapshotchecks stehen in scripts/README.md. Die folgenden alten
Einstiege sind Verlauf, nicht die neue Prioritaet. PDFs/Render/OCR bleiben lokal.

## Verlauf: siebte Etappe abgeschlossen

Ausgangscommit752a61b; Plan6db53b5 und Quellen-/Registercheckpoint5199680
erfolgreich gepusht. Abschlusscommit-Nachricht:
`Complete reviewed cyclic flow audit and continuity handoff`.
Nutzer will systematisch weiterpruefen und spaeter mit Fakten veroeffentlichen.
Weder Gesamtwiderlegung noch vollstaendige Fehlerfindung vorwegnehmen.
Plan `CYCLIC_FLOW_PLAN.md` erledigt; keine neue externe Publikation.

Bericht `06_docs/CYCLIC_FLOW_AND_FINDINGS_2026-09-06.md` und13 Befundgruppen
in `04_reconstruction/alpha_audit/FINDING_REGISTER.json` (keine13 Fehler).
Drei Reviews in `04_reconstruction/alpha_audit/reviews/`: CYCLIC_FLOW_SOURCE,
CORRELATION_CLOSURE_SOURCE und FINDING_SCOPE, jeweils2026-09-06.
Alle abgeschlossen; kein laufender Agent fuer den Wiedereinstieg noetig.

- II157-162: Zyklizitaet als Zustandsrueckkehr, Eigenfrequenz eta,
  lambda=w_f/eta als Aggregatdiameter. eta ist nicht eta_qk; Zustands-A/C
  sind nicht Integrations-A/Korrelations-C. mc*lambda=h wird empirisch genannt.
- Neue positive Teilbruecke: II300/PDF306 H-Stabilitaet -> x5dot=x6dot=0 ->
  w=c fuer Im(Y); II173/174 setzt w_f=w. Bedingt w_f=c bei gleicher
  Objektzuordnung. Diese und Phasengeschwindigkeit bleiben offen.
- A=4P bei festen Endwerten gebunden; A=4C separate Zuordnung;
  C=P und Y3=1 berechenbare Spezialisierung. Unabhaengige Begruendung im
  Suchumfang nicht gefunden, keine Unberechenbarkeit/Fitbehauptung.
- Zweig-/Kehrwert-, Energieordnungs- und bedingter Matrixkonflikt bleiben
  bestehen; Register nennt fuer jeden Voraussetzungen und kleinste Tragweite.
  Alpha-prime-Reproduktion und positive Quellenbefunde ebenfalls enthalten.
- Sechs alte Rechner/Inputs/Snapshots unveraendert, alle --check- und
  Quellhashpruefungen erfolgreich.77 Tests:69 alte+8 neue Metadatentests.
  Neuer Validator prueft Schema/IDs/Dateipfade, keine Wahrheit der Befunde.
  Normalisierungsregister unveraendert47:45 resolved,2 alte Massenblocker.
- H004-Archiv-URL lieferte bei einem zusaetzlichen Webwerkzeug-Abruf HTTP404;
  lokale hashgepruefte PDF vorhanden. Kein neuer Fremdquellenimport/Upload.

Naechster konkreter Einstieg: L*Delta=k und Auswahl(98a), besonders
II Druck266/267 und ihre Rueckverweise; Begriffe, Praemissen, erlaubte
q/k-Konfigurationen und Einfluss auf eta_qk nachvollziehen. Zuerst Quellen-
und Begruendungskarte, dann ein abgegrenzter Konfigurationsfall. Keine
moderne Auswahlregel oder Messwertpassung hineinlesen. Danach B50/Gamma-Q_N
und Verstaendnisbilanz. H-Wellen-/Arbeits-/C-Y3-Offenheiten und Matrixerratum
bleiben separate Seitenzweige, keine erneut ungezielte Endlossuche.

```powershell
py -3.13 scripts/validate_finding_register.py
py -3.13 scripts/audit_wave_closure.py --check --verify-sources
py -3.13 -m unittest discover -s tests -q
```

Alle sechs Nachpruefbefehle stehen im Etappe7-Bericht. PDFs/Render/OCR
weiterhin nur lokal; portable Rechnerpruefung ohne --verify-sources moeglich.
Die nachfolgenden Einstiege sind historischer Verlauf, nicht neue Prioritaet.

## Verlauf: sechste Etappe abgeschlossen

Ausgangscommit 4155762. Nutzer moechte moegliche Luecken begruendet schliessen,
neu rechnen und auch negative Ergebnisse offen veroeffentlichen. Kein
vorweggenommenes Urteil; keine externe Publikation jetzt beauftragt.
Plan `WAVE_CLOSURE_PLAN.md`: H-Wellen-/Randwertproblem, getrennte eigene
skalare Ringdiagnose, Phase/Energie/Impuls und Manuskript/Buch-Schliessung.
Drei Agenten: Wellenquelle, Versionsvergleich, unabhaengige Mathematik.
Alte fuenf Rechner/Snapshots unveraendert lassen; kein Messwertfit.
Eine zusaetzliche Annahme schliesst die Originalherleitung nicht rueckwirkend.

Etappe6: Plan 7e69b13 und gepruefter Rechner-/Berichtcheckpoint e88f000
gepusht. Abschlusscommit-Nachricht:
`Complete wave closure findings and reproducible handoff`.
Neuer Rechner
`scripts/audit_wave_closure.py`, Snapshot und Bericht
`06_docs/WAVE_CLOSURE_2026-09-06.md`;69 Tests/4 Quellhashes passen.
Drei Reviews abgeschlossen. Eigene Ringmoden N1/2/3 und Phase-Ersetzung
aendern die algebraischen Zweige; keine physikalisch bestaetigten Alpha-
Vorhersagen. Exakte Domaenenpruefung und einmalige Doppelwurzelrundung nach
Review ergaenzt, alte Rechner unveraendert. MS-Ak hat eta^+1, Buch eta^-1/2;
gemeinsames eta nur bedingte Vergleichsannahme. Energieordnungsfehler bereits
im Manuskript p4. Quellen-/Versions-/Mathematikreviews fertig, keine
laufenden Agenten fuer den Wiedereinstieg noetig. Register47:45 resolved,
2 historische Massenblocker. Kein vollstaendiger H-Operator rekonstruiert.

Eigene skalare S1-Randbedingungen -> ganzzahliges n, keine Auswahl N=1;
n=0 gueltige raeumliche Mode, keine endliche Wellenlaenge. Nicht als
Wasserstoff-s-Zustand interpretieren. Phase und Gruppengeschwindigkeit
getrennt; deBroglie1929 ist nur freie historische Referenz (neue Quelle M005).
K=alphaPrime*(1-C)=N*zeta*f*s, mit f=beta fuer pc. Bei gleichem Buch-K
N1/2/3 inverse kleine beta137.03596/274.07740/411.11761. Erzwingt man
gleichen Wellen-/Teilchenimpuls, zeta=1/beta -> K=N*s; bei N1
beta0.999973375371. KEINE neue physikalische Alpha-Vorhersage.
Eigene effektive Proportionalitaet C_eff=rho*P_Buch*Y3 zeigt nur das Produkt
rho*Y3 bestimmbar; keine zwei neu behaupteten Heim-Fitparameter.

Naechster Einstieg: EDM2 Druck160/161 und (76), zyklische Fluesse,
Eigenfrequenz und Aggregatdurchmesser auf eine H-Wellen-Bruecke pruefen.
Die Annahmen von A=4A1A2, C und Y3 getrennt zurueckverfolgen. Falls keine
Schliessung gelingt, konkrete Unterbestimmtheit bilanzieren statt immer
weitere Varianten zu fitten. Alte fuenf Rechner/Inputs/Snapshots unveraendert.

```powershell
py -3.13 scripts/audit_wave_closure.py --check --verify-sources
py -3.13 -m unittest discover -s tests -q
```

## Verlauf: fuenfte Etappe abgeschlossen

Nutzer bestaetigt Fortsetzung und fragt nach Heims eigenem Warum; moeglicher
blinder Fleck erst nach dokumentierter Suche. Plan `AUTHOR_RATIONALE_PLAN.md`.
Ausgangscommit f4a5932. Drei Agenten getrennt beauftragt: A_-/Invarianzquelle,
breitere Autorensuche, unabhaengige Boostmathematik. Root implementiert nur
explizite Diagnosen und integriert die Begruendungsbilanz. Keine moderne
Widerlegungsliteratur als Ersatz; negative Suchbefunde nicht verallgemeinern.

Etappe5: Plan cd5cd0b und Rechner-/Berichtcheckpoint b34ba7d gepusht.
Abschlusscommit-Nachricht: `Complete reviewed author rationale and invariance findings`.
Eigener Fraction-Rechner
`scripts/audit_lorentz_meaning.py`, Snapshot und12 neue Tests (56 gesamt)
laufen. Neue Motivation: EDM2 Druck276/277=PDF282/283 erklaert bekannte
Alpha'-Abweichung -> angenommene interne Bindungsstruktur; duales Bild
als Elektronen-Kreiswelle lambda=2*pi*r. A_-Quelle I12/PDF20 behauptet
Masse/Impuls -> E_Q=pc, keine explizite T-Abgrenzung. Neuer Matrixbefund
I21/PDF29: unter normaler Trigonometrie/Transpose AAT !=I; I56/PDF63
anderer R6-Block ohneextrai als Kontexthinweis. Keine stille Reparatur.
Report `06_docs/AUTHOR_RATIONALE_2026-09-06.md` und drei Reviews abgeschlossen;
keine laufenden Agenten fuer den Wiedereinstieg erforderlich. Alte vier
Rechner/Snapshots unveraendert. Register46:44 resolved,2 alte Massenblocker.

Wichtiger neuer Autorenfund: Manuskript Magnetfeld und Drehimpulsdichte,
auf21.12.1981 datiert, mit Heim unterzeichnet. Seiten1/2 erklaeren die
Bindungs-Internstruktur als Grund fuer die Alpha-Korrektur; Seite5 hat
bereits den H-/pc-/Kreis-/Lorentz-Kern. Signatur/Datum visuell geprueft,
keine forensische Echtheitspruefung oder nachgewiesene Journalpublikation.
H011/H012 im Quellenregister; SHA256/URLs in
`03_notes/AUTHOR_RATIONALE_SOURCES_2026-09-06.md`.
ACHTUNG Versionsunterschied: Manuskript p5 nennt freie Integrationskonstante
bei A=4C und Y; nicht still mit Buch/Y3 gleichsetzen. Noch kein neuer Input.

Ergebnis: Motivation und Berufung auf Prinzipien belegt; exaktes H-Wellen-
Randwertproblem, pc als Arbeitsanteil und gesamte Meridianverkuerzung nicht
in den geprueften Quellen hergeleitet. Kein Allsatz ueber den Nachlass.
Boosts unterscheiden Skalar und Gleichungsform; statischer Diagnosekreis
wird Ellipse, ersetzt keine Heim-Schale. Literal-Matrixkonflikt bleibt
separat; eigene Reparatur EC-MATRIX-01 nicht als Autorenabsicht ausgeben.

Naechster aktueller Einstieg: explizites H-Wellenproblem aus II276/277,
297-301 und Manuskript1-5 rekonstruieren (Variable, Welle, Randbedingungen,
Radius und Bezugssystem). A=4C/Integrationsfreiheit als getrennte Version
verfolgen; p21-Matrix in frueherer Ausgabe/Erratum suchen. Keine moderne
passende Atomgleichung hineinschreiben, keine komplette Theorievalidierung.
Die folgenden alten Einstiegsabschnitte sind Verlauf, nicht neue Prioritaet.

```powershell
py -3.13 scripts/audit_lorentz_meaning.py --check --verify-sources
py -3.13 -m unittest discover -s tests -q
```

## Verlauf: vierte Etappe abgeschlossen

Nutzer: "Ok sehr gut, ja dann machen wir weiter". Ausgangspunkt 4ee1e1f.
Plan `ENERGY_KINEMATICS_PLAN.md`, Bericht
`06_docs/ENERGY_KINEMATICS_2026-09-06.md` und drei unabhaengige Reviews liegen vor.
Rechner `scripts/audit_energy_kinematics.py`; Snapshot
`05_analysis/energy_kinematics_diagnostics.json`. 11 neue Tests,44 insgesamt.
Quellen- und Mathematikreview ohne Rechenfehler; zusaetzlicher unabhaengiger
Buchindex-Regressionstest auf Empfehlung aufgenommen. Plan d1e31bc und
Rechner-/Erklaerungscheckpoint c1c6a32 sind gepusht. Keine laufenden Agenten
zum Fortsetzen erforderlich; deren Review-Dateien sind der dauerhafte Stand.

- I Druck81/PDF88 und288/PDF294 wiederholen E=pc; keine isolierte Schreibpanne.
  I81 nennt die Darstellung bekannt, I288 beruft sich auf SR. Die Trennung
  von konventionellem T ist UNSERE Analyse, keine belegte Autorenabgrenzung.
- II m(v_H)=gamma*m0 wird anhand BandI bedingt gelesen, nicht lokal bewiesen.
  Eigenen alten Wortlaut "Ruheenergie" fuer mc^2 korrigiert.
- I12/PDF20 deBroglie h/p; I233/PDF239 nichtzirkulaere Compton-Skala im
  Neutralteilchenkontext; I242/PDF248 photonische Kreiswelle. II301/PDF307
  setzt h/(mc) als Elektronen-Kreiswelle ein. Kontextwechsel bleibt offen,
  kein bedingungsloser Compton-Kreis-Widerspruch behauptet.
- Bei kleinem Buchzweig/Y3=1 gilt bedingt pc/T=274.068273... und
  lambda_dB/lambda_H=137.035960995...; keine Messwerte in der Rechnung.
- Allgemeine Schliessung K=g*f*sqrt(1-beta^2) zeigt Einfluss zweier
  getrennter Energie-/Wellenersetzungen. Nur ungefittete Vorwaertsdiagnosen,
  keine physikalisch konsistente Alternativtheorie oder neue Alpha-Prognose.
- Historische Standard-Begriffskontrolle Einstein1905 Druck920/PDF30,
  keine neuere Kritik-/Widerlegungsrecherche. Quelle/Hash im Bericht.
- Register45:43 resolved,2 alte Massenblocker. Originale und alte Snapshots
  unveraendert. Energieordnungs-Konflikt aus Etappe3 besteht weiter.

Naechster aktueller Einstieg: A_--Matrix (I Druck12/PDF20 und21/PDF29),
Bedeutung von "invariant", operative Energie-/Arbeitsbilanz und anschliessend
Kreisgeometrie/Wellenzuordnung. Zuerst ein konkretes Transformationsbeispiel
mit klaren Bezugssystemen, dann Quellenanspruch beurteilen. Nicht gleich
die Gesamttheorie neu anfangen oder passende Messwerte als Input einsetzen.
Danach L*Delta=k/(98a), B50 und Gamma/Q_N. Die aelteren Einstiegsabschnitte
weiter unten bleiben als Verlauf erhalten, diese aktuelle Prioritaet gilt.

Zusaetzlich zu den unten stehenden alten Pruefbefehlen:

```powershell
py -3.13 scripts/audit_energy_kinematics.py --check --verify-sources
```

## Aktuell: dritte Etappe abgeschlossen

Auftrag: mit Heim weiterarbeiten, Herleitung erklaeren. Abgeschlossener Plan:
`00_admin/CHARGE_DERIVATION_PLAN.md`. Quellen- und Mathematikreviews fertig.
Plan-Checkpoint `d53738e` und Rechnercheckpoint `59dde16` sind gepusht. Rechner
`scripts/audit_charge_averaging.py` und Erklaerung
`06_docs/CHARGE_DERIVATION_2026-09-06.md` liegen geprueft vor.
33 Tests bestehen; Mathematikreview akzeptiert die Rechnung, kleiner
Vorzeichenwortlaut korrigiert. Keine laufenden Agenten erforderlich.
Keine breite neue Widerlegungsrecherche und keine Hardwareentwicklung.

Neue Ergebnisse gegenueber der zweiten Etappe:

- BandI(29a) reproduziert: inverseAlphaPrime137.0380300128048, passend zur
  gedruckten Naeherung137.038. Zwei verschiedene Mittelungsschritte erklaert.
- Buch-eta-Indexbruecke geschlossen: BandII Druck266/267, (98), eta_qk,
  eta_q0=eta_q und eta_10=eta. Fruehere Notizen mit offener Buchdefinition
  sind historischer Stand; die IGW1982(V)-Notation bleibt separat.
- k-Einfuehrung ueber L*Delta=k und Auswahlbeschraenkung(98a) sind als
  Annahmen zu verstehen, nicht als bereits bewiesene physikalische Aussagen.
- Korrelationskette: s(varrho)+s(delta)=s(omega) heuristisch; A=4A1A2
  algebraisch; A=4C separate Zonen-Zaehlannahme; Y3 bleibt offen.
- Neuer lokaler Buchkonflikt: W<=X<=V, E_k>=0 und -E_k=V-W lassen nur
  E_k=0 zu. Quellen- und Algebrareviews bestaetigen den Befund.
  `BOOK_ENERGY_ORDER_ISSUE.md` dokumentiert getrennten Korrekturkandidaten.
- Register44 Entscheidungen:42 resolved,2 historische Massenblocker.
  Der neue Buchbefund ist eine separate Quellenfrage, kein stiller Fix.

Der folgende zweite/erste Etappenstand bleibt als Verlauf erhalten.

## Zweite Audit-Etappe abgeschlossen

Bericht: `06_docs/BOOK_TRACE_2026-09-06.md`.
Fortsetzungsplan: `00_admin/UNDERSTANDING_ROADMAP.md`.
23 Tests bestehen, beide Ergebnis-Snapshots sind reproduzierbar.
Buchquellen- und Mathematikreview (GPT-5.6 Terra high) sowie externe
Provenienzreview (GPT-5.6 Sol high) abgeschlossen. Reviews liegen unter
`04_reconstruction/alpha_audit/reviews/`; keine laufenden Agenten erforderlich.

Der Nutzer erlaubt auch eigene Theorieverbesserungen: plausible Korrekturen
oder neue Annahmen als getrennte, pruefbare Modellvarianten ausarbeiten.
Originale erhalten, neue Freiheitsgrade und nachtraegliche Anpassungen offenlegen.
Neueste Prioritaet: erst Herleitung/Annahmen verstehen, danach neuere Arbeiten
auf physikalische Widerlegung oder Anschluss pruefen. Jetzt nur interne
Konsistenz und Quellenprovenienz; kein Gesamturteil zur Theorie.
Neue Befunde:

- Band I (28a)/(29), Druck247/248: unindiziertes eta und vartheta lokalisiert;
  Ladungs-/Potentialmittelung ist Annahme, nicht durch Folgealgebra bewiesen.
- Band II Druck1: Y_k fuer ungeklaerte Beziehungen; Tabellen mit Y_k=1.
  Y3=1 ist Spezialisierung, keine gefundene theoretische Bestimmung.
- Neue Y3-Inversion ist ausdruecklich ex-post; kein gemeinsames Y3 repariert
  das gedruckte Zweigpaar. Buchstruktur + deklarierte IGW1982-eta-Profile,
  keine bereits buchautarke Zahlenherleitung.
- Binary64-Fehler viel zu klein; 8-stellige Dezimalrechnung kann dagegen
  aehnlich grosse Fehler machen. Historischer Rechenweg bleibt unbekannt.
- Generischer Decimal-Randfall nach unabhaengiger Review behoben:
  unzureichende Praezision fuer exakte Quadrate/Subtraktion wird abgelehnt.
- 1989-Rehost byte-identisch; kein alpha-spezifisches Erratum gefunden.
  Historische Messunsicherheit im IGW-Vergleich falsch/unvollstaendig
  uebertragen; genaue angebliche 1992-Zahlenpaarung weiter ohne Primaerbeleg.
- 42 Normalisierungsentscheidungen: 40 resolved, zwei blocked.
  Formelstatus unveraendert: zwei Alpha-Audits, zwoelf nicht implementiert.

## Auftrag und abgeschlossene Etappe

Alpha-Audit 1982/1989 nach `00_admin/ALPHA_AUDIT_PLAN.md` umsetzen und
wiederholt sichern. Der Nutzer hat Arbeit, bedarfsgerechte Agenten und
Sicherung autorisiert. Save-Workflow umfasst Commit und Push.

Die erste Etappe ist abgeschlossen: ausfuehrbarer Konsistenz-Audit mit
unabhaengiger Review. Die historische Ursache der widerspruechlichen Zahlen
und die vollstaendige Massenrekonstruktion bleiben offen.

## Ausgangspunkt

- Branch: `normalization-review`; Remote: `origin`.
- Ausgangscommit: `1485311` (2026-05-18).
- Arbeitsbaum beim Start sauber.
- 14 Formelgruppen source_checked / not_implemented.
- 37 Normalisierungsentscheidungen resolved, zwei blocked.
- Quellen-PDFs und PNGs lokal vorhanden, absichtlich nicht versioniert.

## Bereits festgestellt

- 1982: woertliche eta-Indexlesart ergibt 1/alpha_plus etwa 137.04918803;
  gedruckt ist 137.03596147. Indexvariante ist bereits separat dokumentiert.
- Gedruckte Zweigpaare in 1982 und 1989 erfuellen die von ihrer Gleichung
  verlangte Identitaet alpha_plus^2 + alpha_minus^2 = 1 nicht.
- Persistente Berechnung und Review bestaetigen diese Befunde.
- 1989 hat zusaetzlich zwei inkompatible B62-/Kehrwertangaben.
- Buchscan EDM2, Druckseite 302 / PDF-Folio 308, (105): dasselbe gedruckte
  Paar und dieselbe linke Seite. Y3 wird als Unsicherheitsfaktor eingefuehrt
  und fuer die konkrete Zahlenrechnung auf 1 spezialisiert.

## Fertige Artefakte der ersten Etappe (historischer Stand)

- Quellenagent abgeschlossen: Review unter
  `04_reconstruction/alpha_audit/reviews/SOURCE_REVIEW_2026-09-06.md`.
- Rechner, Eingaben, Model Card und Ergebnisse liegen vor; 13 Tests bestanden.
  PDF-SHA256 fuer drei Quellen werden geprueft. Default-Rechnung: 80 Stellen;
  120-Stellen-Konvergenz wird im Test geprueft.
- Mathematikreview abgeschlossen und akzeptiert:
  `04_reconstruction/alpha_audit/reviews/MATH_REVIEW_2026-09-06.md`.
- Bericht: `06_docs/ALPHA_AUDIT_2026-09-06.md`.
- Zwei ALPHA-Katalogeintraege `audit_implemented`; 12 andere `not_implemented`.
  41 Normalisierungsentscheidungen: 39 resolved, zwei blocked.
- Keine aktive Agentenarbeit erforderlich. Source-Transkriptionen unveraendert;
  Risikowortlaut und alte Rechennaeherungen wurden praezisiert.

Agentennamen sind Sitzungsreferenzen, keine Voraussetzung zum Neustart.
Bei neuer Sitzung vorhandene Review-Dateien zuerst lesen.

## Naechster konkreter Schritt

Energiebegriff und kinematische Annahmen vor Buch(105) rueckwaerts verfolgen:
m(v_H), E_k=m*v_H*c, mc^2=ch/lambda_H, lambda_H=2*pi*r_H und
Lorentz-/K-Schalen-Konstruktion. Zuerst Bedeutung und interne Konsequenzen
klarstellen; keine Gleichsetzung mit Standardbegriffen ohne Beleg.
Danach L*Delta=k und die bedingte k/q-Auswahl(98a) tiefer nachvollziehen.
Indexsuche nicht neu beginnen: die explizite Buchstelle ist jetzt gefunden.
B50/Gamma-Q_N und die vollstaendige Massenrechnung bleiben offen.

Bereits verifiziert und nicht neu anfangen: 1982-Fitvariante ist nur naeher,
1989-(q,k)-Indexkette ist belegt, alle fuenf Druckpaarchecks sind inkompatibel.
Eine gemeinsame Aenderung der rechten Seite repariert die Zweigidentitaet nicht.

```powershell
py -3.13 scripts/audit_alpha.py --check --verify-sources
py -3.13 scripts/audit_alpha_book.py --check
py -3.13 scripts/audit_charge_averaging.py --check --verify-sources
py -3.13 -m unittest discover -s tests -v
```

Python ist ueber `py -3.13` verfuegbar; keine Fremdprogramme aus ZIPs ausfuehren.

## Sicherung

- Plan-Checkpoint `f9eeeee` committed und erfolgreich gepusht.
- Rechner-Checkpoint `df02845` committed und erfolgreich gepusht.
- Erste Etappe `a2a9e84`, zweite Etappe Plan `c679891`, Diagnosecheckpoint
  `b99395e`: alle erfolgreich gepusht.
- Zweite Etappe Abschluss: Commit-Nachricht
  `Complete reviewed book diagnostics and understanding roadmap`.
  Finalen Hash und Remote-Abgleich mit den folgenden Befehlen feststellen.
- Dritte Etappe Abschluss: Commit-Nachricht
  `Complete charge derivation, book index bridge and energy-order findings`.
- Letzter Nutzerstand: 24.218 verbleibende Credits; keine automatische Live-Abfrage.

```powershell
git log -3 --oneline
git status --short --branch
git rev-parse HEAD
git rev-parse origin/normalization-review
```

Fremd-PDFs sind bewusst nicht auf GitHub. Drei SHA256 plus URLs in `inputs.json`
ermoeglichen den spaeteren Quellenabgleich; der numerische Audit laeuft auch
ohne diese Dateien. Bei einem abweichenden Download keine neue Datei still
als dieselbe Ausgabe behandeln.
Band-I-SHA256/Fundstelle stehen zusaetzlich in der neuen Band-I-Lesenotiz.
