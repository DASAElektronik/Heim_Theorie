# H015: statische Quellenreview von `GSTRUC`

Stand: 2026-09-06. Eng begrenzte Sichtpruefung des fotografierten
FORTRAN-Listings, seines direkten Aufrufkontexts und einer tatsaechlichen
Ausgabeseite. Das historische Programm wurde nicht ausgefuehrt. H004 und
H015 werden als getrennte Fassungen behandelt.

## 1. Ergebnis

`GSTRUC` implementiert eine eigene stufenweise Auswahl von `IK1` bis `IK4`.
Vor der vierten Auswahl besitzt sie nur zwei explizite Resttests:

```text
W4 = W3-ALF3*IK3
W4 == 0  -> Sprung 1
W4 > 1   -> Sprung 3
sonst    -> logarithmischer Zweig
```

Auf den geprueften Listingseiten werden dagegen weder die Buchgroessen
`G_j`, `delta_j G_j` und `beta_j` berechnet noch die Bedingungen aus
H004(107)/(107a) getestet. Insbesondere ist kein Test
`N_(2)^2 > G_3`, kein allgemeiner Test negativer Zonenbandbreiten und kein
Kollaps-/Ruecksetzpfad fuer `beta_j=0` zu sehen.

Der `W4>1`-Zweig ist enger: Er vermindert `IK3` genau einmal, aktualisiert
`IN3` und `N3` und addiert dann einen abgeschnittenen `ALF3*IK3`-Term zu
dem bereits im `COMMON /QUANT/` liegenden `IK4`. In diesem Zweig wird `W4` nicht
neu berechnet, es gibt keine Schleife und keine Buch-107-Nachpruefung.
Das ist ein positiver Befund ueber den fotografierten Kontrollfluss, aber
kein Beweis, dass Heim damit alle spaeteren Buchbedingungen verwerfen
wollte.

## 2. Quelle, Datierung und Bildanker

Quelle H015:

`01_sources/heim_primary/alpha3_origin/Heim_DESY_1982_Archivscan.pdf`

SHA-256:
`C242599F7AAF68BB8E2F3C7756A24687E86FAD879E4D0E22C00585A32403317F`.

Das GSTRUC-Blatt auf physischer PDF-Seite 23 traegt im fotografierten
Listing den Mitgliedsnamen `GSTRUC (HEIMS)`, die interne Zeile
`17/05/82 ... MEMBER NAME GSTRUC` und den Compilerkopf
`DATE 82.223/09.22.05`. Der GPROG-Kopf nennt entsprechend `17/03/82` und
auf Listingseite 2 `DATE 82.223/09.22.03`. Diese sichtbaren Angaben
datieren bzw. bezeichnen die fotografierten Listen; sie sind keine
forensische Authentifizierung des heutigen Scans oder einer vollstaendigen
gemeinsamen Programmfassung.

Visuell vollstaendig geprueft wurden:

- physische PDF23: `GSTRUC`, Listingseiten 1 und 2 auf einem Foto,
  `tmp/pdfs/structure_handling_fortran/originals/h015-022.jpg`;
- physische PDF4: `GPROG`, Listingseite 2 mit direktem Aufruf und Beginn
  der Resonanzgrenzen-Schleife,
  `tmp/pdfs/structure_handling_fortran/originals/h015-003.jpg`;
- physische PDF18: `GPROG`, Listingseite 1 und der angeschnittene Beginn
  von Listingseite 2 bis ISN0049,
  `tmp/pdfs/structure_handling_fortran/originals/h015-017.jpg`;
- physische PDF19: `GPROG`, Listingseite 3 mit ISN0085--0106 und
  Schleifenruecklauf,
  `tmp/pdfs/structure_handling_fortran/originals/h015-018.jpg`;
- physische PDF22: `GBASE`, sichtbare Listingseite 1 und angeschnittener
  Beginn von Seite 2, `tmp/pdfs/alpha3_desy/desy-p22.png`;
- physische PDF14: tatsaechliche Ergebnistabelle mit Spalten
  `IK1 IK2 IK3 IK4` und `N1 N2 N3 N4`,
  `tmp/pdfs/structure_handling_fortran/originals/h015-013.jpg`.

