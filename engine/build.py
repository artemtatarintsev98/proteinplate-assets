import math, html, sys
from collections import defaultdict, OrderedDict
from data import ING, R, WEEKS, DAYS

RID = {r["id"]: r for r in R}
import os
FOCUS = [
 [("Habit of the week","Protein first: eat the protein part of every meal before the carbs."),("Water","Fill a 1 L bottle twice a day. Done."),("Expect","Day 3–4 may feel hungry. Add Snack 2 — that's what it's for.")],
 [("Habit of the week","10-minute walk after dinner. It helps digestion and adds ~1,000 steps."),("Sleep","Aim for the same bedtime 5 nights out of 7."),("Expect","Lunches feel automatic now. Rate your hunger 1–5 in the tracker.")],
 [("Habit of the week","Plate rule: half vegetables, a quarter protein, a quarter carbs."),("Weekend","Eating out? Use the restaurant guide in the bonus section."),("Expect","Clothes may fit differently before the scale moves. Measure your waist.")],
 [("Habit of the week","Pick your 10 favorite recipes — that's your plan after day 28."),("Plan ahead","Write next week's menu on Saturday using the same structure."),("Expect","This is the routine you keep. Repeat any week you liked best.")],
]
BRAND = "PROTEIN PLATE"
TITLE = "The 30-Day High-Protein Reset"

def macros(r):
    k = p = c = f = 0
    for n, g in r["ings"]:
        a = ING[n]; k += a[0]*g/100; p += a[1]*g/100; c += a[2]*g/100; f += a[3]*g/100
    return round(k), round(p), round(c), round(f)
M = {r["id"]: macros(r) for r in R}

def day_tot(day):
    return [sum(M[x][i] for x in day) for i in range(4)]

# ---------- units ----------
SPOON = {"olive oil": ("tsp", 4.5), "honey": ("tsp", 7), "peanut butter": ("tbsp", 16),
         "low-sodium soy sauce": ("tbsp", 16), "teriyaki sauce": ("tbsp", 16), "chia seeds": ("tsp", 4),
         "cocoa powder (unsweetened)": ("tbsp", 5.5), "lemon juice": ("tbsp", 15), "garlic": ("clove", 4),
         "curry paste": ("tbsp", 15), "dark chocolate chips": ("tsp", 4), "almonds": ("almonds", 1.2),
         "parmesan, grated": ("tbsp", 5), "pickled jalapeños / hot sauce": ("tbsp", 10)}
COUNT = {"eggs": ("large egg", 50), "whole wheat tortilla": ("tortilla (8\")", 45),
         "whole wheat English muffin": ("English muffin", 66), "whole wheat bread": ("slice", 35),
         "whole wheat pita": ("pita", 64), "rice cakes": ("rice cake", 9)}

def fmt_num(x):
    if x >= 10: return f"{round(x)}"
    v = round(x*2)/2
    return (f"{v:.1f}".rstrip("0").rstrip(".")) if v != int(v) else str(int(v))

def amount(n, g, mult=1):
    g = g*mult
    if n in COUNT:
        u, w = COUNT[n]; q = g/w
        qs = fmt_num(q) if q >= 0.5 else "½"
        return f"{qs} {u}{'s' if q > 1.01 and not u.endswith(')') else ''}".replace("(8\")s", "(8\")")
    if n in SPOON:
        u, w = SPOON[n]; q = g/w
        qs=fmt_num(q); return f"{qs} {u}{'s' if (u=='clove' and qs not in ('0','0.5','1')) else ''}"
    oz = g/28.35
    return f"{round(g)} g · {fmt_num(oz)} oz" if oz >= 1 else f"{round(g)} g"

def nice(n):
    return n[0].upper()+n[1:]

# ---------- grocery ----------
SECTIONS = ["Meat & Fish", "Dairy & Eggs", "Produce", "Frozen", "Bakery", "Pantry"]
def grocery(week):
    tot = defaultdict(float)
    for day in week["plan"]:
        for rid in day:
            for n, g in RID[rid]["ings"]:
                tot[n] += g
    by = OrderedDict((s, []) for s in SECTIONS)
    for n, g in sorted(tot.items()):
        by[ING[n][4]].append((n, g))
    return by

