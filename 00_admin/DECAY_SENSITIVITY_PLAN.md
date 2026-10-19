# Vorvertrag: A(1)=1/3 versus 1/5

2026-09-06, Etappe 35. Ausgang `22001a2`, Branch `normalization-review`.
Maschinenvertrag: `04_reconstruction/alpha_audit/decay_sensitivity_inputs.json`.
Vor der ersten neuen Auswertung festgelegt und per Git gesichert.

## Auftrag

Vier vorab benannte Zellen: beide bisherigen Buch-Alpha-Profile mal
A=1/3 (Heims Wahl z5) und A=1/5 (eigene Sensitivitaet zum Kandidaten z3).
Alle Zellen berichten, keine Wahl nach Treffer, Rest oder Masse.

- Feste a_j, w, A16, eta, Y3/Y9 und Buchzustandsparameter.
- Gleichzeitig Externterm E_A(N4), Referenz g_A=B+E_A(1) und W_A=w*g_A
  aendern; E_A(0)=1 bleibt. Kein einseitiger Vergleich als Hauptergebnis.
- Gewoehnliche Vorwaertsauswahl nur innerhalb ihres festgelegten Zweiges.
  Keine neue TRC-Promotionsschwelle, Kappung oder Transferregel erfinden.
- Exakte Integergleichung und direkte ungewichtete Strukturbedingungen
  separat von Floor-Ausgabe, reeller N4-Relaxation und 107b-Gewichtung.
- Fuer jede Zelle neue endliche Obermenge herleiten; rationale Intervalle
  zur Vorzeichen-/Zweigpruefung. Keine Toleranz nach Ergebnis waehlen.
- Keine neue Masse, empirische Bewertung, Quellenkorrektur oder Behauptung
  einer aus (79)/(96b) hergeleiteten physikalischen Ersatzfunktion.

## Abschlussstatus

Etappe 35 ist unter dem vorab gesicherten Vertrag ausgewertet. Der Vertrag
wurde nicht nach den Ergebnissen umgestellt:

- `A(k=1)=1/3`: beide Alpha-Profile liefern in ordinary floor
  `(14,9,13,7)` und die direkte Bandbreite `(2459,-10,6)`.
- `A(k=1)=1/5`: beide Alpha-Profile erreichen nach
  `(N1,N2,N3)=(14,10,1)` die Sattigungsgrenze; der reelle vierte Wert
  `~=14.345` liegt ueber der Kappe `alpha3*N3~=0.979`. Der begrenzte
  Rechner gibt deshalb kein `N4` aus und erfindet keine Fortsetzung.
- Frische Obermenge `(14,19,26,25)`: 1239 Tripel und 9231 ganze Tupel je
  Zelle. Keine exakte Loesung von (108) zusammen mit den direkten
  nichtkollabierten Gates.
- Die vorab definierte engere reelle Diagnose `0<=N4<=N3-1` bleibt
  unveraendert und wird als engere Diagnose bezeichnet. Der zusaetzliche
  Bereich bis zur vollen direkten Domaene `0<=N4<N3` wurde separat
  ausgeschlossen; er ist keine nachtraegliche Aenderung des Inputs.
- `fixed` bedeutet paarweise innerhalb desselben Alpha-Profils. Ordinary
  floor ist nicht das vollstaendige Quellen-`TRC`; (107b) bleibt separat.
- 15 neue Tests,331 insgesamt; alte12 Ergebnischecks sowie Existenz-,
  Transport-, Rekurrenz- und Registerchecks bestanden. FIND-045 bezeichnet
  45 Befundgruppen, nicht45 Fehler. Keine Masse, kein Fit und keine neue
  Heim-Fassung.

Naechster begrenzter Auftrag: die vorhandene Buch-Sattigungsregel im
erreichten z3-Zweig anwenden und ihren Gleichungserhalt getrennt pruefen,
ohne freie A-/Y-/Restwahl.

## Arbeitsteilung

- [x] Root: neuer gebundener Rechner, exakte Kontrollen, Integration.
- [x] data_audit: unabhaengige Zahlenauswertung aus eigenem Rechenweg.
- [x] book_derivation: endliche Bereiche, gekoppelte Existenzaussagen.
- [x] alpha_versions: Vergleichsvertrag/Zuschreibung und Ergebnisgegenreview.
- [x] Tests, Register, Bericht und Wiedereinstieg; alte Ergebnischecks und
  die benannten Zertifikats-/Validatorlaeufe bestanden.

Die urspruengliche numerische Arbeitsteilung beschraenkte Agenten auf neue
`DECAY_*_REVIEW`-Dateien. Der spaeter ausdruecklich delegierte administrative
Abschluss aktualisiert zusaetzlich die benannten Navigationsdateien. Alte
Eingaben/Rechner/Snapshots bleiben unveraendert. Ausgangsbelege sind
Etappen30-34; neue Originallekture nur wenn ein konkret fehlender
Vertragsbestandteil auftaucht.
