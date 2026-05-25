# UI/UX-инструкция по сайту Alena Mart

**Проект:** https://alenam-art.netlify.app  
**Формат:** постраничная инструкция для редизайна / доработки UI/UX  
**Тематика:** современное авторское искусство, эмоциональная живопись, личная история, коллекции, выставки, покупка работ / заказ реплик / коллаборации.

---

## 0. Главная UX-цель сайта

Сайт должен работать не как блог или архив картинок, а как **премиальное портфолио художницы**, где пользователь быстро понимает:

1. кто такая Alena Mart;
2. какой у неё художественный мир;
3. какие коллекции можно посмотреть;
4. какие работы доступны для покупки;
5. как заказать реплику, купить работу, пригласить на выставку или написать по сотрудничеству.

Главная формула сайта:

```text
Эмоция → искусство → коллекция → конкретная работа → действие
```

Ключевая проблема текущей версии: сайт уже имеет сильную эмоциональную основу, но UX больше похож на стандартный блог/каталог. Нужно усилить сценарий просмотра, покупки и доверия.

---

## 1. Глобальная структура сайта

### Текущая навигация

```text
ART / MY STORY / BLOG / CONTACT
```

### Рекомендуемая навигация

```text
Art / Available Works / Story / Exhibitions / Contact
```

Или более коротко:

```text
Collections / Available / Story / Events / Contact
```

### Почему нужно изменить

- `ART` — нормальное название, но лучше раскрыть смысл как `Collections`, если сайт строится вокруг серий.
- `MY STORY` можно оставить, но визуально лучше писать `Story` — короче и чище.
- `BLOG` лучше заменить на `Exhibitions` или `Events`, потому что раздел содержит выставки, презентации, аукционы и события. Слово `Blog` снижает профессиональное восприятие.
- Нужно добавить отдельный пункт `Available Works`, потому что покупатель не должен искать доступные работы внутри всех коллекций.

### Глобальный header

**Desktop:**

```text
[Alena Mart]          Art   Available Works   Story   Exhibitions   Contact
```

**Mobile:**

```text
[Alena Mart]                         [menu]
```

В мобильном меню:

```text
Art
Available Works
Story
Exhibitions
Contact
Instagram
```

### Глобальный footer

Сейчас повторяется CTA “If you wish to buy...”. Его нужно оформить аккуратнее.

Рекомендуемый footer:

```text
Alena Mart
Contemporary artist exploring memory, emotion and distorted reality.

[Available Works] [Contact the Artist]

Instagram / Facebook / Email
© 2026 Alena Mart
```

---

## 2. Главная страница

**URL:** https://alenam-art.netlify.app/

### Текущая роль страницы

Главная показывает слоган `ART NEVER COMES FROM HAPPINESS`, блок `MY ART`, несколько работ, коллекции, upcoming events и общий CTA на покупку/реплику.

### Основная UX-проблема

Первый экран эмоциональный, но не объясняет пользователю:

- кто автор;
- что именно можно сделать на сайте;
- где смотреть коллекции;
- какие работы можно купить;
- как связаться.

Слоган сильный, но сам по себе он не заменяет позиционирование.

### Цель новой главной

Главная должна за 3–5 секунд дать ответ:

```text
Это сайт художницы Alena Mart.
Здесь можно посмотреть коллекции, купить доступные работы, заказать реплику или связаться по выставкам/коллаборациям.
```

### Рекомендуемая структура главной

```text
1. Hero
2. Featured works
3. Collections preview
4. Available works preview
5. Story / Artist statement
6. Exhibitions preview
7. Final CTA
```

### Hero-блок

#### Что оставить

- Слоган `ART NEVER COMES FROM HAPPINESS`.
- Драматичную атмосферу.
- Сильное изображение на первом экране.

#### Что изменить критично

Добавить имя, короткое позиционирование и кнопки.

```text
Alena Mart
ART NEVER COMES FROM HAPPINESS

Contemporary artist exploring memory, trauma, tenderness and distorted reality.

[Explore collections] [Available works] [Contact the artist]
```

### Макет hero desktop

```text
┌─────────────────────────────────────────────────────────────┐
│ Alena Mart                       Art Available Story Contact │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ ART NEVER COMES FROM HAPPINESS                              │
│                                                             │
│ Contemporary artist exploring memory, trauma, tenderness    │
│ and distorted reality.                                      │
│                                                             │
│ [Explore collections] [Available works]                     │
│                                                             │
│                         [large artwork / portrait / detail] │
└─────────────────────────────────────────────────────────────┘
```

### Макет hero mobile

