# -*- coding: utf-8 -*-
"""
Hidden Home Secrets — PDF builder.

Two-pass build: pass 1 records the real page each part lands on, pass 2
rebuilds with a correct table of contents. Blank pages are stripped afterwards.
"""
import os, sys, io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import (BOOK, WHY_THIS_BOOK, HOW_TO_USE, SAFETY_NOTE, PARTS,
                     TROUBLESHOOTING, MISTAKES, MYTHS, SAVINGS_TABLE,
                     CHECKLIST_WEEKLY, CHECKLIST_MONTHLY, CHECKLIST_SHOPPING,
                     TOOLKIT, SEASONS, FINAL_WORD, DISCLAIMER)

try:
    import pyphen
    HYPH = pyphen.Pyphen(lang="en_GB")
except Exception:
    HYPH = None

# ---------------------------------------------------------------- palette
# Taken from the live hiddenhomesecrets.com identity.
DARK      = HexColor("#15293b")   # navy — cover, part openers
DARK2     = HexColor("#1d3a52")
ACCENT    = HexColor("#4a7ca8")   # blue steel — headings, bars
LIGHT     = HexColor("#a8d8e8")   # light blue — part-opener accents
GOLD      = HexColor("#c8952e")   # savings, warm callouts
GOLD_TINT = HexColor("#faf3e2")
TINT      = HexColor("#eaf4f9")   # callout background
BODY      = HexColor("#1f2d3a")
MUTED     = HexColor("#5b7185")
RULE      = HexColor("#c9dfea")
WHITE     = HexColor("#ffffff")

PW, PH = letter
M = 0.85 * inch
CW = PW - 2 * M

F   = "Helvetica"
FB  = "Helvetica-Bold"
FI  = "Helvetica-Oblique"
FBI = "Helvetica-BoldOblique"


# ---------------------------------------------------------------- text engine
def _hyphen_pairs(word):
    """Return (head+'-', tail) split options, longest head first."""
    if not HYPH or len(word) < 7:
        return []
    out = []
    for pos in HYPH.positions(word):
        out.append((word[:pos] + "-", word[pos:]))
    out.reverse()
    return out


def wrap(text, font, size, width, hyphenate=True):
    """Greedy wrap with optional hyphenation. Returns list of word-lists.

    Headings and display type pass hyphenate=False — breaking a headline
    across a hyphen looks like a defect, not typography.
    """
    from reportlab.pdfbase.pdfmetrics import stringWidth
    words, lines, cur = text.split(), [], []
    for w in words:
        trial = cur + [w]
        if stringWidth(" ".join(trial), font, size) <= width:
            cur = trial
            continue
        if not cur:
            lines.append([w])
            continue
        placed = False
        if hyphenate:
            base = " ".join(cur)
            for head, tail in _hyphen_pairs(w):
                cand = (base + " " + head) if base else head
                if stringWidth(cand, font, size) <= width:
                    lines.append(cur + [head])
                    cur = [tail]
                    placed = True
                    break
        if not placed:
            lines.append(cur)
            cur = [w]
    if cur:
        lines.append(cur)
    return lines


