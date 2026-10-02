# Stack API & công cụ đề xuất

> Thị trường model AI thay đổi theo tháng. Bảng dưới là **ứng viên nên thử**, chọn theo nhu cầu; trước khi dùng thương mại hãy kiểm tra tài liệu, giá, giới hạn và điều khoản hiện hành của từng nhà cung cấp. Tên model cụ thể chưa được kiểm chứng trong repo này.

## 1. Ngôn ngữ (ý tưởng, kịch bản, kiểm tra)
| Vai trò | Lựa chọn | Lý do |
|---|---|---|
| Chiến lược, kịch bản, transcreation VI/EN, QA | **Claude** (Anthropic API / Claude Code) | Viết tiếng Việt tự nhiên, bám ràng buộc dài, dùng làm điều phối các agent trong repo này |
| Kiểm chéo / ý tưởng thay thế | GPT, Gemini | Lấy ý kiến thứ hai về hook và cách diễn đạt |
| Tra cứu nguồn khoa học | Web search + nguồn gốc (Crossref, OpenAlex, PubMed) | Xác minh số liệu, không tin trí nhớ model |

## 2. Giọng nói (VI + EN là chính)
| Ưu tiên | Dịch vụ | Dùng khi |
|---|---|---|
| 1 | **ElevenLabs** | Cần cảm xúc, đa ngôn ngữ, giọng thương hiệu; có Voice Library, hỗ trợ tiếng Việt |
| 2 | **Azure AI Speech** | Cần SSML sâu, ổn định, giọng Việt chuẩn (`vi-VN-HoaiMyNeural`, `vi-VN-NamMinhNeural`) và Anh đa giọng |
| 3 | **FPT.AI / Viettel AI / Vbee** | Giọng Việt vùng miền, nhà cung cấp trong nước |
| 4 | **Google Cloud TTS** | Dự phòng, chi phí thấp |
| STT | **Whisper (OpenAI/tự host)**, Azure/Google STT | Tạo phụ đề từ audio có sẵn, căn thời gian |

## 3. Hình ảnh & video AI
| Vai trò | Ứng viên |
|---|---|
| Video điện ảnh | Google **Veo**, OpenAI **Sora**, **Runway**, **Kling**, **Luma**, **Seedance**, **Hailuo** |
| Ảnh tham chiếu/keyframe | **Imagen**, **Flux**, GPT image, Midjourney (thủ công) |
| Cổng API gom nhiều model | **fal.ai**, **Replicate** |
| Tăng độ phân giải/khung | Topaz, Real-ESRGAN, RIFE |

## 4. Âm nhạc & SFX
Thư viện có giấy phép: Epidemic Sound, Artlist, YouTube Audio Library. Nhạc AI: Suno, Udio, ElevenLabs Music, Stable Audio (kiểm quyền thương mại theo gói).

## 5. Dựng & hoàn thiện
- **Remotion** (React): chữ, biểu đồ, UI, template đa tỷ lệ.
- **FFmpeg**: ghép, scale, LUT, phụ đề, xuất.
- **DaVinci Resolve / After Effects**: tinh chỉnh thủ công, grade.
- **Whisper + `scripts/make_srt.py`**: phụ đề.

## 6. Chọn nhanh theo loại video
| Loại | Hình | Giọng | Ghi chú |
|---|---|---|---|
| Khoa học (giải thích) | Veo/Kling cho cảnh vi mô-vĩ mô + Remotion cho sơ đồ | ElevenLabs hoặc Azure (tốc độ -5%) | Nguồn tham khảo cuối video |
| Văn phòng/tiện ích số | Screen recording + Remotion, vài cảnh i2v | Azure/ElevenLabs, giọng thân thiện | Giao diện thật, zoom thao tác |
| Sản phẩm/dự án AI | Remotion luồng dữ liệu + cảnh AI tối giản | ElevenLabs, giọng tự tin | Cho thấy kết quả đo được |

## 7. Biến môi trường
Xem `.env.example`. Không commit khóa. Ước lượng chi phí trước khi chạy hàng loạt.

## 8. Rủi ro cần quản lý
- Bản quyền/điều khoản thương mại của từng model, nhạc, font.
- Công bố nội dung AI theo quy định nền tảng.
- Voice cloning chỉ khi chủ giọng đồng ý bằng văn bản.
- Dữ liệu nhạy cảm của khách hàng: không gửi lên API khi hợp đồng không cho phép.
