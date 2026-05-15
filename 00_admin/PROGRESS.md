# Fortschritt

## 2026-05-14

- Projektordner `Heims_Theorie` angelegt.
- Struktur fuer Quellen, Rohdaten, Notizen, Rekonstruktion, Analyse und Dokumentation erstellt.
- Erste oeffentliche Quellen identifiziert:
  - burkhardheim.de Archiv mit Heim-Unterlagen und PDFs.
  - heim-theory.com als aktueller Ordnungs- und Rekonstruktionskontext.
  - PDG 2025 Review of Particle Physics fuer Teilchendaten.
  - NIST/CODATA 2022 Werte fuer Naturkonstanten.
  - HEPData und CERN Open Data als optionale spaetere Datenquellen.
- Startdokumentation und TODO angelegt.
- Priorisierte Heim-Dateien aus dem Manifest lokal nach `01_sources/heim_primary/` geladen.
- Datei-Inventur mit Groesse und SHA256 unter `01_sources/FILE_INVENTORY.csv` erzeugt.
- Drei Agenten eingesetzt:
  - Quellen-Agent: relevante Heim-Dateien, Tabellen, XLSM-Blattbereiche und Risiken identifiziert.
  - Referenzdaten-Agent: PDG 2025 und NIST/CODATA 2022 Startwerte fuer e, mu, tau, p, n, W, Z gesammelt.
  - Critic-Agent: Guardrails gegen Ex-post-Fit, Quellenvermischung und Cherry Picking geliefert.
- Guardrails in `00_admin/GUARDRAILS.md` dokumentiert.
- PDF-Texte in `07_outputs/extracted_text/` erzeugt.
- XLSM statisch nach `07_outputs/xlsm_static_export/` exportiert.
- ZIPs in `01_sources/heim_primary_unpacked_untrusted/` entpackt, aber nichts ausgefuehrt.
- Erste Referenzwerte in `02_raw_data/reference_particle_masses_start.csv` eingetragen.
- Erste Residualtabelle in `05_analysis/initial_mass_residuals.csv` angelegt.
- Sekundaeren C-Output `output_plus_neutrino.txt` nach `05_analysis/gprog_066_output_plus_neutrino.csv` geparst.
- Formelbibliothek unter `04_reconstruction/formula_library/` angelegt.
- 11 Formel-IDs katalogisiert und fuer alle 11 Einzelformel-Dateien erstellt.
- Source-Check-Queue fuer Formelpruefung gegen PDF-Bilder angelegt.
- PDF-Seiten der 1982- und 1989-Massenformel als PNG nach `07_outputs/source_check_images/` exportiert.

## Aktueller Stand

Die sinnvolle erste Arbeitsrichtung ist die Massenformel. Fuer Rohdaten im engen Sinn brauchen wir zunaechst keine LHC-Ereignisdaten, sondern kuratierte Referenzwerte aus PDG/NIST und die behaupteten Heim-Werte aus den Heim-Quellen.

Erster Befund: e, mu, p und n sind in mehreren Heim-nahen Tabellen vorhanden. Tau, W und Z tauchen im Tabellenanhang von `Elementarstrukturen der Materie 2` auf, aber branch-/OCR-/Interpretationsstatus ist noch offen. Die sekundaere C-Implementierung liefert sehr gute Treffer fuer p/n/e, darf aber wegen spaeterer Konstanten-/Referenzdatenwahl nicht als Primaerbeleg gewertet werden.

## 2026-05-15

- Prioritaet-1-Source-Checks fuer die 1982-Massenformel begonnen.
- `HT-F-1982-MU` gegen `1982_massenformel/page-04.png` geprueft und von `raw_ocr` auf `source_checked` gesetzt.
- Review-Korrektur: Der erste Faktor in `HT-F-1982-MU` ist `fourth_root(pi)`, nicht `fourth_root(pi^3)`.
- `HT-F-1982-AUX` gegen `page-04.png` und `page-05.png` geprueft und von `raw_ocr` auf `source_checked` gesetzt.
  - `Phi` ist als sichtbarer Glyphen-Pass transkribiert, bleibt aber wegen Klammern, Exponenten und Bruch-/Produktpraezedenz high-risk fuer Normalisierung.
- `HT-F-1982-SELECTION` gegen `page-06.png` geprueft und von `raw_ocr` auf `source_checked` gesetzt.
  - `(XIII)` enthaelt im Bild rechts `alpha_3`; das bleibt als auffaellige Normalisierungsfrage markiert.
  - `(XIV)` enthaelt im Bild `b_nu_x sqrt(N(N-2))`; OCR hatte den Wurzelterm verloren.
  - Scope praezisiert: `HT-F-1982-SELECTION` deckt nur den Kern `(XIII)` bis `(XV)` ab, nicht den vollstaendigen Zustandsauswahl-Algorithmus.
