# NORM-CONFIGURATION-SELECTION-001

Stand2026-09-06. Isolierte Diagnose von EDM2 Druck265-269, besonders (98a).
Quellenbilder durch Root und Quellenreview kontrolliert; unabhaengige
Algebra vor Implementierung gerechnet. Unabhaengige Implementierungsreview
abgeschlossen;1057 Ergebnis-/Bool-Felder gegen alternative Rechnung geprueft.

## Festgelegte Lesung und Domaene

q,k sind fuer die Auswahl positive ganze Zahlen. Der eta-Helfer laesst
zusaetzlich q=0 und k=0 als formale Grenzfaelle zu, nicht als positive innere
Konfigurationen. eta_qk=pi/(pi^4+q^4*(4+k))^(1/4); eta_q=eta_q0; eta=eta_10.
Alle hier ausgewerteten Verhaeltnisse und L,Delta,k sind dimensionslos.
L=4 und Delta=k/4 sind Quellannahmen, keine bewiesene Quantisierung.
Der Ladungsquotient aus der vierten Wurzel bezeichnet den positiven Zweig
(gleiches Ladungsvorzeichen) bzw. den Betrag, nicht eine Bestimmung des Vorzeichens.

Mit a=eta_q,e=eta,x=1/eta_qk gilt laut Druck268:
V1=a*x; V2=(1+sqrt(a))^2/(4e); Q1=a^2/sqrt(e); Q2=sqrt(e).
Q2 traegt KEIN q unter der Wurzel, hochaufloesend dreifach nachgelesen.
V/Q hier sind Verhaeltnisse, nicht unbemerkt die Energien der H-Bilanz.

## Drei getrennte Aussagen, keine gewaehlte Reparatur

1. Vorgelagerte Identifikation F_i=V_i,G_i=Q_i bei F2-F1+G2-G1>0:
   V1+Q1<V2+Q2, also x<D_q.
2. Gedruckte V/Q-Ungleichung: V1+Q1>V2+Q2, also x>D_q.
3. Gedruckte Folgerung: x<B_q, also k<u_B(q).

B_q=(1+sqrt(a))^2/(4ea)+(1-a/e)*sqrt(e).
D_q=(1+sqrt(a))^2/(4ea)+(1/a-a/e)*sqrt(e).
D_q-B_q=sqrt(e)*(1/a-1)>0 fuer q>=1.
u_R(q)=(pi/q)^4*(R_q^4-1)-4 fuer positives R_q.

Die Diagnose rechnet alle drei Aussagen getrennt, kennzeichnet D als
unsere direkte Umformung und ersetzt keine Quelle oder vorhandene Formel.
Die gedruckten Intervalle fuer u_B werden unabhaengig getestet. Ein
endlicher Scan ist allein kein Beweis fuer alle q; dazu dient ein getrennter
rationaler Schrankenbeweis fuer q>=5 (Bericht und Tests).

## Implementierungsgrenzen

Mathematisches pi, Decimal40-200 Stellen, Konvergenz80/120. Auswahlfaelle
q1..10,k1..20; alle strikten Grenzen bleiben strikt, keine zusaetzliche
Rundung auf Ausgabestellen vor der Entscheidung. Decimal-Grundoperationen
runden weiterhin; der Abstandsschutz ist keine Intervallzertifizierung.
Numerisch unaufloesbare Vergleiche werden abgewiesen.
Keine Messwerte, keine Parameteranpassung. Integer-Helfer verweigern bool,
Float und Strings; Hilfsgroessen muessen im expliziten positiven Bereich liegen.
Ergebnisdatei ist nur eine Diagnose, kein vollstaendiger Massenrechner.

Script scripts/audit_configuration_selection.py; Tests test_configuration_selection.py;
Snapshot05_analysis/configuration_selection_diagnostics.json. Alle sechs
bisherigen Rechner, Inputs, Snapshots und Originaltranskriptionen bleiben
unveraendert. Katalogstatus der14Formelgruppen wird nicht erweitert.
