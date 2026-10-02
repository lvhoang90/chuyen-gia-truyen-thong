#!/usr/bin/env bash
# Mix voice-over + nhạc nền với ducking, chuẩn hóa -14 LUFS, true peak -1 dBTP.
# Dùng: scripts/mix_audio.sh vo.wav music.mp3 mix.wav
set -euo pipefail
[ $# -eq 3 ] || { echo "Dùng: $0 <voice> <music> <out.wav>"; exit 1; }
VO="$1"; MUSIC="$2"; OUT="$3"
ffmpeg -y -i "$VO" -i "$MUSIC" -filter_complex "
[0:a]aresample=48000,highpass=f=80,asplit=2[vo][vo_sc];
[1:a]aresample=48000,volume=-14dB[bg];
[bg][vo_sc]sidechaincompress=threshold=0.04:ratio=8:attack=20:release=300[ducked];
[vo][ducked]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1:LRA=8[out]
" -map "[out]" -ar 48000 -c:a pcm_s24le "$OUT"