- Neue offene Queue-Eintraege fuer die Fortsetzung der Auswahlregel angelegt:
  - `HT-F-1982-SELECTION-WVX` fuer `w_nu_x`, `w(1)`, `w(2)`, `a_nu_x`, `b_nu_x` und A-Matrix-Terme.
  - `HT-F-1982-SELECTION-N` fuer Resonanzordnung `N`.
  - `HT-F-1982-SELECTION-ALGO` fuer die algorithmische Quadrupelwahl und W4-Faelle.
- `formula_catalog.csv`, `SOURCE_CHECK_QUEUE.csv`, Einzelformel-Dateien und `DERIVATION_INDEX.md` synchronisiert.
- `PARAMETER_BOOK.md` mit den source-geprueften Konstanten aus dem 1982-Block ergaenzt.
- Review-Korrekturen nachgezogen: `HT-F-1982-MU` korrigiert auf `fourth_root(pi)`; `HT-F-1982-SELECTION` explizit als Core-Check abgegrenzt; `HT-F-1982-AUX/Phi` vorsichtiger als sichtbarer Transkriptionspass formuliert.
- Agenten-Workspace unter `04_reconstruction/formula_library/agent_workspace/` eingerichtet:
  - getrennte Worker-Pakete und Critic-Reviews.
  - eigene Task-Queue fuer OCR-Arbeit.
  - Protokolle fuer Worker, Critic und Integration.
  - erster Fokus: `HT-F-1982-SELECTION-WVX`, `HT-F-1982-SELECTION-N`, `HT-F-1982-SELECTION-ALGO`.
- Erster Agenten-Workflow ausgefuehrt:
  - Zwei Worker-Pakete fuer `OCR-1982-SELECTION-WVX` erzeugt.
  - Critic-Review mit Verdict `critic_ready` erstellt.
  - `HT-F-1982-SELECTION-WVX` als neue Formeldatei integriert und Queue/Katalog/Derivation-Index aktualisiert.
  - Status bleibt `not_implemented`; Slash-Bindungen, dichte Exponenten und Matrixterme brauchen Normalisierung.
- `OCR-1982-SELECTION-N` ausgefuehrt:
  - Zwei Worker-Pakete erzeugt.
  - Erster Critic-Review ergab `worker_conflict` wegen `nu x` vs. `vx`.
  - Hochaufgeloeste Seite 8 und Crops unter `07_outputs/source_check_images/1982_massenformel_hi/` erzeugt.
  - Resolver-Review ergab `conflict_resolved`; akzeptiert ist source-lokal `vx`.
  - `HT-F-1982-SELECTION-N` integriert; `sqrt(N(N-2))`, sichtbares `+ + exp[...]` und gedrucktes `(XVII)`-Label bleiben erhalten.
- `OCR-1982-SELECTION-ALGO` ausgefuehrt:
  - Zwei Worker-Pakete erzeugt.
  - Critic-Review ergab `critic_ready`.
  - `HT-F-1982-SELECTION-ALGO` integriert; korrigierter Zeilenbereich ist `395-435`.
  - Erhalten bleiben `Q = Q(0)` des `x_v`, die source-lokale `vx`-Notation, das sichtbare `K < 0` in Fall `(c)` und die `K_j`-Dezimalstellenregel aus dem `Vermerk`.
- `OCR-1982-QNUM` ausgefuehrt:
  - Zwei Worker-Pakete erzeugt.
  - Critic-Review ergab `critic_ready`.
  - `HT-F-1982-QNUM` von `raw_ocr` auf `source_checked` gesetzt.
  - Korrigiert wurden die Kronecker-Deltas `delta_{1lambda}`/`delta_{1P}`, `q = |q_x|` und der sichtbare Stack `P` ueber `2`; die Bindung der zwei unterstrichenen `Q(P)`-Zeilen an `P_1/P_2` bleibt offen.
- `OCR-1982-ALPHA` ausgefuehrt:
  - Zwei Worker-Pakete erzeugt.
  - Critic-Review ergab `critic_ready`.
  - `HT-F-1982-ALPHA` von `raw_ocr` auf `source_checked` gesetzt; korrigierter Zeilenbereich ist `117-147`.
  - Bestaetigt wurden `9 vartheta`, die reziproken Zweigwerte `alpha_(+)^-1` und `alpha_(-)^-1` sowie griechisches `beta` statt OCR-`ss`/`ß`.
  - `C_pm` bleibt nur Kontext; die spaetere `eta_kq`/`eta_qk`-Normalisierung bleibt offen.
