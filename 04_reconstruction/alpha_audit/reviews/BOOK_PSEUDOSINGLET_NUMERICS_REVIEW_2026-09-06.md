# Buch-Pseudosingulett: unabhaengige Numerik des fixierten Vertrags

2026-09-06, Etappe 30. Numerischer Anschluss zum separaten
`BOOK_PSEUDOSINGLET_STRUCTURE_REVIEW_2026-09-06.md`.
Vertragsbasis vor Auswertung: Commit `05a0bab`,
`04_reconstruction/alpha_audit/NORM-BOOK-PSEUDOSINGLET.md` und
`book_pseudosinglet_inputs.json`, beide vollstaendig gelesen.
Es werden genau deren zwei Profile und keine weiteren Varianten gerechnet.

## 1. Feste Annahmen und unabhaengige Methode

H004, Buchausgabe1996, ist die einzige Formelquelle des Vertrags. Y3=Y9=1,
k=P=Q=kappa=q=1, epsilon=1,C=0,qx=-1,N=0 und f(0)=0 bleiben fest.
Q=(3,3,2,1); N ist nicht einer der vier Werte N_(j), n_j=N_(j)-Q_j.
Mathematisches pi/e und xi=(1+sqrt(5))/2, keine H006-Dezimalprofile.
Die empirische Autorenidentifikation des Musters ist vorausgesetzt, nicht
durch diese Rechnung abgeleitet. Kein Y9-Fit, keine Masse, kein F_S.

Der folgende Code importiert keinen Root-Rechner und keine Testhelfer.
Er kodiert die beiden vorab festgelegten Profile selbstenthalten:
`book_eq105_y3_1` und `book_printed_alpha_sensitivity` mit alpha exakt
0.007297354572 als eigener Druckwert-Sensitivitaetseingabe.
Der zweite Wert wird nicht zugleich als exakte Loesung von (105) ausgegeben.

pi entsteht aus der Machin-Identitaet 16*atan(1/5)-4*atan(1/239) und
alternierenden Reihen. Eta wird als Kehrwert zweier Quadratwurzeln von
1+(4+k)/pi^4 berechnet. Der kleine Alpha-Zweig wird durch die Iteration
a_(i+1)=R/sqrt(1-a_i^2), a_0=R, gewonnen, nicht durch einen importierten
quadratischen Zweigloeser. Fuer 0<R<1/2 ist die kleine positive Loesung
der monotone Grenzwert in (0,1/sqrt(2)); das grenzt den Zweig algebraisch ab.
Decimal-ln/exp/sqrt werden aus der Standardbibliothek benutzt.

Beide Rechnungen verwenden 120 bzw. 160 Ausgabestellen, jeweils 20 interne
Schutzstellen. Uebereinstimmende Ergebnisse sind eine unabhaengige
Praezisionskontrolle, keine gerichtete Intervallzertifizierung. Insbesondere
sind numerische Abstaende keine physikalischen Fehler- oder Y-Intervalle.
Sonderzweige ausserhalb des vertraglich freigegebenen gewoehnlichen TRC-
Zweigs werden gemeldet und nicht durch eigene Saettigung/Transfers ersetzt.

## 2. Selbstenthaltener ausfuehrbarer Rechenblock

