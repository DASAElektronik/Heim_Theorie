# H006-Elektron bei N=0: Herkunft des Besetzungsquadrupels

Stand: 2026-09-06. Begrenzte Quellen- und statische Codepruefung fuer die
Elektronkomponente des in H006 mit `x_2` bezeichneten Multipletts bei `N=0`.
Unbekannte Programme und Makros wurden nicht ausgefuehrt. Die beiden XLS-Dateien
im Paket wurden weder geoeffnet noch analysiert.

## Kurzbefund

Ein **literal als Elektron-Tabellenzeile gespeichertes** Quadrupel
`n1 n2 n3 n4` wurde im untersuchten H006-nahen Material nicht gefunden.
H006 selbst liefert aber einen kurzen, fassungsinternen Formelweg zu

    (n1,n2,n3,n4) = (0,0,0,0).

Der entscheidende H006-Satz ist nicht das Konfigurationslabel `(0110)`,
sondern die Definition des Basisanstiegs `g(qk)` auf Druckseite 6 als Wert
**„fuer n_j=0“**. Fuer die Elektronkomponente folgt aus den unmittelbar
gedruckten Quantenzahlen `w_nux=1`, daher `W_nux=g(qk)`; bei `N=0` ist zudem
`f(0)=0`. Das ist ein **quellengeneriertes**, nicht ein aus einer Masse
ausgewaehltes Besetzungsquadrupel.

Die spaetere Pascal-Transkription 0.62c bildet denselben Algorithmus statisch
ab und bezeichnet `n1..n4` ausdruecklich als Zonen-Strukturparameter. Sie ist
aber eine 2006 veraenderte Hilfsimplementierung, kein Originalprogramm und
kein Primaerbeweis. Besonders `K4` lag in einer frueheren Trunkierungslesart
an der Grenze: `K4=0` haette `n4=-1` ergeben, waehrend 0.62c durch einen
expliziten Rundungsoffset `K4=1` und damit `n4=0` erzeugt. H006s eigene
gedruckte `99...99 -> 1`-Regel und die exakte Formel sprechen im H006-Profil
fuer `K4=1`; ein Massentreffer wird dafuer nicht benutzt.

## 1. Quellen und Provenienz

### H006

Datei:
`01_sources/heim_primary/Massenformel_nach_B_Heim_1982.pdf`

SHA-256 laut bestehendem Quellenkontext:
`F74DA0DAC8496BCD01226F54D88598152D67E1C954943AF61D0EC1811F5527BE`.

Der Umschlag bezeichnet die Datei als *Wiedergabe der Urschrift von Burkhard
Heim*, Forschungskreis Heimsche Theorie/IGW, 2002. Der Seitenkopf nennt IGW
Innsbruck 2003; der wiedergegebene Text ist auf den 25.2.1982 datiert.
H006 ist damit editorisch vermittelte 1982-Quelle, kein Originalfaksimile.

Visuell gepruefte Vollseiten:

- Druck/PDF 3: Multiplettnotation und `x_2(0110)_0(0,-1) = (e0,e-)`;
- Druck/PDF 5: `Q_j`, Besetzungsparameter `n_j` und Zonenbedeutung;
- Druck/PDF 6: Basisanstieg (XV), Strukturpotenz (XVI)-(XIX), `0^0`-Regel;
- Druck/PDF 8: `N=0`, `f=0`, Besetzungsparameterquadrupel und Elektronfall;
- Druck/PDF 9: stufenweise Bestimmung der `K_j`, `n_j=K_j-Q_j` und Rundung.

Bildanker: `07_outputs/source_check_images/1982_massenformel/page-03.png`,
`page-05.png`, `page-06.png`, `page-08.png`, `page-09.png`.

### H010, entpacktes untrusted Hilfspaket

Archivherkunft laut Manifest:
`https://burkhardheim.de/assets/massformula.zip`, lokal als H010 registriert.
Der Inhalt bleibt als `heim_primary_unpacked_untrusted` klassifiziert.

Statisch gelesen wurden:

- `Pascal 0.62/GPROG 0.62c.PAS`, SHA-256
  `1C1D60DC68F0EB540AA0E061896EF03559E3F57846D1E8A3AA28563694CDC59C`;
- `Pascal 0.62/gprogin.dat`;
- `Pascal 0.62/readme gprog 0.62.txt`, SHA-256
  `32F3FEA726B772170355622CED2465BE8227A69D85DF9859808D03A5454D9371`;
- `Pascal 0.62/comparison GPROGOUT Fortran - Pascal 0.62.txt`, SHA-256
  `F30D419B1A753EE59572429484A6CF9C133F5579731E17A052C10938CB87C99B`;
