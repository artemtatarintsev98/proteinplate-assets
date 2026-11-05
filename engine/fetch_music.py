"""Download royalty-free tracks (Pixabay Content License: free commercial use, no attribution) listed in music_urls.txt.
URLs are collected from Pixabay search in a real browser (Pixabay pages block datacenter IPs; the CDN does not)."""
import os, requests
ROOT = os.path.dirname(os.path.abspath(__file__)); DIR = os.path.join(ROOT, "music")
H = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/128 Safari/537.36", "Referer": "https://pixabay.com/"}
got = 0
for line in open(os.path.join(ROOT, "music_urls.txt")):
    if not line.strip(): continue
    tag, url = line.split()
    name = f"pixabay-{tag}-{url.split('_')[-1]}"
    path = os.path.join(DIR, name)
    if os.path.exists(path): continue
    r = requests.get(url, headers=H, timeout=120)
    print(r.status_code, len(r.content), name)
    if r.status_code == 200 and 300_000 < len(r.content) < 12_000_000:
        open(path, "wb").write(r.content); got += 1
print("downloaded", got)
