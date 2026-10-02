#!/usr/bin/env python3
"""Dựng video dọc 9:16 từ ảnh 3:4 + script.json + SRT bằng FFmpeg.

Mỗi cảnh: ảnh 3:4 (1080x1440) đặt giữa nền tối, zoom 100%->108%, phụ đề burn-in ở dải dưới.
Có thể thêm --audio mix.wav để ghép âm thanh.

  python scripts/build_reel.py projects/academic-agent --lang vi --out projects/academic-agent/out/reel.vi.mp4
"""
import argparse, json, os, subprocess, sys, tempfile

W, H, FPS = 1080, 1920, 30
IMG_W, IMG_H = 1080, 1440
BG = "0x0A0F1F"


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr[-1500:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--lang", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--audio")
    ap.add_argument("--font", default="DejaVu Sans")
    ap.add_argument("--poster", default="Tro ly hoc thuat AAA.png")
    a = ap.parse_args()

    data = json.load(open(os.path.join(a.project, "script.json"), encoding="utf-8"))
    assets = os.path.join(a.project, "assets")
    imgs = sorted(f for f in os.listdir(assets) if f[:2].isdigit() and f.endswith(".png"))
    imgs.append(a.poster)
    scenes = data["scenes"]
    if len(imgs) != len(scenes):
        sys.exit(f"Số ảnh ({len(imgs)}) khác số cảnh ({len(scenes)})")

    # cache clip theo cảnh: lần render sau (đổi phụ đề/âm thanh) không dựng lại hình
    tmp = os.path.join(os.path.dirname(os.path.abspath(a.out)), ".clips")
    os.makedirs(tmp, exist_ok=True)
    clips = []
    for sc, img in zip(scenes, imgs):
        d = sc["end"] - sc["start"]
        frames = round(d * FPS)
        out = os.path.join(tmp, sc["id"] + ".mp4")
        if os.path.exists(out):
            clips.append(out)
            continue
        # zoompan trên ảnh đã scale lớn để mượt, rồi đặt giữa nền
        vf = (
            f"scale={IMG_W*2}:{IMG_H*2},"
            f"zoompan=z='1+0.08*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={IMG_W}x{IMG_H}:fps={FPS},"
            f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2+0:color={BG},format=yuv420p"
        )
        run(["ffmpeg", "-y", "-loop", "1", "-i", os.path.join(assets, img), "-vf", vf,
             "-frames:v", str(frames), "-c:v", "libx264", "-crf", "16", "-preset", "medium", out])
        clips.append(out)

    lst = os.path.join(tmp, f"list.{a.lang}.txt")
    open(lst, "w").write("".join(f"file '{os.path.abspath(c)}'\n" for c in clips))
    srt = os.path.join(a.project, "subs", f"sub.{a.lang}.srt")
    style = (f"FontName={a.font},Bold=1,FontSize=6.5,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
             f"Outline=0.6,Shadow=0,Alignment=2,MarginV=10,MarginL=9,MarginR=9")
    vf = f"subtitles='{srt}':force_style='{style}'"
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst]
    if a.audio:
        cmd += ["-i", a.audio, "-map", "0:v", "-map", "1:a", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest"]
    cmd += ["-vf", vf, "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-pix_fmt", "yuv420p",
            "-movflags", "+faststart", a.out]
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    run(cmd)
    print("Đã ghi", a.out)


if __name__ == "__main__":
    main()
