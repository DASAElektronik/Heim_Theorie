# F16 nach A16: unabhängige reduzierte Bestimmtheitsprüfung

2026-09-06, Etappe 28. Gelesen: [Etappe-27-Bericht](../../../06_docs/A16_ORIGIN_2026-09-06.md)
und [eigene A16-Algebrareview](A16_ALGEBRA_REVIEW_2026-09-06.md).
Neue Vollseitenlesungen H004 Druck330–335 wurden von Root und
book_derivation mitgeteilt, nicht hier selbst als Glyphenprüfung durchgeführt.
Keine neue Masse, Wahl eines Y9-Wertes oder Anpassung an ein Ergebnis.

## 1. Welche Voraussetzungen werden tatsächlich untersucht?

Die mitgeteilten Quellenstellen ordnen F_im metronischen R3-Selektoren
und den Koordinaten-Metronzahlen mu_s zu. Sie fordern auf S.331 konstante
endliche Grenzwerte bei divergierenden mu_s. S.334 verknüpft den Grenzfall
tau gegen null mit mu gegen unendlich und endlichen reellen A_im.
Für F16 wird diese allgemeine Forderung über den Indexanschluss angewandt;
sie ist keine zusätzliche, nur für F16 gedruckte Randgleichung.
Der lokale Beitrag auf S.332 ist X6=kappa*eta_qk*F16.

Für den folgenden mathematischen Test reduzieren wir dies ausdrücklich auf:

1. Eine gewöhnliche reelle dimensionslose Folge hat einen konstanten
   endlichen Grenzwert A. Positivität wird in den Zeugen zusätzlich erfüllt.
2. Bei festem c=kappa*d, d=eta_qk, gilt x_n=c*f_n; weder x_n noch sein
   Grenzwert ist zusätzlich als unabhängiger Zahlenwert vorgegeben.
3. Keine weitere Funktionsgleichung, Normierung oder Randwertforderung
   wird in diesem reduzierten Test vorausgesetzt.

Der eigene Folgenindex n ist kein identifizierter physikalischer Metron-
oder Resonanzindex. Gewöhnliche skalare Folgen sind keine als gültig
nachgewiesenen metronischen Lösungen Heims. Der Test entscheidet nur,
welche Folgerung aus genau diesem reduzierten Bedingungspaket möglich ist.

## 2. Ein genauer Nicht-Eindeutigkeitszeuge

Für n=0,1,... erfüllen die beiden eigenen Folgen

```text
f_n^(1)=1+1/(n+1),  f_n^(2)=2+1/(n+1)
```

alle reduzierten Anforderungen, haben aber verschiedene Grenzwerte 1
und 2. Beide sind positiv, endlich und dimensionslos; der Rest zum
jeweiligen Grenzwert ist sogar identisch. Die Konvergenz folgt direkt
aus 1/(n+1) gegen null, nicht aus dem Test endlich vieler Folgenglieder.
Mit demselben c erfüllen beide x_n=c*f_n. Der lineare Anschluss gibt
den Übertragungsfaktor vor, bestimmt aber ohne unabhängig vorgegebenes x
keinen der beiden Grenzwerte. Dimensionslosigkeit allein wählt ebenfalls
keinen Zahlenwert aus. Schon konstante Folgen 1 und 2 wären weitere Zeugen.

Bei c=0 verschwindet der sichtbare Beitrag für jeden endlichen F16-Wert.
Bei c ungleich null und unabhängig vorgegebenem Grenzwert x_infty würde
A=x_infty/c hingegen eindeutig folgen. Das ist eine zusätzliche Angabe,
keine Konsequenz der bloßen Anschlussdefinition.

Insbesondere darf der von einem Korrelationszentrum festgelegte
Koordinatenursprung nicht zu F16(0)=0 umgedeutet werden. Auch der bei
kappa=0 inaktive spinorielle Beitrag setzt keinen F16-Wert fest.
Gerüst-/Shiftbedingungen brauchen einen expliziten Anschluss, bevor sie
als Randwert für F16 verwendet werden. Die Forderungen f(N)>=0 und
delta_N f>0 auf S.330 betreffen die Resonanzergänzung f, nicht automatisch F16.

## 3. Positive bedingte Bestimmtheit durch die Auswahlgleichung

Eine von Root mitgeteilte weitere Gleichung darf nicht unterschlagen werden:
Im festgelegten k=1,Q=kappa=q=1-Kontext ergibt der Anschluss an (108)

```text
T108 = g*(1+d*A)*(1+f).
```

T108 ist hier unsere Kurzbezeichnung für die linke Seite aus den dortigen
N_(j), NICHT eine Lebensdauer. Bei unabhängig vorgegebenen T108,g,d,f,
mit g,d>0 und f ungleich -1, folgt exakt und eindeutig

```text
A = [T108/(g*(1+f))-1]/d.
```

Zwei verschiedene A können dann dieselbe linke Seite nicht liefern,
weil die Differenz g*d*(1+f)*(A1-A2) wäre. Ob der so erhaltene Wert weitere
physikalische oder positive Bereichsbedingungen erfüllt, bleibt separat.
Falls T108 beziehungsweise die N_(j) erst im an W(A) gekoppelten
Auswahlprozess bestimmt werden, ist T108 nicht unabhängig vorgegeben.
Dann muss die gemeinsame Kopplung untersucht werden; das Umstellen
allein beweist weder Eindeutigkeit noch einen freien Parameter.
Es ist kein nachgewiesener historischer Rückwärtsfit und wird hier mit
keinen Zustands- oder Messwerten ausgewertet.

