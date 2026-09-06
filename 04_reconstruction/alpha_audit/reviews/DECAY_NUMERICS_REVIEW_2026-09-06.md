# A=1/3 und A=1/5: unabhaengige Vier-Zellen-Numerik

2026-09-06, Etappe35. Vorvertrag gelesen:
`00_admin/DECAY_SENSITIVITY_PLAN.md` und
`04_reconstruction/alpha_audit/decay_sensitivity_inputs.json`, vor Auswertung
gesichert in3a3ad73. Die beiden bisherigen Alpha-Profile bleiben unveraendert.
A=1/5 ist eine eigene, vorher benannte Sensitivitaet, keine Heim-Korrektur.
Keine Originalquelle neu gelesen, keine Masse oder Zielzahl eingesetzt.

## 1. Rechenvertrag und unabhaengige Methode

Fuer jedes Alpha-Profil sind a1,a2,a3,d,A16,w und Q=(3,3,2,1) fest.
Nur E_A(n)=exp(-A*n) aendert sich, und zwar GEMEINSAM in
`g_A=B+E_A(1)`, `W_A=w*g_A` und dem linken Externterm, mit
`B=27*a1+9*a2+2*a3`. Die Nullreferenz bleibt E_A(0)=1.

Der folgende selbstenthaltene Block verwendet keine Root-Rechner oder
Testhelfer. Eigene Machin-Reihe, rational gerichtete Intervalloperationen,
isqrt und Taylorreste sichern Vorzeichen und Zweige. Die alte eigene
Et32-Kette ist hier eigenstaendig ausgeschrieben und nur um den expliziten
A-Parameter erweitert. Decimal120/160 mit jeweils20 Schutzstellen liefert
unabhaengige Darstellungs-/Stabilitaetskontrollen, keine physikalische Genauigkeit.

Greedy bestimmt nur N1..N3. Die reelle Umkehrung `raw=-ln(r)/A` ist eine
Hilfszahl, kein ausgewaehlter Zustand. Floor wird NUR im freigegebenen Fall
0<r<=1 und raw<=a3*N3 als N4 ausgegeben. Ein Kappenverstoss wird gemeldet,
ohne N4 zu kappen, umzubuchen oder einen Transfer zu erfinden. Volle Gates,
R und107b werden nur fuer eine tatsaechlich freigegebene Ausgabe berichtet;
am blossen reellen Umkehrwert heissen dieselben Groessen ausdruecklich
Hilfsdiagnosen und duerfen einen gescheiterten Gatecheck nicht ersetzen.

## 2. Selbstenthaltener Kontrollblock

