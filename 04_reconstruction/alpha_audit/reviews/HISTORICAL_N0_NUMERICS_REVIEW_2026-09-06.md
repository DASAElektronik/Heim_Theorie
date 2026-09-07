# HISTORICAL_N0_NUMERICS_REVIEW

Datum: 2026-09-06. Unabhaengige statische Mathematikreview, Etappe 17,
Ausgang 99a2efa. Autor: data_audit. Keine fremden Programme ausgefuehrt.

## 1. Ergebnis und Quellenumfang

Der H010-Elektronpfad besitzt dieselbe **bedingte exakte Nullbesetzung**
wie der eng freigegebene H006-Pfad: Wenn die ersten drei maximalen
Ganzzahlschritte K=(3,3,2) ergeben, ist der letzte Rest exp(-1/3), also
K4=1 und n4=0. Die historischen Portierungen ersetzen dieses analytische
Zertifikat jedoch durch einen numerischen Logarithmus mit Abschneiden
und kleinem Zuschlag. Damit ist die archivierte Rundungsdiagnose
mathematisch plausibel, aber noch keine bitgenaue Reproduktion eines
bestimmten historischen Laufs.

Gelesene H010-Dateien, statisch und ohne Kompilierung/Ausfuehrung:

- `01_sources/heim_primary_unpacked_untrusted/massformula/Pascal 0.62/GPROG 0.62c.PAS`
  (im Folgenden **PAS**).
- `01_sources/heim_primary_unpacked_untrusted/massformula/C 0.66/gprog_0.66.c`
  (**C**), zugehoerige README und Eingabedatei.
- Pascal-README (**README-P**) und
  `comparison GPROGOUT Fortran - Pascal 0.62.txt` (**OUT-P**).
- Kopf der C-Datei `output_plus_neutrino.txt` (**OUT-C**).

H006-Bezug: vorhandene Vollseitenreview
`N0_INPUT_CONTRACT_REVIEW_2026-09-06.md`, Abschnitte 3--7, und
`NORM-N0-ELECTRON-AUDIT.md`. Hier keine erneute PDF-Glyphenpruefung.
Insbesondere wird der Konflikt H006 (XIV) gegen (XV)/(XXVI) nicht
stillschweigend durch H010 geheilt. Die Aussage zu H006 benutzt
ausschliesslich dessen schon offengelegten (XV)/(XXVI)/p9-Pfad.

Kein neues Konstanteninventar und kein allgemeiner GMASS-Formelvergleich:
diese getrennten Reviews duerfen durch den gemeinsamen Auswahlpfad
nicht vorweggenommen werden.

## 2. Index und expliziter N=0-Pfad

PAS 677--701 und C 1198--1227 lesen/verwenden fuer das Elektronmultiplett
k=1, P=Q=1, kappa=0, epsilon=+1, C_s=0. Der Programmindex laeuft von
1 bis P+1, nicht von 0 bis P. In genau diesem Fall ist

    q_x = (P+2-2*x_program - 1)/2 = 1-x_program.

Programmx=2 ergibt q_x=-1 und q=abs(q_x)=1. Das ist H006 x=1 mit
q_x=-x_H006; die Bruecke lautet x_program=x_H006+1. Die Zahl 2 ist hier
ein Komponentenindex, nicht eine andere Anregungsstufe oder eine neue
Elektronkonfiguration. Das Multipletlabel x_2 ist davon nochmals getrennt.

Bei k=1 sind Q_j=(3,3,2,1), PAS 368--372 / C 788--793. Die Formeln
verwenden dabei verschiedene numerische Hilfsmittel (Pascal `round`,
C aktives `ROUND2`), stimmen an den exakten hier eingesetzten Werten
aber ueberein. Keine Behauptung zu beliebigen, ungenau gegebenen Indizes.

PAS 409--425 / C 834--860 waehlen den k=1-Zweig. Dort verschwindet
wg1 wegen 1-Q=0 und kappa=0, und wgxk=wg1+1=1, also W=g. Das `+1`
ist ein expliziter Zweig, nicht ein Aufruf eines allgemeinen 0^0-Auswerters.
PAS 722--724 / C 1248--1251 setzen anschliessend N=0 und rufen Auswahl
und Masse auf. Bei endlichen agx,bgx gilt f(0)=0. Auch der vorangestellte
Faktor 1-Q(2-k)(1-kappa) ist hier null; das ersetzt aber keine
Definitionsbereichskontrolle vor einem numerischen 0*ungueltig.

