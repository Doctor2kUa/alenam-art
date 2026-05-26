# КОНСОЛИДИРОВАННЫЙ ПЛАН ЗАДАЧ ALENA MART

## Источники:
- ai_agent_plan_alenam_art_new_version.md (новая версия правок)
- STORY_PLAN.md (изображения для Story с оригинала)

---

## P0 — КРИТИЧЕСКИЕ ЗАДАЧИ

### P0.1: Исправить даты в Exhibitions & Events
**Проблема:** У старых выставок (2013-2019) в карточках указаны даты December 2024 / November 2024 (дата публикации поста вместо даты события).

**Что сделать:**
- Для каждого события использовать реальную дату события, а не дату публикации
- Формат: `May 2025 · Prague · SANTE` или `April 2018 · Minsk` или `Autumn 2014 · Minsk`
- Если точная дата неизвестна — использовать только год или сезон + год

**Конкретные исправления:**
- "boys vs girls" → `December 2019` (не `December 2024`)
- "Dream on" → `October 2019` (не `December 2024`)
- "35 Expo" → `April 2018` (не `December 2024`)
- "Chaotic still-life" → `Autumn 2014` (не `November 2024`)
- "First Expo" → `2013` (не `November 2024`)

**Acceptance:** Нет противоречий между датой в карточке и датой в описании. Старые события показывают реальные годы.

---

### P0.2: Исправить навигацию Previous/Next между коллекциями
**Проблема:** Порядок коллекций в навигации не соответствует порядку на `/art/`, у Mind Games пустой `Next →`.

**Единый порядок коллекций:**
1. Big City Life
2. Bits and Pieces
3. Little Pleasures
4. At the Seaside
5. Mind Games
6. Confessions should be better planned
7. Flora

**Правильная навигация:**
- Big City Life: `All Collections / Next → Bits and Pieces`
- Bits and Pieces: `← Previous Big City Life / All Collections / Next → Little Pleasures`
- Little Pleasures: `← Previous Bits and Pieces / All Collections / Next → At the Seaside`
- At the Seaside: `← Previous Little Pleasures / All Collections / Next → Mind Games`
- Mind Games: `← Previous At the Seaside / All Collections / Next → Confessions should be better planned`
- Confessions: `← Previous Mind Games / All Collections / Next → Flora`
- Flora: `← Previous Confessions should be better planned / All Collections`

**Acceptance:** Нет пустых `Next →` или `Previous →` без названия. Порядок совпадает с `/art/`.

---

### P0.3: Сделать фильтры интерактивными
**Проблема:** Фильтры выглядят как текст, не работают при клике.

**Страницы коллекций — фильтры:**
- All / Available / Sold / Private collection

**Available Works — фильтры:**
- All / Paintings / Drawings / Small format / Large format
- Дополнительно: фильтр по коллекциям (All / Big City Life / Little Pleasures / Confessions / Flora)

**Требования:**
- Активный фильтр визуально выделен
- При выборе фильтра список работ обновляется без перезагрузки
- Если результатов нет → показать "No works in this category right now."
- Работает на mobile, доступно с клавиатуры

**Acceptance:** Фильтры — это `<button>` с active state, реально меняют список карточек.

---

### P0.4: Привязать Request price к конкретной работе
**Проблема:** Кнопка `Request price` ведёт на Contact без контекста работы.

**Что сделать:**
- Ссылка с карточки: `/contact/?interest=buy&artwork=Gone&collection=Confessions%20should%20be%20better%20planned`
- На Contact автоматически выбирается "Buying an available artwork"
- Subject заполняется: "Price request: Gone"
- В message добавляется текст: "Hello, I am interested in the artwork "Gone" from the collection "Confessions should be better planned"."

**Acceptance:** Пользователю не нужно вручную писать название картины. В заявке есть название работы.

---