```text
┌──────────────────────────────┐
│ Alena Mart              Menu │
├──────────────────────────────┤
│ [large artwork]              │
│                              │
│ ART NEVER COMES              │
│ FROM HAPPINESS               │
│                              │
│ Contemporary artist...       │
│                              │
│ [Explore collections]        │
│ [Available works]            │
└──────────────────────────────┘
```

### Блок `MY ART`

Сейчас блок работает как эмоциональная цитата. Его лучше превратить в короткий artist statement.

#### Рекомендуемый вариант

```text
My Art
Art is the magic glue that is capable of sticking a broken heart back together and filling it with hope and love.

Alena’s work turns emotional tension, memories and fragile moments into expressive visual stories.
```

### Блок `Collections`

Сейчас на главной показаны только несколько коллекций и кнопка `View All`.

#### Что изменить

Показать 3–4 карточки коллекций с более понятной структурой:

```text
[Image]
Big City Life
Cities, memories and emotional landscapes.
[View collection]
```

```text
[Image]
Confessions should be better planned
Raw expression, hidden truths and emotional chaos.
[View collection]
```

```text
[Image]
Flora
Flowers, femininity, fragility and preserved memory.
[View collection]
```

### Блок `Available Works`

Добавить обязательно.

```text
Available Works
Selected artworks currently available for purchase.

[Artwork card] [Artwork card] [Artwork card]
[View all available works]
```

### Блок `Upcoming events`

Сейчас он есть, но выглядит второстепенно. Для художницы события повышают доверие.

Рекомендуемый формат:

```text
Exhibitions & Events
Recent presentations, auctions and exhibitions.

[Date] [City] [Title] [Read more]
```

### Критично для главной

- Добавить CTA в первый экран.
- Добавить `Available Works`.
- Сделать коллекции визуальными карточками.
- Убрать ощущение блогового шаблона.
- На мобильной версии сначала показывать искусство и CTA, потом длинные тексты.

---

## 3. Страница ART / Collections

**URL:** https://alenam-art.netlify.app/art/

### Текущая роль страницы

Страница показывает список коллекций:

- Big City Life
- Bits and Pieces
- Little Pleasures
- At the Seaside
- Mind Games
- Confessions should be better planned
- Flora

У каждой коллекции есть изображение, описание и ссылка `see more`.

### Основная UX-проблема

Страница больше похожа на список постов, а не на каталог художественных коллекций. Визуальная иерархия слабая: все коллекции выглядят почти одинаково, хотя у каждой разная эмоциональная тема.

### Цель страницы

Сделать страницу не просто списком, а **галерейным входом в художественные миры автора**.

### Рекомендуемая структура

```text
1. Page hero
2. Краткое объяснение: что такое коллекции
3. Сетка коллекций
4. CTA к Available Works
5. CTA к Contact
```

### Заголовок страницы

Вместо просто:

```text
ART
```

лучше:

```text
Collections
Each series reveals a different emotional landscape — from city memories to hidden confessions, symbolic sketches and fragile flowers.
```

### Макет desktop

```text
┌──────────────────────────────────────────────────────────┐
│ Collections                                               │
│ Each series reveals a different emotional landscape.      │
├──────────────────────────────────────────────────────────┤
│ [Big City Life]        [Confessions...]      [Flora]      │
│ Image                 Image                 Image         │
│ Short text             Short text            Short text   │
│ [View collection]      [View collection]     [View...]    │
├──────────────────────────────────────────────────────────┤
│ [Bits and Pieces]     [Little Pleasures]    [Mind Games]  │
│ ...                   ...                   ...           │
└──────────────────────────────────────────────────────────┘
```

### Макет mobile

```text
Collections
Short intro

[Big City Life image]
Big City Life
Short description
[View collection]

[Confessions image]
Confessions should be better planned
Short description
[View collection]
```

### Карточка коллекции

Каждая карточка должна иметь:

```text
- изображение;
- название;
- 1–2 строки описания;
- эмоциональный тег;
- количество работ, если возможно;
- наличие доступных работ, если есть;
- кнопку View collection.
```

Пример:

```text
Big City Life
Cities, memory, movement
11 works
[View collection]
```

```text
Confessions should be better planned
Raw expression, masks, hidden emotions
Available works inside
[View collection]
```

### Критично для ART

- Заменить `see more` на `View collection`.
- Переименовать страницу в `Collections` или добавить это слово рядом с ART.
- Добавить CTA `View available works`.
- Дать каждой коллекции разный визуальный характер.
- Не смешивать коллекции и блоговые посты.

---

## 4. Общий шаблон страницы категории / коллекции

**Применяется к:**

- `/art/big-city-life/`
- `/art/bits-and-pieces/`
- `/art/little-pleasures/`
- `/art/at-the-seaside/`
- `/art/mind-games/`
- `/art/confessions-should-be-better-planned/`
- `/art/flora/`

### Текущая проблема

Категории выглядят неоднородно:

