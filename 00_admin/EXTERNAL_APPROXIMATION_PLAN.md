# Externzonennaeherung: Quellenbruecke und beidseitiger Fehlertransport

2026-09-06, Etappe33. Ausgang df9dff6, Branch normalization-review.

## Vor Beginn festgelegter Auftrag

1. (79b)/(79c) -> H004322/323 -> g/108 an den Originalen pruefen:
   Zuordnung r zu N_(4), Parameter, Amplitude und Normierung.
2. Positive Quellenregeln zuerst erfassen. Bereits bestimmte skalare
   Asymptote/Restschranke aus EXPONENTIAL_CONTEXT nicht als neuen Fund zaehlen.
3. Eine Korrektur des Externzonenverlaufs muss, falls quellenbegruendet,
   zugleich seinen Referenzbeitrag in g und damit W beruecksichtigen.
4. Erst bei belegter Bruecke einen physikalischen Fehlerrahmen einsetzen.
   Bei offener Bruecke nur klar gekennzeichnete bedingte Mathematik und
   synthetische Kontrollen, keine erfundene r(N4)- oder Parameterwahl.
5. Bisherige Profile, Rechner, Snapshots und FIND-042 unveraendert erhalten.
   Keine Y9-/Massen-/Restoptimierung, kein Autorenerratum erfinden.

## Arbeitsteilung

- [ ] Root: Originalsicht, Integration, eigene Tests/Fehleralgebra, Bericht.
- [ ] book_derivation:79/79a-c und322/323, Bruecke/Gueltigkeitsbereich.
- [ ] alpha_versions:322-330, A/mu_+/g/W und Bezugskonfiguration.
- [ ] data_audit: unabhaengige bedingte Fehlerfortpflanzung/Kontrollblock.
- [ ] Reviews gegenlesen und selbstenthaltenen Code wiederholen.
- [ ] Tests/alte Ergebnischecks, Register, Bericht und Wiedereinstieg sichern.

Agenten schreiben ausschliesslich ihre drei neuen Reviewdateien.
Der mathematische Vorvertrag bei unveraenderten a_i und w lautet:
R_neu=R_alt+delta(N4)-w*delta(Q4), mit Q4=1 im festen Buchfall.
Dies ist eine eigene bedingte Identitaet, keine bereits belegte Heim-Korrektur.
Gemeinsame Fehler, unabhaengige Fehler und Aenderungen anderer Groessen
muessen getrennt bleiben. Ein fehlender Quellenanschluss ist ein Ergebnis.
