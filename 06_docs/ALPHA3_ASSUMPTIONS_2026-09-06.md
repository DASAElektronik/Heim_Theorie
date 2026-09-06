# Werden Heims alpha3-Koeffizienten erzwungen?

2026-09-06, Etappe 19 ab df6934c; Plancheckpoint 5e92cda.

## Ergebnis

**Im untersuchten Buchabschnitt nicht.** H004, *Elementarstrukturen der
Materie II*, Druck272-275/PDF278-281, baut eine Familie von Formeln auf.
Auf Druck275 bezeichnet Heim die Koeffizienten ausdruecklich als frei
waehlbar und seine konkrete Wahl als an Elektron/Proton angepasst.
Das ist keine von uns aus einer Zahlenabweichung erschlossene Vermutung.

Die Familie ist nicht schon deshalb eindeutig, weil ihre Ausdruecke
dimensionslos und positiv sind oder bestimmte Grenzwerte besitzen. Wir
koennen jetzt einfache andere Exponenten angeben, die diese Eigenschaften
erhalten, aber andere Funktionswerte liefern. Das sind lokale mathematische
Zeugen, **keine vollstaendigen alternativen Heim-Loesungen** und kein Fit.

Die Aussage unterscheidet sich von einem Rechenfehler: Sind Heims gewaehlte
Koeffizienten einmal eingesetzt, folgt die in Etappe18 gefundene Buch-/Codeform
durch korrektes gewoehnliches Exponentieren. Offen ist die unabhaengige
physikalische Festlegung dieser Koeffizienten.

## 1. Welche Schritte welche Information liefern

Root hat Druck271-275/PDF277-281 vollstaendig bildlich gelesen; der
Quellenreview erfasst ausserdem Druck270 und den Abschluss(98c) auf278.

| Schritt im Buch | Status im eng geprueften Zusammenhang |
| --- | --- |
| alpha3=f(k)-qF(k,q), F=H+G, Druck271/272 | Ansatz fuer den Uebergang der dritten zur vierten Zone; nicht bloss eine Umformung bereits bekannter Funktionen. |
| f(1)=1 und die zusaetzliche funktionale Bedingung, Druck271/272 | Heim erhaelt daraus k*f=exp(k-1). Der Anfangswert allein wuerde f nicht bestimmen; die weitere Bedingung traegt Information. Keine allgemeine Validierung metronischer Integration durch unseren Check. |
| Additive logarithmische Variationen mit drei A- und vier B-Koeffizienten, Druck272/273 | Ansatzform mit nur von k abhaengigen Gewichten. Die Integration laesst diese Gewichte als Multiplikatoren der Logarithmen stehen. |
| Potentialgrenzen fuer H/G, Druck273/274 | Untere Grenzen werden induktiv vorgeschlagen. Fuer H wird 3V_beta=alpha*V_omegaepsilon angesetzt; fuer G bezeichnet Heim die Identifikation e*V_b=V_rhorho(k=q=1) ausdruecklich als spekulativ. Ein Feldproblem, das diese Festlegungen erzwingt, ist hier nicht rekonstruiert. |
| Sigma-Anschluss fuer C_k, Druck274 | Unter dem angegebenen Anschlussgesetz folgt C_k=2^(k-2) algebraisch. Dieser bedingte positive Befund betrifft C_k, nicht die Wahl aller A_i/B_i. |
| Rekursion X_n=X_(n-1)+X_(n-2), Druck272/275 | Der angenommene positive wachsende Rekursionszweig motiviert den Grenzwert Y=xi^2 mit xi=(1+sqrt(5))/2. Rekursion und Grenzregime sind Voraussetzungen; der Grenzwert bestimmt keine A/B-Koeffizienten. |
| Spezielle A/B-Werte, Druck275 | Explizit freie Vorgabe mit empirischer Motivation. Die vorangehende Logform liefert noch kein Gleichungssystem, das genau diese Wahl auswaehlt. |

