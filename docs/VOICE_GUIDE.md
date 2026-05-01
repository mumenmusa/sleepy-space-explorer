# 🎙️ Voice Guide

## Chosen Voice: ElevenLabs — Fable

After testing OpenAI TTS voices (all speeds), **ElevenLabs with Fable** is the confirmed production voice.

- **Why ElevenLabs:** Dramatically more natural and warm than OpenAI TTS — no robotic processing artifacts
- **Why Fable:** Warm storyteller quality, perfect for bedtime narration
- **OpenAI TTS rejected:** All speeds (0.75x, 0.85x, 1.0x) had a robotic echo/processing quality
- **Lesson:** OpenAI TTS speed reduction below 0.9x introduces heavy artifacts; even at 1.0x the voice processing sounds synthetic for long-form narration

## TTS Settings

| Setting | Value |
|---------|-------|
| Model | `tts-1-hd` |
| Voice | `fable` |
| Speed | `0.75` |
| Format | `mp3` |

## Generation Script

```bash
OPENAI_KEY=$(cat ~/.config/openai/api_key.txt)

# Generate a chunk (max ~4096 chars per API call)
curl -s https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1-hd",
    "input": "<SCRIPT_TEXT>",
    "voice": "fable",
    "speed": 0.75
  }' \
  --output episodes/ep01/narration-part1.mp3
```

## Chunking Long Scripts

OpenAI TTS has a ~4096 character limit per call. For a 30-min episode (~4,500 words):

1. Split script at natural paragraph breaks into chunks of ~3,000 chars
2. Generate each chunk as a separate MP3
3. Concatenate with ffmpeg:

```bash
# Create file list
ls episodes/ep01/narration-part*.mp3 | sort > /tmp/parts.txt
ffmpeg -f concat -safe 0 -i /tmp/parts.txt -c copy episodes/ep01/narration-full.mp3
```

## Adding Ambient Audio

Layer soft background audio under narration:

```bash
# Mix narration (0 dB) with ambient (reduced to -20 dB)
ffmpeg \
  -i episodes/ep01/narration-full.mp3 \
  -i assets/ambient-space-hum.mp3 \
  -filter_complex "[1:a]volume=0.15[bg];[0:a][bg]amix=inputs=2:duration=first" \
  episodes/ep01/narration-with-ambient.mp3
```

## Narration Style Tips

Write the script with pauses in mind:

- Use `...` for natural breathing pauses
- Short sentences. One idea at a time.
- Repeat calming phrases gently ("And you are safe... so very safe...")
- End sections with a long ellipsis or soft landing phrase