Die Seitenfolge des Scans ist keine fortlaufende Listingfolge: PDF18 zeigt
`MAIN`-Seite 1 und nur den Beginn von Seite 2; die vollstaendige relevante
`MAIN`-Seite 2 liegt auf PDF4, waehrend Seite 3 auf PDF19 fotografiert ist.
PDF5 beginnt bereits `GINIT`. Deshalb wird eine im Scan
nicht durchgehend sichtbare Initialisierung nicht aus der physischen
PDF-Reihenfolge erschlossen.

## 3. Die Auswahl in `GSTRUC`

Der Kommentar nennt als Routinenzweck die Berechnung der
Strukturparameter `N1,N2,N3,N4` aus Quantenzahlen und Konstanten. Der
tatsaechliche Deklarationsblock schreibt `COMMON /QUANT/`; in dessen
Fortsetzungszeilen liegen sowohl `IN1` bis `IN4` als auch `IK1` bis `IK4`.
Der nachfolgende Block `COMMON /EXCHA/` beginnt dagegen mit den
Arbeitsgroessen `WGX,AGX,BGX,ALF1,ALF2,ALF3,FN,...`. `COMMON /CONST/`
enthaelt den Konstantenblock. Damit wird die sichtbare Code-Deklaration
nicht mit der abweichenden Schreibweise im Prosakommentar vermischt.

Die ersten drei Schritte stehen auf PDF23, GSTRUC-Seite 1:

```text
ISN0011 / 00002000  W1=WGX*(1.Q0+FN)
ISN0012--0015       IK1=IQINT((W1/ALF1)**(1.Q0/3.Q0)); IN1=IK1-IQ1
ISN0016--0020       W2=W1-QFLOAT(IK1)**3*ALF1;
                    IK2=IQINT(QSQRT(W2/ALF2)); IN2=IK2-IQ2
ISN0021--0025       W3=W2-QFLOAT(IK2)**2*ALF2;
                    IK3=IQINT(W3/ALF3); IN3=IK3-IQ3
ISN0026 / 00003800  W4=W3-QFLOAT(IK3)*ALF3
```

`IQINT` ist hier die konkrete Ganzzahlprojektion des Listings. Die Quelle
druckt keine separate Suche nach einem Tupel, das nachtraeglich alle
H004-Strukturbedingungen erfuellt.

## 4. Die drei Kontrollzweige fuer `IK4`

Der normale positive Restzweig lautet:

```text
ISN0031 / 00003920  REST=QFLOAT(2*IK-1)/QFLOAT(3*IQ4)
ISN0032 / 00004000  TEMP=-QLOG(W4)/REST
ISN0033 / 00004100  IK4=IQINT(TEMP)
```

Bei `W4=0` springt ISN0027 zu Label 1 und setzt in
ISN0035/00004210:

```text
IK4=IQINT(ALF3*QFLOAT(IK3)).
```

Bei `W4>1` springt ISN0029 zu Label 3. Der gedruckte Ablauf ist:

```text
ISN0037 / 00004230  IK3=IK3-1
ISN0038 / 00004240  IN3=IK3-IQ3
ISN0039 / 00004250  N3=QFLOAT(IN3)
ISN0040 / 00004260  IK4=IK4+IQINT(ALF3*QFLOAT(IK3))
ISN0041 / 00004300  IN4=IK4-IQ4
ISN0042 / 00004400  N4=QFLOAT(IN4)
```

Damit ist der Additionsterm eindeutig an den **bereits verminderten**
`IK3` gebunden. Ebenso eindeutig bleibt aber der linke Summand der alten
Variablen `IK4` erhalten. Innerhalb dieses aufgerufenen GSTRUC-Zweigs gibt
es davor keine lokale `IK4`-Zuweisung: Die Log- und Nullzweige werden durch
den Sprung uebersprungen. Weil `IK4` im `COMMON /QUANT/` liegt, ist die
engste sichere Aussage, dass dieser Pfad den beim Eintritt vorhandenen
Wert weiterverwendet. Die nur ausschnittsweise fotografierten Caller- und
GBASE-Seiten belegen nicht, dass der Wert im ganzen Programm niemals
initialisiert wird; eine Behauptung ueber undefinierten Speicher oder den
tatsaechlichen Erstaufruf waere daher zu stark.

