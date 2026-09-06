# BOOK-ENERGY-ORDER-001: Ordnung der Energiegrenzen

Stand:2026-09-06. Status: bestaetigter lokaler Quellenkonflikt fuer einen
nichttrivialen positiven kinetischen Anteil; historische Korrektur offen.
Dies ist eine neue Buchfrage, kein weiterer Eintrag im alten Massenkatalog.

## Quellenlesung

EDM2, PDF305/306 = Druck299/300, visuell durch Quellenagent und Hauptagent
geprueft. Die Quelle druckt:

```text
W <= X <= V, 0 <= E <= E_k                          [Druck299]
-E_k = integral(W to V, dX) = V-W = V*(1-C)         [Druck300]
W=V*C; 4*pi*epsilon0*y*V=-e_minus^2                 [Druck300]
```

Es liegt keine bloss aus OCR abgeleitete Ungleichungsrichtung vor.
Quelle/Hash sind im bestehenden Alpha-Quellenprofil dokumentiert.

## Kurzer algebraischer Nachweis

Aus W<=V folgt V-W>=0. Aus E_k>=0 folgt -E_k<=0. Sind beide Groessen gleich,
koennen sie nur null sein: E_k=0 und W=V; damit auch X=W=V und E=0.
Fuer den spaeter behandelten nichttrivialen Fall E_k>0 sind diese Aussagen
unvereinbar. Der Beweis benoetigt weder einen modernen Messwert noch eine
Gleitkommarechnung.

Zusaetzliche Kontrolle im gewaehlten Buchfall: V<0, Y3=1 und0<A1*A2=C<1
geben V<W=VC<0, also die umgekehrte gedruckte Ordnung. Die Voraussetzung
E_k>0 wird im weiteren Modell durch positive Geschwindigkeit, positive
Masse und E_k=m*v_H*c verwendet; diese Energiebeziehung wird durch den
vorliegenden Ordnungscheck nicht physikalisch gerechtfertigt.

## Eigener minimaler Korrekturkandidat EC-ENERGY-01

Nur als unsere getrennte Version koennte `V <= X <= W` statt `W <= X <= V`
gesetzt werden. Dann waere fuer einen Weg von X=W nach X=V:

```text
integral(W to V,dX)=V-W<0
E_k=W-V=-V*(1-C)>0.
```

Damit bleiben die anschliessend verwendete Gleichung E_k=-V*(1-C) und
deren Weiterverwendung zur gedruckten Alpha-Gleichung unveraendert. Diese
lokale Ordnungsreparatur aendert deshalb nicht die bereits berechneten
Alpha-Zweige und kann deren Druckwiderspruch nicht beheben. Sie begruendet
auch nicht den Korrelationsfaktor, die Energie-/Wellenlaengenrelationen
oder die Physik des Modells.

Autorenabsicht unbekannt: Ebenso koennte ein historischer Fehler am
Integralvorzeichen, den Grenzen oder einer unerklaerten Konvention liegen.
Keine dieser Varianten wird ohne Kennzeichnung in die Quelle geschrieben.

## Reviews und naechste Aufgabe

- Glyphen-/Kontextkontrolle:
  `reviews/CORRELATION_CHAIN_REVIEW_2026-09-06.md`, Nachtrag.
- Unabhaengige bedingte Algebra:
  `reviews/ENERGY_ORDER_MATH_REVIEW_2026-09-06.md`.

Naechste Aufgabe: Energiebezeichnungen, m(v_H), E_k=m*v_H*c und
lambda_H=2*pi*r_H in ihren frueheren Definitionen rueckverfolgen. Erst dann
ueber lokale physikalische Konsistenz und moegliche weitere Korrekturen urteilen.
