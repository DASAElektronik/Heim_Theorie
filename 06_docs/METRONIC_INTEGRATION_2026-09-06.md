# Metronische Integration: exakte Grenzen, bedingte Logarithmen

2026-09-06, Etappe 20. Ausgang bb24534, Plancheckpoint 2b12a48.
Untersuchter Ausschnitt: H003 M2/M2a/M3a/M7/M8 und H004 II267,272-275.
Keine neue Massenrechnung, keine Gesamtwiderlegung und kein neuer Fit.

## Ergebnis

Die bisher auffaellige untere Grenze `z-1` ist erklaert: Sie folgt exakt
aus Heims Rueckwaertsdifferenz und inklusiver metronischer Summation.
Auch die vier Potentialquotienten der H/G-Logformen lassen sich aus
seinen gesetzten Endpotentialen und (98) algebraisch rekonstruieren.

Die Logarithmusregel ist dagegen schon in Band I ausdruecklich eine
Naeherung. Unter der dortigen unskalierten Rueckwaertsdifferenz wird der
relative Sprung der in Band II benutzten Fibonacci-Folge X bei grossem
Index nicht klein. Allein die dort angefuehrte grosse Metronenzahl macht
diesen Austausch daher weder exakt noch relativ beliebig genau.

Das ist ein konkreter, bedingter Einwand gegen diese Begruendung, noch
kein berechneter Fehler von alpha3 oder einer Teilchenmasse: Die genaue
Verbindung zwischen delta und delta_e sowie die gemeinsame Fehlerbilanz
von X, Potentialen und H/G fehlen fuer eine solche Aussage.

## 1. Welche Rechnung definiert Heim?

H003 Druck103/PDF109, M2, definiert fuer den Einheitsschritt

    delta F(n) = F(n)-F(n-1).

Die inklusive Summe M2a auf Druck104/PDF110 liefert deshalb

    sum_(n=a)^b delta F(n) = F(b)-F(a-1).

Die Quelle setzt hier a>=1,b>a. In unseren Zeugen sind alle benoetigten
Nachbarwerte definiert. Insbesondere fuer positives X:

    sum_(n=z)^(z+1) delta ln X(n)
      = ln X(z+1)-ln X(z-1)
      = ln[X(z+1)/X(z-1)] = ln Y.

Genau diesen Ausdruck druckt H004 II273/PDF279. Es werden zwei
Rueckwaertsdifferenzen addiert; der Nenner X(z-1) ist kein nachgewiesener
Druckfehler. Dieser Schritt braucht keine Kleinheitsnaeherung.

Weitere exakte Regeln zeigen, warum gewoehnliche Ableitungsregeln hier
nicht ohne Pruefung gelten. M3a (I105/PDF111) enthaelt den Zusatzterm

    delta(uv) = u*delta v + v*delta u - delta u*delta v,

und M8 (I110/PDF116) verwendet einen endlichen dividierten Quotienten:

    delta f(V) = [f(V)-f(V-delta V)]/delta V * delta V.

Fuer delta V!=0 ist der Quotientenfaktor im Allgemeinen nicht f'(V).
Beispiel f(V)=V^2: Er ist 2V-delta V, nicht 2V.

## 2. Was leistet die Korrektur der unteren Grenze?

Soll F(b)-F(a) herauskommen, muss die inklusive Summe bei a+1 anfangen.
Bei einem Potentialpfad gilt dann exakt

    V_(a+1) = V_a + delta V_(a+1),

nicht allgemein V_a+delta V_a. Fuer das synthetische V_n=n^2,a=3 waeren
das 16 gegenueber 14. Die allgemeine diskrete Randverschiebung ist damit
verstanden; die richtige Indizierung gehoert aber zur Anwendung.

H004 II274/PDF280 fordert, zur unteren Potentialgrenze die metronische
Variation delta_e des Potentials zu addieren, versieht diese Anweisung
jedoch nicht mit einem Schrittindex. Wir erklaeren daraus weder jede
Potentialgrenze fuer exakt bewiesen noch das Pluszeichen fuer falsch.
Die indizierte Umsetzung und die Wirkung von delta_e bleiben zu klaeren.

## 3. Wo beginnt die Naeherung?

