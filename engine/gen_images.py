"""Generate missing food photos img/<id>.jpg for extra recipes via Gemini image model (runs in GitHub Actions)."""
import os, sys, base64, io, time, random, requests, urllib.parse
from PIL import Image
import extra
KEY = os.environ.get("GEMINI_API_KEY", ""); API = "https://generativelanguage.googleapis.com/v1beta"
ROOT = os.path.dirname(os.path.abspath(__file__))

def image_models():
    names = []
    url = f"{API}/models?key={KEY}&pageSize=200"
    for m in requests.get(url, timeout=60).json().get("models", []):
        n = m["name"].split("/")[-1]
        if "image" in n and "generateContent" in m.get("supportedGenerationMethods", []) and "imagen" not in n:
            names.append(n)
    print("image-capable models:", names)
    pref = sorted(names, key=lambda n: (("preview" in n), ("pro" in n), n))
    return pref

def gen(model, prompt):
    r = requests.post(f"{API}/models/{model}:generateContent?key={KEY}", timeout=180, json={
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"], "imageConfig": {"aspectRatio": "16:9"}}})
    if r.status_code != 200: raise RuntimeError(f"{r.status_code} {r.text[:300]}")
    for p in r.json()["candidates"][0]["content"]["parts"]:
        d = p.get("inlineData") or p.get("inline_data")
        if d: return base64.b64decode(d["data"])
    raise RuntimeError("no image in response")

def pollinations(prompt):
    url = ("https://image.pollinations.ai/prompt/" + urllib.parse.quote(prompt) +
           f"?width=1400&height=788&model=flux&nologo=true&seed={random.randint(1, 99999)}")
    for i in range(4):
        r = requests.get(url, timeout=240)
        if r.status_code == 200 and r.headers.get("content-type", "").startswith("image"): return r.content
        print("pollinations", r.status_code, r.text[:150]); time.sleep(20)
    raise RuntimeError("pollinations failed")

def main():
    only = sys.argv[1:]
    models = image_models() if os.environ.get("USE_GEMINI") else []
    models.append("pollinations")
    made = fail = 0
    for r in extra.XR:
        if only and r["id"] not in only: continue
        out = os.path.join(ROOT, "img", f"{r['id']}.jpg")
        if os.path.exists(out): continue
        for model in models:
            try:
                raw = pollinations(extra.photo_prompt(r)) if model == "pollinations" else gen(model, extra.photo_prompt(r))
                im = Image.open(io.BytesIO(raw)).convert("RGB")
                w, h = im.size; th = int(w * 781 / 1400)
                if h > th: im = im.crop((0, (h - th) // 2, w, (h - th) // 2 + th))
                im.resize((1400, 781), Image.LANCZOS).save(out, quality=88)
                print("OK", r["id"], model); made += 1; break
            except Exception as e:
                print("FAIL", r["id"], model, e)
        else:
            fail += 1
        time.sleep(16)
    print(f"made={made} failed={fail}")

if __name__ == "__main__":
    main()