class Doc:
    def __init__(self, path, toc_pages=None):
        self.c = canvas.Canvas(path, pagesize=letter)
        self.page = 0
        self.y = 0
        self.part_tag = ""
        self.toc_pages = toc_pages or {}
        self.recorded = {}

    # -- page furniture ----------------------------------------------------
    def _header(self):
        c = self.c
        c.setFont(F, 7.5)
        c.setFillColor(MUTED)
        c.drawString(M, PH - M + 14, BOOK["title"].upper())
        if self.part_tag:
            c.drawRightString(PW - M, PH - M + 14, self.part_tag.upper())
        c.setStrokeColor(RULE)
        c.setLineWidth(0.5)
        c.line(M, PH - M + 8, PW - M, PH - M + 8)

    def _footer(self):
        self.c.setFont(F, 8)
        self.c.setFillColor(MUTED)
        self.c.drawCentredString(PW / 2, M - 22, str(self.page))

    def new_content_page(self):
        """Start a fresh white content page. Draws its own header."""
        if self.page:
            self.c.showPage()
        self.page += 1
        self._header()
        self._footer()
        self.y = PH - M - 12
        self.c.setFillColor(BODY)

    def new_plain_page(self):
        if self.page:
            self.c.showPage()
        self.page += 1
        self._footer()
        self.y = PH - M
        self.c.setFillColor(BODY)

    def space(self, n):
        self.y -= n

    def need(self, n):
        if self.y - n < M + 12:
            self.new_content_page()
            return True
        return False

    # -- text blocks -------------------------------------------------------
    def para(self, text, size=10.4, font=F, color=BODY, lead=None,
             justify=True, indent=0, width=None):
        from reportlab.pdfbase.pdfmetrics import stringWidth
        lead = lead or size * 1.42
        width = width or (CW - indent)
        lines = wrap(text, font, size, width)
        for i, ln in enumerate(lines):
            self.need(lead)
            self.c.setFont(font, size)
            self.c.setFillColor(color)
            last = (i == len(lines) - 1)
            if justify and not last and len(ln) > 1:
                natural = stringWidth(" ".join(ln), font, size)
                gap = (width - natural) / (len(ln) - 1)
                space_w = stringWidth(" ", font, size)
                # loose-justification guard: fall back to ragged right
                if gap + space_w > space_w * 2.5:
                    self.c.drawString(M + indent, self.y, " ".join(ln))
                else:
                    x = M + indent
                    for w in ln:
                        self.c.drawString(x, self.y, w)
                        x += stringWidth(w, font, size) + space_w + gap
            else:
                self.c.drawString(M + indent, self.y, " ".join(ln))
            self.y -= lead
        return self.y

    def heading(self, text, size=15, color=DARK, bar=True, space_before=18):
        self.need(size + 46 + space_before)
        self.space(space_before)
        if bar:
            self.c.setFillColor(ACCENT)
            self.c.rect(M, self.y + 6, 34, 2.6, fill=1, stroke=0)
            # accent bar must clear the ascenders below it
            self.space(22)
        self.c.setFont(FB, size)
        self.c.setFillColor(color)
        for ln in wrap(text, FB, size, CW, hyphenate=False):
            self.c.drawString(M, self.y, " ".join(ln))
            self.y -= size * 1.15
        self.space(6)

    def kicker(self, text):
        self.need(30)
        self.c.setFont(FB, 7.4)
        self.c.setFillColor(ACCENT)
        self.c.drawString(M, self.y, text.upper())
        self.y -= 9
        self.space(9)          # >= 8pt clear gap before the entry title

    def bullet(self, text, size=10, mark="•", indent=16, color=BODY):
        self.need(size * 1.45)
        self.c.setFont(FB, size)
        self.c.setFillColor(ACCENT)
        self.c.drawString(M + 2, self.y, mark)
        self.para(text, size=size, color=color, justify=False, indent=indent)
        self.space(3)

    def checkbox_item(self, text, size=10):
        self.need(size * 1.6)
        self.c.setStrokeColor(ACCENT)
        self.c.setLineWidth(0.8)
        self.c.rect(M + 2, self.y - 1.5, 8, 8, fill=0, stroke=1)
        self.para(text, size=size, justify=False, indent=20)
        self.space(4)

    def callout(self, label, text, accent=ACCENT, bg=TINT):
        from reportlab.pdfbase.pdfmetrics import stringWidth
        size, lead, pad = 9.6, 13.6, 9
        inner = CW - 24
        lines = wrap(text, F, size, inner)
        h = pad * 2 + 12 + len(lines) * lead
        if self.y - h < M + 12:
            self.new_content_page()
        top = self.y + 4
        self.c.setFillColor(bg)
        self.c.rect(M, top - h, CW, h, fill=1, stroke=0)
        self.c.setFillColor(accent)
        self.c.rect(M, top - h, 3, h, fill=1, stroke=0)
        self.c.setFont(FB, 7.4)
        self.c.setFillColor(accent)
        self.c.drawString(M + 14, top - pad - 6, label.upper())
        self.c.setFont(F, size)
        self.c.setFillColor(BODY)
        yy = top - pad - 20
        for ln in lines:
            self.c.drawString(M + 14, yy, " ".join(ln))
            yy -= lead
        self.y = top - h - 12

    def divider(self):
        self.need(20)
        self.space(8)
        self.c.setStrokeColor(RULE)
        self.c.setLineWidth(0.6)
        self.c.line(M + CW * 0.34, self.y, M + CW * 0.66, self.y)
        self.space(12)


