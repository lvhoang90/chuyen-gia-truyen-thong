---
name: voiceover-tts
description: Chọn giọng và sinh voice-over tiếng Việt/tiếng Anh chuẩn bằng API TTS (ElevenLabs, Azure Speech, FPT.AI, Google Cloud TTS), chuẩn hóa văn bản và SSML cho phát âm đúng. Dùng khi tạo hoặc sửa giọng đọc.
---

# Voice-over TTS

Script: `python scripts/tts.py --provider elevenlabs|azure --lang vi|en --text-file x.txt --out audio/vo/S01.mp3`

## Lựa chọn nhà cung cấp
| Nhu cầu | Gợi ý | Ghi chú |
|---|---|---|
| Chất lượng cảm xúc cao, đa ngôn ngữ, giọng thương hiệu | **ElevenLabs** (`eleven_multilingual_v2` hoặc model mới hơn) | Hỗ trợ tiếng Việt; chọn giọng trong Voice Library, nghe thử với từ khó |
| Ổn định, SSML đầy đủ, giọng Việt chuẩn, giá dễ đoán | **Azure Speech** (`vi-VN-HoaiMyNeural` nữ, `vi-VN-NamMinhNeural` nam; `en-US-AvaMultilingualNeural`, `en-US-AndrewMultilingualNeural`, `en-GB-SoniaNeural`) | Kiểm tra danh sách giọng hiện hành |
| Giọng Việt bản địa các vùng miền | **FPT.AI TTS**, **Viettel AI**, **Vbee** | Có giọng Bắc/Trung/Nam; nghe thử trước, kiểm điều khoản thương mại |
| Dự phòng, chi phí thấp | **Google Cloud TTS** (`vi-VN-Neural2-*`, Chirp 3 HD) | |
| Giọng thương hiệu riêng | Voice cloning (ElevenLabs, Azure Custom Neural Voice) | Chỉ khi có văn bản đồng ý của chủ giọng |

Luôn nghe mẫu 10–15s của 2–3 giọng với đoạn có: số, đơn vị, tên riêng, từ viết tắt, thuật ngữ chuyên ngành. Người dùng chọn rồi mới sinh toàn bộ.

## Chuẩn hóa văn bản (đặc biệt tiếng Việt)
- Số → chữ: `25%` → "hai mươi lăm phần trăm"; `2026` → "hai nghìn không trăm hai mươi sáu" hoặc "năm hai nghìn không trăm hai mươi sáu" tùy ngữ cảnh; ngày `02/10` → "ngày hai tháng mười".
- Đơn vị: `km/h` → "ki-lô-mét trên giờ"; `GB` → "gi-ga-bai"; `AI` → "ây-ai" (hoặc "trí tuệ nhân tạo").
- Viết tắt/thương hiệu tiếng Anh: ghi phiên âm tiếng Việt hoặc dùng thẻ phát âm (`<phoneme>`/`<sub alias>` của SSML).
- Tách câu ngắn; dấu phẩy = ngắt nhẹ, dấu chấm = ngắt rõ, "…" = ngập ngừng; thêm `<break time="400ms"/>` ở chỗ cần.
- Tên riêng nước ngoài trong câu tiếng Việt: kiểm tra bằng tai; thay bằng thẻ `<lang xml:lang="en-US">` nếu giọng đọc sai.

## Thông số khuyến nghị
- ElevenLabs: `stability` 0.45–0.6, `similarity_boost` 0.75, `style` 0.1–0.3, `use_speaker_boost` true. Văn khoa học: stability cao hơn; quảng bá năng động: thấp hơn.
- Azure: `<prosody rate="-5%">` cho thuyết minh khoa học; `+5%` cho quảng bá; style (`cheerful`, `friendly`...) chỉ khi giọng hỗ trợ.
- Định dạng: sinh WAV/PCM hoặc MP3 ≥ 128 kbps; hậu kỳ ở 48 kHz.
- Một file mỗi cảnh (`audio/vo/S03.vi.mp3`, `S03.en.mp3`) để chỉnh cục bộ và khớp hình.

## Bảo mật & pháp lý
- Khóa API từ biến môi trường (`ELEVENLABS_API_KEY`, `AZURE_SPEECH_KEY`, `AZURE_SPEECH_REGION`); không ghi vào repo.
- Ghi lại nhà cung cấp, giọng, phiên bản model, điều khoản sử dụng thương mại vào `audio/LICENSES.md`.
- Không mô phỏng giọng người thật khác khi chưa được phép.
