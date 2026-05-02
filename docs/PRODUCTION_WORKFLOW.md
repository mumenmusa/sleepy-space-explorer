# Production Workflow — Sleepy Space Explorer

Follow this process for every episode, start to finish.

---

## Phase 1 — Script Writing

### Voice & Tone Rules

#### 🌟 Story-First, Not Meditation-First (core principle)
- **The listener is IN the story** — they are experiencing an adventure, not being coached through relaxation exercises
- **Sensory adventure narrative** — describe what the explorer sees, hears, touches, smells; let the story carry them to sleep
- **Gentle awe and wonder** — "oh wow, look at that" energy; calm delight, not instruction
- **Narrative over body coaching** — don't say "let your legs be heavy" or "feel your breath" — instead describe what the explorer is doing/seeing and let the sleepiness come naturally from the story
- **Think: bedtime story that makes you sleepy, not a guided meditation**
- ✅ Right: *"The little explorer's boots crunched on the silver dust. Ahead, a crater the size of a swimming pool glowed faintly blue..."*
- ❌ Wrong: *"Feel the weight of your legs. Let them be heavy. Think about your day..."*

#### Pacing & Formatting
- **Narrator is a presence, not a coach** — never say "Good", "That's great", "Well done" — the narrator can't see the listener
- **One idea per line** — never run two thoughts together on the same line
- **Short phrases** — if a sentence can be split in two, split it
- **Ellipses as pauses** — use `...` at the end of a line to signal a natural breath/pause
- **`...` on its own line** — adds a longer beat of silence between thoughts (use generously)
- **Empty lines between beats** — every emotional moment gets a full empty line before and after
- **Repetition is good** — lingering on a feeling ("Let them rest. ... Let them rest.") is intentional
- **No information density** — this is not a story with plot twists; every section should feel like it could go on forever
- **Imagery over instruction** — describe what the listener sees/experiences, don't tell them what to do next

### Script Structure (per episode)
1. **INTRO** — the world before liftoff; ground the listener in a familiar, sensory place
2. **DEPARTURE** — the explorer discovers the spacecraft and lifts off gently
3. **JOURNEY** — ascending through clouds, then into deep space; slow drift and wonder
4. **ARRIVAL** — the destination reveals itself; landing is soft and quiet
5. **EXPLORATION** — the explorer moves through the world; sensory detail, slow pacing
6. **STILLNESS** — the explorer finds a place to rest within the story world; the story simply... slows... and drifts

#### 🌙 Ending Rule (added 2026-05-01)
- **End inside the story — never instruct the listener to sleep**
- The episode ends as a narrative moment, not a coaching cue
- The explorer simply gets very still, very quiet, in the story world — and the narrator's voice fades with the story
- ✅ Right: *"She leaned back against the moon rock. The stars were so many. And so quiet. And she was..."*
- ❌ Wrong: *"Sleep now, little explorer. Let your eyes close. Drift off to sleep."*
- The listener falls asleep inside the adventure, not because they were told to

### Target Length
- ~22,000 chars / ~20 min per episode (calibration: ~1,100 chars ≈ 1 min at Fable 1.0x)
- Split into 18–22 chunks of ≤ 4,096 chars each

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
| Story-first — listener is IN the adventure | Coach listener through relaxation exercises |
| Sensory details (crunch of moon dust, glow of stars) | "Let your legs be heavy", "feel your breath" |
| Gentle awe and wonder | Body scan / meditation language |
| One idea per line | Run thoughts together |
| `...` on its own line for long pauses | Use ffmpeg speed changes |
| Repeat phrases to linger | Add coaching words ("good", "well done") |
| Short, broken sentences | Write dense paragraphs |
| Narrative imagery over instruction | Information density or plot twists |
| End inside the story (explorer rests, world goes still) | "Sleep now", "close your eyes", "drift off" |
| Aim for ~20 min per episode (~22,000 chars) | Episodes shorter than 15 min |
| Fable 1.0x always | Any speed param other than 1.0 |
