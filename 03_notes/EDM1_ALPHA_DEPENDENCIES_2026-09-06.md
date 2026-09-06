# Band I: Rueckverfolgung der Alpha-Abhaengigkeiten

Stand: 2026-09-06. Begrenzte Quellenpruefung des Hauptagenten, keine
vollstaendige Rekonstruktion oder physikalische Bewertung.

## Quelle

Burkhard Heim, *Elementarstrukturen der Materie*, Band I, lokaler Scan
`01_sources/heim_primary/Burkhard Heim - 1998 - Elementarstrukuren der Materie 1.pdf`.
[Archivfundstelle](https://burkhardheim.de/assets/Burkhard%20Heim%20-%201998%20-%20Elementarstrukuren%20der%20Materie%201.pdf).
SHA256: `49C79028C4F5B4FEE97F0541EF1655C37755C3C3C2FD3A10DD6E72CB454DE459`.

Titel/Impressum laut Textauszug: dritte, veraenderte Auflage, Innsbruck 1998;
Copyright 1980, Manuskripteinreichung 17.09.1978. Fuer diese bibliographischen
Angaben steht die Bildkontrolle noch aus. Daraus folgt insbesondere keine
unveraenderte Ueberlieferung der folgenden Formeln seit 1978/1980.

Visuell geprueft: PDF-Folios 253 und 254 (einsbasiert), Druckseiten 247/248.
Renderdateien, absichtlich nicht versioniert:
`tmp/pdfs/book1_trace/page-253.png` und `page-254.png`.

## Was sich jetzt belegen laesst

Auf Druckseite 247 wird `eta_1 = eta` gesetzt. (28a) gibt

```text
eta * fourth_root(4 + pi^4) = pi
e_r = epsilon_pm * sqrt(eta)
e_d = epsilon_pm * (1 - sqrt(eta))
2*e_w = epsilon_pm * (1 + sqrt(eta))
```

Damit ist der im Alpha-Audit verwendete **unindizierte** eta-Ausdruck in
dieser Band-I-Ausgabe explizit belegt. Das einfach indizierte `eta_1` ist
nicht ohne weiteren Beleg mit `eta_11` der zweifach indizierten Familie
gleichzusetzen. Die Definition der zwei Indexpositionen bleibt offen.

Der Text auf Seite 247 motiviert Ladungskomponenten und ihre Potentiale
aus einer bereits bemerkten Abweichung zwischen theoretischer und gemessener
Elementarladung. Er kennzeichnet die vorgeschlagenen Beziehungen selbst als
spekulativ bzw. als moegliche Annahmen. Auf Seite 248 wird das arithmetische
Mittel `2*V_ee = V_rr + V_ww` als moegliche Konzeption eingefuehrt.

Mit gleichen Zentralfeldfaktoren folgt algebraisch:

```text
2*e_pm^2 = e_r^2 + e_w^2
           = epsilon_pm^2 * (4*eta + (1+sqrt(eta))^2)/4
vartheta = 5*eta + 2*sqrt(eta) + 1
```

Die letzte Vereinfachung ist nachvollziehbare Algebra. Die Auswahl gerade
dieses Mittelwerts ist damit noch nicht aus einem Grundprinzip bewiesen.
Die fuer Band II referenzierte Beziehung (29) steht hier zusammen mit der
expliziten vartheta-Definition. (29a) lautet `(2*pi)^5 * alpha_prime = 9*vartheta`.
Die Quelle nennt den vorlaeufigen Wert `1/alpha_prime = 137,038` und dessen
Abweichung von damaligen Messdaten; Band II soll diese Diskrepanz beheben.

## Bedeutung fuer das Verstaendnis

Die Rueckverfolgung schliesst einen Teil der Definitionskette:

```text
Band I (28a): unindiziertes eta
  -> gewaehlte Ladungskomponenten und Potential-Mittelung
  -> Band I (29): vartheta, Elementarladungsansatz
  -> Band I (29a): vorlaeufige Alpha-Naeherung
  -> Band II (105): Korrelationskorrektur mit offenem Y3
```

Dies ist eine **gemischte Kette aus Definitionen, Algebra und Annahmen**.
Dass eine spaetere Stelle (29) als exakt bezeichnet, macht die zuvor
gewaehlte physikalische Mittelung nicht nachtraeglich zu einem Beweis.
Umgekehrt ist eine offen formulierte Annahme allein noch keine Widerlegung.

Die bekannte Abweichung gehoert zur Entwicklungsmotivation; daraus folgt
nicht, dass jeder Koeffizient empirisch angepasst wurde. Der behauptete
Vorhersagestatus ist gesondert anhand datierter Unterlagen zu pruefen.

## Noch erforderlich

- Herleitung und Bedeutung der einfach und zweifach indizierten eta-Familien
  aus (27) und den spaeteren Konfigurationsregeln; keine Indexwahl nach Fit.
- Begruendung fuer die Ladungs-/Potential-Mittelung und den Uebergang zum
  Korrelationsansatz in Band II, Druckseiten 297-301.
- Fruehere Ausgabe oder Begleitheft fuer einen belastbaren Editionsabgleich.
- Keine allgemeine Widerlegungsrecherche: gemeldete Nutzerprioritaet ist
  zuerst Rekonstruktion/Verstaendnis, danach externe physikalische Bewertung.
