# -*- coding: utf-8 -*-
"""Helper kecil untuk bina HTML slide."""
import json


def bullets(items, small=False, light=False):
    cls = "clean" + (" small" if small else "") + (" light" if light else "")
    return '<ul class="%s">%s</ul>' % (cls, "".join("<li>%s</li>" % i for i in items))


def cards(items, cols=3):
    inner = "".join('<div class="card"><h3>%s</h3><p class="muted">%s</p></div>' % (t, d) for t, d in items)
    return '<div class="grid g%d">%s</div>' % (cols, inner)


def flow(steps, arrows=True, big=False):
    parts = []
    for i, s in enumerate(steps):
        num, title, desc = s if len(s) == 3 else (s[0], s[1], "")
        parts.append('<div class="card fcard%s"><div class="num">%s</div><h3>%s</h3><p class="muted">%s</p></div>'
                     % (" big" if big else "", num, title, desc))
        if arrows and i < len(steps) - 1:
            parts.append('<div class="arrow">→</div>')
    return '<div class="flow">%s</div>' % "".join(parts)


def table(head, rows, small=False):
    h = "".join("<th>%s</th>" % c for c in head)
    b = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return '<table class="%s"><tr>%s</tr>%s</table>' % ("small" if small else "", h, b)


def note(text):
    return '<div class="note">%s</div>' % text


def promptbox(pid, compact=False, style="", hide_body=False):
    """Penanda — diganti oleh build.py dengan kotak prompt sebenar."""
    return "[[PROMPT %s]]" % json.dumps(dict(id=pid, compact=compact, style=style, hide=hide_body))