Zum positiven C_k-Schritt: Mit s=k^2+1 und Q_sigma=2^(s-1)-1 wird

```text
(2*C_k)^(k+1) = (1+Q_sigma)/2 = 2^(k^2-1).
```

Fuer k>=1 und C_k>0 gibt es genau die Loesung C_k=2^(k-2), weil
k^2-1=(k+1)(k-1). Die Quelle setzt das Anschlussgesetz voraus; unsere
Algebra bestaetigt seine Folge, nicht seine physikalische Notwendigkeit.

## 2. Der allgemeine Ansatz und die gewaehlte Spezialisierung

Setze d=eta_qk, s=sqrt(d), Y=xi^2, C=alpha*(1+s)/3,
V=eta11/e und Z=2^k*((1-s)/(1+s))^2. C,V,Z sind hier nur Abkuerzungen.
H/G bezeichnen die alpha3-Korrekturen, nicht die KGH-Polynome der Masse.
Bei positiven alpha,eta11,e,d,Y und fuer G zusaetzlich d!=1 gilt:

```text
ln H = A1*ln C + A2*ln Y + A3*ln d,
ln G = B1*ln(V/d) + B2*ln Y + B3*ln d + B4*ln Z.

H = C^A1 * Y^A2 * d^A3,
G = (V/d)^B1 * Y^B2 * d^B3 * Z^B4.
```

Heim waehlt A=(1,(2k+1)/2,1-4k) und B=(1,k/2,k,1).
Fuer feste Koeffizienten sind die positiven Auswertungen eindeutig.
Die Existenz solcher Auswertungen bestimmt umgekehrt nicht die Koeffizienten.
Auch Dimensionsanalyse hilft hier nicht: Alle potenzierten Basen sind
dimensionslos. Ganzzahliges k erzwingt ebenfalls keine bestimmte Funktion von k.

## 3. Ein konkreter Nicht-Eindeutigkeitszeuge

Aendere nur A3 von 1-4k auf 2-4k oder nur B3 von k auf k+1. Es folgt exakt:

```text
H_neu = d*H_alt,       G_neu = d*G_alt.
```

Jede der beiden Aenderungen kann separat vorgenommen werden. Der Ansatz
bleibt derselbe; die Exponenten bleiben nur von k abhaengig und ganzzahlig.
A1=B1=B4=1 kann erhalten bleiben: H bleibt linear in alpha und G linear
in eta11. Fuer 0<d<1 sind die neuen Werte positiv und echt kleiner.
Die Identitaeten gelten fuer jedes feste positive xi, also auch wenn der
goldene Buchwert vorher feststeht; xi wird hier nicht als neuer Fitparameter benutzt.

Die formale Grenzbetrachtung d->1 bei festen uebrigen Groessen ergibt:

```text
H -> (2*alpha/3)^A1 * Y^A2,
G ~ (eta11/e)^B1 * Y^B2 * 2^((k-4)*B4) * |d-1|^(2*B4).
```

A3 und B3 verschwinden aus diesen fuehrenden Grenztermen. Die Aenderungen
erhalten deshalb sogar deren numerische Amplituden. G->0 fordert nur
B4>0; ein zusaetzlich verlangtes quadratisches Verschwinden wuerde B4=1
fixieren, aber noch nicht B3. Bei d=1 ist ln Z undefiniert: Gemeint ist
die stetige Fortsetzung des exponentierten Ausdrucks, nicht ln(0).

Das sind unsere Pruefbedingungen, keine behaupteten zusaetzlichen
Randvorgaben Heims. Ein kontinuierlich veraenderbares d ist ausserdem
kein nachgewiesener Weg durch seine diskreten q,k-Zustaende. Ebenso zeigt
q=0 im formalen Ausdruck nur das Wegfallen einer endlichen Korrektur;
unser Test mit synthetisch festem d ist keine physikalische q=0-Konfiguration.

## 4. Was ein einzelner passender Wert aussagt

