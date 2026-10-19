# Koennen wir die Luecke der Kreiswelle schliessen?

Stand 2026-09-06, sechste begrenzte Etappe. Ausgangspunkt 4155762.
Nutzerziel: fehlende Schritte nach Moeglichkeit besser herleiten, neu rechnen
und auch elementare Fehler oder negative Ergebnisse offen dokumentieren.

## 1. Ergebnis und entscheidende Unterscheidung

Wir koennen einen einfachen mathematischen Ringschluss vollstaendig
herleiten. Er zeigt aber gerade, welche ZUSATZANNAHMEN erforderlich sind.
Damit ist noch keine Luecke der originalen Heim-Herleitung geschlossen.

- Periodizitaet erlaubt ganzzahlige Moden; sie bestimmt weder genau eine
  Wellenlaenge pro Umfang noch den Radius oder die Wellendynamik.
- Wird der Wellenimpuls mit dem korpuskularen Impuls gleichgesetzt, muessen
  Energie, Welle und Bezugssystem zusammenpassen. Eine Phasengeschwindigkeit
  c folgt fuer diese Gleichsetzung nicht einfach aus dem Quantendualismus.
- Eigene ungefittete Ergaenzungen aendern die algebraischen Ergebnisse
  erheblich. Das sind Diagnosevarianten, keine bestaetigte Verbesserung.
- Das Manuskript1981 und BandII unterscheiden sich nicht nur in Y/Y3,
  sondern in der Definition von A_k und in der Begruendung von A=4C.

Wir unterscheiden deshalb: **aus vorhandenen Annahmen hergeleitet**,
**durch eigene Annahmen ergaenzt**, **lokal widerspruechlich** und
**im untersuchten Umfang noch nicht bestimmt**. Keine dieser Kategorien
darf unbemerkt in eine andere uebergehen.

## 2. Was Heim tatsaechlich vorgibt

Die gezielte Quellenreview bestaetigt EDM2 Druck276/277=PDF282/283:
lambda_H=2*pi*r_H wird ausdruecklich eingesetzt. Die Welle heisst stehend
und soll die ganze Kugeloberflaeche 4*pi*r_H^2 als s-Niveau bestimmen.
Druck301/PDF307 verwendet die Meridianrelation nochmals. Das sind
Quellenannahmen/Modellzuordnungen, keine von uns erfundenen Formeln.

Nicht in der geprueften H-Kette ausgeschrieben sind die Wellenfunktion,
ein passender Operator, die Phasenrandbedingungen und eine Auswahl n=1.
Andere allgemeine Wellen-/Eigenwertgleichungen kommen im Buch durchaus
vor; deren Uebertragung auf genau dieses H-Problem wurde nicht nachgewiesen.
Der negative Befund betrifft nicht den gesamten Nachlass.

Eine neue Kontextstelle, Druck161/PDF168, verbindet zyklischen Kondensorfluss,
Eigenfrequenz und eine als Aggregatdurchmesser bezeichnete Wellenlaenge.
Heim nennt mc*lambda=h dort empirischen Quantendualismus. Diese allgemeine
Deutung ist noch keine Gleichsetzung mit einer laufenden de-Broglie-Welle
des gebundenen Elektrons. Der Kontextwechsel muss weiterhin erklaert werden.

Quelle/Lesung: `reviews/WAVE_CLOSURE_SOURCE_REVIEW_2026-09-06.md` unter
`04_reconstruction/alpha_audit/`. Hauptagent hat Druck161,276,277 visuell
kontrolliert; die Review dokumentiert weitere Seiten und Suchgrenzen.

## 3. Unsere explizite Ringherleitung

Wir setzen selbst einen Ring mit festem Radius R>0 voraus, einen komplexen
skalaren, zweimal differenzierbaren Zustand psi(phi) und den Operator
L=-d^2/dphi^2. Dies ist ein eindimensionaler Kreis S1, keine Kugelschale,
kein Spinor und noch kein Wasserstoff-Hamiltonoperator.

```text
L psi = kappa^2 psi,
psi(2*pi)=psi(0),  psi'(2*pi)=psi'(0),  psi nicht identisch null.
```

