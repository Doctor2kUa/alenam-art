# AI Agent Task: migrate Alena Mart site to Sveltia CMS + GitHub + Netlify + Cloudflare R2

Дата подготовки: 2026-05-27

## Роль агента

Ты работаешь в репозитории `Doctor2kUa/alenam-art`.
Нужно конвертировать текущий Astro static site в сайт, управляемый через Sveltia CMS:

- GitHub хранит код и контент.
- Netlify собирает и публикует сайт.
- Sveltia CMS доступна по `/admin/` и коммитит контент в GitHub.
- Cloudflare R2 хранит изображения и видео.

Работай маленькими шагами. После каждого шага должна быть конкретная проверка. Не делай большой переписывающий коммит без промежуточных проверок.

## Ветка и публикация

Нельзя пушить новую версию прямо в `main`.

В начале работы:

```bash
git fetch origin
git switch main
git pull --ff-only
git switch -c feature/sveltia-cms-r2-migration
```

В конце работы:

```bash
npm run build
git status --short
git push -u origin feature/sveltia-cms-r2-migration
```

После пуша открыть PR из `feature/sveltia-cms-r2-migration` в `main`. В PR указать Netlify Deploy Preview URL и список ручных настроек, которые требуют доступов Cloudflare/Netlify.

## Текущее состояние проекта

Проект сейчас:

- Astro static site.
- Tailwind через `@tailwindcss/vite`.
- Netlify уже настроен: `netlify.toml` выполняет `npm run build`, публикует `dist`, Node `22`.
- CMS сейчас нет.
- Основной контент зашит прямо в `.astro` файлах.
- Изображения в коде ссылаются на `https://alenam.art/wp-content/uploads/`.
- Локальные папки `public/uploads/` и `wordpress-backup/` не отслеживаются Git и весят около 929 МБ и 1.0 ГБ.
- `npm run build` проходит, но есть предупреждения о дублях маршрутов `/contact` и `/story`.

Важные файлы текущей реализации:

```text
src/pages/index.astro
src/pages/art/index.astro
src/pages/art/[...slug].astro
src/pages/art/[collection]/[work].astro
src/pages/art/available/index.astro
src/pages/blog/index.astro
src/pages/story.astro
src/pages/story/index.astro
src/pages/contact.astro
src/pages/contact/index.astro
src/layouts/BaseLayout.astro
src/components/Header.astro
src/components/Footer.astro
.github/scripts/check_artwork_images.py
.github/workflows/check-artwork-images.yml
```

## Документация, которую нужно учитывать

- Sveltia CMS start guide: `https://sveltiacms.app/en/docs/start`
- Sveltia GitHub backend: `https://sveltiacms.app/en/docs/backends/github`
- Sveltia media storage: `https://sveltiacms.app/en/docs/media`
- Sveltia Cloudflare R2 integration: `https://sveltiacms.app/en/docs/media/cloudflare-r2`
- Sveltia troubleshooting: `https://sveltiacms.app/en/docs/troubleshooting`
- Netlify OAuth provider tokens: `https://docs.netlify.com/manage/security/secure-access-to-sites/oauth-provider-tokens/`

Документация Sveltia прямо говорит:

- `public/admin/index.html` должен подключать только `https://unpkg.com/@sveltia/cms/dist/sveltia-cms.js`.
- Не добавляй CSS-файл Sveltia.
- Не добавляй `type="module"` к script.
- Если Cloudflare Rocket Loader включен, добавь `data-cfasync="false"` к script.
- GitHub backend использует `backend.name: github` и `repo: owner/repo`.
- Git LFS в GitHub backend не поддерживается.
- Для R2 secret access key нельзя хранить в `config.yml`; пользователь вводит его в UI CMS при первом использовании.

## Целевая структура

Сделай один канонический источник контента. Не оставляй данные работ, коллекций и событий продублированными в нескольких `.astro` файлах.

Рекомендуемая структура:

```text
public/admin/index.html
public/admin/config.yml
src/content/config.ts
src/content/settings/site.json
src/content/pages/home.json
src/content/pages/story.md
src/content/collections/big-city-life.json
src/content/collections/bits-and-pieces.json
src/content/collections/little-pleasures.json
src/content/collections/at-the-seaside.json
src/content/collections/mind-games.json
src/content/collections/confessions-should-be-better-planned.json
src/content/collections/flora.json
src/content/artworks/<collection-slug>/<artwork-slug>.json
src/content/events/<event-slug>.md
src/lib/content.ts
src/lib/media.ts
```

