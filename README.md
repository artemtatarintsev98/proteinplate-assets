# Protein Plate — automation

- Root `*.jpg`: Pinterest pin images (public URLs used by scheduled pins — do not move).
- `engine/`: recipes (`data.py`), Reel renderer (`reel.py` + `mkreel.py`), daily job `run_daily.py`.
- `reels/`: rendered videos (public URLs, reused for Instagram/TikTok APIs later).
- `.github/workflows/daily-reel.yml`: every day renders the next recipe Short and uploads it to YouTube.

Secrets (Settings → Secrets and variables → Actions):
`GEMINI_API_KEY`, `YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN`.
