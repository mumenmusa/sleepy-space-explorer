# Production Workflow — Sleepy Space Explorer

Follow this process for every episode, start to finish.

---

## Phase 1 — Script Writing

### Voice & Tone Rules
- **Narrator is a presence, not a coach** — never say "Good", "That's great", "Well done" — the narrator can't see the listener
- **One idea per line** — never run two thoughts together on the same line
- **Short phrases** — if a sentence can be split in two, split it
- **Ellipses as pauses** — use `...` at the end of a line to signal a natural breath/pause
- **`...` on its own line** — adds a longer beat of silence between thoughts (use generously)
- **Empty lines between beats** — every emotional moment gets a full empty line before and after
- **Repetition is good** — lingering on a feeling ("Let them rest. ... Let them rest.") is intentional
- **No information density** — this is not a story with plot twists; every section should feel like it could go on forever
- **Imagery over instruction** — describe what the listener feels/sees, don't tell them what to do next

### Script Structure (per episode)
1. **INTRO** — breathing invitation, settle into the body
2. **PART 1** — body scan / settling in (arms heavy, legs heavy, eyes heavy)
3. **PART 2** — liftoff / transition to journey
4. **PART 3** — first wonder moment (clouds, stars, deep space, etc.)
5. **PART 4** — deep journey (the main location / destination)
6. **PART 5** — arrival / landing
7. **PART 6** — stillness at the destination
8. **WIND-DOWN** — eyes heavy, body sinking, drift to sleep

### Target Length
- ~4,500–5,000 words for a ~30 min episode
- The intro alone (phases 1–2) should run ~8–10 min

---

## Phase 2 — Audio Generation

### TTS Settings (locked)
- **Engine:** OpenAI TTS
- **Model:** `tts-1-hd`
- **Voice:** `fable`
- **Speed:** `1.0` — **never adjust speed**; pacing comes entirely from the script
- **No post-processing speed changes** — ffmpeg `atempo` introduces robotic artifacts even at 0.85x

### Chunking
- Split script at `---` section dividers
- Each chunk must be ≤ 4,096 characters
- Generate each chunk separately, then concatenate with ffmpeg

### Concatenation
```bash
# Build file list
ls episodes/epXX/audio/part*.mp3 | sort > /tmp/epXX-parts.txt
sed -i '' "s|^|file '|; s|$|'|" /tmp/epXX-parts.txt

# Concatenate
ffmpeg -f concat -safe 0 -i /tmp/epXX-parts.txt \
  -acodec copy episodes/epXX/audio/narration-epXX-final.mp3
```

---

## Phase 3 — Review & QA

1. Listen to the full narration
2. Check for any rushed sections — if a section feels fast, add more `...` lines to the script and regenerate that chunk only
3. Verify no reactive affirmations ("good", "well done", "that's right") slipped in
4. Check transitions between chunks sound seamless

---

## Phase 4 — Ambient Mix (future)

- Layer soft space ambient audio at -20dB under the voice
- Fade in at start, fade out at end
- No music with melody — only texture/hum/white noise
- Tools: ffmpeg `amix` filter

---

## Phase 5 — Publishing

1. Generate cover art (see `episodes/epXX/art-prompt.md`)
2. Export final mixed MP3
3. Upload to YouTube as a static video (cover art as visual)
4. Use metadata from `episodes/epXX/metadata.md` for title/description/tags
5. Commit script + metadata to GitHub (audio excluded via `.gitignore`)

---

## Quick Reference — Do's and Don'ts

| ✅ Do | ❌ Don't |
|-------|---------|
| One idea per line | Run thoughts together |
| `...` on its own line for long pauses | Use ffmpeg speed changes |
| Repeat phrases to linger | Add coaching words ("good", "well done") |
| Short, broken sentences | Write dense paragraphs |
| Imagery and sensation | Plot or action |
| Fable 1.0x always | Any speed param other than 1.0 |
