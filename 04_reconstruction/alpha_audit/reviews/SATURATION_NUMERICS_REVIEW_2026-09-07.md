# Saettigungsfortsetzung: unabhaengige Vier-Zellen-Kontrolle

2026-09-07, Etappe36. Vorvertragfa25c42 gelesen:
`00_admin/SATURATION_PLAN.md` und `saturation_inputs.json`.
Der kanonische JSON-SHA256 wurde unabhaengig bestaetigt:
`902f775de16e96628825c7ebab93881e58cae1a334f2f1a4710b7528eec98f98`.
Keine neue Quellenlesung, Masse, Fehlerzulage oder angepasste Eingabe.

## 1. Enger Vertrag und Reproduktionsbasis

Alle vier Et35-Zellen bleiben fest. A=1/3 ist Kontrolle, A=1/5 die schon
vorher benannte eigene Sensitivitaet. g_A und W_A bleiben in jeder Zelle
unveraendert gegenueber Et35; die neue Frage betrifft ausschliesslich die
jetzt vertraglich angefragte Fortsetzung des dort gestoppten Saettigungszweigs.

Es gilt cap=a3*N3 und im Saettigungszweig
`t=TRC(cap)`, danach `N4=t-1` NUR wenn t>cap, sonst N4=t.
Fuer beide1/5-Zellen ist cap streng zwischen0 und1. Die eigene konservative
TRC-Huelle t in{0,1} liefert deshalb in BEIDEN Faellen N4=0. Eine unbekannte
Promotionsschwelle wird weder erfunden noch aus den Dezimalstellen abgeleitet.
Dies behauptet nicht, dass die ganze Quellen-TRC-Funktion immer floor sei.

Die unabhaengige Machin-/Taylor-/Fraction-Kette aus der eigenen Et35-Review
wird wiederbenutzt, nicht ein Root-Rechner. Ihre gelesene Datei
`DECAY_NUMERICS_REVIEW_2026-09-06.md` hat SHA256
`A2335E497A31E15BD8BD0D031FFECC69927B82A5342EC07F0FB47B69D6B9E302`.
Der erste Pythonblock dieser Datei stellt alle benoetigten eigenen
Rechenfunktionen bereit; danach wird der folgende Anschlussblock ausgefuehrt.
So bleiben beide Rechenschritte aus den Reviewdateien reproduzierbar, ohne
historische oder Root-Programme zu importieren.

```powershell
$priorPath = '04_reconstruction/alpha_audit/reviews/DECAY_NUMERICS_REVIEW_2026-09-06.md'
if ((Get-FileHash -Algorithm SHA256 -LiteralPath $priorPath).Hash -ne 'A2335E497A31E15BD8BD0D031FFECC69927B82A5342EC07F0FB47B69D6B9E302') { throw 'Prior review changed' }
$priorText = Get-Content -Raw -LiteralPath $priorPath
$currentText = Get-Content -Raw -LiteralPath '04_reconstruction/alpha_audit/reviews/SATURATION_NUMERICS_REVIEW_2026-09-07.md'
$pattern = '(?s)```python\r?\n(.*?)\r?\n```'
$firstBlock = [regex]::Match($priorText, $pattern).Groups[1].Value
$nextBlock = [regex]::Match($currentText, $pattern).Groups[1].Value
($firstBlock + "`n" + $nextBlock) | py -3.13 -B -
```

## 2. Eigener Anschlussblock

```python
from decimal import ROUND_CEILING

def saturation_d(printed,denom,precision):
    with localcontext() as ctx:
        ctx.prec=precision+20
        b=base(pi_d(),D(1).exp(),(1+D(5).sqrt())/2,printed)
        g=b['B']+(-D(1)/denom).exp(); W=b['w']*g
        rem=W; prefix=[]
        for j,power in enumerate((3,2,1),1):
            coefficient=b['a'+str(j)]; integer=0
            while coefficient*(integer+1)**power<=rem: integer+=1
            prefix.append(integer); rem-=coefficient*integer**power
        raw=-D(denom)*rem.ln(); cap=b['a3']*prefix[2]
        if raw<=cap:
            candidates=(int(raw.to_integral_value(rounding=ROUND_FLOOR)),)
            branch='unchanged_ordinary_control'; t_values=None
        else:
            assert 0<cap<1
            t_values=(int(cap.to_integral_value(rounding=ROUND_FLOOR)),
                      int(cap.to_integral_value(rounding=ROUND_CEILING)))
            candidates=tuple(sorted({t-1 if D(t)>cap else t for t in t_values}))
            branch='saturation_continuation'
        assert len(candidates)==1
        n4=candidates[0]; N=tuple(prefix)+(n4,)
        small=tuple(n-q for n,q in zip(N,(3,3,2,1)))
        beta=prefix_gates(prefix)['beta_first2']+(prefix[2]-n4,)
        second=prefix_gates(prefix)['second_margins']
        poly=sum((b['a'+str(j)]*prefix[j-1]**p for j,p in enumerate((3,2,1),1)),D(0))
        external=(-D(n4)/denom).exp()
        values=dict(a3=b['a3'],w=b['w'],g=g,W=W,r=rem,raw=raw,cap=cap,
                    R_direct=poly+external-W,R_external=external-rem,
                    sigma=cap-n4)
        exact=dict(branch=branch,N=N,n=small,t_candidates=t_values,
                   beta=beta,second_margins=second,
                   direct_pass=min(beta)>=1 and min(second)>=0 and N[0]>0,
                   lower_bounds_pass=all(n>=-q for n,q in zip(small,(3,3,2,1))))
        if denom==5:
            assert t_values==(0,1) and n4==0
            values['R_one_minus_r']=1-rem
        ctx.prec=precision
        return {key:+v for key,v in values.items()},exact