```python
from decimal import Decimal as D, localcontext, ROUND_FLOOR
from fractions import Fraction as F
from math import factorial, isqrt

SCALE=10**60
class I:
    def __init__(self, lo, hi=None):
        lo,hi=F(lo),F(lo if hi is None else hi)
        assert lo<=hi
        self.lo=F((lo*SCALE).__floor__(),SCALE)
        self.hi=F((hi*SCALE).__ceil__(),SCALE)
    @staticmethod
    def cast(x):
        return x if isinstance(x,I) else I(x)
    def __add__(self,x):
        x=I.cast(x); return I(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self):
        return I(-self.hi,-self.lo)
    def __sub__(self,x):
        return self+-I.cast(x)
    def __rsub__(self,x):
        return I.cast(x)+-self
    def __mul__(self,x):
        x=I.cast(x)
        ends=[a*b for a in (self.lo,self.hi) for b in (x.lo,x.hi)]
        return I(min(ends),max(ends))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=I.cast(x); assert not x.lo<=0<=x.hi
        return self*I(1/x.hi,1/x.lo)
    def __rtruediv__(self,x):
        return I.cast(x)/self
    def __pow__(self,n):
        assert type(n) is int and n>=0
        answer=I(1)
        for _ in range(n): answer=answer*self
        return answer
    def sqrt(self):
        assert self.lo>=0
        lo=isqrt(self.lo.numerator*SCALE*SCALE//self.lo.denominator)
        hi=isqrt(self.hi.numerator*SCALE*SCALE//self.hi.denominator)
        if F(hi,SCALE)**2<self.hi: hi+=1
        assert F(lo,SCALE)**2<=self.lo<=self.hi<=F(hi,SCALE)**2
        return I(F(lo,SCALE),F(hi,SCALE))

def atan_i(n):
    partial=sum((F((-1)**j,(2*j+1)*n**(2*j+1)) for j in range(100)),F(0))
    return I(partial,partial+F(1,201*n**201))

def expneg_i(x):
    # Taylor through degree99. Lagrange remainder is positive and <=x^100/100!.
    x=F(x); assert 0<=x<=4
    partial=sum(((-x)**n/factorial(n) for n in range(100)),F(0))
    return I(partial,partial+x**100/factorial(100))

def constants_i():
    pi=16*atan_i(5)-4*atan_i(239)
    partial=sum((F(1,factorial(n)) for n in range(100)),F(0))
    e=I(partial,partial+F(1,factorial(100))/(1-F(1,101)))
    return pi,e,(1+I(5).sqrt())/2

def pi_d():
    def atan(n):
        x=D(1)/n; term=total=x; j=1
        while True:
            term*=-x*x; new=total+term/(2*j+1)
            if new==total: return new
            total,j=new,j+1
    return 16*atan(5)-4*atan(239)

def base(pi,e,xi,printed):
    one=pi*0+1
    eta,d,t=(1/(one+(4+j)/pi**4).sqrt().sqrt() for j in (0,1,2))
    s,st=d.sqrt(),t.sqrt()
    c1,c2=s*(1-s)/(1+s),st*(1-st)/(1+st)
    rhs=9*(5*eta+2*eta.sqrt()+1)*(1-c1*c2)/(32*pi**5)
    if printed:
        alpha=I('0.007297354572') if isinstance(rhs,I) else D('0.007297354572')
    elif isinstance(rhs,I):
        assert 0<rhs.lo<=rhs.hi<F(1,2)
        alpha=(2*rhs**2/(1+(1-4*rhs**2).sqrt())).sqrt()
    else:
        alpha=rhs
        for _ in range(1000):
            nxt=rhs/(1-alpha**2).sqrt()
            if nxt==alpha: break
            alpha=nxt
        else: raise ArithmeticError('small alpha iteration')
    a1,a2=(1+s)/2,1/d
    a3=1-alpha*(1+s)*xi**3/(3*d**3)-2*xi*d/e*((1-s)/(1+s))**2
    a16=(pi*e)**2*(1+alpha*(1+6*alpha/pi)/(5*eta))
    w=1+d*a16; B=27*a1+9*a2+2*a3
    return dict(alpha=alpha,a1=a1,a2=a2,a3=a3,d=d,A16=a16,w=w,B=B)

def prefix_gates(n):
    n1,n2,n3=n
    return dict(beta_first2=(n1**3-n2*(n2+1)*(2*n2+1)//6,
                             n2*n2-n3*(n3+1)//2),
                second_margins=(n1**3-n2*n2,n2*n2-n3,n3-1),
                center=n1**3)

def cell_d(printed,denom,precision):
    with localcontext() as ctx:
        ctx.prec=precision+20
        b=base(pi_d(),D(1).exp(),(1+D(5).sqrt())/2,printed)
        g=b['B']+(-D(1)/denom).exp(); W=b['w']*g
        g0=b['B']+(-D(1)/3).exp()
        values=dict(b,g=g,W=W,delta_g=g-g0,delta_W=b['w']*(g-g0))
        rem=W; n=[]
        for j,power in enumerate((3,2,1),1):
            coeff=b['a'+str(j)]; integer=0
            while coeff*(integer+1)**power<=rem: integer+=1
            n.append(integer); rem-=coeff*integer**power
            values['rest'+str(j)]=rem
            values['upper_gap'+str(j)]=coeff*(integer+1)**power-(rem+coeff*integer**power)
        assert 0<rem<=1
        raw=-D(denom)*rem.ln(); cap=b['a3']*n[2]
        values.update(r=rem,raw_N4=raw,cap=cap,cap_margin=cap-raw,
                      real_beta4=n[2]-raw,real_sigma=cap-raw,
                      real_relax_margin=n[2]-1-raw,
                      real_inverse_R=(-raw/D(denom)).exp()-rem)
        exact=dict(N123=tuple(n),**prefix_gates(n))
        if raw<=cap:
            N4=int(raw.to_integral_value(rounding=ROUND_FLOOR))
            selected=tuple(n)+(N4,)
            exact.update(status='ordinary_floor',N=selected,
                         small_n=tuple(a-b for a,b in zip(selected,(3,3,2,1))),
                         beta4=n[2]-N4)
            values['R']=(-D(N4)/denom).exp()-rem
            values['sigma_107b']=cap-N4
            direct=sum((b['a'+str(j)]*n[j-1]**p for j,p in enumerate((3,2,1),1)),D(0))
            values['R_direct']=direct+(-D(N4)/denom).exp()-W
        else:
            exact['status']='saturation_boundary_no_N4_selected'
        ctx.prec=precision
        return {key:+v for key,v in values.items()},exact

def cell_i(printed,denom,chosen):
    b=base(*constants_i(),printed)
    assert min(b['a'+str(j)].lo for j in (1,2,3))>0
    g=b['B']+expneg_i(F(1,denom)); W=b['w']*g
    oldg=b['B']+expneg_i(F(1,3))
    values=dict(b,g=g,W=W,delta_g=g-oldg,delta_W=b['w']*(g-oldg))
    rem=W
    for j,(integer,power) in enumerate(zip(chosen,(3,2,1)),1):
        coeff=b['a'+str(j)]
        assert (rem-coeff*integer**power).lo>=0
        gap=coeff*(integer+1)**power-rem
        assert gap.lo>0
        rem=rem-coeff*integer**power
        values['rest'+str(j)]=rem; values['upper_gap'+str(j)]=gap
    assert 0<rem.lo<=rem.hi<1
    # Positive r, monotone exp: these are exact inverse-log brackets, not selections.
    raw_lo,raw_hi=(7,8) if denom==3 else (14,15)
    assert expneg_i(F(raw_hi,denom)).hi<rem.lo
    assert rem.hi<expneg_i(F(raw_lo,denom)).lo
    cap=b['a3']*chosen[2]
    if denom==3:
        assert F(raw_hi)<cap.lo
        values['R']=expneg_i(F(raw_lo,denom))-rem
        assert values['R'].lo>0
        values['sigma_107b']=cap-raw_lo
        assert values['sigma_107b'].lo>0
    else:
        assert cap.hi<F(raw_lo)
        assert chosen[2]-1<F(raw_lo)  # Real inverse violates declared relaxation cap too.
    # Fresh common outer bounds from this cell's W, never an inherited cutoff.
    assert I(F(996,1000)).hi<b['a1'].lo and W.hi<2838
    assert 15**3*b['a1'].lo>W.hi
    assert 20*21*41//6>14**3 and 27*28//2>19**2
    return values,(raw_lo,raw_hi)

all_cells={}
for printed in (False,True):
    for denom in (3,5):
        low,lexact=cell_d(printed,denom,120)
        high,hexact=cell_d(printed,denom,160)
        assert low.keys()==high.keys() and lexact==hexact
        diffs={key:abs(F(low[key])-F(high[key])) for key in low}
        assert max(diffs.values())<F(1,10**112)
        assert abs(F(high['real_inverse_R']))<F(1,10**150)
        if hexact['status']=='ordinary_floor':
            assert abs(F(high['R'])-F(high['R_direct']))<F(1,10**150)
        intervals,raw_bracket=cell_i(printed,denom,hexact['N123'])
        for key,interval in intervals.items():
            for value in (low[key],high[key]):
                assert interval.lo<=F(value)<=interval.hi,key
        if denom==5:
            assert intervals['delta_g'].lo>0 and intervals['delta_W'].lo>0
        else:
            assert high['delta_g']==high['delta_W']==0
        with localcontext() as ctx:
            ctx.prec=45
            print('\nCELL',printed,denom,hexact)
            print('fields',len(high),'exact_intervals',len(intervals),
                  'raw_bracket',raw_bracket,'max_delta',
                  D(max(diffs.values()).numerator)/D(max(diffs.values()).denominator))
            for key in ('g','W','delta_g','delta_W','r','raw_N4','cap','cap_margin',
                        'R','sigma_107b','real_beta4','real_sigma','real_relax_margin'):
                if key in high: print(key,+high[key])
        all_cells[printed,denom]=(high,hexact)
print('\nAll four fixed cells; no mass, no repaired selection, no Root imports.')
```

