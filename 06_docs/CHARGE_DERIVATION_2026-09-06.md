# Wie Heim von Ladungskomponenten zur Alpha-Naeherung gelangt

Stand:2026-09-06. Dritte, begrenzte Rekonstruktionsetappe.
Dieser Text erklaert Definitionen, Algebra und die noch offenen Annahmen.
Er ist keine vollstaendige Herleitung der Theorie und keine moderne
experimentelle Bewertung.

## Ergebnis vorweg

Die lokale Rechnung von BandI(27b)-(29a) ist nachvollziehbar:
`1/alpha_prime = 137.0380300128048...` reproduziert die dort gedruckte
Naeherung `137,038`. Dafuer braucht man jedoch die von Heim gewaehlten
Ladungskomponenten und zwei verschiedene Mittelungsschritte.

Ein korrektes Ausmultiplizieren bestaetigt diese Voraussetzungen nicht
automatisch. Die offene Frage lautet nun praeziser: Welche physikalische
Begruendung waehlt genau diese Komponenten und genau diese Mittelungen aus?

## 1. Was die Symbole bedeuten

Quelle ist *Elementarstrukturen der Materie*, BandI, dritte veraenderte
Auflage1998: Druck245,247,248 / PDF-Folios251,253,254. Titel/Impressum wurden
auf PDF3/4 geprueft; die Gleichungen werden nicht ungeprueft zurueckdatiert.
Hash und Fundstelle: [Band-I-Quellennotiz](../03_notes/EDM1_ALPHA_DEPENDENCIES_2026-09-06.md).

Wir nennen den Betrag von Heims theoretischer Ladung epsilon_pm hier
`e_roh`, die spaeter als beobachtbar angesetzte Ladung `e_eff`. Beide haben
Ladungseinheiten (Coulomb). Das ist nur eine gut lesbare Umbenennung:
`e_roh` bedeutet nicht automatisch die nackte Ladung der modernen QED.

`eta` ist dimensionslos. BandI(27) schreibt fuer gleichen n-Wert ein
Verhaeltnis zwischen geladenem und neutralem Massenterm:

```text
m(n,q) / m(n) = eta_q = pi / fourth_root(pi^4+4*q^4).
Fuer q=1: eta=eta_1=pi/fourth_root(pi^4+4) ~= 0.9899896408193424.
```

Das ist an dieser Stelle ein uebernommenes Ergebnis des vorherigen
Spektrumsansatzes. Wir haben dessen gesamte Herleitung noch nicht bewiesen.
Das einfach indizierte eta_1 nicht stillschweigend mit eta_11 identifizieren.

## 2. Der erste Schluss: ein reduzierter Ladungsbetrag

Heim nimmt Wechselwirkungs-Ausdruecke der Form

```text
V_xy(r) = e_x*e_y*f(r)
```

an. Mit seinem Coulomb-artigen f(r) hat V_xy die Dimension einer Energie,
also Joule, nicht eines elektrischen Potentials in Volt. Das ist fuer die
Interpretation wichtig, obwohl die Quelle diese Groessen Potentiale nennt.
Wir leiten hier nicht die physikalische Gueltigkeit oder das Vorzeichen von
f(r) her, sondern verfolgen den gemeinsamen Faktor in seinen Quotienten.

Fuer den Quotienten mit gleichem, nichtverschwindendem f(r) gilt

```text
V_rr / V_roh,roh = (e_r/e_roh)^2.
```

Heim setzt diesen Quotienten mit dem Energie-/Massenverhaeltnis eta bei
gleichem n und q=1 in Beziehung. **Unter dieser Annahme** folgt bei gleichen
Ladungsvorzeichen bzw. fuer Betraege:

```text
t = sqrt(eta)
e_r = e_roh*t.
```

Die Wurzel ist also kein willkuerlicher Rechenschritt. Sie folgt daraus,
dass das Modell eine Ladung im Produkt zweimal enthaelt. Die physikalische
Identifikation des Quotienten mit eta ist dagegen eine Voraussetzung.

## 3. Zwei zusaetzliche Komponenten

BandI(28a) setzt ferner

```text
e_d = e_roh - e_r = e_roh*(1-t)
e_w = (e_roh+e_r)/2 = e_roh*(1+t)/2.
```

Hier ist e_w ein **arithmetischer Ladungsmittelwert**. Dass gerade diese
Differenz und dieses Mittel physikalisch wirksame Komponenten sind, wird
im Text als Moeglichkeit eingefuehrt. Die Identitaet e_r+e_d=e_roh ist
algebraisch richtig, aber noch kein Nachweis zweier real separierbarer Ladungen.

## 4. Die zweite Mittelung: jetzt von Energien

Die beobachtbare Groesse soll nach der vorgeschlagenen Beziehung auf
Druck248 durch

```text
2*V_eff,eff = V_rr+V_ww
```

beschrieben werden. Nach Herauskuerzen desselben f(r) ergibt sich:

```text
e_eff^2 = (e_r^2+e_w^2)/2
e_eff/e_roh = sqrt([t^2+((1+t)/2)^2]/2).
```

Das ist ein **quadratischer Ladungsmittelwert**, nicht (e_r+e_w)/2.
Die zwei Mittelungen im Text sind deshalb nicht austauschbar.

Ein kleines, bewusst kuenstliches Lernbeispiel: Sind e_r/e_roh=1/2 und
e_w/e_roh=3/4, ergibt die arithmetische Ladungsmittelung5/8=0.625. Aus der
gleichen Energiemittelung folgt dagegen sqrt(13/32), etwa0.637377.
Die Differenz ihrer Quadrate ist exakt1/64. Dieses Beispiel prueft die
Algebra; es ist kein Heim-Messwert.

