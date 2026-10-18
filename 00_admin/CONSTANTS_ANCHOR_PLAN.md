# Quellenvertrag: Konstantenkorrektur und Elektronenanker

2026-10-18, Etappe 40. Git-Ausgang `442adf7` plus uncommittierter,
abgeschlossener Etappe 39. Bestehende Änderungen bleiben erhalten.

## Frage und vorab begrenzter Umfang

H004 Druck 348-349 nach(115), Tabellenvermerk371 und die ausdrücklich
genannten Beziehungen29/97/112: empirische Eingaben, Modellannahmen,
Rückrechnung und nachfolgende Ausgaben auseinanderhalten. (29) in der
lokalen H003-Ausgabe quellengetrennt prüfen; Editionsbrücke offen ausweisen.
R_ und die Hilfsbeziehungen zu c, epsilon0, mu0 zurückverfolgen.

Der erste Originalblick auf349 zeigt bereits den ausdrücklichen Einsatz
von gemessenem e und m_e mit hbar und c. Dieser Quellenbefund ist vor
weiterer Rechnung bekannt. Keine unabhängige Elektronenmassenvorhersage
aus dem nachkalibrierten Rückweg ableiten.

Zulässig sind algebraische Umkehrung bei festem dimensionslosem
Elektronenfaktor, Einheiten-/Abhängigkeitsprüfung und Konsistenzchecks der
gedruckten Konstanten mit deklarierten Rundungsintervallen. Numerische
Werte vor Auswertung an Quelle binden; keine moderne Empirie, freie
Konstanten-/Y-Wahl oder neue Massenanpassung. H006 und H004 nicht mischen.

## Dokumentation und Prüfung

Bericht `06_docs/CONSTANTS_ANCHOR_2026-10-18.md`, Quellenumfang
`03_notes/CONSTANTS_ANCHOR_SOURCES_2026-10-18.md`, Register und Einstieg.
Bei neuer Rechenlogik eigener kleiner Diagnosecode mit sinnvollen
Tests; ansonsten keine Tests bloßer Textwiederholung. Quellhashes,
Altbefund-Erhalt, relevante Regressionen und Diff prüfen.
Ein Agent; keine neue unabhängige Gegenprüfung behaupten. Kein Commit/Push
ohne entsprechenden Nutzerauftrag. Alle alten Rechenprofile bleiben erhalten.

## Vorab fixierte Zahlendiagnose

Vor erster Rechnung: H004371 druckt h=6.626173e-34 (nicht hbar),
gamma=6.672131e-11, epsilon0=8.854323e-12, mu0=1.256618e-6,
|e|=1.602188e-19, jeweils SI. Dies sind Endwerte, keine belegten
ursprünglichen Kalibriereingaben. Nur ihre interne Verträglichkeit prüfen.
Für jeden Drucktoken hypothetisch Rundung zur nächsten letzten Stelle
(± halbe letzte Einheit); keine Messfehlerinterpretation.

M006 Druck15/PDF34: c=299792458 m/s, historische Standardunsicherheit
1.2 m/s; zunächst Zentralwert, zusätzlich dessen ±1-sigma-Bereich als
Sensitivitätsvergleich, nicht als harte Messschranke. Prüfe c² epsilon0 mu0=1
mit exakten rationalen Druckintervallen; berechne impliziertes c und R.
Prüfe separat die wörtliche H003(29)-Brücke mit hbar=h/(2pi),
eta=pi/(4+pi^4)^(1/4), vartheta=5eta+2sqrt(eta)+1.
H004301 verwendet29 weiterhin;105 ersetzt29a, nicht stillschweigend29.
Keine Gleichsetzung der105-Kopplung mit e²R/(4pi hbar).
Decimal-Vergleich bei60/90 Stellen ist Stabilitätskontrolle, kein
Intervallzertifikat für irrationale Funktionen. Massenskaleninversion
nur symbolisch und mit synthetischen Testwerten; kein neuer D_e-Fit.
