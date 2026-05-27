#!/usr/bin/env python3
"""
Проверяет что все изображения из content collections доступны по HTTP.
Читает напрямую из JSON/MD файлов, не парсит .astro.
"""

import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

# Базовый URL для проверки — берём из env или fallback на WP
BASE_URL = os.environ.get("MEDIA_BASE_URL", "https://alenam.art/wp-content/uploads/").rstrip("/") + "/"
PROJECT_DIR = Path(__file__).resolve().parent.parent.parent


def check_image_url(url: str) -> tuple:
    """Проверяет что изображение доступно и корректно. Возвращает (ok, message)."""
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Artwork Image Checker)",
        "Accept": "image/avif,image/*,*/*",
    })
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        content_type = resp.headers.get("Content-Type", "unknown")
        data = resp.read()
        size = len(data)

        if "image" not in content_type and "octet-stream" not in content_type:
            return False, f"Invalid Content-Type: {content_type} ({size:,} bytes)"
        if size < 1000:
            return False, f"Too small: {size} bytes ({content_type})"
        if data[:4] in [b'<!DO', b'<htm', b'<HTM']:
            return False, f"File starts with HTML markup, not image data ({size:,} bytes)"
        return True, f"OK ({size:,} bytes, {content_type})"
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        return False, f"URL Error: {e.reason}"
    except Exception as e:
        return False, f"Error: {e}"


def collect_images_from_json(filepath: Path) -> list:
    """Извлекает все image/cover_image из JSON файла."""
    images = []
    rel = filepath.relative_to(PROJECT_DIR)
    try:
        data = json.loads(filepath.read_text())
    except (json.JSONDecodeError, Exception):
        return images

    name = data.get("name", data.get("title", filepath.stem))

    for field in ("image", "cover_image"):
        val = data.get(field)
        if isinstance(val, str) and val.strip():
            images.append({"name": name, "path": val.strip(), "source": str(rel)})

    # Массив images/gallery
    for field in ("images", "gallery"):
        val = data.get(field)
        if isinstance(val, list):
            for i, item in enumerate(val):
                if isinstance(item, dict):
                    img_val = item.get("image", item.get("url", ""))
                elif isinstance(item, str):
                    img_val = item
                else:
                    continue
                if img_val and isinstance(img_val, str):
                    img_name = item.get("name", item.get("title", f"{name}_{i}")) if isinstance(item, dict) else f"{name}_{i}"
                    images.append({"name": img_name, "path": img_val.strip(), "source": str(rel)})

    return images


def collect_images_from_md(filepath: Path) -> list:
    """Извлекает cover_image из frontmatter MD файла."""
    images = []
    rel = filepath.relative_to(PROJECT_DIR)
    content = filepath.read_text()

    if not content.startswith("---"):
        return images

    end = content.find("---", 3)
    if end == -1:
        return images

    fm = content[3:end]
    # Простой парсинг YAML frontmatter
    for line in fm.split("\n"):
        line = line.strip()
        if line.startswith("cover_image:"):
            val = line.split(":", 1)[1].strip().strip("'\"")
            if val:
                images.append({"name": filepath.stem, "path": val, "source": str(rel)})
                break

    return images


def normalize_image_path(path: str) -> str:
    """Убирает префиксы и нормализует путь для проверки через BASE_URL."""
    path = path.strip()
    # Убираем абсолютные WP URL
    if "wp-content/uploads/" in path:
        path = path.split("wp-content/uploads/")[-1]
    # Убираем ведущий /
    path = path.lstrip("/")
    # Убираем uploads/ если есть
    if path.startswith("uploads/"):
        path = path[len("uploads/"):]
    return path


def main():
    errors = []
    checked = 0
    seen_urls = set()

    dirs_to_check = [
        ("Artworks", PROJECT_DIR / "src/content/artworks", collect_images_from_json, "*.json"),
        ("Collections", PROJECT_DIR / "src/content/collections", collect_images_from_json, "*.json"),
        ("Events", PROJECT_DIR / "src/content/events", collect_images_from_md, "*.md"),
        ("Pages", PROJECT_DIR / "src/content/pages", collect_images_from_json, "*.json"),
    ]

    for label, dirpath, extractor, pattern in dirs_to_check:
        if not dirpath.exists():
            continue

        print(f"\n{'=' * 60}")
        print(f"Checking {label} in {dirpath.relative_to(PROJECT_DIR)}...")
        print("=" * 60)

        files = list(dirpath.rglob(pattern)) if "**" in pattern else list(dirpath.glob(pattern))
        local_checked = 0

        for f in sorted(files):
            images = extractor(f)
            for img in images:
                rel_path = normalize_image_path(img["path"])
                if not rel_path:
                    continue
                url = BASE_URL + rel_path
                if url in seen_urls:
                    continue
                seen_urls.add(url)

                ok, msg = check_image_url(url)
                checked += 1
                local_checked += 1
                icon = "✓" if ok else "✗"
                print(f"  {icon} {img['name']} — {msg}")

                if not ok:
                    errors.append({
                        "source": img["source"],
                        "artwork": img["name"],
                        "url": url,
                        "error": msg,
                    })

        print(f"  Checked {local_checked} files, {len([u for u in seen_urls])} unique images")

    print(f"\n{'=' * 60}")
    print(f"Total checked: {checked} images | Errors: {len(errors)}")
    print("=" * 60)

    if errors:
        print("\nFAILED:")
        for e in errors:
            print(f"  ✗ {e['artwork']} ({e['source']})")
            print(f"    URL: {e['url']}")
            print(f"    Error: {e['error']}")
        sys.exit(1)
    else:
        print("\nAll images OK!")
        sys.exit(0)


if __name__ == "__main__":
    main()
