#!/usr/bin/env python3
"""
Generate per-chunk MP3 audio from a script.md file using OpenAI TTS.
Usage: python3 scripts/generate_audio.py <script.md> <audio_output_dir/>
"""
import sys, os, re, pathlib, time

OPENAI_KEY_FILE = "/Users/mini-1/.config/openai/api_key.txt"
MODEL = "tts-1-hd"
VOICE = "fable"
SPEED = 1.0
CHUNK_LIMIT = 4096

def load_key():
    with open(OPENAI_KEY_FILE) as f:
        return f.read().strip()

def parse_chunks(script_path):
    with open(script_path) as f:
        content = f.read()
    parts = re.split(r'\n---\n', content)
    chunks = [c.strip() for c in parts[1:] if c.strip()]
    return chunks

def generate_chunk(key, text, out_path):
    import urllib.request, json
    if os.path.exists(out_path):
        size = os.path.getsize(out_path)
        print(f"  skip (exists, {size} bytes)")
        return
    payload = json.dumps({"model": MODEL, "input": text, "voice": VOICE, "speed": SPEED}).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/audio/speech",
        data=payload,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    with open(out_path, "wb") as f:
        f.write(data)
    print(f"  done — {len(data):,} bytes -> {out_path}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 generate_audio.py <script.md> <audio_dir/>")
        sys.exit(1)
    script_path, audio_dir = sys.argv[1], sys.argv[2]
    pathlib.Path(audio_dir).mkdir(parents=True, exist_ok=True)
    key = load_key()
    chunks = parse_chunks(script_path)
    print(f"Parsed {len(chunks)} chunks from {script_path}")
    for i, chunk in enumerate(chunks, 1):
        if len(chunk) > CHUNK_LIMIT:
            print(f"  ⚠️  Part {i:02d} is {len(chunk)} chars — over limit!")
        out_path = os.path.join(audio_dir, f"part{i:02d}.mp3")
        print(f"Part {i:02d} ({len(chunk)} chars)...")
        generate_chunk(key, chunk, out_path)
        time.sleep(0.3)
    print("\nAll chunks done.")

if __name__ == "__main__":
    main()
