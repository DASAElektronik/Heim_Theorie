# Woher Heims alpha3-Terme kommen

Stand2026-09-06, Etappe18 ab a989f03, Plancheckpoint c9beca4.

## Ergebnis

Die beiden in Etappe17 gegenueber H006 auffaelligen Programmterme haben
einen konkreten Buchbeleg: **Elementarstrukturen der Materie II, Druck275
und278, Gleichung98c**. Dort steht dieselbe Potenzklammer und derselbe
wurzellose zweite Faktor wie in H010. Wir muessen die Programmform daher
nicht mehr als bloss unbegruendete spaetere Schreibweise behandeln.

Das ist aber keine rein aus Anfangspostulaten abgeschlossene Herleitung:
Heim nennt Annahmen und legt die beteiligten Koeffizienten ausdruecklich
unter Bezug auf die Empirie von Elektron und Proton fest. Er verschweigt
die Anpassung an dieser Stelle nicht.

Zusaetzlich zeigt der neu gefundene H015-Archivscan dieselben zwei Terme
in einem mit1982 datierten FORTRAN-Listing. Die Abweichung von H006
entstand demnach nicht erst bei der spaeteren Pascal/C-Uebertragung.
Der Buchscan selbst ist Ausgabe1996. Eine lueckenlose Ueberlieferung ab1978,
eine forensische Echtheitspruefung oder ein Autorenerratum folgen daraus nicht.

## 1. Heims Denkansatz fuer die dritte Zone

Druck271 beschreibt alpha_j als Faktoren, welche das Traegheitsmass der
jeweiligen Konfigurationszone modifizieren. Bei j=3 interessiert Heim
der Anschluss seiner inneren Struktur an die aeussere Zone j=4.
Er setzt fuer diesen Uebergang an:

```text
alpha3(k,q) = f(k) - q*F(k,q),   F = H_Korr + G_Korr.
```

`H_Korr/G_Korr` sind hier unsere unterscheidenden Namen fuer die im Buch
H/G genannten Korrekturteile. Sie sind NICHT die gleichnamigen spaeteren
KGH-Polynome der Massensumme.

f soll den Geruestanteil ausdruecken, qF die Verminderung durch das
Ladungsfeld. Mit f(1)=1 und einer zusaetzlich angesetzten funktionalen
Bedingung fuehrt Heim auf Druck271/272 zu k*f(k)=exp(k-1).
Wir haben damit seine Argumentationsrichtung lokalisiert; die Bedingung
und metronische Integration sind nicht allein durch diese Wiedergabe bewiesen.

Die Teile H_Korr und G_Korr entwickelt der Text auf Druck272-274 ueber
Potentialkomponenten und metronische Variationen. Fuer H_Korr setzt er
die elektromagnetische Kopplung alpha/3 an. Eine Potentialidentifikation
fuer G_Korr bezeichnet er auf Druck274 selbst als spekulativ.

## 2. Wo die konkreten Potenzen herkommen

Setze d=eta_qk, s=sqrt(d), R=(1-s)/(1+s). Am Ende von Druck274 stehen
logarithmische Ausdruecke. Druck275 waehlt:

```text
A1=B1=B4=1,   A2=(2k+1)/2,   A3=1-4k,
B2=k/2,      B3=k,          Y=xi^2, xi>0.
```

Die A_i/B_i koennen laut Text frei vorgegeben werden. Die genannte
Festsetzung sei „der Empirie des Elektrons und Protons optimal angepaßt“.
Das ist ein direkter Autorenhinweis auf die Auswahl, kein von uns aus
dem Massentreffer erschlossener Vorwurf. Ein vollstaendiges Optimierungs-
protokoll, eine Zielfunktion oder eine Unsicherheitsanalyse liefert die
betrachtete Stelle nicht.

Nach dieser Festlegung folgt fuer positive Logarithmusargumente durch
gewoehnliches Exponentieren:

```text
H_Korr = alpha/3*(1+s)*Y^((2k+1)/2)*d^(1-4k)
       = alpha/3*(1+s)*(xi/d^2)^(2k+1)*d^3,

G_Korr = eta11/(e*d)*Y^(k/2)*d^k*2^k*R^2
       = eta11/(e*d)*(2*xi*d)^k*R^2.
```

So ist nachvollziehbar, warum `(1+s)` in dieser Buchfassung NICHT unter
der Potenz2k+1 steht. Ebenso stammt der zweite Faktor von
`sqrt(Y)=xi`, nicht von `sqrt(xi*d)`. Im Buch ist diese Algebra explizit
nachvollziehbar; sie beweist nicht rueckwirkend die physikalischen
Annahmen und die empirische Wahl der A_i/B_i.

