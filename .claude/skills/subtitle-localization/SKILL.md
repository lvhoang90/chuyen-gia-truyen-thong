---
name: subtitle-localization
description: Tạo và kiểm phụ đề tiếng Việt/tiếng Anh (SRT/VTT), quy tắc ngắt dòng, tốc độ đọc, và bản địa hóa video đa ngôn ngữ. Dùng khi làm phụ đề hoặc xuất bản song ngữ.
---

# Phụ đề & bản địa hóa

Script: `python scripts/make_srt.py script.json --lang vi --out out/sub.vi.srt`

## Quy tắc phụ đề
- Tối đa 2 dòng, ≤ 42 ký tự mỗi dòng (16:9); với 9:16 ≤ 28–32 ký tự mỗi dòng, 2–3 dòng ngắn.
- Tốc độ đọc ≤ 17 ký tự/giây (tiếng Anh ≤ 20 cps); mỗi cue hiển thị 1–6 giây, tối thiểu 1 giây.
- Ngắt dòng theo cụm nghĩa; không tách giới từ/mạo từ khỏi danh từ, không tách số khỏi đơn vị.
- Phụ đề khớp thời gian với âm thanh: vào sớm 0–100ms, ra muộn ~200ms.
- Bản burn-in cho mạng xã hội đặt trong vùng an toàn; có nền mờ nhẹ hoặc viền đảm bảo tương phản.

## Bản địa hóa (transcreation)
- Tiếng Việt ↔ Anh: đổi ví dụ, đơn vị tiền/đo lường, định dạng ngày (`dd/mm/yyyy` VI, theo vùng EN), dấu thập phân (`,` VI, `.` EN).
- Chữ trên màn hình cũng bản địa hóa: dựng 2 phiên bản (không hard-code chữ vào clip AI).
- Hạn chế dùng chữ trên cảnh sinh bằng AI; chữ do lớp motion graphics phủ lên giúp đổi ngôn ngữ nhanh.
- Kiểm tên riêng và thuật ngữ theo bảng thuật ngữ của dự án (`projects/<slug>/glossary.md`).

## Xuất
`<slug>_vi.srt`, `<slug>_en.srt`, tùy chọn `.vtt` cho web; bản burn-in VI, bản burn-in EN, bản không phụ đề.
