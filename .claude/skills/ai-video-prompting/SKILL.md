---
name: ai-video-prompting
description: Viết prompt và kế hoạch sinh video/ảnh AI có kiểm soát (text-to-video, image-to-video, nhân vật nhất quán, chuyển động camera), chọn engine phù hợp và lập shot list JSON tái lập được. Dùng khi chuyển storyboard thành lệnh sinh.
---

# Prompting video AI

> Các model thay đổi rất nhanh. Trước khi chạy, xác nhận tên model, giới hạn thời lượng, độ phân giải, giá và điều khoản trong tài liệu chính thức của nhà cung cấp. Danh sách ở `docs/api-stack.md` là điểm khởi đầu, không phải sự thật cố định.

## Công thức prompt
`[Chủ thể + chi tiết] + [hành động] + [bối cảnh] + [ánh sáng] + [camera, ống kính, chuyển động] + [phong cách/grade] + [ràng buộc]`

Ví dụ (khoa học):
> A single drop of water falls into still water in extreme macro, slow motion, concentric ripples catching soft blue rim light, 100mm macro lens, shallow depth of field, locked-off camera, clean laboratory aesthetic, cool teal and white palette, fine film grain, no text, no logos.

Ví dụ (văn phòng/AI):
> Overhead shot of a tidy wooden desk, a laptop screen glowing softly, hands pause then a stack of paper notes dissolves into neat floating cards that arrange themselves into a grid, warm morning light from the left, slow top-down push-in, 35mm, minimal Scandinavian palette, no readable text.

## Quy tắc
- Mô tả cái **thấy được**, không mô tả khái niệm trừu tượng ("innovation").
- Một chuyển động camera chính, một hành động chính mỗi shot.
- Ràng buộc: `no text, no logos, no watermark, natural hands, consistent proportions`; dùng negative prompt nếu engine hỗ trợ.
- Tính liên tục: dùng ảnh tham chiếu/khung đầu–cuối (first/last frame) nếu engine hỗ trợ; khóa seed; giữ nguyên chuỗi mô tả nhân vật ("character sheet") trong mọi prompt.
- Cảnh có người: ưu tiên góc không lộ chi tiết khó (bàn tay đang gõ phím cận, bóng lưng, góc nghiêng, tiêu cự dài).
- Chữ/UI/biểu đồ: **không** sinh bằng AI.
- Không dùng tên người thật, thương hiệu, tác phẩm, họa sĩ còn sống làm "phong cách của ...".

## Chọn engine (theo nhu cầu, kiểm tra lại phiên bản hiện hành)
| Nhu cầu | Ứng viên |
|---|---|
| Điện ảnh, có thể kèm âm thanh gốc | Google Veo, OpenAI Sora |
| Kiểm soát camera, chỉnh sửa video-to-video | Runway |
| Chuyển động nhân vật/chi tiết, giá hợp lý | Kling, Seedance (ByteDance), Hailuo/MiniMax |
| Nhanh, ý tưởng, i2v mượt | Luma |
| Ảnh tham chiếu/keyframe chất lượng cao | Imagen, Flux, Midjourney (thủ công), GPT image |
| Upscale / khử nhiễu / nội suy khung | Topaz, Real-ESRGAN, RIFE (tự host) |

Gợi ý gọi API linh hoạt qua nền tảng tổng hợp (fal.ai, Replicate) để đổi model mà không viết lại mã.

## Schema `05-shotlist.json`

```json
{
  "project": "ten-du-an-202610",
  "defaults": {"aspect": "16:9", "resolution": "1080p", "fps": 24},
  "shots": [
    {
      "id": "S03",
      "engine": "veo",
      "mode": "i2v",
      "duration_s": 6,
      "prompt": "...",
      "negative": "text, watermark, extra fingers, distorted face",
      "ref_images": ["refs/S03_start.png"],
      "seed": 42117,
      "camera": "slow dolly-in",
      "trim_s": [0.5, 4.5],
      "fallback": {"engine": "kling", "note": "dùng nếu bị lỗi tay"},
      "status": "planned"
    }
  ]
}
```

## Kiểm soát chi phí
1. Chạy 1–2 shot khó nhất ở chế độ rẻ/nhanh để kiểm tra phong cách.
2. Báo người dùng ước lượng: số shot × số lần thử (mặc định 2–3) × giá/giây.
3. Ghi `gen-log.md`: shot, engine, phiên bản, seed, prompt, kết quả đạt/không, lý do.