```python
from decimal import Decimal as D, localcontext, ROUND_FLOOR
from fractions import Fraction as F

PROFILES = ('book_eq105_y3_1', 'book_printed_alpha_sensitivity')

def machin_pi():
    def atan_reciprocal(n):
        x = D(1)/n
        term = total = x
        j = 1
        while True:
            term *= -x*x
            new = total+term/(2*j+1)
            if new == total:
                return new
            total = new
            j += 1
    return 16*atan_reciprocal(5)-4*atan_reciprocal(239)

def small_alpha(rhs, precision):
    assert 0 < rhs < D('0.5')
    value = rhs
    for _ in range(4*precision):
        new = rhs/(1-value*value).sqrt()
        if new == value:
            assert 0 < new < 1/D(2).sqrt()
            return new
        value = new
    raise ArithmeticError('small-branch iteration did not stagnate')

def greedy(value, coefficient, power):
    assert value >= 0 and coefficient > 0
    n = 0
    while coefficient*(n+1)**power <= value:
        n += 1
    remainder = value-coefficient*n**power
    upper_gap = coefficient*(n+1)**power-value
    assert remainder >= 0 and upper_gap > 0
    return n, remainder, upper_gap

def evaluate(profile, precision):
    assert profile in PROFILES
    with localcontext() as ctx:
        ctx.prec = precision+20
        pi, e, xi = machin_pi(), D(1).exp(), (1+D(5).sqrt())/2
        eta, d, t = (1/(1+D(4+j)/pi**4).sqrt().sqrt() for j in (0, 1, 2))
        assert 0 < t < d < eta < 1
        sd, st, se = d.sqrt(), t.sqrt(), eta.sqrt()
        a1corr = sd*(1-sd)/(1+sd)
        a2corr = st*(1-st)/(1+st)
        vartheta = 5*eta+2*se+1
        rhs = 9*vartheta*(1-a1corr*a2corr)/(32*pi**5)
        alpha = (small_alpha(rhs, ctx.prec) if profile == PROFILES[0]
                 else D('0.007297354572'))
        assert 0 < alpha < 1/D(2).sqrt()
        ac1, ac2 = (1+sd)/2, 1/d
        h_corr = alpha*(1+sd)*xi**3/(3*d**3)
        g_corr = 2*xi*d/e*((1-sd)/(1+sd))**2
        ac3 = 1-h_corr-g_corr
        assert min(ac1, ac2, ac3) > 0
        a16 = (pi*e)**2*(1+alpha*(1+6*alpha/pi)/(5*eta))
        q = (3, 3, 2, 1)
        basis = ac1*q[0]**3+ac2*q[1]**2+ac3*q[2]+(-D(1)/3).exp()
        w = 1+d*a16
        w1 = basis*w
        assert a16 > 0 and basis > 0 and w1 > 0
        values = dict(pi=pi, e=e, xi=xi, eta=eta, eta11=d, eta12=t,
                      A1=a1corr, A2=a2corr, vartheta=vartheta,
                      correction_product=a1corr*a2corr, alpha_RHS=rhs,
                      alpha=alpha,
                      alpha_equation_residual=alpha*(1-alpha**2).sqrt()-rhs,
                      alpha1=ac1, alpha2=ac2, alpha3=ac3,
                      H_corr=h_corr, G_corr=g_corr, A16=a16,
                      g=basis, w=w, W1=w1)
        exact = dict(Q=q)
        numbers, residual = [], w1
        for index, (coefficient, power) in enumerate(((ac1, 3), (ac2, 2), (ac3, 1)), 1):
            n, residual, upper = greedy(residual, coefficient, power)
            numbers.append(n)
            values['W'+str(index+1)] = residual
            values['lower_gap_'+str(index)] = residual
            values['upper_gap_'+str(index)] = upper
        exact['N_first3'] = tuple(numbers)
        if not 0 < residual <= 1:
            status = 'unsupported_remainder_branch'
        else:
            raw = -3*residual.ln()
            cap = ac3*numbers[2]
            values.update(W5=raw, raw_cap=cap, raw_cap_gap=cap-raw)
            if not 0 <= raw <= cap:
                status = 'unsupported_raw_cap_branch'
            else:
                n4 = int(raw.to_integral_value(rounding=ROUND_FLOOR))
                numbers.append(n4)
                status = 'ordinary_TRC_only'
                exact['N'] = tuple(numbers)
                exact['n'] = tuple(n-offset for n, offset in zip(numbers, q, strict=True))
                n1, n2, n3, n4 = numbers
                zones = (F(n1*n1*(n1+1)**2, 4), F(n2*(n2+1)*(2*n2+1), 6),
                         F(n3*(n3+1), 2), F(n4))
                differences = (F(n1**3), F(n2**2), F(n3), F(1))
                beta = tuple(differences[j]-zones[j+1] for j in range(3))
                exact.update(G=zones, D=differences, B=beta,
                             active_107a=all(b >= 1 for b in beta),
                             order_107=all(differences[j] >= differences[j+1] for j in range(3)),
                             center_positive=differences[0] > 0)
                sigma = ac3*n3-n4
                floor_sigma = sigma.to_integral_value(rounding=ROUND_FLOOR)
                values.update(integer_gap_lower=raw-n4, integer_gap_upper=n4+1-raw,
                              remainder_108=(-D(n4)/3).exp()-residual,
                              beta4_sigma=sigma, beta4_sigma_gap_to_1=sigma-1,
                              beta4_sigma_minus_unweighted=sigma-D(beta[2].numerator)/beta[2].denominator,
                              beta4_difference_formula=(ac3-1)*n3,
                              sigma_nearest_integer_gap=min(sigma-floor_sigma, floor_sigma+1-sigma))
                exact['sigma_positive_numeric'] = sigma > 0
                exact['sigma_ge1_numeric'] = sigma >= 1
        # Round only for the declared comparison/output precision.
        ctx.prec = precision
        return ({key: +value for key, value in values.items()}, exact, status)

all_results = {}
for profile in PROFILES:
    low, low_exact, low_status = evaluate(profile, 120)
    high, high_exact, high_status = evaluate(profile, 160)
    assert low.keys() == high.keys() and low_exact == high_exact
    assert low_status == high_status
    with localcontext() as ctx:
        ctx.prec = 180
        absolute = {key: abs(low[key]-high[key]) for key in low}
        relative = {key: absolute[key]/abs(high[key]) for key in low
                    if high[key] != 0 and key != 'alpha_equation_residual'}
        max_abs_key = max(absolute, key=absolute.get)
        max_rel_key = max(relative, key=relative.get)
        assert absolute[max_abs_key] < D('1e-112')
        if profile == PROFILES[0]:
            assert abs(high['alpha_equation_residual']) < D('1e-170')
        print('\nPROFILE', profile, 'STATUS', high_status)
        print('decimal_fields', len(low), 'max_abs', max_abs_key, absolute[max_abs_key])
        print('max_relative', max_rel_key, relative[max_rel_key])
        print('exact', high_exact)
        for key in ('alpha', 'eta', 'eta11', 'eta12', 'alpha1', 'alpha2', 'alpha3',
                    'H_corr', 'G_corr', 'A16', 'g', 'w', 'W1', 'W2', 'W3', 'W4',
                    'W5', 'raw_cap_gap', 'integer_gap_lower', 'integer_gap_upper',
                    'remainder_108', 'beta4_sigma', 'beta4_sigma_minus_unweighted',
                    'sigma_nearest_integer_gap', 'alpha_equation_residual'):
            if key in high:
                print(key, format(high[key], '.45g'))
        all_results[profile] = (high, high_exact, high_status)
for profile, (values, exact, status) in all_results.items():
    with localcontext() as ctx:
        ctx.prec = 180
        assert status == 'ordinary_TRC_only' and exact['N'][1:3] == (9, 13)
        assert F(12*13, 2) == 78 < 81 < 91 == F(13*14, 2)
        needed_at_12 = values['W4']+values['alpha3']
        assert needed_at_12 > 1
        print('Fixed-N1/N2 required exp at N3=12:', profile,
              format(needed_at_12, '.45g'))
print('\nNo mass, no Y9 variation, no imported calculator.')
```