- одни страницы показывают только описание и изображения;
- другие содержат список работ с техникой, размером и статусом;
- статус `Available` иногда есть, но визуально не выделен;
- покупка/заказ вынесены в общий CTA внизу, а не рядом с конкретной работой;
- навигация `Prev / Next` выглядит как блоговая.

### Цель шаблона коллекции

Каждая коллекция должна работать как мини-выставка.

Пользователь должен понять:

1. о чём эта серия;
2. какие работы входят в серию;
3. какие работы доступны;
4. как запросить цену / покупку / реплику;
5. как перейти к следующей коллекции.

### Рекомендуемая структура страницы коллекции

```text
1. Collection hero
2. Концепция коллекции
3. Фильтры / статусы
4. Галерея работ
5. Featured artwork / ключевая работа
6. CTA: запросить работу / реплику
7. Навигация между коллекциями
```

### Collection hero

```text
Big City Life
A tribute to cities, memories and emotional landscapes.

[Back to collections] [Available works]
```

Дата публикации не должна быть главным элементом. Для коллекции дата `January 20, 2025` выглядит как дата поста, а не как часть художественного каталога. Её можно убрать из hero или заменить на:

```text
Collection · 2025
```

### Макет страницы коллекции

```text
┌────────────────────────────────────────────────────────────┐
│ ← Back to collections                                      │
│                                                            │
│ Big City Life                                              │
│ A tribute to cities that shaped the artist’s journey.      │
│                                                            │
│ [All] [Available] [Sold] [Private collection]              │
├────────────────────────────────────────────────────────────┤
│ [Artwork image]       [Artwork image]       [Artwork image]│
│ The Tram              Gone                 Apple           │
│ Oil on canvas         Acrylic on canvas     Acrylic        │
│ Private collection    Available             Available      │
│                       [Request price]       [Request price]│
└────────────────────────────────────────────────────────────┘
```

### Карточка работы

Обязательные поля:

```text
Название
Техника
Материал
Размер
Год / месяц
Статус
CTA
```

Пример:

```text
Gone
Acrylic on canvas · 40×60 cm · 2022
Available
[Request price]
```

Для недоступных работ:

```text
The Tram
Oil on canvas · 90×60 cm · 2013
Private collection
[Ask about replica]
```

### Статусы

Сделать бейджи:

```text
Available
Sold
Private collection
Replica possible
```

### Фильтры

Обязательно добавить:

```text
All / Available / Sold / Private collection
```

Если работ немного, фильтры можно оставить только на desktop, а на mobile заменить выпадающим списком.

### Навигация между коллекциями

Сейчас `Prev / Next` выглядит как навигация по постам. Лучше:

```text
Previous collection: Bits and Pieces
Next collection: Flora
```

Или визуальные карточки:

```text
Continue exploring
[Bits and Pieces] [Flora]
```

### Критично для всех категорий

- Убрать блоговую подачу.
- Сделать единый шаблон для всех коллекций.
- Выделить статусы работ.
- Добавить CTA рядом с доступными работами.
- Сделать изображение главным элементом, а не текстовую дату.
- Добавить fullscreen-preview / lightbox для просмотра картин.

---

## 5. Категория Big City Life

**URL:** https://alenam-art.netlify.app/art/big-city-life/

### Смысл коллекции

Коллекция о городах, которые сформировали путь художницы: города, где она жила, гуляла, мечтала или, возможно, никогда не побывает.

### Что оставить

- Тему городов как глав жизни.
- Эмоциональный текст про память, любовь, надежду и отчаяние.
- Крупные изображения работ.

### Что изменить

Сейчас страница выглядит как пост с датой и галереей. Нужно подать её как коллекцию.

### Рекомендуемый hero

```text
Big City Life
Cities as chapters of a life lived fully.

A tribute to the places that shaped Alena’s journey — real, remembered, imagined and loved.
```

### Визуальный стиль

- Больше воздуха.
- Урбанистичный ритм сетки.
- Можно использовать горизонтальные карточки для городских сюжетов.
- Акцент на “city memory / movement / loneliness / love”.

### Особенность UX

Для этой коллекции хорошо работает режим просмотра:

```text
View as journey
```

Порядок работ можно оформить как маршрут:

```text
City → Memory → Emotion → Artwork
```

### CTA

```text
Interested in a city-inspired work?
[Ask about available works]
[Request a replica]
```

---

## 6. Категория Bits and Pieces

**URL:** https://alenam-art.netlify.app/art/bits-and-pieces/

### Смысл коллекции

Коллекция о красоте в деталях: вкусах, запахах, маленьких следах памяти, ощущениях и ностальгии.

### Что оставить

- Идею “beauty exists in everything”.
- Сенсорные описания: ripe fruit, warm light, cool leather.
- Мягкую, интимную атмосферу.