Ein bekannter positiver H-Wert liefert bei festem k eine lineare Gleichung
in den Logarithmen, nicht automatisch drei unabhaengige Bedingungen fuer A.
Mit bereits festgesetztem A1=1 verbleiben normalerweise zwei Koeffizienten.

Rein synthetisches Beispiel, ausdruecklich keine Teilchenkonstanten:
k=1, alpha=1/2, xi=2, d0=1/4. Sowohl A=(1,3/2,-3) als auch
A=(1,5/2,-2) ergeben H=128. Am zweiten Punkt d=4/9 ergeben sie jedoch
405/16 bzw.45. Allgemein multipliziert A2->A2+t, A3->A3+t den Wert mit
(Y*d)^t, das am ersten Punkt genau1 ist.

Diese Ankerfamilie ist von der Grenzwertfamilie aus Abschnitt3 zu
unterscheiden: Sie erhaelt nicht zugleich jede fest vorgegebene Grenzamplitude.
Das Beispiel belegt lediglich die begrenzte Information eines Einzelankers.

Umgekehrt koennen genug unabhaengige Bedingungen Eindeutigkeit herstellen.
Bei festem A1 und Y=4 liefern etwa d=1/4 und d=1/16 fuer Verschiebungen
von (A2,A3) die Matrix ln(4)*[[1,-1],[1,-2]], deren Determinante ungleich0
ist. Eine solche zusaetzliche Information muss aber hergeleitet oder als
Kalibrierung ausgewiesen werden. Das ist keine Aufforderung zum Nachfitten.

Insbesondere ist eine bekannte Masse nicht automatisch ein bekannter
Einzelwert von H und G; ln(H+G) ist nicht ln H+ln G. Die drei A- und vier
B-Komponenten bei festem k sind deshalb **keine ermittelte Zahl von sieben
unabhaengigen globalen Fitparametern**. Ein Kalibrierungsprotokoll und die
uebrigen Modellkopplungen waeren dafuer gesondert zu untersuchen.

## 5. Konsequenz und naechster Schritt

FIND-031 dokumentiert eine lokale offene Begruendung mit expliziten
mathematischen Freiheitszeugen. Es ist weder eine empirische Widerlegung
noch der Nachweis, dass das ganze Werk keine weiteren Bedingungen enthaelt.

Fuer eine staerkere Herleitung muessten zusaetzliche, unabhaengig begruendete
Potential-, Variations- oder Randbedingungen diese Freiheiten beseitigen.
Der konkrete naechste Quellenauftrag ist der metronische Integrationsschritt
auf Druck273/274: Operatorregel, untere Grenzkorrektur und Potentialverhaeltnisse
aus(98) einzeln gegen die Definitionen pruefen. Dabei nicht still die Regeln
gewoehnlicher Differentialrechnung auf endliche metronische Schritte uebertragen.
Der frueher vorgemerkte H015-XIV/XXVI-Vergleich bleibt eine getrennte Aufgabe.

## Nachpruefung und Sicherung

Zwei begrenzte Reviews: Quelle und unabhaengige Mathematik. Root hat die
relevanten Buchvollseiten selbst gelesen und den eigenstaendigen Reviewcode
erneut ausgefuehrt: 389 gezaehlte exakte Fraction-Kontrollen bestanden.
Elf neue Tests in `tests/test_alpha3_assumptions.py`, insgesamt 144 Tests,
alle zehn bisherigen Rechenchecks samt Quellhashes bestanden. Kein neuer
Massenrechner, keine neue Ergebnissnapshot-Datei, kein Fremdprogrammlauf.

```powershell
py -3.13 -m unittest discover -s tests -p test_alpha3_assumptions.py -v
py -3.13 -m unittest discover -s tests -q
```

Quellenumfang und Suchgrenzen:
[Quellennotiz](../03_notes/ALPHA3_ASSUMPTIONS_SOURCES_2026-09-06.md).
Alle alten Rechner, Eingaben, Snapshots und Normalisierungen bleiben erhalten.