Wichtige Laufgrenze: GBASE berechnet weitere Anregerkoeffizienten trotz
N=0 (PAS 426--438 / C 862--880). Die algebraische Reduktion allein
beweist deshalb nicht, dass jedes fremde Binary bis zur Massenausgabe
laeuft. Quelldatei, ausgewaehlter Datensatz, Schalter, Compiler und
Gleitkommaformat sind fuer eine historische Laufzuordnung eigenstaendig.

## 3. Maximalitaet, W4 und Rundung

Mit den jeweils zur Formelversion gehoerenden positiven a1,a2,a3 und
u=exp(-1/3) steht in PAS 406 / C 831:

    g=27*a1+9*a2+2*a3+u.

Fuer W=g sind K1=3, K2=3, K3=2 genau dann die drei hier gemeinten
maximalen nichtnegativen Integer, wenn insbesondere

    64*a1-g > 0,
    7*a2-2*a3-u > 0,
    a3-u > 0

gelten. Die unteren Schranken folgen aus a1,a2,a3,u>0. Dann sind die
Restwerte W2=9*a2+2*a3+u, W3=2*a3+u und W4=u positiv. Die H006-Margen
wurden in Etappe 16 geprueft; fuer eine H010-Formelzelle muessen sie mit
deren eigenen a3/Konstanten neu geprueft werden. Gleiche Programmnamen
machen unterschiedliche Koeffizienten nicht identisch.

Im regulären Zweig 0<W4<=1 gilt fuer k=Q4=1 der reelle Rohwert

    L4(W4)=-3*ln(W4),   L4(exp(-1/3))=1,
    dL4/dW4=-3/W4.

Schreibt man den numerischen Rest als u*(1+epsilon), ist exakt

    L4=1-3*ln(1+epsilon),  epsilon>-1.

Ein kleiner positiver Restfehler ergibt damit L4<1 und kann beim
Abschneiden K4=0, n4=-1 statt K4=1, n4=0 erzeugen. Das ist eine
lokale Konditionierungs-/Entscheidungsdiagnose, keine Behauptung ueber
den tatsaechlichen Fehler jedes historischen Compilers.

| Stufe | Statisch aktive Regel | Reichweite |
|---|---|---|
| H006-Nullfall, eigene Etappe 16 | Exaktes Zertifikat -3*ln(exp(-1/3))=1 nach geprueften K1--3 | Kein allgemeiner toleranzbasierter Integerizer |
| PAS 465/471/475/482/483/488 | trunc(v+1e-10) | Derselbe positive Zuschlag auch ausserhalb des positiven Logarithmusfalls |
| C 63--70, 469--499 | myround(v)=trunc(v+sign_0(v)*1e-7), sign_0(v)=+1 fuer v>=0, sonst -1 | Aktive Makros ROUND **und** ROUND2; kein kaufmaennisches Runden |

README-P 14--20 beschreibt konkret das endliche Dezimalbeispiel
0.333333333333333*3<1 und die Ergaenzung von 1e-10. Das belegt die
Dokumentation der Portierung, nicht selbst den originalen DESY-Maschinenlauf.
Die C-README uebernimmt historischen Pascal-Changelogtext; die aktive
C-Funktion verwendet dagegen 1e-7. Kommentierte Fortran-Fragmente
(PAS 112--134 / C 502--525) sind keine dritte ausgefuehrte Referenz.

Die Zuschlaege sind nicht allgemein mathematisch gleichwertig mit der
maximalen Integerregel. Fuer v=m-delta/2<m kann trunc(v+delta)=m
ueber die exakte Schranke gehen und bei einer Restsubtraktion einen
negativen Rest erzeugen. PAS und C unterscheiden sich ausserdem fuer
negative v; schon PAS trunc(-1+1e-10)=0 gegen C myround(-1)=-1.
Dieses negative Beispiel liegt **nicht** auf dem hier behandelten
regulaeren Elektronpfad und ist keine neue Resonanzbehauptung.

PAS 482--491 / C 937--950 unterscheiden W4<=0 und W4>1; im zweiten
Fall wird auch K3 vermindert. Eine solche gekoppelte Korrektur darf
nicht nachtraeglich als reiner n4-Schritt etikettiert werden. Auf dem
exakten Nullfall 0<u<1 werden beide Sonderfaelle nicht betreten.
W4=1 selbst wuerde regulaer K4=0 und n4=-1 liefern; negative n4 sind
in H006 nicht pauschal verboten, sondern erfuellen n4>=-Q4.

## 4. Isolierter n4-Schritt und zulässige Gegenfaktoren

