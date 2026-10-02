---
name: storyboard-shotlist
description: Chuyển kịch bản thành storyboard và shot list có mã cảnh, thời lượng, góc máy, công cụ sản xuất (AI video, ảnh+chuyển động, motion graphics, screen recording). Dùng khi cần kế hoạch hình ảnh chi tiết trước khi sinh/dựng.
---

# Storyboard & Shot list

## Khối cảnh (`04-storyboard.md`)

```markdown
### S03 · 4.0s · 00:12–00:16
- Công cụ: AI video (i2v) | motion graphics | screen rec | ảnh + parallax
- Khung hình: <mô tả 1–2 câu, tiêu điểm>
- Góc/ống kính/chuyển động: <ví dụ: 35mm, eye-level, slow dolly-in>
- Lời (VI/EN): <trích>
- On-screen text: <tối đa 8 từ>
- Âm thanh: <SFX/nhạc/khoảng lặng>
- Chuyển cảnh: cut | match cut | dissolve 12f | whip (chỉ khi hợp)
- Vùng an toàn: 16:9 ✓ 9:16 ✓ 4:5 ✓
```

## Chọn công cụ cho từng loại cảnh
| Loại cảnh | Công cụ tốt nhất |
|---|---|
| Giao diện sản phẩm, thao tác phần mềm | Screen recording + zoom/cursor trong Remotion |
| Số liệu, biểu đồ, sơ đồ, quy trình | Motion graphics (Remotion/Lottie/After Effects) |
| Hiện tượng khoa học vi mô/vĩ mô, bối cảnh giàu hình | Video AI (Veo/Kling/Runway/Luma...) |
| Nhân vật nhất quán | Ảnh tham chiếu → image-to-video |
| Cảnh bàn làm việc, con người thật | Quay thật hoặc video AI i2v; ưu tiên quay thật nếu có |
| Chữ, logo, tiêu đề | Luôn dựng bằng motion graphics |

## Shot list máy đọc (`05-shotlist.json`)
Xem schema trong skill `ai-video-prompting`.

## Quy tắc
- Tổng thời lượng các cảnh = thời lượng voice-over + đệm; cảnh AI sinh 4–8s rồi cắt.
- Tối đa 1/3 số cảnh là video AI nếu ngân sách hạn chế; cảnh còn lại dùng motion graphics/ảnh để chất lượng ổn định và rẻ.
- Mỗi cảnh trả lời được: "người xem học/cảm được gì ở cảnh này?" Nếu không, bỏ.
