#!/usr/bin/env bash
# Kiểm kỹ thuật nhanh: codec, độ phân giải, fps, thời lượng, loudness.
# Dùng: scripts/qa_check.sh video.mp4
set -euo pipefail
F="${1:?Dùng: $0 <file>}"
echo "== Thông số =="
ffprobe -v error -show_entries stream=codec_type,codec_name,width,height,r_frame_rate,pix_fmt,sample_rate,channels \
  -show_entries format=duration,bit_rate -of default=nw=1 "$F"
echo "== Loudness (mục tiêu I≈-14, TP≤-1) =="
ffmpeg -hide_banner -nostats -i "$F" -af loudnorm=I=-14:TP=-1:LRA=8:print_format=summary -f null - 2>&1 \
  | grep -E "Input (Integrated|True Peak|LRA)"
echo "== faststart =="
ffprobe -v trace "$F" 2>&1 | grep -m2 -E "type:'(moov|mdat)'" || true