- `C 0.66/gprog_0.66.c`, SHA-256
  `29CBF3EBC197EFC8044C2C34D71AB40DD7C6F6829368A412812C7868A287B7B0`;
- `C 0.66/gprogin.dat` und `C 0.66/output_plus_neutrino.txt`.

Die Pascal-Kopfzeilen nennen eine GPROG-Fassung von H. D. Schulz/DESY vom
17.3.1982, Heim-Formeln vom 17.9.1978, eine MS-Fortran-Transkription von
A. Mueller 2001 und die Pascal-Transkription Olaf Posdzech 2006. Diese Angaben
sind **Selbstauskunft der spaeteren Datei**; der originale Fortran-Quelltext
liegt im entpackten Inventar nicht vor. Der C-Port wird `leovinus` zugeschrieben.
Der Vergleichsausdruck traegt daneben den Programmkopf `H.D. Schulz,
26/07/82 DESY`; die beiden eingebetteten Programmdaten werden nicht zu einer
ungeprueften einheitlichen Originalfassung zusammengezogen.

## 2. H006 bezeichnet n1..n4 ausdruecklich als Besetzungen

H006 Druck/PDF 5 schreibt fuer `1<=j<=4`, dass `Q_j` zeitlich konstant seien
und `n_j=n_j(t)` die **Besetzungsparameter** seien. Unmittelbar darunter werden
die vier Konfigurationszonen als `n(j=1),m(j=2),p(j=3),sigma(j=4)` benannt.
Die Massenhilfsfunktionen `K,G,H,Phi` enthalten anschliessend `n1..n4`.

H006 Druck/PDF 8 nennt die von der Resonanzordnung ausgewaehlten Werte sogar
„Besetzungsparameterquadrupel“. Das gesuchte Objekt ist somit eindeutig das
Viererfeld `n_j`, nicht eine Viererfolge aus der Multiplettsignatur.

H006 Druck/PDF 3 definiert dagegen die allgemeine Multiplettdarstellung als

    x_nu (epsilon B, epsilon P, epsilon Q, epsilon kappa)_epsilon C(q0,...,qP)

und listet

    x_2 (0110)_0(0,-1) = (e0,e-).

`(0110)` ist daher die Konfigurationssignatur des Multipletts, **nicht**
`(n1,n2,n3,n4)`. Das tiefgestellte `2` an `x_2` ist die laufende
Multiplettnummer `nu=2`; es ist nicht die Komponentenzahl des Algorithmus.

## 3. H006-interne Ableitung fuer die e--Komponente

### 3.1 Fester, nicht massenabhaengiger Eingang

Aus H006 Druck/PDF 3 folgen fuer das Mesonenmultiplett `x_2`:

    k=1, B=0, P=1, Q=1, kappa=0, epsilon=+1, C=0.

Die gedruckte Ladungsliste `(0,-1)` weist der geladenen Komponente `q_x=-1`
und damit `q=|q_x|=1` zu. In H006s nullbasiger Komponentenvariable ist dies
`x=1`; die spaetere Programmschleife verwendet dafuer den einbasierten Wert
`x=2`. Diese zwei Bedeutungen von `x_2` und `x=2` sind getrennt zu halten.

### 3.2 Warum die Strukturpotenz genau 1 ist

H006 Druck/PDF 6 definiert

    W_nux = g(qk) * w_nux.

In (XVII) besteht `w(1)` aus einem Term mit Vorfaktor `(1-Q)` und einem mit
Vorfaktor `kappa*Q`. Fuer `Q=1,kappa=0` verschwinden beide, also `w(1)=0`.
Die Quelle erklaert auf derselben Seite die auftretenden `0^0`-Faelle als 1
und gibt die fuer die Programmierung korrigierte Form an. Fuer `k=1` gilt:

    w_nux(k=1) = 1+w(1) = 1.

Damit folgt ohne Masse oder Referenzwert:

    W_nux = g(qk).

### 3.3 Warum daraus n=(0,0,0,0) folgt

H006 (XV) definiert gerade

    g(qk) = Q1^3*alpha1 + Q2^2*alpha2 + Q3*alpha3
            + exp[(1-2k)/3]                         fuer n_j=0.

H006 Druck/PDF 8 setzt fuer `N=0` ausdruecklich `f=0`. Die dortige Gleichung
(XXVI) hat daher dieselbe linke Seite mit `n_j+Q_j` und rechts `W_nux=g`.
Da (XV) diesen Wert ausdruecklich als Basisfall fuer `n_j=0` etikettiert,
lautet das source-lokale Besetzungsquadrupel:

    n1=0, n2=0, n3=0, n4=0.