H003 I109/PDF115, M7, fuehrt delta_e=a_scale*delta ein und gibt fuer
eine kleine skalierte Variation die Regeln ausdruecklich approximativ an:

    delta_e V approx V*delta_e ln V,
    delta_e exp(V) approx exp(V)*delta_e V.

a_scale ist hier unser unterscheidender Name fuer den Quellfaktor a,
kein neuer physikalischer Parameter. H004 II272/273 nennt die
Groessenordnung sqrt(tau) fuer Ladungsvariationen und verwendet daneben
den unskalierten X-Schritt. Die Absicht einer Naeherung ist also belegt;
ihre ausreichende Genauigkeit fuer den konkreten Pfad damit noch nicht.

Fuer positive skalare Nachbarwerte V_n,V_(n-1) und
r=delta V_n/V_n<1 gilt exakt

    delta ln V_n = -ln(1-r) = r+E(r),
    E(r) = -ln(1-r)-r
         = r^2*integral_0^1 u/(1-r*u) du >= 0.

Bei |r|<=rho<1 folgt die kontrollierbare Schranke

    r^2/[2(1+rho)] <= E(r) <= r^2/[2(1-rho)].

Sie gilt auch fuer negative r; E(r)>0 ausser bei r=0. Bei mehreren
Schritten und moeglicherweise negativen festen Gewichten gilt

    abs(sum_i w_i E(r_i)) <= sum_i abs(w_i)*r_i^2/[2(1-rho)].

Das ist eine eigene mathematische Fehlerkontrolle, keine aus dem Buch
uebernommene physikalische Genauigkeitszusage.

Wird delta_e woertlich als derselbe skalare Multiplikator a_scale*delta
auf allen Ausdruecken gelesen, dann ist der vorzeichenbehaftete Rest
a_scale*E(r), sein Betrag also |a_scale|*E(r). Fuer a_scale!=0 und r!=0
bleibt dessen Verhaeltnis zum Betrag von delta_e V/V gleich E(r)/|r|.
Bei r=0 ist die Logregel exakt; dieser relative Quotient ist dann 0/0.
Kleineres a_scale verbessert dann nicht die relative Genauigkeit.
Eine echte Verkleinerung des Argumentversatzes V(x)-V(x-h) kann dagegen
r=O(h) und E=O(h^2) liefern. Dieser Operator ist nicht allgemein h*delta_1.
Eine solche Praezisierung ist gesondert zu belegen; sie darf nicht als
stille Reparatur der Quelle eingesetzt werden. M7 wird hier nicht fuer
jede denkbare metronische Interpretation pauschal verworfen.

## 4. X: Warum eine grosse Zahl nicht genuegt

H004 II272 nennt X_n=X_(n-1)+X_(n-2); II275 benutzt fuer den wachsenden
Zweig X_n/X_(n-1)->xi=(1+sqrt(5))/2. Unter M2 folgt daraus

    delta X_n/X_n -> 1-1/xi = 1/xi^2,
    delta ln X_n  -> ln xi.

| Ausdruck | Grenzwert, gerundet |
|---|---:|
| Ein relativer Rueckwaertsschritt | 0.381966011250105152 |
| Ein logarithmischer Rueckwaertsschritt | 0.481211825059603447 |
| Summe zweier relativer Schritte z..z+1 | 0.763932022500210304 |
| lnY im selben Grenzfall | 0.962423650119206895 |
| Differenz der beiden Zweischrittausdruecke | 0.198491627618996591 |

Der relative Sprung geht nicht gegen null. Der Austausch delta X/X
durch delta lnX wird unter diesen Annahmen auch fuer z->unendlich nicht
beliebig genau. Dies ist der enge Konflikt FIND-032. Die exakte
Teleskopie von delta lnX zu lnY bleibt davon unberuehrt.

Wichtige Reichweitengrenze: Wenn im vereinfachten gemeinsamen
Schrittmodell r_H=sum_i A_i*r_i gilt, dann ist der ganze Logrest

    delta lnH - sum_i A_i*delta lnV_i
      = E(r_H)-sum_i A_i*E(r_i).

Andere Reste koennen sich aufheben, insbesondere bei gemischten
Gewichtsvorzeichen. Das Modell ist nur eine Erlaeuterung der fehlenden
Bilanz, keine ungepruefte Gleichsetzung der gemischten delta/delta_e
in H004. Aus dem isolierten X-Rest folgt weder eine bestimmte
alpha3-Abweichung noch ein Prozentfehler einer Masse.

