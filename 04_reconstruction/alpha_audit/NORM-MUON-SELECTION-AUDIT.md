# Bedingter H006-x3-Auswahlvertrag ohne Masse

2026-09-06, Etappe26; vorab festgelegt in Plancheckpoint `d960144`.
Ergaenzender enger Rechenvertrag, keine Aenderung der 49 CSV-Entscheidungen.

## Quelle, Zustand und Grenzen

H006 ist die IGW-Wiedergabe 2002/2003 eines auf 25.2.1982 datierten,
Heim zugeschriebenen Textes. Keine hier authentifizierte Urschrift.
PDF-Pfad/Hash und Scope sind in `muon_selection_inputs.json` fixiert.
H006 Druck/PDF3 (III): x3(0111), epsilon=+1,k=1,B=0,P=Q=kappa=1,C=0.
Die beiden Stellen x=0,1 geben nach (II) qx=-1, q=1. Die Quelle zieht
(-1,-1) zu (-1) zusammen; physikalische Multiplizitaet nicht hergeleitet.
Die Signatur ist keine Besetzung. N=0/f=0 kommt separat aus Druck/PDF8.

Nur gruppierter XV/XXVI/XXX/XXXI-Pfad; abweichendes XIV nicht verwendet
oder still berichtigt. Das bekannte Elektronprofil bleibt unveraendert.
Es wird keine Masse, Resonanz, Messgroesse oder Sollbesetzung eingelesen.

## Profile vor Ergebnis festgelegt

Die drei alten H006-Zahlenprofile werden unveraendert uebernommen:

| ID-Kurzform | pi, e in Koeffizienten | xi |
|---|---|---|
| M | mathematische Werte | 1.61803399 |
| G | mathematische Werte | (1+sqrt(5))/2 |
| D | 3.1415926535, 2.71828183 | 1.61803399 |

Natuerliches exp/ln bleibt in allen Profilen mathematisch definiert;
gedrucktes e ist nur ein Koeffizienteneingang. Nacktes alpha und beta
kommen aus `1982_source_literal`, mit eta12=(k=1,q=2), nicht aus
gedruckter Alpha-Loesung oder Messwert. eta=pi/(pi^4+4)^(1/4), dagegen
d=eta11=pi/(pi^4+5)^(1/4); s=sqrt(d). Keine Gleichsetzung eta=d.

A16-P (alter Default): (pi*e)^2*[1+alpha*(1+6alpha/pi)/(5eta)].
A16-L (Sensitivitaet): (pi*e)^2*[1+(alpha*(1+6alpha/pi)/5)*eta].
Die kompakte Slashzeile auf H006p7 erzwingt diese Klammerung nicht.
Andere Matrix-Slashbindungen folgen dem bestehenden Nennerproduktvertrag.

alpha3-Wurzel I (alter Default): sqrt(xi*d).
alpha3-Wurzel O (Sensitivitaet): sqrt(xi)*d.
Der JSON-Name `sqrt_xi_times_d` bezeichnet ausdruecklich sqrt(xi*d).
Alle 3*2*2 Kombinationen werden ausgewiesen. Keine H004-/H010-alpha3-
Ersetzung und keine Auswahl anhand eines kleineren Rests oder Massentreffers.

## Reduzierte, bedingte Formeln

Mit a_i=alpha_i aus H006(IX), nicht nacktem alpha:

```text
a1 = (1+s)/2; a2 = 1/d
a3 = 1 - alpha*xi^3*(1+s)^3/(3*d^3)
       - 2*root/e * ((1-s)/(1+s))^2
A26 = 2*[1-pi*(e*xi*alpha)^2*sqrt(eta)/2]/(e*xi^2)
A31 = (pi*e*alpha)^2*[1-(pi*e)^2*(1-beta^2)]
w1 = d*A16; w2 = A26+d^2*A31
w = 1+w1
g = 27*a1+9*a2+2*a3+exp(-1/3)
W = g*w
Q_j = (3,3,2,1); K_j = n_j+Q_j
```

Die weggefallenen Klammern bleiben an ihre Definitionsbereiche gebunden:
eta,d,alpha,pi,e,xi/beta-Divisionen, A24/A36-Nenner, 3-q und
8-A66^[q(q-1)] werden geprueft; XVIII-A24-Nenner wird 1. Die getrennte
XVI-Schreibweise 1-A24 wird nur als Domainkontrolle, nicht als aktiver
XVIII-Term benutzt. w2 und 1+w2 bleiben definiert und positiv. Auch
Resonanznenner A41/A61/XXIII werden geprueft, ohne N>0 auszuwerten.
Kein 0*undef-Wegkuerzen. Die Quelle nennt die A-Matrix einen Vorschlag;
der Formelanschluss ist keine physikalische Herleitung ihrer Eintraege.

K1..3 sind successive maximale nichtnegative Ganzzahlen bei Potenzen3,2,1.
Fuer den erreichten Fall(b): r=W4 in(0,1], rawK4=-3ln(r), K4=floor(rawK4).
Keine Neunerfolgen-Promotion. Sonderfaelle(a,c) wuerden eine separate
Auswertung verlangen, nicht automatisch durch eine eigene Regel ersetzt.
XIII (rechts weiterhin a3*K1^3) und XXXII getrennt pruefen. Eine
Zonenuebertragung nicht allein aus vorhandenen Ungleichungen erfinden.

## Reproduzierbarkeit und Aussagegrenze

`scripts/audit_muon_selection.py` verwendet nur reine Alpha-Hilfsarithmetik
aus `audit_alpha.py`, nie dessen Messvergleich oder einen Massenevaluator.
Zustand, Quellenmetadaten, Profile und Scope sind gegen stille Aenderung
gesperrt; Input-Hash wird mitgeschrieben. Lokaler PDF-Hashcheck ist explizit
`--verify-sources`; Snapshotgleichheit allein ist kein Quellencheck.

80/120-Stellenstabilitaet und unabhaengige 120/160-Stellenrechnung sind
keine gerichteten Intervalle und keine physikalische Unsicherheit.
Alle Angaben gelten nur unter diesem festgelegten Vertrag. Ergebnis:
`06_docs/MUON_SELECTION_2026-09-06.md`, `05_analysis/muon_selection_results.json`.