Dies ist keine aus der Elektronenmasse gewaehlte Loesung. Es ist die von H006
selbst benannte Basisbelegung, nachdem die Elektron-Quantenzahlen die
Strukturpotenz auf 1 reduziert haben.

## 4. Kontrolle mit dem H006-Auswahlalgorithmus und die K4-Grenze

Aus H006 (X) ergibt sich fuer `k=1`, also `s=k^2+1=2`:

    (Q1,Q2,Q3,Q4) = (3,3,2,1).

H006 Druck/PDF 9 setzt bei `N=0` zuerst `W1=W_nux=g` und zieht maximal den
Kubik-, Quadrat- und Linearanteil ab. Fuer den Basisanstieg liefert dies

    (K1,K2,K3) = (Q1,Q2,Q3) = (3,3,2),

und als Rest

    W4 = exp[(1-2k)/3] = exp(-1/3).

Dies ist Fall (b). Mit der gedruckten Beziehung

    K4*(2k-1) = -3*Q4*ln(W4)

folgt bei `k=1,Q4=1` exakt `K4=1`. Da H006 anschliessend `n_j=K_j-Q_j`
setzt, ergibt sich erneut `n=(0,0,0,0)`.

Die gleiche Seite warnt, dass bei `K4` regelmaessig Dezimalstellen auftreten.
Nur eine Folge `99...99` sei als 1 zu behandeln; sonst werde abgeschnitten.
Der analytische Elektronrest liegt genau auf dieser Ganzzahlgrenze. Damit ist
der H006-Entscheid `K4=1` quellenintern begruendet und nicht nach Masse gewaehlt.

## 5. Was der statische Pascal-Code bestaetigt

`Pascal 0.62/gprogin.dat`, Zeilen 12-16, speichert fuer den Datensatz
`e,e0` nur die Multiplett-Eingaenge:

    k=Baryon number+1=1, P=1, Q=1, kappa=0.

Es speichert kein `n1..n4`-Quadrupel. `GPROG 0.62c.PAS`, Zeilen 672-704,
liest diese Werte, bildet die Komponentenladung und erhaelt fuer seine
einbasige Komponente `x=2` den geladenen Elektronfall `q_x=-1,q=1`.

Die Prozedur `GBASE`, Zeilen 350-425, ist als Rechnung fuer `N=0` bezeichnet.
Sie erzeugt `Q1..Q4`, `gkq`, und fuer den mesonischen Fall `wgxk=wg1+1`.
Mit `Q=1,kappa=0` wird `wg1=0`, also `wgx=gkq`.

Die Prozedur `GSTRUC`, Zeilen 452-512, traegt den Kommentar:

> calculates the structure parameters n1, n2, n3, n4 by use of the quantum numbers and N

Sie setzt in den Zeilen 466,472,476 und 492 jeweils `ni=ki-qi`. Bei
`print>1` wuerde sie in Zeile 508 den Tabellenkopf

    K1 K2 K3 K4 n1 n2 n3 n4

und darunter die erzeugten Werte ausgeben. Die Vorgabe steht in Zeile 38
auf `print=2`. Ein dazugehoeriges vollstaendiges `gprogout.lis` liegt im
Inventar jedoch nicht vor; der gespeicherte Vergleichsauszug zeigt beim
Elektron nur Quantenzahlen und Masse, nicht die `K/n`-Zeile.

Die statische Substitution des fest vorgegebenen Elektronfalls in genau diesen
0.62c-Pfad gibt `Q=(3,3,2,1)`, `K=(3,3,2,1)` und damit `n=(0,0,0,0)`.
Diese Aussage beschreibt den Codepfad; der Code wurde nicht ausgefuehrt.

## 6. Versionswarnung: 0.62c ist keine neutrale Kopie

Das Readme zu 0.62c dokumentiert fuer das Elektron ausdruecklich die Aenderung

    K4=trunc(0.333333333333333/1*3)=0

zu einer Berechnung mit internem Offset `0.0000000001`, die `K4=1` liefert.
Der Offset wurde in 0.62c allen Trunkierungen hinzugefuegt. Ohne diesen
Grenzentscheid waere bei `Q4=1` der Codewert `n4=-1`, also das abweichende
Quadrupel `(0,0,0,-1)`. Das ist eine dokumentierte numerische
Implementierungsvariante, nicht ein zweites von H006 gedrucktes Elektronmodell.