## 5. Die vier Potentialquotienten

H004 II267/PDF273 setzt bei gemeinsamem Abstand r
4*pi*epsilon0*V_xy=e_x*e_y*f(r). Mit d=eta_qk,s=sqrt(d) liefert (98)
e_rho=epsilon*s, e_omega=epsilon*(1+s)/2, e_delta=epsilon*(1-s).
epsilon-Zweig, Radius und gemeinsamer Proportionalitaetsfaktor werden
in den Quotienten festgehalten. rho ist der Potentialindex, nicht q.

| Anteil | Gesetzte Endpunkte auf II274 | Folgender Quotient |
|---|---|---|
| H, A1 | 2V_alpha=V_epsilon; 3V_beta=alpha*V_(omega,epsilon) | V_beta/V_alpha=alpha*(1+s)/3 |
| H/G, A3/B3 | V_epsilon nach V_(rho,rho) | d |
| G, erster Anteil | Va=V_(rho,rho)(q,k); eVb=V_(rho,rho)(1,1) | eta11/(e*d) |
| G, B4 | Wa=V_(omega,omega); Wb=2^(k-2)*V_(delta,delta) | 2^k*((1-s)/(1+s))^2 |

Beim letzten Quotienten stammt ein Faktor 4 aus dem quadrierten
Verhaeltnis e_delta/e_omega. Beim dritten ist e die Eulerzahl, keine
Ladung; der Potentialstrich bezeichnet k=1, keine Ableitung. Die
Abklingannahme e^-1 wird im Buch selbst spekulativ eingefuehrt.

Die Quotienten bestaetigen die bedingte Endpunktalgebra, nicht die
Eindeutigkeit der Grenzen, die Logarithmusnaeherung oder die empirische
A/B-Wahl. Quellengetreu zu vermerken ist ausserdem: II274 druckt vor
dem ersten G-Logarithmus B'_1, II273 und II275 verwenden B1. Eine
lokale Gleichsetzung ist nicht angegeben; die Endform benutzt effektiv
Exponent 1. Kein neuer unabhaengiger Parameter oder Erratum wird daraus
abgeleitet. Fruehere ungestrichene Kurznotation ist insofern bedingt.

## 6. Nachpruefung, Sicherung und naechster Auftrag

Zwei begrenzte Quellenreviews und eine unabhaengige Mathematikreview;
Root hat die tragenden Vollseiten selbst gelesen. Der eigenstaendige
Reviewcode wurde von Root erneut ausgefuehrt: exakte Fraction-Identitaeten
und 13 numerische Felder bei 80/120 Stellen, maximale relative Differenz
3.072074353802e-80. Das ist Rechenstabilitaet, keine physikalische
Fehlergrenze. Die Fibonacci-Startwerte 1,1 und der Index 1000 sind reine
Konvergenzzeugen, keine rekonstruierten Metronzahlen eines Teilchens.

14 neue Tests in `tests/test_metronic_integration.py` verwenden exakte
rationale Logarithmuseinschliessungen mit expliziter Reihenschwanzschranke.
Alle 158 Tests und alle zehn bisherigen Rechenchecks samt Quellhashes
bestanden. Kein neuer Ergebnissnapshot und keine alte Eingabe geaendert.
FIND-032 erweitert das Register auf 32 Befundgruppen, nicht 32 Fehler.

```powershell
py -3.13 -m unittest discover -s tests -p test_metronic_integration.py -v
py -3.13 -m unittest discover -s tests -q
py -3.13 scripts/validate_finding_register.py
```

Naechster enger Auftrag: Welche Argumente und Schrittweiten meinen
delta und delta_e in der H004-X/H/G-Kette genau? Erst danach konkrete
relative Potential- und H/G-Schritte sowie eine gemeinsame Fehlerbilanz
rekonstruieren. Weder ein passender Massenzielwert noch ein erfundener
kleiner Schritt darf diese Quellenluecke ersetzen. Moderne Empirie und
der separate H015-XIV/XXVI-Vergleich bleiben nachgeordnet.

Fundstellen, Hashes und Suchgrenzen:
[Quellennotiz](../03_notes/METRONIC_INTEGRATION_SOURCES_2026-09-06.md).
