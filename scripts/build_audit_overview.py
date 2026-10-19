"""Build the dated two-page overview and three SVG figures (ReportLab only).

Run from any directory: py -3.13 -B scripts/build_audit_overview.py
Reads the checked diagnostic JSON; does not change the research calculation.
"""
from pathlib import Path
import json
import reportlab
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics import renderPDF, renderSVG
from reportlab.graphics.shapes import Drawing, Rect, Line, Polygon, String, Circle
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "07_outputs/figures"
PDF = ROOT / "output/pdf/Heim_Audit_Ueberblick_2026-10-18.pdf"
INK = HexColor("#193344")
MUTED = HexColor("#526677")
TEAL = HexColor("#087f83")
OCHRE = HexColor("#ac6421")
PALE = HexColor("#edf4f5")
GRID = HexColor("#d7e1e5")
FONT, BOLD = "AuditSans", "AuditBold"
WIDTH, HEIGHT = 595.276, 841.89
MARGIN, CONTENT = 43, 509


def fonts():
    folder = Path(reportlab.__file__).parent / "fonts"
    pdfmetrics.registerFont(TTFont(FONT, str(folder / "Vera.ttf")))
    pdfmetrics.registerFont(TTFont(BOLD, str(folder / "VeraBd.ttf")))
    pdfmetrics.registerFontFamily(FONT, normal=FONT, bold=BOLD, italic=FONT, boldItalic=BOLD)


def label(d, x, y, text, size=10, color=INK, bold=False, anchor="start"):
    d.add(String(x, y, text, fontName=BOLD if bold else FONT,
                 fontSize=size, fillColor=color, textAnchor=anchor))


def box(d, x, y, width, title, lines, color=TEAL):
    d.add(Rect(x, y, width, 78, rx=7, ry=7, fillColor=PALE, strokeColor=GRID))
    d.add(Rect(x, y+74, width, 4, fillColor=color, strokeColor=None))
    label(d, x+12, y+53, title, 10, color, True)
    for i, text in enumerate(lines):
        label(d, x+12, y+32-i*15, text, 9)


def arrow(d, x1, y1, x2, y2, color=TEAL):
    d.add(Line(x1, y1, x2, y2, strokeColor=color, strokeWidth=1.7))
    if abs(x2-x1) > abs(y2-y1):
        d.add(Polygon([x2,y2,x2-6,y2+3,x2-6,y2-3], fillColor=color, strokeColor=None))
    else:
        d.add(Polygon([x2,y2,x2-3,y2+6,x2+3,y2+6], fillColor=color, strokeColor=None))


def dependency():
    d = Drawing(CONTENT, 255)
    label(d, 0, 239, "Was geht hinein, was kommt heraus?", 13, INK, True)
    box(d, 0, 132, 148, "MESSWERTE", ["Elektronenmasse, Ladung", "hbar und c"])
    box(d, 180, 132, 148, "MODELL + RÜCKWEG", ["Gleichungen (29), (112)", "D_e bedingt fest"])
    box(d, 360, 132, 148, "ABGELEITET", ["gamma, epsilon0, mu0", "nach H004, Seite 349"])
    arrow(d, 151, 171, 176, 171)
    arrow(d, 331, 171, 356, 171)
    arrow(d, 434, 128, 434, 105)
    box(d, 180, 20, 328, "ELEKTRON ERNEUT BERECHNET", [
        "Rückgabe des Ankers: kein zusätzlicher unabhängiger Test.",
        "Andere Größen benötigen einen getrennten Vorhersagetest."], OCHRE)
    label(d, 0, 85, "D_e fasst den", 9, MUTED)
    label(d, 0, 71, "dimensionslosen", 9, MUTED)
    label(d, 0, 57, "Elektronenfaktor zusammen.", 9, MUTED)
    label(d, 0, 0, "Eigene Darstellung nach H004, Druck 349/371. Keine vollständige Theorieübersicht.", 8, MUTED)
    return d


