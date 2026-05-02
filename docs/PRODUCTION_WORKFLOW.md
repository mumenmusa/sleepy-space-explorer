# Production Workflow — Sleepy Space Explorer

Follow this process for every episode, start to finish.

⚠️ **Gated workflow — stop and wait for approval at each phase before proceeding.**
Do not run all the way to MP4 in one shot. Each phase requires Mumen's explicit sign-off.

---

## Phase 1 — Script Writing (STOP — await approval before Phase 2)

### Voice & Tone Rules

#### 🌟 Story-First, Not Meditation-First (core principle)
- **The listener is IN the story** — they are experiencing an adventure, not being coached through relaxation exercises
- **Sensory adventure narrative** — describe what the explorer sees, hears, touches, smells; let the story carry them to sleep
- **Gentle awe and wonder** — "oh wow, look at that" energy; calm delight, not instruction
- **Narrative over body coaching** — don't say "let your legs be heavy" or "feel your breath" — instead describe what the explorer is doing/seeing and let the sleepiness come naturally from the story
- **Think: bedtime story that makes you sleepy, not a guided meditation**
- ✅ Right: *"The little explorer's boots crunched on the silver dust. Ahead, a crater the size of a swimming pool glowed faintly blue..."*
- ❌ Wrong: *"Feel the weight of your legs. Let them be heavy. Think about your day..."*

#### Script File Structure
- **Section headers (`## Part 01 — ...`) are internal script markers only** — they must never appear in TTS chunk text
- When splitting into TTS chunks, strip all headers before sending to the API
- **Section breaks in the audio = long pause cluster** — use 3–5 `...` lines on their own to create a natural breath between story beats; never announce a new section
- ✅ Right: strip header, start chunk with the first line of narration
- ❌ Wrong: feeding `## Part 03 — Liftoff` into TTS (it will be read aloud as "Part 03, hashtag hashtag Liftoff")

#### Episode Independence
- **Each episode is self-contained** — a listener can start at any episode and feel complete
- **No callbacks to previous episodes** — never reference "last time" or "remember when we visited the Moon"
- **Shared world elements are fine** — the backyard, the spacecraft, the explorer can recur, but woven in as part of the world, not as explicit continuity
- **Subtle, not serial** — if two episodes share a detail, it should feel like a familiar texture, not a reminder

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

### Phase 1 Deliverable
- Post the full script as a `.md` file upload to Slack (thread reply)
- Include char count, estimated duration, and chunk count in the message
- Ask: *"Script ready for review — approve to proceed to audio?"*
- **Wait for explicit approval before moving to Phase 2**

---

## Phase 2 — Audio Generation (STOP — await approval before Phase 3)

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

### Phase 2 Deliverable
- Upload the 128k MP3 narration to Slack (thread reply)
- Include duration in the message
- Ask: *"Narration ready — approve to proceed to art + video?"*
- **Wait for explicit approval before moving to Phase 3**

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

## Phase 5 — Cover Art

### Style (locked from ep01)
- **Model:** `openai/gpt-image-1` (OpenAI image generation v2)
- **Style:** Pixar-storybook — bold, clean, friendly, slightly cartoonish but warm and detailed
- **Palette:** Deep midnight blue, warm golds, soft silver — rich but calming
- **Character:** Cute kid explorer with a face and personality — gives ages 6–8 something to connect with
- **Mood:** Curious and cozy, not scared or excited
- **Format:** 1024×1024 square
- **No text in image** — title goes on YouTube as overlay/thumbnail text if needed

### 3-Scene Video Art (for YouTube MP4)
Generate 3 illustrations following the story arc:
1. **Scene 1 — The World Before** — familiar, grounded setting (backyard, forest, beach — wherever the episode starts)
2. **Scene 2 — The Journey** — in transit; spacecraft interior, clouds, deep space, underwater, etc.
3. **Scene 3 — The Destination** — arrived and at rest; moon surface, forest floor, ocean shelf, etc.

Each scene holds for ~1/3 of the episode duration. Concatenate with ffmpeg (no crossfade needed — simple cut is fine).

### Video Assembly Command
```bash
# 1. Render each scene as a silent clip (~1/3 of audio duration each, 4fps)
DUR=$(ffprobe -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 narration.mp3 | awk '{printf "%d", $1/3}')
ffmpeg -y -loop 1 -t $DUR -i scene1.png -vf "scale=1024:1024,format=yuv420p" -r 4 -c:v libx264 -preset ultrafast -crf 28 /tmp/clip1.mp4
ffmpeg -y -loop 1 -t $DUR -i scene2.png -vf "scale=1024:1024,format=yuv420p" -r 4 -c:v libx264 -preset ultrafast -crf 28 /tmp/clip2.mp4
ffmpeg -y -loop 1 -t $DUR -i scene3.png -vf "scale=1024:1024,format=yuv420p" -r 4 -c:v libx264 -preset ultrafast -crf 28 /tmp/clip3.mp4

# 2. Concatenate clips + add narration audio
printf "file '/tmp/clip1.mp4'\nfile '/tmp/clip2.mp4'\nfile '/tmp/clip3.mp4'\n" > /tmp/clips.txt
ffmpeg -y -f concat -safe 0 -i /tmp/clips.txt -i narration.mp3 \
  -map 0:v -map 1:a -c:v libx264 -preset fast -crf 26 -c:a aac -b:a 128k -shortest \
  ep-youtube.mp4
```
⚠️ Use `-r 4` (4fps) for still-image clips — keeps file size small. Do NOT use xfade filter on still images — it's too slow.

---

## Phase 6 — Publishing

### YouTube Upload Checklist
1. **File:** MP4 (H.264 + AAC) — YouTube does not accept MP3
2. **Thumbnail:** Use Scene 3 (destination/rest) or a dedicated cover image — Pixar-storybook style, face visible
3. **Title format:** `[Episode Title] 🌙 | Sleepy Space Explorer Ep. [N] | Kids Bedtime Story`
4. **Description template:**
```
[1-2 sentence hook — what happens in this episode]

This is a calm, story-first bedtime podcast for kids ages 5–10. No body-scan coaching — just a slow, wonder-filled adventure that carries your little one gently to sleep.

🌙 Perfect for:
- Bedtime wind-down
- Naptime
- Calm listening anytime

🚀 New episodes coming soon — subscribe so you don't miss them!

---
Sleepy Space Explorer is a kids' bedtime podcast full of gentle adventures through space, nature, and dreamlike worlds. Each episode is a slow, sensory story designed to carry children peacefully to sleep.
```
5. **Tags:** kids bedtime story, bedtime podcast for kids, sleep story for kids, kids meditation, space story for kids, calm kids podcast, children's podcast, ages 5-8
6. **Category:** Education
7. **Made for Kids:** ✅ Yes — required; affects YouTube Kids eligibility
8. **Visibility:** Public
9. **Commit** script + metadata to GitHub after publishing (audio/video excluded via `.gitignore`)

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
