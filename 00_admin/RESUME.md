# Wiedereinstieg

Aktualisiert: 2026-09-06.

## Aktuell: zweite Etappe laeuft

Plan: `00_admin/BOOK_TRACE_PLAN.md`. Ausgangscommit `a2a9e84` ist gepusht.
Quellenagenten `book_derivation` (GPT-5.6 Terra high) und `alpha_versions`
(GPT-5.6 Sol high) bearbeiten Buchabhaengigkeiten bzw. externe Fassungen.
Hauptagent entwickelt eine getrennte Y3-/Rechengenauigkeitsdiagnose.
Reviews landen in `04_reconstruction/alpha_audit/reviews/`.
Der Nutzer erlaubt auch eigene Theorieverbesserungen: plausible Korrekturen
oder neue Annahmen als getrennte, pruefbare Modellvarianten ausarbeiten.
Originale erhalten, neue Freiheitsgrade und nachtraegliche Anpassungen offenlegen.
Neueste Prioritaet: erst Herleitung/Annahmen verstehen, danach neuere Arbeiten
auf physikalische Widerlegung oder Anschluss pruefen. Jetzt nur interne
Konsistenz und Quellenprovenienz; kein Gesamturteil zur Theorie.
Quellenreviews liegen inzwischen vor; `book_derivation` prueft unabhaengig
die neue Mathematik. Diagnosecode und Snapshot fertig, 21 Tests bestanden;
noch nicht als unabhaengig freigegeben behandeln.
Die folgenden Angaben beschreiben die fertiggestellte erste Etappe.

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

## Fertige Artefakte

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

Die Buchherleitung um (105), Druckseiten 297-302, rueckwaerts auf eta-, A_k-
und Y3-Definitionen verfolgen. Ziel: Ursache der gedruckten Inkonsistenz
lokalisieren. Danach 1989 B58-B62 mit weiteren datierbaren Fassungen/Errata
vergleichen. Nicht automatisch einen Faktor oder Index nach Zielwert waehlen.

Bereits verifiziert und nicht neu anfangen: 1982-Fitvariante ist nur naeher,
1989-(q,k)-Indexkette ist belegt, alle fuenf Druckpaarchecks sind inkompatibel.
Eine gemeinsame Aenderung der rechten Seite repariert die Zweigidentitaet nicht.

```powershell
py -3.13 scripts/audit_alpha.py --check --verify-sources
py -3.13 -m unittest discover -s tests -v
```

Python ist ueber `py -3.13` verfuegbar; keine Fremdprogramme aus ZIPs ausfuehren.

## Sicherung

- Plan-Checkpoint `f9eeeee` committed und erfolgreich gepusht.
- Rechner-Checkpoint `df02845` committed und erfolgreich gepusht.
- Abschlussstand: Commit-Nachricht `Complete audited alpha findings and recovery handoff`.
  Den Hash und Remote-Abgleich mit den folgenden Befehlen feststellen.
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