## 3. Ausfuehrung und Ergebnis

Der Block wurde eigenstaendig via `py -3.13 -B -` ausgefuehrt, Exitcode0.
Alle vier Zellen bestanden ihre rationalen Zweig- und Bereichsbelege.
Decimal120/160 verglich 29 Felder je1/3-Zelle und26 je1/5-Zelle, insgesamt
110 Felder. Diese enthalten abhaengige Hilfsgroessen und sind nicht110
unabhaengige Aussagen. Groesster Absolutabstand aller vier Zellen:
4.9747143599631e-117. Dazu76 rationale Intervalle, die jeweils beide
Dezimalausgaben einschliessen; Raw-Logarithmen selbst werden durch die
unten erklaerten Exponentialschranken zertifiziert, nicht durch Decimal.

Die folgenden Zahlen sind gerundete mathematische Rechenausgaben, keine
physikalischen Vorhersagen oder Messunsicherheiten. Primar bezeichnet den
kleinen Buch-(105)-Zweig; Druck bezeichnet die festgelegte Alpha-Sensitivitaet.

| Alpha-Profil | A | g_A | W_A | Delta W relativ zu A=1/3 |
|---|---:|---:|---:|---:|
| Primar | 1/3 | 38.70297671932081516476 | 2830.26325766809626412716 | 0 |
| Primar | 1/5 | 38.80517616182500777301 | 2837.73687731165673087423 | 7.47361964356046674707 |
| Druck | 1/3 | 38.70297671947027738528 | 2830.26325766422754316483 | 0 |
| Druck | 1/5 | 38.80517616197446999352 | 2837.73687730774893268732 | 7.47361964352138952250 |

