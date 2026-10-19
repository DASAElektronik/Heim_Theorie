# Historische Exponentenfassung in H006

Stand: 2026-09-06. Eng begrenzte Quellen- und Glyphenpruefung der
IGW-Wiedergabe H006; keine neue Massenrechnung.

## 1. Kurzergebnis

In H006 weicht in der hier geprueften kleinen Formelgruppe nur (XIV) in der
sichtbaren Stellung der Klammern ab. Dort steht linear:

```text
exp[1-2k(n4+Q4)/3Q4]
```

Die Basisformel (XV), die N=0-Gleichung (XXVI), der N=1-Realteil (XXVII), die
reelle Beziehung (XXIX), die beiden Algorithmusschritte (XXX)/(XXXI) und die
Grenzgleichung (XXXV) setzen dagegen den Zaehler `1-2k` in Klammern. Die
hochaufgeloeste Gegenlesung korrigiert damit eine moegliche Kleinbildlesung:
Auch (XXVII) und (XXIX) sind **geklammert**, nicht wie (XIV) gesetzt.

Dieser Befund lokalisiert eine interne Druckfassungsdifferenz. Er beweist
weder, dass (XIV) ein Druckfehler ist, noch welche Entstehungsursache die
Abweichung hat. Die vorliegende Datei ist eine IGW-Wiedergabe von 2002/2003,
die sich auf eine Urschrift von 1982 beruft; sie ist kein hier
authentifiziertes Faksimile dieser Urschrift.

## 2. Gepruefte Quelle und Editionsstatus

Lokale Quelle:

`01_sources/heim_primary/Massenformel_nach_B_Heim_1982.pdf`

Am 2026-09-06 lokal nachgepruefter SHA-256:
`F74DA0DAC8496BCD01226F54D88598152D67E1C954943AF61D0EC1811F5527BE`.

Alle Seiten tragen den Kopf:

```text
Einfuehrung in die Heimsche Massenformel
(C) IGW Innsbruck, 2003
```

Die Titelseite (Druckseite/PDF-Folio 1) nennt:

```text
Die Massenformel nach Burkhard Heim (1982)
Wiedergabe der Urschrift von Burkhard Heim zur Programmierung seiner
Massenformel
Forschungskreis Heimsche Theorie IGW Innsbruck, 2002
```

Die Schlussseite (Druckseite/PDF-Folio 10) traegt in der Wiedergabe die
Angaben `Northeim, Schillerstrasse 2`, `gez. (Heim)` und `25.2.1982` sowie
eine Verteilerliste, unter anderem an DESY, ETH, Max-Planck-Institut und MBB.

Diese Angaben belegen, wie IGW das wiedergegebene Dokument zuschreibt und
datiert. Sie sind kein unabhaengiger Echtheitsnachweis der Urschrift oder
einer eigenhaendigen Signatur. Auch die PDF-Metadaten (`Author: Admin`,
Erstellungsdatum 16.09.2003) beschreiben die spaetere PDF-Datei, nicht den
Entstehungszeitpunkt des behaupteten Ausgangsmanuskripts.

## 3. Glyphentreue kleine Exponentenkarte

Die folgende Tabelle gibt nur den jeweils relevanten sichtbaren Ausdruck
wieder. Insbesondere bleibt der flach gesetzte Nenner `/3Q4` glyphentreu
zunaechst ohne nachtraeglich eingefuegte Nennerklammer.

| Stelle | Druck-/PDF-Seite | sichtbare Zeichenfolge des Exponenten |
|---|---:|---|
| (XIV), Auswahlregel | 6 | `exp[1-2k(n4+Q4)/3Q4]` |
| (XV), Basisanstieg | 6 | `exp[(1-2k)/3]` |
| (XXVI), Fall `N=0` | 8 | `exp[(1-2k)(n4+Q4)/3Q4]` |
| (XXVII), Realteil bei `N=1` | 8 | `exp[(1-2k)(n4+Q4)/3Q4]` |
| (XXIX), reelle Beziehung | 8 | `exp[(1-2k)(n4+Q4)/3Q4]` |
| (XXX), Rest `W2` | 9 | `exp[(1-2k)(n4+Q4)/3Q4]` |
| (XXXI), Rest `W3` | 9 | `exp[(1-2k)(n4+Q4)/3Q4]` |
| (XXXV), Grenzordnung `L` | 10 | `exp[(1-2k)(L4+Q4)/3Q4]` |

Hinweis zur Nummerierung auf Seite 10: (XXXIV) bezeichnet dort drei
Bauprinzip-Grenzen und enthaelt keinen Exponentialterm. Der Exponentialterm
der impliziten Grenzgleichung folgt erst in (XXXV).

Auf Seite 8 steht in (XXIX) unmittelbar vor `exp` zusaetzlich ein sichtbares
doppeltes Plus (`+ +`). Das ist eine weitere Satzauffaelligkeit derselben
Wiedergabe, wird hier aber nicht als Grundlage fuer eine Korrektur des
Exponenten benutzt.

