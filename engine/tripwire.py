"""$7 tripwire: '7 High-Protein Dinners in 20 Minutes' PDF -> ../products/7-dinners-20-min.pdf"""
import os, html
from reel import RID, M          # includes extra recipes + unit fixes
from build import amount, nice, buy
from collections import defaultdict
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.abspath(__file__)); E = html.escape
IDS = ["D2", "D15", "X18", "D10", "D13", "D7", "V12"]
OFFER = "proteinplatehq.gumroad.com/l/high-protein-reset/PLATE8"

CSS = """@font-face{font-family:Lora;src:url(fonts/Lora-Variable.ttf);font-weight:100 900}
@font-face{font-family:Inter;src:url(fonts/Inter-SemiBold.otf);font-weight:600}
@font-face{font-family:Inter;src:url(fonts/Inter-ExtraBold.otf);font-weight:800}
@page{size:A4;margin:0} *{box-sizing:border-box;margin:0} body{font-family:Inter;color:#1f2a22;font-weight:600}
.pg{width:210mm;height:297mm;padding:18mm 18mm 16mm;position:relative;page-break-after:always;background:#FBF6EE;overflow:hidden}
h1{font-family:Lora;font-size:44pt;line-height:1.05;color:#24452F} h2{font-family:Lora;font-size:26pt;color:#24452F;margin-bottom:4mm}
.lead{font-size:13pt;line-height:1.5;margin-top:6mm;color:#3c4a40}
.cover{background:#24452F;color:#FBF6EE;padding:0} .cover .img{height:150mm;background-size:cover;background-position:center}
.cover .t{padding:14mm 18mm} .cover h1{color:#FBF6EE} .cover .k{color:#E9A07F;font-weight:800;letter-spacing:.2em;font-size:10pt;margin-bottom:5mm}
.photo{height:88mm;border-radius:6mm;background-size:cover;background-position:center;margin-bottom:6mm}
.pills{display:flex;gap:3mm;margin:2mm 0 6mm} .pill{background:#E6EDE3;border-radius:20mm;padding:2mm 4.5mm;font-size:10pt}
.pill.p{background:#D9734E;color:#fff}
.cols{display:grid;grid-template-columns:1fr 1.25fr;gap:9mm;font-size:10.5pt;line-height:1.45}
h3{font-size:9pt;letter-spacing:.18em;color:#D9734E;font-weight:800;margin-bottom:3mm}
ul{list-style:none;padding:0} li{display:flex;justify-content:space-between;gap:3mm;border-bottom:1px dotted #cfc6b8;padding:1.6mm 0}
li b{white-space:nowrap;color:#24452F} ol{padding-left:5mm} ol li{display:list-item;border:0;padding:0 0 2.5mm}
.tip{margin-top:5mm;background:#fff;border-left:3px solid #D9734E;padding:3mm 4mm;font-size:10pt}
.foot{position:absolute;bottom:9mm;left:18mm;right:18mm;font-size:8pt;color:#8a8f86;display:flex;justify-content:space-between}
.toc li{font-size:12pt;padding:3mm 0} .shop{columns:2;column-gap:10mm;font-size:10.5pt} .shop h3{margin-top:4mm}
.cta{background:#24452F;color:#FBF6EE} .cta h1,.cta h2{color:#FBF6EE} .code{display:inline-block;background:#D9734E;color:#fff;padding:3mm 6mm;border-radius:3mm;font-weight:800;font-size:16pt;margin:6mm 0}
"""

def page(inner, cls="", n=None):
    f = f"<div class='foot'><span>Protein Plate · 7 High-Protein Dinners in 20 Minutes</span><span>{n or ''}</span></div>"
    return f"<div class='pg {cls}'>{inner}{f}</div>"

