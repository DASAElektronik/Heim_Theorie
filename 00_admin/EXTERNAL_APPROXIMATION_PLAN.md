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

- [x] Root: Originalsicht, Integration, eigene Tests/Fehleralgebra, Bericht.
- [x] book_derivation:79/79a-c und322/323, Bruecke/Gueltigkeitsbereich.
- [x] alpha_versions:322-330, A/mu_+/g/W und Bezugskonfiguration.
- [x] data_audit: unabhaengige bedingte Fehlerfortpflanzung/Kontrollblock.
- [x] Reviews gegenlesen und selbstenthaltenen Code wiederholen.
- [x] Tests/alte Ergebnischecks, Register, Bericht und Wiedereinstieg sichern.

Agenten schreiben ausschliesslich ihre drei neuen Reviewdateien.
Der mathematische Vorvertrag bei unveraenderten a_i und w lautet:
R_neu=R_alt+delta(N4)-w*delta(Q4), mit Q4=1 im festen Buchfall.
Dies ist eine eigene bedingte Identitaet, keine bereits belegte Heim-Korrektur.
Praezisierung nach Vollsicht322/323: dieser Vorvertrag setzt die
Endpunktnormierung delta(0)=0 voraus oder verwendet bereits die effektive
Korrektur delta(n)=h(n)-h(0). Fuer eine rohe Korrektur F(n)=exp(-n/3)+h(n)
und unveraendertes mu_+/alpha4=1 gilt wegen Delta(0)=0 allgemeiner
R_neu-R_alt=h(N4)-w*h(Q4)+(w-1)*h(0). Beide Bezugspunkte erhalten.
Gemeinsame Fehler, unabhaengige Fehler und Aenderungen anderer Groessen
muessen getrennt bleiben. Ein fehlender Quellenanschluss ist ein Ergebnis.

## Abschluss

Bericht: `06_docs/EXTERNAL_APPROXIMATION_2026-09-06.md`.
Explizite Nullpunkt-/Geruestnormierung gefunden; A(1)=1/3 auf Druck 325
ausdruecklich heuristisch. Keine geschlossene r-/nu-/N4-Fehlerbruecke im
geprueften Anschluss. Eigene Dreipunktidentitaet und strikte uniforme
Robustheitsbedingung, keine frei eingesetzte physikalische Korrektur.
16 neue Tests, 304 insgesamt; 12 alte Ergebnischecks und alte Zertifikate
bestanden. Drei interne Reviews; 179 unabhaengige rationale Kontrollen
und alte unabhaengige Intervallkette samt w durch Root wiederholt.
Keine neuen Besetzungs-/Massenprofile. Weiter: konkreten (96b)-Verweis
pruefen; alternative A-Kandidaten erst nach eigenem Vorvertrag untersuchen.
