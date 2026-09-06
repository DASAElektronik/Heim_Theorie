# Etappe 17: historischer Vergleich des einen N0-Elektronfalls

Beginn 2026-09-06, Ausgang 99a2efa. Keine Erweiterung auf andere Teilchen.

1. H006-Auditprofil und H010 Pascal/C statisch gegenueberstellen:
   Konfiguration, aktive AUX-/Phi-Formeln, Naturkonstanten, Alpha und Rundung.
2. Implementierungsfassungen und gespeicherte Ausgaben unterscheiden.
   Spaeterer Code ist kein unveraendertes Originalprogramm von 1982.
3. Erst nach Festhalten der Unterschiede ein eigenes begrenztes
   Vergleichsprofil rechnen. Keine fremden Programme/Makros ausfuehren,
   keine Variante wegen eines passenden Massenergebnisses uebernehmen.
4. Unterschiede durch getrennte Gegenrechnungen aufschluesseln;
   Wechselwirkungen und Abhaengigkeit von der Vergleichsreihenfolge benennen.
5. Bericht, Tests, Befundgrenzen und Wiedereinstieg sichern.

Keine moderne Widerlegungsrecherche, kein neues allgemeines Spektrum,
kein stilles Aendern des bestehenden H006-N0-Profils.

## Arbeitsteilung

- alpha_versions: aktive Formeln H006 gegen Pascal/C.
- book_derivation: Konstanten, Versionskoepfe und gespeicherte Ausgaben.
- data_audit: Auswahl-/Ganzzahl-/Rundungslogik und Aussagegrenzen.
- Root: Quellengegenpruefung, ggf. Vergleichsrechnung, Tests und Bericht.

## Abschlusskriterien

- [ ] Formel- und Konstantenunterschiede mit Herkunft festgehalten.
- [ ] Numerischer Vergleich unabhaengig kontrolliert oder Grenze benannt.
- [ ] Alte neun Rechenchecks unveraendert bestanden.
- [ ] Bericht, Register und Wiedereinstieg gesichert.