PAS 524 / C 998--1000 enthalten den Summanden 4*K4 in kgh. Phi/fig
(PAS 528--531 / C 1005--1008) enthaelt n1, aber kein n4. Bei festen
Q4, a_j, Phi, mu und alpha_mass_plus folgt daher exakt:

    M(n4=0)-M(n4=-1) = 4*mu*alpha_mass_plus.

Dies gilt auch fuer die schon gepruefte H006-Teilsummenformel. Im
historischen Ausdruck steht bei einer MeV-Ausgabe zusaetzlich dessen
Umrechnungsfaktor fakMeV (PAS 546); kg-Schritt und Ausgabeschritt sind
nicht numerisch ohne diese Konversion identisch. Es wird hier weder
ein moderner Referenzwert eingefuehrt noch eine historische Ausgabe
darauf angepasst.

Ein isoliertes Ersetzen n4=-1 durch 0 ist eine eigene algebraische
Intervention bei festgehaltenem Rest, kein unabhaengig bestaetigter
Zustandsuebergang. Es ist auch keine Empfehlung, n4 aufgrund einer
guenstigeren Masse zu waehlen. Fuer die echte Nullfallauswahl gilt das
Quellen-/Margen-/Identitaetszertifikat aus Abschnitt 3.

Fuer eine transparente Attribution eignen sich getrennte, vorher
festgelegte Achsen: dimensionale Konstanten c, nacktes Alpha a,
Formel-/Hilfskoeffizientenfassung f und Besetzungsschritt s. Reine
Zahlen (pi,e,xi), Umrechnung und abhängige Faktoren mu,alpha_mass+/-
muessen ebenfalls sichtbar einem Profil bzw. einer Achse zugeordnet
bleiben; abhaengige Faktoren werden nicht unbegruendet eingefroren.

Ein Vergleich M(c,a,f,s) erlaubt benannte Ein-Faktor-Differenzen und
eine exakt teleskopierende Gesamtbilanz entlang einer angegebenen
Reihenfolge. Die einzelnen Beitraege sind bei Wechselwirkungen aber
nicht eindeutig oder kausal. Schon der s-Schritt haengt vom Profil ab:

    Delta_s(c)=4*mu(c)*alpha_mass_plus(c),
    I_cs=4*(mu(c1)*alpha_mass_plus(c1)
           -mu(c0)*alpha_mass_plus(c0)).

Ein nichtnulliges I_cs macht die Zuordnung zu 'Konstanten' und
'Besetzung' reihenfolgeabhaengig. Eine vollstaendige kleine Faktortafel
kann diese Interaktionen zeigen; sie beseitigt sie nicht. Bei jedem
Formel-/Alphaprofil muessen zusaetzlich die Auswahlmargen kontrolliert
werden, bevor derselbe analytische n0-Auswahlpfad verwendet wird.

Unzulaessig waeren deshalb eine unqualifizierte Prozentursache des
historischen Fehlers, eine Auswahl der Profile anhand einer Sollmasse
oder die Behauptung, die n4-Diagnose erklaere bereits die ganze Differenz
zwischen H006, H010 und archivierten Ausgaben. Historische dimensionale
Konstanten sind selbst empirisch; korrekt ist 'keine neuen Massen- oder
Alphazielwerte zur Wahl', nicht 'ohne empirische Eingaben'.

## 5. Ausfuehrbare unabhaengige Kontrollen

Nur Standardbibliothek, keine Imports/Aufrufe der historischen Programme.
Die folgenden kuenstlichen Zahlen sind Grenz- und Algebrazeugen, keine
Teilchenparameter oder historische Laufrekonstruktion.

```python
from fractions import Fraction as F

pas=lambda v:int(v+F(1,10**10))
c=lambda v:int(v+(F(1,10**7) if v>=0 else -F(1,10**7)))
documented=F(333333333333333,10**15)*3
assert documented==1-F(1,10**15)
assert (int(documented),pas(documented),c(documented))==(0,1,1)
between=1-F(5,10**8)
assert (int(between),pas(between),c(between))==(0,0,1)
assert (pas(F(-1)),c(F(-1)))==(0,-1)  # not the electron W4 branch
below_three=3-F(1,2*10**10)
assert below_three<3 and pas(below_three)==3
for xp in (1,2):
    xh=xp-1
    assert F((1+2-2*xp)-1,2)==1-xp==-xh

# Synthetic mass polynomial: Phi and the other occupations are fixed.
mass=lambda mu,ap,rest,n4:mu*ap*(rest+4*(n4+1))
for mu in (F(2,7),F(5,11)):
    for ap in (F(3,17),F(7,19)):
        assert mass(mu,ap,F(23,5),0)-mass(mu,ap,F(23,5),-1)==4*mu*ap
m0,m1,ap,rest=F(2,7),F(5,11),F(3,17),F(23,5)
step=lambda m:mass(m,ap,rest,0)-mass(m,ap,rest,-1)
interaction=step(m1)-step(m0)
assert interaction==4*ap*(m1-m0)!=0
total=mass(m1,ap,rest,0)-mass(m0,ap,rest,-1)
path_cs=(mass(m1,ap,rest,-1)-mass(m0,ap,rest,-1))+step(m1)
path_sc=step(m0)+(mass(m1,ap,rest,0)-mass(m0,ap,rest,0))
assert total==path_cs==path_sc
print('Exact Fraction checks: indices, integer boundaries, mass step, interaction OK')
```