Delta g ist in beiden Alpha-Profilen dieselbe feste Differenz
`exp(-1/5)-exp(-1/3)=0.1021994425041926082443314117...>0`.
Delta W=w*Delta g unterscheidet sich wegen des jeweiligen unveraenderten w.
Es wurde nicht nur der linke Externterm geaendert.

| Alpha / A | N1,N2,N3 | r=W4 | raw=-ln(r)/A | a3*N3 | Vertragsstatus |
|---|---|---:|---:|---:|---|
| Primar /1/3 | (14,9,13) | 0.078485285181275285 | 7.634532365054299342 | 12.72256426813403140 | Gewoehnlich: N4=7 |
| Druck /1/3 | (14,9,13) | 0.078485280341049889 | 7.634532550065752143 | 12.72256426910553583 | Gewoehnlich: N4=7 |
| Primar /1/5 | (14,10,1) | 0.056750745033477030 | 14.34543247181796681 | 0.978658789856463954 | Kappenverstoss; keine N4-Ausgabe |
| Druck /1/5 | (14,10,1) | 0.056750741050947733 | 14.34543282269701118 | 0.978658789931195064 | Kappenverstoss; keine N4-Ausgabe |

Bei A=1/3 lauten die tatsaechlich ausgegebenen Tupel (14,9,13,7), die
kleinen Besetzungen (11,6,11,6) und die direkten Bandbreiten (2459,-10,6).
Die Differenzreihenfolge und das Zentrum bestehen, der zweite der ersten
Strukturgates scheitert weiterhin exakt an-10. Die getrennte107b-Groesse
ist5.7225642681340313975 beziehungsweise5.7225642691055358309. Der positive
Rest links minus rechts betraegt0.01848668268312977783 beziehungsweise
0.01848668752335517354. Das sind dieselben bedingten Ergebnisse wie zuvor,
keine exakten Loesungen von108.