- Nachreview der integrierten OCR-Bloecke ausgefuehrt:
  - Ein kleiner Transkriptionspunkt in `HT-F-1982-ALPHA` wurde korrigiert: die gedruckten reziproken Werte stehen nun mit Dezimalkomma.
  - Symbolregister-Hinweis fuer `alpha_plus` an die source-gepruefte Branch-Notation angepasst.
- `OCR-1982-MASS` als fehlender Agenten-Task nachgetragen und ausgefuehrt:
  - Zwei Worker-Pakete erzeugt.
  - Critic-Review ergab `critic_ready`.
  - `HT-F-1982-MASS` von `raw_ocr` auf `source_checked` gesetzt.
  - Quelle ist `page-05.png`; source-sichtbar bleiben `µα+` und das unterstrichene `G`.
- `OCR-1989-QX` als fehlender 1989-Task nachgetragen und ausgefuehrt:
  - Zwei Worker-Pakete erzeugt.
  - Critic-Review ergab `critic_ready`.
  - `HT-F-1989-QX` von `raw_ocr` auf `source_checked` gesetzt.
  - Quelle ist `1989_erweiterte_massenformel/page-02.png`; `C/k` bleibt source-sichtbare Prosa getrennt von `(B2)`, und der Stack `P` ueber `2` in `(B1)` bleibt Normalisierungsrisiko.
- `OCR-1989-MASS` ausgefuehrt:
  - Zwei Worker-Pakete erzeugt.
  - Critic-Review ergab `critic_ready`.
  - `HT-F-1989-MASS` von `raw_ocr` auf `source_checked` gesetzt.
  - `(B3)` ist image-bestaetigt als `M = µα+ [(G + S + F + Φ) + 4 q α_-]`; `(B4)` bleibt Kontext/Abhaengigkeit fuer die Alpha-Konstanten und wird nicht in die Massengleichung normalisiert.
- `OCR-1989-FPHI` ausgefuehrt:
  - Zwei Worker-Pakete erzeugt.
  - Critic-Review ergab `critic_ready`.
  - `HT-F-1989-FPHI` von `raw_ocr` auf `source_checked` gesetzt.
  - Quellen sind `page-02.png` fuer `(B5)` und `page-03.png` fuer `(B6)` bis `(B14)`.
  - Bewusst erhalten bleiben u.a. `BUW^{-1}_{N=0}`, die sichtbare Doppel-Minus-Stelle in `(B50)`, `(Q/3)` in der Selbstkopplungszeile und der fuehrende Faktor `4` innerhalb der quadrierten Klammer in `(B13)`.
- `OCR-1989-ALPHA` ausgefuehrt:
  - Zwei Worker-Pakete erzeugt.
  - Critic-Review ergab `critic_ready`.
  - `HT-F-1989-ALPHA` von `raw_ocr` auf `source_checked` gesetzt.
  - Quelle ist `1989_erweiterte_massenformel/page-09.png`.
  - Korrigiert wurde vor allem `(B59)`: die alte Kurzform `1 - C_prime = 1 - K_alpha` war strukturell falsch; erhalten bleibt die volle source-sichtbare Gleichungskette bis `= K_α`.
  - Der Vergleich mit Nistler & Weirauch 2002 bleibt Quellenkontext, kein historischer Prognosebeleg fuer 1989.
- `OCR-1989-NEUTRINO` ausgefuehrt:
  - Zwei Worker-Pakete erzeugt.
  - Critic-Review ergab `critic_ready`.
  - `HT-F-1989-NEUTRINO` von `raw_ocr` auf `source_checked` gesetzt.
  - Quellen sind `page-09.png` fuer den Abschnittsbeginn und `page-10.png` fuer `(B63)` bis Zustandsliste/Interpretation.
  - Zeilenbereich wurde von `491-552` auf `491-554` erweitert, damit der letzte Interpretationssatz vollstaendig ist.
  - Erhalten bleiben `M_ν = µα_+ (Φ + φ_0)`, die Zustandsliste `ν_1(1010)` bis `ν_5(2111)`, die barred Antistruktur `\bar{ν}_i` und die Trennung zwischen Heim-interner Neutrino-Interpretation und moderner Validierung.

Naechster harter Schritt: Normalisierungsreview fuer die source-geprueften 1982/1989-Bloecke, bevor eine Implementierung begonnen wird.
