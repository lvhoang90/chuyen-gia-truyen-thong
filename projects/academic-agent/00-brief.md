# Brief: Trợ lý học thuật (aaa.isavietnam.app)

- Sản phẩm: ứng dụng AI chấm độ phù hợp của tài liệu với đề tài, gợi ý đoạn đáng trích và tạo trích dẫn đúng chuẩn.
- Mục tiêu: giải thích quy trình 8 bước, kéo người dùng thử.
- Đối tượng: sinh viên, nghiên cứu sinh, giảng viên.
- Thông điệp: từ một tài liệu đến trích dẫn đúng chuẩn trong 8 bước.
- CTA: thử ngay tại https://aaa.isavietnam.app/ (miễn phí 2 lượt/ngày).
- Định dạng: 9:16 (1080×1920), ảnh 3:4 đặt giữa, nền tối đồng màu, chừa trên/dưới cho phụ đề.
- Ngôn ngữ: hai bản VI và EN, mỗi bản có phụ đề đầy đủ.
- Phương án lời dẫn (C): **phụ đề giữ nguyên văn đầy đủ; giọng đọc chỉ nói câu chính của mỗi cảnh.**
- Thời lượng: ~50 giây (8 cảnh 4,5–7,5 giây + 3 giây cảnh kết). Dài hơn mốc 30 giây ban đầu vì phụ đề đầy đủ phải đọc được (≤17 ký tự/giây VI, ≤20 EN).
- Tài nguyên: 8 ảnh `01-dang-ky.png` … `08-diem-thap.png` và `marketing/poster-3x4.png` (**chưa có trong repo**, đặt vào `assets/`).
- Giả định / `[CẦN XÁC MINH]`:
  - "hơn 10.000 kiểu tạp chí" (S06)
  - "tệp không bị lưu lại" (S03)
  - "2 lượt phân tích mỗi ngày" (S01)
  - "năm tiêu chí" (S04)
  - "đối chiếu nguyên văn" (S05)
  - "gợi ý từ EduFind" (S08)
- Dữ liệu trong ảnh là dữ liệu minh họa: thêm chú thích nhỏ "Dữ liệu minh họa / Illustrative data" ở S04–S07.

## Tệp
- `script.json`: lời dẫn, phụ đề, mốc thời gian từng cảnh.
- `out/sub.vi.srt`, `out/sub.en.srt`: phụ đề (tách cue theo câu).
- Tái tạo: `python scripts/make_srt.py projects/academic-agent/script.json --lang vi --width 36 --split --out projects/academic-agent/out/sub.vi.srt`

## Việc tiếp theo
1. Thêm 9 ảnh vào `assets/`.
2. Chọn giọng (mẫu 10–15 giây, 2–3 giọng) rồi sinh `audio/vo/Sxx.{vi,en}.mp3` từ `vo_vi`/`vo_en`.
3. Dựng Remotion/FFmpeg: zoom 100→108% mỗi cảnh, cắt 0,3 giây, nhạc nhẹ, mix -14 LUFS.
4. QA bằng `video-qa-checklist`.