## 3. Ergebnis und Reichweite

Ausgefuehrt wurde der unveraenderte obige Block via `py -3.13 -B -`;
Exitcode 0. Ein zweiter Lauf mit zusaetzlicher Ausgabe der bereits berechneten
Greedy-Abstaende bestaetigte dieselben Resultate. Beide Profile erreichen
den vertraglich vorgesehenen gewoehnlichen TRC-Zweig, ohne Saettigung,
Transfer oder numerische Neuner-Promotion.

Gemeinsam, exakt als ausgegebene Integer/Fraction-Werte:

```text
Q       = (3,3,2,1)
N_(j)   = (14,9,13,7)
n_j     = (11,6,11,6)
G       = (11025,285,91,7)
D       = (2744,81,13,1)
(B2,B3,B4) = (2459,-10,6).
```

Die nachfolgende Tabelle zeigt gerundete Rechenausgaben, keine entsprechend
genauen physikalischen Vorhersagen oder Messwerte:

| Groesse | book_eq105_y3_1 | book_printed_alpha_sensitivity |
|---|---:|---:|
| alpha | 0.007297354597567135362767 | 0.007297354572 |
| alpha3 | 0.978658789856463953655877 | 0.978658789931195063915071 |
| A16 | 73.0360701176661706927356 | 73.0360701172789933461934 |
| W1 | 2830.26325766809626412716 | 2830.26325766422754316483 |
| W4=r | 0.0784852851812752849781085 | 0.0784852803410498892742070 |
| W5=-3 ln(r) | 7.63453236505429934238359 | 7.63453255006575214302350 |
| (108)-Rest links minus rechts | 0.0184866826831297778317981 | 0.0184866875233551735356997 |
| B4_sigma | 5.72256426813403139752640 | 5.72256426910553583089592 |
| B4_sigma-B4 | -0.277435731865968602473596 | -0.277435730894464169104080 |