Можно выбрать YAML вместо JSON, если это лучше сочетается с Sveltia config. Главное: Astro должен читать те же файлы, которые редактирует CMS.

## Модель контента

### Collection

Минимальные поля:

```text
slug
title
subtitle
description
cover_image
order
prev_slug
next_slug
cta
featured_on_home
```

`works` и `available` не вводить руками. Считать из `artworks`.

### Artwork

Минимальные поля:

```text
slug
collection
name
technique
size
year
status: Available | Sold | Private collection
image
images
cta
order
featured_on_home
featured_available
description
```

`collection` должен быть relation/select на существующую коллекцию.

### Event

Минимальные поля:

```text
slug
title
event_date
published_date
city
country
venue
cover_image
gallery
excerpt
related_collection
related_artworks
body
```

На карточках `/blog/` показывать `event_date`, а не дату публикации.

### Site settings

Минимальные поля:

```text
site_title
site_description
artist_name
email
instagram_url
facebook_url
linkedin_url
logo
og_image
favicon
media_base_url
```

## R2 и медиа

Не коммить `public/uploads/` и `wordpress-backup/`.

Цель: все используемые на сайте медиа должны грузиться из Cloudflare R2 public URL, например:

```text
https://media.alenam.art/uploads/2025/01/IMG_5829.avif
```

Если R2 production domain еще не выдан, используй временный `pub-*.r2.dev` только для проверки и оставь явный TODO для замены на production custom domain.

Нужные параметры для `public/admin/config.yml`:

```yaml
media_libraries:
  all:
    slugify_filename: true
    transformations:
      raster_image:
        format: webp
        quality: 85
        width: 2048
        height: 2048
  cloudflare_r2:
    access_key_id: REPLACE_WITH_R2_ACCESS_KEY_ID
    bucket: REPLACE_WITH_R2_BUCKET
    account_id: REPLACE_WITH_CLOUDFLARE_ACCOUNT_ID
    public_url: https://media.alenam.art
    prefix: uploads/
    jurisdiction: default
```

Не добавляй `secret_access_key` в репозиторий.

Для Cloudflare R2 CORS нужно разрешить домен админки:

```json
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET", "PUT", "HEAD"],
    "AllowedOrigins": [
      "https://alenam.art",
      "https://*.netlify.app"
    ],
    "ExposeHeaders": ["ETag"],
    "MaxAgeSeconds": 3000
  }
]
```

Если Cloudflare не принимает wildcard в таком виде для конкретной настройки, указать точный production домен и точный Netlify preview/admin домен.

## Маленькие задачи

### 1. Зафиксировать baseline

Действия:

- Запустить `git status --short --branch`.
- Запустить `npm run build`.
- Сохранить в заметках предупреждения сборки.

Проверка:

- Сборка проходит.
- Предупреждения о `/contact` и `/story` записаны как известные проблемы.

### 2. Создать Sveltia admin shell

Действия:

- Создать `public/admin/index.html`.
- Создать минимальный `public/admin/config.yml`.
- Использовать GitHub backend:

```yaml
backend:
  name: github
  repo: Doctor2kUa/alenam-art
  branch: feature/sveltia-cms-r2-migration
```

На финальном production PR явно решить, оставить `branch: main` после merge или использовать editorial workflow. Не оставляй случайно production CMS, который пишет в миграционную ветку.

`index.html`:

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="robots" content="noindex">
    <title>Sveltia CMS</title>
  </head>
  <body>
    <script data-cfasync="false" src="https://unpkg.com/@sveltia/cms/dist/sveltia-cms.js"></script>
  </body>
