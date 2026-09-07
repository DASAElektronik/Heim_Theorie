# NORM-HISTORICAL-N0-COMPARISON

2026-09-06, Etappe 17. Festlegung vor der neuen Vergleichsrechnung.
Die Etappe-16-Eingaben, ihr Rechner und ihre drei Snapshots bleiben erhalten.

## Enger Rechenvertrag

Nur die bereits vorgegebene Elektronkomponente, N=0. H006-x=1 entspricht
Code-x=2. Die spaeteren H010-Dateien werden ausschliesslich statisch gelesen.
W=g und positive erste drei Greedy-Abstaende erlauben weiterhin das
analytische Zertifikat K4=-3 ln(exp(-1/3))=1; keine Code-Offsets uebernehmen.
Der XIV/XXVI-Konflikt bleibt ausgeschlossen wie im H006-N0-Vertrag.

Mit d=eta(k=1,q=1), s=sqrt(d), a=nacktes alpha, R=(1-s)/(1+s):

```text
H006-N0-Profillesart:
alpha3 = 1 - a*xi^3*(1+s)^3/(3*d^3) - 2*sqrt(xi*d)/e * R^2

Aktives H010 Pascal/C, reell-algebraisch reduziert:
alpha3 = 1 - a*xi^3*(1+s)/(3*d^3) - 2*xi*d/e * R^2
```

Die erste Klammergrenze ist visuell eindeutig. Beim zweiten Term zeigt
H006 `(2 sqrt xi eta_qk)^k` mit Wurzelglyph, aber ohne belastbaren
horizontalen Wurzelstrich. Die bereits verwendete Lesart sqrt(xi*d) ist
eine deklarierte Normalisierung, nicht durch einen Vinculum bewiesen.
sqrt(xi)*d wird deshalb als zusaetzliche Lesartsensitivitaet gerechnet.
Beide enthalten gegenueber dem Code eine Wurzel; keine davon wird anhand
der Elektronenmasse zur richtigen Autorenfassung erklaert.

KGH des Codes ist im betrachteten Zustand die verschobene XI-Polynomform,
kein eigener Massenterm. Phi/fig ist hier faktorweise gleich; cos(pi(P+Q))
wird als exaktes (-1)^(P+Q)=1 verwendet. Mu ist algebraisch gleich.
Wir simulieren keine C-double- oder Pascal-extended-Auswertungsreihenfolge.

## Vorab festgelegtes Vergleichsraster

Alle 2^6=64 Kombinationen genau dieser Achsen:

1. Potenz des Faktors (1+s): 3 -> 1.
2. Zweiter alpha3-Faktor: sqrt(xi*d) -> xi*d.
3. Alpha: vorhandene source_literal-Rechnung -> 1/137.03599976.
4. Xi: gedruckte Dezimalzahl -> (1+sqrt(5))/2.
5. Hbar: H006-Wert -> aktiver H010-Wert.
6. Gamma: H006-Wert -> aktiver H010-Wert.

Das gemeinsame c und s0 aendern sich nicht. Mathematische pi/e bilden eine
Hochpraezisions-Idealisierung, keinen bitgleichen historischen Lauf.
Beta aendert sich im historischen Code ebenfalls; es hat nach regulaerer
Nullreduktion keinen aktiven Massenbeitrag. Die beiden A36-Domaenen werden
getrennt geprueft. Rg betrifft hier die separate Ladungsrechnung, nicht M.
Historische Konstanten sind keine parameterfreie physikalische Vorhersage.

Die gemischten Kombinationen sind **eigene Gegenrechnungen**, keine
behaupteten Editionsfassungen. Einzelwechsel gegen den H006-Ausgangspunkt
und zwei vollstaendige Ketten (obige Reihenfolge und ihre Umkehr) werden
ausgegeben. Differenzen sind wegen Wechselwirkungen reihenfolgeabhaengig;
nur die Gesamtdifferenz ist bei gleichen Endpunkten eindeutig. Zusaetzlich
werden Minimum und Maximum jeder Achsenwirkung im ganzen Raster angegeben.

Primare Einheit bleibt kg. Nur zum historischen Ausgabevergleich wird
H010-fakMeV=5.6095892e29 fuer **beide** Endpunkte verwendet, mit Einheit
MeV/c^2. Der gespeicherte Programmwert wird erst nach abgeschlossener
Berechnung verglichen und beeinflusst weder Input noch Zweigwahl.

Der hypothetische Wechsel n4=0 -> -1 hat bei festem Rest DeltaM=-4mu*alpha+.
Er wird gesondert protokolliert, niemals per pauschaler Toleranz ausgewaehlt.

## Nachweis und Grenzen

Neuer separater Rechner, Quellhashes, 80/120-Stellenvergleich, algebraisch
anders angeordnete Gegenrechnung und Tests. Fremde Programme/Makros sowie
die XLS-Workbooks bleiben unausgefuehrt und ungeoeffnet.

Ein Anschluss an gespeicherte H010-Zahlen ist hoechstens eine bedingte
Implementierungsreproduktion. Keine moderne empirische Pruefung, kein
Nachweis des Originalprogramms 1982, keine Rechtfertigung einer der beiden
alpha3-Aenderungen. C0.62-Ausgabekopf und C0.66-Quelldatei bleiben getrennt.