```python
from decimal import Decimal as D, localcontext

def diagnose(precision):
    with localcontext() as ctx:
        ctx.prec=precision
        u=(-D(1)/3).exp()
        eps=D('1e-30')
        direct=-3*(u*(1+eps)).ln()
        reduced=1-3*(1+eps).ln()
        assert 0<u<1 and direct<1
        assert abs(direct-reduced)<D(10)**(-precision+3)
        assert abs(-3*u.ln()-1)<D(10)**(-precision+3)
        return +u,+(-3/u),+reduced

v80,v120=diagnose(80),diagnose(120)
with localcontext() as ctx:
    ctx.prec=120
    assert max(abs(a-b) for a,b in zip(v80,v120))<D('1e-77')
for name,value in zip(('W4_exact_case','slope_dL4_dW4','L4_relative_perturbation_1e-30'),v120):
    print(name,format(value,'.45g'))
print('80/120-digit Decimal check OK; no historical binary execution')
```

Beide Bloecke am 2026-09-06 erfolgreich ausgefuehrt. Die drei
Decimal-Felder stimmen bei 80/120 Stellen absolut besser als 1e-77
ueberein; W4=0.716531310573789250425604096925379667453112060 und
dL4/dW4=-4.18683727525826858588437595880776051279371955 (jeweils
hier gerundet). `git diff --check` ohne Befund. Das prueft die angegebenen
eigenen Gleichungen und Grenzzeugen, nicht ein fremdes Rundungssystem.

## 6. Reproduktions- und Urteilsgrenze

OUT-P 4--6 unterscheidet selbst Fortran-Ausgaben und mit P bezeichnete
Pascal-Werte. OUT-C 4 nennt eine C-Version 0.62; die gelesene Quelldatei
ist Version 0.66. Beides sind Provenienzgrenzen fuer eine exakte
Zuordnung, nicht ein mathematischer Einwand gegen die Nullfallidentitaet.

Der statische Befund rechtfertigt eine eigene, deutlich beschriftete
Gegenrechnung der genannten Pfade. Er reproduziert weder eine alte
Binärdatei noch validiert er die Massenformel physikalisch. Insbesondere
bleiben GMASS-Version, Konstantenwahl, nacktes Alpha und Rundungsregel
getrennte Pruefobjekte. Eine spaetere eigene Implementierungsreview wird
nur nach Vorliegen des neuen Rechners angehaengt.

## 7. Unabhaengige 64+1-Zellen-Gegenrechnung

Nachtrag nach Vorlage von `NORM-HISTORICAL-N0-COMPARISON.md`,
`historical_n0_inputs.json`, `scripts/audit_historical_n0.py` und
`05_analysis/historical_n0_results.json`. Die vorab festgelegten sechs
Achsen werden uebernommen, aber nicht die neue Auswertungsfunktion.

Der Vertrag trennt die zwei alpha3-Formelwechsel, nacktes Alpha, xi,
hbar und gamma; die sechs Bits erzeugen 64 benannte Kombinationen.
Die zusaetzliche engere Wurzellesart sqrt(xi)*d bleibt eine 65. Rechnung
nur am unveraenderten Ausgangspunkt. Keine dieser gemischten Zellen
wird als historische Editionsfassung oder fitfreier Naturbeweis ausgegeben.
Die Radikandgrenze ist hier aus der separaten Quellenreview uebernommen,
nicht in dieser Mathematikreview neu visuell entschieden.

Die unabhaengige Rechnung unten verwendet:

- pi aus der Machin-Reihe, e aus der Fakultaetsreihe;
- ausschliesslich Newton-Verfahren fuer Wurzeln und fuer den kleinen
  positiven Alpha-Zweig a^4-a^2+K^2=0;
