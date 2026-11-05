"""Daily STORY post: Artem's real story told a new way each day (carousel slides + 18s video).
Runs in GitHub Actions ~11:45 Zagreb. Output: ../stories/<date>/slide-N.png, story.mp4, meta.json
(the 12:33 Chrome task posts them to TikTok / Instagram / Threads). Also uploads the video as a YouTube Short."""
import os, sys, json, random, glob, html, datetime, subprocess, requests
from run_daily import yt_upload, FREE

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "..", "stories")
STATE = os.path.join(ROOT, "story_state.json")
E = html.escape

# Artem's REAL story. Only these facts may be used. Extend this list only with facts Artem confirms.
FACTS = [
 "For years I ate badly and without any system.",
 "I felt bad all the time: low energy, heavy, not like myself.",
 "My weight kept swinging: sometimes too much, sometimes too little. Never stable.",
 "Nothing I tried stuck.",
 "Then I built myself a simple plan: real food, protein in every meal.",
 "Now I feel amazing. Eating like this is easy and actually tasty.",
 "Out of this plan I made Protein Plate (30-Day High-Protein Reset), and a free High-Protein Grocery List.",
]
ANGLES = [
 "POV opener: 'POV: you're tired of your weight going up and down'",
 "'Nobody talks about being underweight AND overweight in the same year'",
 "'The day I stopped dieting and started planning'",
 "'If you feel bad all the time, it might be your plate' (gentle, not medical)",
 "'I used to think eating healthy meant eating less'",
 "'What changed when I put protein in every meal' (feelings only)",
 "'Things I wish I knew before my weight rollercoaster'",
 "'I didn't need more willpower. I needed a plan.'",
 "'Me 2 years ago vs me now' (feelings, no numbers)",
 "'Why every diet failed me (and what didn't)'",
 "'The boring plan that fixed how I feel'",
 "'Stop starting over every Monday'",
]
STYLES = ["dark", "notes", "photo"]

def gemini(prompt):
    key = os.environ.get("GEMINI_API_KEY")
    if not key: return None
    for model in ("gemini-flash-latest", "gemini-flash-lite-latest"):
        try:
            r = requests.post(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}",
                json={"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"responseMimeType": "application/json", "temperature": 1.0}},
                timeout=150)
            if r.status_code == 200:
                return json.loads(r.json()["candidates"][0]["content"]["parts"][0]["text"])
            print(model, r.status_code, r.text[:200])
        except Exception as e:
            print(model, e)
    return None

FALLBACK = {"slides": ["POV: your weight won't stop going up and down",
  "For years I ate badly. No system, no plan.", "I felt bad all the time. Heavy. Tired. Not me.",
  "Too much weight. Then too little. Then too much again.", "Nothing stuck. So I built myself a simple plan.",
  "Real food. Protein in every meal. That's it.", "Now I feel amazing. And I actually enjoy eating.",
  "I turned it into a free grocery list. Link in bio."],
 "caption": "I didn't need more willpower. I needed a plan. Free high-protein grocery list → link in bio",
 "yt_title": "I didn't need willpower, I needed a plan #shorts",
 "threads": "For years my weight swung up and down and I felt bad all the time.\n\nWhat fixed it wasn't a diet. It was a simple plan: real food, protein in every meal.\n\nNow I feel amazing. Anyone else been on that rollercoaster?"}

def write(angle, recent):
    p = ("You write a short story carousel for TikTok/Instagram for the brand Protein Plate, told in first person by its founder.\n"
         "Use ONLY these true facts (you may rephrase, reorder, dramatize the feeling, but NEVER add new facts, numbers, kg, ages, "
         "diagnoses, medical claims, specific foods, or claims about other people's results):\n- " + "\n- ".join(FACTS) +
         f"\nToday's angle/hook: {angle}\nStructure: hook -> pain (2-3 slides) -> turning point -> the plan -> how I feel now (climax, emotional) -> soft CTA.\n"
         "Audience: busy US women 25-45 who feel stuck with food and weight. Simple, punchy, human words, no hashtags on slides, max 14 words per slide, 7-8 slides. "
         "Last slide: soft CTA to the free High-Protein Grocery List (say 'link in bio').\n"
         f"Do not reuse these recent hooks: {recent}\n"
         "Return ONLY JSON: {\"slides\": [strings], \"caption\": TikTok/IG caption, 1-2 lines + 'Free high-protein grocery list → link in bio' + 4 hashtags, "
         "\"yt_title\": <=90 chars ending with #shorts, \"threads\": the same story as a Threads text post <=450 chars ending with a question to get replies}")
    d = gemini(p)
    if not d or not isinstance(d.get("slides"), list) or len(d["slides"]) < 5: return FALLBACK
    d["slides"] = [str(s).strip() for s in d["slides"]][:8]
    for k in ("caption", "yt_title", "threads"): d.setdefault(k, FALLBACK[k])
    return d