Bei A=1/5 bestehen an der N1..N3-Vorwahl die ersten beiden direkten Gates
mit2359 und99; die zweite Reihenfolge hat Margen(2644,99,0), das Zentrum2744.
Dies ist KEINE bestandene Vollstruktur: Im vertraglich gesperrten
Saettigungszweig wird N4 weder auf14 abgeschnitten noch auf die Kappe gesetzt.
Deshalb existieren dort keine ausgewaehlten R-/beta4-/107b-Ausgabewerte.

Nur an der reellen Hilfsumkehrung, die die Exponentialgleichung isoliert
loest, ist `beta4_real=1-raw` etwa-13.34543247 beziehungsweise-13.34543282
und `sigma_real=a3-raw` etwa-13.36677368 beziehungsweise-13.36677403.
Auch die vorab deklarierte reelle Relaxation verlangt bei N3=1 schon
0<=N4<=0; raw>14 verletzt diese Schranke. Diese reelle Zahl ist somit
nicht einmal eine zulaessige Loesung der erklaerten Relaxation an diesem
Vorwahlpraefix. Ueber andere gekoppelte N1..N3-Wahlen urteilt dieser
Vorwaertsbefund allein noch nicht.

Die Intervallmethode zertifiziert Greedy-Grenzen und den Kappenvergleich
ohne einen Logarithmus zu runden: Aus exp(-A*(j+1))<r<exp(-A*j) folgt
streng j<raw<j+1. Das ist im nicht freigegebenen Zweig lediglich eine
Rohwert-Einhuellung, keine heimlich ausgegebene Besetzung.

Alle vier Zellen liefern frisch W<2838, a1>0.996 und 3375*a1>W. Daher
muss jede exakte Loesung N1<=14 haben. Die ersten beiden direkten Gates
geben dann N2<=19 und N3<=26, der dritte ganzzahlige Gate N3>N4 liefert
N4<=25. Die gleiche Box entsteht also erneut aus JEDER neuen Eingabe,
nicht durch Uebernahme der alten Energiegrenze. Dies allein ist noch kein
Nachweis einer Loesung oder Nichtloesung innerhalb dieser Box.

Der Rechnerblock fuehrt keine historischen Programme aus und importiert
keinen neuen oder alten Root-Rechner. Nur diese neue eigene Review wurde
geschrieben; bestehende Eingaben, Rechner, Snapshots und Tests blieben
unangetastet. Die Beurteilung einer aus den Quellen abgeleiteten
physikalischen Ersatzfunktion ist nicht Gegenstand dieser Sensitivitaet.

## 4. Neue Codegegenreview und unabhaengige gekoppelte Endpunktkontrolle

`scripts/audit_decay_sensitivity.py` und `tests/test_decay_sensitivity.py`
vollstaendig gegengelesen. Keine materiellen Fehler im gebundenen Vier-Zellen-
Vertrag gefunden. Fuer x>=0 reduziert der neue Rechner mit m=max(1,ceil(x))
auf0<=x/m<=1; positive Taylorhuelle, Kehrwert und m-te Potenz schliessen
exp(-x) ein. Die Wiederverwendung derselben Intervalle verbreitert moegliche
Abhaengigkeiten, verengt sie aber nicht unberechtigt.

Die Rohwertkappe hat die richtige Richtung: raw<=a3*N3 ist aequivalent zu
r>=exp(-A*a3*N3). Der gewoehnliche Zweig wird fuer beide1/3-Zellen streng
zertifiziert; in beiden1/5-Zellen gibt es keine erfundene N4-, R- oder
sigma-Ausgabe. Fuer die Baseline wird Delta g exakt0 als Funktionsidentitaet
gesetzt, statt zwei identische, aber voneinander unabhaengig behandelte
Intervalle zu subtrahieren. Delta W ist dann ebenfalls exakt0.

Die neue Bereichsherleitung verwendet jeweils die betreffende W-Huelle,
nicht einen alten Cutoff. `gates` trennt die direkten Bedingungen von107b;
1239 direkte, ganzzahlige N1..N3-Praefixe decken mit je N3 moeglichen
Integerwerten N4 insgesamt9231 Zustaende ab. Monotonie des Externterms
macht die Pruefung an den beiden N4-Endpunkten vollstaendig. Der positive
Restabstand oberhalb der N1-Box wird ebenfalls mitgefuehrt.

