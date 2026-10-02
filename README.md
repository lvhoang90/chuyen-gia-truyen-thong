# Chuyên gia truyền thông đa phương tiện

Bộ **agents + skills + scripts** cho Claude Code để sản xuất video quảng bá sáng tạo (khoa học, văn phòng, tiện ích số, sản phẩm/dự án AI), ưu tiên tiếng Việt và tiếng Anh, thẩm mỹ chuẩn quốc tế.

## Cách dùng
Mở repo bằng Claude Code và nói, ví dụ:
> Dùng producer-director làm video 60 giây giới thiệu công cụ AI tóm tắt tài liệu, bản VI và EN, tỷ lệ 16:9 và 9:16.

## Agents (`.claude/agents/`)
| Agent | Vai trò |
|---|---|
| `producer-director` | Điều phối pipeline, cổng duyệt, kiểm soát chi phí |
| `creative-strategist` | Insight, big idea, 3 hướng concept |
| `scriptwriter-bilingual` | Kịch bản VI/EN, transcreation, ghi chú TTS |
| `art-director` | Style bible, storyboard, chọn công cụ theo cảnh |
| `video-prompt-engineer` | Prompt video/ảnh AI, shot list JSON, nhất quán |
| `voice-sound-director` | TTS VI/EN, nhạc, SFX, mix -14 LUFS |
| `editor-colorist` | Dựng, grade, chữ, phụ đề, xuất đa tỷ lệ |
| `qa-localization-reviewer` | QC nội dung, ngôn ngữ, kỹ thuật, pháp lý |

## Skills (`.claude/skills/`)
`video-brief`, `script-vi-en`, `aesthetic-direction`, `storyboard-shotlist`, `ai-video-prompting`, `voiceover-tts`, `sound-music-design`, `motion-graphics-remotion`, `subtitle-localization`, `video-qa-checklist`.

## Scripts
`tts.py` (ElevenLabs/Azure), `make_srt.py`, `mix_audio.sh`, `assemble.sh`, `qa_check.sh`. Cần Python 3, FFmpeg.

## Tài liệu
- `docs/api-stack.md`: lựa chọn API và công cụ.
- `.env.example`: biến môi trường (không commit khóa).

## Cấu trúc dự án
`projects/<slug>/` gồm `00-brief.md` → `07-qa-report.md`, `audio/`, `clips/`, `out/`.