def buy(n, g):
    if n in COUNT:
        u, w = COUNT[n]; q = math.ceil(g/w)
        return f"{q} {u}{'s' if q>1 and not u.endswith(')') else ''}"
    if n.startswith("cooked ") and n != "cooked lentils":
        dry = {"cooked white rice": 0.36, "cooked brown rice": 0.4, "cooked quinoa": 0.37}[n]
        return f"{round(g)} g cooked ≈ {round(g*dry)} g dry ({fmt_num(g*dry/28.35)} oz)"
    if n == "cooked lentils":
        return f"{round(g)} g cooked ≈ {round(g*0.42)} g dry"
    if n in SPOON and g < 120:
        u, w = SPOON[n]; q=g/w; return f"{fmt_num(q)} {u}{'s' if u=='clove' and q>1 else ''}"
    if n == "avocado": return f"{fmt_num(g/150) if g>=150 else ('¼' if g<=45 else '½')} avocado ({round(g)} g)"
    if n == "banana": return f"{math.ceil(g/115)} banana{'s' if g>115 else ''}"
    if n == "apple": return f"{math.ceil(g/180)} apple{'s' if g>180 else ''}"
    if n == "bell pepper": return f"{math.ceil(g/150)} pepper{'s' if g>150 else ''} ({round(g)} g)"
    lb = g/453.6
    if lb >= 1: return f"{round(g)} g · {fmt_num(lb*16/16) if lb>=10 else round(lb,2)} lb".replace(".0 lb"," lb")
    return f"{round(g)} g · {fmt_num(g/28.35)} oz"

# ---------- html ----------
E = html.escape
def pill(label, val, cls=""):
    return f'<span class="pill {cls}"><b>{val}</b>{label}</span>'

def macro_row(m):
    return (pill(" kcal", m[0], "k") + pill(" g protein", m[1], "p") + pill(" g carbs", m[2]) + pill(" g fat", m[3]))

pages = []
def page(inner, cls="", foot=True):
    pages.append((inner, cls, foot))

MEAL_CLS = {"Breakfast": "bf", "Lunch": "lu", "Dinner": "di", "Snack": "sn"}

# Cover
page(f"""
<div class="cover-top">{BRAND}</div>
<div class="cover-mid">
  <div class="kicker">4-week done-for-you meal plan</div>
  <h1 class="cover-title">The 30-Day<br><em>High-Protein</em><br>Reset</h1>
  <p class="cover-sub">120 g of protein a day from real food.<br>Most meals in 20 minutes or less. Zero calorie-counting.</p>
</div>
<div class="cover-photos"><div style="background-image:url(img/L1.jpg)"></div><div style="background-image:url(img/D6.jpg)"></div><div style="background-image:url(img/B5.jpg)"></div></div>
<div class="cover-stats">
  <div><b>30</b><span>days of meals</span></div>
  <div><b>{len(R)}</b><span>recipes with macros</span></div>
  <div><b>4</b><span>weekly grocery lists</span></div>
  <div><b>~1,450</b><span>kcal / day base</span></div>
</div>
""", "cover", foot=False)