- eta(c)=(1+c/pi^4)^(-1/4), mit c=4,5,80; das letzte c bedeutet
  ausschliesslich die deklarierte H006-Indexlesart k=1,q=2;
- mu als positive zwoelfte Wurzel von
  pi^7*hbar^10/(9*gamma^2*c_speed^6*s0^8), algebraisch aus (VI);
- am=eta*(ap+1)-1 und die reduzierte Massensumme
  M=mu*[ap*G+(ap-am)*L+4*am] statt mu*ap*(G+Phi).

Damit sind insbesondere die zwei durch Kompensationen empfindlichen
Stellen Alpha-Zweig und mu anders ausgewertet. Die historische
Umrechnung wird erst nach dem kg-Ergebnis multipliziert. Die gespeicherte
Ausgabemasse wird nur im abschliessenden Vergleichsteil benutzt.

Der Code kontrolliert in allen 65 Zellen die positiven Greedy-Margen,
die drei XIII- und die drei XXXII-Margen, beide A36-Nenner und ap>am>0.
Die dritte XXXII-Marge ist korrekt 162*a1-84*a2. K4 bleibt ein exaktes
Zertifikat, kein numerisch abgerundeter Wert. Numerisch gespeichert werden
je Zelle 21 vergleichbare Felder; eigene zusaetzliche Strukturmargen
muessen positiv sein, sind aber nicht neue Felder des Root-Snapshots.

Ausfuehrung im Repository-Wurzelverzeichnis; keine Schreiboperation im
Code. Erst **nach** der unabhaengigen Rechnung wird der eigene neue
Projekt-Rechner fuer die API-Gegenpruefung importiert; keine historische
Pascal-/C-Datei wird importiert, kompiliert oder ausgefuehrt.

