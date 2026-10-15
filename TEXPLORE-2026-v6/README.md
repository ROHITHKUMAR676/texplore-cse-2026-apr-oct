# TEXPLORE 2026 — REC CSE Magazine (animated flipbook) — v2

## Open it
Double-click `index.html` (Chrome, Edge, Safari or Firefox). Everything runs offline: the page-flip library is in `vendor/`, fonts are in `fonts/`, and all photos are embedded in `index.html`.

## Controls
- Click "Open the magazine" after the logo intro (Enter also works, "Skip intro" skips it).
- Flip: drag a page corner, click the page edge, use ← → keys or the Prev / Next buttons.
- Adhi (the mascot) talks about ONE page at a time: left page first, then right page, then waits for you to flip. Click a highlighted photo or Adhi to hear about it. "Mascot guide" button (or the G key) turns the auto-talk on/off.

## What's new in v2
- **Adhi talks.** He now speaks every bubble aloud, one page at a time, with a speech-synced glow, equalizer bars and a talking bounce. Voice on/off button and a voice picker are in the bottom bar.
  The voice comes from your browser/OS, so quality depends on it: Microsoft Edge (Natural / Online voices such as "Prabhat" or "Ravi" for Indian English) sounds the most human on Windows; Chrome uses Google voices; Safari/iPhone use Apple voices (download an "Enhanced" or "Premium" voice in system settings). The picker lists the best English voices first and remembers your choice.
- **Your own voice (optional).** `adhi-script.txt` lists every line Adhi says with an ID. Record or generate audio for each line, save as `audio/<ID>.mp3`, then set `window.ADHI_AUDIO=true` near the end of `index.html`. Missing files fall back to the browser voice.
- **New cover:** a wall of event photos behind TEXPLORE 2026, the department name and the tagline. `TEXPLORE-2026-cover.png` is the same cover as a high-resolution image.

## Folder map
- `index.html` — the finished magazine (self-contained).
- `TEXPLORE-2026-cover.png` — cover as an image.
- `adhi-script.txt` and `audio/` — Adhi's lines and the drop-in folder for your own audio.
- `vendor/` — StPageFlip 2.0.7 (MIT).
- `fonts/` — Unbounded + Figtree (OFL, via @fontsource).
- `assets/originals/` — everything you supplied (PDF, logos, mascot, smoke backgrounds).
- `assets/logos/`, `assets/mascot/`, `assets/backgrounds/` — the same, organised; `mascot/adhi-facing-left.png` is the mirrored pose with the jacket "R" corrected.
- `assets/extracted-from-pdf/` — every photo/poster pulled out of CSE_PPT.pdf at full resolution (file name = `p-<pdf page>-<image id>`).
- `source/` — build scripts: `assets.py` (picks/compresses photos into `assets.json`), `build.py` (writes `index.html`; page layouts are in it), `style.css`, `app.js`.

## Rebuild after editing
```
cd source
pip install pillow
python3 assets.py     # only if you changed photos
MODE=zip python3 build.py
```
Page layouts live in `source/build.py`; photo keys such as `iwdc` or `kba3` map to files in `assets.py`.

## Placeholders (fill later)
Pages 3 (HoD photo/message) and 25 (Meet the Team). v7 adds: About the Department (p2), Editors’ Desk (p4), edition line on cover and last page.
