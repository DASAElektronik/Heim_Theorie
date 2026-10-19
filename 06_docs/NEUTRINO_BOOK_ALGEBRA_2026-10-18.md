# Buchinterne Neutrinoreduktion: ein Faktor zwei im pi-Anteil

2026-10-18, Einheit52. [Vertrag](../00_admin/NEUTRINO_BOOK_ALGEBRA_PLAN.md).
Ausgangspunkt ec86083. H004111/111a und118b passen für e und mu
zusammen. Für pi bleibt unter dem belegten Y=1-Profil eine positive
Differenz im nichtkonstanten Term. Das ist ein lokaler Formelbefund,
keine Aussage, die gesamte pi-Neutrinomasse sei doppelt so groß.

## Quellen und Abgrenzung

Erneut vollständig visuell gelesen: H004 Druck342/343 (PDF348/349),
352/353 (PDF358/359) und Einführung1 (PDF12). Vorhandene vollständige
Poppler-Seitenbilder; die Einführung belegt Y_k=1 für die Buchtabellen.
Die Formeln ohne Y auf342 liefern dieselbe hier geprüfte Einschränkung.
Quellendatei und SHA256 unverändert wie im [Buchbericht51](NEUTRINO_BOOK_2026-10-18.md).
Keine OCR-Ziffer als alleiniger Nachweis, kein Original verändert.

Die auf352 erklärte Notation `kP(0|Q kappa; C 0)` ergibt:

| Buchlabel | k | P | Q | kappa | q |
|---|---:|---:|---:|---:|---:|
| nu_e | 1 | 1 | 1 | 0 | 0 |
| nu_mu | 1 | 1 | 1 | 1 | 0 |
| nu_pi | 1 | 2 | 0 | 0 | 0 |

Insbesondere ist die12 vor der pi-Matrix k=1,P=2; kein vertauschtes Q.
Die Zustände und die Bezeichnungen gehören zum Buch. H007/B65,
C-Portlabels und moderne Flavourgrößen werden hier nicht eingesetzt.

## Direkte Einsetzung

111 lautet in unserer ASCII-Transkription:

```text
phi = A_v*F1*Fq*Fkappa/F2 + B_v*(P+Q) + 4*q*alpha_minus/alpha_plus
```

Für k=1,q=0 reduzieren sich die Faktoren aus111a auf:

```text
F1 = P*(P+Q)*(-1)^(P+Q)
F2 = 1 + 4*xi*choose(P,2)*Y41
Fq = 2*(3-alpha)*sqrt(eta11)
Fkappa = 1 + 2*kappa*xi/(3*eta^2)
                  *[1+pi^2*xi^2*(P-Q)]*Y43
```

Bei Fq kürzt sich sqrt(eta_qk); Y42 multipliziert nur den verschwindenden
Term q*eta²*(k−1), nicht die gesamte Klammer. Bei e/pi ist kappa=0;
bei mu ist P−Q=0. Der weitere Faktor in Fkappa fällt deshalb bei allen
drei Zuständen aus. B_v bleibt in beiden Formeln dieselbe Konstante,
einschließlich eines gemeinsamen Y44. Für Y41=Y43=1 folgt:

| Zustand | Aus111 | Gedrucktes118b |
|---|---|---|
| e | `4*A_v*(3-alpha)*sqrt(eta11)+2*B_v` | identisch |
| mu | `4*A_v*(1+2*xi/(3*eta^2))*(3-alpha)*sqrt(eta11)+2*B_v` | identisch |
| pi | `8*A_v*(3-alpha)*sqrt(eta11)/(1+4*xi)+2*B_v` | gleicher Ausdruck mit4 statt8 |

Die8 entsteht transparent aus F1=2*(2+0)=4 und dem Faktor2 in Fq.
118b druckt an dieser Stelle eindeutig4. Es gibt auf352/353 keine
zusätzliche Halbierungsoperation für diesen Zustand.

Setzen wir nur zur übersichtlichen Darstellung
`C=4*A_v*(3-alpha)*sqrt(eta11)`, so gilt:

```text
phi_pi(111)  = 2*C/(1+4*xi) + 2*B_v
phi_pi(118b) =   C/(1+4*xi) + 2*B_v
Differenz   =   C/(1+4*xi)
```

Bei A_v>0, eta11>0, xi>0 und0<alpha<3 ist die Differenz positiv.
Für B_v>0 liegt das Verhältnis der gesamten Ausdrücke strikt zwischen1
und2. Die gemeinsame positive Massenskala mu*alpha_plus aus118a
ändert diesen Verhältnisbefund nicht, muss aber für eine absolute
Massendifferenz bekannt sein.

## Exakte Kontrollen und Grenzen

Der [Rechner](../scripts/audit_neutrino_book_algebra.py) verwendet
rationale synthetische Eingaben, keine historischen Konstanten oder
angepassten Massenziele. Die
[Ergebnisse](../05_analysis/neutrino_book_algebra_results.json)
halten beide Formeln getrennt. Mit den ausdrücklich synthetischen
Werten A=3,B=5,alpha=1/100,sqrt(eta11)=2,xi=1/2,eta²=4
beträgt die Differenz598/25. Das ist keine Größe in eV.

Vier Tests prüfen e/mu als Kontrollen, die Unabhängigkeit der Differenz
von B, die nennerfreie Relation zum e-Zustand und die Eingabedomain.
Wiederholung: `py -3.13 scripts/audit_neutrino_book_algebra.py --check`.
FIND-058 erfasst den lokalen Widerspruch unter dem genannten Profil.

Nicht entschieden: welche Druckstelle zu korrigieren wäre, welche
Formel die historische Tabelle tatsächlich erzeugte, eine korrigierte
Masse, alle Buchausgaben oder ein empirisches Gesamturteil. Ein anderer
Y41-Wert könnte den pi-Ausdruck verändern, wäre aber ein anderer
Vertrag als die hier explizit geprüfte Einsannahme. Keine Suche nach
einem passenden Y oder nach einer passenden Skala.

Der nächste sinnvolle Schritt ist eine skalenfreie Prüfung der
Tabellenrelationen gegen die festgelegten Hilfsgrößen, soweit diese
ohne den offenen historischen Eingabevertrag tragfähig sind.