### P0.5: Исправить данные работ
**Проблемы:**
- В Confessions повторяется фраза "Selected works from this collection are available for purchase." — убрать дубль
- У "The tune" статус "Available" попал в строку метаданных вместо даты — добавить год, статус вынести отдельно
- `Acrylic, canvas` и `Acrylic on canvas` — унифицировать в `Acrylic on canvas`
- `Paper, acryl, coal, pencil` → `Paper, acrylic, charcoal, pencil`
- Проверить что Rainy Eiffel и Rainy Eiffel II — разные работы с разными изображениями

**Единый формат карточки:**
```
[image]
Title
Technique · Size · Year
[Status badge]
[Request price] — only if available
```

**Acceptance:** Нет `acryl`, нет статуса в строке даты, нет дублей текста, Request price только для Available.

---

### P0.6: Сделать Contact-форму рабочей
**Проблема:** Форма визуальная, но не отправляет данные.

**Что сделать (Netlify Forms):**
- Добавить `data-netlify="true"` и `netlify-honeypot="bot-field"` к форме
- Добавить hidden field `form-name` = `contact`
- Все поля добавить в `name` атрибуты
- Добавить success state: "Thank you. Your request has been sent."
- Добавить error state: "Something went wrong. Please try again or email directly at alenam.art@gmail.com."
- Добавить privacy note: "Your message will be sent directly to the artist."
- Обработка query params от Request price (P0.4)

**Acceptance:** Тестовая заявка отправляется. Есть validation, success/error states. Поля доступны с клавиатуры.

---

## P1 — ВАЖНЫЕ ЗАДАЧИ

### P1.1: Улучшить Available Works как коммерческую страницу
**Что сделать:**
- Добавить верхний блок: "Original artworks available for purchase. For price, shipping and availability details, send a request for a specific piece."
- Добавить блок доверия: "Original artworks · Direct contact with the artist · Shipping details on request · Replicas and commissions available"
- Карточки: Image / Title / Collection / Technique · Size · Year / [Available] / [Request price]
- Группировка по коллекциям

**Acceptance:** Покупатель за 5 секунд понимает какие работы можно купить. CTA передаёт контекст в Contact.

---

### P1.2: Улучшить Collections (/art/) — бейджи и счётчики
**Что сделать:**
- Заменить "Available works inside" на конкретное число: "11 works · 2 available"
- Формат карточки: [image] / Title / Description / "11 works · 2 available" / [View collection →]
- Если доступных работ нет — не показывать ложный коммерческий намёк
- Сделать всю карточку кликабельной

**Acceptance:** Все 7 коллекций видны. Количество работ совпадает с реальным. Бейджи для доступных работ.

---

### P1.3: Улучшить тон Exhibitions
**Что сделать:**
- Переписать excerpts в профессиональном тоне (убрать "Thanks a million to @sante_praha...")
- Пример: "A presentation of the "Confessions should be better planned" collection took place at SANTE Prague, supported by local partners and attended by the Prague art community."
- Добавить CTA "View event" или "Read more"

**Acceptance:** Список событий звучит как профессиональная хроника, а не пост в соцсетях.

---

### P1.4: Проверить detail pages для работ
**Что сделать:**
- Убедиться что кликабельные названия ведут на полноценные страницы работ
- Минимальная detail-page: Title / Large image / Collection / Technique · Size · Year / Status / [Request price] / [Back to collection]
- Нет пустых страниц и broken links

**Acceptance:** Все ссылки работают, у доступных работ есть Request price на detail-page.

---

### P1.5: Улучшить Story — тон и изображения
**Что сделать:**
- Заменить "Emotional Trauma" на "Pain & Transformation" или "Emotional Transformation"
- Добавить CTA: [View Collections] и [See Exhibitions]
- Добавить изображения с оригинала (из STORY_PLAN.md):
  - Hero: alena-mart-1.avif
  - Grid 2×2: 4.avif, 3.avif, tramvai-alena.avif, photo_5262762490696168254_y-1.avif
  - Collections preview: tramvai-alena.avif, IMG_5841.avif, IMG_5801.avif

**Acceptance:** Story звучит профессионально и эмоционально. Есть изображения. Нет только травмы.

