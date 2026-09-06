# NORM-LORENTZ-MEANING-001

Stand2026-09-06. Lokale Implementierungsgrenze; Review vor Abschluss.

## Drei getrennte Untersuchungen

1. Eigener gewoehnlicher passiver Lorentzboost in der reellen Reihenfolge
   (ct,x) bzw. (epsilon,q): L=[[gamma,-gamma*b],[-gamma*b,gamma]].
   b=u/c ist die Geschwindigkeit zweier Bezugssysteme, NICHT automatisch
   Heims alpha oder die Geschwindigkeit des Teilchens in jedem System.
   J=diag(1,-1), L^T*J*L=J. Fuer einen normierten massiven Vierimpuls gilt
   epsilon=E_tot/(m0*c^2), q=p_x/(m0*c), epsilon^2-q^2=1.
   Positive pc-Groesse ist |q|, Vergleichs-T ist epsilon-1.
2. Eigener statischer Kreis in einem Inertialsystem, R=1 als Laengeneinheit.
   Die gleichzeitige Sektion ct'=0 waehlt ct=b*x. Dann x'=x/gamma, y'=y.
   Keine Modellierung einer rotierenden, gravitativen oder strukturellen Schale.
   Fuer s=1/gamma und 0<|b|<1 gilt fuer Umfangsverhaeltnis P:
   (1+s)/2 < P < sqrt((1+s^2)/2). Obere Schranke als Quadrat speichern.
3. Source-literaler EDM1-p21-Block in (x1,x4), x4=ict:
   [[cos(psi),i*sin(psi)],[-i*sin(psi),cos(psi)]], tan(psi)=i*b.
   Unter gewoehnlicher analytischer Trigonometrie und kontinuierlichem
   Vorzeichenzweig bei b=0 wird er zu [[gamma,-gamma*b],[gamma*b,gamma]].
   Sein Produkt mit dem TRANSponierten ist ((1+b^2)/(1-b^2))*I, nicht I.
   Der Rechner behaelt diesen Block als Diagnose, nicht als Lorentzboost.
   Komplex-orthogonal heisst Transposition, nicht hermitesche Konjugation.

## Quellenbasis und Varianten

Heim EDM1 Druck12/PDF20, Druck21/PDF29 (Literalblock), Druck81/PDF88,
Druck288/PDF294; EDM2 Druck300/301/PDF306/307. Root hat die Kernseiten
visuell geprueft. Die Substitution tan(psi)=i*b benutzt eine gewoehnliche
Trigonometriekonvention und ist explizit BEDINGT. Kein stiller Quellenfix.
Weiterer Quellenkontext EDM1 Druck56/PDF63 wird getrennt gegengeprueft.
Der reelle Standardboost ist eine eigene Referenzkonstruktion; in
Einstein1905 Druck902/PDF12 sind die dazugehoerigen Koordinatengleichungen
visuell belegt, Druck903/PDF13 beschreibt die gleichzeitige Ellipsoidform.

Alle Beispielwerte werden exakt als Fraction berechnet. Die Hilfsfunktionen
akzeptieren nur rationale b mit |b|<1 und rationalem gamma; andere b werden
ehrlich abgelehnt. Das ist eine Rechenbeschraenkung fuer exakte Beispiele,
keine physikalische Auswahlregel. Feste Hauptdiagnose b=3/5, keine Messwerte.
Nullboost ist fuer Identitaets-/Grenztests zulaessig; Umfangsgrenzen dort
nicht strikt. Nicht alle inneren Algebrahelfer sind allgemeine Physik-APIs.

## Outputs und Nichtziele

`scripts/audit_lorentz_meaning.py` und `05_analysis/lorentz_meaning_diagnostics.json`:
exakte Boosttabellen, Metrikpruefung, Kreis-Ereignisse und Literalblocktest.
Keine Herleitung des gesamten A_-/R6-Modells, keine Atomrechnung, keine
Kalibrierung, kein Nachweis der Autorenabsicht. Alte Profile unveraendert.
Bei nicht eindeutiger Notation muss die Abweichung in Berichten stehen bleiben.