# Welcome
page(f"""
<div class="kicker">Start here</div>
<h2>Eat more protein.<br>Stop guessing what to cook.</h2>
<p class="lead">Most diets fail for one reason: you're hungry, you're tired, and you have no plan at 6 pm. This reset fixes the plan part. Every breakfast, lunch, dinner and snack for 30 days is already decided (4 fully planned weeks + 2 "favorites" days) — with the grocery list, the Sunday prep and the numbers done for you.</p>
<div class="grid2">
  <div class="card"><h4>Why protein?</h4><p>Protein keeps you full longer than carbs or fat, helps you keep muscle while you lose fat, and takes more energy to digest. Hitting ~120 g a day is the single easiest change that makes eating less feel normal.</p></div>
  <div class="card"><h4>Why a set plan?</h4><p>Decision fatigue is real. When the meal is already chosen and half-prepped, you eat it. Lunches are batch-cooked on Sunday, dinners are 15–35 minutes, snacks take 2 minutes.</p></div>
</div>
<h3>How to use this guide</h3>
<ol class="steps">
  <li><b>Saturday:</b> open the weekly overview and shop from the grocery list.</li>
  <li><b>Sunday (60–90 min):</b> follow the prep checklist — lunches, breakfasts, eggs, chopped veg.</li>
  <li><b>Every day:</b> eat what's on the plan. Swap any meal for another one from the same category if you like — the numbers stay close.</li>
  <li><b>Track 3 things only:</b> did you hit your protein, drink 2 L of water, walk 7,000+ steps. Use the tracker at the back.</li>
</ol>
<div class="note"><b>Important:</b> This guide is general nutrition education, not medical advice. If you are pregnant, breastfeeding, have kidney disease, diabetes or any medical condition, or take medication, talk to your doctor before changing your diet. Nutrition values are calculated from USDA data and are estimates — brands vary.</div>
""")

# Targets / calories
page(f"""
<div class="kicker">Your numbers</div>
<h2>Pick your level — no math needed</h2>
<p class="lead">The base plan averages <b>about 1,450 kcal and 125 g protein a day</b>. That's a sensible starting point for many women who want to lose fat. If you're taller, very active, or always hungry on the base plan, move up a level.</p>
<table class="levels">
<tr><th>Level</th><th>What to do</th><th>Approx. per day</th></tr>
<tr><td><b>Base</b></td><td>Follow the plan exactly as written.</td><td>~1,350–1,550 kcal · 115–135 g protein</td></tr>
<tr><td><b>Level 2</b></td><td>Add a second snack from the snack list every day.</td><td>~1,550–1,750 kcal · 130–150 g protein</td></tr>
<tr><td><b>Level 3</b></td><td>Second snack + 1.5× the rice / pasta / potato / bread at lunch and dinner.</td><td>~1,750–1,950 kcal · 135–155 g protein</td></tr>
</table>
<h3>Signs you need more food</h3>
<p>Constant hunger, poor sleep, workouts feel terrible, or you're losing more than ~1% of your body weight per week after the first two weeks. Move up a level — slow and steady wins.</p>
<h3>What counts as a "swap"?</h3>
<div class="grid2">
  <div class="card"><h4>Any meal ↔ same meal type</h4><p>Don't like a dinner? Use any other dinner from the book. Every recipe shows its calories and protein, so you'll always know where you are.</p></div>
  <div class="card"><h4>Vegetarian?</h4><p>Every recipe has a <b>Veg swap</b> line. Tofu, tempeh, eggs, Greek yogurt, cottage cheese, edamame and lentils carry the protein.</p></div>
</div>
""")

# Protein cheat sheet
cheat = [("Chicken breast, 5 oz cooked", 43), ("Nonfat Greek yogurt, 1 cup", 23), ("Canned tuna, 1 can drained", 25),
         ("Cottage cheese, 1 cup", 26), ("Shrimp, 5 oz cooked", 34), ("Salmon, 5 oz cooked", 31),
         ("Lean ground turkey, 4 oz raw", 21), ("Egg whites, ½ cup", 13), ("2 large eggs", 13),
         ("Firm tofu, ½ block (200 g)", 35), ("Edamame, 1 cup shelled", 18), ("Lentils, 1 cup cooked", 18),
         ("Part-skim mozzarella stick", 7), ("Turkey deli slices, 3 oz", 15)]
