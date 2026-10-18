# B65 ist nicht die Feldextraktion des C-Ports

2026-10-18, Einheit50, Ausgang defc8d1.
[Vertrag](../00_admin/NEUTRINO_FIELD_BRIDGE_PLAN.md),
[exakte Kontrollen](../scripts/audit_neutrino_field_bridge.py),
[Ergebnisprotokoll](../05_analysis/neutrino_field_bridge_results.json).

## Ergebnis

Die Gleichsetzung scheitert bereits an einer symbolischen Eigenschaft:
H007/B65 ergibt für1110 und1111 bei neutraler leerer Struktur denselben
Feldterm. Der C-Ausdruck ergibt selbst unter einer von uns zusätzlich
eingesetzten neutralen Leerraumprojektion zwei verschiedene Terme.
Ihre Differenz ist unter den unten angegebenen Bedingungen strikt positiv.
Eine bloße Subtraktion des Ladungsterms macht den Port daher nicht zu
einer Implementierung von B65.

Das ist ein Fassungs-/Implementierungsvergleich, kein experimenteller
Massenfehler. Es wurden keine historischen Neutrinomassen berechnet,
keine physikalischen Konstanten passend gewählt und keine alten Profile
repariert. Die aktive C-Zuordnung aus49 bleibt als eigener Vertrag erhalten.

## Gelesene Quelle und geltende Normalisierung

H007 PDF2/3/7/8 vollständig visuell gelesen: B3–B14, Auswahl-/Lebensdauer-
Kontext und Wiederholung B49/B50. PDF10/B63–B65 wurde bereits in49
vollständig gelesen. Das Deckblatt bezeichnet eine spätere Redaktion
nach einem1989-Manuskript; PDF2 erwähnt geschätzte Ergänzungen fehlender
Klammern. Die bestehende Normalisierung von B13 und B49 bleibt gültig;
der B50-Doppelminus-Befund bleibt ungelöst.

H010 C0.66 GMASS998–1027 ist die unveränderte Vergleichsstelle.
Hashes wie in49 beziehungsweise48. Keine Programme aus den Quellen
ausgeführt. Kein unabhängiges Originalmanuskript neu gefunden.

## Warum B50 diese begrenzte Prüfung nicht verhindert

Bei B63 gilt `sigma=-Q_sigma`. In B49 steht der gesamte B50-abhängige
Summand unter einem Faktor `sigma+Q_sigma`. Für endliche, definierte
B,U und ein von null verschiedenes W_N0 verschwindet er daher exakt.
Diese Rechnung ist keine Entscheidung für eines der B50-Vorzeichen
und keine Behauptung, dass `0*undefiniert` zulässig wäre.

Der verbleibende Ausdruck bei q=0 ist

```text
phi_0 = P(P-2)^2 * (1+kappa/(2*alpha*theta))
        * (pi/e)^2 * sqrt(eta_12) * (Q_m-Q_n)
        - (P+1)*choose(Q,3)/alpha.
```

Für k=1 gelten Q_n=Q_m=3. Für den betrachteten Zustand P=Q=1
verschwindet zusätzlich choose(1,3). Somit ist `phi_0=0` für beide
KAPPA-Werte. Dies betrifft die reguläre Einschränkung auf diese Domain;
die allgemeine numerische Auswertung von B49 bleibt gesperrt.

## Die quellenbelegte Gleichheit

Mit q=0 gilt eta_(q,k)=1. In B10 verschwindet für k=1 bereits
der Faktor k(k−1), also N5=A. In B13 hat der erste Summand den Faktor
k²−1; der verbleibende N6-Term ist ebenfalls unabhängig von KAPPA.
B6 und B65 ergeben, nach Herausnehmen des gemeinsamen Faktors
mu*alpha_plus,

```text
H_1110 = H_1111 = 2*N5 + 2*N6.
```

