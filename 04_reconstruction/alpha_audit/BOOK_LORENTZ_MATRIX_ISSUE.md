# BOOK-LORENTZ-MATRIX-001: gedruckter A_--Block

Stand2026-09-06. Neuer lokaler Befund, getrennt von Energieordnung und
Alpha-Druckpaaren. Gilt unter gewoehnlicher komplexer Trigonometrie und
Matrixtransposition. Keine Aussage ueber einen Defekt der ganzen Theorie.

## Quellenlesung

EDM1, dritte geaenderte Auflage1998, Druck21/PDF29. Zwei unabhaengige
Bildlesungen durch Hauptagent und Quellenagent bestaetigen im 1-4-Block:

```text
A = [[cos(psi), i*sin(psi)], [-i*sin(psi), cos(psi)]]
tan(psi) = i*beta,   c*beta=v
behauptet: A_minus * A_minus^T = I4.
```

Die anderen beiden Raumkomponenten bleiben jeweils1. `sin` und `cos`
stehen im Druck, nicht `sinh` und `cosh`. Fuer ein anderes Produkt,
eine andere Transposition oder nichtstandardmaessige Trigonometrie wurde
im untersuchten unmittelbaren Kontext keine Definition gefunden.

## Bedingte Rechnung

Mit a=cos(psi), d=sin(psi) gilt exakt:

```text
A*A^T = (a^2-d^2)*I2
a^2+d^2=1, d/a=i*beta
a^2=1/(1-beta^2), d^2=-beta^2/(1-beta^2)
A*A^T = ((1+beta^2)/(1-beta^2))*I2.
```

Bei beta=3/5 ergibt das17/8 statt1. Fuer die volle4x4-Matrix ist das
Produkt diagonal(17/8,1,1,17/8), NICHT17/8 mal die ganze Einheitsmatrix.
Bei beta=0 verschwindet der Konflikt. Ein gemeinsamer Vorzeichenwechsel
von sin/cos aendert ihn nicht. Konjugiertes Transponieren ist ein anderer
Test und darf nicht still fuer das gedruckte T eingesetzt werden.

## Vergleichsstelle und moegliche Reparatur

EDM1 Druck56/PDF63, (5c), gibt in einer anderen, sechsdimensionalen Matrix
C fuer den 1-4-Block gerade [[cos(psi),sin(psi)],[-sin(psi),cos(psi)]]
an, mit i*beta=tan(psi) und u*beta=v. Dieses Muster ist unter denselben
Trigonometrieidentitaeten komplex-orthogonal. Der Kontext fordert, dass
der Raumzeitabschnitt die elektromagnetische Lorentzmatrix approximiert.
u ist aber dort die eigene Weltgeschwindigkeitsgroesse, nicht ungeprueft c.

Eine plausible eigene Minimalvariante EC-MATRIX-01 waere, die zwei
zusaetzlichen i-Faktoren im p21-Block zu entfernen. Das bringt ihn in das
komplex-orthogonale Muster und hat den spaeteren Block als Kontextstuetze.
Weder eine Autorenkorrektur noch eine Identitaet beider Matrizen wurde
gefunden. Denkbar sind auch Fehler der Winkelnotation statt der Matrix.
Keine Variante wird in die Quellen oder alten Rechner uebernommen.

Dieser Befund beantwortet insbesondere NICHT, warum pc als kinetische
Energie zu verwenden waere. Auch eine korrekt orthogonale Lorentzmatrix
waere allein keine Begruendung dieser Energiezuordnung.

## Nachpruefen

`scripts/audit_lorentz_meaning.py --check --verify-sources` rechnet den
Literalblock getrennt vom eigenen Standardboost; alles exakt als Brueche.
Reviews: `INVARIANCE_RATIONALE_SOURCE_REVIEW_2026-09-06.md` und
`LORENTZ_DIAGNOSTIC_MATH_REVIEW_2026-09-06.md` im Unterordner `reviews/`.
EDM1-Hash wie in `inputs`/Etappe4:49C79028C4F5B4FEE97F0541EF1655C37755C3C3C2FD3A10DD6E72CB454DE459.
