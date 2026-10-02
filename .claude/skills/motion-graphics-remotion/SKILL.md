---
name: motion-graphics-remotion
description: Dựng motion graphics, chữ, số liệu, UI và ghép toàn bộ video bằng Remotion (React) hoặc FFmpeg; xuất đa tỷ lệ. Dùng khi cần chữ/biểu đồ/giao diện chính xác hoặc dựng tự động hóa theo shot list.
---

# Motion graphics & dựng

## Khi nào dùng gì
- **Remotion** (React → video): chữ có dấu tiếng Việt chuẩn, biểu đồ theo dữ liệu, giao diện sản phẩm, lower-third, tái sử dụng template cho nhiều video/tỷ lệ. Chạy `npx create-video@latest`, render bằng `npx remotion render`.
- **FFmpeg**: ghép clip, cắt, scale/crop theo tỷ lệ, mix âm, burn phụ đề, LUT, xuất. Dùng `scripts/assemble.sh`.
- **After Effects/DaVinci Resolve**: nếu người dùng có sẵn và muốn tinh chỉnh thủ công; giao file project + preset.
- **Lottie/Rive**: icon động nhẹ cho web.

## Quy ước Remotion
- Tách `Composition` theo tỷ lệ: `16x9` (1920×1080), `9x16` (1080×1920), `4x5` (1080×1350); chung component, khác layout qua `useVideoConfig()`.
- Dữ liệu từ `projects/<slug>/05-shotlist.json` và `script.json` (props), không hard-code.
- Font: nạp qua `@remotion/google-fonts` hoặc file cục bộ; bắt buộc `subsets: ['vietnamese','latin']`.
- Animation: `spring()`/`interpolate()` với easing nhất quán (xem `aesthetic-direction`); thời gian tính theo khung hình, 30 fps cho web, 24 fps cho cảm giác điện ảnh.
- Biểu đồ: số liệu chỉ từ nguồn đã xác minh; hiển thị đơn vị và nguồn.

## FFmpeg công thức nhanh
```bash
# crop từ 16:9 sang 9:16 giữa khung
ffmpeg -i in.mp4 -vf "crop=ih*9/16:ih,scale=1080:1920" -c:a copy out_9x16.mp4
# áp LUT .cube
ffmpeg -i in.mp4 -vf "lut3d=grade.cube" -c:a copy graded.mp4
# burn phụ đề với font hỗ trợ tiếng Việt
ffmpeg -i in.mp4 -vf "subtitles=sub.srt:force_style='FontName=Be Vietnam Pro,FontSize=18,Outline=1,MarginV=60'" out.mp4
# xuất chuẩn web
ffmpeg -i in.mp4 -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -movflags +faststart -c:a aac -b:a 192k out.mp4
```

## Hoàn thiện
Poster frame (khung đẹp nhất), bản GIF/loop 3–5s, bản không chữ (clean) cho tái sử dụng, và thư mục `deliverables/` có tên chuẩn: `<slug>_<lang>_<aspect>_v<n>.mp4`.