Die zusaetzliche reelle Pruefung0<=N4<N3 ist klar vom VORHER deklarierten
0<=N4<=N3-1 getrennt. Im groesseren Bereich ist exp(-A*N3) eine nicht
erreichte untere Exponentialgrenze; eine bereits strikt positive untere
Restschranke dort schliesst alle tatsaechlichen Argumente sicher aus.
Dies aendert keine Eingaben und behauptet keine physikalische Relaxation.

Selbst ausgefuehrt, jeweils Exitcode0:

```text
py -3.13 -B scripts/audit_decay_sensitivity.py --check --verify-sources
  H004-Hash und alle vier Zellen erfolgreich.
py -3.13 -B -m unittest discover -s tests -p test_decay_sensitivity.py -v
  15 Tests bestanden.
```

Anschliessend wurde die Endpunktkontrolle unabhaengig mit der EIGENEN
Intervallkette oben wiederholt. Der folgende Anschlussblock wird nach dem
obigen Hauptblock ausgefuehrt und importiert selbst keinen Root-Rechner:

```python
for printed in (False,True):
    for denom in (3,5):
        _,exact=all_cells[printed,denom]
        own,_=cell_i(printed,denom,exact['N123'])
        a1,a2,a3,W=(own[key] for key in ('a1','a2','a3','W'))
        # Independent fixed fourfold reduction; arguments are <=26/(3*4).
        exps=[expneg_i(F(j,denom)/4)**4 for j in range(27)]
        min_closed=min_open=a1.lo*3375-W.hi
        triples=states=0
        for n1 in range(15):
            for n2 in range(20):
                if n1**3<=n2*(n2+1)*(2*n2+1)//6: continue
                for n3 in range(1,27):
                    if not(n2*n2>n3*(n3+1)//2 and n1**3>=n2*n2>=n3>=1): continue
                    triples+=1; states+=n3
                    poly=a1*n1**3+a2*n2*n2+a3*n3
                    upper=poly+1-W
                    closed_low=poly+exps[n3-1]-W
                    open_low=poly+exps[n3]-W
                    assert closed_low.lo>0 or upper.hi<0
                    assert open_low.lo>0 or upper.hi<0
                    min_closed=min(min_closed,closed_low.lo if closed_low.lo>0 else -upper.hi)
                    min_open=min(min_open,open_low.lo if open_low.lo>0 else -upper.hi)
        assert triples==1239 and states==9231
        assert min_closed>0 and min_open>0
        if denom==5:
            assert min_closed>F('0.9432492549') and min_open>F('0.7619800080')
        scale=10**12
        print('independent endpoints',printed,denom,triples,states,
              'closed/open lower bounds rounded DOWN',
              F((min_closed*scale).__floor__(),scale),
              F((min_open*scale).__floor__(),scale))
```

Alle vier Zellen bestanden. Fuer A=1/5 sind die unabhaengig gesicherten
Restabstaende im engeren geschlossenen Bereich groesser als0.943249254966
beziehungsweise0.943249258949. In der zusaetzlichen offenen Domain sind
sie groesser als0.761980008044 beziehungsweise0.761980012027. Diese Werte
sind konservative rationale Untergrenzen, keine optimierten physikalischen
Fehlerschranken. Der getrennte gekoppelte Nachweis erweitert also den blossen
Vorwaertsbefund aus Abschnitt3; er folgt nicht schon aus dessen Kappenverstoss.

Zudem separat den neuen Root-Rechner fuer einen Kreuzvergleich importiert:
72 Root-Intervalle enthalten die engeren eigenen Intervalle vollstaendig.
Bei den vier Baseline-Feldern Delta g/Delta W wurde stattdessen die exakte
Nullidentitaet geprueft; das verhindert einen unsinnigen Vergleich gegen
eine breitere, abhaengigkeitsvergessene Differenzhuelle. Der eigenstaendige
Haupt- und Endpunktblock bleiben ohne Root-Import reproduzierbar. Nur diese
eigene Review wurde um die Gegenpruefung ergaenzt.
