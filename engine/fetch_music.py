"""Download extra royalty-free tracks from Pixabay Music (Pixabay Content License: free commercial use, no attribution)."""
import os, re, sys, time, requests
ROOT = os.path.dirname(os.path.abspath(__file__)); DIR = os.path.join(ROOT, "music")
QUERIES = ["acoustic happy", "lofi chill", "upbeat ukulele", "inspiring piano", "feel good", "positive morning",
           "chill guitar", "soft indie", "summer acoustic", "hopeful"]
H = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36",
     "Accept-Language": "en-US,en;q=0.9"}
want = int(sys.argv[1]) if len(sys.argv) > 1 else 24
have = set(os.listdir(DIR)); got = 0
for q in QUERIES:
    if got >= want: break
    url = f"https://pixabay.com/music/search/{requests.utils.quote(q)}/?duration=0-180"
    r = requests.get(url, headers=H, timeout=60); print(q, r.status_code, len(r.text))
    links = list(dict.fromkeys(re.findall(r'https://cdn\.pixabay\.com/(?:download/)?audio/[^"\'\s\\]+?\.mp3', r.text)))
    print("  found", len(links))
    for link in links[:4]:
        name = re.sub(r"[^a-z0-9.-]+", "-", link.split("/")[-1].split("?")[0].lower())
        if name in have: continue
        a = requests.get(link, headers=H, timeout=120)
        if a.status_code == 200 and 300_000 < len(a.content) < 9_000_000:
            open(os.path.join(DIR, name), "wb").write(a.content); have.add(name); got += 1; print("  +", name)
        time.sleep(2)
    time.sleep(3)
print("downloaded", got)
