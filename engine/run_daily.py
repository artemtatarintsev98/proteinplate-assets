"""Daily job: render the next recipe Reel/Short and publish it.
Runs in GitHub Actions. Secrets (env): GEMINI_API_KEY, YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN.
No Claude involved. Missing secrets -> that step is skipped, the video is still rendered and saved to ../reels/."""
import os, json, sys, re, requests
from data import R
from build import M
from reel import render
from mkreel import make

FREE = "https://proteinplatehq.gumroad.com/l/free-grocery-list"
ROOT = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(ROOT, "state.json")
REELS = os.path.join(ROOT, "..", "reels")

def load_state():
    try: return json.load(open(STATE))
    except Exception: return {"posted": []}

def next_recipe(state):
    ids = [r["id"] for r in R]
    done = [p["id"] for p in state["posted"]]
    for rid in ids:
        if rid not in done: return rid
    # all done once -> start a new round with the oldest one
    return state["posted"][0]["id"] if not done else min(ids, key=lambda i: max(j for j,p in enumerate(state["posted"]) if p["id"]==i))

def caption(r, m):
    base = {
        "title": f"{r['name']} — {m[1]}g protein #shorts",
        "description": (f"{r['name']}: {m[1]} g protein, {m[0]} kcal, ready in {r['mins']} minutes.\n\n"
                        f"Free high-protein grocery list + 3 sample days at ~125 g protein: {FREE}\n\n"
                        "#highprotein #mealprep #healthyrecipes #proteinrecipes #easyrecipes"),
        "tags": ["high protein", "meal prep", "healthy recipes", "protein recipes", "easy dinner"],
    }
    key = os.environ.get("GEMINI_API_KEY")
    if not key: return base
    prompt = (
        "Write YouTube Shorts metadata for a high-protein recipe video by the brand Protein Plate. "
        "Audience: busy US women who want to eat more protein. Honest, no medical claims, no fake reviews.\n"
        f"Recipe: {r['name']} | {m[1]} g protein | {m[0]} kcal | {r['mins']} min | meal: {r['meal']}\n"
        f"Ingredients: {', '.join(n for n,_ in r['ings'])}\n"
        "Return ONLY JSON: {\"title\": <=90 chars, curiosity hook, include protein grams, end with #shorts>, "
        "\"description\": 2-3 short lines + a line 'Free high-protein grocery list: LINK' + 5 hashtags, "
        "\"tags\": up to 10 short keyword strings}")
    try:
        res = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={key}",
            json={"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"responseMimeType": "application/json"}},
            timeout=60)
        res.raise_for_status()
        txt = res.json()["candidates"][0]["content"]["parts"][0]["text"]
        d = json.loads(txt)
        d["description"] = d["description"].replace("LINK", FREE)
        if FREE not in d["description"]: d["description"] += f"\n\nFree high-protein grocery list: {FREE}"
        d["title"] = d["title"][:100]
        return {**base, **{k: d[k] for k in ("title", "description", "tags") if d.get(k)}}
    except Exception as e:
        print("Gemini failed, using template:", e)
        return base

def yt_token():
    cid, sec, ref = (os.environ.get(k) for k in ("YT_CLIENT_ID", "YT_CLIENT_SECRET", "YT_REFRESH_TOKEN"))
    if not (cid and sec and ref): return None
    r = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": cid, "client_secret": sec, "refresh_token": ref, "grant_type": "refresh_token"}, timeout=30)
    r.raise_for_status(); return r.json()["access_token"]

def yt_upload(path, meta):
    tok = yt_token()
    if not tok: print("YouTube secrets missing -> skip upload"); return None
    body = {"snippet": {"title": meta["title"], "description": meta["description"], "tags": meta["tags"], "categoryId": "26"},
            "status": {"privacyStatus": "public", "selfDeclaredMadeForKids": False, "containsSyntheticMedia": True}}
    init = requests.post("https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
                         headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json",
                                  "X-Upload-Content-Type": "video/mp4"}, json=body, timeout=60)
    init.raise_for_status()
    up = requests.put(init.headers["Location"], data=open(path, "rb"), headers={"Content-Type": "video/mp4"}, timeout=600)
    up.raise_for_status(); vid = up.json()["id"]; print("YouTube video:", vid); return vid

def main():
    os.chdir(ROOT); os.makedirs(REELS, exist_ok=True)
    state = load_state()
    rid = sys.argv[1] if len(sys.argv) > 1 else next_recipe(state)
    r = next(x for x in R if x["id"] == rid); m = M[rid]
    pngs = render(rid)
    out = os.path.join(REELS, f"{rid}.mp4")
    track = make(rid, pngs, out)
    meta = caption(r, m)
    entry = {"id": rid, "track": track, "title": meta["title"]}
    try:
        entry["youtube"] = yt_upload(out, meta)
    except Exception as e:
        print("YouTube upload failed:", e); entry["youtube_error"] = str(e)[:300]
    if entry.get("youtube"):
        state["posted"].append(entry)
    else:
        state.setdefault("rendered_only", []).append(entry)
    json.dump(state, open(STATE, "w"), indent=1)
    print(json.dumps(entry, indent=1))

if __name__ == "__main__":
    main()
