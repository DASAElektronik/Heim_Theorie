# H006 x3/mu−: unabhaengige masselose Auswahlrechnung

2026-09-06, Etappe 26, Vertrag aus MUON_SELECTION_PLAN nach Checkpoint d960144.
Nur eigene Standardbibliotheksrechnung; keine bestehenden Audit-Evaluatoren
oder historischen Programme importiert/ausgefuehrt, keine Massenauswertung.

## Vertrag und Quellenlesung

Gelesen wurden Plan, n0_electron_inputs, bestehende H006-Alpha-/WVX-Eintraege,
A-Matrix-Slash-Entscheidung sowie audit_alpha und audit_n0_electron als
Formel-/Profilvergleich, nicht als ausfuehrbare Rechenbausteine.
Quellenlesung von Root/Quellenagenten uebernommen, keine eigene PDF-Pruefung:
epsilon=+1,k=P=Q=kappa=1,C=0,N=0; x=0 und x=1 liefern qx=-1,q=1.
Die Ladungsliste zieht beide Eintraege zusammen. Nach diesem Vertrag hat
die betrachtete W-Formel keinen weiteren x-Eingang; beide Auswertungen sind
identisch. Das klaert nicht von selbst die physikalische Multiplizitaet.

Es gelten d=eta11, w1=d*A16, w2=A26+d^2*A31 und w=1+d*A16, W=g*w.
Unindiziertes eta in A16/A26 ist NICHT d. w2 ist definiert und positiv,
auch wenn sein nullter Exponent keinen variablen Beitrag zu w liefert.
Nenner weggefallener Terme werden vor der Nullfaktorkuerzung geprueft.
Die Kette verwendet N0/(XV)/(XXVI)/Restalgorithmus, nicht H006s abweichendes XIV.

Zwoelf vorab benannte Kombinationen, keine Auswahl nach kleinstem Rest:

- M: mathematische pi/e, xi=1.61803399; G: mathematische pi/e und
  xi=(1+sqrt(5))/2; D: gedruckte pi/e/xi wie im alten Eingabevertrag.
- A16-P: Nennerprodukt 5*eta (Default); A16-L: linkassoziativ /5*eta.
- Wurzel I: sqrt(xi*d) (alter Default); O: sqrt(xi)*d.

Nacktes alpha stammt ausschliesslich aus dem kleinen Zweig des alten
1982_source_literal-Profils mit eta12=(k=1,q=2), nicht aus einer Messzahl.
Mathematische exp/ln bleiben auch bei gedrucktem e-Eingang unveraendert.
H004-/H010-alpha3, Massenkonstanten, Sollmassen und neue Fits fehlen bewusst.

## Eigener reproduzierbarer Rechenweg

Machin-pi ersetzt die Gauss-Legendre-Iteration des bestehenden Rechners.
Die eta-Werte werden als normierte inverse Viertelwurzeln berechnet.
Die Iteration z=rhs^2/(1-z), gestartet bei rhs^2, liefert den kleinen
Alpha-Quadratwert; keine direkte Uebernahme von solve_branches.
Der reduzierte alpha3-Ausdruck und A26 sind algebraisch umgeschrieben.
In A31/A36 wird 1-beta^2=alpha^2 aus derselben Zweiggleichung verwendet.
Ganzzahlen K1..3 folgen aus ganzzahligen Potenzvergleichen, nicht aus
gerundeten Wurzeln. Es gibt keine Epsilon-Promotion fuer K4.

