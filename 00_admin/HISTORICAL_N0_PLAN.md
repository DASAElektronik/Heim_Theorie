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

- [x] Formel- und Konstantenunterschiede mit Herkunft festgehalten.
- [x] Numerischer Vergleich unabhaengig kontrolliert oder Grenze benannt.
- [x] Alte neun Rechenchecks unveraendert bestanden.
- [x] Bericht, Register und Wiedereinstieg erstellt; gemeinsam im Abschlusscommit.

## Abschluss

Plan f6d7598, Rechenvertrag vor Auswertung ca9abb1 gepusht.
64 vorab feste Zellen und zusaetzliche Wurzellesart, 16 neue Tests;
127 Tests und zehn Rechenchecks bestanden. Unabhaengige 65-Zellen-Rechnung
mit drei Vergleichsgruppen je 1365 Felder; Root fuehrte Reviewcode erneut aus.
FIND-029 ist ein Versions-/Implementierungsbefund, keine Gesamtwiderlegung.
Folgefrage: konkrete alpha3-Herleitungs-/Formelblattspur, keine Massentrefferwahl.