### Что изменить

Страница должна ощущаться как собрание фрагментов памяти, а не обычная галерея.

### Рекомендуемый hero

```text
Bits and Pieces
Small details. Grand impressions. Emotional traces.

A collection about sensory memory, nostalgia and the quiet beauty hidden in ordinary things.
```

### Визуальный стиль

- Более камерная сетка.
- Можно использовать masonry-grid.
- Подписи к работам должны быть короткими и чувственными.

### UX-идея

Добавить теги:

```text
Memory / Taste / Light / Texture / Nostalgia
```

### CTA

```text
Looking for a quiet emotional piece?
[View available works]
```

---

## 7. Категория Little Pleasures

**URL:** https://alenam-art.netlify.app/art/little-pleasures/

### Смысл коллекции

Коллекция о маленьких радостях, которые часто остаются незамеченными: обычные предметы, свет, отражения, мягкая пастельная гармония.

### Что оставить

- Светлое настроение.
- Тему повседневной красоты.
- Мягкость и спокойствие.

### Что изменить

Эту коллекцию важно визуально отделить от более тяжёлых и драматичных серий. Она должна быть “точкой дыхания” на сайте.

### Рекомендуемый hero

```text
Little Pleasures
Everyday objects turned into quiet joy.

A soft pastel collection about light, reflection and the beauty we notice only when we slow down.
```

### Визуальный стиль

- Светлее, мягче, больше пастельного пространства.
- Меньше драматичного красного.
- Больше “air / pause / calm”.

### UX-идея

Добавить короткую фразу перед галереей:

```text
These works are about slowing down and seeing what usually disappears in the rush.
```

### CTA

```text
Bring a quiet pleasure into your space.
[Ask about this collection]
```

---

## 8. Категория At the Seaside

**URL:** https://alenam-art.netlify.app/art/at-the-seaside/

### Смысл коллекции

Коллекция о море, озёрах, океанах, воде, вдохновении, свободе, силе и надежде.

### Что оставить

- Энергию воды.
- Мотив release / peace / hope.
- Морские образы: boats, palm trees, lighthouses, beaches.

### Что изменить

Нужно усилить ощущение пространства и свободы. Галерея не должна быть слишком плотной.

### Рекомендуемый hero

```text
At the Seaside
Water as strength, peace and release.

A collection inspired by lakes, seas, oceans and the feeling of breathing freely again.
```

### Визуальный стиль

- Большие изображения.
- Больше горизонтальных отступов.
- Можно использовать wide cards.
- На mobile — крупные вертикальные карточки без мелких деталей.

### UX-идея

Добавить переключатель настроения:

```text
Peace / Hope / Escape / Freedom
```

Не обязательно как функциональный фильтр — можно как визуальные теги.

### CTA

```text
Interested in a seaside-inspired piece?
[Contact the artist]
```

---

## 9. Категория Mind Games

**URL:** https://alenam-art.netlify.app/art/mind-games/

### Смысл коллекции

Серия скетчей с символами, скрытыми смыслами и загадками. В тексте уже есть важный образ: bold black-and-white compositions with touches of red.

### Что оставить

- Чёрно-белую драму.
- Красные акценты.
- Идею hidden meanings / puzzles.
- Список работ с названиями, техникой и размером.

### Что изменить критично

Сейчас список работ идёт как обычный markdown/bullet-list. Для такой сильной символической серии это слишком слабо.

Нужно превратить список в карточки работ.

### Рекомендуемый hero

```text
Mind Games
Symbols, puzzles and hidden meanings.

A black-and-white sketch series with sharp red accents and stories that reveal themselves only when you look closer.
```

### Карточка работы

```text
Night dweller
Paper, pencil · A3 · July 2021
[View details]
```

```text
Good evening candles
Paper, pencil, gouache · A3 · July 2021
Sold
[Ask about similar work]
```

### UX-идея

Для Mind Games можно добавить интерактивность:

```text
Look closer
```

При наведении/тапе показывать короткую подсказку или символический мотив.

Пример:

```text
[Artwork]
Night dweller
Symbol: night / solitude / hidden self
```

### Визуальный стиль

- Чёрно-белая сетка.
- Красный только для акцентов: статус, hover, CTA.
- Больше контраста.
- Можно использовать тонкие линии, как в sketchbook.

### Критично

- Убрать bullet-list как основной вид работ.
- Добавить статусы и CTA.
- Сделать эту коллекцию самой “интеллектуальной” и интерактивной.

---

## 10. Категория Confessions should be better planned

**URL:** https://alenam-art.netlify.app/art/confessions-should-be-better-planned/

### Смысл коллекции