# ---------------------------------------------------------------- graphics
def bar_chart(d, title, rows, unit="$", h=132):
    """rows: [(label, value_a, value_b)] — a = commercial, b = this book."""
    d.need(h + 74)
    d.heading(title, size=11.5, bar=False, space_before=8)
    c = d.c
    # legend sits above the plot, clear of the category labels below the axis
    ly = d.y - 2
    c.setFont(F, 7); c.setFillColor(ACCENT)
    c.rect(M, ly, 7, 7, fill=1, stroke=0)
    c.drawString(M + 11, ly + 1, "Store-bought, per year")
    c.setFillColor(GOLD)
    c.rect(M + 152, ly, 7, 7, fill=1, stroke=0)
    c.drawString(M + 163, ly + 1, "This book's method, per year")
    top = ly - 12
    maxv = max(max(r[1], r[2]) for r in rows) or 1
    bw, gap = 15, (CW - 40) / len(rows)
    base = top - h + 26
    c.setStrokeColor(RULE); c.setLineWidth(0.6)
    c.line(M, base, M + CW, base)
    for i, (lab, a, b) in enumerate(rows):
        x = M + 22 + i * gap
        for j, (v, col) in enumerate(((a, ACCENT), (b, GOLD))):
            bh = (v / maxv) * (h - 42)
            c.setFillColor(col)
            c.rect(x + j * (bw + 3), base, bw, bh, fill=1, stroke=0)
            c.setFont(FB, 6.6); c.setFillColor(col)
            c.drawCentredString(x + j * (bw + 3) + bw / 2, base + bh + 3,
                                f"{unit}{v:g}")
        c.setFont(F, 6.8); c.setFillColor(MUTED)
        for k, part in enumerate(lab.split("\n")):
            c.drawCentredString(x + bw + 1, base - 11 - k * 8, part)
    d.y = base - 11 - 16 - 14


def ph_scale(d):
    d.need(120)
    d.heading("The pH Scale, And Where Each Method Sits", size=11.5,
              bar=False, space_before=8)
    c, top = d.c, d.y
    x0, w, hh = M, CW, 20
    y = top - 34
    steps = 14
    for i in range(steps):
        t = i / (steps - 1.0)
        col = HexColor("#%02x%02x%02x" % (
            int(220 - 150 * t), int(90 + 90 * t), int(70 + 150 * t)))
        c.setFillColor(col)
        c.rect(x0 + i * (w / steps), y, w / steps + 0.6, hh, fill=1, stroke=0)
    c.setFont(F, 6.6); c.setFillColor(MUTED)
    for i in range(0, 15, 2):
        c.drawCentredString(x0 + (i / 14.0) * w, y - 9, str(i))
    marks = [(2.4, "Vinegar"), (7.0, "Water"), (8.3, "Baking soda"),
             (11.4, "Washing soda")]
    for i, (val, lab) in enumerate(marks):
        mx = x0 + (val / 14.0) * w
        c.setStrokeColor(DARK); c.setLineWidth(1.1)
        yy = y + hh + 6 + (14 if i % 2 else 0)
        c.line(mx, y + hh, mx, yy)
        c.setFont(FB, 6.8); c.setFillColor(DARK)
        c.drawCentredString(mx, yy + 3, f"{lab} ({val})")
    d.y = y - 24