## 5. Woher 5*eta+2*sqrt(eta)+1 kommt

Setzt man die Komponenten ein, lautet die rein algebraische Vereinfachung:

```text
e_eff^2/e_roh^2
 = 1/2 * [eta + (1+sqrt(eta))^2/4]
 = [4*eta + 1+2*sqrt(eta)+eta]/8
 = [5*eta+2*sqrt(eta)+1]/8
 = vartheta/8.
```

Der Faktor5 ist in diesem lokalen Schritt also nachvollziehbar: vier eta
kommen aus der ersten Komponente, eines aus dem ausmultiplizierten Quadrat.
Die Formel fuer vartheta ist bei den gewaehlten Mittelungen korrekt.

## 6. Von der Ladung zu alpha_prime

BandI(27b) gibt fuer den Rohbetrag

```text
e_roh^2 = 9*hbar/(pi^4*R_vacuum).
```

Mit der ueblichen Beziehung
`alpha=e^2/(4*pi*epsilon0*hbar*c)` und `R_vacuum*epsilon0*c=1` folgt aus der
lokalen Rekonstruktion:

```text
alpha_prime = 9/(4*pi^5) * e_eff^2/e_roh^2
            = 9*vartheta/(32*pi^5)
            = 9*vartheta/(2*pi)^5.
```

Die hbar-, Impedanz- und Geschwindigkeitsfaktoren kuerzen sich **unter
diesen Voraussetzungen**. Das erklaert, warum diese Alpha-Naeherung nur noch
pi enthaelt; es beweist nicht die Voraussetzungen des Rohladungsansatzes.
Die SI-Alpha-Beziehung ist auch auf der
[NIST-Erklaerseite](https://physics.nist.gov/cuu/Constants/alpha.html) angegeben.
Wir verwenden dort nur diese Beziehung; andere Aussagen der historischen
Seite zum damaligen SI oder zur damaligen Messlage werden nicht uebernommen.

Die Rechnung liefert `1/alpha_prime=137.038030012804813...`.
Der Quellenwert137,038 ist damit auf seine angegebene Rundungsstelle
reproduziert. Alpha_prime ist die **vorlaeufige** Naeherung aus BandI, nicht
schon die spaetere Zweiggleichung mit sqrt(1-alpha^2) und Y3 aus BandII.

## 7. Was passiert, wenn die gleiche Gewichtung nicht vorausgesetzt wird?

Als eigene logische Diagnose halten wir e_r und e_w fest und ersetzen nur
die zweite Mittelung durch:

```text
e_eff^2(lambda) = lambda*e_r^2+(1-lambda)*e_w^2, 0<=lambda<=1.
```

Lambda ist **unser kuenstlicher Diagnoseparameter**, kein neu entdeckter
Parameter Heims. Es gibt keinen Fit an einen Messwert. Die fuenf Gewichte
sind vorab als0,1/4,1/2,3/4,1 festgelegt. Der Buchansatz liegt bei1/2.

| Gewicht des e_r-Energieanteils lambda | 1/alpha_prime(lambda) | Rolle |
|---|---:|---|
| 0 | 136.693786161170 | Eigener Diagnosefall |
| 1/4 | 136.865691627259 | Eigener Diagnosefall |
| 1/2 | 137.038030012805 | Quellenspezialisierung |
| 3/4 | 137.210802955240 | Eigener Diagnosefall |
| 1 | 137.384012100262 | Eigener Diagnosefall |

Alle Glieder dieser gebauten Familie besitzen passende Einheiten. Daraus
folgt keine physikalische Zulaessigkeit und auch kein Unsicherheitsintervall
der Theorie. Es zeigt nur: Die Einheitenrechnung alleine waehlt lambda1/2
nicht aus. Eine physikalische Begruendung muss mehr leisten.

Auch die **erste** Mittelung zur Konstruktion von e_w bleibt eine Annahme;
diese Diagnose variiert sie gerade nicht. Daher ist die Familie weder die
vollstaendige Menge moeglicher Alternativen noch eine neue Theorie.

## 8. Quellenketten und Fortsetzung

Die separate Quellenpruefung verfolgt die zweifache eta-Indizierung und den
spaeteren Korrelationsschluss. Ihre Ergebnisse werden hier nach Kontrolle
integriert. Bis dahin keine Aenderung der bisherigen IGW-Indexprofile.

Offene Begruendungsfragen fuer unsere weitere Arbeit:

1. Warum laesst sich das betrachtete Massenterm-Verhaeltnis mit genau diesem
   Potential-/Energiequotienten identifizieren?
2. Welches Prinzip bestimmt e_w als gleichen Ladungsmittelwert?
3. Warum werden gerade V_rr und V_ww gleich gewichtet, und welche Rolle
   haben andere moegliche Komponenten/Kreuzterme?
4. Wie verbindet die spaetere Korrelationsannahme diese Konstruktion mit
   einer physikalisch definierten beobachtbaren Groesse?

## Reproduzierbarkeit

```powershell
py -3.13 scripts/audit_charge_averaging.py --check --verify-sources
py -3.13 -m unittest discover -s tests -v
```

Rechner und Daten sind vom ersten Alpha-Audit und der Y3-Inversion getrennt.
Die neue Diagnose importiert keine modernen Referenzwerte, fittet nichts und
veraendert keine Quellwerte. Normalisierungsentscheidung:
`NORM-CHARGE-001`; Ergebnisse: `05_analysis/charge_averaging_diagnostics.json`.
Unabhaengige Mathematikreview ist fuer diesen Zwischenstand noch offen.