def decimal_cell(interval,digits=20):
    scale=10**digits
    return F((interval.lo*scale).__floor__(),scale),F((interval.hi*scale).__ceil__(),scale)

def finite_decimal(value):
    with localcontext() as ctx:
        ctx.prec=80
        return str(D(value.numerator)/D(value.denominator))

saturation_results={}
for printed in (False,True):
    for denom in (3,5):
        low,lexact=saturation_d(printed,denom,120)
        high,hexact=saturation_d(printed,denom,160)
        assert lexact==hexact and low.keys()==high.keys()
        differences=[abs(F(low[key])-F(high[key])) for key in low]
        assert max(differences)<F(1,10**112)
        assert abs(F(high['R_direct'])-F(high['R_external']))<F(1,10**150)
        own,_=cell_i(printed,denom,hexact['N'][:3])
        n1,n2,n3,n4=hexact['N']
        polynomial=own['a1']*n1**3+own['a2']*n2**2+own['a3']*n3
        external=expneg_i(F(n4,denom))
        cap_i=own['a3']*n3
        certificates=dict(R_direct=polynomial+external-own['W'],
                          R_external=external-own['rest3'],sigma=cap_i-n4)
        assert hexact['lower_bounds_pass']
        if denom==5:
            assert 0<cap_i.lo<=cap_i.hi<1
            # Both admissible TRC-envelope outcomes coincide after the stated correction.
            assert {t-1 if F(t)>cap_i.hi else t for t in (0,1)}=={0}
            assert hexact['N']==(14,10,1,0) and hexact['n']==(11,7,-1,-1)
            assert hexact['beta']==(2359,99,1) and hexact['direct_pass']
            assert 0<certificates['sigma'].lo<=certificates['sigma'].hi<1
            certificates['R_one_minus_r']=1-own['rest3']
            assert high['R_external']==high['R_one_minus_r']
        else:
            assert hexact['N']==(14,9,13,7) and hexact['beta']==(2459,-10,6)
            assert not hexact['direct_pass']
        for key,interval in certificates.items():
            assert interval.lo>0
            assert interval.lo<=F(low[key])<=interval.hi
            assert interval.lo<=F(high[key])<=interval.hi
        bounds={key:decimal_cell(interval) for key,interval in certificates.items()}
        print('\nSATURATION CELL',printed,denom,hexact)
        print('fields',len(high),'certificates',len(certificates),
              'max120_160',finite_decimal(max(differences)))
        for key in ('R_direct','R_external','sigma'):
            print(key,'in',tuple(finite_decimal(v) for v in bounds[key]))
        saturation_results[printed,denom]=(high,hexact,bounds)
