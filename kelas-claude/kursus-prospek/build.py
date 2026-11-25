# -*- coding: utf-8 -*-
"""Jana slides.html, nota-penceramah.html, prompt-pack.html dan prompt-pack.txt dari content.py.

    python3 build.py && node render.js
"""
import html, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import SLIDES, PROMPTS, COURSE_TITLE, COURSE_SUB, TEAM, DISCLAIMER  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
P = {p[0]: dict(id=p[0], title=p[1], when=p[2], text=p[3]) for p in PROMPTS}


def fmt_prompt(text):
    t = html.escape(text)
    t = re.sub(r"\{\{(.+?)\}\}", r'<span class="var">{{\1}}</span>', t)
    t = re.sub(r"\[([^\]\n]*)\]", r'<span class="fill">[\1]</span>', t)
    return t


def render_promptbox(m):
    o = json.loads(m.group(1))
    p = P[o["id"]]
    cls = "pbox" + (" compact" if o["compact"] else "")
    head = '<div class="phead"><span class="pid">%s</span>%s</div>' % (p["id"], p["title"])
    if o["hide"]:
        return '<div class="pref" style="%s"><span class="pid">%s</span>%s <span class="muted">— salin dari Prompt Pack</span></div>' % (o["style"], p["id"], p["title"])
    return '<div class="%s" style="%s">%s<div class="ptext">%s</div></div>' % (cls, o["style"], head, fmt_prompt(p["text"]))


def expand(s):
    return re.sub(r"\[\[PROMPT (\{.*?\})\]\]", render_promptbox, s)


SLIDE_CSS = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()


def build_slides():
    out = []
    n = len(SLIDES)
    for i, s in enumerate(SLIDES, 1):
        lay = s["layout"]
        foot_l = "KELAS CLAUDE AI · " + TEAM.upper()
        if s.get("prompts"):
            foot_l = "Prompt Pack: " + ", ".join(s["prompts"])
        foot = '<div class="foot"><span>%s</span><span>%02d / %02d</span></div>' % (foot_l, i, n)
        if lay == "cover":
            out.append('<section class="slide dark cover"><div class="blob b1"></div><div class="blob b2"></div>'
                       '<div class="cover-in"><div class="kicker">Kelas Eksklusif · %s</div><h1 style="font-size:58px">%s</h1>'
                       '<p class="lead-d">%s</p></div>%s</section>' % (TEAM, s["title"], s["body"], foot.replace('KELAS CLAUDE AI · ' + TEAM.upper(), DISCLAIMER)))
        elif lay == "section":
            out.append('<section class="slide section"><div class="blob b3"></div><div class="sec-in">'
                       '<div class="kicker">%s</div><h1>%s</h1><p class="lead">%s</p></div>%s</section>'
                       % (s["kicker"], s["title"], s["body"], foot))
        else:
            cls = {"std": "", "dark": "dark", "accent": "accent"}[lay]
            out.append('<section class="slide %s"><div class="kicker">%s</div><h2>%s</h2><div class="body">%s</div>%s</section>'
                       % (cls, s.get("kicker", ""), s["title"], expand(s["body"]), foot))
    doc = ('<!doctype html><html lang="ms"><head><meta charset="utf-8"><title>%s</title><style>%s</style></head><body>%s</body></html>'
           % (COURSE_TITLE, SLIDE_CSS, "\n".join(out)))
    open(os.path.join(HERE, "slides.html"), "w", encoding="utf-8").write(doc)


