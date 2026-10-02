---
name: script-vi-en
description: Viết và transcreate kịch bản video/voice-over song ngữ Việt–Anh, tối ưu cho nghe và cho TTS, có mốc thời gian theo tốc độ đọc, chuẩn thuật ngữ khoa học/công nghệ. Dùng khi soạn hoặc chỉnh lời thoại.
---

# Kịch bản song ngữ VI–EN

## Cấu trúc nhịp (mặc định cho video 60s)
1. **Hook (0–3s)**: một hình ảnh/câu hỏi/con số khiến người xem dừng lại.
2. **Căng thẳng (3–15s)**: vấn đề, cái giá của việc không giải quyết.
3. **Chuyển hóa (15–40s)**: giải pháp/cơ chế, thể hiện bằng hình, lời bổ trợ.
4. **Bằng chứng (40–52s)**: kết quả cụ thể.
5. **CTA (52–60s)**: một hành động, nói rõ nơi làm.

## Viết cho tai nghe
- Câu ngắn, chủ ngữ rõ, động từ mạnh. Một ý một câu.
- Hình ảnh nói điều hình ảnh làm được; lời chỉ bổ sung điều hình không nói.
- Lặp có chủ đích một cụm then chốt (tối đa 2 lần) để tạo nhớ.
- Đọc to lại: chỗ nào vấp thì sửa.

## Tiếng Việt
- Ưu tiên từ thuần Việt, tránh Hán–Việt dày đặc và cấu trúc dịch từ tiếng Anh ("được thực hiện bởi", "nhằm mục đích để").
- Thuật ngữ: dùng bản chuẩn của lĩnh vực; lần đầu có thể kèm bản gốc trong ngoặc ở phụ đề, không đọc cả hai.
- Xưng hô nhất quán: "bạn" cho đại chúng/mạng xã hội; "quý vị" cho hội thảo trang trọng; tránh trộn.
- Dấu thanh đúng chuẩn, thống nhất kiểu dấu (hòa/hoà → chọn một kiểu cho cả dự án).
- Số: viết chữ nếu ≤ 10 khi đọc; số lớn ghi dạng dễ đọc ("hai mươi lăm phần trăm" trong cột TTS note).

## Tiếng Anh
- Tự nhiên, đời thường (contractions), động từ chủ động; tránh "leverage, seamless, revolutionary, cutting-edge".
- Điều chỉnh ví dụ và hài hước theo văn hóa; không dịch thành ngữ Việt theo nghĩa đen.
- Dùng spelling nhất quán (US hoặc UK) cho cả dự án.

## Định dạng đầu ra

```markdown
| Cảnh | Time | Hình ảnh | Lời (VI) | TTS note | On-screen text |
|------|------|----------|----------|----------|----------------|
| S01  | 0–3  | ...      | ...      | ...      | ...            |
```
File EN dùng cùng mã cảnh để ghép dễ dàng. Cuối file: tổng số từ, thời lượng ước tính, danh sách thuật ngữ & cách đọc, danh sách `[CẦN XÁC MINH]`.

## Tự kiểm
- [ ] Tổng thời lượng ước tính ≤ thời lượng brief (+10% đệm).
- [ ] Mỗi câu ≤ 22 từ (VI) / 20 từ (EN).
- [ ] Không còn số liệu chưa có nguồn.
- [ ] Hai bản VI/EN khớp mã cảnh và độ dài trong ±10%.
