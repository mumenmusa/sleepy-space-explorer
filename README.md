# 🚀 Sleepy Space Explorer

A kids' bedtime sleep podcast on YouTube — calm, slow-paced space storytelling designed to help children drift off to sleep.

**Format:** 30-minute narrated stories, soft ambient audio, static visual  
**Target age:** 5–10 years  
**Voice:** OpenAI TTS (Shimmer voice, 0.80x speed)  
**Art:** AI-generated album artwork per episode  

## Channel Concept

Sleepy Space Explorer delivers soothing bedtime stories set in the cosmos — gentle journeys to the moon, drifting through Saturn's rings, floating on a space station. No action, no suspense. Just calm, wonder, and sleep.

## Project Structure

```
sleepy-space-explorer/
├── episodes/
│   └── ep01/
│       ├── script.md          # Full narration script
│       ├── metadata.md        # Title, description, tags, thumbnail prompt
│       └── art-prompt.md      # Image generation prompt for cover art
├── art/                       # Generated cover art (not tracked in git — add to .gitignore if large)
├── scripts/                   # Production helper scripts
├── docs/
│   ├── PLAN.md               # Full channel plan + production pipeline
│   ├── VOICE_GUIDE.md        # Voice settings + TTS workflow
│   └── EPISODE_IDEAS.md      # Story ideas backlog
└── README.md
```

## Production Pipeline

1. **Write** — draft script in `episodes/epNN/script.md`
2. **Voice** — run TTS via OpenAI API (Shimmer, 0.80x speed)
3. **Art** — generate cover image from `art-prompt.md`
4. **Audio** — combine narration + soft ambient background (rain, space hum)
5. **Video** — static image + audio → YouTube upload
6. **Publish** — use metadata from `metadata.md` for title, description, tags

## Voice Settings

- **Model:** `tts-1-hd`
- **Voice:** `shimmer` (OpenAI's softest voice)
- **Speed:** `0.80`
- **Format:** MP3

## Episode Ideas Backlog

See `docs/EPISODE_IDEAS.md`

---

*Part of the Toolups LLC content portfolio.*