Die C-Datei 0.66 verwendet wiederum eine eigene Funktion `myround` mit
`eps=0.0000001`. Ihr gespeichertes `output_plus_neutrino.txt` nennt im Kopf
allerdings „C version 0.62“, druckt beim Elektron nur `N=0` und die Masse und
enthaelt keinen `K/n`-Tabellensatz. Dieses Output darf daher weder als
literal gespeichertes Besetzungsquadrupel noch ohne Vorbehalt als Ausgabe der
vorliegenden Datei `gprog_0.66.c` bezeichnet werden.

Pascal/C verwenden zudem spaetere Konstanten, beispielsweise CODATA-1998
`hbar`, `alpha^-1=137.03599976` und einen eigenen Gamma-Wert. Die Dateien
enthalten auch spaetere Referenzmassen und Hinweise auf deren Optimierung.
Diese Werte duerfen nicht in einen H006-historischen Massenlauf importiert
werden. Fuer den hier gefundenen Basisbesetzungsweg sind sie nicht noetig.

## 7. Literal gespeichert oder generiert?

| Material | Elektronzuordnung | `n1..n4`-Status |
| --- | --- | --- |
| H006 Druck 3/5/6/8/9 | `x_2`, geladene Komponente, `N=0` | Nicht als eigene Tabellenzeile gespeichert; ueber den ausdruecklich fuer `n_j=0` definierten Basisanstieg fassungsintern generiert. |
| Pascal `gprogin.dat` | Datensatz `e,e0`, spaeter einbasig `x=2,q_x=-1` | Kein n-Tupel gespeichert; nur Konfigurationseingang. |
| Pascal 0.62c Quelltext | `GBASE -> GSTRUC` | Generiert `n=(0,0,0,0)`; Tabellenkopf vorhanden, zugehoerige gespeicherte Elektronzeile fehlt. |
| Fortran/Pascal-Vergleichstext | Zeilen 79-94 `e0/e-`, jeweils `N=0` | Druckt fuer Elektron keine `K/n`-Zeile; kein literal Tupel. |
| C-Ausgabe | Multiplet 2, element `x=2`, `q_x=-1,N=0` | Keine `K/n`-Zeile; Konstanten und Versionskopf sind spaeter/uneinheitlich. |
| XLS-Dateien | nicht geprueft | Keine Aussage; Workbookanalyse war nicht Teil dieses Auftrags. |

## 8. Ansatzpunkt ohne Sollmassenauswahl

Der H006-Lehrfall kann nun vor jedem Massenvergleich so eingefroren werden:

    Quelle/Version = H006, IGW-Wiedergabe des auf 25.2.1982 datierten Textes
    Multiplett      = x_2, (B,P,Q,kappa)=(0,1,1,0)
    Komponente      = e-, epsilon=+1, C=0, q_x=-1, q=1
    Anregung        = N=0, f=0
    Strukturpotenz  = w_nux=1
    W_nux           = g(qk)
    Besetzung       = (n1,n2,n3,n4)=(0,0,0,0)
    Strukturzahlen  = (Q1,Q2,Q3,Q4)=(3,3,2,1)
    Auswahlzahlen   = (K1,K2,K3,K4)=(3,3,2,1), H006-Rundungsregel

Damit ist die fruehere Besetzungsluecke fuer **diesen** H006-N0-Fall auf
Formelebene geschlossen. Noch nicht geschlossen sind die korrekte historische
Konstantenfassung, alle Massenhilfsterme und ein vollstaendiger unabhaengiger
Rechenlauf. Der naechste Test darf das eingefrorene Nullquadrupel einsetzen
und Teilsummen ausgeben; er darf weder ein alternatives n-Tupel noch eine
Rundungs- oder Konstantenversion nach Naehe zur Elektronenmasse waehlen.

## 9. Suchgrenze

Geprueft wurden die H006-Vollseiten 3,5,6,8,9, der vorhandene H006-OCR-Text,
das komplette per `rg --files --no-ignore` inventarisierte entpackte H010-
Verzeichnis sowie gezielt alle Text-, Pascal-, C-, DAT- und gespeicherten
Outputstellen zu `n1..n4`, Elektron, `x2`, `(0110)` und Tabellenkoepfen.
H004, H007 und H013 wurden nicht als Besetzungsquelle importiert. Die XLS-
Dateien blieben ungeoeffnet; kein Programm und kein Makro wurde ausgefuehrt.

Der Negativbefund ist daher eng: Im untersuchten Text-/Code-/Outputinventar
liegt keine literal gespeicherte Elektronzeile mit vier n-Werten. Er ist keine
Behauptung, dass in unverzeichneten historischen Ausdrucken oder Archiven kein
solcher Datensatz existiert.