def flow(d, title, steps):
    d.need(96)
    d.heading(title, size=11.5, bar=False, space_before=8)
    c, top = d.c, d.y
    n = len(steps)
    bw = (CW - (n - 1) * 16) / n
    y = top - 46
    for i, (t, sub) in enumerate(steps):
        x = M + i * (bw + 16)
        c.setFillColor(TINT)
        c.rect(x, y, bw, 44, fill=1, stroke=0)
        c.setFillColor(ACCENT)
        c.rect(x, y, bw, 2.2, fill=1, stroke=0)
        c.setFont(FB, 8.2); c.setFillColor(DARK)
        c.drawCentredString(x + bw / 2, y + 30, t)
        c.setFont(F, 6.9); c.setFillColor(MUTED)
        for k, ln in enumerate(sub.split("\n")):
            c.drawCentredString(x + bw / 2, y + 18 - k * 8, ln)
        if i < n - 1:
            c.setStrokeColor(ACCENT); c.setLineWidth(1.2)
            ax = x + bw + 4
            c.line(ax, y + 22, ax + 8, y + 22)
            c.setFillColor(ACCENT)
            p = c.beginPath(); p.moveTo(ax + 11, y + 22)
            p.lineTo(ax + 6, y + 25); p.lineTo(ax + 6, y + 19); p.close()
            c.drawPath(p, fill=1, stroke=0)
    d.y = y - 16


def timeline(d):
    d.need(140)
    d.heading("Why The Ring Comes Back: Days Since Cleaning", size=11.5,
              bar=False, space_before=8)
    c, top = d.c, d.y
    gh, gw = 84, CW - 30
    base, x0 = top - gh - 22, M + 26
    c.setStrokeColor(RULE); c.setLineWidth(0.6)
    c.line(x0, base, x0 + gw, base)
    c.line(x0, base, x0, base + gh)
    series = [("Scrub only", [4, 26, 58, 84, 96], ACCENT),
              ("Weekly peroxide", [4, 8, 11, 12, 12], GOLD)]
    for name, vals, col in series:
        c.setStrokeColor(col); c.setLineWidth(1.6)
        pts = [(x0 + i * (gw / (len(vals) - 1.0)), base + (v / 100.0) * gh)
               for i, v in enumerate(vals)]
        for i in range(len(pts) - 1):
            c.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1])
        c.setFillColor(col)
        for px, py in pts:
            c.circle(px, py, 2.1, fill=1, stroke=0)
        c.setFont(FB, 7); c.setFillColor(col)
        c.drawString(pts[-1][0] - 62, pts[-1][1] + 6, name)
    c.setFont(F, 6.8); c.setFillColor(MUTED)
    for i, lab in enumerate(["0", "3", "7", "14", "21"]):
        c.drawCentredString(x0 + i * (gw / 4.0), base - 10, lab)
    c.drawString(M, base + gh - 4, "visible")
    c.drawString(M, base + gh - 12, "ring")
    d.y = base - 24


def table(d, headers, rows, widths, size=8.2, head_bg=DARK):
    lead = 12
    def draw_head(yy):
        d.c.setFillColor(head_bg)
        d.c.rect(M, yy - 4, CW, 17, fill=1, stroke=0)
        d.c.setFont(FB, size); d.c.setFillColor(WHITE)
        x = M + 5
        for h, w in zip(headers, widths):
            d.c.drawString(x, yy + 2, h)
            x += w
        return yy - 12

    d.need(70)
    y = draw_head(d.y)
    alt = False
    for row in rows:
        cells = [wrap(str(cv), F, size, w - 9) for cv, w in zip(row, widths)]
        rh = max(len(c_) for c_ in cells) * lead + 7
        if y - rh < M + 12:
            d.new_content_page()
            y = draw_head(d.y)
            alt = False
        if alt:
            d.c.setFillColor(HexColor("#f3f8fb"))
            d.c.rect(M, y - rh + 9, CW, rh, fill=1, stroke=0)
        x = M + 5
        for cell, w in zip(cells, widths):
            yy = y
            d.c.setFont(F, size); d.c.setFillColor(BODY)
            for ln in cell:
                d.c.drawString(x, yy, " ".join(ln))
                yy -= lead
            x += w
        y -= rh
        alt = not alt
        d.c.setStrokeColor(RULE); d.c.setLineWidth(0.4)
        d.c.line(M, y + 9, M + CW, y + 9)
    d.y = y - 8