## 4. Normalisierte Lesart und Beziehung zu (XV)

Die im bestehenden Befund FIND-027 verwendete **explizite
Nennernormalisierung** liest den
flachen Nenner als `(3 Q4)`. Dann lauten die beiden konkurrierenden Formen:

```text
(XIV)   exp[1 - 2 k (n4+Q4)/(3 Q4)]
(XXVI)  exp[(1-2k)(n4+Q4)/(3 Q4)]
```

Das ist eine explizite algebraische Normalisierung der Druckzeichen und
nicht dieselbe Aussage wie deren glyphentreue Transkription.

Fuer `n_j=0` und `Q4 != 0` reduziert sich die Form aus (XXVI) unmittelbar zu

```text
exp[(1-2k)/3],
```

also genau zum in (XV) gedruckten letzten Summanden von `g(qk)`. Die Form aus
(XIV) reduziert sich unter derselben Normalisierung dagegen zu
`exp[1-2k/3]`. Damit besteht die lokale Inkonsistenz bereits zwischen
(XIV), (XV) und (XXVI), ohne dass eine Teilchenmasse eingesetzt werden muss.

## 5. Anschluss an den gedruckten Algorithmus

Die Seiten 8--9 legen fuer `N=0` folgende quelleninterne Folge dar:

1. (XXVI) setzt die vier Zonenbeitraege gleich `W_nux`.
2. Der Algorithmus zieht nacheinander den kubischen, quadratischen und
   linearen Anteil ab; (XXX) und (XXXI) lassen denselben geklammerten
   Exponentialterm als letzten Rest stehen.
3. Fuer den Fall `0 < W4 <= 1` wird gedruckt:

   ```text
   ln W4 <= 0 und K4(2k-1) = -3Q4 ln W4.
   ```

Diese Umkehrbeziehung ist algebraisch mit
`W4 = exp[(1-2k)K4/(3Q4)]` vereinbar. Zusammen mit (XV) stuetzt sie die
bestehende Normalisierung des Nenners als `3Q4` und die geklammerte
Zaehlerform innerhalb dieses Algorithmus. Sie ist kein eigenstaendiger
historischer Nachweis dafuer, dass (XIV) redaktionell zu aendern sei.

Die Schlussseite wiederholt fuer die Grenzbesetzungen `L_j` in (XXXV)
ebenfalls die geklammerte Form. (XXXIV) liefert nur die vorangehenden
Ungleichungen fuer diese Grenzen.

## 6. Was daraus folgt -- und was nicht

Quellenfest ist:

- (XIV) besitzt in der IGW-Wiedergabe eine andere Klammerstellung als alle
  hier geprueften homologen Wiederholungen.
- (XV), (XXVI), (XXVII), (XXIX), (XXX), (XXXI), (XXXV) und der logarithmische
  `K4`-Schritt bilden unter dieser Nennernormalisierung eine lokal
  zusammenpassende
  Exponentenkette.
- Die N=0-Reduktion von (XXVI) stimmt mit (XV) ueberein; die gedruckte Form
  von (XIV) tut dies nicht.

Nicht quellenfest ist:

- dass Heim selbst an (XIV) einen Druckfehler markiert oder ein Erratum
  angegeben habe;
- ob die Abweichung aus Heims behaupteter Urschrift, einer spaeteren
  Transkription, einer redaktionellen Neusetzung oder einer Revision stammt;
- dass die lokal konsistentere Form deshalb bereits physikalisch richtig
  oder als historische Autorabsicht bewiesen sei;
- dass aus dieser einen Abweichung ein Urteil ueber die gesamte
  Massenformel oder deren empirische Guete folgt.

Der engste belastbare Status lautet daher: **interne
Klammerinkonsistenz der IGW-Wiedergabe, mit einer mehrfach wiederholten und
algorithmisch angeschlossenen geklammerten Fassung; Fehlerursache und
autoritative Korrektur bleiben ohne Urschriftfaksimile oder Erratum offen.**

## 7. Bildbelege der Sichtpruefung

- Titel/Provenienz: `tmp/pdfs/n0_alias/h006-01.png`
- (XIV)/(XV): `tmp/pdfs/n0_alias/h006-06.png`
- (XXVI)--(XXIX), 600 dpi:
  `tmp/pdfs/historical_exponent/h006-p8-600.png`
- (XXX)/(XXXI), logarithmischer `K4`-Schritt:
  `tmp/pdfs/n0_alias/h006-09.png`
- (XXXIV)/(XXXV), Schlussvermerk und Datierung:
  `tmp/pdfs/historical_exponent/h006-end-10.png`

Die Bildpruefung ist der tragende Beleg fuer Klammern und Glyphen. Die
PDF-Textschicht wurde nur zur Navigation und nicht als Ersatz fuer die
visuelle Lesung verwendet.