rows = "".join(f"<tr><td>{a}</td><td class='num'>{b} g</td></tr>" for a, b in cheat)
page(f"""
<div class="kicker">Cheat sheet</div>
<h2>Hit 120 g without protein shakes</h2>
<p class="lead">Think in "protein anchors": build every meal around one item from this list, then add vegetables and a carb.</p>
<div class="grid2">
<table class="cheat">{rows}</table>
<div>
<div class="card big"><h4>The 30-30-40-20 rule</h4><p>Breakfast <b>~30 g</b> · Lunch <b>~35–40 g</b> · Dinner <b>~40 g</b> · Snack <b>~15–20 g</b>.<br>That's 125 g, spread so you're never starving.</p></div>
<div class="card"><h4>3 easy upgrades</h4><ul><li>Whisk egg whites into oatmeal — invisible +11 g.</li><li>Use Greek yogurt instead of sour cream or mayo.</li><li>Blend cottage cheese into pancake batter or pasta sauce.</li></ul></div>
<div class="card"><h4>Hunger killers</h4><ul><li>Volume: fill half the plate with vegetables.</li><li>Drink a glass of water before each meal.</li><li>Eat protein first, carbs last.</li></ul></div>
</div></div>
""")

# Weeks
for wi, w in enumerate(WEEKS, 1):
    rows = ""
    for d, day in zip(DAYS, w["plan"]):
        t = day_tot(day)
        cells = "".join(f"<td><span class='rid'>{rid}</span> {E(RID[rid]['name'])}</td>" for rid in day)
        rows += f"<tr><th>{d}</th>{cells}<td class='num'>{t[0]}<br><small>{t[1]} g P</small></td></tr>"
    avg = [round(sum(day_tot(d)[i] for d in w["plan"])/7) for i in range(4)]
    page(f"""
<div class="kicker">Week {wi} of 4</div>
<h2>{E(w['title'].split('· ')[1])}</h2>
<p class="lead">{E(w['theme'])}</p>
<table class="week">
<tr><th></th><th class="bf">Breakfast</th><th class="lu">Lunch</th><th class="di">Dinner</th><th class="sn">Snack</th><th>kcal</th></tr>
{rows}
</table>
<div class="grid3">{''.join(f"<div class='card'><h4>{a}</h4><p>{b}</p></div>" for a,b in FOCUS[wi-1])}</div>
<p class="avg">Daily average this week: <b>{avg[0]} kcal · {avg[1]} g protein · {avg[2]} g carbs · {avg[3]} g fat</b></p>
""", "landscape-ish")

    g = grocery(w)
    cols = ""
    for sec, items in g.items():
        if not items: continue
        lis = "".join(f"<li><span class='box'></span><span class='gi'>{E(nice(n))}</span><span class='gq'>{E(buy(n,gm))}</span></li>" for n, gm in items)
        cols += f"<div class='gsec'><h4>{sec}</h4><ul class='glist'>{lis}</ul></div>"
    page(f"""
<div class="kicker">Week {wi} · Grocery list</div>
<h2>Shop once. Done for the week.</h2>
<p class="small">Amounts cover all 7 days for one person. Spices you'll want on hand: salt, pepper, garlic powder, paprika, cumin, chili powder, oregano, cinnamon, taco seasoning.</p>
<div class="gcols">{cols}</div>
""")

    # Sunday prep
    used = []
    for day in w["plan"]:
        for rid in day:
            if rid not in used: used.append(rid)
    lunches = [r for r in used if r.startswith("L")]
    bfs = [r for r in used if r.startswith("B")]
    prep = []
    for L in lunches:
        n = sum(1 for d in w["plan"] if d[1] == L)
        prep.append(f"Cook <b>{RID[L]['name']}</b> — {n} portions. Pack into containers.")
    for B in bfs:
        n = sum(1 for d in w["plan"] if d[0] == B)
        if B in ("B1", "B2", "B6"): prep.append(f"Make <b>{RID[B]['name']}</b> × {n} (keeps 4 days in the fridge).")
    prep += ["Boil 6–8 eggs for snacks and quick breakfasts.",
             "Wash and chop: peppers, cucumber, carrots, onion. Store in airtight boxes.",
             "Cook a big pot of rice or quinoa if your dinners use it (check this week's plan).",
             "Portion snacks: yogurt cups, cottage cheese, edamame bags."]
    lis = "".join(f"<li><span class='box'></span>{p}</li>" for p in prep)
    page(f"""
<div class="kicker">Week {wi} · Sunday prep</div>
<h2>60–90 minutes that save your whole week</h2>
<ul class="check">{lis}</ul>
<div class="grid2">
<div class="card"><h4>Container tips</h4><p>Glass containers keep food fresher. Keep sauces and dressings separate until you eat. Cooked chicken, turkey and rice are best within 4 days — freeze anything for Thursday onward if you prefer.</p></div>
<div class="card"><h4>No time on Sunday?</h4><p>Buy a rotisserie chicken (skin off), microwave rice pouches and pre-cut veg. It costs a bit more but keeps you on plan — and that's what matters.</p></div>
</div>
""")