def season_grid(d):
    d.need(150)
    d.heading("Maintenance Through The Year", size=11.5, bar=False,
              space_before=8)
    c, top = d.c, d.y
    cw = CW / 4
    y = top - 16
    boxh = 118
    for i, (name, items) in enumerate(SEASONS):
        x = M + i * cw
        c.setFillColor(TINT)
        c.rect(x + 2, y - boxh, cw - 4, boxh, fill=1, stroke=0)
        c.setFillColor(ACCENT)
        c.rect(x + 2, y - 18, cw - 4, 18, fill=1, stroke=0)
        c.setFont(FB, 8.4); c.setFillColor(WHITE)
        c.drawCentredString(x + cw / 2, y - 12.5, name)
        yy = y - 30
        for it in items:
            for ln in wrap(it, F, 7.1, cw - 18):
                c.setFont(F, 7.1); c.setFillColor(BODY)
                c.drawString(x + 8, yy, " ".join(ln))
                yy -= 9.2
            yy -= 4
    d.y = y - boxh - 14


# ---------------------------------------------------------------- pages
LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "images", "logo-print.png")


def portrait(c, cx, cy, r, ring=LIGHT, ring2=GOLD):
    """Circular channel portrait with a two-tone ring. Falls back to a
    typographic mark if the image is missing."""
    if os.path.exists(LOGO):
        c.drawImage(ImageReader(LOGO), cx - r, cy - r, 2 * r, 2 * r,
                    mask="auto")
        c.setStrokeColor(ring); c.setLineWidth(2.2)
        c.circle(cx, cy, r + 1.2, fill=0, stroke=1)
        c.setStrokeColor(ring2); c.setLineWidth(0.9)
        c.circle(cx, cy, r + 6, fill=0, stroke=1)
    else:
        c.setStrokeColor(ring); c.setLineWidth(1.6)
        c.circle(cx, cy, r, fill=0, stroke=1)
        c.setStrokeColor(ring2); c.setLineWidth(0.9)
        c.circle(cx, cy, r - 6, fill=0, stroke=1)
        c.setFont(FB, int(r * 0.95)); c.setFillColor(ring)
        c.drawCentredString(cx, cy - r * 0.33, "H")


def cover(d, logo=None):
    c = d.c
    d.page += 1
    c.setFillColor(DARK)
    c.rect(0, 0, PW, PH, fill=1, stroke=0)
    c.setFillColor(DARK2)
    c.rect(0, PH * 0.60, PW, PH * 0.40, fill=1, stroke=0)
    portrait(c, PW / 2, PH - 2.45 * inch, 52)

    c.setFont(FB, 8.5); c.setFillColor(LIGHT)
    c.drawCentredString(PW / 2, PH - 3.9 * inch, "T H E   F I E L D   G U I D E")

    c.setFont(FB, 43); c.setFillColor(WHITE)
    c.drawCentredString(PW / 2, PH - 5.0 * inch, "HIDDEN HOME")
    c.drawCentredString(PW / 2, PH - 5.62 * inch, "SECRETS")

    c.setStrokeColor(GOLD); c.setLineWidth(1.4)
    c.line(PW / 2 - 80, PH - 6.0 * inch, PW / 2 + 80, PH - 6.0 * inch)

    c.setFont(FI, 14); c.setFillColor(LIGHT)
    c.drawCentredString(PW / 2, PH - 6.5 * inch, BOOK["subtitle"])

    c.setFont(F, 9.6); c.setFillColor(HexColor("#8fb6cc"))
    for i, ln in enumerate([
            "31 methods  ·  6 reference charts  ·  3 printable checklists",
            "Everything costs about a dollar"]):
        c.drawCentredString(PW / 2, PH - 7.3 * inch - i * 15, ln)

    c.setFont(FB, 9); c.setFillColor(GOLD)
    c.drawCentredString(PW / 2, 1.15 * inch, BOOK["byline"].upper())
    c.setFont(F, 7.8); c.setFillColor(HexColor("#7fa6bf"))
    c.drawCentredString(PW / 2, 0.95 * inch, BOOK["site"])