def interval_plot(title, rows, limits, ticks, axis_title, note):
    d = Drawing(CONTENT, 190)
    label(d, 0, 174, title, 12, INK, True)
    left, right, bottom, top = 190, 496, 53, 145
    x = lambda value: left+(value-limits[0])/(limits[1]-limits[0])*(right-left)
    for tick in ticks:
        d.add(Line(x(tick), bottom, x(tick), top, strokeColor=GRID, strokeWidth=.6))
        label(d, x(tick), 37, str(tick).replace(".", ","), 8, MUTED, anchor="middle")
    d.add(Line(left, bottom, right, bottom, strokeColor=MUTED, strokeWidth=.8))
    for i, (name, detail, low, high, center, color) in enumerate(rows):
        y = 129-i*51
        label(d, 0, y+1, name, 9, color, True)
        label(d, 0, y-13, detail, 8, MUTED)
        d.add(Line(x(low), y, x(high), y, strokeColor=color, strokeWidth=3))
        for value in (low, high):
            d.add(Line(x(value), y-5, x(value), y+5, strokeColor=color, strokeWidth=1.3))
        d.add(Circle(x(center), y, 3.4, fillColor=color, strokeColor=white, strokeWidth=.7))
    label(d, (left+right)/2, 20, axis_title, 8, MUTED, anchor="middle")
    label(d, 0, 0, note, 8, MUTED)
    return d


def charts(data):
    c = float(data["historical_c_m_s"])
    clo, chi = map(float, data["c_implied_rounding_range_m_s"])
    cplot = interval_plot("Lichtgeschwindigkeit: Druckwerte sind vereinbar", [
        ("Aus epsilon0 und mu0", "Angenommene Druckrundung", clo-c, chi-c,
         float(data["c_implied_m_s"])-c, TEAL),
        ("PDG 1974", "Messwert +/- 1 Standardabweichung", -1.2, 1.2, 0, OCHRE),
    ], (-100, 75), [-100,-50,0,50], "Abweichung von 299 792 458 m/s [m/s]",
       "Rundungsbereich und Messunsicherheit sind unterschiedliche Angaben.")
    e = float(data["source_tokens_SI"]["e"])
    ppm = lambda value: (float(value)/e-1)*1e6
    plo, phi = map(ppm, data["printed_charge_rounding_range_C"])
    elo, ehi = map(ppm, data["eq29_charge_rounding_range_C"])
    eplot = interval_plot("Elementarladung: kleine bedingte Abweichung", [
        ("Gedruckte Ladung", "H004, Seite 371: Rundungsbereich", plo, phi, 0, OCHRE),
        ("Aus Gleichung (29)", "H003-Brücke + H004-Endkonstanten", elo, ehi,
         ppm(data["eq29_charge_C"]), TEAL),
    ], (-.5, 1.2), [-.5,0,.5,1.0], "Abweichung von 1,602188 x 10^-19 C [ppm]",
       "Beide Balken: angenommene Druckrundung. Endpunkte numerisch ausgewertet.")
    return cplot, eplot


def paragraph(c, text, top, size=10, color=INK, width=CONTENT, bold=False):
    style = ParagraphStyle("body", fontName=BOLD if bold else FONT,
                           fontSize=size, leading=size*1.45, textColor=color)
    p = Paragraph(text, style)
    _, height = p.wrap(width, HEIGHT)
    p.drawOn(c, MARGIN, top-height)
    return top-height


def heading(c, kicker, title, subtitle, page):
    c.setFillColor(TEAL)
    c.rect(MARGIN, HEIGHT-43, 32, 4, stroke=0, fill=1)
    paragraph(c, kicker, HEIGHT-57, 9, TEAL, bold=True)
    paragraph(c, title, HEIGHT-82, 23, INK, bold=True)
    paragraph(c, subtitle, HEIGHT-124, 10, MUTED)
    c.setStrokeColor(GRID)
    c.line(MARGIN, 43, WIDTH-MARGIN, 43)
    paragraph(c, "HEIM-AUDIT  |  18.10.2026  |  Etappen 39 und 40", 32, 8, MUTED)
    c.setFont(FONT, 8)
    c.setFillColor(MUTED)
    c.drawRightString(WIDTH-MARGIN, 20, f"{page} / 2")