Im primaeren Profil betragen die drei unteren Greedy-Abstaende gerundet
94.8210512702, 12.8010495533 und 0.07848528518; die oberen sind
534.211030449, 6.43821010867 und 0.900173504675. Beide Profile haben
minimalen Abstand zu einer Grenze der ersten drei Greedyschritte >0.0784.
Der Abstand des Logwertes zum naechsten Integer ist jeweils >0.3654,
der Abstand zur Rohwertkappe alpha3*N3 jeweils >5.0880. Das sind numerische
Abstandsangaben aus der erklaerten Praezisionskontrolle, keine Intervallbeweise.

Der normale Auswahlzweig ist somit von einer bestandenen Strukturpruefung
zu unterscheiden: Die Differenzreihenfolge (2744>=81>=13>=1) und das
Zentrumsgate bestehen. Aber die erste ungewichtete (107)-Reihe scheitert
an j=2 nach j=3 exakt: D2=81 ist nicht groesser als G3=91; B3=-10 ist
auch nicht der Kollapsrand B3=0. Dies ist fuer beide vorab fixierten Profile
ein lokaler nicht bestandener Gatecheck, kein Gegenbeispiel gegen jede
moegliche Quelleingabe oder Aussage ueber die Existenz des Myons.

Die separate (107b)-Groesse ist positiv und numerisch >1, anders als die
ganzzahlige ungewichtete B4=6. Die beiden Definitionen werden nicht gemischt.
Die Differenz ist (alpha3-1)*13. Bereits H_Korr>0 und G_Korr>0 implizieren
fuer diese positiven Eingaben alpha3<1 und damit ihr negatives Vorzeichen;
ihre Groesse ist oben numerisch ausgewiesen. Der Abstand zur naechsten
Ganzzahl liegt numerisch bei etwa 0.2774. Daraus wird kein allgemeines
Integerpruefverfahren fuer unbekannte reelle Quellenkoeffizienten gemacht.

Die positiven (108)-Reste stammen aus dem gewoehnlichen Abschneiden von W5
auf N4=7. Sie sind keine Massenresiduen und werden nicht durch Variation
von Y9, der N_j oder des Alpha-Eingangs minimiert. Insbesondere bleibt der
gescheiterte ungewichtete Gatecheck stehen; ein Kaskaden-/Kollaps- oder
anderer Reparaturalgorithmus wird weder angewendet noch als Autorwille angenommen.

## 4. Tatsaechlicher Umfang der Praezisionskontrolle

Verglichen wurden je Profil 42 benannte Decimal-Felder zwischen 120 und
160 Stellen, einschliesslich einiger wiederholter Rest-/Margenaliase;
das sind nicht 42 voneinander unabhaengige Aussagen. Dazu kommen exakt
gleiche Q/N/n-Tupel, Zonenwerte und Gateentscheidungen in beiden Laeufen.

- Groesster absoluter Abstand primaer: W1, 6.1970833968e-118.
- Groesster absoluter Abstand Druckwertprofil: W1, 1.7726909427e-117.
- Groesster relativer Abstand der verglichenen Nichtnullfelder beider
  Profile: correction_product, 4.11535193394e-120. Der Alpha-Gleichungsrest
  wird wegen seines Null-/Kleinstwertcharakters nicht relativ verglichen.
- Primaerer Alpha-Gleichungsrest in der 180-stelligen Arbeitsarithmetik:
  0E-182. Dies ist numerische Stagnation, keine Behauptung einer endlichen
  exakten Dezimaldarstellung der algebraischen Loesung.
- Druckwertprofil: alpha*sqrt(1-alpha^2)-Ralpha =
  -2.55650930894401754735050368449e-11. Der deklarierte Druckwert ist
  deshalb weiterhin nicht zugleich als exakte Loesung von (105) behandelt.