## 4. Grenzwert ist noch keine quantitative endliche Näherung

Die Quelle nennt nach den mitgeteilten Seiten keine Konvergenzrate oder
Gleichmäßigkeitsforderung, obwohl sie die Näherung bei richtig bestimmten
A_im als sehr gut beschreibt. Als eigenständige gewöhnlich-skalare Diagnose
betrachte für feste A,B,L>0 und m>=0

```text
f_L(m)=A+B*L/(L+m).
```

Für jedes feste L gilt f_L(m) gegen A bei m gegen unendlich.
Für 0<epsilon<B wird der Rest höchstens epsilon erst dann garantiert,
wenn m>=L*(B/epsilon-1). Ohne eine obere Schranke für L gibt es keine
gemeinsame hinreichende endliche m-Grenze für diese Familie: Bei jedem
beliebig großen m>0 kann L=m sein, und der Rest ist B/2. Für festes
endliches m>0 ist das Supremum des Rests über L>0 sogar B.

L ist ausschließlich unser dimensionsloser Spielparameter, keine
behauptete Heim-Skala oder ein eingeführter Y-Faktor. Dieser Zeuge zeigt
nicht, dass die wirkliche unbekannte F16 langsam konvergiert; er zeigt,
dass Grenzwertkonvergenz allein eine behauptete kleine endliche Abweichung
nicht liefert. Er verletzt keine als vorausgesetzt behandelte tatsächliche
F16-Konvergenzrate, denn eine solche wurde hier nicht angegeben.
Die Quelle verknüpft tau- und mu-Grenzfälle; wir konstruieren keine
physikalischen tau/mu-Tripel und setzen keine unabhängige Variation beider
Parameter oder eine neue Beziehung zwischen ihnen voraus.

## 5. Selbstenthaltener exakter Kontrollcode

Die allgemeinen Grenz- und Eindeutigkeitsaussagen sind oben begründet.
Der Code prüft dazu endliche rationale Identitäten und eigene Zeugen;
er beweist nicht allein durch Stichproben eine Konvergenzaussage.

```python
from fractions import Fraction as F
from itertools import product

def sequence(A, n):
    return A+F(1, n+1)

checks = 0
for n, c in product((0, 1, 2, 9, 999, 10**30), (F(0), F(1, 3), F(3, 4))):
    f1, f2 = sequence(F(1), n), sequence(F(2), n)
    assert f1 > 0 and f2 > 0
    assert f1-1 == f2-2 == F(1, n+1)
    assert f2-f1 == 1 and c*f2-c*f1 == c
    if c == 0:
        assert c*f1 == c*f2 == 0
    else:
        assert (c*F(1))/c == 1 and (c*F(2))/c == 2
    checks += 1

def approaching(A, B, L, m):
    return A+B*L/(L+m)

for m in (1, 10, 10**6, 10**30):
    assert approaching(F(2), F(1), F(m), F(m))-2 == F(1, 2)
    checks += 1
for L, epsilon in product((F(1), F(5), F(37)), (F(1, 10), F(1, 1000))):
    threshold = L*(1/epsilon-1)
    m = -(-threshold//1)
    assert approaching(F(2), F(1), L, m)-2 <= epsilon
    assert approaching(F(2), F(1), L, m-1)-2 > epsilon
    checks += 1

for g, d, f, A in product((F(1), F(7, 3)), (F(1, 2), F(3, 4)),
                           (F(0), F(1, 2), F(2)), (F(1), F(2))):
    T108 = g*(1+d*A)*(1+f)
    recovered = (T108/(g*(1+f))-1)/d
    assert recovered == A
    assert g*(1+d*F(2))*(1+f)-g*(1+d*F(1))*(1+f) == g*d*(1+f)
    assert g*d*(1+f) != 0
    checks += 1
for A in (F(1), F(2)):
    assert F(3)*(1+F(1, 2)*A)*(1+F(-1)) == 0  # Excluded degeneracy.
print("OK:", checks, "exact reduced-condition checks; no Heim solution or fitted value")
```

Der eigene Block wurde mit py -3.13 -B aus dieser Review ausgeführt:
52 exakte Kontrollfälle bestanden, Exitcode 0. Keine alten Dateien geändert.

## Ergebnisgrenze

Die reduzierte Grenzwert-/Dimensions-/Anschlussforderung bestimmt A16
nicht. Das ist KEINE globale Nichtbestimmtheit der Heim-Theorie und
auch keine Aussage, A16 sei heute numerisch undefiniert: Die in Etappe 27
lokalisierte heuristische Formel legt es bei festen Eingaben und Y9 fest;
Y9=1 ist eine ausdrücklich benannte Tabellenspezialisierung.
Berechenbarkeit dieser Vorschrift, unabhängige Herleitung ihrer Notwendigkeit
und eine quantitative Genauigkeit der endlichen F16-Näherung sind verschiedene Fragen.
Zusätzliche echte Gleichungen oder unabhängig gegebene Rand-/Normalisierungswerte
könnten den Grenzwert festlegen, wie der bedingte (108)-Anschluss zeigt.
Kein Grenzwert, Y9 oder A16 wurde hier an eine Masse oder ein K4-Ergebnis angepasst.
