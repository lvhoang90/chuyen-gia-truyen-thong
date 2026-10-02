---
name: video-qa-checklist
description: Checklist kiểm định chất lượng cuối cho video quảng bá có AI: nội dung, ngôn ngữ, hình ảnh, âm thanh, kỹ thuật, bản quyền và công bố AI. Dùng trước khi giao hoặc đăng.
---

# QA checklist

Mức: **B** = Bắt buộc, **N** = Nên sửa, **G** = Gợi ý.

## Nội dung
- [B] Mọi số liệu, tuyên bố khoa học/sản phẩm có nguồn đã xác minh.
- [B] Không hứa hẹn quá mức (y tế, tài chính, hiệu năng AI "100%").
- [B] Thông điệp và CTA rõ, một hành động.
- [N] Hook giữ chân trong 3 giây đầu.

## Ngôn ngữ
- [B] Tiếng Việt: dấu, chính tả, thuật ngữ, xưng hô nhất quán.
- [B] Tiếng Anh: tự nhiên, ngữ pháp, spelling nhất quán.
- [B] Phụ đề khớp tiếng, không lỗi font/dấu khi burn-in.
- [N] Hai bản VI/EN tương đương nghĩa và độ dài.

## Hình ảnh
- [B] Không biến dạng tay/mặt/vật thể, không chữ giả, không logo/watermark lạ trong cảnh AI.
- [B] Màu/grade nhất quán giữa các cảnh; không cháy sáng, không bệt tối.
- [B] Chữ trong vùng an toàn của từng tỷ lệ; tương phản đạt AA.
- [N] Nhịp cắt hợp lý, không cảnh thừa.
- [G] Poster frame hấp dẫn.

## Âm thanh
- [B] Giọng đọc đúng thanh điệu, không vấp, không cắt cụt âm cuối.
- [B] Mix -14 LUFS (±1), true peak ≤ -1 dBTP; không clipping.
- [N] Nhạc không lấn lời; ducking mượt.
- [N] Không tiếng ồn nền, tiếng click/pop ở điểm cắt.

## Kỹ thuật
- [B] Codec H.264/AAC, `yuv420p`, `faststart`; độ phân giải/tỷ lệ đúng yêu cầu.
- [B] Âm thanh ở cả hai kênh, đồng bộ hình–tiếng (lệch < 40ms).
- [N] Dung lượng phù hợp nền tảng (ví dụ ≤ 500MB cho Facebook/IG nếu cần, kiểm tra giới hạn hiện hành).

Chạy tự động: `scripts/qa_check.sh <file>` (độ phân giải, fps, codec, loudness).

## Pháp lý & đạo đức
- [B] Giấy phép nhạc, font, footage, model AI cho mục đích thương mại được ghi lại.
- [B] Không dùng khuôn mặt/giọng nói/tác phẩm của người khác không phép; voice clone có đồng ý bằng văn bản.
- [B] Công bố nội dung do AI tạo/chỉnh sửa theo yêu cầu của nền tảng và quy định hiện hành (nhãn "AI-generated" trên YouTube/Meta/TikTok khi áp dụng).
- [N] Có ghi chú nguồn dữ liệu/tài liệu khoa học ở cuối hoặc trong mô tả.

## Kết luận
PASS: không còn mục B nào lỗi. PASS CÓ ĐIỀU KIỆN: còn mục N. FAIL: còn mục B.
