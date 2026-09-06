# Parameterbuch

Zweck: Alle Freiheitsgrade sichtbar machen. Dazu zaehlen nicht nur kontinuierliche Konstanten, sondern auch diskrete Labels, Zweigwahlen, Teilchenzuordnungen, Rundungsregeln und Korrekturen.

## Ergaenzung: isolierter Alpha-Audit 2026-09-06

Model Card: `alpha_audit/MODEL_CARD.md`; maschinenlesbare Profile:
`alpha_audit/inputs.json`. 1982 lokale eta-Indizes und vorhandene Indexvariante
sowie 1989-(q,k)-Quellenverweis und (k,q)-Gegenversuch bleiben getrennt.
Mathematisches pi und gedrucktes pi=3.1415926535 sind separate Profile.
CODATA-Alpha geht ausschliesslich in den nachfolgenden Vergleich ein.

Im Buch EDM2, Druckseiten 301-302 / PDF-Folios 307-308, wird Y3 als
Unsicherheitsfaktor in (105) eingefuehrt und fuer die anschliessende Rechnung
auf 1 gesetzt. Die zweite Etappe bestaetigt: Schon Druckseite 1 bezeichnet
Y_k als Platzhalter fuer nicht vollstaendig geklaerte Beziehungen und setzt
sie fuer die Tabellen auf 1. Eine theoretische Festlegung von Y3 wurde nicht
gefunden. Der erste Alpha-Audit bleibt bei Y3=1 und fitfrei.

Die getrennte Buchstruktur-Diagnose `scripts/audit_alpha_book.py` kehrt die
Gleichung nach Y3 um. Bei Wahl eines gemessenen Alpha ist das **ein**
kontinuierlicher Fitparameter, zuzueglich der offen dokumentierten diskreten
Indexvariante. Diese Diagnose aendert keine kanonischen historischen Inputs.
Kein einzelnes Y3 kann beide gedruckten Zweigwerte gleichzeitig treffen.
Details: `alpha_audit/EXTENSION_CANDIDATES.md`.

Etappe3: Buch(98) und Druck266 schliessen die lokale eta-Indexbruecke:
eta_qk mit erster Position q, zweiter k; eta_10=eta. Die IGW1982(V)-Variante
bleibt getrennt. Eine Gewichtung lambda variiert in der neuen Diagnose nur
probeweise die Energiemittelung von BandI(29): lambda=1/2 ist source-belegt;
die anderen vorab festgelegten Gewichte sind unsere ungefitten Gegenfaelle,
kein behaupteter weiterer Heim-Parameter. Energieordnungs-Korrekturvarianten
sind in `alpha_audit/BOOK_ENERGY_ORDER_ISSUE.md` gesondert ausgewiesen.

## Kontinuierliche Konstanten

Etappe4: `audit_energy_kinematics.py` hat keine angepassten Parameter.
Y3=1 ist die unveraenderte Quellenspezialisierung, nicht neu bestimmt.
Zwei diskrete diagnostische Aenderungen werden sichtbar getrennt: pc durch
T ersetzen; zusaetzlich h/(mc) durch h/p ersetzen. Fuenf feste beta-Lehrwerte
und der ungefitete kleine Buchzweig sind die Auswertungsstellen. Die
Gleichsetzung von m(v_H) mit gamma*m0 ist eine bedingte Quellenbruecke.
Diese Groessen sind keine neuen physikalisch gerechtfertigten Freiheitsgrade.