</html>
```

Проверка:

- `npm run build` проходит.
- В `dist/admin/index.html` есть script Sveltia.
- В `public/admin/index.html` нет Sveltia CSS и нет `type="module"`.

### 3. Добавить схемы Astro content collections

Действия:

- Создать `src/content/config.ts`.
- Описать схемы для `settings`, `pages`, `collections`, `artworks`, `events`.
- Поля `status`, `collection`, `slug`, `order`, `image` валидировать строго.

Проверка:

- `npm run build` проходит.
- Ошибки схемы не скрываются через `any`.

### 4. Перенести коллекции в content files

Действия:

- Извлечь коллекции из `src/pages/art/index.astro` и `src/pages/art/[...slug].astro`.
- Создать файлы в `src/content/collections/`.
- Удалить ручные `works` и `available`; считать их позже из работ.

Проверка:

- `rg "const collections" src/pages` не находит массивов с бизнес-данными.
- `/art/` визуально показывает те же 7 коллекций.
- `npm run build` проходит.

### 5. Перенести artworks в один источник

Действия:

- Извлечь все работы из `src/pages/art/[...slug].astro`, `src/pages/art/[collection]/[work].astro`, `src/pages/art/available/index.astro`.
- Создать `src/content/artworks/<collection-slug>/<artwork-slug>.json`.
- Устранить расхождения между списком коллекции, detail page и Available Works.
- Если у работы нет `slug`, создать стабильный slug и проверить ссылки.

Проверка:

- `rg "const availableWorks|artworks: \\[" src/pages` не находит старых массивов.
- `/art/<collection>/` строится из content files.
- `/art/<collection>/<work>/` строится из тех же content files.
- `/art/available/` строится фильтром `status === "Available"`.
- Количество available работ на `/art/` совпадает с фактическими работами.
- `npm run build` проходит.

### 6. Перенести события в content files

Действия:

- Извлечь события из `src/pages/blog/index.astro`.
- Создать `src/content/events/<event-slug>.md`.
- Разделить `event_date` и `published_date`.
- Создать страницу detail route `src/pages/blog/[event].astro`.

Проверка:

- `/blog/` показывает список из content files.
- Все ссылки `View event` открывают реальные страницы, не 404.
- `find dist/blog -maxdepth 3 -name index.html` показывает index и event pages.
- `npm run build` проходит.

### 7. Перенести home, story, settings

Действия:

- Вынести данные главной страницы в `src/content/pages/home.json`.
- Вынести story/body в `src/content/pages/story.md`.
- Вынести email, соцсети, logo, og image, favicon в `src/content/settings/site.json`.
- Header, Footer, BaseLayout должны читать settings через helper, а не держать WP URLs в компоненте.

Проверка:

- `rg "alenam.art/wp-content/uploads" src/components src/layouts src/pages` не находит новых hardcoded ссылок.
- Главная, Story, Header, Footer визуально не потеряли текущую структуру.
- `npm run build` проходит.

### 8. Убрать дубли маршрутов

Действия:

- Оставить только один route для `/story/`.
- Оставить только один route для `/contact/`.
- Если нужно сохранить старые файлы временно, переименовать их так, чтобы Astro не создавал route.

Проверка:

- `npm run build` больше не показывает warnings о route collision `/story` и `/contact`.
- `/story/` и `/contact/` доступны.

### 9. Сделать media helper и заменить WordPress origin

Действия:

- Создать `src/lib/media.ts`.
- Helper должен корректно принимать:
  - абсолютный `https://...` URL;
  - `/uploads/...`;
  - `uploads/...`;
  - старый `https://alenam.art/wp-content/uploads/...` и превращать его в R2 public URL.
- Добавить `PUBLIC_MEDIA_BASE_URL` с fallback на `https://media.alenam.art`.
- Обновить `.env.example`, если файла нет - создать.

Проверка:

- `rg "wp-content/uploads" src public/admin` не находит активных ссылок, кроме исторических инструкций/комментариев, если они действительно нужны.
- HTML в `dist/` не содержит `wp-content/uploads`.
- `npm run build` проходит.

### 10. Подготовить перенос используемых медиа в R2

Действия:

- Не загружать все 929 МБ вслепую.
- Написать скрипт или команду, которая собирает только реально используемые asset paths из content files.
- Сформировать manifest `ai_instructions/r2_used_assets_manifest.md` или `.json` со списком source path -> R2 key.
- Если есть доступы AWS-compatible/R2, загрузить используемые файлы из `public/uploads/` в R2 с сохранением ключей `uploads/YYYY/MM/file.ext`.
- Если доступов нет, оставить manifest и точные команды для владельца.

