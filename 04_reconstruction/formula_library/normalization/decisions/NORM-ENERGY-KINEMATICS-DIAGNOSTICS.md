# NORM-ENERGY-KINEMATICS-001

Stand: 2026-09-06. Begrenzte Implementierungsfreigabe nach Quellbildkontrolle
und abgeschlossener unabhaengiger Rechnerreview. Kein Rechenfehler gefunden;
empfohlener unabhaengiger Buchindex-Regressionstest zusaetzlich aufgenommen.

## Quellen und Bedeutungsgrenze

EDM1 (3. geaenderte Auflage 1998), Druck81/PDF88 und Druck288/PDF294:
m=m0/sqrt(1-beta^2), p=mv und positive Wurzel E=pc aus
E^2=(m^2-m0^2)c^4. Gross-/Kleinschreibung im Rechner vereinheitlicht.
EDM2 (2. unveraenderte Auflage 1996), Druck300/301/PDF306/307:
beta=v_H/c=alpha; E_k=beta*m*c^2; mc^2=ch/lambda_H;
lambda_H=2*pi*r_H; y=r_H*sqrt(1-beta^2).

Die aus BandI uebertragene m=gamma*m0-Lesart fuer EDM2 ist eine explizite
bedingte Verbindung, keine stillschweigende Definition der Autorenabsicht.
Der Rechner nennt die Energie `source_pc`, NICHT Standard-Bewegungsenergie.
`beta` im Rechner bezeichnet nur v/c, nicht Heims andere Beta-Symbole.
`m0` ist die Ruhemasse, nicht ein berechneter Tabellenwert. Keine Masse als Input.

## Erlaubte eigene Vergleichskonstruktionen

Setze s=sqrt(1-beta^2), E=f*mc^2, lambda=g*h/(mc), r=lambda/(2*pi), y=r*s.
Aus e^2(1-C)=4*pi*epsilon0*y*E folgt K=alpha_prime*(1-C)=g*f*s.

| Profil | f | g | K(beta) | Status |
|---|---|---|---|---|
| source_pc | beta | 1 | beta*s | bedingte Quellenrekonstruktion |
| kinetic_energy_only | 1-s | 1 | s*(1-s) | eigener ungefiteter Energieersatz |
| kinetic_energy_and_dB | 1-s | 1/beta | s*(1-s)/beta | zwei eigene Ersetzungen |

T=(m-m0)c^2 ist ein getrennt benannter Vergleich; historische Standardreferenz
Einstein1905, Druck920. Eine alternative Wellenlaenge h/p entspricht der
Beziehung aus EDM1(H1), darf aber nur dann mit lambda_H gleichgesetzt werden,
wenn dieselbe Welle/Bezugsbeschreibung nachgewiesen ist. Die zwei anderen
Profile sind weder Heim-Formeln noch physikalisch gepruefte Reparaturen.

Rechendomäne: finite 0<beta<1. Null/Einspunkt wegen Masse/Wellenlaenge nicht
zulaessig; Grenzwerte nur in der Erklaerung. Stabile Auswertung:
s=sqrt((1-beta)*(1+beta)), 1-s=beta^2/(1+s). Der Rechner beansprucht keine
relative Genauigkeit der sehr kleinen Differenz eines gerundeten s zu 1.

## Inputs und Outputs

Feste dimensionslose Lehrbeispiele beta=0.001,0.01,0.1,0.6,0.9 sowie der
kleine, NICHT aus Messdaten bezogene Buchzweig bei Y3=1. Dieser wird aus
mathematischem pi, Buch(98)-eta_qk mit q=1,k=1/2, BandI-vartheta und
K=9*vartheta*(1-A1*A2)/(2*pi)^5 berechnet. Keine Zielwerte, keine Fits.
Die alte 1982-Quellnotation und alle vorhandenen Snapshots bleiben unberuehrt.

Outputs sind ausschliesslich dimensionslose Energie-, Wellenlaengen- und
Laengenverhaeltnisse sowie die drei Schliessungsfunktionen. Laengeneinheit
L0=hbar/(m0*c); diese Normierung bestimmt keine gemessene Atomgroesse.
Moderne Konstantentabellen oder Hardwaremessungen sind nicht erforderlich.

Script: `scripts/audit_energy_kinematics.py`.
Snapshot: `05_analysis/energy_kinematics_diagnostics.json`.
Review: `04_reconstruction/alpha_audit/reviews/ENERGY_KINEMATICS_MATH_REVIEW_2026-09-06.md`.