```python
from decimal import Decimal as D, localcontext
from itertools import product


def atan_reciprocal(q):
    t = D(1) / q
    square = t * t
    term = total = t
    for j in range(1, 20000):
        term *= -square
        updated = total + term / (2 * j + 1)
        if updated == total:
            return total
        total = updated
    raise ArithmeticError("Machin series did not stabilize")


def evaluate(precision, profile, a16_binding, root_scope):
    with localcontext() as ctx:
        ctx.prec = precision
        one = D(1)
        pi = 16 * atan_reciprocal(D(5)) - 4 * atan_reciprocal(D(239))
        eb, xi = one.exp(), D("1.61803399")
        if profile == "G":
            xi = (one + D(5).sqrt()) / 2
        elif profile == "D":
            pi, eb = D("3.1415926535"), D("2.71828183")
        assert profile in ("M", "G", "D")
        assert a16_binding in ("P", "L") and root_scope in ("I", "O")
        eta, d, eta12 = [one / (one + D(v) / pi**4).sqrt().sqrt()
                         for v in (4, 5, 80)]
        se, s, u = eta.sqrt(), d.sqrt(), eta12.sqrt()
        corr1, corr2 = s * (1-s) / (1+s), u * (1-u) / (1+u)
        rhs = 9 * (5*eta + 2*se + 1) * (1-corr1*corr2) / (32*pi**5)
        assert 0 < rhs < D("0.01")
        z = rhs**2
        for iteration in range(200):
            updated = rhs**2 / (1-z)
            if updated == z:
                break
            z = updated
        else:
            raise ArithmeticError("Small alpha root did not stabilize")
        alpha, beta = z.sqrt(), (1-z).sqrt()
        root = (xi*d).sqrt() if root_scope == "I" else xi.sqrt()*d
        a1, a2 = (1+s)/2, 1/d
        a3 = 1-alpha*xi**3*(1+s)**3/(3*d**3)-2*root/eb*((1-s)/(1+s))**2
        small = alpha*(1+6*alpha/pi)/5
        a16 = (pi*eb)**2*(1+(small/eta if a16_binding == "P" else small*eta))
        a26 = 2/(eb*xi**2)-pi*eb*alpha**2*se
        squared = (pi*eb*alpha)**2
        a31 = squared*(1-squared)
        a24 = 2*xi**2/(3*eta)
        domains = {
            "A36_den": 1-pi*eb*(xi*eb)**2*alpha**2,
            "XVI_alt_A24_den": 1-a24,
            "XVIII_A24_den": one,
            "three_minus_q": D(2), "eight_minus_A66_power": D(7),
            "A41_den": 2*beta-alpha, "b_den": 3+eta,
        }
        assert all(v.is_finite() and v != 0 for v in domains.values())
        assert all(v.is_finite() and v > 0
                   for v in (pi, eb, xi, eta, d, eta12, alpha, beta, a1, a2, a3))
        w1, w2 = d*a16, a26+d*d*a31
        assert w1 > 0 and w2 > 0 and 1+w2 > 0
        w = 1+w1
        g = 27*a1+9*a2+2*a3+(-one/3).exp()
        target = g*w
        values = dict(pi=pi, e_base=eb, xi=xi, eta=eta, d=d, eta12=eta12,
                      rhs=rhs, alpha=alpha, beta=beta, a1=a1, a2=a2, a3=a3,
                      A16=a16, A26=a26, A31=a31, A24=a24,
                      w1=w1, w2=w2, w=w, g=g, W=target, **domains)
        remainder, integers = target, []
        for index, (coeff, power) in enumerate(((a1, 3), (a2, 2), (a3, 1)), 1):
            integer = 0
            while coeff*(integer+1)**power <= remainder:
                integer += 1
                if integer > 10000:
                    raise ArithmeticError("Outside the bounded candidate")
            upper = coeff*(integer+1)**power-remainder
            remainder -= coeff*integer**power
            assert remainder >= 0 and upper > 0
            values[f"greedy_lower_{index}"] = remainder
            values[f"greedy_upper_{index}"] = upper
            integers.append(integer)
        assert 0 < remainder <= 1  # Observed case, not a universal source rule.
        raw = -3*remainder.ln()
        fourth = int(raw//1)       # Nonnegative floor, no decimal promotion.
        integers.append(fourth)
        k1, k2, k3, k4 = integers
        xiii_pairs = ((a3*k3, D(k4)), (a2*k2**2, a3*k3), (a3*k1**3, a2*k2**2))
        xxxii_pairs = ((a3*k3, D(k4)), (2*a2*k2**2, a3*k3*(1+k3)),
                       (6*a1*k1**3, a2*k2*(2*k2**2+3*k2+1)))
        for name, pairs in (("XIII", xiii_pairs), ("XXXII", xxxii_pairs)):
            for index, (right, left) in enumerate(pairs, 1):
                gap = right-left
                values[f"{name}_gap_{index}"] = gap
                values[f"{name}_relative_gap_{index}"] = gap/max(one, abs(left), abs(right))
        values.update(W4=remainder, K4_raw=raw,
                      K4_floor_lower_gap=raw-k4, K4_floor_upper_gap=k4+1-raw,
                      K4_raw_cap_gap=a3*k3-raw,
                      raw_equation_error=(-raw/3).exp()-remainder,
                      floor_equation_error=(-D(k4)/3).exp()-remainder,
                      alpha_equation_error=alpha*beta-rhs)
        assert all(values[f"{name}_gap_{index}"] > 0
                   for name in ("XIII", "XXXII") for index in (1, 2, 3))
        assert values["K4_floor_lower_gap"] > 0 and values["K4_floor_upper_gap"] > 0
        assert 0 < values["floor_equation_error"] < 1-(-one/3).exp()
        return values, tuple(integers), tuple(j-q for j, q in zip(integers, (3, 3, 2, 1)))


cases = list(product(("M", "G", "D"), ("P", "L"), ("I", "O")))
runs = {case: {p: evaluate(p, *case) for p in (120, 160)} for case in cases}
error_fields = ("raw_equation_error", "alpha_equation_error")
with localcontext() as ctx:
    ctx.prec = 180
    max_absolute = max_relative = D(0)
    for case in cases:
        low, low_k, low_n = runs[case][120]
        high, high_k, high_n = runs[case][160]
        assert low_k == high_k and low_n == high_n
        for field in low:
            difference = abs(low[field]-high[field])
            max_absolute = max(max_absolute, difference)
            if field not in error_fields and high[field] != 0:
                max_relative = max(max_relative, difference/abs(high[field]))
        print("/".join(case), "K", high_k, "n", high_n,
              *[f"{key}={high[key]:.20g}" for key in
                ("W", "W4", "K4_raw", "floor_equation_error")])
    assert max_absolute < D("1e-110") and max_relative < D("1e-110")
    print("fields_per_cell", len(runs[cases[0]][120][0]))
    print("max_absolute_120_160", max_absolute)
    print("max_relative_nonzero_120_160", max_relative)
    print("max_raw_equation_error_120",
          max(abs(runs[case][120][0]["raw_equation_error"]) for case in cases))
    for label, fields in (
        ("greedy_upper", [f"greedy_upper_{i}" for i in (1, 2, 3)]),
        ("K4_integer_distance", ["K4_floor_lower_gap", "K4_floor_upper_gap"]),
        ("zone_absolute_gap", [f"{name}_gap_{i}" for name in ("XIII", "XXXII") for i in (1, 2, 3)]),
        ("zone_relative_gap", [f"{name}_relative_gap_{i}" for name in ("XIII", "XXXII") for i in (1, 2, 3)]),
    ):
        print("minimum_"+label, min(runs[case][160][0][field] for case in cases for field in fields))
    default = runs[("M", "P", "I")][160][0]
    print("DEFAULT_FIELDS")
    for field, value in default.items():
        print(field, format(value, ".26g"))
```

