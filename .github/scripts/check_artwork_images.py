#!/usr/bin/env python3
"""
Проверяет что все изображения работ из коллекций и Available Works
доступны по HTTP (возвращают 200 OK).
"""

import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

BASE_URL = "https://alenam.art/wp-content/uploads/"
ASTRO_DIR = Path("src/pages/art")

def extract_astro_images(filepath: str) -> list[dict]:
    """Извлекает все изображения из .astro файла."""
    with open(filepath, "r") as f:
        content = f.read()
    
    # Ищем все блоки artwork со статусом
    blocks = re.findall(r'\{[^{}]*slug:[^{}]*\}', content, re.DOTALL)
    
    images = []
    for block in blocks:
        name = re.search(r"name: '([^']+)'", block)
        slug = re.search(r"slug: '([^']+)'", block)
        status = re.search(r"status: '([^']+)'", block)
        image = re.search(r"image: base \+ '([^']+)'", block)
        
        if name and slug and image:
            images.append({
                "name": name.group(1),
                "slug": slug.group(1),
                "status": status.group(1) if status else "unknown",
                "image": image.group(1),
                "source": filepath,
            })
    
    return images


def extract_available_works(filepath: str) -> list[dict]:
    """Извлекает все работы из available/index.astro."""
    with open(filepath, "r") as f:
        content = f.read()
    
    blocks = re.findall(r'\{[^{}]*name:[^{}]*\}', content, re.DOTALL)
    
    images = []
    for block in blocks:
        name = re.search(r"name: '([^']+)'", block)
        image = re.search(r"image: base \+ '([^']+)'", block)
        collection = re.search(r"collection: '([^']+)'", block)
        
        if name and image:
            images.append({
                "name": name.group(1),
                "image": image.group(1),
                "collection": collection.group(1) if collection else "unknown",
                "source": filepath,
            })
    
    return images


def check_image_url(url: str) -> tuple[bool, str]:
    """Проверяет что изображение доступно и корректно. Возвращает (ok, message)."""
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Artwork Image Checker)",
        "Accept": "image/avif,image/*,*/*",
    })
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        # Сначала читаем заголовки
        content_type = resp.headers.get("Content-Type", "unknown")
        # Потом читаем тело
        data = resp.read()
        size = len(data)
        
        # Проверяем MIME type — файл должен быть изображением, не HTML
        if "image" not in content_type and "octet-stream" not in content_type:
            return False, f"Invalid Content-Type: {content_type} ({size:,} bytes) — file may not be a real image"
        
        # Проверяем минимальный размер
        if size < 1000:
            return False, f"Too small: {size} bytes ({content_type})"
        
        # Проверяем что файл начинается с магических байтов изображения (не HTML)
        if data[:4] in [b'<!DO', b'<htm', b'<HTM']:
            return False, f"File starts with HTML markup, not image data ({size:,} bytes)"
        
        return True, f"OK ({size:,} bytes, {content_type})"
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        return False, f"URL Error: {e.reason}"
    except Exception as e:
        return False, f"Error: {e}"


def main():
    errors = []
    checked = 0
    
    # 1. Проверяем все изображения в коллекциях
    print("=" * 60)
    print("Checking artwork images in collections...")
    print("=" * 60)
    
    collections_file = ASTRO_DIR / "[...slug].astro"
    if collections_file.exists():
        images = extract_astro_images(str(collections_file))
        print(f"Found {len(images)} artworks in collections")
        
        for img in images:
            url = BASE_URL + img["image"]
            ok, msg = check_image_url(url)
            checked += 1
            
            status_icon = "✓" if ok else "✗"
            print(f"  {status_icon} {img['name']} ({img['status']}) — {msg}")
            
            if not ok:
                errors.append({
                    "file": str(collections_file),
                    "artwork": img["name"],
                    "slug": img["slug"],
                    "url": url,
                    "error": msg,
                })
    
    # 2. Проверяем все изображения в Available Works
    print()
    print("=" * 60)
    print("Checking artwork images in Available Works...")
    print("=" * 60)
    
    available_file = ASTRO_DIR / "available" / "index.astro"
    if available_file.exists():
        works = extract_available_works(str(available_file))
        print(f"Found {len(works)} works in Available Works")
        
        for work in works:
            url = BASE_URL + work["image"]
            ok, msg = check_image_url(url)
            checked += 1
            
            status_icon = "✓" if ok else "✗"
            print(f"  {status_icon} {work['name']} — {msg}")
            
            if not ok:
                errors.append({
                    "file": str(available_file),
                    "artwork": work["name"],
                    "slug": "N/A",
                    "url": url,
                    "error": msg,
                })
    
    # 3. Проверяем изображения в detail pages
    print()
    print("=" * 60)
    print("Checking artwork images in detail pages...")
    print("=" * 60)
    
    detail_file = ASTRO_DIR / "[collection]" / "[work].astro"
    if detail_file.exists():
        images = extract_astro_images(str(detail_file))
        print(f"Found {len(images)} artworks in detail pages")
        
        for img in images:
            url = BASE_URL + img["image"]
            ok, msg = check_image_url(url)
            checked += 1
            
            status_icon = "✓" if ok else "✗"
            print(f"  {status_icon} {img['name']} ({img['status']}) — {msg}")
            
            if not ok:
                errors.append({
                    "file": str(detail_file),
                    "artwork": img["name"],
                    "slug": img["slug"],
                    "url": url,
                    "error": msg,
                })
    
    # Итог
    print()
    print("=" * 60)
    print(f"Checked: {checked} images | Errors: {len(errors)}")
    print("=" * 60)
    
    if errors:
        print("\nFAILED IMAGES:")
        for e in errors:
            print(f"  ✗ {e['artwork']} in {e['file']}")
            print(f"    URL: {e['url']}")
            print(f"    Error: {e['error']}")
        sys.exit(1)
    else:
        print("\nAll images are accessible!")
        sys.exit(0)


if __name__ == "__main__":
    main()
