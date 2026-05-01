# 🎙️ Voice Guide

## Chosen Voice: Shimmer

After testing all 5 OpenAI TTS voices (Alloy, Echo, Fable, Onyx, Nova) and slower variations, **Shimmer** was selected as the production voice for Sleepy Space Explorer.

- **Why Shimmer:** OpenAI's softest voice — hushed, gentle, perfect for bedtime
- **Runner-up:** Fable (storyteller warmth) or Nova (soothing)

## TTS Settings

| Setting | Value |
|---------|-------|
| Model | `tts-1-hd` |
| Voice | `shimmer` |
| Speed | `0.80` |
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
    "voice": "shimmer",
    "speed": 0.80
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