## Ergebnis und Reichweite

Der eigene Codeblock wurde mit py -3.13 -B aus dieser Review ausgefuehrt;
Exitcode 0. Er liefert in allen Kombinationen K1..3=(14,9,3).
A16-P fuehrt zu K4=0 und n=(11,6,1,-1); A16-L zu K4=1 und n=(11,6,1,0).
Beide Ausgangsindizes besitzen unter dem uebernommenen Vertrag dieselben
reduzierten Eingaben. Die verschiedenen Wurzelweiten und Zahlenprofile
veraendern diese jeweilige Ganzzahlentscheidung nicht. Aus der 160-stelligen
Auswertung, hier gerundet (R bezeichnet nur exp(-K4/3)-W4):

| Profil/A16/Wurzel | W4 | K4_raw | K4 | R nach floor |
| --- | ---: | ---: | ---: | ---: |
| M/P/I | 0.7755039220886995 | 0.7627267166448646 | 0 | 0.2244960779113005 |
| M/P/O | 0.7755120560046683 | 0.7626952511432173 | 0 | 0.2244879439953317 |
| M/L/I | 0.6927848240193449 | 1.1011074817730742 | 1 | 0.0237464865544443 |
| M/L/O | 0.6927929576918099 | 1.1010722603402288 | 1 | 0.0237383528819793 |
| G/P/I | 0.7755039502393991 | 0.7627266077452254 | 0 | 0.2244960497606009 |
| G/P/O | 0.7755120841553648 | 0.7626951422447325 | 0 | 0.2244879158446352 |
| G/L/I | 0.6927848521692018 | 1.1011073598743750 | 1 | 0.0237464584045875 |
| G/L/O | 0.6927929858416636 | 1.1010721384429744 | 1 | 0.0237383247321256 |
| D/P/I | 0.7755069136887019 | 0.7627151438050104 | 0 | 0.2244930863112981 |
| D/P/O | 0.7755150476046777 | 0.7626836784247173 | 0 | 0.2244849523953223 |
| D/L/I | 0.6927878155092382 | 1.1010945276060766 | 1 | 0.0237434950645511 |
| D/L/O | 0.6927959491817101 | 1.1010593063252882 | 1 | 0.0237353613920791 |