Серия о сыром, нефильтрованном выражении: скрытые правды, маски, невысказанные слова, сложность коммуникации, желания и эмоции, которые невозможно удержать.

### Что оставить

- Сильное название.
- Тему communication / masks / hidden truths.
- Список работ с размерами, техникой и статусами.
- Наличие работ `Available` — это важно для продаж.

### Что изменить критично

Это, вероятно, самая коммерчески важная коллекция, потому что на странице уже указано много работ со статусом `Available`.

Нужно сделать её главным входом для покупки.

### Рекомендуемый hero

```text
Confessions should be better planned
Raw expression, hidden truths and emotional chaos.

A series about words left unspoken, desires misread and emotions too intense to stay inside.
```

### Верхний CTA

```text
Selected works from this collection are available for purchase.

[View available works] [Ask about the collection]
```

### Карточки доступных работ

```text
Gone
Acrylic on canvas · 40×60 cm · February 2022
Available
[Request price]
```

```text
Disconnect
Acrylic on canvas · 50×70 cm · March 2024
Available
[Request price]
```

```text
What have I done?
Acrylic on canvas · 70×100 cm · January 2025
Available
[Request price]
```

### Фильтр

```text
All / Available / Sold / Not listed
```

### UX-идея

Добавить блок:

```text
Why this collection matters
```

Коротко объяснить связь коллекции с личной историей и благотворительной/социальной темой, если она актуальна для продажи и выставок.

### Визуальный стиль

- Драматичный.
- Больше красного акцента.
- Контрастные карточки.
- Можно использовать крупные названия работ.

### Критично

- Сделать эту страницу сильной landing page для покупки.
- Все `Available` превратить в видимые бейджи.
- Добавить `Request price` рядом с каждой доступной работой.
- Добавить форму/переход на Contact с предзаполненной темой.

---

## 11. Категория Flora

**URL:** https://alenam-art.netlify.app/art/flora/

### Смысл коллекции

Коллекция о девушках и цветах, хрупкости, красоте, памяти, радости и печали. Цветы увядают, но на холсте сохраняются навсегда.

### Что оставить

- Женственность.
- Хрупкость.
- Тему fleeting beauty / eternal life on canvas.
- Эмоциональную связь цветов и памяти.

### Что изменить

Сейчас страница выглядит очень коротко: описание и галерея. Нужно добавить больше художественного контекста.

### Рекомендуемый hero

```text
Flora
Fleeting beauty preserved forever.

A collection about flowers, femininity, sorrow, joy and the delicate fragrance of memory.
```

### Визуальный стиль

- Мягкий, но не декоративный.
- Не превращать в “милую цветочную” страницу — сохранить драму автора.
- Использовать красный/тёмный акцент аккуратно.

### UX-идея

Добавить подзаголовки для работ:

```text
Joy / Sorrow / Memory / Fragility
```

### CTA

```text
Interested in Flora works or a floral commission?
[Contact the artist]
```

---

## 12. Новая страница Available Works

**URL:** рекомендуется добавить `/available/` или `/art/available/`

### Почему нужна

Сейчас доступные работы спрятаны внутри коллекций. Покупатель должен вручную читать каждую страницу. Это плохо для UX и продаж.

### Цель страницы

Показать только те работы, которые можно купить сейчас.

### Структура

```text
Available Works
Original artworks currently available for purchase.

[Filter by collection]
[Filter by size]
[Filter by technique]

[Artwork card]
[Artwork card]
[Artwork card]
```

### Карточка

```text
Image
Title
Collection
Technique · Size · Year
Available
[Request price]
```

### Форма запроса

При клике `Request price` пользователь попадает на Contact, где тема уже понятна:

```text
Subject: Inquiry about “Gone”
Message: I’m interested in the artwork “Gone”. Please send me price, availability and shipping details.
```

### Критично

Эту страницу нужно добавить в навигацию.

---

## 13. Страница Story

**URL:** https://alenam-art.netlify.app/story/

### Текущая роль страницы

Страница рассказывает личную историю художницы: Восточная Европа, художественная семья, сложное детство, отец-художник и архитектор, травматический опыт, первая коммерческая успешность в Германии, Нью-Йорк, Tram, связь с людьми с особыми потребностями и “crooked reality / sharp emotions”.

### Что хорошо

История сильная, честная и эмоциональная. Она объясняет, почему искусство Alena Mart связано с болью, памятью, надеждой и искажённой реальностью.

### Основная UX-проблема

История подана как длинный биографический текст. Для коллекционеров, галерей и новых посетителей лучше дать структуру.

### Рекомендуемая структура

```text
1. Artist portrait / hero
2. Artist statement
3. Biography
4. Key turning points
5. Themes in the art
6. Social / emotional mission
7. CTA
```

### Новый верх страницы