DOC_CSS = """
@page { size: A4; margin: 16mm 16mm 18mm; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Inter", sans-serif; color: #1d1b18; font-size: 11pt; line-height: 1.5; }
h1 { font-family: "Inter Display", "Inter", sans-serif; font-size: 28pt; line-height: 1.1; font-weight: 800; letter-spacing: -.01em; }
h2 { font-size: 15pt; font-weight: 800; margin-bottom: 4pt; }
.kicker { color: #d9622b; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; font-size: 9pt; margin-bottom: 6pt; }
.muted { color: #6b645a; }
.cover { height: 250mm; display: flex; flex-direction: column; justify-content: center; page-break-after: always; }
.cover p { font-size: 13pt; margin-top: 14pt; max-width: 140mm; }
.legend { margin-top: 26pt; border: 1px solid #e7e0d5; border-radius: 8pt; padding: 12pt 14pt; font-size: 10pt; }
.legend div { margin-bottom: 4pt; }
.fill { color: #c0501d; font-weight: 700; }
.var { color: #2f6fb0; font-weight: 700; }
/* notes */
.ns { display: grid; grid-template-columns: 74mm 1fr; gap: 8mm; padding: 6mm 0; border-bottom: 1px solid #e7e0d5; page-break-inside: avoid; }
.ns img { width: 74mm; border: 1px solid #e7e0d5; border-radius: 4pt; display: block; }
.ns .no { font-size: 9pt; font-weight: 700; color: #d9622b; letter-spacing: .08em; }
.ns h2 { font-size: 13pt; }
.ns ul { padding-left: 14pt; margin-top: 4pt; }
.ns li { margin-bottom: 3pt; font-size: 10pt; }
.ns .pr { margin-top: 6pt; font-size: 9pt; color: #6b645a; }
.ns.sec { background: #faf7f2; }
/* prompt pack */
.pp { page-break-inside: avoid; margin-bottom: 9mm; }
.pp .top { display: flex; align-items: baseline; gap: 8pt; }
.pp .id { background: #d9622b; color: #fff; font-weight: 800; font-size: 9pt; padding: 2pt 7pt; border-radius: 4pt; }
.pp .when { font-size: 9.5pt; color: #6b645a; margin: 2pt 0 6pt; }
.pp pre { font-family: "DejaVu Sans Mono", monospace; font-size: 9pt; line-height: 1.5; white-space: pre-wrap; background: #faf7f2; border: 1px solid #e7e0d5; border-left: 3pt solid #d9622b; border-radius: 4pt; padding: 9pt 11pt; }
.toc { columns: 2; column-gap: 10mm; font-size: 10pt; margin-top: 10pt; }
.toc div { margin-bottom: 3pt; break-inside: avoid; }
.toc b { color: #d9622b; display: inline-block; width: 26pt; }
"""


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def build_notes():
    rows = []
    for i, s in enumerate(SLIDES, 1):
        notes = s.get("notes") or ["Slide pemisah bahagian. Ringkaskan apa yang baru selesai, dan apa yang akan dipelajari dalam bahagian ini."]
        pr = ""
        if s.get("prompts"):
            pr = '<div class="pr">Prompt: %s</div>' % ", ".join("%s (%s)" % (x, P[x]["title"]) for x in s["prompts"])
        rows.append('<div class="ns%s"><img src="thumbs/%02d.png"><div><div class="no">SLIDE %02d</div><h2>%s</h2><ul>%s</ul>%s</div></div>'
                    % (" sec" if s["layout"] == "section" else "", i, i, strip_tags(s["title"]),
                       "".join("<li>%s</li>" % html.escape(n) for n in notes), pr))
    cover = ('<div class="cover"><div class="kicker">Untuk penceramah sahaja</div><h1>Nota Penceramah</h1>'
             '<p>%s</p><p class="muted">Setiap slide: apa yang perlu diterangkan, soalan untuk peserta, dan bila buat demo live.</p>'
             '<div class="legend"><div><b>Sebelum kelas, sediakan:</b></div>'
             '<div>☐ Sistem lead kau sendiri berjalan: group Telegram + report terkini sedia untuk demo</div>'
             '<div>☐ App Claude Desktop dipasang di laptop demo, dan Threads dah login dalam browser app</div>'
             '<div>☐ Minta peserta pasang app Claude Desktop &amp; Telegram, dan ada akaun Threads sebelum kelas</div>'
             '<div>☐ Ganti semua teks <span class="fill">[dalam kurungan]</span> di slide dengan maklumat sebenar</div>'
             '<div>☐ Semak harga Claude, nama menu app Desktop, dan garis panduan pemasaran Coway terkini</div>'
             '<div>☐ Hantar PDF Prompt Pack kepada peserta sebelum kelas mula</div></div></div>') % COURSE_TITLE
    doc = ('<!doctype html><html lang="ms"><head><meta charset="utf-8"><title>Nota Penceramah</title><style>%s</style></head><body>%s%s</body></html>'
           % (DOC_CSS, cover, "".join(rows)))
    open(os.path.join(HERE, "nota-penceramah.html"), "w", encoding="utf-8").write(doc)


def build_pack():
    toc = "".join('<div><b>%s</b>%s</div>' % (p[0], p[1]) for p in PROMPTS)
    cover = ('<div class="cover"><div class="kicker">Prompt Pack Peserta · ' + TEAM + '</div><h1>%s</h1><p>%s</p>'
             '<div class="legend"><div><b>Cara guna</b></div>'
             '<div>1. Cari nombor prompt yang tertera di bawah slide (cth. P08).</div>'
             '<div>2. Salin keseluruhan prompt ke dalam Claude.</div>'
             '<div>3. Ganti teks <span class="fill">[dalam kurungan]</span> dengan maklumat kau sendiri.</div>'
             '<div>4. P01–P11: guna di claude.ai (dalam Project Brand Brain). P12–P21: guna dalam app Claude Desktop.</div>'
             '</div><div class="toc">%s</div><p class="muted" style="font-size:9pt;margin-top:14pt">' + DISCLAIMER + '</p></div>') % (COURSE_TITLE, COURSE_SUB, toc)
    items = "".join('<div class="pp"><div class="top"><span class="id">%s</span><h2>%s</h2></div><div class="when">Bila guna: %s</div><pre>%s</pre></div>'
                    % (p["id"], p["title"], p["when"], fmt_prompt(p["text"])) for p in P.values())
    doc = ('<!doctype html><html lang="ms"><head><meta charset="utf-8"><title>Prompt Pack</title><style>%s</style></head><body>%s%s</body></html>'
           % (DOC_CSS, cover, items))
    open(os.path.join(HERE, "prompt-pack.html"), "w", encoding="utf-8").write(doc)

    txt = [COURSE_TITLE, "PROMPT PACK PESERTA", "=" * 60, ""]
    for p in P.values():
        txt += ["%s — %s" % (p["id"], p["title"]), "Bila guna: " + p["when"], "-" * 60, p["text"], "", "=" * 60, ""]
    open(os.path.join(HERE, "prompt-pack.txt"), "w", encoding="utf-8").write("\n".join(txt))


if __name__ == "__main__":
    build_slides(); build_notes(); build_pack()
    print("OK: %d slide, %d prompt" % (len(SLIDES), len(PROMPTS)))