Diese algebraische Reduktion bestätigt die auf PDF10 ausdrücklich
gedruckte Gleichheit M_nu(1110)=M_nu(1111). Es ist keine Annahme aus
einer numerischen Ähnlichkeit. Die positive oder negative Gesamtgröße
wird hier nicht numerisch bestimmt.

## Was nach der Ladungssubtraktion im C-Code bleibt

Setze ausschließlich zum Vergleich k=P=Q=1 und KQ=q=0 in GMASS.
Diese neutrale Projektion für KAPPA=1 ist kein behaupteter erreichbarer
Elternzustand der unveränderten MAIN-Ladungsregel. Der C-Port führt sie
nicht automatisch aus. Mit t=n1/Q1 reduziert sich FIK auf

```text
C_kappa(t) = B*(1+kappa*T)*(1+(1-kappa)*t) + D

B = 12/pi * (1-r) * (1-alpha/3) * sqrt(eta_11)
    * (1+4*pi*alpha/(eta*sqrt(eta)))
T = 2*xi/(3*eta^2)
D = 8*(1-r)*alpha/xi^2
r = alpha_minus/alpha_plus.
```

Hier heißen B,T,D nur unsere kompakten Vergleichskoeffizienten. Sie
sind weder B aus H007/B28 noch eine Lebensdauer T oder eine bereits
anderweitig benutzte Hilfsgröße D. Die im Skript verwendeten Zahlen
B=3,T=2,D=5 sind ausdrücklich synthetisch.

Die gewöhnliche Eltern-Grundbelegung t=0 und die hypothetische
Leerraumbelegung t=−1 ergeben:

| KAPPA | Portterm bei t=0 | Portterm bei t=−1 | H007/B65 leer |
|---:|---|---|---|
| 0 | B+D | D | 2N5+2N6 |
| 1 | B(1+T)+D | B(1+T)+D | 2N5+2N6 |

Die Leerraumdifferenz des Ports ist `B*(1+T)`. Für pi,eta,eta_11,xi>0,
0<alpha<3 und r<1 ist sie strikt positiv. Damit kann nicht gleichzeitig
für beide Zustände dieselbe B65-Funktion vorliegen. Diese Aussage
benötigt keine konkrete Wahl der universellen Konstanten und keinen
historischen Alpha-Plus-Abgleich.

Zugleich unterscheidet sich bei KAPPA=0 die bloße Eltern-Feldextraktion
von der Leerraumprojektion um B. Deshalb sind schon innerhalb desselben
Ports zwei getrennte Operationen zu unterscheiden. Eine andere freie
Neuzuordnung könnte die Diagnose nicht rückwirkend in eine Quellen-
identität verwandeln; sie wäre ein neuer Vertrag.

## Prüfung und Konsequenz

Vier exakte rationale Tests prüfen den verschwindenden B49-Term bei
verschiedenen endlichen BUW-Werten, die B6-Gewichte, die strikt positive
Portdifferenz und den Unterschied Elternzustand/Leerraumprojektion.
Die synthetischen Wurzelsymbole sind keine Näherungswerte für eine
Teilchenrechnung. Die Nichtgleichheit ist zusätzlich analytisch oben
begründet; der Snapshot speichert keine Massenvorhersage.

```powershell
py -3.13 scripts/audit_neutrino_field_bridge.py --check
py -3.13 -m unittest tests.test_neutrino_field_bridge
```

FIND-056 dokumentiert die begrenzte Versionsdifferenz. Der allgemeine
B50-Blocker wird nicht aufgehoben und die bisherigen55 Befunde bleiben
unverändert. Eine vollständige Rekonstruktion aller B65-Zustände und die
Messgrößenzuordnung bleiben getrennte Aufgaben. Der nächste konkrete
Quellenweg führt zu den Neutrino-/Feldmassenstellen im Buch, nicht zu
einem Fit der C-Ausgabe auf moderne Massengrenzen.

Abschlussprüfung:381 Tests erfolgreich; Snapshot und Registermetadaten gültig.