```python
import json
import sys
from decimal import Decimal as D, getcontext, localcontext
from pathlib import Path

ROOT=Path.cwd()
contract=json.loads((ROOT/'04_reconstruction/alpha_audit/historical_n0_inputs.json').read_text(encoding='utf-8'))
AXES=('a3_first_power','a3_root_factor','alpha_input','xi','hbar','gamma')
assert contract['axes_in_forward_order']==list(AXES)
assert contract['target_fitting'] is False

def nth(z,n):
    assert z>0 and n>=2
    x=D(10)**(z.adjusted()//n)
    for _ in range(2000):
        y=((n-1)*x+z/x**(n-1))/n
        if abs(y-x)<=abs(y)*D(10)**(-getcontext().prec+5):
            return y
        x=y
    raise ArithmeticError('Newton root did not converge')

def atan_recip(n):
    x=D(1)/n
    term=x
    total=x
    for j in range(1,10000):
        term=-term*x*x
        new=total+term/(2*j+1)
        if new==total:
            return total
        total=new
    raise ArithmeticError('Machin series did not converge')

def natural_e():
    total=term=D(1)
    for n in range(1,10000):
        term/=n
        new=total+term
        if new==total:
            return total
        total=new
    raise ArithmeticError('e series did not converge')

def small_alpha(K):
    x=K
    for _ in range(100):
        y=x-(x**4-x*x+K*K)/(4*x**3-2*x)
        if abs(y-x)<=abs(y)*D(10)**(-getcontext().prec+5):
            assert 0<y<nth(D(1)/2,2)
            return y
        x=y
    raise ArithmeticError('Small-alpha Newton iteration did not converge')

def independent(precision):
    with localcontext() as ctx:
        ctx.prec=precision+25
        pi=16*atan_recip(5)-4*atan_recip(239)
        eb=natural_e()
        eta=lambda z:1/nth(1+D(z)/pi**4,4)
        h,d,d12=eta(4),eta(5),eta(80)
        s,s12,sh=nth(d,2),nth(d12,2),nth(h,2)
        A1,A2=s*(1-s)/(1+s),s12*(1-s12)/(1+s12)
        K=9*(5*h+2*sh+1)*(1-A1*A2)/(32*pi**5)
        source_alpha=small_alpha(K)
        u=1/nth(eb,3)
        invbeta=D(contract['historical']['beta_inverse'])
        c=D(contract['shared']['c_m_per_s'])
        s0=D(contract['shared']['s0_m'])
        conv=D(contract['units']['comparison_factor_kg_to_MeV_c2'])
        rows=[]
        all_structural=[]
        for identifier in range(65):
            mask=identifier if identifier<64 else 0
            alternate=identifier==64
            selected=lambda bit:bool(mask & (1<<bit))
            xi=nth(D(5),2)/2+D(1)/2 if selected(3) else D(contract['baseline']['xi'])
            a=1/D(contract['historical']['alpha_inverse']) if selected(2) else source_alpha
            power=1 if selected(0) else 3
            rf=xi*d if selected(1) else nth(xi*d,2)
            if alternate:
                rf=nth(xi,2)*d
            first=(a/3)*(xi/d**2)**3*d**3*(1+s)**power
            second=(2/eb)*rf*((1-s)/(1+s))**2
            a1,a2,a3=(1+s)/2,1/d,1-first-second
            t=1-D(2)/3*xi*h*h*(1-sh)
            ap=t/nth(h**7,3)-1
            am=h*(ap+1)-1
            assert ap>am>0 and min(a1,a2,a3)>0
            G=a1*3**2*(3+1)**2+(D(2)/3*a2)*3*(2*3**2+3*3+1)+(2*a3)*2*(2+1)+4
            L=12*s/pi*(1-a/3)*(1+4*pi*a/(h*sh))+8*a/xi**2
            phi_numerator=(ap-am)*L+4*am
            phi=phi_numerator/ap
            hbar=D(contract['historical' if selected(4) else 'baseline']['hbar_Js'])
            gamma=D(contract['historical' if selected(5) else 'baseline']['gamma_m3_per_kg_s2'])
            mu=nth(pi**7*hbar**10/(9*gamma**2*c**6*s0**8),12)
            mass=mu*(ap*G+phi_numerator)
            minus=mu*(ap*(G-4)+phi_numerator)
            step=mu*ap*4
            g=27*a1+9*a2+2*a3+u
            upper=(64*a1-g,7*a2-2*a3-u,a3-u)
            structural=(2*a3-1,9*a2-2*a3,27*a3-9*a2,
                        2*a3-1,18*a2-6*a3,162*a1-84*a2)
            dom6=1-pi*eb**3*xi**2*source_alpha**2
            dom10=1-pi*eb**3*xi**2*((invbeta-1)*(invbeta+1)/invbeta**2)
            assert min(upper+structural+(dom6,dom10))>0
            all_structural.extend(structural)
            vals=dict(alpha=a,xi=xi,alpha3=a3,first=first,second=second,
                      mass_plus=ap,mass_minus=am,G_aux=G,Phi_aux=phi,L_reduced=L,
                      A36_H006=dom6,A36_H010=dom10,mu_kg=mu,mass_kg=mass,
                      mass_MeV_c2=mass*conv,one_n4_step_kg=step,
                      diagnostic_n4_minus1_mass_kg=minus,
                      diagnostic_n4_minus1_mass_MeV_c2=minus*conv,
                      upper1=upper[0],upper2=upper[1],upper3=upper[2])
            with localcontext() as rounded:
                rounded.prec=precision
                rows.append({key:+value for key,value in vals.items()})
        return rows,min(all_structural)

own80,struct80=independent(80)
own120,struct120=independent(120)
assert len(own120)==65 and all(len(v)==21 for v in own120)

# Only now read the old output comparison and invoke the NEW own project API.
snapshot=json.loads((ROOT/'05_analysis/historical_n0_results.json').read_text(encoding='utf-8'))
sys.path.insert(0,str(ROOT/'scripts'))
import audit_historical_n0 as checked
fresh120=checked.build_report(120)

def flatten(report):
    ans=[]
    for row in report['cells']+[report['baseline_alternate_root_scope']]:
        vals={key:D(row[key]) for key in own120[0]
              if key not in ('first','second','A36_H006','A36_H010','upper1','upper2','upper3')}
        vals.update(first=D(row['alpha3_subtrahends'][0]),second=D(row['alpha3_subtrahends'][1]),
                    A36_H006=D(row['A36_denominators']['H006']),A36_H010=D(row['A36_denominators']['H010']))
        vals.update({f'upper{n+1}':D(v) for n,v in enumerate(row['first_three_upper_margins'])})
        assert row['occupations']==[0,0,0,0]
        assert row['K4_method']=='analytic_identity_W_equals_g'
        ans.append(vals)
    assert [r['mask'] for r in report['cells']]==list(range(64))
    for row in report['cells']:
        assert row['changed_axes']==[a for n,a in enumerate(AXES) if row['mask'] & (1<<n)]
        assert row['alternate_root_scope'] is False
    assert report['baseline_alternate_root_scope']['alternate_root_scope'] is True
    return ans

with localcontext() as ctx:
    ctx.prec=140
    for label,other,tolerance in (
        ('own80_vs_own120',own80,D('1e-78')),
        ('snapshot80_vs_own120',flatten(snapshot),D('1e-74')),
        ('new_API120_vs_own120',flatten(fresh120),D('1e-114'))):
        worst=max(abs(row[k]-ref[k])/abs(ref[k]) for row,ref in zip(other,own120) for k in ref)
        assert worst<tolerance,(label,worst)
        print(label,'comparisons',65*21,'max_relative_error',format(worst,'.12E'))
    M=lambda mask:own120[mask]['mass_kg']
    baseline=M(0)
    mass_tol=baseline*D('1e-74')
    delta_total=M(63)-M(0)
    for report in (snapshot,fresh120):
        for field,order in (('forward_attribution',tuple(range(6))),
                            ('reverse_attribution',tuple(reversed(range(6))))):
            before=0
            for row,bit in zip(report[field],order):
                after=before | (1<<bit)
                delta=M(after)-M(before)
                assert row['axis']==AXES[bit] and row['before_mask']==before and row['after_mask']==after
                assert abs(D(row['delta_kg'])-delta)<mass_tol
                assert abs(D(row['ppm_of_baseline'])-delta/baseline*D('1e6'))<D('1e-65')
                before=after
            assert before==63
        for bit,row in enumerate(report['marginal_ranges']):
            effects=[M(mask | (1<<bit))-M(mask) for mask in range(64) if not mask & (1<<bit)]
            assert len(effects)==32 and row['axis']==AXES[bit]
            for field,val in (('min_delta_kg',min(effects)),('max_delta_kg',max(effects)),
                              ('alone_delta_kg',M(1<<bit)-M(0))):
                assert abs(D(row[field])-val)<mass_tol
        comparison=report['comparison']
        saved=D(contract['comparison_only']['saved_program_mass_MeV_c2'])
        converted=own120[63]['mass_MeV_c2']
        assert D(comparison['saved_program_mass_MeV_c2'])==saved
        assert abs(D(comparison['own_historical_minus_saved_MeV_c2'])-(converted-saved))<D('1e-74')
        assert abs(D(comparison['relative_to_saved'])-(converted-saved)/saved)<D('1e-74')
        assert abs(D(comparison['total_ppm_of_baseline'])-delta_total/baseline*D('1e6'))<D('1e-65')
        expected={
            'total_delta_kg':delta_total,
            'sum_of_isolated_deltas_minus_total':sum(M(1<<b)-M(0) for b in range(6))-delta_total,
            'alternate_root_scope_delta_kg':own120[64]['mass_kg']-M(0),
            'forward_telescope_residual':D(0),'reverse_telescope_residual':D(0)}
        for field,val in expected.items():
            assert abs(D(comparison[field])-val)<mass_tol
    for identifier in (0,63,64):
        row=own120[identifier]
        print('cell',identifier,'mass_kg',format(row['mass_kg'],'.40g'),
              'MeV_c2',format(row['mass_MeV_c2'],'.40g'))
    print('minimum_upper_margin',format(min(r[k] for r in own120 for k in ('upper1','upper2','upper3')),'.30g'))
    print('minimum_structural_margin',format(struct120,'.30g'))
    print('minimum_A36',format(min(r[k] for r in own120 for k in ('A36_H006','A36_H010')),'.30g'))
    print('n4_step_baseline_kg',format(own120[0]['one_n4_step_kg'],'.40g'))
    print('two_orders_six_marginal_ranges_and_all_comparison_fields OK')
```