CSS = """@font-face{font-family:Lora;src:url(fonts/Lora-Variable.ttf);font-weight:100 900}
@font-face{font-family:Inter;src:url(fonts/Inter-SemiBold.otf);font-weight:600}
@font-face{font-family:Inter;src:url(fonts/Inter-ExtraBold.otf);font-weight:800}
*{box-sizing:border-box;margin:0}body{margin:0;width:1080px;height:1920px;overflow:hidden;font-family:Inter}
.s{width:1080px;height:1920px;position:relative;display:flex;align-items:center;justify-content:center;padding:120px}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.t{position:relative;font-family:Lora;font-size:92px;line-height:1.15;text-align:center;font-weight:600}
.n{position:absolute;bottom:120px;left:0;right:0;text-align:center;font-weight:800;font-size:30px;letter-spacing:.25em}
.dark{background:#1b1f1c;color:#F3EEE6}.dark .bg{filter:grayscale(1) brightness(.28) blur(10px);transform:scale(1.15)}
.h .t{font-size:112px;font-weight:700}
.photo{color:#fff}.photo .bg{filter:brightness(.55)}.photo .t,.after .t{background:rgba(15,20,17,.62);padding:50px 56px;border-radius:40px;text-shadow:none}
.notes{background:#FFF9E6;color:#222;justify-content:flex-start;align-items:flex-start;padding-top:260px}
.notes .t{font-family:Inter;font-weight:600;font-size:76px;text-align:left}
.notes .bar{position:absolute;top:120px;left:120px;right:120px;font-weight:800;color:#D9A400;font-size:40px}
.after{color:#fff}.after .bg{filter:brightness(.6) saturate(1.15)}
.cta{background:#24452F;color:#fff}.cta .t{color:#fff}.cta em{color:#D9734E;font-style:normal}"""

def slides_html(slides, style, imgs):
    out, n = [], len(slides)
    turn = max(3, n - 4)  # from here on the story turns bright
    for i, txt in enumerate(slides):
        last = i == n - 1
        if last:
            cls, bg = "cta", ""
        elif style == "notes" and i < turn:
            cls, bg = "notes", ""
        elif i < turn:
            cls, bg = ("dark" if style != "photo" else "photo"), imgs[i % len(imgs)]
        else:
            cls, bg = "after", imgs[i % len(imgs)]
        inner = (f"<div class='bar'>Notes</div>" if cls == "notes" else "") + \
                (f"<div class='bg' style=\"background-image:url('img/{bg}')\"></div>" if bg else "") + \
                f"<div class='t'>{E(txt)}</div><div class='n'>PROTEIN PLATE · {i+1}/{n}</div>"
        out.append(f"<div class='s {cls}{' h' if i == 0 else ''}'>{inner}</div>")
    return out

def render(frames, outdir):
    from playwright.sync_api import sync_playwright
    pngs = []
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for i, f in enumerate(frames, 1):
            h = os.path.join(ROOT, f"_story{i}.html")
            open(h, "w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{f}</body></html>")
            pg.goto("file://" + h); pg.wait_for_load_state("networkidle"); pg.wait_for_timeout(300)
            png = os.path.join(outdir, f"slide-{i}.png"); pg.screenshot(path=png); pngs.append(png); os.remove(h)
        b.close()
    return pngs

def video(pngs, out, per=2.6):
    mus = random.choice(sorted(glob.glob(os.path.join(ROOT, "music", "*.mp3"))))
    n = len(pngs); d = 0.35; total = per * n - d * (n - 1)
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for p in pngs: cmd += ["-loop", "1", "-t", str(per), "-i", p]
    cmd += ["-ss", str(random.randint(0, 30)), "-i", mus]
    fc, prev = "", "0:v"
    for i in range(n): fc += f"[{i}:v]scale=1080:1920,fps=30,setsar=1[v{i}];"
    prev = "v0"
    for i in range(1, n):
        fc += f"[{prev}][v{i}]xfade=transition=fade:duration={d}:offset={per*i - d*i:.2f}[x{i}];"; prev = f"x{i}"
    fc += f"[{n}:a]afade=t=in:d=0.6,afade=t=out:st={total-1:.2f}:d=1,volume=0.75[au]"
    cmd += ["-filter_complex", fc, "-map", f"[{prev}]", "-map", "[au]", "-t", f"{total:.2f}",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True)
    return os.path.basename(mus)

def main():
    os.chdir(ROOT)
    try: st = json.load(open(STATE))
    except Exception: st = {"posted": []}
    day = datetime.date.today().isoformat()
    outdir = os.path.join(OUT, day); os.makedirs(outdir, exist_ok=True)
    k = len(st["posted"])
    angle = ANGLES[k % len(ANGLES)]; style = STYLES[k % len(STYLES)]
    recent = [p.get("hook", "") for p in st["posted"][-10:]]
    d = write(angle, recent)
    imgs = random.sample(sorted(os.path.basename(x) for x in glob.glob("img/*.jpg")), 8)
    pngs = render(slides_html(d["slides"], style, imgs), outdir)
    mp4 = os.path.join(outdir, "story.mp4")
    track = video(pngs, mp4)
    meta = {"date": day, "angle": angle, "style": style, "track": track, **d}
    yt = None
    if "--no-yt" not in sys.argv:
        try:
            yt = yt_upload(mp4, {"title": d["yt_title"][:100], "description": d["caption"].replace("link in bio", FREE) + f"\n\n{FREE}",
                                 "tags": ["high protein", "my story", "healthy eating", "weight", "meal plan"]})
        except Exception as e:
            print("YouTube upload failed:", e); meta["youtube_error"] = str(e)[:300]
    meta["youtube"] = yt
    json.dump(meta, open(os.path.join(outdir, "meta.json"), "w"), indent=1)
    st["posted"].append({"date": day, "hook": d["slides"][0], "style": style, "youtube": yt})
    json.dump(st, open(STATE, "w"), indent=1)
    print(json.dumps(meta, indent=1))

if __name__ == "__main__":
    main()
