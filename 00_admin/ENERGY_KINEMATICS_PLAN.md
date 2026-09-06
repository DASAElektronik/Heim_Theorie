# Vierte Etappe: Energie, Masse und Wellenlaenge

Beginn: 2026-09-06. Auftrag: mit Heim weiter; Anschluss an Commit 4ee1e1f.

## Begrenztes Ziel

Die Eingaben der Alpha-Herleitung in EDM2 Druck300/301 rueckwaerts verstehen:
m(v_H), E_k=m*v_H*c, mc^2=ch/lambda_H, lambda_H=2*pi*r_H,
y=r_H*sqrt(1-alpha^2). Bedeutung, Beleg und Algebra trennen. Keine breite
moderne Widerlegungsrecherche, keine Hardwareentwicklung, kein Zielwertfit.

## Arbeit und Zustaendigkeit

1. Hauptagent: relevante Quellseiten selbst ansehen, Begriffs-/Abhaengigkeitskarte,
   dimensionslose bedingte Diagnose und Tests, Bericht und Integration.
2. book_derivation: fruehere Masse-/Energiebegriffe, eigene Quellenreview.
3. alpha_versions: Wellenlaenge und Lorentz-/K-Schalen-Geometrie, eigene Review.
4. data_audit: unabhaengige Algebra und anschliessend Rechnergegenpruefung.

Quellenagenten schreiben jeweils nur ihre benannte Review-Datei. Keine
Fremdprogramme, Makros oder bestehende Quellformeln ausfuehren/aendern.
OCR lokalisiert; Seitenbilder entscheiden. Quellen-PDFs bleiben lokal/ignoriert.

## Abschlusskriterien

- [x] Fruehere Definitionen mit Druckseite, PDF-Seite und Bildkontrolle.
- [x] E=pc von T=(m-m0)c^2 und Ruhe-/Gesamtenergie begrifflich getrennt.
- [x] lambda=h/(mc) von einer zusaetzlichen lambda=h/p-Lesart getrennt.
- [x] Einfluss der eingesetzten Relationen auf Alpha-Gleichung algebraisch klar.
- [x] Eigene Alternativen nur als ungefittete bedingte Diagnosen kennzeichnen.
- [x] Tests, unabhaengige Reviews, verstaendlicher Bericht und Wiedereinstieg.
- [x] Plan d1e31bc und Rechner-/Berichtcheckpoint c1c6a32 committed/gepusht.

Abschlusscommit-Nachricht: `Complete reviewed energy and wavelength reconstruction`.
Finalen Remote-Abgleich mit `git status --short --branch` und
`git rev-parse HEAD origin/normalization-review` kontrollieren.

## Sicherungen

Plancheckpoint zuerst, dann Rechner-/Ergebnischeckpoint und gepruefter Abschluss.
Agentennamen sind keine Voraussetzung fuer einen spaeteren Neustart.