def recipe_page(r, n):
    k, p, c, f = M[r["id"]]
    ings = "".join(f"<li><span>{E(nice(a))}</span><b>{E(amount(a, g))}</b></li>" for a, g in r["ings"])
    steps = "".join(f"<li>{E(s)}</li>" for s in r["steps"])
    tip = f"<div class='tip'>{E(r['tip'])}</div>" if r.get("tip") else ""
    swap = f"<div class='tip'>{E(r['swap'] if r['swap'].lower().startswith('swap') else 'Swap: ' + r['swap'])}</div>" if r.get("swap") and r["swap"] != "Already vegan." else ""
    return page(f"""<div class='photo' style="background-image:url('img/{r['id']}.jpg')"></div>
      <h2>{E(r['name'])}</h2>
      <div class='pills'><span class='pill p'>{p} g protein</span><span class='pill'>{k} kcal</span>
      <span class='pill'>{r['mins']} min</span><span class='pill'>serves {r['serves']}</span></div>
      <div class='cols'><div><h3>PER SERVING</h3><ul>{ings}</ul></div><div><h3>STEPS</h3><ol>{steps}</ol>{tip}{swap}</div></div>""", n=n)

def main():
    os.chdir(ROOT)
    rs = [RID[i] for i in IDS]
    pages = [page(f"""<div class='img' style="background-image:url('img/{IDS[0]}.jpg')"></div><div class='t'>
      <div class='k'>PROTEIN PLATE</div><h1>7 High-Protein Dinners in 20 Minutes</h1>
      <p class='lead' style='color:#e8e1d4'>Real food. One pan most nights. 40+ g protein per plate. Made for busy evenings.</p></div>""", "cover")]
    toc = "".join(f"<li><span>{i+1}. {E(r['name'])}</span><b>{M[r['id']][1]} g · {r['mins']} min</b></li>" for i, r in enumerate(rs))
    pages.append(page(f"""<h2>Dinner, handled.</h2><p class='lead'>Seven dinners you can cook on the most tired night of the week.
      Every recipe is 20 minutes or less, built around a real protein source, and scales up for the whole family —
      just multiply the amounts by the number of people.</p><h3 style='margin-top:10mm'>INSIDE</h3><ul class='toc'>{toc}</ul>
      <p class='lead' style='font-size:11pt'>Amounts are per serving. Nutrition is estimated from USDA data and rounded.</p>""", n=2))
    for i, r in enumerate(rs):
        pages.append(recipe_page(r, i + 3))
    tot = defaultdict(float)
    for r in rs:
        for a, g in r["ings"]: tot[a] += g
    from data import ING
    sections = defaultdict(list)
    for a, g in sorted(tot.items()): sections[ING[a][4]].append(f"<li><span>{E(nice(a))}</span><b>{E(buy(a, g))}</b></li>")
    shop = "".join(f"<h3>{E(s.upper())}</h3><ul>{''.join(v)}</ul>" for s, v in sections.items())
    pages.append(page(f"<h2>Shopping list</h2><p class='lead' style='margin:0 0 4mm'>All 7 dinners, 1 serving each. Multiply for your household.</p><div class='shop'>{shop}</div>", n=len(pages) + 1))
    pages.append(page(f"""<h2>Want the other 23 days planned too?</h2>
      <p class='lead' style='color:#e8e1d4'>The 30-Day High-Protein Reset is the full plan: breakfast, lunch, dinner and snacks for 30 days,
      ~120 g protein a day, weekly shopping lists and meal-prep guides. No shakes, no counting every bite.</p>
      <div class='code'>Code PLATE8 · $8 off</div><p class='lead' style='color:#fff'>{OFFER}</p>""", "cta", n=len(pages) + 1))
    htmlf = os.path.join(ROOT, "_tripwire.html")
    open(htmlf, "w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(pages)}</body></html>")
    out = os.path.join(ROOT, "..", "products"); os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); pg.goto("file://" + htmlf); pg.wait_for_load_state("networkidle")
        pg.pdf(path=os.path.join(out, "7-dinners-20-min.pdf"), format="A4", print_background=True)
        pg.set_viewport_size({"width": 1280, "height": 720}); pg.goto("file://" + htmlf)
        b.close()
    os.remove(htmlf)
    print("pages", len(pages))

if __name__ == "__main__":
    main()
