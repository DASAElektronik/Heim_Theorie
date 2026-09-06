# Eta_22 in B47/B55: H007-Rollenreview — 2026-09-06

## Auftrag, Ausgabe und Grenze

Diese Teilreview behandelt nur die Existenzzeitkette B41–B57 sowie deren
direkte Schlussbemerkungen in H007. Sie rekonstruiert weder die
Gesamtmassenformel noch B50 und ergänzt keine Klammern.

H007 ist *Die erweiterte Massenformel nach Burkhard Heim (1989)*, nach der
Titelseite „Nach einem Manuskript von Burkhard Heim“, IGW Innsbruck 2002;
die Seitenköpfe nennen © IGW Innsbruck 2003. Die Einleitung (Druck 11 /
PDF 2) erklärt, das Programm sei nicht mehr auffindbar, im Manuskript seien
bei langen Gleichungen Klammern nach bestem Ermessen ergänzt worden und das
aktuelle IGW-Programm enthalte keine Lebensdauern. Diese Ausgabe beweist
deshalb weder einen unveränderten 1989er Wortlaut noch eine heutige
Ausführung von B47/B55.

Vollständig visuell geprüft: Druck 10–11 / PDF 1–2, Druck 13–17 / PDF 4–8
und Druck 20 / PDF 11. OCR war ausschließlich Locator.

## Direkte Abhängigkeit von B47 und B55

**Druck 15 / PDF 6:** B41 setzt `w=W_(N=0)(1+f)`. Unter B15–B21 und B40
werden die Zonenwerte `n,m,p,sigma` per Exhaustionsverfahren gewonnen;
B46 hält sie fest. Zwei direkte Hilfsgrößen auf **Druck 13 / PDF 4** sind

`H=Q_n+Q_m+Q_p+Q_sigma` (B24),

`B=3H[k^2(2k-1)]^(-1)` (B28).

Dieses `B` ist eine B28-Hilfsgröße und **nicht** die Baryonenziffer
`B=k-1` aus EDM2.

**Druck 16 / PDF 7** trägt die Überschrift „Die mittleren Lebensdauern der
Grundzustände“. `T` bezeichnet dort die mittlere Lebensdauer der durch B3
bestimmten Massen; `T_N=T(N)<<T` und `T_0=0`. Die Formel lautet sichtbar:

```text
(T-T_N) = [192 h H y /
 {M c^2 [eta_2,2(1-sqrt(eta))^2(1-sqrt(eta_1,1))^2
 (1-sqrt(eta_1,2))^2](H+n+m+p+sigma)
 (n+|m|+|p| beta_(0))}] delta .                         (B47)
```

Der Text schreibt `delta=delta(N)` wie B7, `M` aus B3 und `H` aus B24. Er
bezeichnet B47 als „nach Heim“ einheitliche Existenzzeitbeziehung, liefert
in den geprüften Seiten jedoch keine Herleitung der Faktorwahl.

Die Verbindung zu B55 ist allein

`y=F[phi+(-1)^s(1+phi)(b_1+b_2/W_(N=0))]`  (B48).

Also ist B55 ein `b_2`-Baustein von `y`, das in B47 eingeht. B55 ist nicht
die Massenformel B3 und keine als Massenkorrektur beschriebene Gleichung.

**Druck 17 / PDF 8** ordnet davor `phi` (B49), `U` (B50),
`Z=k+P+Q+kappa` (B51), `F` (B52), `s` (B53) und `b_1` (B54) ein; es sagt
ausdrücklich, `B` werde aus B28 ermittelt. Danach folgen B55 und
`beta_(0)` (B56).

## B55: eta_2,2 und Literalnotation

Der Anfang und Mittelteil der sichtbaren B55-Zeile lauten (einschließlich
des **kleinen** `b` in `B(5b+3)`):

```text
b_2 = B(5b+3)+(2H-3)/(P+1)+C^k{B(3B+2(H+1))+H+1/2}(1-q)
      -Q{B(2(B+H)-1)+H/2+3}+kappa q{B(3B+1)-5/2}(k-Q)
      -binom(P,2)P^2(P+Q)^2[8B+1
       -{5B-(2H+1)(1+2binom(P,3)-Q)+2}q]
      -binom(P,2)H(1-q)-(B-3/4)^2(P-1)(P-2)(P-3)(-1)^(k-1)
      +(Q-q)(1-q+Bq){3(H+B)+pi e/eta-q/4}(P+1)^3(k-1)
```

Die Schreibweise `B(5b+3)` ist ein H007-Literalbefund; sie wird hier nicht
an eine abweichende Lesart anderer Quellen angepasst.