### Tatsaechlicher Prueflauf und Ergebnis

Am 2026-09-06 erfolgreich ausgefuehrt; 21 Felder mal 65 Zellen in
jedem der folgenden drei Vergleiche, insgesamt 4095 Feldvergleiche:

| Vergleich | Maximaler relativer Feldfehler |
|---|---:|
| Eigene 80 gegen eigene 120 Stellen | 3.072074353802e-80 |
| Root-Snapshot 80 gegen eigene 120 Stellen | 6.777276539362e-78 |
| Neues Root-API 120 gegen eigene 120 Stellen | 4.680943492175e-118 |

Das sind Stabilitaets-/Reproduktionszahlen, keine physikalischen
Unsicherheiten. Vergleichene Felder umfassen alpha, xi, alpha3 und
beide Subtrahenden, ap/am, G/Phi/L, zwei A36-Nenner, mu, beide
Masseneinheiten, n4-Schritt und hypothetische n4=-1-Masse sowie alle
drei oberen Auswahlmargen.

| Profil / eigene Zelle | Masse in kg | Historische Umrechnung in MeV/c^2 |
|---|---:|---:|
| H006-Ausgangspunkt, Maske 0 | 9.078017464516427097595915517541e-31 | 0.5092394872636273266926139365131 |
| H010-reelle Idealisierung, Maske 63 | 9.109380891976903867530980751052e-31 | 0.5109988467032000658474002028651 |
| Zusaetzliche engere Wurzellesart am Ausgangspunkt | 9.078017492717489556154844147927e-31 | 0.5092394888455910806531900725990 |

