# alpha3/N3 in H007, H013 und H014

Stand: 2026-09-06, Etappe 18 ab `a989f03`.

## Ergebnis

H013 und H014 enthalten eine positive, direkte Vorstufe zu H007(B8):
beide definieren `N3` logarithmisch in (8c). Nach den unmittelbar
gedruckten Substitutionen `u=2*pi*e` und `3*omega=4*c` ist die Form von
H007(B8) algebraisch dieselbe. Alle drei Fassungen verbinden sie spaeter
durch `2*alpha3=N3` mit dem Auswahlkoeffizienten `alpha3`.

Diese Formel ist aber nicht die H006(IX)-Formel in anderer Klammerung.
Sie enthaelt weder deren potenziertes Produkt mit `xi` noch deren
Wurzelglyph vor `xi eta_qk`. Daher entscheiden H007/H013/H014 weder den
Potenzbereich noch die Radikandgrenze des H006-H010-Unterschieds.

## Quellenstatus und Vollseiten

- H007, `Erweiterte_Massenformel_Nach_Heim_1989.pdf`: IGW-Wiedergabe
  2002/2003 eines berichteten Manuskripts 1989, kein Originalfaksimile;
  geprueft Druck12/PDF3 (B8) und Druck15/PDF6 (B40).
- H013, `eta22_context/J0033-Heim_Ausgewaehlte-Ergebnisse-b.pdf`:
  undatierter autorbezeichneter Scan; Druck14-15/PDF15-16, Druck17/PDF18.
- H014, `eta22_context/J0032-Heim_Ausgewaehlte-Ergebnisse-a.pdf`:
  getrennte undatierte autorbezeichnete Fassung; Druck9-10/PDF9-10,
  Druck12/PDF12.

Tragende Bilder:
`tmp/pdfs/eta22_context/j0033-render-15.png`, `j0033-render-16.png`,
`j0033-render-18.png`,
`tmp/pdfs/alpha3_origin/h014-09.png`, `h014-10.png`, `h014-12.png`,
und `tmp/pdfs/eta22_roles_igw/h007-pre-03.png`, `h007-06.png`.

Der PDF-Skill wurde gelesen; Hauptbeleg sind die visuell geprueften Seiten.

## Homologe Formel

H013(8c) und H014(8c) schreiben, mit `r=alpha-/alpha+` nur als
Lesekuerzel:

```text
ln(N3*k/2) = (k-1) * [1 - pi*(1-eta_qk)/(1+sqrt(eta_q1))
  * {1-u*eta_q1/vartheta_q1*(1-r)*(1-sqrt(eta))^2}]
 - omega/(c*u)*(1-sqrt(eta))^2
  * [2*c*u^2/(omega*vartheta)
     *(1+sqrt(eta_q1))/(1-eta)-1].
```

Direkt darunter steht in beiden Fassungen (8c1)

```text
u=2*pi*e,       3*omega=4*c.
```

Damit folgen exakt

```text
omega/(c*u) = 2/(3*pi*e),
2*c*u^2/(omega*vartheta) = 6*pi^2*e^2/vartheta.
```

Das sind die zwei entsprechenden Faktoren in H007(B8). H007 ist hier
eine algebraisch eingesetzte Darstellung derselben N3-Form, nicht ein
Beleg fuer eine weitere Herleitung.

H013 Druck17/PDF18 (11a) und H014 Druck12/PDF12 (11a) setzen `alpha1=N1`,
`2*alpha2=3*N2`, `2*alpha3=N3` und nennen sie „neue Koeffizienten“.
H007 Druck15/PDF6 (B40) schreibt `alpha3=1/2*N3`.

## Bezug zu H006 und H010

H007 Druck12/PDF3 sagt vor (B8), `N1` und `N2` lauteten wie in H006(IX),
und fuehrt danach die „uebrigen Ni mit i>2“ neu auf. Der Rueckverweis auf
H006(IX) uebernimmt also gerade nicht dessen alte `N3=2*alpha3`-Formel
einschliesslich des dortigen algebraischen Ausdrucks fuer `alpha3`.

H006(IX) besitzt im ersten Korrekturterm

```text
[(1+sqrt(eta_qk))*(xi/eta_qk^2)]^(2k+1),
```

waehrend H010-Pascal383/C807 `1+sqrt(eta_qk)` ausserhalb dieser Potenz
setzt. H006 zeigt im zweiten Term ein Wurzelglyph vor `xi eta_qk`;
H010-Pascal384/C808 schreibt ohne Wurzel `(2*xi*eta_qk)^k`.

In (8c)/(B8) fehlen beide homologen Teilausdruecke und `xi` insgesamt.
Auch fuer `k=1` ist die neue N3-Form keine Entscheidung zwischen den
alten Varianten: Der mit `k-1` multiplizierte erste Block verschwindet,
der zweite, anders aufgebaute Block bleibt bestehen.

## Erklaerungs- und Suchgrenze

Die geprueften Manuskriptseiten sagen, die Funktionen `N1..N6` haingen
von `k,q` ab, geben (8a)-(8f) an und fuehren spaeter „neue Koeffizienten“
ein. Sie zeigen auf diesen Seiten keine Ableitung von H006-alpha3, keine
Begruendung der H010-Klammerform und kein Erratum zur alten Wurzelstelle.

Positiv belegt ist daher eine H013/H014-(8c)-zu-H007(B8)-Formelbruecke,
nicht die Herkunft der zwei H010-Aenderungen. Die Suche war auf die
direkten N_i-Definitions- und alpha3-Anschlussseiten begrenzt; daraus
folgt keine Aussage, dass im gesamten Nachlass keine Herleitung existiert.
Aus den undatierten H013/H014-Scans wird keine Reihenfolge untereinander
oder gegen das berichtete Manuskriptjahr von H007 abgeleitet.