```text
My Story
Alena Martsyanava is an indie artist from Eastern Europe whose work transforms trauma, memory and emotional tension into visual stories.
```

### Artist statement

```text
Artist Statement
I create from the places where words fail — from memory, pain, tenderness, distorted reality and the fragile hope of healing.
```

### Биография в блоках

```text
Artistic roots
Born into an artistic family, Alena grew up surrounded by beauty and emotional tension.

Turning point
A visit to New York in 2012 pushed her to take art more seriously.

The Tram
One of her most successful works became a symbol of personal tragedy transformed into art.

Current themes
Broken hearts, special needs, communication, hidden emotions and crooked reality.
```

### Что изменить критично

- Убрать повтор CTA внизу: сейчас он дублируется.
- Разделить длинный текст на смысловые блоки.
- Добавить quote / artist statement.
- Добавить блок “Selected collections connected to this story”.

### Макет Story

```text
┌──────────────────────────────────────────────┐
│ [Portrait / artwork detail]                  │
│ My Story                                     │
│ Art as a way to transform pain into hope.    │
├──────────────────────────────────────────────┤
│ Artist Statement                             │
│ Short emotional statement                    │
├──────────────────────────────────────────────┤
│ Timeline                                     │
│ Childhood → Germany → New York → The Tram    │
├──────────────────────────────────────────────┤
│ Themes                                       │
│ Memory / Trauma / Tenderness / Distortion    │
├──────────────────────────────────────────────┤
│ [Explore collections] [Contact the artist]   │
└──────────────────────────────────────────────┘
```

### Важно по этике и тону

Травматичная история должна быть подана уважительно и профессионально. Не делать её “сенсацией”. Она должна объяснять художественный язык, а не превращаться в шок-контент.

---

## 14. Страница Blog / Exhibitions

**URL:** https://alenam-art.netlify.app/blog/

### Текущая роль страницы

Раздел называется `Blog`, но внутри есть выставки, презентации, аукционы, коллекции и события.

### Основная UX-проблема

Смешаны разные типы контента:

- события;
- выставки;
- аукционы;
- публикации о коллекциях;
- обычные блоговые записи.

Из-за этого раздел выглядит как стандартный список постов, а не как профессиональная хроника художницы.

### Рекомендуемое название

Лучше заменить `Blog` на:

```text
Exhibitions & Events
```

или:

```text
Journal
```

Если оставить `Blog`, добавить фильтры.

### Рекомендуемая структура страницы

```text
Exhibitions & Events
Exhibition reviews, presentations, auctions and behind-the-scenes stories.

[All] [Exhibitions] [Auctions] [Collections] [Behind the scenes]

Cards grid
```

### Карточка события

```text
Image
June 1, 2025 · Prague
Amazing evening, amazing place, amazing people!
Presentation / Exhibition
[Read more]
```

### Карточка аукциона

```text
Image
January 3, 2025 · Wroclaw, Poland
Auction in Wroclaw, Poland
Auction · Sold work
[Read more]
```

### Карточка коллекции

Если в этом разделе остаются страницы коллекций, нужно визуально отличить их:

```text
Collection
Big City Life
[View collection]
```

Но лучше не дублировать коллекции в Blog. Коллекции должны жить в `Art / Collections`, а Blog/Events — только для событий и новостей.

### Критично

- Переименовать `Blog`.
- Добавить фильтры по типам записей.
- Не смешивать коллекции и события без визуального различия.
- Добавить город/место/тип события на карточки.
- Показать события как социальное доказательство профессиональности.

---

## 15. Шаблон страницы события / blog post

**Примеры:**

- `/blog/amazing-evening-amazing-place-amazing-people/`
- `/blog/a-presentation-of-the-art-collection-confessions-should-be-better-planned-by-alena-martsyanava/`
- `/blog/taking-part-in-contro-la-violenza-sulle-donne-expo/`
- `/blog/auction-in-wroclaw-poland/`

### Текущая проблема

Страница события выглядит как короткий пост. Для выставок и аукционов нужно больше структуры.

### Рекомендуемый шаблон

```text
Event / Exhibition / Auction
Title
Date · City · Venue

Hero image

Intro paragraph
Details
Related artworks
Gallery
CTA
Back to Exhibitions
```

### Пример для презентации коллекции

```text
A presentation of “Confessions Should Be Better Planned”
May 23, 2025 · Prague · SANTE

The concept: buy art and help people.

Details
Date: 23 May 2025
Place: SANTE, Puškinovo náměstí 518/8, Prague
Time: 18:00
Entrance: Free

[View collection]
[Contact about available works]
```

### Пример для аукциона

```text
Auction in Wroclaw, Poland
Auction · Wroclaw · January 2025

Alena’s artwork in grattage technique was sold to a local art admirer.

[View related work]
[See more exhibitions]
```

