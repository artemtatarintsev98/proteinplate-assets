import json, html, os, sys
from data import R
from build import M, amount, nice
E=html.escape
RID={r["id"]:r for r in R}
HOOK={"Breakfast":"breakfast","Lunch":"meal-prep lunch","Dinner":"dinner","Snack":"snack"}
css="""@font-face{font-family:Lora;src:url(fonts/Lora-Variable.ttf);font-weight:100 900}
@font-face{font-family:Lora;font-style:italic;src:url(fonts/Lora-Italic-Variable.ttf);font-weight:100 900}
@font-face{font-family:Inter;src:url(fonts/Inter-Regular.otf);font-weight:400}
@font-face{font-family:Inter;src:url(fonts/Inter-SemiBold.otf);font-weight:600}
@font-face{font-family:Inter;src:url(fonts/Inter-Bold.otf);font-weight:700}
@font-face{font-family:Inter;src:url(fonts/Inter-ExtraBold.otf);font-weight:800}
*{box-sizing:border-box;margin:0}body{margin:0;font-family:Inter;width:1080px;height:1920px;overflow:hidden}
.s{width:1080px;height:1920px;position:relative;background:#FBF6EE;color:#1E2A22}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.0) 35%,rgba(20,35,25,.85) 78%)}
.hook{position:absolute;left:80px;right:80px;bottom:330px;color:#fff}
.hook .k{font-size:34px;letter-spacing:.2em;text-transform:uppercase;font-weight:800;color:#F6D7A7}
.hook h1{font-family:Lora;font-size:104px;line-height:1.02;margin:22px 0 30px}
.badge{display:inline-block;background:#D9734E;color:#fff;font-weight:800;font-size:46px;padding:16px 34px;border-radius:60px}
.tag{position:absolute;left:80px;top:180px;background:#FBF6EE;color:#24452F;font-weight:800;font-size:28px;letter-spacing:.25em;padding:14px 26px;border-radius:40px}
.pad{position:absolute;left:90px;right:90px;top:260px}
h2{font-family:Lora;font-size:84px;color:#24452F;margin-bottom:16px}
.sub{font-size:36px;color:#6B746C;margin-bottom:40px}
ul{list-style:none;padding:0}li.i{display:flex;justify-content:space-between;font-size:44px;padding:24px 0;border-bottom:3px dotted #E4DCCF}
li.i b{color:#D9734E}
ol{padding-left:70px}ol li{font-size:48px;line-height:1.38;margin-bottom:40px}
.mac{position:absolute;left:90px;right:90px;bottom:300px;display:flex;gap:18px;flex-wrap:wrap}
.pill{font-size:38px;padding:12px 28px;border-radius:50px;background:#DDE6D3;color:#24452F;font-weight:700}.pill.p{background:#D9734E;color:#fff}
.cta{background:#24452F;color:#fff;display:flex;flex-direction:column;justify-content:center;padding:110px}
.cta h2{color:#fff;font-size:100px;line-height:1.05}.cta h2 em{color:#D9734E}
.cta p{font-size:46px;color:#DDE6D3;margin:40px 0 60px;line-height:1.4}
.ph2{position:absolute;left:90px;right:90px;bottom:170px;height:640px;border-radius:36px;background-size:cover;background-position:center}
.btn{align-self:flex-start;background:#D9734E;color:#fff;font-weight:800;font-size:46px;padding:30px 50px;border-radius:70px}"""
def frames(rid):
    r=RID[rid]; m=M[rid]
    f1=f"""<div class="s"><div class="ph" style="background-image:url('img/{rid}.jpg')"></div><div class="shade"></div><span class="tag">PROTEIN PLATE</span>
<div class="hook"><div class="k">{r['mins']}-minute {HOOK[r['meal']]}</div><h1>{E(r['name'])}</h1><span class="badge">{m[1]} g protein · {m[0]} kcal</span></div></div>"""
    ings="".join(f"<li class='i'><span>{E(nice(n))}</span><b>{E(amount(n,g))}</b></li>" for n,g in r['ings'][:8])
    f2=f"""<div class="s"><div class="pad"><h2>You need</h2><div class="sub">per serving</div><ul>{ings}</ul></div>
<div class="mac"><span class="pill p">{m[1]} g protein</span><span class="pill">{m[0]} kcal</span><span class="pill">{m[2]} g carbs</span><span class="pill">{m[3]} g fat</span></div></div>"""
    st="".join(f"<li>{E(x)}</li>" for x in r['steps'][:4])
    f3=f"""<div class="s"><div class="pad"><h2>How to make it</h2><div class="sub">{r['mins']} minutes</div><ol>{st}</ol></div><div class="ph2" style="background-image:url('img/{rid}.jpg')"></div></div>"""
    f4="""<div class="s cta"><h2>Want 30 days of meals like this <em>planned for you?</em></h2><p>Start with our free High-Protein Grocery List. One page, 3 sample days at ~125 g protein.</p><span class="btn">Link in bio →</span></div>"""
    return [f1,f2,f3,f4]

def render(rid, outdir="out"):
    """Render 4 PNG frames for recipe rid; returns list of png paths."""
    from playwright.sync_api import sync_playwright
    os.makedirs(outdir, exist_ok=True)
    pngs=[]
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
        for i,f in enumerate(frames(rid),1):
            h=f"{rid}-f{i}.html"
            open(h,"w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{f}</body></html>")
            pg.goto("file://"+os.path.abspath(h)); pg.wait_for_load_state("networkidle"); pg.wait_for_timeout(300)
            png=f"{outdir}/{rid}-f{i}.png"; pg.screenshot(path=png); pngs.append(png); os.remove(h)
        b.close()
    return pngs
