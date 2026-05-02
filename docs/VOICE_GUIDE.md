# Voice Guide — Sleepy Space Explorer

## Locked Settings

| Setting | Value |
|---------|-------|
| Engine | OpenAI TTS |
| Model | `tts-1-hd` |
| Voice | `fable` |
| Speed | `1.0` — never change |
| Format | `mp3` |

## Why Fable
Fable has a natural storyteller warmth — slightly British, gently expressive. It reads ellipses and line breaks as natural breaths, which is exactly what sleep content needs.

## Why 1.0x Always
Any speed reduction (even 0.85x) via the API introduces time-stretching artifacts that sound robotic. All pacing comes from the script itself — ellipses, line breaks, and short phrases.

## Pacing Technique
- `...` at end of line → short breath pause
- `...` on its own line → longer beat of silence
- Empty line between thoughts → emotional space
- One idea per line → nothing rushes past

## Voice Don'ts
- No coaching affirmations ("good", "well done", "that's right") — the narrator can't see the listener
- No speed post-processing via ffmpeg
- No SSML tags (not supported by OpenAI TTS)
