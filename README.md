# 🧠 Helping_study — Local Edition

> Trợ lý AI giúp sinh viên lập kế hoạch học tập cân bằng. **Chạy 100% offline trên máy bạn**, không cần API key, không tốn phí.

![status](https://img.shields.io/badge/status-MVP-blue) ![python](https://img.shields.io/badge/python-3.10+-green) ![license](https://img.shields.io/badge/license-MIT-orange)

## ✨ Tính năng

- 💬 **UI chat-style** như ChatGPT / Claude — paste text + đính kèm file
- 📎 **Multi-file**: PDF, DOCX, ảnh (OCR tiếng Việt), text — đính kèm nhiều file 1 lúc
- 🤖 **LLM local** (Qwen GGUF) — không cần internet sau khi setup
- 📅 **Lập lịch thông minh**: bin-packing với buffer trước deadline
- 🎚 **Learning pace** (slow / medium / fast) — AI tự điều chỉnh thời gian theo năng lực
- 📊 **Stats dashboard**: heatmap hoạt động cả năm, completion %, streak, breakdown theo thứ
- 🗂 **Archive**: lưu lịch sử mọi tuần đã qua (tách rời khỏi plan, không mất khi xoá plan)
- ⚠️ **Cảnh báo quá tải** + ✅ tracking progress + 🔥 streak gamification
- 📤 **Export iCalendar** vào Google/Apple Calendar

### Giao diện 4 tab

| Tab | Mục đích |
|---|---|
| **Plan** | Chat với AI để tạo plan mới, tick task, theo dõi plan hiện tại |
| **Stats** | Dashboard tổng quan: 4 card chỉ số + heatmap hoạt động + bar chart theo thứ |
| **Archive** | Danh sách các tuần đã qua với mini bar chart; click để xem chi tiết từng task |
| **Settings** | Tốc độ học, giờ rảnh/ngày, dự phòng deadline — áp dụng cho mọi plan mới |

## 📋 Yêu cầu hệ thống

| Item | Tối thiểu | Khuyến nghị |
|------|-----------|-------------|
| **Python** | 3.10 | 3.11 / 3.12 |
| **RAM** | 6 GB (model 1.5B) | 8-16 GB (model 3B-7B) |
| **Disk** | ~3 GB (deps + model) | ~10 GB |
| **GPU** | ❌ Không cần | NVIDIA CUDA / Apple Metal để tăng tốc |
| **Tesseract** | ❌ Không cần | ✅ Nếu muốn upload ảnh đề bài |

Tốc độ sinh kế hoạch (model 3B Q4 trên CPU):
- CPU laptop thường: ~30s-2 phút
- M1/M2 Mac: ~10-20s (với Metal)
- NVIDIA GPU: ~5-10s

---

## 🚀 Cài đặt — 4 bước

### Bước 1 — Python dependencies

```bash
# Giải nén và vào folder
cd balance-buddy

# Tạo venv (khuyến nghị)
python -m venv .venv

# Activate venv:
#   Windows:        .venv\Scripts\activate
#   macOS / Linux:  source .venv/bin/activate

# Cài libraries
pip install -r requirements.txt
```

> **⚠️ Windows + lỗi `[WinError 127]` khi import llama_cpp?**
> Đây là lỗi thiếu C++ runtime. Fix:
> 1. Cài **Visual C++ Redistributable**: https://aka.ms/vs/17/release/vc_redist.x64.exe
> 2. Restart terminal
> 3. Cài lại từ pre-built wheel:
>    ```bash
>    pip uninstall llama-cpp-python -y
>    pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
>    ```

### Bước 2 — Tải model

Vào folder `models/` xem hướng dẫn chi tiết. Hoặc tải nhanh:

**Mặc định: Qwen2.5-3B-Instruct (~1.93 GB)**

🔗 https://huggingface.co/bartowski/Qwen2.5-3B-Instruct-GGUF/resolve/main/Qwen2.5-3B-Instruct-Q4_K_M.gguf

- Click link → trình duyệt sẽ tải file `.gguf` về
- **Copy file vào folder `models/`**
- Xong! App sẽ tự detect

**Nếu máy yếu (RAM < 8GB): Qwen2.5-1.5B (~1.12 GB)**

🔗 https://huggingface.co/bartowski/Qwen2.5-1.5B-Instruct-GGUF/resolve/main/Qwen2.5-1.5B-Instruct-Q4_K_M.gguf

### Bước 3 — (Tuỳ chọn) Cài Tesseract OCR

**Chỉ cần nếu muốn upload ảnh đề bài.** Có thể bỏ qua bước này — vẫn dùng được PDF/DOCX/text bình thường.

<details>
<summary><b>Windows</b></summary>

1. Tải installer: https://github.com/UB-Mannheim/tesseract/wiki
2. Khi cài, chọn additional languages → **Vietnamese**
3. Thêm path `C:\Program Files\Tesseract-OCR` vào PATH (hoặc reboot)
</details>

<details>
<summary><b>macOS</b></summary>

```bash
brew install tesseract tesseract-lang
```
</details>

<details>
<summary><b>Ubuntu/Debian</b></summary>

```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-vie tesseract-ocr-eng
```
</details>

### Bước 4 — Chạy

```bash
# Windows:
run.bat

# macOS / Linux:
bash run.sh
```

Mở trình duyệt: **http://localhost:8000**

---

## 🎯 Cách dùng

1. **Tab Settings** (lần đầu): chọn **learning pace** (slow/medium/fast) và giờ rảnh/ngày → bấm **Lưu thay đổi**
2. **Tab Plan**: paste đề bài hoặc đính kèm PDF / DOCX / ảnh, chọn deadline, bấm gửi (→)
3. AI sẽ phân rã + sắp lịch trong 30s-2 phút (theo pace đã chọn)
4. Tick từng task khi hoàn thành để cập nhật progress + streak + lưu vào history
5. **Tab Stats**: xem heatmap cả năm, completion %, streak, breakdown theo thứ
6. **Tab Archive**: xem từng tuần đã qua, click vào để xem chi tiết task

### Giải thích Learning pace

| Pace | Multiplier | Khi nào dùng |
|---|---|---|
| **Slow** 🚶 | ×1.5 | Bạn cần đọc kỹ, hấp thụ chậm — AI cho thêm thời gian mỗi task |
| **Medium** 🏃 | ×1.0 | Mặc định, nhịp chuẩn |
| **Fast** ⚡ | ×0.7 | Tiếp thu nhanh, muốn session dày hơn |

Pace ảnh hưởng cả việc **AI phân rã** (gợi ý chương dài/ngắn) lẫn **scheduler** (nhân thời gian từng task).

---

## 📂 Cấu trúc project

```
balance-buddy/
├── backend/
│   ├── main.py         FastAPI app (plan, settings, stats, archive endpoints)
│   ├── llm.py          Llama-cpp inference + JSON schema enforcement + pace-aware prompt
│   ├── parsers.py      PDF / DOCX / OCR / text extractors
│   ├── scheduler.py    Greedy bin-packing + learning-pace multiplier
│   ├── db.py           SQLite — plans, tasks, settings, persistent task_history
│   └── models.py       Pydantic schemas (plan, settings, stats, archive)
├── frontend/
│   └── index.html      4-tab SPA: Plan / Stats / Archive / Settings
├── models/             ← Copy file *.gguf vào đây
│   └── README.md       Hướng dẫn model
├── sample_data/
│   └── sample_assignment.txt
├── requirements.txt
├── .env                Cấu hình (model, GPU, OCR)
├── run.bat             Launcher Windows
├── run.sh              Launcher macOS / Linux
└── data.db             SQLite (tự tạo khi chạy lần đầu)
```

---

## ⚙️ Cấu hình nâng cao

Edit file `.env`:

### Bật GPU acceleration

```env
N_GPU_LAYERS=-1    # đẩy hết layer lên GPU
```

Sau đó cài lại `llama-cpp-python` với CUDA hoặc Metal support:

```bash
# NVIDIA CUDA 12.1:
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu121

# Apple Metal (Mac M-series):
CMAKE_ARGS="-DGGML_METAL=on" pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
```

### Đổi model

```env
MODEL_FILE=Qwen2.5-1.5B-Instruct-Q4_K_M.gguf
```

(Bỏ trống = auto-detect file đầu tiên trong `models/`)

### Mock mode (test UI không cần model)

```env
MOCK_LLM=1
```

→ Mọi request trả về plan cố định trong 0.1s. Dùng để demo UI khi chưa cài xong model.

---

## 🛠 API endpoints

| Method | Path | Mô tả |
|---|---|---|
| GET | `/api/health` | Health + model status |
| GET | `/api/model/status` | Trạng thái model (loading / ready / error) |
| POST | `/api/model/preload` | Trigger model load |
| **POST** | **`/api/plan`** | **Tạo plan (tự đọc settings; có thể override pace/daily/buffer)** |
| GET | `/api/plans` | Liệt kê plan |
| GET | `/api/plans/{id}` | Chi tiết plan |
| DELETE | `/api/plans/{id}` | Xoá plan (history vẫn còn) |
| PATCH | `/api/tasks/{id}` | Toggle complete |
| GET | `/api/streak` | Streak info |
| GET | `/api/plans/{id}/ics` | Export iCalendar |
| **GET / PUT** | **`/api/settings`** | **Đọc / cập nhật learning pace + cấu hình thời gian** |
| **GET** | **`/api/stats/summary`** | **4 card: avg %, best week, streak, weeks tracked** |
| **GET** | **`/api/stats/activity?days=365`** | **Heatmap hoạt động** |
| **GET** | **`/api/stats/by-weekday?mode=distribution\|completion`** | **Bar chart 7 thứ** |
| **GET** | **`/api/archives`** | **Danh sách tuần đã lưu** |
| **GET** | **`/api/archives/{week_id}`** | **Chi tiết tuần** (week_id format `YYYY-Www`) |
| **DELETE** | **`/api/archives/{week_id}`** | **Xoá 1 tuần** |
| **DELETE** | **`/api/archives`** | **Xoá toàn bộ history** |

Swagger UI tự động tại: http://localhost:8000/docs

---

## 🐛 Troubleshooting

| Lỗi | Cách fix |
|---|---|
| `[WinError 127]` import llama_cpp | Cài VC++ Redistributable (xem Bước 1) |
| `Không tìm thấy file .gguf trong ./models/` | Tải model về và copy vào `models/` (Bước 2) |
| `TesseractNotFoundError` | Cài Tesseract binary (Bước 3), hoặc dùng PDF/text |
| `Missing language pack` (OCR) | Cài Vietnamese pack, hoặc đổi `OCR_LANGS=eng` |
| Generation chậm > 3 phút | Dùng model 1.5B, hoặc bật GPU (`N_GPU_LAYERS=-1`) |
| Out of memory | Dùng model 1.5B, giảm `N_CTX=2048` |
| Port 8000 đã bị dùng | Chạy: `uvicorn main:app --port 8080` |
| Server crash khi load model | Set `PRELOAD_MODEL=0` trong `.env` để debug |

---

## 🧩 Kiến trúc tổng quan

```
   User (chat UI)
        │ text + files
        ▼
   ┌──────────────────────────┐
   │  FastAPI /api/plan       │
   └──────┬───────────────────┘
          ▼
   ┌──────────────────────────┐
   │  parsers.py              │
   │  PDF → pdfplumber        │
   │  DOCX → python-docx      │
   │  Image → pytesseract OCR │
   │  Text → utf-8 decode     │
   └──────┬───────────────────┘
          ▼ plain text
   ┌──────────────────────────┐
   │  llm.py                  │
   │  llama-cpp-python        │
   │  + GGUF model (./models/)│
   │  + JSON schema grammar   │
   │  → guaranteed valid JSON │
   └──────┬───────────────────┘
          ▼ DecomposedAssignment
   ┌──────────────────────────┐
   │  scheduler.py            │
   │  greedy bin-packing      │
   │  + daily budget          │
   │  + buffer days           │
   └──────┬───────────────────┘
          ▼ schedule dict
   ┌──────────────────────────┐
   │  db.py (SQLite)          │
   └──────┬───────────────────┘
          ▼ StudyPlan JSON
       Frontend renders plan
```

---

## 📜 License

MIT — Free cho mọi mục đích, kể cả thương mại.