Partielle Integration liefert wegen der Randbedingungen
integral(psi* L psi)=integral(|psi'|^2)>=0. Die Eigenwerte sind nichtnegativ.
Fuer kappa>0 ist die allgemeine Loesung eine Kombination aus exp(+i*kappa*phi)
und exp(-i*kappa*phi). Die Randbedingungen haben nur dann eine nichttriviale
Loesung, wenn cos(2*pi*kappa)=1. Somit sind die Moden ganzzahlig:

```text
psi_n(phi)=a*exp(i*n*phi), n ganzzahlig,
Eigenwert von L: n^2,
N=|n|>=1:  lambda=2*pi*R/N.
```

Fuer n=0 ergibt die Differentialgleichung psi=a+b*phi; Periodizitaet setzt
b=0. Die konstante Mode ist also erlaubt, hat aber keine endliche raeumliche
Wellenlaenge. Sie darf nicht aus dem raeumlichen Problem gestrichen werden.

Genau lambda=2*pi*R erhalten wir erst durch die weitere Auswahl N=1:
nichtkonstante Mode und kleinste nichtverschwindende Wellenzahl. Dies ist
nicht automatisch der niedrigste Energiezustand einer noch unbekannten
Dynamik. Die Periodizitaet allein legt R oder eine Frequenz ueberhaupt nicht
fest. Der Ausschluss n=0 aus unserer spaeteren endlichen Wellenlaengenrechnung
ist insbesondere kein Ausschluss des Wasserstoff-Grundzustands.

### Stehende Welle ist nicht eine einzelne laufende Mode

Mit einer zusaetzlichen Zeitabhaengigkeit exp(-i*omega*t) laufen die Moden
n und -n in entgegengesetzter Phasenrichtung. Ihre Ueberlagerung kann ein
stehendes Muster ergeben. Bei der ebenfalls zusaetzlichen Quantenkonvention
-i*hbar*d/dphi hat eine einzelne Mode den Drehgeneratorwert hbar*n.
Fuer eine ausgeglichene stehende Kombination ist dessen Mittelwert null,
der Mittelwert des Quadrats aber hbar^2*n^2.

Man darf daher weder der ganzen stehenden Welle ungekennzeichnet den
signierten Impuls einer Teilwelle zuweisen noch aus dem verschwindenden
Mittelwert eine verschwindende Wellenzahl folgern. hbar*n/R ist hier ein
tangentialer Modenimpuls, kein globaler kartesischer Impulseigenwert.

## 4. Welche Welle traegt welche Energie und welchen Impuls?

Fuer unsere Diagnose sei in EINEM Bezugssystem ausdruecklich angenommen:

```text
E_tot=mc^2=h*nu>0,  nu=v_phase/lambda,
zeta=v_phase/c>0,  p_korpuskel=beta*m*c,  0<beta<1.
```

Die Masse m ist wie im bisherigen Audit bedingt die gleiche geschwindigkeits-
abhaengige Masse; keine neue Ruhemasse wird eingesetzt. Dann folgt

```text
lambda=zeta*h/(m*c),
|p_welle|=h/lambda=m*c/zeta.
```

Wenn zusaetzlich dieser Impuls einer laufenden Teilwelle mit dem
korpuskularen Impuls identisch sein soll, muss

```text
zeta=1/beta, also v_phase=c^2/v
```

gelten. zeta=1 kann diese zusaetzliche Gleichsetzung bei 0<beta<1 nicht
erfuellen. Eine andere Ringmodenzahl hilft nicht; N kuerzt sich hier heraus.
Die Folgerung setzt dieselbe Welle, denselben Energiebegriff und denselben
Impulsbegriff voraus. Ohne diese Bruecken ist sie KEIN unmittelbarer
Widerspruch zwischen beliebigen Compton- und de-Broglie-Kontexten Heims.

Historische Gegenkontrolle: de Broglies Nobelvortrag von1929, Druck247-249,
PDF4-6, entwickelt fuer ein freies Teilchen die Phasengeschwindigkeit c^2/v,
unterscheidet sie von der Gruppengeschwindigkeit v und gibt lambda=h/p an.
Das ist eine historische Begriffsreferenz, keine geloeste Beschreibung des
Heim-H-Systems im Protonfeld. Eine Phasengeschwindigkeit oberhalb c ist hier
nicht die Geschwindigkeit eines Signals oder des Elektrons.
[Offizielle Vortragsfassung](https://www.nobelprize.org/uploads/2016/04/broglie-lecture.pdf).
Dateihash und eng gepruefter Umfang: `03_notes/WAVE_REFERENCE_2026-09-06.md`.

## 5. Die neu berechnete, ausdruecklich bedingte Schliessung

Wir behalten fuer eine isolierte Diagnose Heims noch nicht gerechtfertigte
Geometrieregel y=R*s, s=sqrt(1-beta^2), und die bisherige Energiebilanz bei.
f bezeichnet hier den eingesetzten Energiefaktor, NICHT eine Frequenz:

```text
e^2*(1-C)=4*pi*epsilon0*y*E_kin,
E_kin=f*mc^2,
alpha_prime=e^2/(4*pi*epsilon0*hbar*c),
R=N*lambda/(2*pi)=N*zeta*hbar/(mc).
```

Nach Einsetzen und Kuerzen folgt ohne fehlenden Dimensionsfaktor

```text
K := alpha_prime*(1-C) = N*zeta*f*sqrt(1-beta^2).
```

Vor dem Kuerzen haben y*E_kin und hbar*c beide die Einheit Joule mal Meter.
C ist der dimensionslose Korrekturfaktor, keine Ladung. Fuer N=1,zeta=1
und f=beta entsteht die bisherige Quellen-Schliessung K=beta*s.

Die folgenden Werte benutzen nur den unveraenderten Buchfall Y3=1 und
mathematisches pi. KEIN gemessener Alpha-Wert wird als Ziel eingesetzt.
beta ist die algebraische Geschwindigkeitsvariable; ihre Zuordnung zu
einer messbaren Kopplung bleibt eine Quellenannahme.

| Eigene Diagnose bei gleichem Buch-K | Bedingung | Rechenergebnis |
|---|---|---|
| N=1, Phasengeschwindigkeit c, Energie pc | K=beta*s | 1/beta_klein=137.035960995152 |
| N=2, sonst unveraendert | K=2*beta*s | 1/beta_klein=274.077395315928 |
| N=3, sonst unveraendert | K=3*beta*s | 1/beta_klein=411.117613252161 |
| N=1, gleicher Wellen-/Korpuskelimpuls erzwungen, Energie weiterhin pc | zeta=1/beta, also K=s | beta=0.999973375371 |

Bei festem N und zeta besitzen die ersten Faelle zwei positive Zweige,
sofern 0<K/(N*zeta)<1/2; am Maximum fallen sie zusammen. Periodizitaet
entscheidet nicht zwischen ihnen. In der letzten Zeile ist beta=sqrt(1-K^2).
Es bleibt dort kein kleiner beta-Zweig wie im Quellenansatz.

Diese letzte Zeile ist KEINE neu vorhergesagte Feinstrukturkonstante. Sie
zeigt die Konsequenz einer einzelnen expliziten Ersetzung, waehrend pc,
Meridianregel und weitere offene Annahmen stehen bleiben. Eine physikalisch
konsistente Reparatur muesste Energie, Geometrie und Dynamik gemeinsam
begrunden. Die alte numerische Uebereinstimmung wird durch eine bessere
Begriffszuordnung nicht automatisch erhalten.

## 6. Manuskript und Buch muessen getrennt bleiben

Die visuelle Versionsreview findet fuer t_k=sqrt(eta_1k):

```text
Manuskript1981 p4/5: eta_1k*A_k*(1+t_k)=1-t_k,
BandII p299/302:     eta_1k^(-1/2)*A_k*(1+t_k)=1-t_k.
```

Bei formal gleichgesetzten eta ergibt das
A_k_MS=A_k_Buch/eta_1k^(3/2). Beide lokalen Definitionen koennen intern
mit A=4*A1*A2 verwendet werden, sind aber nicht dieselbe Funktion.
Eine vollstaendige historische Gleichsetzung der jeweiligen eta-Definitionen
wurde damit nicht nachgewiesen. Der Rechner verwendet weiterhin NUR Buch-A_k.

Im Manuskript p5 wird A=4C wegen freier Verfuegbarkeit einer Integrations-
konstante erwogen; BandII p301 motiviert die angenommene Proportionalitaetszahl
vier mit vier besetzten Zonen. Y des Manuskripts ist nicht still Buch-Y3.
Eine Begruendungsvariation ist ein Versionsbefund, fuer sich kein Beleg
eines numerischen Fits oder einer absichtlichen Manipulation.

Wir koennen die offene Proportionalitaet als EIGENE Diagnose sichtbar machen:
C_eff=rho*P*Y3 mit P=A1_Buch*A2_Buch. Die Quelle fuehrt Y3 direkt in der
Schliessung ein; C_eff ist unsere effektive Zusammenfassung, keine dort
ausgeschriebene C-Definition. Im neuen Rechner heisst dieses Ausgabefeld C.
rho ist unser zusaetzlicher Faktor, kein neu gefundenes Heim-Symbol.
Dann ist K=alpha_prime*(1-rho*P*Y3).
Die Paare (rho,Y3)=(1,1),(2,1/2),(1/2,2) liefern exakt dasselbe K.
Diese Korrektur bestimmt nur das Produkt rho*Y3, nicht beide Faktoren
einzeln. Y3 multipliziert dabei NICHT das ganze K. Die Demonstration
passt nichts an und schreibt Heim nicht automatisch zwei freie Parameter zu.

Der bekannte Energieordnungs-Konflikt steht bereits im Manuskript p4:
W<=X<=V und E_k>0 passen nicht zu -E_k=V-W. Das ist ein lokaler
algebraischer Widerspruch der gemeinsam gelesenen Aussagen. Dasselbe
Problem in einer frueheren Fassung ist staerker belegt als ein einzelner
OCR-Fehler; es beweist aber noch nicht, dass jede korrigierte Fassung oder
die gesamte Theorie unrettbar waere. Details und eigener minimaler
Korrekturkandidat bleiben in `BOOK_ENERGY_ORDER_ISSUE.md` getrennt.

Versionsreview: `04_reconstruction/alpha_audit/reviews/CLOSURE_VERSION_REVIEW_2026-09-06.md`.

## 7. Was spaeter fair veroeffentlicht werden kann

Ein belastbarer Bericht muss Version, Seite, genaue Annahmen, Rechenweg,
unabhaengige Gegenpruefung und Aussagegrenze enthalten. Zu trennen sind:

- Ein gedruckter lokaler Widerspruch unter gleichzeitig geltenden Aussagen.
- Eine nicht gerechtfertigte, fuer eine Schlussfolgerung benoetigte Beziehung.
- Eine eigene Ergaenzung und ihre bedingt berechneten Folgen.
- Ein experimentelles Scheitern einer hinreichend bestimmten Modellfassung.

Den letzten Punkt haben wir in dieser Etappe nicht untersucht. Eine Luecke
allein beweist keine falsche Vorhersage; ein echter Widerspruch in notwendigen
Voraussetzungen kann dagegen eine konkrete Fassung zu Fall bringen. Erst
die Abhaengigkeitspruefung zeigt, wie weit der Befund reicht. Wir wollen
weder eine Uebereinstimmung erzwingen noch eine Widerlegung vorwegnehmen.
Jetzt entstehen Arbeitsberichte und Git-Sicherungen, keine neue externe
Publikation im Namen des Nutzers.

## 8. Reproduzierbarkeit und Fortsetzung

Neuer Rechner `scripts/audit_wave_closure.py`, Snapshot
`05_analysis/wave_closure_diagnostics.json`. 13 neue Tests,69 insgesamt.
Rationale Dimensionskontrolle und 80/120-Stellen-Konvergenz sind enthalten.
Die unabhaengige Review fand zwei Randfaelle beim Maximum der Zweiggleichung:
getrennte Rundung einer Doppelwurzel und Rundung von Eingaben auf die
Definitionsgrenze. Der neue Rechner prueft diese Grenze exakt mit Fraction
und rundet die Doppelwurzel nur einmal. Unzureichende Praezision wird
explizit abgelehnt. Die bisherigen fuenf Rechner/Snapshots bleiben unveraendert.
Testgruener Code ist keine Bestaetigung der zugrunde liegenden Physik.
Die Quellen-, Versions- und Implementierungsreviews sind abgeschlossen;
192 zusaetzliche rationale Vergleichswerte wurden unabhaengig kontrolliert.

```powershell
py -3.13 scripts/audit_wave_closure.py --check --verify-sources
py -3.13 -m unittest discover -s tests -q
```

Naechster inhaltlicher Einstieg: die allgemeinen zyklischen Fluss- und
Eigenfrequenzbegriffe um EDM2 Druck160/161 und (76) auf eine moegliche
Bruecke zur H-Welle pruefen. Daneben die Integration A=4A1A2 und die
unabhaengige Festlegung von C/Y3 verfolgen. Falls eine solche Bruecke fehlt,
ist die Alpha-Herleitung als bedingt/unterbestimmt zu bilanzieren; nicht
beliebig immer weitere Varianten auf bekannte Zahlen einstellen.