Alle Werte in der Tabelle sind hier gerundet. Die kleinste Greedy-Marge
ueber alle 65 Zellen ist 0.198669735966646741805672336455; die kleinste
XIII/XXXII-Marge 0.830402093080871984462552866761; der kleinste der beiden
A36-Nenner 0.991204598568176056597554421608. Die Auswahl wird daher in
keiner dieser festgelegten Zellen durch einen nahen oberen Ganzzahlrand
der ersten drei Schritte zweifelhaft. K4 bleibt die gesonderte exakte
Identitaet, nicht eine vierte solche numerische Marge.

Der isolierte Schritt n4=-1 nach 0 betraegt am Ausgangspunkt
1.655602349359115736412344016233e-32 kg. Seine Groesse darf nicht
als Anteil einer beobachteten Massenabweichung interpretiert werden.
Die zwei vollstaendigen Attributionsketten, sechs Minimal-/Maximal-
Achsenwirkungen ueber jeweils 32 Paare und alle numerischen
`comparison`-Felder wurden ebenfalls gegen die eigenen 120-Stellen-Zellen
nachgerechnet. Insbesondere sind Gesamtbilanz und Nichtadditivitaet
der isolierten Ausgangspunktdifferenzen bestaetigt.

### Code-, Vertrags- und Testgegenlesung

`evaluate_cell` sperrt fremde Masken, andere Zustaende, geaenderte
festgelegte Zahlen und einen True-Fit-Schalter. Der nachgelagerte
gespeicherte Ausgabewert geht in keine Zelle oder Auswahl ein.
Die alternate-root-Zelle bleibt von den 64 Zellen getrennt. Keine
Pascal-/C-Trunkationszuschlaege werden in den Rechner uebernommen.
Die vorhandene `zero_selection` prueft vor dem K4-Zertifikat K1--3
sowie XIII/XXXII; die Reduktion wird nicht aufgrund einer guenstigen
Massenzahl gewaehlt.

Die neue `mu`-Auswertung stimmt mit der unabhaengigen zwoelften
Wurzel ueberein. Fuer die beiden reinen Formelachsen bestaetigen
die Tests ferner DeltaM=12*mu*ap*Deltaalpha3 bei unveraendertem Phi;
fuer die getrennte Besetzungsdiagnose gilt DeltaM=4*mu*ap.
Ein hoehere-Praezision-Raster ist eine Idealisierung derselben positiven
reellen Gleichungen, keine Emulation der historischen Ausdrucksfolge.

Ausgefuehrte Projektkontrollen:

```text
python -B scripts/audit_historical_n0.py --check --verify-sources
python -B -m unittest discover -s tests -p 'test_historical_n0.py' -v
git diff --check
```

Snapshot identisch, alle vier H006/H010-Dateihashes bestaetigt,
15 neue Tests erfolgreich, kein whitespace-Befund. Kein numerischer
oder algebraischer Defekt im geprueften neuen Raster gefunden.

Kleine Dauerregressions-Empfehlung an Root: einige nichtempirische
Zahlenanker aus dieser unabhaengigen Rechnung, mindestens Maske63
und die Zusatzlesart, in den neuen Tests sichern. Die bisherigen
Tests sind sinnvoll, vergleichen aber vielfach dieselbe neue
Auswertungsfunktion bzw. den gemeinsamen alten Rechenkern. Die hier
ausgefuehrte Gegenrechnung ersetzt diese Abhaengigkeit fuer den
aktuellen Stand, aber nicht automatisch fuer jede spaetere Aenderung.

Nur diese Review wurde von data_audit geaendert. Alte Rechner,
Eingaben, Snapshots, Normalisierungen und historische Dateien wurden
nicht bearbeitet. Die enge Uebereinstimmung mit dem gespeicherten
H010-Wert ist eine bedingte Ausgabereproduktion; weder zeitliche
Originalitaet noch empirische Vorhersagekraft noch die Absicht hinter
den zwei alpha3-Unterschieden folgt daraus.