### Критично

- Добавить тип события.
- Добавить место и город в отдельные поля.
- Если есть связанная коллекция — давать ссылку на неё.
- Если работа была продана — использовать это как trust signal.

---

## 16. Страница Contact

**URL:** https://alenam-art.netlify.app/contact/

### Текущая роль страницы

Страница предлагает покупку работ, заказ commission и collaboration. Есть email, соцсети и форма с полями:

```text
Your name
Your email
Subject
Your message
Send Message
```

### Что хорошо

Контактная страница уже говорит о покупке, commission и collaboration. Это правильный сценарий.

### Основная UX-проблема

Форма слишком общая. Она не помогает пользователю выбрать тип запроса.

### Рекомендуемая структура

```text
Get in Touch
For available works, commissions, replicas, exhibitions or collaborations.

I want to:
[ ] Buy an available work
[ ] Ask about a replica
[ ] Commission a piece
[ ] Invite Alena to an exhibition
[ ] Collaborate
[ ] General question

Name
Email
Artwork / Collection name
Message
[Send request]
```

### Макет Contact

```text
┌─────────────────────────────────────────────┐
│ Get in Touch                                │
│ Interested in purchasing artwork, ordering  │
│ a replica, commissioning a piece or         │
│ collaborating?                              │
├─────────────────────────────────────────────┤
│ I want to:                                  │
│ ( ) Buy an available work                   │
│ ( ) Ask about a replica                     │
│ ( ) Commission a piece                      │
│ ( ) Exhibition / collaboration              │
├─────────────────────────────────────────────┤
│ Name                                        │
│ Email                                       │
│ Artwork / Collection                        │
│ Message                                     │
│ [Send request]                              │
├─────────────────────────────────────────────┤
│ Email: alenam.art@gmail.com                 │
│ Instagram / Facebook / LinkedIn             │
└─────────────────────────────────────────────┘
```

### Что изменить критично

- Заменить `Send Message` на `Send request`.
- Добавить выбор типа запроса.
- Добавить поле `Artwork / Collection`.
- Если пользователь пришёл с конкретной работы, автоматически подставлять название в subject/message.
- Убрать повтор CTA внизу или заменить на аккуратный финальный блок.

### Финальный CTA

```text
Not sure which artwork to choose?
Write a short message — Alena will help you find the right piece or discuss a custom request.
```

---

## 17. Визуальная система

### Общий стиль

Сайт должен выглядеть как:

```text
private gallery + emotional artist portfolio + modern exhibition archive
```

Не как:

```text
standard WordPress blog
```

### Цвета

Подходит палитра:

```text
Black / Off-white / Deep red / Warm gray
```

Рекомендации:

- красный использовать только как акцент;
- не перегружать декоративными цветами;
- фон может быть не чисто белым, а молочный/тёплый серый;
- для Mind Games можно усилить чёрно-белый контраст.

### Типографика

Рекомендуется:

- крупные заголовки;
- короткие подзаголовки;
- не делать длинные абзацы шире 650–720 px;
- использовать разный размер для названий коллекций и описаний;
- сохранить артистичность, но не жертвовать читаемостью.

### Изображения

- Делать изображения главным элементом интерфейса.
- Добавить fullscreen/lightbox.
- На карточках использовать одинаковые пропорции или аккуратный masonry layout.
- Добавить hover/tap состояние.
- Подписи должны быть видимыми без открытия модального окна.

### Анимации

Использовать осторожно:

- плавное появление изображений;
- hover на карточках;
- мягкий переход в lightbox;
- без агрессивных эффектов.

Арт не должен конкурировать с UI-анимацией.

---

## 18. Mobile-first требования

### Главное правило

Большая часть пользователей будет приходить с телефона, особенно из Instagram, QR-кодов, соцсетей и событий.

### Что проверить

- Первый экран не должен быть пустым или только декоративным.
- CTA должны быть видны быстро.
- Галерея должна листаться вертикально.
- Карточки работ должны быть читаемыми.
- Размер кнопок минимум 44 px по высоте.
- Текст не должен быть мелким.
- Изображения должны грузиться быстро.

### Mobile-паттерн карточки работы

```text
[image]
Title
Technique · Size · Year
Available
[Request price]
```

### Mobile-паттерн коллекции

```text
Collection title
Short description
[All / Available]

[Artwork]
[Artwork]
[Artwork]
```

---

## 19. SEO и структура контента

### Title страниц

Рекомендуемые title:

```text
Alena Mart — Contemporary Artist
Collections — Alena Mart
Available Works — Alena Mart
Big City Life — Alena Mart
Confessions Should Be Better Planned — Alena Mart
Exhibitions & Events — Alena Mart
Contact — Alena Mart
```

