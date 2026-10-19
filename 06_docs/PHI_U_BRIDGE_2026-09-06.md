# Phi/U: eine Formelbruecke, aber noch keine geschlossene Herleitung

Stand: 2026-09-06. Dreizehnte Etappe ab bf96741.
Frage: Liefert ein anderer Zugang die vorher fehlende Massenbeziehung,
oder wird eine Schwierigkeit unter anderen Voraussetzungen umgangen?

## 1. Ergebnis in einfachen Worten

Innerhalb des Autoren-Typoskripts H013 gibt es tatsaechlich die gesuchte
Verbindung: Ein Selbstkopplungsterm wird zuerst in der Massenformel
verwendet und spaeter im Abschnitt ueber Existenzzeiten explizit angegeben.
Heim weist selbst auf diesen Anschluss hin. Die Formelstelle ist also
nicht einfach ohne spaetere Ergaenzung geblieben.

Damit sind aber zwei verschiedene Fragen noch nicht gleich beantwortet:

- Eine fehlende Rechenvorschrift wird durch einen angegebenen Ausdruck
  ersetzt: in diesem lokalen Sinn ist die Verbindung belegt.
- Dass genau dieser Ausdruck aus den Grundannahmen datenunabhaengig folgt,
  ist auf den geprueften Seiten nicht gezeigt. Heim nennt bestimmte
  Konstanten selbst als empirisch angepasst und erwartet weitere Korrekturen.

Es handelt sich daher um eine explizite, teilweise empirisch bestimmte
Formelbruecke mit offenem Herleitungsstatus. Kein Beweis einer vollstaendigen
Theorie, aber auch kein Beleg, dass der Autor die offene Stelle ignorierte.
Die Reihenfolge der Abschnitte ist belegt; eine zeitliche Reihenfolge
der undatierten Manuskriptfassungen ist damit nicht bewiesen.
Die explizite Angabe bedeutet zudem noch keine eindeutige numerische
Implementierung: Das unten beschriebene U-Vorzeichen bleibt offen.

## 2. Was Heim unter Selbstkopplung versteht

H013 Druck13/14, PDF14/15, verbindet K mit den inneren Zonen p und sigma
und mit der zeitlichen Ausdehnung x4 eines Grundzustands. In(5e) steht

    phi = N4*K*delta(N),  delta(0)=1,  delta(N>0)=0.

Die Masse enthaelt phi ueber den Summanden F aus(5c). Beim Lebensdauer-
abschnitt Druck29/30, PDF32/33, kuendigt der Autor eine explizite Bestimmung
von phi an und gibt sie in(21b) zusammen mit U(21b1) an. Druck32/PDF35
erlaeutert, dass damit zugleich eine numerische Massenrechnung moeglich sei.

Das ist Heims behaupteter physikalischer Weg. Nicht gefunden wurden dort
die Zwischenschritte, welche aus der zeitlichen Strukturbeschreibung gerade
die vollstaendige21b-/U-Form mit allen Koeffizienten erzwingen.

Die Auswahl N=0 ist wichtig: Im H013-Massenabschnitt ist der Selektor
bereits Teil von phi; H007(B5) schreibt stattdessen phi*delta(N).
Der N4-Faktor steht bereits in der expliziten21b-Form. Den gesamten
Ausdruck nochmals mit N4 zu multiplizieren waere keine Quellenauswertung.
Bei N=0 und N4 ungleich null laesst sich K algebraisch als phi/N4
zurueckgewinnen. Das ist keine unabhaengige Dynamikherleitung von K.

## 3. Explizite Parameterfunktion, kein erzwungener Rechenkreis

Nach der bestehenden B49-Normalisierung laesst sich die lokale Struktur
mit eigenen Hilfsnamen schreiben als

    A_phi = N4*p^2/(1+p^2) * (sigma+Q_sigma)/sqrt(1+sigma^2),
    E_phi = P*(P-2)^2 * [1+kappa*(1-q)/(2*alpha*vartheta)]
            * (pi/e)^2 * sqrt(eta12) * (Q_m-Q_n),
    R_phi = (P+1)*binom(Q,3)/alpha,

    phi = A_phi*[fourth_root(2)-4*B*U/W0] + E_phi - R_phi.

W0 steht fuer W_N=0. Die Inverse betrifft nur W, nicht den ganzen BUW-
Ausdruck. B=3H/[k^2(2k-1)] ist eine Hilfsgroesse, NICHT die Baryonenziffer.
Grosses Phi, kleines phi, kappa und die verschiedenen K bleiben getrennt.

Die explizite rechte Seite benutzt kein gemessenes M oder T. Fuer
festgelegte Zustandsparameter und Koeffizienten ist der lokale Rechenweg

    Zustandsparameter/Koeffizienten -> B, U, W0, N4 -> phi
                                                        -> F_mass -> M
                                                        -> y ---------> T
                                                                     ^
                                                           M --------|