def part_opener(d, part):
    c = d.c
    c.showPage()
    d.page += 1
    c.setFillColor(DARK)
    c.rect(0, 0, PW, PH, fill=1, stroke=0)
    c.setFont(FB, 10); c.setFillColor(GOLD)
    c.drawString(M, PH - 2.6 * inch, part["num"])
    c.setStrokeColor(GOLD); c.setLineWidth(1.2)
    c.line(M, PH - 2.75 * inch, M + 54, PH - 2.75 * inch)

    y = PH - 3.5 * inch
    for ln in wrap(part["title"], FB, 31, CW - 40, hyphenate=False):
        c.setFont(FB, 31); c.setFillColor(WHITE)
        c.drawString(M, y, " ".join(ln))
        y -= 36
    y -= 6
    for ln in wrap(part["subtitle"], FI, 13, CW - 60, hyphenate=False):
        c.setFont(FI, 13); c.setFillColor(LIGHT)
        c.drawString(M, y, " ".join(ln))
        y -= 18
    y -= 22
    for ln in wrap(part["intro"], F, 10.6, CW - 70):
        c.setFont(F, 10.6); c.setFillColor(HexColor("#c3dcea"))
        c.drawString(M, y, " ".join(ln))
        y -= 15.4
    c.setFont(F, 8); c.setFillColor(HexColor("#6d93ab"))
    c.drawCentredString(PW / 2, M - 22, str(d.page))
    d.y = 0


def entry(d, e):
    d.need(150)
    d.kicker(e["kicker"])
    d.need(30)
    d.c.setFont(FB, 16.5); d.c.setFillColor(DARK)
    d.c.drawString(M, d.y, e["title"])
    d.y -= 19
    d.space(3)                       # small gap before the hook
    d.para(e["hook"], size=10.6, font=FI, color=ACCENT, justify=False)
    d.space(11)
    d.c.setFont(FB, 7.4); d.c.setFillColor(ACCENT)
    d.c.drawString(M, d.y, "THE FIX")
    d.y -= 13
    for p in e["fix"]:
        d.para(p)
        d.space(7)
    d.space(4)
    d.callout("Pro tip", e["tip"], accent=ACCENT, bg=TINT)
    d.callout("What it saves you", e["saves"], accent=GOLD, bg=GOLD_TINT)
    d.divider()