Im alten Default M/P/I sind A16=73.03605945222875288,
w1=72.12778214819897153, w2=0.28435454552308406,
g=38.57608235880488516 und W=2820.98334686566515376.
Die reellen Auswahlreste sind W2=85.54114046777116622,
W3=3.52113875088419632 und das tabellierte W4.
Die drei oberen Greedy-Abstaende betragen 543.4909412512781,
15.71812091110164 und 0.1397076875097995.

Die Default-XIII-Abstaende (rechte minus linke Seite) sind
(2.74563482879550,79.27436688809147,2429.32065502139415),
die XXXII-Abstaende
(2.74563482879550,153.05746411859195,14681.11986880863901).
XIII verwendet rechts weiterhin alpha3, nicht eine still ersetzte alpha1.
Der A36-Nenner ist 0.99120459856817606, der XVIII-A24-Nenner exakt 1;
auch die getrennte alternative XVI-Lesung 1-A24=-0.76300430149185797
ist nicht singulaer. Alle weiteren im Code geprueften Nenner sind definiert.

Alle Faelle liegen im Zweig 0<W4<1; das reelle K4 ist nicht ganzzahlig.
Nach floor verbleibt ein positiver Fehler exp(-K4/3)-W4. Er ist ein
dimensionsloser Rest dieser Gleichung, kein Massenfehler. Die kleinere
Abweichung der linkassoziativen Lesart ist kein Auswahl- oder Editionsbeweis.
Die XIII-/XXXII-Abstaende sind strikt positiv; negative Besetzung n4=-Q4
ist erlaubt und darf nicht durch ein kuenstliches n4>=0-Verbot beseitigt werden.
Keine durch diesen Vergleich festgestellte Gleichheit fordert eine
Zonenuebertragung. Eine allgemeine Uebergangsdynamik ist damit nicht validiert.

Praezisionsvergleich: 54 numerische Felder je Zelle, insgesamt 648
Vergleiche bei 120 gegen 160 Stellen; alle K-/n-Tupel unveraendert.
Maximaler absoluter Unterschied <1.703e-115; maximaler relativer Unterschied
der Nichtnullfelder ohne reine Rechenresiduen <1.685e-114.
Der reelle Restgleichungsfehler betraegt bei 120 Stellen hoechstens 1e-120.
Beobachtete Minima ueber alle Zellen, gerundet:
Greedy-Oberabstand 0.1396966187605726; K4-Abstand zur naechsten
Ganzzahlgrenze 0.1010593063252882; XIII-/XXXII-Abstand 1.7456348287585773.
Mit Normierung durch max(1, Betrag linker Seite, Betrag rechter Seite)
liegt der kleinste Strukturabstand bei 0.6357855059508609.
Es wurde also weder eine nahe Ganzzahlentscheidung noch eine nahe
Gleichheit der geprueften Strukturbedingungen beobachtet.

Decimal-Stabilitaet ist weder gerichtete Intervallarithmetik
noch eine physikalische Unsicherheitsabschaetzung. Die Aussage bleibt von
Quellenzuordnung, N0-Teilpfad, Alpha-Profil und den expliziten Lesarten abhaengig;
keine bestaetigte Myonmasse, keine neue H006-Gesamtfassung und kein Fit.