Dabei sind F_mass aus H007(B5)/H013(5c) und F_time aus H007(B52)/H013(21c)
verschiedene Ausdruecke trotz gleichen Buchstabens in der Quelle. F_time
steht im Lebensdauer-Zaehler y; F_mass ist ein Massenbeitrag. Eine
Gleichsetzung wuerde eine fremde, moeglicherweise scheinbar zirkulaere
Rechnung erzeugen.
Ebenso ist das H013-y aus(13e)/(13e1) zur Bestimmung von W0 lokal vom
spaeteren y aus(21a) zu trennen. H007 nennt die erste Groesse y'.

W0 ist im expliziten Hilfsapparat B22-B31 eine vorgelagerte Parameter-
funktion. Das beweist keine Kreisfreiheit des ganzen Theorieprogramms:
B15 verwendet M0 in einer Zonenobergrenze, die vollstaendige Zustands-
auswahl ist hier nicht rekonstruiert, und historische Kalibrierung kann
Messdaten einbringen, ohne M oder T als Laufzeiteingabe zu enthalten.

## 4. Was sich schon exakt pruefen laesst

Bei festgehaltenem Rest ist phi affin in U:

    d(phi)/dU = -4*A_phi*B/W0.

Der direkte H007-Massenbeitrag ist

    M_phi = mu*alpha_plus*phi*delta(N).

Fuer N=0 ist sein Koeffizient mu*alpha_plus; fuer N>0 verschwindet dieser
direkte Beitrag. Das ist keine Aussage ueber jede indirekte Abhaengigkeit
in einer vollstaendigen Resonanzrechnung.

Auch T muss nicht einfach proportional zu phi sein: phi veraendert sowohl
y im Zaehler als auch M im Nenner. Mit eigenem J=(-1)^s*(b1+b2/W0)
lautet der Zaehler y=F_time*[J+(1+J)*phi]. Die Voraussetzungen und die
formale Weitergabe stehen im unabhaengigen Mathematikreview; keine
gemessene Lebensdauer oder Teilchenmasse wird dafuer eingesetzt.

Fuer N0, m_phi=mu*alpha_plus und festgehaltene uebrige Groessen folgt
mit eigenem phi-unabhaengigen Vorfaktor K_time einschliesslich F_time:

    T(phi) = K_time*[J+(1+J)*phi]/[M_rest+m_phi*phi],
    dT/dphi = K_time*[(1+J)*M_rest-m_phi*J]/[M_rest+m_phi*phi]^2.

Diese formale Diagnose fuehrt nur den direkten phi-Beitrag der Masse
mit. Ohne Vorzeichenkenntnis folgt kein allgemeines Monotoniegesetz;
ein verschwindender Nenner ist ausgeschlossen. Anders als in Etappe12
wird hier M nicht insgesamt festgehalten. Die beiden Diagnosen duerfen
nicht als gleiche Variation ausgegeben werden.

### Der alte B50-Vorzeichenblocker

H007 hat an einer U-Stelle zwei Minuszeichen, einmal auf derselben Zeile,
einmal ueber einen Zeilenumbruch verteilt. Die neue H013-Stelle zeigt
ebenfalls Minuszeichen an Zeilenende und Folgezeilenanfang. Vergleichbare
Fortsetzungszeichen auf derselben Manuskriptseite machen eine einfache
Subtraktion plausibel. Sie liefern aber kein eindeutig belegtes Erratum
fuer die H007-Fassung. Wir behalten den alten Blocker und die Originale.

Nur fuer eine ausdrueckliche Diagnose definieren wir U_plus/U_minus mit
vorangestelltem Plus- bzw.Minuszeichen vor dem fraglichen Summanden.
Dessen Wert kann seinerseits beide Vorzeichen haben. Dann ist exakt

    U_plus - U_minus
      = 2 * 2^Z/eta_qk^2 * (k-1) * 4*pi/fourth_root(2) * (P-Q)*(1-q).

Somit koennen Rechnungen bei k=1, P=Q oder q=1 die beiden Lesarten
ueberhaupt nicht unterscheiden. Auch die Weitergabe an phi kann null
sein, etwa bei p=0 oder sigma=-Q_sigma. Das betrifft den Unterschied
der Varianten, nicht das Verschwinden von ganz U, phi, M oder T.
Alle Ausgangsnenner muessen weiterhin definiert sein: 0*(1/0) ist keine
zulaessige Auswertung.

Ein konkreter begrenzter Zahlencheck benutzt das bereits untersuchte
Delta-Kontexttupel k=2, P=Q=3, kappa=0, q=2. Hier sind Z=8 und die
gemeinsame U-Klammer 9-3+9=15. Beide Vorzeichen liefern daher

    U = 3840/eta22^2 = 5410.905148099404631131279413983334...

Dieser Test bestaetigt die algebraische Auswertung, entscheidet aber
gerade NICHT das Vorzeichen. U ist eine Hilfsgroesse, keine Masse oder
Lebensdauer. W0, phi, Zonenbesetzungen und M/T wurden fuer dieses Tupel
nicht vollstaendig berechnet. Keine physikalische Zulaessigkeit aus
diesem Einzeltest ableiten; der fruehere Buch-Auswahlbefund bleibt bestehen.

## 5. Fortschreibbarkeit ist eine ausdrueckliche Autorenabsicht

