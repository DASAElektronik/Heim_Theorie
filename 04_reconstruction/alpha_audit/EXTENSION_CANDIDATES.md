# Korrektur- und Erweiterungskandidaten: Alpha

Stand: 2026-09-06. Eigene Arbeitsvarianten, keine Aussagen Heims und keine
bestaetigte neue Physik. Quellen bleiben unveraendert.

## EC-ALPHA-01: arithmetisch konsistente Auswertung

Status: fuer die vier ausdruecklichen IGW-Profile implementiert/geprueft in
`scripts/audit_alpha.py`. Die Originalgleichung bleibt erhalten, ebenso die
Unsicherheiten der Indexlesart. Die beiden positiven Loesungen werden stabil
berechnet und muessen `alpha_plus^2 + alpha_minus^2 = 1` erfuellen.

Mehrwert: Wir koennen Formel und Druckwerte auseinanderhalten und eine
spaetere Massenrekonstruktion mit klar versionierten Eingaben durchfuehren.
Zusaetzliche angepasste Parameter: keine. Nicht erreicht: Begruendung der
Formel, historische Fehlerursache oder experimentelle Bestaetigung.

## EC-ALPHA-02: Y3-Kalibrierung als Diagnose

Status: getrennte, ausdruecklich nachtraegliche Inversion in
`scripts/audit_alpha_book.py`. Sie kombiniert die Struktur von Buch (105) mit
den zwei bereits dokumentierten IGW1982-eta-Profilen. Nachtrag Etappe3:
Die lokale Buch-Indexbruecke ist inzwischen an(98) source-belegt (q,k).
Die historischen Diagnoseprofile und die abweichende IGW-Schreibweise bleiben
getrennt; eine physikalische Herleitung folgt aus dem Definitionsfund nicht.

```text
R0 = 9*vartheta/(2*pi)^5
P = A1*A2
alpha*sqrt(1-alpha^2) = R0*(1-P*Y3)
Y3(d) = (1 - sqrt(d^2-1)/(d^2*R0))/P, d=1/alpha >= 1
```

Anpassung an CODATA2022-alpha gibt einen kontinuierlichen Fitparameter.
Dieser Messwert ist damit verbraucht und kein Validierungstest mehr.
Der komplementaere Zweig folgt algebraisch; ohne unabhaengig begruendete
physikalische Messgroesse ist er keine zusaetzliche bestaetigte Vorhersage.
Ein gemeinsames Y3 kann das gedruckte historische Zweigpaar nicht retten.

Naechster echter Mehrwert waere eine begruendete Abhaengigkeit von Y3 und
eine davon unabhaengige Pruefgroesse. Bis dahin nur Diagnose, nicht Ersatz
fuer die Originaltheorie. Keine angepassten Alpha-Zahlen in deren Profile
einschleusen.

## EC-ALPHA-03: theoretische Schliessung der offenen Annahme

Status: Forschungsfrage, noch keine neue Gleichung vorgeschlagen.
Zu verstehen sind zuerst die physikalische Bedeutung der Mittelung in
Band I (28)/(29) und die Proportionalitaet in Band II vor (105). Gesucht
waere eine begruendete Bestimmung von Y3 statt der numerischen Setzung 1.

Akzeptanzkriterien fuer einen Vorschlag:

1. Voraussetzungen, Symmetrien und Definitionsbereich explizit angeben.
2. Die neue Beziehung aus diesen Voraussetzungen herleiten; offene Schritte
   nicht durch einen Zahlenfit ersetzen.
3. Alle kontinuierlichen und diskreten Zusatzentscheidungen zaehlen.
4. Eine noch nicht zur Wahl der Beziehung benutzte Konsequenz vorab festhalten.
5. Nach der Verstaendnisbilanz an unabhaengigen Quellen/Daten pruefen; dabei
   auch bestaetigte Grenzen oder eine Widerlegung akzeptieren.

Beliebige Aenderungen der linken Seite, eigens um zwei bekannte Zahlen zu
treffen, sind derzeit kein begruendeter Kandidat. Das schliesst eine spaeter
physikalisch motivierte Aenderung nicht aus.

## Nutzen fuer andere Projekte

Etappe6: `audit_wave_closure.py` formuliert ein eigenes skalares periodisches
Ringproblem. Es liefert lambda=2*pi*R/N, aber keine physikalische Auswahl
N1, Radius oder Dispersion. Erzwingt man gleiche Teilwelle/Energie/Impuls,
folgt bedingt zeta=1/beta; bei beibehaltenem pc und y=R*s wird K=N*s.
Das ist eine isolierte, ungefittete Ersetzung, keine neue Atomtheorie.
Die effektive eigene rho*P_Buch*Y3-Familie macht die Proportionalitaetsluecke
sichtbar, schliesst EC-ALPHA-03 jedoch nicht. Keine neue bestaetigte Physik.

EC-MATRIX-01 (Etappe5): Entfernen der zwei zusaetzlichen i-Faktoren aus
dem gedruckten EDM1-p21-Block waere eine eigene lokale Reparaturhypothese.
Die andere R6-Matrix auf p56 liefert Kontext, aber keine Autorenkorrektur.
`BOOK_LORENTZ_MATRIX_ISSUE.md` trennt alle Lesarten. Die neue Boostdiagnose
uebernimmt keinen Fix in Heim und bestimmt keine neue Alpha-/Massenformel.

Etappe4: `scripts/audit_energy_kinematics.py` zeigt den Einfluss von zwei
diskreten Ersetzungen (pc durch T; danach h/(mc) durch h/p). Diese bleiben
ungefittete Diagnosen, keine neuen physikalischen Erweiterungskandidaten.
Bei unveraenderten anderen Annahmen aendert sich K=beta*s zu s*(1-s) oder
s*(1-s)/beta. Eine begruendete Erweiterung muesste zuerst Energie/Arbeit,
Kreisgeometrie und beobachtbare Zuordnung konsistent gemeinsam herleiten.

Ergaenzender Korrekturkandidat EC-ENERGY-01: Umkehr der gedruckten
Energieintervallordnung, siehe `BOOK_ENERGY_ORDER_ISSUE.md`. Diese lokale
algebraische Reparatur ist keine gesicherte Autorenabsicht und keine
Loesung des Alpha-Druckwiderspruchs.

Die lambda-Familie in `scripts/audit_charge_averaging.py` dient nur dem
Verstaendnis der Mittelungsannahme; sie ist kein neuer physikalischer Kandidat.

Bereits uebertragbar ist die Arbeitsmethode: versionierte Annahmen,
reproduzierbare Rechnung, getrennte Referenzen, unabhaengige Reviews und
Fortsetzungsprotokolle. Ein technischer Nutzen von Heim-spezifischen
physikalischen Effekten ist bislang nicht nachgewiesen.