---

### P1.6: Проверить дубли навигации в DOM
**Что сделать:**
- Проверить desktop и mobile viewport
- Убедиться что меню не дублируется визуально
- Скрытое меню должно иметь `aria-hidden="true"`
- Проверить Tab order — меню должно быть одно

**Acceptance:** Пользователь видит одно меню. Tab проходит меню один раз.

---

## P2 — УЛУЧШЕНИЯ

### P2.1: Fullscreen-просмотр работ
- При клике на изображение → fullscreen viewer с данными работы
- Работает на mobile, закрытие по Esc

### P2.2: SEO-метаданные
- Уникальный title и description для каждой страницы
- Open Graph image для главной и коллекций

### P2.3: Улучшить изображения и alt-тексты
- Responsive sizes, lazy loading
- Alt описывает работу: "Gone, acrylic painting by Alena Mart from the Confessions collection"

### P2.4: Empty states и loading states
- "No works in this category right now." для фильтров
- "Sending..." / "Thank you. Your request has been sent." / error для формы

---

## ПОСТРАНИЧНЫЙ ПЛАН

### Главная (/)
- Проверить CTA ведут на правильные страницы
- Проверить mobile hero
- Проверить блок Available Works содержит только реально доступные работы
- Добавить пояснение "цены и доставка уточняются по запросу"

### Collections (/art/)
- 7 коллекций с бейджами доступных работ
- Карточки одинаковой структуры

### Available Works (/art/available/)
- Рабочие фильтры + фильтр по коллекциям
- Request price с контекстом

### Big City Life (/art/big-city-life/)
- Проверить Rainy Eiffel и Rainy Eiffel II — разные работы
- Исправить prev/next

### Bits and Pieces (/art/bits-and-pieces/)
- Исправить prev/next
- Если все private — CTA "Interested in a similar work or replica?"

### Little Pleasures (/art/little-pleasures/)
- Исправить prev/next
- Проверить Little pleasure I доступна

### At the Seaside (/art/at-the-seaside/)
- Исправить prev/next
- Empty state для Available фильтра

### Mind Games (/art/mind-games/)
- Исправить пустой Next
- acryl → acrylic, coal → charcoal

### Confessions (/art/confessions-should-be-better-planned/)
- Убрать повтор фразы
- Исправить The tune (добавить год)
- Исправить prev/next

### Flora (/art/flora/)
- Исправить prev/next
- Проверить Flora I и Flora VIII доступны

### Story (/story/)
- Заменить Emotional Trauma
- Добавить изображения с оригинала
- Добавить CTA

### Exhibitions (/blog/)
- Исправить даты
- Профессиональные excerpts
- Metadata: Date · City · Venue

### Contact (/contact/)
- Рабочая форма (Netlify Forms)
- Query params от Request price
- Success/error states

---

## ПРИОРИТЕТ ВЫПОЛНЕНИЯ

```
1. P0.1 Exhibitions dates
2. P0.2 Previous/Next navigation
3. P0.5 Artwork data cleanup
4. P0.3 Functional filters
5. P0.4 Request price → Contact context
6. P0.6 Working Contact form
---
7. P1.1 Available page improvements
8. P1.2 Collections badges
9. P1.3 Exhibitions tone
10. P1.5 Story tone + images
11. P1.4 Detail pages
---
12. P2.1 Fullscreen viewer
13. P2.2 SEO metadata
14. P2.3 Images + alt
15. P2.4 Empty states
16. P1.6 Navigation duplicate check
```

---

## ФИНАЛЬНЫЙ КРИТЕРИЙ ГОТОВНОСТИ

**Сценарий 1 (покупка):**
Открыть главную → понять кто художница → перейти в Available Works → выбрать работу → нажать Request price → попасть в Contact с контекстом → отправить заявку

**Сценарий 2 (коллекции):**
Открыть Collections → выбрать коллекцию → отфильтровать Available/Sold/Private → запросить работу → перейти к следующей коллекции через Next/Previous