H013 Druck37/PDF40 beschreibt nicht nur unbestimmte Restgroessen z(N)
und T_N. Heim erwartet dort, dass spaetere Untersuchungen rueckwirkend
Resonanzbeziehungen korrigieren koennten. Auch die geplante Beschreibung
von Wirkungsquerschnitten koennte Korrekturen an Phi und phi erforderlich
machen. Das passt zur Nutzeridee einer fortschreitenden Arbeit.

Im selben Zusammenhang nennt Heim aber die drei empirisch angepassten
Konstantenformen

    fourth_root(2),  (pi/e)^2,  4*pi*fourth_root(1/2).

H007 Druck20/PDF11 uebernimmt diese Einschraenkung. Feste Zahlen aus pi/e
sind deshalb nicht automatisch datenunabhaengig abgeleitete Zahlen.
Der genaue Anpassungsdatensatz, das Verfahren und die verbleibende
Vorhersagefreiheit muessen vor einem spaeteren empirischen Test geklaert
werden. Daraus folgt noch kein gesonderter Fit von eta22 oder Alpha.

Als getrennter Kontext nennt H004 II335/PDF341 eine heuristische
Bestimmung von A_im/A_66 aus Grundzustandsdaten und die Hoffnung auf
spaetere Bestaetigung mit Y_k=1. Das ist nicht automatisch derselbe
Gegenstand wie phi/U. Die explizite phi-Form schliesst diese Buchluecke
deshalb nicht schon durch aehnliche Zielsetzung.

## 6. Weshalb wir keine Fassungen zusammenkopieren

Am Massenanschluss stehen weitere sichtbar verschiedene Ausdruecke:

| Stelle | H013 | H007 |
| --- | --- | --- |
| Massenklammer | (4): mu*[(G+S+F+Phi)*alpha_plus+4q*alpha_minus] | B3: mu*alpha_plus*[(G+S+F+Phi)+4q*alpha_minus] |
| Erster n-Term in F_mass | (5c) mit N1 | B5 ohne N1 |
| Grundzustandsselektor | In phi=N4*K*delta aus(5e) | phi*delta im Massenbeitrag B5 |

Es sind lokale Fassungsunterschiede, noch kein Beweis, welche Fassung
richtig oder frueher ist. Wir setzen auch gleichnamige Hilfskonstanten
nicht ungeprueft gleich. Die alten Massen-Transkriptionen und Alpha-
Rechenprofile werden nicht aus diesen Teilbeobachtungen ueberschrieben.
Der gemeinsame direkte phi-Koeffizient beiN0 bleibt davon abgegrenzt.

## 7. Bilanz und Fortsetzung

FIND-023 dokumentiert die positive Formelbruecke, ihren Kalibrierungs-
und Herleitungsstatus sowie die bedingte Algebra. FIND-024 haelt die
neuen lokalen Massen-Fassungsgrenzen fest. Keine zwei neuen behaupteten
physikalischen Fehler und keine Gesamtwiderlegung.

Die bisherige Frage wird damit genauer: Nicht mehr nur, wo phi angegeben
ist, sondern wie seine spezifische Form begruendet und kalibriert wurde.
Die erneute reine Suche nach B49/BUW/2^Z ist nicht erforderlich. Fuer den
alten Vorzeichenknoten braucht es neue Editions- oder Rechenbelege, nicht
eine nach Trefferqualitaet ausgewaehlte Lesart.

Naechste begrenzte Einheit: Gamma/Q_N und die Anregungs-/Auswahlgrenze
versionsgebunden rekonstruieren. Dabei Quellen-Gamma/Q_N nicht ohne
Beleg mit einer modernen Zerfallsbreite gleichsetzen. Anschliessend
die Abhaengigkeitskarte und verbleibenden Voraussetzungen zu einer
Verstaendnisbilanz zusammenfuehren. Vor einem vollstaendigen Massenfall
muessen dessen Fassung, Inputs, Selektoren und offenen Lesarten feststehen.

Quellen-/Pruefspur: `03_notes/PHI_U_SOURCE_CONTEXT_2026-09-06.md` und
drei PHI_U-Reviews unter `04_reconstruction/alpha_audit/reviews/`.
Ausfuehrbare unabhaengige Algebra-/Konvergenzkontrollen im Mathematikreview.
Pruefergebnisse, Checkpoints und genauer Wiedereinstieg in `00_admin/RESUME.md`.

Root hat alle drei Codebloecke separat ausgefuehrt:96 exakte rationale
Selektor-/Weitergabefaelle und sechs Quotientendifferenzen bestehen;
eta22/U bei80/120Stellen unterscheiden sich maximal absolut um weniger
als4.77e-77. Das ist eine Konvergenzkontrolle, keine Intervallzertifizierung.
Acht bisherige Snapshot-/verfuegbare Quellhashchecks,98 Softwaretests und
Registervalidator bestehen. Alte Rechner, Inputs, Snapshots, Tests und49
Normalisierungen bleiben unveraendert. Die unabhaengige Schlussgegenlesung
hat Formeln und Reichweite akzeptiert; Vorzeichenwortlaut wurde praezisiert.
