# Vorvertrag: A(1)=1/3 versus 1/5

2026-09-06, Etappe 35. Ausgang `22001a2`, Branch `normalization-review`.
Maschinenvertrag: `04_reconstruction/alpha_audit/decay_sensitivity_inputs.json`.
Vor der ersten neuen Auswertung festgelegt und per Git gesichert.

## Auftrag

Vier vorab benannte Zellen: beide bisherigen Buch-Alpha-Profile mal
A=1/3 (Heims Wahl z5) und A=1/5 (eigene Sensitivitaet zum Kandidaten z3).
Alle Zellen berichten, keine Wahl nach Treffer, Rest oder Masse.

- Feste a_j, w, A16, eta, Y3/Y9 und Buchzustandsparameter.
- Gleichzeitig Externterm E_A(N4), Referenz g_A=B+E_A(1) und W_A=w*g_A
  aendern; E_A(0)=1 bleibt. Kein einseitiger Vergleich als Hauptergebnis.
- Gewoehnliche Vorwaertsauswahl nur innerhalb ihres festgelegten Zweiges.
  Keine neue TRC-Promotionsschwelle, Kappung oder Transferregel erfinden.
- Exakte Integergleichung und direkte ungewichtete Strukturbedingungen
  separat von Floor-Ausgabe, reeller N4-Relaxation und 107b-Gewichtung.
- Fuer jede Zelle neue endliche Obermenge herleiten; rationale Intervalle
  zur Vorzeichen-/Zweigpruefung. Keine Toleranz nach Ergebnis waehlen.
- Keine neue Masse, empirische Bewertung, Quellenkorrektur oder Behauptung
  einer aus (79)/(96b) hergeleiteten physikalischen Ersatzfunktion.

## Arbeitsteilung

- [ ] Root: neuer gebundener Rechner, exakte Kontrollen, Integration.
- [ ] data_audit: unabhaengige Zahlenauswertung aus eigenem Rechenweg.
- [ ] book_derivation: endliche Bereiche, gekoppelte Existenzaussagen.
- [ ] alpha_versions: Vergleichsvertrag/Zuschreibung und Ergebnisgegenreview.
- [ ] Tests, alte Ergebnischecks, Register, Bericht und Wiedereinstieg sichern.

Agenten schreiben nur neue DECAY_*_REVIEW-Dateien. Alte Eingaben/Rechner/
Snapshots bleiben unveraendert. Ausgangsbelege sind Etappen30-34; neue
Originallekture nur wenn ein konkret fehlender Vertragsbestandteil auftaucht.