print('Four fixed cells, two unchanged controls; no mass or adjusted W/A.')
```

## 3. Ausfuehrungsbefund und Grenzen

Der oben dokumentierte Ablauf wurde eigenstaendig ausgefuehrt, Exitcode0.
Im neuen Anschluss wurden42 Decimal-Felder zwischen120/160 Stellen verglichen
(10 jeKontrollzelle,11 jeSaettigungszelle). Groesster Absolutabstand:
4.9747143599631e-117. Fuer14 benannte, teilweise identische Rest-/sigma-
Groessen lagen beide Dezimalausgaben zugleich innerhalb der unabhaengigen
rationalen Intervalle. Die Rechenpraezision ist kein physikalisches Fehlerbudget.

Die beiden Saettigungszellen liefern exakt

```text
N=(14,10,1,0), n=N-Q=(11,7,-1,-1),
beta_direct=(2359,99,1), second_margins=(2644,99,0).
```

Die folgenden geschlossenen Huellen besitzen exakte rationale Dezimalenden.
Direkte Berechnung und Restidentitaet wurden getrennt eingeschlossen und
liefern jeweils dieselbe hier dargestellte20-Dezimalstellen-Huelle:

| Profil / A | R-Untergrenze | R-Obergrenze | sigma-Untergrenze | sigma-Obergrenze |
|---|---:|---:|---:|---:|
| Primar /1/3 | 0.01848668268312977783 | 0.01848668268312977784 | 5.72256426813403139752 | 5.72256426813403139753 |
| Primar /1/5 | 0.94324925496652297000 | 0.94324925496652297001 | 0.97865878985646395365 | 0.97865878985646395366 |
| Druck /1/3 | 0.01848668752335517353 | 0.01848668752335517354 | 5.72256426910553583089 | 5.72256426910553583090 |
| Druck /1/5 | 0.94324925894905226716 | 0.94324925894905226717 | 0.97865878993119506391 | 0.97865878993119506392 |

Fuer z3 ist R exakt `1-W4` mit dem unveraenderten Et35-Rest W4. Die
direkte Summe P+exp(-A*N4)-W wurde ebenfalls frisch ausgewertet. Die
Kontrollen behalten N=(14,9,13,7) und ihren direkten Gateverstoss beta3=-10;
die neue Fortsetzung macht aus ihnen keine Saettigungsfaelle.

Die fehlende Besetzungsuntergrenze n_j>=0 wird nicht hinzugefuegt: Die Quelleingabe
verwendet hier n_j>=-Q_j, entsprechend nichtnegativen Gesamtbesetzungen.
Auch 0<sigma<1 wird nicht automatisch als Verbot interpretiert; sigma
ist die separat gewichtete107b-Groesse, nicht die ganzzahlige direkte beta4.
N4=0 bedeutet hier insbesondere NICHT beta4=0; der direkte Wert ist1,
also kein auf diese Zahl gestuetzter beta4-Nullkollaps.

Ein bestandenes direktes Gatepaket ist von einer exakt erfuellten
Energiegleichung und von physikalischer Zulaessigkeit zu unterscheiden.
Der alte gekoppelte Ausschluss wird nicht als weiterer Fehler neu gezaehlt.
Nur diese neue eigene Review wird geschrieben; kein Root-Rechner, Test,
Altprofil, Ergebnissnapshot oder Quellenprogramm wird geaendert.

## 4. Begrenzte Code- und Testgegenreview

`scripts/audit_saturation.py` und `tests/test_saturation.py` vollstaendig
gegengelesen. Keine materiellen Fehler gefunden. Die Bindung umfasst den
neuen Vertrag und transitiv die unveraenderten Et35-/Buchvertraege. Die
cap-Auswertung lehnt eine Intervallunsicherheit an einer Integergrenze ab,
statt eine Praezisionsschwelle zu erfinden. Fuer eine zertifizierte Integer-
Zelle bildet sie die eigene floor/ceil-Obermenge und wendet t-1 ausschliesslich
bei bewiesenem t>cap an. Exakt ganzzahlige Kappen bleiben ohne pauschales
Minus1; das ist keine Implementation der ganzen Quellen-TRC-Funktion.

Die gewoehnlichen Ausgaben werden kopiert, nicht veraendert. Im Saettigungs-
zweig entsteht eine neue Besetzungsliste; der vorherige Et35-Diagnoseausgang
bleibt einschliesslich seines Stopstatus unveraendert. Direkte Summe und
Externrestidentitaet sind algebraisch korrekt, ihre Intervalle ueberlappen.
Gates, kleine Besetzungsuntergrenzen und sigma bleiben getrennte Angaben.

Selbst ausgefuehrt, jeweils erfolgreich:

```text
py -3.13 -B scripts/audit_saturation.py --check --verify-sources
  Exitcode0, H004-Hash und vier Zellen bestaetigt.
py -3.13 -B -m unittest discover -s tests -p test_saturation.py -v
  Exitcode0, 11 Tests bestanden.
```

Die synthetischen Kappentests behaupten nur das Ergebnis der deklarierten
TRC-Obermenge, keine allgemeine Quellenidentitaet TRC=floor. Der Test fuer
unveraenderte Et35-Ausgaben prueft echte Strukturkopien. Eine neue globale
Zustaendszulaessigkeit wird aus den Tests nicht abgeleitet.

Fuer einen SEPARATEN Kreuzvergleich wurde anschliessend der neue Root-
Rechner importiert. Alle12 Root-Intervalle fuer R_direct, R_identity und
sigma107b der vier Zellen enthalten die entsprechenden engeren eigenen
Fraction-Intervalle vollstaendig. N, n und die direkten Beta-Werte stimmen
exakt ueberein. Der unabhaengige Zahlenweg oben bleibt ohne diesen Import
reproduzierbar. Auch fuer den Nachtrag wurde nur diese Review bearbeitet.
