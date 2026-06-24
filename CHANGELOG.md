# Changelog

## v1.1.0 — 2026-06-10

### ✨ New

- **Learning pace** (slow / medium / fast) — AI tự điều chỉnh độ dài micro-task khi phân rã và scheduler nhân hệ số tương ứng (×1.5 / ×1.0 / ×0.7).
- **Stats dashboard** — 4 card chỉ số (avg completion, best week, week streak, weeks tracked) + activity heatmap 365 ngày + bar chart 7 thứ trong tuần (toggle distribution / completion).
- **Archive** — danh sách mọi tuần đã có task; click vào xem chi tiết task được group theo môn học (assignment). Lịch sử **không bị xoá** khi xoá plan.
- **Settings tab** — chọn learning pace + cấu hình chương dài/quỹ rảnh/buffer; lưu vào DB và áp dụng cho mọi plan mới.

### 🏗 Backend

- `models.py`: thêm `UserSettings`, `StatsSummary`, `ActivityCell`, `WeekdayStats`, `ArchiveWeekSummary`, `ArchiveDetail`.
- `db.py`: 2 bảng mới (`user_settings`, `task_history`) + 8 hàm query mới (get/update_settings, stats_summary, stats_activity, stats_by_weekday, list_archives, archive_detail, delete_archive, clear_all_archives). Migration tự động backfill task_history từ tasks cũ ở `init_db()` (idempotent).
- `scheduler.py`: hàm `apply_pace()` + scheduler nhận thêm tham số `pace`.
- `llm.py`: `decompose_assignment(content, pace, avg_minutes_per_chapter)` — inject pace hint vào system prompt.
- `main.py`: 7 endpoint mới:
  - `GET/PUT /api/settings`
  - `GET /api/stats/summary`
  - `GET /api/stats/activity?days=N`
  - `GET /api/stats/by-weekday?mode=distribution|completion`
  - `GET /api/archives`
  - `GET /api/archives/{week_id}` (week_id = `YYYY-Www`)
  - `DELETE /api/archives/{week_id}` & `DELETE /api/archives`

  `POST /api/plan` giờ tự đọc settings, các form field `learning_pace` / `daily_free_minutes` / `buffer_days` là **optional override**.

### 🎨 Frontend

- Rewrite thành SPA 4 tab (Plan / Stats / Archive / Settings) với hash routing.
- Plan tab giữ nguyên chat UI, thêm pill hiển thị pace ở dưới (click → mở Settings).
- Stats & Archive tab dùng aesthetic "cream / rust" (#F5F1E8 bg, #FAF7F0 cards, #A04A2A serif numbers) lấy cảm hứng từ planner.amysteriousbeaver.com.
- Heatmap 53×7 cells với month label + day label (Mon/Wed/Fri).
- Archive detail modal: 7 day markers + tasks group theo assignment, mỗi task có weekday label (MON/TUE/...).

### 🛠 Repair (4 file lỗi extract từ .rar gốc)

- `backend/parsers.py` — rebuild từ string trong `.pyc` đã extract được.
- `run.sh`, `run.bat` — rebuild với venv detection + auto pip install.
- `.gitignore` — rebuild theo chuẩn Python.

### 🗃 Migration

Khi chạy lần đầu trên `data.db` cũ:
- 2 bảng mới được tạo (`CREATE TABLE IF NOT EXISTS`).
- Mọi task trong `tasks` được **tự sao chép** sang `task_history` (idempotent — chạy nhiều lần không nhân đôi).
- `user_settings` insert row mặc định (`id=1, pace='medium', ...`).
- Không có bất kỳ data cũ nào bị mất.

### 📦 Đóng gói

Output là `.zip` thay vì `.rar` (Linux env không có rar writer). Cấu trúc thư mục giống hệt — extract bằng WinRAR / 7-Zip / unzip đều OK.