# Recipes
order = sorted(R, key=lambda r: ("BLDS".index(r["id"][0]), int(r["id"][1:])))
current = None
batch = []
def flush():
    global batch
    if batch:
        page("".join(batch), "recipes"); batch = []

for r in order:
    if r["meal"] != current:
        flush()
        current = r["meal"]
        cnt = sum(1 for x in R if x["meal"] == current)
        page(f"""<div class="divider-inner"><div class="kicker">Recipes</div><h1 class="div-title">{current}{'s' if current!='Lunch' else 'es'}</h1><p>{cnt} recipes · macros per serving</p></div>""", "divider " + MEAL_CLS[current], foot=False)
    m = M[r["id"]]
    ings = "".join(f"<li><span>{E(nice(n))}</span><span class='amt'>{E(amount(n,g))}</span></li>" for n, g in r["ings"])
    steps = "".join(f"<li>{E(s)}</li>" for s in r["steps"])
    serves = f"Makes {r['serves']} servings — ingredients below are <b>per serving</b>; multiply by {r['serves']}." if r["serves"] > 1 else "1 serving"
    tip = f"<p class='tip'>💡 {E(r['tip'])}</p>".replace("💡 ", "<b>Tip:</b> ") if r["tip"] else ""
    batch.append(f"""
<div class="recipe">
 <div class="rhead"><span class="tag {MEAL_CLS[r['meal']]}">{r['meal']} · {r['id']}</span><span class="time">{r['mins']} min</span></div>
 {f"<div class='rimg' style=\"background-image:url('img/{r['id']}.jpg')\"></div>" if os.path.exists(f"img/{r['id']}.jpg") else ""}
 <h3>{E(r['name'])}</h3>
 <div class="macros">{macro_row(m)}</div>
 <p class="serves">{serves}</p>
 <div class="rbody"><ul class="ings">{ings}</ul><ol class="rsteps">{steps}</ol></div>
 <p class="swap"><b>Veg swap:</b> {E(r['swap'])}</p>{tip}
</div>""")
    if len(batch) == 1: flush()
flush()

