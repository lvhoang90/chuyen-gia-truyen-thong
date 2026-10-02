#!/usr/bin/env python3
"""Sinh voice-over qua ElevenLabs hoặc Azure Speech.

Khóa API đọc từ biến môi trường (xem .env.example). Chỉ dùng thư viện chuẩn.

Ví dụ:
  python scripts/tts.py --provider elevenlabs --voice <voice_id> --text-file s01.txt --out audio/vo/S01.vi.mp3
  python scripts/tts.py --provider azure --lang vi --text-file s01.txt --out audio/vo/S01.vi.mp3
"""
import argparse
import os
import sys
import urllib.error
import urllib.request
import json
from xml.sax.saxutils import escape

AZURE_DEFAULT_VOICES = {"vi": "vi-VN-HoaiMyNeural", "en": "en-US-AvaMultilingualNeural"}


def die(msg):
    sys.exit(f"Lỗi: {msg}")


def env(name):
    v = os.environ.get(name)
    if not v:
        die(f"thiếu biến môi trường {name}")
    return v


def post(url, headers, body):
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        die(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:500]}")


def elevenlabs(text, voice, model, stability, similarity, style):
    if not voice:
        die("ElevenLabs cần --voice <voice_id>")
    body = json.dumps({
        "text": text,
        "model_id": model,
        "voice_settings": {
            "stability": stability,
            "similarity_boost": similarity,
            "style": style,
            "use_speaker_boost": True,
        },
    }).encode()
    headers = {
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    # Có biến môi trường thì gửi khóa; nếu không, dựa vào credential của môi trường
    # (hệ thống tự chèn header xi-api-key cho api.elevenlabs.io).
    key = os.environ.get("ELEVENLABS_API_KEY")
    if key:
        headers["xi-api-key"] = key
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128"
    return post(url, headers, body)


def azure(text, voice, lang, rate, ssml):
    region = env("AZURE_SPEECH_REGION")
    voice = voice or AZURE_DEFAULT_VOICES[lang]
    xml_lang = "vi-VN" if lang == "vi" else "en-US"
    if ssml:
        body_xml = text  # người dùng tự cung cấp SSML hoàn chỉnh
    else:
        body_xml = (
            f"<speak version='1.0' xml:lang='{xml_lang}' "
            f"xmlns='http://www.w3.org/2001/10/synthesis'>"
            f"<voice name='{voice}'><prosody rate='{rate}'>{escape(text)}</prosody></voice></speak>"
        )
    headers = {
        "Ocp-Apim-Subscription-Key": env("AZURE_SPEECH_KEY"),
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-48khz-192kbitrate-mono-mp3",
        "User-Agent": "chuyen-gia-truyen-thong",
    }
    url = f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1"
    return post(url, headers, body_xml.encode("utf-8"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--provider", choices=["elevenlabs", "azure"], required=True)
    ap.add_argument("--lang", choices=["vi", "en"], default="vi")
    ap.add_argument("--voice", help="voice_id (ElevenLabs) hoặc tên giọng (Azure)")
    ap.add_argument("--text-file", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="eleven_multilingual_v2")
    ap.add_argument("--stability", type=float, default=0.5)
    ap.add_argument("--similarity", type=float, default=0.75)
    ap.add_argument("--style", type=float, default=0.2)
    ap.add_argument("--rate", default="0%", help="Azure prosody rate, ví dụ -5%%")
    ap.add_argument("--ssml", action="store_true", help="--text-file là SSML hoàn chỉnh (Azure)")
    a = ap.parse_args()

    text = open(a.text_file, encoding="utf-8").read().strip()
    if not text:
        die("file văn bản rỗng")

    if a.provider == "elevenlabs":
        audio = elevenlabs(text, a.voice, a.model, a.stability, a.similarity, a.style)
    else:
        audio = azure(text, a.voice, a.lang, a.rate, a.ssml)

    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, "wb") as f:
        f.write(audio)
    print(f"Đã ghi {a.out} ({len(audio)//1024} KB)")


if __name__ == "__main__":
    main()
