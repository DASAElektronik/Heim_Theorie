# Quellenvertrag: Elektron-N0 im fotografierten FORTRAN

2026-10-18, Etappe42. Ausgang b2c1113 plus uncommittierte Etappe41;
deren Dateien und alle älteren Profile bleiben erhalten. Ein Agent.

Auftrag: den negativ geladenen E-Grundzustand des H015-Listings aus
GINIT, MAIN, GBASE, GSTRUC, ETAQK und GMASS rekonstruieren und mit
seinem Ausdruck vergleichen. Kein fremdes Programm ausführen, keine
modernen Messdaten oder H010-Ersatzkonstanten. PDF-Lesung nach PDF-Skill:
vollständige relevante Fotoseiten, Ausschnitte nur zur Detailkontrolle.

## Vor der neuen Zahlenauswertung fixiert

- H015 PDF18/4: K=PG=QG=1, KAPPA=0, EPS=1, IX=2; daraus CS=0,
  QX=-1, KQ=1. IN=N=0 ist der erste Schleifendurchlauf. MAIN ruft
  GINIT, GBASE, GSTRUC und GMASS in dieser Reihenfolge auf.
- Konstanten exakt wie Etappe41; insbesondere PI=3.1415926535,
  XI=1.61803399, ALFA=1/137.03602725, BETA=1/1.00001411,
  FAKMEV=0.05609545e31. Keine mathematische-pi-/Goldenschnitt-Ersetzung.
- ETAQK aufPDF24: d=PI/(PI^4+5)^(1/4) für KQ=K=1;
  GINIT-ETA=PI/(PI^4+4)^(1/4) getrennt halten.
- GBASE PDF22/7: Q=(3,3,2,1), ALF1=(1+sqrt(d))/2, ALF2=1/d;
  ALF3=1-ALFA*XI^3*(1+sqrt(d))/(3*d^3)
  -2*XI*d/EBN*((1-sqrt(d))/(1+sqrt(d)))^2.
  Beide Zweige liefern TEMP1=TEMP2=1, damit WGX=GKQ.
- GSTRUC PDF23: FN=0, W1=GKQ. Erste drei Ganzzahlen und ihre
  Abstände nachrechnen, nicht aus dem Ausdruck übernehmen. Danach
  W4=exp(-1/3) und -3log(W4)=1 exakt, sofern K1..3=(3,3,2).
  Diesen letzten Schritt analytisch behandeln und rohe Dezimalabschneidung
  separat dokumentieren; keine allgemeine Epsilon-Korrektur hinzufügen.
- GMASS PDF24: KGH=4*(a1*K1^2*(1+K1)^2/4
  +a2*K2*(2*K2^2+3*K2+1)/6+a3*K3*(K3+1)/2+K4).
  Für diesen Zustand und n1=0 reduziert FIG auf
  (1-ALFM/ALFP)*[12*sqrt(d)/PI*(1-ALFA/3)
  *(1+4*PI*ALFA/ETA^(3/2))+8*ALFA/XI^2]+4*ALFM/ALFP.
  Vergleich mit separater Produktform aus der fotografierten FIG-Zeile.
  AM=AMU*FAKMEV*ALFP*(KGH+FIG), zusätzlich kg ausweisen.
- Bekannter Vergleichswert aufPDF27: 0.51100326Q+00, daneben
  K=(3,3,2,1), n=(0,0,0,0). Ausdruck war vor Rechnung bekannt;
  keine blinde Vorhersage. Angenommene halbe letzte Druckeinheit5e-9.
- Decimal60/90-Stabilität, unabhängige algebraische/Umrechnungsprüfung,
  eigene binary64-Gegenrechnung. Keine IBM-REAL*16-Emulation oder
  numerische Garantie eines historischen Compilers behaupten.

Ausgabe: separater Input, eigener begrenzter Rechner, Ergebnis, sinnvolle
Tests, Quellenumfang und Bericht. Alte51 Befunde semantisch erhalten;
neuen Befund nur nach Ergebnis. H004-Kalibrierung und F_S-Provenienz bleiben
separate Fragen. Keine neue Commit-/Push-Anweisung in diesem Auftrag.