Sechs neue exakte Fraction-Tests sichern diese Umformungen, die
abweichende H006-Potenz und die Trennung beider Wurzellesarten. Es sind
kuenstliche rationale Algebrazeugen, keine neuen Teilchenberechnungen.

## 3. Fassungen getrennt halten

H004(98c) und H010-Code stimmen an den zwei strittigen Termen ueberein.
H006(IX) druckt weiterhin die andere Klammer und ein Wurzelzeichen.
Der Buchbeleg ist mit einer Uebertragungs-/Redaktionsfehlerhypothese fuer
H006 vereinbar, entscheidet aber nicht zwischen ihr und einer absichtlichen
Fassungsabweichung. Er ist weder Autorenerratum noch vollstaendige Editionsgeschichte.
Die alten Rechenprofile, Ergebnisse und FIND-029 bleiben nachvollziehbar.

H013/H014(8c) und H007(B8) verwenden dagegen eine neue logarithmische
N3-Form. Nach u=2*pi*e und3*omega=4*c stimmen die betreffenden Faktoren
ueberein; spaeter gilt jeweils2*alpha3=N3. Das ist eine positive
Quellenbruecke, aber keine Herleitung der alten H006/H010-Terme. In
der neuen Form fehlen deren charakteristische xi-Teilausdruecke.
Undatierte Manuskripte werden nicht allein nach Etiketten chronologisch sortiert.

## 4. Das fotografierte FORTRAN-Listing

Der neu gesicherte [H015-Archivscan](https://burkhardheim.de/media/f/c57c27a0-3692-5fae-920d-5ba89ad58349)
enthaelt fotografierte FORTRAN-Listings und Teile eines datierten
Formeltyposkripts. Entscheidend ist PDF22, GBASE, gedruckte Listingseite1:
Kommentar `17/03/82`, Compilerkopf `DATE 82.223/09.22.05`.
ISN0021, rechte Zeilennummern00003710-00003713, setzt ALF3 zusammen aus
`exp(k-1)/k - q*(H_Korr+G_Korr)`, mit genau den beiden Buchformen:

- `(1+QSQRT(ETAQK(...)))` steht ausserhalb der Potenz2k+1.
- `(2.Q0*XI*ETAQK(...))**IK` enthaelt keine Wurzel.

ISN0022/00004100 setzt `AN3=2.Q0*ALF3`. Auch der bereits aus H010
bekannte Kommentarverweis `(3-5)` steht unmittelbar am alten ALF3-Block.
Root und Quellenagent haben Vollseite und vergrösserte Zeilen unabhaengig
gelesen. Das ist ein belegter Formvergleich, kein ausgefuehrter FORTRAN-Lauf
und keine globale Gleichheit der Programme oder ihrer Konstanten.

Das Typoskript auf PDF43/Druck7 nennt Northeim25.2.1982. Die fotografierten
Seiten duerfen nicht mit der heutigen PDF-Paginierung gleichgesetzt werden:
PDF38 ist eine Ausgabetabelle, PDF39 bereits Typoskriptseite4. Das benoetigte
urspruengliche Formelblatt(3-5) ist damit noch nicht als Bildstelle identifiziert.
Gleiche Formel und sichtbare Datumszeilen ersetzen weder die Provenienzpruefung
noch einen Nachweis der historischen Fehlerursache in H006.

Herkunft, Hash, Suchumfang und weitere unbewertete2009-Korrespondenzspur stehen in
[den Quellennotizen](../03_notes/ALPHA3_ORIGIN_SOURCES_2026-09-06.md).

## 5. Naechster enger Schritt

Die noch offene physikalische Frage ist nicht mehr nur „Wo steht die
Formel?“, sondern: Welche Teile der Potential-/Variationsannahmen tragen
unabhaengig, und wie eindeutig ist die empirische Koeffizientenwahl?
Keine passende Masse als Beweis verwenden und keinen neuen Fit einfuehren.

## Pruefung

Zwei Quellenagenten mit drei begrenzten Reviews (Buch, Manuskripte, FORTRAN),
Root-Vollseitengegenlesung und eigene Algebra-Tests. Alle zehn bisherigen
Rechenchecks bleiben unveraendert; 133 Tests bestehen. FIND-030 ist eine
bedingte Quellen-/Algebrabruecke: insgesamt 30 Befundgruppen, keine 30 Fehler.
Interne Gegenpruefungen sind kein externes Peer Review.

```powershell
py -3.13 -m unittest discover -s tests -p test_alpha3_origin.py -v
py -3.13 -m unittest discover -s tests -q
```
