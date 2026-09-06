# Wiedereinstieg

Aktualisiert: 2026-09-06.

## Aktuell: vierte Etappe in Arbeit

Nutzer: "Ok sehr gut, ja dann machen wir weiter". Ausgangspunkt 4ee1e1f,
Arbeitsbaum sauber. Plan: `ENERGY_KINEMATICS_PLAN.md`.
Quellenagenten verfolgen Masse/Energie und Wellenlaenge/Geometrie getrennt;
Mathematikreview unabhaengig. Hauptagent implementiert nur bedingte,
ungefittete Diagnosen und erklaert die Quellenkette. Originale und alte
Snapshots unveraendert lassen; keine moderne Widerlegungsrecherche vorziehen.

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