## 5. Caller und sichtbare Ausgabe

GPROG-Seite 2 auf physischer PDF4 ruft zunaechst `GBASE` auf
(ISN0044/00004800), laeuft dann ueber Anregungsordnungen und druckt:

```text
ISN0059 / 00005600  CALL GSTRUC
ISN0060 / 00005700  CALL GMASS(AM)
```

Die argumentlose Form des ersten Aufrufs stimmt mit dem Datenaustausch
ueber die `COMMON`-Bloecke ueberein. Die danach auf GPROG-Seiten 2--3
stehende `COMPUTE THE RESONANCE LIMITS`-Schleife ist ein eigener
nachgelagerter Programmteil; sie ist kein in GSTRUC eingebauter Ersatz fuer
die Buchbedingungen (107)/(107a).

GSTRUC-Seite 2 enthaelt fuer `IPRINT>=2` eine Ausgabe von
`W1,W2,W3,W4,REST` (ISN0043/00004500). Unbedingt ausgegeben werden danach
`IK1...IK4` und `IN1...IN4` (ISN0046/00004700). Die fotografierte
Ergebnistabelle auf PDF14 zeigt die entsprechenden `IK`- und `N`-Spalten.
Auf dieser Stichprobenseite steht kein zusaetzliches Feld fuer
`G_j`, `beta_j`, einen Gate-Status oder eine Kollapskorrektur. Das ist eine
begrenzte Bestätigung der sichtbaren Ausgabestruktur, kein vollstaendiger
Audit aller Ergebnisblaetter.

## 6. Enger Vergleich mit H004(107)/(107a)

H004 Druck321/PDF327 verlangt in (107) unter anderem
`delta_j G_j>G_(j+1)` und `delta_j G_j>=delta_(j+1)G_(j+1)`.
Druck328/PDF334 formuliert in (107a) den nicht kollabierten Zweig als
`beta_(j+1)=delta_j G_j-G_(j+1)>=1` und einen gesonderten Kollapsfall bei
`beta=0`. Fuer den Uebergang 2 nach 3 fuehrt die dortige Buchdefinition zum
konkreten Gate `N_(2)^2>G_3`.

Keine dieser Groessen oder Vergleiche kommt auf den beiden vollstaendig
sichtbaren GSTRUC-Listingseiten vor. Auch nach `IN2=IK2-IQ2` und
`N2=QFLOAT(IN2)` folgt unmittelbar die Restbildung `W3`; es steht dort kein
Zwischensprung zu einer Strukturkorrektur. Der `W4>1`-Zweig betrifft nur
die dritte und vierte Auswahl und ist daher keine Implementierung des
fehlenden 2-nach-3-Gates.

Quellenfest ist somit nur: **Das fotografierte H015-GSTRUC berechnet ein
Tupel durch seine eigene Exhaustions-/Restlogik und prueft die unmittelbaren
Buch-107/107a-Gates nicht.** Ob die spaetere Buchfassung eine theoretische
Revision, Erweiterung oder ausfuehrlichere Darstellung einer anderen
Programmfassung ist, laesst sich aus der Formähnlichkeit und den sichtbaren
Datumszeilen nicht entscheiden.

## 7. Such- und Aussagegrenze

Gezielt gelesen wurden GSTRUC, der sichtbare direkte GPROG-Aufruf,
GPROG-Schleifenende, der sichtbare GBASE-Kontext und eine repräsentative
Ausgabeseite. GMASS und die Resonanzmassen wurden nicht neu analysiert, da
sie die vorgeschaltete Tupelauswahl nicht definieren. Nicht behauptet wird,
dass der gesamte 43-seitige Archivscan jede historische Initialisierung,
Programmrevision oder externe Vorpruefung enthaelt. Ebenso folgt aus dem
fehlenden Gate in GSTRUC keine globale Widerlegung der diskreten
Strukturidee.