| Name | Wert | Einheit | Quelle | Modellversion | Status | Notiz |
|---|---:|---|---|---|---|---|
| alpha | TBD | dimensionslos | `Massenformel_nach_B_Heim_1982.pdf`, page image `1982_massenformel/page-04.png`, Feinstrukturkonstante block | 1982/IGW transcription | source_checked | Source gives `alpha_(+) = alpha` and printed `alpha_(+)^-1 = 137,03596147`; branch alias, not yet implementation value |
| gamma | 6.6732e-11 | N m^2 kg^-2 | `Massenformel_nach_B_Heim_1982.pdf`, page image `1982_massenformel/page-04.png`, label `(VI)` constants block | 1982/IGW transcription | source_checked | Newtonsche Gravitationskonstante; historical value, not modern CODATA |
| hbar | 1.0545887e-34 | J s | `Massenformel_nach_B_Heim_1982.pdf`, page image `1982_massenformel/page-04.png`, label `(VI)` constants block | 1982/IGW transcription | source_checked | Printed as `h = h/2pi`; use `hbar` in code to avoid ambiguity |
| c | 2.99792458e8 | m s^-1 | `Massenformel_nach_B_Heim_1982.pdf`, page image `1982_massenformel/page-04.png`, label `(VI)` constants block | 1982/IGW transcription | source_checked | Lichtgeschwindigkeit |
| epsilon0 | 8.8542e-12 | A s V^-1 m^-1 | `Massenformel_nach_B_Heim_1982.pdf`, page image `1982_massenformel/page-04.png`, label `(VI)` constants block | 1982/IGW transcription | source_checked | Influenzkonstante; listed in same block but not directly used by `HT-F-1982-MU` |
| mu0 | 1.2566e-6 | A^-1 s V m^-1 | `Massenformel_nach_B_Heim_1982.pdf`, page image `1982_massenformel/page-04.png`, label `(VI)` constants block | 1982/IGW transcription | source_checked | Induktionskonstante; listed in same block but not directly used by `HT-F-1982-MU` |
| R_vacuum | 376.73037659 | V A^-1 | `Massenformel_nach_B_Heim_1982.pdf`, page image `1982_massenformel/page-04.png`, label `(VI)` constants block | 1982/IGW transcription | source_checked | Printed as `R_ = (mu0/epsilon0)^(1/2)`; not directly used by `HT-F-1982-MU` |
| pi | 3.1415926535 | dimensionslos | `Massenformel_nach_B_Heim_1982.pdf`, page image `1982_massenformel/page-04.png`, constants block below `(VI)` | 1982/IGW transcription | source_checked | Printed value used by `HT-F-1982-MU`; distinguish from runtime library pi in implementation |
| s0 | 1 | m | `Massenformel_nach_B_Heim_1982.pdf`, page image `1982_massenformel/page-04.png`, formula `(VI)` | 1982/IGW transcription | source_checked | Eichfaktor in mass element formula |

## Diskrete Freiheitsgrade

| Name | Wertebereich | Quelle | Status | Notiz |
|---|---|---|---|---|
| k | 1, 2 | 1982-Formelskript | offen | Konfigurationszahl |
| P | ganzzahlig | 1982-Formelskript | offen | Doppelter Isospin |
| Q | ganzzahlig | 1982-Formelskript | offen | Doppelter Raumspin |
| kappa | 0, 1 | 1982-Formelskript | offen | Doublettziffer |
| x | Komponentenindex | 1982-Formelskript | offen | Teilchenkomponente im Multiplett |
| N | Resonanzordnung | 1982/1989 | offen | N=0 Grundzustand; N>0 kritisch wegen z(N)/Q(N) |

## Branch-/Korrekturentscheidungen

| Entscheidung | Optionen | Quelle | Modellversion | Status | Risiko |
|---|---|---|---|---|---|
| 1982 vs. 1989b Formel | 1982, 1989b | Heim/IGW/XLSM | TBD | offen | Vermischung von Original und spaeterer Korrektur |
| Modellversionierung der Massenformel | `model_1982_from_text`, `model_1989_extension` | `NORM-1989-MASS-VERSIONING` | 1982/1989 | entschieden | Keine unversionierte Massenformel verwenden |
| Konstantenprofil 1982 | `model_1982_igw2003_printed`, modern comparison profile | `NORM-1982-MU-HISTORICAL-CONSTANTS` | 1982/IGW transcription | entschieden | Historische und moderne Konstanten nicht mischen |
| Klammerkorrekturen 1989 | Original, IGW-Schaetzung | 1989-PDF Einleitung | TBD | offen | Ex-post-Anpassung |
| K_j Dezimalstellenregel 1982 | `,99...99 = 1`; sonst Dezimalstellen abschneiden, nicht aufrunden | `Massenformel_nach_B_Heim_1982.pdf`, page image `1982_massenformel/page-09.png`, Vermerk lines 431-435 | 1982/IGW transcription | source_checked | Diskrete Rundungs-/Abschneideregel fuer K4/K_j; nicht mit spaeteren Code-Kommentaren vermischen |
| Alpha-Zweigkuerzung 1982 | `alpha_(+) = alpha`; `alpha_(-) = beta ~= 137 alpha` | `Massenformel_nach_B_Heim_1982.pdf`, page image `1982_massenformel/page-04.png`, lines 141-147 | 1982/IGW transcription | source_checked | Source prints reciprocal numeric branch values; branch aliases nicht mit 1989/XLSM vermischen |
| Rundung `K > x.99` | verwenden, nicht verwenden | C/Pascal-Kommentar | TBD | offen | Kann einzelne Treffer stark beeinflussen |
| W/Z Branch | a, beta | Elementarstrukturen 2 Tabellenanhang | TBD | offen | Branchwahl kann Cherry Picking erzeugen |