# Bonus pages
page("""
<div class="kicker">Bonus</div>
<h2>Eating out without falling off</h2>
<p class="lead">One restaurant meal won't undo a week. These orders keep you close to plan almost anywhere.</p>
<div class="grid2">
<div class="card"><h4>Mexican / Chipotle-style</h4><p>Bowl, double chicken or steak, fajita veg, half rice, beans, salsa, lettuce. Skip sour cream & queso, small guac if you want it.</p></div>
<div class="card"><h4>Burger place</h4><p>Single patty, lettuce wrap or regular bun, extra pickles & tomato. Side salad instead of fries — or share the fries.</p></div>
<div class="card"><h4>Italian</h4><p>Grilled chicken or fish with vegetables, or a tomato-based pasta + a side of protein. Bread: one piece, enjoy it.</p></div>
<div class="card"><h4>Sushi</h4><p>Sashimi + 1 roll, edamame, miso soup. Avoid tempura and "crunchy" rolls with mayo sauces.</p></div>
<div class="card"><h4>Coffee shop</h4><p>Egg-white bites or a protein box, latte with skim or unsweetened milk. Skip the muffin — it's often 400+ kcal.</p></div>
<div class="card"><h4>Drinks</h4><p>Vodka soda / tequila soda with lime, or a light beer. Alternate every drink with water. Plan a high-protein meal before you go.</p></div>
</div>
""")
page("""
<div class="kicker">Bonus</div>
<h2>Craving swaps that actually work</h2>
<table class="levels">
<tr><th>When you want…</th><th>Have this instead</th><th>Why it works</th></tr>
<tr><td>Ice cream</td><td>Chocolate Protein Pudding (S7), frozen 30 min</td><td>19 g protein, ~160 kcal</td></tr>
<tr><td>Chips</td><td>Edamame with sea salt (S5) or air-popped popcorn</td><td>Salty + crunchy, more volume</td></tr>
<tr><td>Something sweet after dinner</td><td>Greek yogurt + berries + honey (S1)</td><td>Sweet, high protein, ~150 kcal</td></tr>
<tr><td>Pizza</td><td>Whole wheat pita + marinara + mozzarella + turkey, 8 min in the oven</td><td>~35 g protein, ~420 kcal</td></tr>
<tr><td>Fast-food burger</td><td>Burger Night Bowls (D12)</td><td>Same flavors, half the calories</td></tr>
<tr><td>Wine every night</td><td>Sparkling water + lime in a wine glass on weeknights</td><td>Keeps the ritual, drops ~120 kcal a glass</td></tr>
<tr><td>Late-night snacking</td><td>Herbal tea + brush your teeth after dinner</td><td>Simple "kitchen closed" signal</td></tr>
</table>
<h3>The 80/20 rule</h3>
<p>Follow the plan 80% of the time and enjoy life the other 20%. A birthday dinner isn't failure — skipping the next three days of the plan is. Next meal, back on track.</p>
""")

# Trackers
for wi in range(1, 5):
    rows = "".join(f"<tr><th>{d}</th>" + "<td></td>"*6 + "</tr>" for d in DAYS)
    page(f"""
<div class="kicker">Printable tracker</div>
<h2>Week {wi} check-in</h2>
<table class="tracker">
<tr><th></th><th>Protein ✓<br><small>120 g</small></th><th>Water<br><small>2 L</small></th><th>Steps<br><small>7,000+</small></th><th>Sleep<br><small>7 h+</small></th><th>Energy<br><small>1–5</small></th><th>Hunger<br><small>1–5</small></th></tr>
{rows}
</table>
<div class="grid2">
<div class="card lines"><h4>Weigh-in (same day, same time)</h4><p>Start: ________  End: ________</p><h4>Waist (optional)</h4><p>Start: ________  End: ________</p></div>
<div class="card lines"><h4>What went well this week?</h4><p>____________________________________</p><p>____________________________________</p><h4>One thing to do better next week</h4><p>____________________________________</p></div>
</div>
""")

page(f"""
<div class="end">
<div class="kicker">You did it</div>
<h2>30 days. One new routine.</h2>
<p class="lead"><b>Days 29 & 30:</b> repeat your two favorite days from the plan — you've earned them. After that, you don't need another "new diet" on Monday. Repeat your favorite week, rotate recipes you liked, and keep the 3 daily habits: protein, water, steps.</p>
<p>Questions or feedback? Reply on Threads — we read everything.</p>
<p class="small">© {BRAND}. For personal use only. Please don't share or resell this file. This guide is for educational purposes and is not a substitute for advice from a doctor or registered dietitian.</p>
</div>
""", "endpage", foot=False)

CSS = open("style.css").read()
body = ""
for i, (inner, cls, foot) in enumerate(pages, 1):
    f = f'<div class="foot"><span>{TITLE}</span><span>{i}</span></div>' if foot else ""
    body += f'<section class="page {cls}">{inner}{f}</section>\n'
doc = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"
open("product.html", "w").write(doc)
print("pages", len(pages))