### Meta description

Пример для главной:

```text
Alena Mart is a contemporary artist exploring memory, trauma, tenderness and distorted reality through emotionally charged paintings and collections.
```

### Alt-тексты

Не использовать только:

```text
Alena artwork
```

Лучше:

```text
The Tram, oil on canvas by Alena Mart
```

или:

```text
Artwork from Confessions should be better planned collection by Alena Mart
```

### URL

Текущие URL в целом нормальные. Важно добавить:

```text
/available/
/exhibitions/
```

Если `blog` оставить технически, можно в UI показывать `Exhibitions`.

---

## 20. Приоритеты внедрения

### Этап 1 — критично

```text
1. Добавить CTA в hero главной.
2. Добавить страницу Available Works.
3. Переименовать Blog в Exhibitions / Events.
4. Сделать единый шаблон карточки работы.
5. Выделить статусы Available / Sold / Private collection.
6. Добавить Request price рядом с доступными работами.
7. Исправить Contact-форму под реальные сценарии.
```

### Этап 2 — важно

```text
1. Перестроить ART как страницу коллекций.
2. Сделать единый шаблон всех коллекций.
3. Разделить Story на блоки.
4. Добавить фильтры в коллекциях.
5. Добавить lightbox для просмотра работ.
6. Добавить карточки событий с городом, датой и типом события.
```

### Этап 3 — улучшения

```text
1. Добавить micro-interactions.
2. Добавить теги к коллекциям.
3. Добавить related works.
4. Добавить timeline на Story.
5. Добавить SEO-оптимизацию для каждой коллекции.
6. Добавить schema.org для Artwork/Event, если планируется SEO-продвижение.
```

---

## 21. Короткий чеклист для дизайнера

```text
[ ] Главная выглядит как сайт художницы, а не блог.
[ ] Первый экран объясняет кто автор и что можно сделать.
[ ] Есть CTA Explore collections / Available works / Contact.
[ ] ART оформлен как Collections.
[ ] У каждой коллекции есть единый шаблон.
[ ] Работы имеют карточки с названием, техникой, размером, датой и статусом.
[ ] Available-работы видны сразу.
[ ] Есть отдельная страница Available Works.
[ ] Blog переименован в Exhibitions / Events.
[ ] Story структурирована и не выглядит как длинная простыня текста.
[ ] Contact-форма учитывает покупку, реплику, commission, выставку, collaboration.
[ ] Мобильная версия удобнее desktop, а не просто его уменьшенная копия.
[ ] Изображения открываются в fullscreen/lightbox.
[ ] Footer не дублирует CTA некрасиво.
```

---

## 22. Короткий чеклист для разработчика

```text
[ ] Создать компонент ArtworkCard.
[ ] Создать компонент CollectionCard.
[ ] Создать компонент EventCard.
[ ] Создать общий CollectionPageTemplate.
[ ] Вынести данные работ в структуру: title, collection, technique, material, size, date, status, image, CTA.
[ ] Добавить status badge.
[ ] Добавить фильтр Available / Sold / Private collection.
[ ] Добавить страницу /available/.
[ ] Настроить переход Request price → Contact с параметром artwork.
[ ] Добавить lightbox/gallery viewer.
[ ] Проверить mobile breakpoints.
[ ] Добавить alt-тексты изображений.
[ ] Обновить meta title/description.
```

---

## 23. Итоговая концепция редизайна

Сайт должен стать не просто местом, где лежат работы, а **эмоциональным маршрутом по миру художницы**.

Нужный эффект:

```text
Я попал в личный, драматичный и профессионально оформленный художественный мир.
Я понимаю, какие коллекции существуют.
Я вижу, какие работы доступны.
Я легко могу написать по покупке, реплике, выставке или сотрудничеству.
```

Главные изменения:

```text
1. Больше структуры.
2. Меньше блоговой логики.
3. Больше галерейности.
4. Видимые статусы работ.
5. Отдельный путь к покупке.
6. Сильнее Story, но профессиональнее поданная.
7. Mobile-first просмотр искусства.
```

---

## Источники / проверенные страницы

- https://alenam-art.netlify.app/
- https://alenam-art.netlify.app/art/
- https://alenam-art.netlify.app/art/big-city-life/
- https://alenam-art.netlify.app/art/bits-and-pieces/
- https://alenam-art.netlify.app/art/little-pleasures/
- https://alenam-art.netlify.app/art/at-the-seaside/
- https://alenam-art.netlify.app/art/mind-games/
- https://alenam-art.netlify.app/art/confessions-should-be-better-planned/
- https://alenam-art.netlify.app/art/flora/
- https://alenam-art.netlify.app/story/
- https://alenam-art.netlify.app/blog/
- https://alenam-art.netlify.app/contact/