Проверка:

- Для каждого `image`/`gallery` значения есть R2 key в manifest.
- Не добавлены файлы из `public/uploads/` в Git.
- `git status --short` не показывает staged/untracked media files из `public/uploads/`.

### 11. Настроить Sveltia collections

Действия:

- В `public/admin/config.yml` описать collections для:
  - Site Settings
  - Home Page
  - Story Page
  - Collections
  - Artworks
  - Events
- Для статусов использовать select.
- Для collection у artwork использовать relation/select.
- Для изображений использовать image/file widgets и R2 media storage.
- Обязательные поля пометить required.
- Порядок и labels сделать понятными редактору.

Проверка:

- `/admin/` открывается в Netlify preview.
- CMS показывает все коллекции.
- Создание тестовой записи локально или через preview не ломает `npm run build`.
- В config нет secret values.

### 12. Настроить GitHub authentication через Netlify

Действия:

- В Netlify подключить GitHub OAuth provider для сайта.
- GitHub OAuth callback URL должен быть:

```text
https://api.netlify.com/auth/done
```

- Владелец/редактор должен иметь write access к GitHub repo.
- Если Netlify OAuth недоступен, временно использовать Sveltia "Sign In with Token" и описать это в PR.

Проверка:

- Редактор может зайти в `/admin/`.
- CMS видит repo `Doctor2kUa/alenam-art`.
- Тестовый content edit создает commit в правильной ветке.

### 13. Netlify и environment

Действия:

- Проверить `netlify.toml`; build должен остаться `npm run build`, publish `dist`, Node `22`.
- Добавить в Netlify environment:

```text
PUBLIC_MEDIA_BASE_URL=https://media.alenam.art
```

- Если production media domain еще не готов, использовать preview value и оставить TODO в PR.

Проверка:

- Netlify deploy preview собирается.
- Preview HTML использует R2 public URL.
- Netlify Forms на `/contact/` не сломан.

### 14. Обновить image checker

Действия:

- Переписать `.github/scripts/check_artwork_images.py`, чтобы он читал content files, а не парсил `.astro` regex-ами.
- Проверять все artwork/event/page images через итоговый public URL.
- Обновить workflow branch list, если нужна новая migration branch.

Проверка:

- `python .github/scripts/check_artwork_images.py` проходит локально.
- GitHub Action проходит на PR.

### 15. Финальная чистка

Действия:

- Удалить неиспользуемые hardcoded arrays.
- Удалить старые route duplicates.
- Проверить, что старые WordPress URLs не попали в итоговый HTML.
- Проверить, что site title, OG image, favicon берутся из settings/content.
- Обновить `README.md` кратким разделом "Content editing" с `/admin/`, Netlify, R2 и запретом коммита media.

Проверка:

```bash
npm run build
rg "wp-content/uploads" dist src public/admin
rg "const collections|const events|const availableWorks|artworks: \\[" src/pages
git status --short
```

Допустимо, если `wp-content/uploads` встречается только в старых markdown-инструкциях, не в `src`, `public/admin` и `dist`.

## Definition of Done

Готово только если:

- Сайт собирается без Astro route collision warnings.
- `/admin/` доступен в Netlify Deploy Preview.
- Sveltia CMS настроена на GitHub backend.
- Контент работ, коллекций, событий, story и home редактируется через файлы в `src/content`.
- Нет дублирования одного и того же artwork/event массива в нескольких `.astro`.
- `/art/`, `/art/<collection>/`, `/art/<collection>/<work>/`, `/art/available/`, `/blog/`, `/blog/<event>/`, `/story/`, `/contact/` работают.
- Изображения в итоговом HTML идут через R2 public URL, не через WordPress origin.
- Secret Access Key от R2 не хранится в репозитории.
- `public/uploads/` и `wordpress-backup/` не добавлены в Git.
- Новая версия запушена в отдельную ветку и открыта как PR.

## Что написать в финальном отчете

В финальном ответе владельцу проекта укажи:

- имя ветки;
- ссылку на PR;
- ссылку на Netlify Deploy Preview;
- R2 public URL, который использован;
- какие ручные действия остались в Cloudflare/Netlify;
- результат `npm run build`;
- результат image checker;
- есть ли оставшиеся TODO и почему.
