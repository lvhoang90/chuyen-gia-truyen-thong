#!/usr/bin/env bash
# Ghép danh sách clip + âm thanh, scale/crop về đúng tỷ lệ, xuất chuẩn web.
# Dùng: scripts/assemble.sh clips.txt mix.wav out.mp4 [16x9|9x16|4x5] [sub.srt]
#   clips.txt: mỗi dòng  file 'clips/S01.mp4'   (định dạng concat của ffmpeg)
set -euo pipefail
[ $# -ge 3 ] || { sed -n '2,4p' "$0"; exit 1; }
LIST="$1"; AUDIO="$2"; OUT="$3"; ASPECT="${4:-16x9}"; SRT="${5:-}"
case "$ASPECT" in
  16x9) W=1920; H=1080 ;;
  9x16) W=1080; H=1920 ;;
  4x5)  W=1080; H=1350 ;;
  *) echo "Tỷ lệ không hỗ trợ: $ASPECT"; exit 1 ;;
esac
VF="scale=${W}:${H}:force_original_aspect_ratio=increase,crop=${W}:${H},fps=30,format=yuv420p"
[ -n "$SRT" ] && VF="${VF},subtitles=${SRT}:force_style='FontName=Be Vietnam Pro,FontSize=18,Outline=1,MarginV=60'"
ffmpeg -y -f concat -safe 0 -i "$LIST" -i "$AUDIO" -map 0:v -map 1:a \
  -vf "$VF" -c:v libx264 -crf 18 -preset slow -movflags +faststart \
  -c:a aac -b:a 192k -ar 48000 -shortest "$OUT"
