# `alpha3` im fotografierten DESY-FORTRAN-Listing

Stand: 2026-09-06. Eng begrenzte Sichtpruefung der PDF-Folios 21--26.

## 1. Ergebnis

Das fotografierte FORTRAN-Listing zeigt in `GBASE`, ISN 0021, die
`ALF3`-Formel bereits in derselben algebraischen Gestalt wie die spaeteren
H010-Pascal-/C-Transkriptionen. Insbesondere sind beide gegenueber H006
festgehaltenen Unterschiede schon im Foto sichtbar:

1. `1+sqrt(eta_qk)` steht **vor** und damit ausserhalb der Potenz
   `2*IK+1`.
2. Der zweite Korrekturterm enthaelt `(2*xi*eta_qk)**IK`, ohne einen
   Wurzeloperator.

Damit sind diese beiden Formen jedenfalls nicht erst als Aenderungen der
Pascal-/C-Uebertragung von 2006 nachweisbar. Das Listing erklaert aber nicht,
warum diese Form gegenueber dem Druck H006 abweicht, und entscheidet nicht,
welche Fassung physikalisch beabsichtigt oder richtig ist.

## 2. Quelle und Beleggrenze

Geprueft wurde statisch:

`01_sources/heim_primary/alpha3_origin/Heim_DESY_1982_Archivscan.pdf`

SHA-256:
`C242599F7AAF68BB8E2F3C7756A24687E86FAD879E4D0E22C00585A32403317F`.

PDF-Folio 22 zeigt im Kopf des fotografierten Ausdrucks:

```text
17/03/82 ... MEMBER NAME GBASE (HEIMS) ... FORTRAN
SYSTEM/370 FORTRAN H EXTENDED (ENHANCED)
DATE 82.223/09.22.05
```

Das belegt die im Foto sichtbare Bezeichnung und Datierung des Listings.
Es ist keine forensische Authentifizierung des Papieroriginals, keine
Handschrift-/Signaturpruefung und kein Nachweis einer persoenlichen
Autorfreigabe jeder Codezeile. Das Programm wurde weder kompiliert noch
ausgefuehrt.

## 3. Wortnahe Transkription

Auf PDF-Folio 22, Listing-Seite `GBASE PAGE 1`, steht nach dem Kommentar
`(3-5) # F(KQ,K) REAL` bei ISN 0021 und den gedruckten physischen
Listingzeilen `00003710`--`00003713`:

```fortran
ALF3=QEXP(K-1.Q0)/K-KQ*(ALFA/3.Q0*(1.Q0+QSQRT(ETAQK(KQ,K)))*
*(XI/ETAQK(KQ,K)**2)**(2*IK+1)*ETAQK(KQ,K)**3+ETAQK(1.Q0,1.Q0)/
*(EBN*ETAQK(KQ,K))*(2.Q0*XI*ETAQK(KQ,K))**IK*((1.Q0-
*QSQRT(ETAQK(KQ,K)))/(1.Q0+QSQRT(ETAQK(KQ,K))))**2)
```

Die Sternchen am linken Fortsetzungsrand gehoeren zur
FORTRAN-Fortsetzungssetzung. Normalisiert, aber ohne Umformung, ist dies:

```text
alpha3 = exp(k-1)/k
       - q * [ (alpha/3)*(1+sqrt(eta_qk))
               *(xi/eta_qk^2)^(2k+1)*eta_qk^3
             + eta_11/(e*eta_qk)*(2*xi*eta_qk)^k
               *((1-sqrt(eta_qk))/(1+sqrt(eta_qk)))^2 ].
```

`IK` ist im Listing der ganzzahlige Index, waehrend `K` seine
Gleitkommadarstellung ist; diese Schreibdifferenz aendert den hier
verglichenen Potenzbereich nicht.

Unmittelbar danach setzt ISN 0022, physische Listingzeile `00004100`,

```fortran
AN3=2.Q0*ALF3
```

und bildet damit auch die aus H006/H010 bekannte Beziehung `N3=2*alpha3`
im Programm ab.

## 4. Anschluss im selben Foto-Listing

PDF-Folio 23 (`GSTRUC`) verwendet `ALF3` anschliessend bei der Ermittlung
der vierten Strukturkomponente, unter anderem in den sichtbaren Zeilen
`00003800`, `00004210` und `00004260`. Das stuetzt die Lesart als aktiven
Rechenwert und nicht bloss als auskommentierte Alternativformel. Es liefert
keine zusaetzliche Herleitung der Formel.

## 5. Abgleich mit H006 und H010

- H010-Pascal, Zeilen 383--384, und H010-C, Zeilen 807--808, setzen genau
  dieselben beiden fraglichen Bereiche: einfacher Faktor
  `(1+sqrt(eta_qk))` vor der Potenz und keine Wurzel um den zweiten
  `2*xi*eta_qk`-Faktor.
- H006 (IX), Druck/PDF 5, setzt demgegenueber den ersten Produktfaktor mit
  unter die Potenz und zeigt im zweiten Term ein Wurzelglyph. Dessen genaue
  Radikandenreichweite bleibt wegen des fehlenden klaren Vinculums offen;
  dass im FORTRAN-Term gar kein `QSQRT` steht, ist dagegen eindeutig.
- Der neue Fund ist daher eine positive alte Codebruecke zur H010-Form,
  aber kein Erratumbeleg gegen H006 und keine theoretische Begruendung.

## 6. Begrenzte Durchsicht der sechs Folios

- PDF 21: Fortsetzung/Abschluss `GINIT`; keine `ALF3`-Definition.
- PDF 22: `GBASE`; einzige Definition im geprueften Bereich.
- PDF 23: `GSTRUC`; aktive Verwendung von `ALF3`, keine neue Definition.
- PDF 24: `GMASS` und Beginn `ETAQK`; keine alternative `ALF3`-Formel.
- PDF 25: `IBINOM` und Compilerzusammenfassung; keine `ALF3`-Formel.
- PDF 26: Linkage-/Module-Map; keine `ALF3`-Formel.

Tragende Vollseitenbilder:

- `tmp/pdfs/alpha3_desy/desy-p22.png` (`GBASE`, Formel)
- `tmp/pdfs/alpha3_desy/desy-p23.png` (`GSTRUC`, Verwendung)

Lesecrop ohne eigene inhaltliche Retusche:
`tmp/pdfs/alpha3_desy/desy-p22-alf3.png`.

Die Durchsicht dieses Ausschnitts erlaubt keine Aussage, dass nicht
gepruefte oder im Scan fehlende Typoskriptseiten 1--3 keine weitere
Erklaerung enthielten.