Der eta_2,2-haltige Endterm von B55 ist sichtbar

```text
-(5/2) H^2 binom(P,3)
 {q[1+(pi/3)(2-q) eta_2,2] B - (2-q)(1-q)} .             (B55)
```

Der vorausgehende, für die Klammerlage wichtige Druckabschnitt lautet

```text
+ kappa {(-1)^(1-q)[7HB+3(H+B)-5/2
  +(1-q){H(3B-4)+B+7/2}](k-1)
  + Q binom(P,2){(2-q)(1+epsilon q_x)[B/2(H+2)+3/4]
    +5/2 HB+3H-(B+5)/(P+1)}
  - (5/2) H^2 binom(P,3)
    {q[1+(pi/3)(2-q)eta_2,2]B-(2-q)(1-q)} .             (B55)
```

Die Vollseite zeigt: Nach `+ kappa {` steht vor der Gleichungsnummer B55
keine sichtbare weitere `}` zum Schließen dieser äußeren Klammer. Der
Befund bleibt absichtlich offen; die Ausgabe selbst berichtet zudem von
Klammerergänzungen in langen Manuskriptformeln. Keine stillschweigende
Normalisierung ist hier vertretbar.

Der lokale eta_2,2-Koeffizient des Endterms ist proportional zu
`q(2-q) binom(P,3)` (zusätzlich zu `H^2B`). Daher verschwindet dieser
eta_2,2-Beitrag für `q=0` und **für `q=2`**. Das folgt aus dem sichtbaren
Teilprodukt und ist unabhängig von der ungeklärten äußeren kappa-Klammer.

In B47 steht eta_2,2 dagegen direkt im Nenner neben `eta`, `eta_1,1` und
`eta_1,2`. Die geprüften Seiten definieren oder motivieren weder dort noch
in B55, warum genau der Index `(2,2)` gewählt ist: Er wird formelhaft
vorausgesetzt. B55 liefert insbesondere keine Motivation für eine aktive
Delta-`q=2`-Korrektur; sein lokaler eta_2,2-Term fällt gerade bei `q=2` weg.

## Anspruch, Einheiten und empirische Anpassung

Nach **Druck 17 / PDF 8** sollen aus Tabelle I, B3–B14 und B47–B57 die
Existenzdauern `T` aller Multiplettkomponenten bei `N=0` berechnet und mit
Empirie verglichen werden. Die ausgegebenen Werte seien Vielfache von
`10^-8` Sekunden. Das ist eine Tabellen-/Ausgabeangabe, keine auf den
geprüften Seiten ausgeführte Dimensionsherleitung von B47.

Die Schlussbemerkungen auf **Druck 20 / PDF 11** begrenzen den Anspruch:

* Für `N>0` seien B33–B36 nicht gut abgesichert, `z(N)` und daher `Q(N)`
  unbekannt; Massen der Spektren seien stark approximativ und `T_N` solcher
  Zustände könne noch nicht beschrieben werden.
* Für `phi` in B49 seien mit B50 frei wählbare Parameter empirischen
  Gegebenheiten angepasst worden. Das ist ein expliziter Fit-Hinweis für
  B49/B50, nicht für eta_2,2 in B47 oder B55.

## Entscheidung

| Frage | Quellenbefund |
|---|---|
| Rolle von B47 | Behauptete Existenzzeitrelation für Grundzustände, nicht B3. |
| Rolle von B55 | `b_2 -> y` gemäß B48 -> B47; keine direkte Massenformel. |
| eta_2,2 in B55 bei q=2 | Lokaler Beitrag ist wegen `q(2-q)` null. |
| eta_2,2 in B47 | Direkt im Nenner; keine motivierende Herleitung auf den geprüften Seiten. |
| Empirische Anpassung | Textlich nur frei wählbare B49/B50-Parameter, nicht eta_2,2. |
| Original-/Ausführungsstatus | Editorische Nachmanuskript-Ausgabe; verlorenes Programm, fehlende Lebensdauer-Implementierung und dokumentierte Klammerprobleme. |

## Kontrollbilder und Suchgrenze

Tragende Bilder: `tmp/pdfs/eta22_roles_igw/h007-pre-04.png` (B22–B28),
`h007-06.png` (B41), `h007-07.png` (B47–B48), `h007-08.png` und
`h007-hi-08.png` (B49–B57), `h007-11.png` (Schlussbemerkungen) sowie
`h007-front-01.png` und `h007-front-02.png` (Quellenstatus). Nicht geprüft
wurden Tabellen I–III/Kapitel G, die Originalprogrammdatei, eine
B50-Gesamtlösung, der ganze 57-Seiten-Bericht oder externe Literatur.
