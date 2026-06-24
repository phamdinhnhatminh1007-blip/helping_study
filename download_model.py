"""Tải model GGUF từ Hugging Face vào folder ./models/.

Cách dùng:
    python download_model.py qwen3-8b   # ⭐ Khuyến nghị (~5 GB, smart)
    python download_model.py qwen3-14b  # 🚀 Mạnh nhất (~8.5 GB, cần 16GB RAM)
    python download_model.py 3b         # Qwen2.5-3B (cũ, ~1.9 GB, nhanh nhưng kém)
    python download_model.py 1.5b       # Qwen2.5-1.5B (máy yếu)
    python download_model.py 7b         # Qwen2.5-7B (~4.4 GB)
    python download_model.py deepseek   # DeepSeek-R1 distill (reasoning, ~5 GB)
"""
from __future__ import annotations

import sys
from pathlib import Path

# (repo_id, filename, approx_size_gb, description)
MODELS = {
    # --- 2026 RECOMMENDED ---
    "qwen3-8b": (
        "bartowski/Qwen_Qwen3-8B-GGUF",
        "Qwen_Qwen3-8B-Q4_K_M.gguf",
        5.03,
        "⭐ Qwen3-8B — Mới nhất, tiếng Việt cực tốt, reasoning mạnh. Cần ~10GB RAM.",
    ),
    "qwen3-14b": (
        "bartowski/Qwen_Qwen3-14B-GGUF",
        "Qwen_Qwen3-14B-Q4_K_M.gguf",
        8.99,
        "🚀 Qwen3-14B — Mạnh nhất trong tầm laptop. Cần ~16GB RAM.",
    ),
    "deepseek": (
        "bartowski/DeepSeek-R1-Distill-Qwen-7B-GGUF",
        "DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf",
        4.68,
        "🧠 DeepSeek-R1-Distill-Qwen-7B — Reasoning siêu mạnh (chain-of-thought).",
    ),

    # --- Qwen2.5 (cũ hơn nhưng vẫn ổn) ---
    "7b": (
        "bartowski/Qwen2.5-7B-Instruct-GGUF",
        "Qwen2.5-7B-Instruct-Q4_K_M.gguf",
        4.36,
        "Qwen2.5-7B — Trung gian, cần ~8GB RAM.",
    ),
    "3b": (
        "bartowski/Qwen2.5-3B-Instruct-GGUF",
        "Qwen2.5-3B-Instruct-Q4_K_M.gguf",
        1.93,
        "Qwen2.5-3B — Nhỏ, nhanh nhưng KHÔNG đủ thông minh cho lý thuyết phức tạp.",
    ),
    "1.5b": (
        "bartowski/Qwen2.5-1.5B-Instruct-GGUF",
        "Qwen2.5-1.5B-Instruct-Q4_K_M.gguf",
        1.12,
        "Qwen2.5-1.5B — Cực nhỏ, chỉ cho test hoặc máy <6GB RAM.",
    ),
}

ALIASES = {
    "qwen3": "qwen3-8b",
    "default": "qwen3-8b",
    "best": "qwen3-14b",
    "smart": "qwen3-8b",
    "fast": "1.5b",
}


def verify_gguf(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, "file không tồn tại"
    size_gb = path.stat().st_size / 1e9
    if size_gb < 0.5:
        return False, f"size quá nhỏ ({size_gb:.3f} GB) — có thể download chưa xong"
    with open(path, "rb") as f:
        magic = f.read(4)
    if magic != b"GGUF":
        return False, f"không phải file GGUF (magic={magic!r})"
    return True, f"OK ({size_gb:.2f} GB, magic GGUF)"


def list_models() -> None:
    print("Các model có sẵn:\n")
    for key, (repo, fname, size, desc) in MODELS.items():
        print(f"  {key:12s} {size:5.2f} GB  {desc}")
    print("\nAliases: " + ", ".join(f"{k}→{v}" for k, v in ALIASES.items()))
    print("\nCách dùng:  python download_model.py <key>")
    print("Ví dụ:      python download_model.py qwen3-8b")


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "list"):
        list_models()
        return

    choice = sys.argv[1].lower()
    choice = ALIASES.get(choice, choice)

    if choice not in MODELS:
        print(f"❌ Không biết model: {sys.argv[1]!r}\n")
        list_models()
        sys.exit(1)

    repo_id, filename, size_gb, desc = MODELS[choice]
    target_dir = Path(__file__).parent / "models"
    target_dir.mkdir(exist_ok=True)
    target_path = target_dir / filename

    if target_path.exists():
        ok, msg = verify_gguf(target_path)
        if ok:
            print(f"✅ File đã có sẵn: {target_path}")
            print(f"   {msg}")
            print(f"\n💡 Để app dùng model này, set trong .env:")
            print(f"   MODEL_FILE={filename}")
            return
        else:
            print(f"⚠ File hiện có không hợp lệ ({msg}), tải lại...")
            target_path.unlink()

    print(f"📥 {desc}")
    print(f"   Repo:  {repo_id}")
    print(f"   File:  {filename}")
    print(f"   Đích:  {target_path}")
    print(f"   Size:  ~{size_gb} GB")
    print(f"   (Có thể mất 5-30 phút tuỳ tốc độ mạng. Resume nếu bị đứt.)")
    print()

    try:
        from huggingface_hub import hf_hub_download
    except ImportError:
        print("❌ Thiếu huggingface_hub. Chạy: pip install -r requirements.txt")
        sys.exit(1)

    try:
        local = hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir=str(target_dir),
        )
        print(f"\n✓ Đã tải xong: {local}")
    except Exception as e:
        print(f"\n❌ Lỗi tải: {e}")
        print("   Thử lại / dùng VPN / chọn model khác.")
        sys.exit(1)

    print("\n🔍 Verify file...")
    ok, msg = verify_gguf(target_path)
    if ok:
        print(f"✅ {msg}")
        print(f"\n📝 Cập nhật .env để dùng model này:")
        print(f"   MODEL_FILE={filename}")
        print(f"\n👉 Sau đó chạy: run.bat (hoặc bash run.sh)")
    else:
        print(f"❌ {msg}")
        sys.exit(1)


if __name__ == "__main__":
    main()