def build():
    fonts()
    FIGURES.mkdir(parents=True, exist_ok=True)
    PDF.parent.mkdir(parents=True, exist_ok=True)
    data = json.loads((ROOT / "05_analysis/constants_anchor_results.json").read_text(encoding="utf-8"))
    flow = dependency()
    cplot, eplot = charts(data)
    for name, drawing in [("konstanten_rueckrechnung", flow),
                          ("lichtgeschwindigkeit_rundung", cplot),
                          ("elementarladung_rundung", eplot)]:
        target = FIGURES / f"{name}.svg"
        renderSVG.drawToFile(drawing, str(target))
        # Browser-readable font families; PDF uses the embedded Vera fonts.
        svg = target.read_text(encoding="utf-8")
        svg = svg.replace("font-family: AuditBold", "font-family: sans-serif; font-weight: bold")
        svg = svg.replace("font-family: AuditSans", "font-family: sans-serif")
        target.write_text(svg, encoding="utf-8")
    c = canvas.Canvas(str(PDF), pagesize=(WIDTH, HEIGHT), invariant=1, pageCompression=1)
    c.setTitle("Heim-Audit: Eingaben, Rückrechnung und offene Prüfungen")
    c.setAuthor("Projekt Heims_Theorie - eigene Audit-Darstellung")
    c.setSubject("Begrenzter Quellen- und Rechenstand vom 18.10.2026, Etappen 39/40")
    heading(c, "QUELLEN UND ABHÄNGIGKEITEN", "Was sagen die bisherigen Treffer?",
            "Ein grafischer Einstieg in den geprüften Ausschnitt der Massen- und Konstantenrechnung.", 1)
    paragraph(c, "<b>Der Elektronentreffer nach der Konstantenkorrektur ist kein unabhängiger "
              "Vorhersagetest.</b> Heim beschreibt, die gemessene Elektronenmasse und Ladung "
              "zusammen mit hbar und c einzusetzen und daraus Konstanten zurückzurechnen. "
              "Der Tabellenanhang verweist auf dieses Verfahren. [1]", 665, 11)
    renderPDF.draw(flow, c, MARGIN, 304)
    y = paragraph(c, "Was darüber hinaus belegt ist", 280, 13, INK, bold=True)
    y = paragraph(c, "<b>F_S:</b> 17 zugeordnete Teilchenkomponenten; im Tabellenstand "
              "16 Masseneinträge wegen gemeinsamem pi+/-Wert. Das sind keine 17 "
              "nachgewiesenen unabhängigen Messbedingungen. Die ursprüngliche "
              "F_S-Eingabeliste bleibt offen. [2]", y-10, 10)
    y = paragraph(c, "<b>Y-Faktoren:</b> Alle Y_k=1 ist eine ausdrücklich genannte "
              "Tabellenannahme, damit auch Y41-44=1. Eine unabhängige Herleitung "
              "dieser Festlegung ist dadurch nicht belegt. [2]", y-10, 10)
    paragraph(c, "<b>Nächster aussagekräftiger Test:</b> Einen historischen Eingabesatz "
              "festlegen und eine zusätzliche Größe prüfen, die weder direkt noch indirekt "
              "zur Anpassung verwendet wurde. Eine Rückrechnung allein ist kein "
              "Gegenbeweis gegen das Modell.", y-11, 10)
    c.showPage()
    heading(c, "ZAHLEN UND REICHWEITE", "Passen die Druckwerte zusammen?",
            "Zwei getrennte Konsistenzchecks. Punkte: Zentralwerte. Balken: die jeweils benannte Spanne.", 2)
    renderPDF.draw(cplot, c, MARGIN, 473)
    renderPDF.draw(eplot, c, MARGIN, 257)
    y = paragraph(c, "Einordnung", 234, 12, INK, bold=True)
    y = paragraph(c, "Die Ladungsdifferenz beträgt rund <b>0,87 ppm</b>. Unter der geprüften "
              "Editionsbrücke überlappen die angenommenen Rundungsbereiche nicht. "
              "Die damalige Messunsicherheit lag bei rund 2,9 ppm (eine Standardabweichung). "
              "Das ist ein bedingter Darstellungsbefund, kein empirischer Widerlegungsnachweis. [1,3]", y-7, 9)
    y = paragraph(c, "<b>Methodik:</b> Rundung auf die nächste letzte Druckstelle angenommen. "
              "c-Produktprüfung mit exakten Brüchen; Ladungsendpunkte bei 60/90 Dezimalstellen "
              "stabil, ohne zertifizierte Intervallrechnung. Originale ungerundete Eingaben "
              "und vollständige historische Kalibrierung fehlen weiterhin.", y-7, 8.5)
    paragraph(c, "<b>Quellen:</b> [1] Heim, Bd. II, lokale Ausgabe 1996 (H004), Druck 253, "
              "301-302, 344, 349, 371; Bd. I, Ausgabe 1998 (H003), Druck 242, 247-248. "
              "[2] H004, Einführung 1-3, Druck 288-291, 342-343, 371-376. "
              "[3] PDG, Review of Particle Properties, April 1974 (M006), Druck 15. "
              "Quellhashes und Detailbelege: Berichte FS_PROVENANCE und CONSTANTS_ANCHOR "
              "vom 18.10.2026 unter 06_docs/. Grafiken und Einordnung: eigene Rekonstruktion.", y-8, 7.5, MUTED)
    c.save()
    print(PDF)
    print(f"3 SVG figures: {FIGURES}")


if __name__ == "__main__":
    build()
