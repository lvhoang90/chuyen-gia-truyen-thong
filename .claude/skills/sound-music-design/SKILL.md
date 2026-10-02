---
name: sound-music-design
description: Thiết kế âm thanh cho video quảng bá: chọn nhạc nền, SFX, ducking, khoảng lặng và mix đạt chuẩn âm lượng (LUFS). Dùng khi chọn nhạc, sinh nhạc AI hoặc mix âm thanh.
---

# Âm nhạc & thiết kế âm thanh

## Chọn nhạc
| Chủ đề | Gợi ý |
|---|---|
| Khoa học | Ambient/piano nhẹ, synth chậm, nhịp 70–90 BPM, ít giai điệu để không lấn lời |
| Văn phòng/tiện ích số | Lo-fi sạch, electronic nhẹ, 100–115 BPM, có điểm nhấn nhịp khớp chuyển cảnh |
| Sản phẩm AI | Pulse nhẹ, texture tối giản, build-up đến CTA |

Nguồn: thư viện có giấy phép thương mại rõ (Epidemic Sound, Artlist, YouTube Audio Library, Pixabay Music), hoặc nhạc AI (Suno, Udio, ElevenLabs Music, Stable Audio) **sau khi kiểm tra điều khoản thương mại của gói đang dùng**. Ghi nguồn và giấy phép vào `audio/LICENSES.md`.

## SFX
- Chỉ thêm khi phục vụ hành động: click, whoosh nhẹ, riser trước CTA, tiếng nền môi trường.
- Layer 2–3 lớp ngắn thay vì 1 lớp to. Cắt đuôi sạch.

## Mix (đích: web & mạng xã hội)
- Tích hợp **-14 LUFS**, true peak ≤ **-1 dBTP**, loudness range hợp lý (≤ 8 LU).
- Voice ~ -16 LUFS đứng một mình; nhạc thấp hơn voice 12–18 dB khi có lời; được tăng 4–6 dB trong đoạn không lời.
- Sidechain/ducking: attack ~20ms, release ~300ms.
- EQ voice: cắt dưới 80 Hz, giảm 250–400 Hz nếu đục, thêm nhẹ 3–5 kHz cho độ rõ; de-ess 5–8 kHz nếu cần.
- 48 kHz / 24-bit trong khi làm, xuất AAC 192–256 kbps.

Script: `scripts/mix_audio.sh vo.wav music.mp3 mix.wav`.

## Nguyên tắc
Khoảng lặng là công cụ. Hook có thể không nhạc; nhạc vào ở nhịp đầu tiên của phần giải pháp; nhạc kết thúc dứt khoát cùng CTA.