Keine neue externe Datenquelle und kein fremder Programmlauf. Diese eigene
Review ist ein unabhaengiger Rechenweg des vereinbarten lokalen Vertrags,
kein externes PeerReview. Die zuvor identifizierten Quellen-, TRC-,
Grenz- und Strukturanschlussfragen bleiben davon getrennt und offen.

## 5. Begrenzte Implementierungs- und Testgegenreview

`scripts/audit_book_pseudosinglet.py` und `tests/test_book_pseudosinglet.py`
vollstaendig gelesen. Keine materiellen Fehler in den zwei vertraglichen
Profilen gefunden: 105/Druckalpha bleiben getrennt, die Eta-Indizes,
98c-H/G-Terme, A16 mit 5*eta im Nenner, g/W, Direktrest und die beiden
getrennten Strukturdiagnosen stimmen mit der eigenen Implementierung ueberein.
Die wiederbenutzten Root-Helfer fuer pi/Zweige/Serialisierung sind nicht
die Grundlage des obigen unabhaengigen Rechenblocks.

Ausgefuehrt, jeweils erfolgreich:

```text
py -3.13 -B -m unittest discover -s tests -p test_book_pseudosinglet.py -v
  17 Tests bestanden.
py -3.13 -B scripts/audit_book_pseudosinglet.py --check --verify-sources
  H004-Hash und vorhandener Ergebnissnapshot bestaetigt.
```

Die Guards sperren geaenderte Eingabeprofile, Bool-/Typwechsel und ungueltige
Rechenbereiche am vorgesehenen build_report-Eingang. Dies ist eine gebundene
Diagnose, keine generische API fuer beliebige Zustaende oder TRC-Schwellen.
Die zunaechst benannte nicht blockierende Testluecke ist inzwischen geschlossen:
Root ergaenzte im bestehenden W-Pfadtest die ausmultiplizierte A16-Formel
und g=27*alpha1+9*alpha2+2*alpha3+exp(-1/3). Beide Ergaenzungen wurden
erneut gelesen und der isolierte Testsatz nochmals ausgefuehrt: weiterhin
17 Tests bestanden, Exitcode 0. Die Assertions sind algebraisch korrekt
fuer den unveraenderten Vertrag Y9=1. Alle vorhandenen Formel- und
Ergebnistests sind zutreffend begrenzt.

Root fuehrte zusaetzlich beide unabhaengigen Reviewbloecke erneut aus und
berichtete einen vollstaendigen Feldabgleich: 84 benannte Decimal-Felder
(zwei Profile) des Root-Rechners bei 120 Stellen gegen diese Review bei
160 Stellen, maximaler Absolutabstand 4.5725614163e-115; Q/N/n/G/D/B exakt
gleich. Dieser separat berichtete Kreuzvergleich ist von der oben selbst
ausgefuehrten internen 120/160-Kontrolle zu unterscheiden.

Der neue Test zum alleinigen Senken von N3 ist korrekt: Bei festem N2=9
fordert die ungewichtete erste (107)-Reihe G3(N3)<81. Da die Dreieckszahlen
monoton sind und G3(12)=78<81<G3(13)=91 gilt, ist N3<=12 notwendig.
Bei unveraendertem W3=13*alpha3+r und alpha3>0 waere fuer jeden solchen
N3 der benoetigte Exponentialwert mindestens r+alpha3. Der erneut ausgefuehrte
eigene Block ergibt 1.05714407503773923863 bzw. 1.05714407027224495319.
Beide sind numerisch >1, waehrend exp(-N4/3)<=1 fuer N4>=0 gilt.
Somit repariert eine Aenderung von N3 allein bei festem W3,N1,N2 nicht
gleichzeitig dieses Gate und die exakte Gleichung(108), auch wenn N4
frei nichtnegativ neu gewaehlt werden duerfte. Dies behauptet weder einen
neuen Loesungsalgorithmus noch Unmoeglichkeit bei anderen N1/N2/Eingaben.
Es bleibt eine lokale Folgerung mit der benannten numerischen >1-Praemisse,
keine nachtraegliche Anpassung oder neue Aussage ueber Teilchenexistenz.

Nur diese eigene Numerikreview wurde fuer den Nachtrag geaendert;
kein Root-Code, Test, Snapshot oder Eingabeprofil wurde bearbeitet.