# ---------------------------------------------------------------- build
def build(path, toc_pages=None):
    d = Doc(path, toc_pages)
    cover(d)

    # ---- title / contents
    d.new_content_page()
    d.heading("Contents", size=22, space_before=4)
    d.space(6)
    for p in PARTS:
        pg = d.toc_pages.get(p["num"], "")
        d.need(20)
        d.c.setFont(FB, 10.4); d.c.setFillColor(DARK)
        d.c.drawString(M, d.y, f"{p['num']}  ·  {p['title']}")
        d.c.setFont(F, 10.4); d.c.setFillColor(MUTED)
        d.c.drawRightString(PW - M, d.y, str(pg))
        d.y -= 14
        d.c.setFont(FI, 8.6); d.c.setFillColor(MUTED)
        d.c.drawString(M + 12, d.y, p["subtitle"])
        d.y -= 17
    for label, key in (("Reference & Charts", "REF"),
                       ("Troubleshooting Guide", "TROUBLE"),
                       ("Checklists", "CHECK"),
                       ("Myths, Mistakes & Final Word", "CLOSE")):
        pg = d.toc_pages.get(key, "")
        d.need(18)
        d.c.setFont(FB, 10.4); d.c.setFillColor(DARK)
        d.c.drawString(M, d.y, label)
        d.c.setFont(F, 10.4); d.c.setFillColor(MUTED)
        d.c.drawRightString(PW - M, d.y, str(pg))
        d.y -= 20

    # ---- front matter
    d.part_tag = "Introduction"
    d.new_content_page()
    d.heading("Why This Book Exists", size=19)
    for p in WHY_THIS_BOOK:
        d.para(p); d.space(8)
    d.space(10)
    d.heading("How To Use This Handbook", size=19)
    for p in HOW_TO_USE:
        d.para(p); d.space(8)
    d.space(10)
    d.heading("Before You Start: Three Rules", size=19)
    for p in SAFETY_NOTE:
        d.para(p); d.space(8)

    # ---- parts
    for part in PARTS:
        d.part_tag = part["title"]        # set BEFORE the page is created
        part_opener(d, part)
        d.new_content_page()
        d.recorded[part["num"]] = d.page
        for e in part["entries"]:
            entry(d, e)

    # ---- reference
    d.part_tag = "Reference"
    d.new_content_page()
    d.recorded["REF"] = d.page
    d.heading("Reference & Charts", size=21, space_before=2)
    d.para("The visual version of everything in the preceding parts. These are "
           "the pages worth printing and keeping with your cleaning supplies.",
           font=FI, color=MUTED, justify=False)
    d.space(12)
    ph_scale(d)
    d.space(6)
    bar_chart(d, "Annual Cost: Store-Bought Versus This Book",
              [("Bowl\ncleaner", 100, 15), ("Tank\ntablets", 75, 11),
               ("Odour\nspray", 85, 6), ("Carpet\nstain", 60, 8),
               ("Limescale", 35, 5), ("Grout", 30, 4)])
    d.space(6)
    timeline(d)
    d.space(8)
    flow(d, "The Peroxide Reset, Start To Finish",
         [("FLUSH", "work while\nrefilling"), ("POUR", "240 ml\nunder rim"),
          ("WAIT", "30–60 min\nno scrubbing"), ("BRUSH", "once, at\nwaterline"),
          ("FLUSH", "ring lifts,\nnot fades")])
    d.space(8)
    flow(d, "The Monthly Tank Soak",
         [("SCOOP", "2 tbsp into\nthe tank"), ("DISSOLVE", "stir, lid\nback on"),
          ("WAIT", "30 min\nno flush"), ("FLUSH ×2", "through jets,\nthen rinse")])
    d.space(8)
    season_grid(d)
    d.space(10)
    d.heading("Annual Savings Reference", size=13)
    table(d, ["Product category", "Typical/yr", "Replace with", "Cost/yr", "Saved"],
          SAVINGS_TABLE, [148, 78, 108, 62, 74])

    # ---- troubleshooting
    d.part_tag = "Troubleshooting"
    d.new_content_page()
    d.recorded["TROUBLE"] = d.page
    d.heading("Troubleshooting Quick Guide", size=21, space_before=2)
    d.para("Find the symptom, read across. Most recurring problems are a "
           "mismatch between the chemistry used and the problem present.",
           font=FI, color=MUTED, justify=False)
    d.space(14)
    table(d, ["Symptom", "Actual cause", "What to do"],
          TROUBLESHOOTING, [176, 158, 136])

    # ---- checklists
    d.part_tag = "Checklists"
    d.new_content_page()
    d.recorded["CHECK"] = d.page
    d.heading("Printable Checklists", size=21, space_before=2)
    d.space(8)
    d.heading("Weekly — Five Minutes", size=13)
    for it in CHECKLIST_WEEKLY:
        d.checkbox_item(it)
    d.space(12)
    d.heading("Monthly — Half An Hour", size=13)
    for it in CHECKLIST_MONTHLY:
        d.checkbox_item(it)
    d.space(12)
    d.heading("The Complete Shopping List", size=13)
    table(d, ["Item", "Where", "Cost"], CHECKLIST_SHOPPING, [246, 158, 66])
    d.space(10)
    d.heading("Your Tool Kit", size=13)
    for it in TOOLKIT:
        d.bullet(it)

    # ---- closing
    d.part_tag = "Closing"
    d.new_content_page()
    d.recorded["CLOSE"] = d.page
    d.heading("Ten Mistakes Worth Avoiding", size=21, space_before=2)
    d.space(6)
    for i, m in enumerate(MISTAKES, 1):
        d.need(34)
        d.c.setFont(FB, 11); d.c.setFillColor(GOLD)
        d.c.drawString(M, d.y, f"{i:02d}")
        d.para(m, size=9.9, indent=24, justify=False)
        d.space(8)

    d.new_content_page()
    d.heading("Six Myths, Corrected", size=21, space_before=2)
    d.space(6)
    for claim, truth in MYTHS:
        d.need(70)
        d.c.setFont(FBI, 10.4); d.c.setFillColor(DARK)
        d.para("“" + claim + "”", size=10.4, font=FBI, color=DARK,
               justify=False)
        d.space(4)
        d.para(truth, size=9.9, color=BODY)
        d.space(13)

    d.new_content_page()
    d.heading("A Final Word", size=21, space_before=2)
    d.space(6)
    for p in FINAL_WORD:
        d.para(p, size=10.8); d.space(9)

    # ---- about
    d.part_tag = "About"
    d.new_content_page()
    c = d.c
    cx, cy, r = PW / 2, d.y - 82, 46
    portrait(c, cx, cy, r, ring=ACCENT, ring2=GOLD)
    d.y = cy - r - 40
    c.setFont(FB, 20); c.setFillColor(DARK)
    c.drawCentredString(PW / 2, d.y, "Hidden Home Secrets")
    d.y -= 24
    c.setFont(FI, 11); c.setFillColor(MUTED)
    c.drawCentredString(PW / 2, d.y, BOOK["subtitle"])
    d.y -= 30
    for p in [
        "Hidden Home Secrets is a channel about the cheap, unglamorous fixes "
        "that actually hold — the dollar-store ingredients and the small "
        "technique changes that solve problems the cleaning aisle keeps "
        "selling you a subscription for.",
        "This handbook collects those methods in one place, with the detail a "
        "video cannot carry: exact ratios, dwell times, the limits of each "
        "method, and what to do when cleaning is not the answer at all.",
        "New methods go up on the channel regularly. If something here saved "
        "you a call-out or a Saturday, that is the whole point of it.",
    ]:
        d.para(p, size=10.4); d.space(9)
    d.space(14)
    c.setStrokeColor(RULE); c.setLineWidth(0.7)
    c.line(M + 90, d.y, PW - M - 90, d.y)
    d.y -= 24
    c.setFont(FB, 8.4); c.setFillColor(ACCENT)
    c.drawCentredString(PW / 2, d.y, "WATCH THE CHANNEL")
    d.y -= 17
    c.setFont(FB, 11.6); c.setFillColor(DARK)
    c.drawCentredString(PW / 2, d.y, BOOK["channel_url"])
    d.y -= 20
    c.setFont(F, 10); c.setFillColor(MUTED)
    c.drawCentredString(PW / 2, d.y, BOOK["site"])
    d.y -= 15
    c.drawCentredString(PW / 2, d.y, BOOK["contact"])

    # ---- disclaimer
    d.new_content_page()
    d.heading("Disclaimer", size=17, space_before=2)
    d.space(4)
    for p in DISCLAIMER:
        d.para(p, size=9.6, color=MUTED); d.space(9)

    d.c.showPage()
    d.c.save()
    return d.recorded


def strip_blanks(path):
    """Remove pages that are >98% white."""
    try:
        from pypdf import PdfReader, PdfWriter
    except Exception:
        return None
    try:
        import fitz  # noqa
    except Exception:
        fitz = None
    reader = PdfReader(path)
    keep = []
    for i, pg in enumerate(reader.pages):
        txt = (pg.extract_text() or "").strip()
        has_draw = "/XObject" in (pg.get("/Resources") or {}) or bool(txt)
        # a page with only a page number is still blank for our purposes
        meaningful = len(txt.replace("\n", "").strip()) > 4
        keep.append(meaningful or has_draw)
    if all(keep):
        return len(reader.pages)
    w = PdfWriter()
    for i, pg in enumerate(reader.pages):
        if keep[i]:
            w.add_page(pg)
    with open(path, "wb") as f:
        w.write(f)
    return len(w.pages)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "Hidden Home Secrets.pdf")
    tmp = out + ".pass1"
    rec = build(tmp, None)              # pass 1 — record real page numbers
    build(out, rec)                     # pass 2 — correct TOC
    try:
        os.remove(tmp)
    except OSError:
        pass
    n = strip_blanks(out)
    print("built:", out)
    print("pages:", n)
