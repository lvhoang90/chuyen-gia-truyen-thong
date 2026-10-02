#!/usr/bin/env python3
"""Tạo SRT từ script.json.

script.json:
{"scenes":[{"id":"S01","start":0.0,"end":3.2,"vi":"...","en":"..."}]}

  python scripts/make_srt.py script.json --lang vi --out out/sub.vi.srt
"""
import argparse
import json
import os
import re
import sys


def ts(t):
    ms = round(t * 1000)
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def wrap(text, width):
    """Ngắt tối đa 2 dòng theo từ, cố cân bằng độ dài."""
    words = text.split()
    if len(text) <= width:
        return text
    best, best_diff = None, None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        if len(a) <= width and len(b) <= width:
            d = abs(len(a) - len(b))
            if best_diff is None or d < best_diff:
                best, best_diff = f"{a}\n{b}", d
    return best or text  # quá dài: giữ nguyên, QA sẽ cảnh báo


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--lang", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--width", type=int, default=42)
    a = ap.parse_args()

    data = json.load(open(a.script, encoding="utf-8"))
    out, n = [], 0
    for sc in data["scenes"]:
        text = re.sub(r"\s+", " ", sc.get(a.lang, "")).strip()
        if not text:
            continue
        n += 1
        dur = sc["end"] - sc["start"]
        cps = len(text) / dur if dur > 0 else 999
        if cps > 20:
            print(f"Cảnh báo {sc['id']}: {cps:.1f} ký tự/giây, quá nhanh", file=sys.stderr)
        out.append(f"{n}\n{ts(sc['start'])} --> {ts(sc['end'])}\n{wrap(text, a.width)}\n")

    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(out))
    print(f"Đã ghi {a.out} ({n} cue)")


if __name__ == "__main__":
    main()
