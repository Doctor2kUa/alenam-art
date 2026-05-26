# План изменений для AI-агента: новая версия сайта Alena Mart

Аудируемый сайт:

```text
https://alenam-art-0u7i5kpw.netlify.app
```

Дата аудита: 2026-05-26

---

## Роль AI-агента

Ты — AI-агент, который должен доработать новую версию сайта художницы Alena Mart.

Твоя задача — не начинать редизайн заново, а **аккуратно довести текущую версию до профессионального состояния**: исправить ошибки в данных, навигации, фильтрах, событиях, форме контакта и коммерческом сценарии.

Сайт должен оставаться атмосферным, драматичным и художественным. Не превращай его в стерильный SaaS-сайт или обычный интернет-магазин.

---

## Главный вывод по новой версии

Новая версия стала заметно лучше предыдущей:

- меню приведено к структуре `Collections / Available / Story / Exhibitions / Contact`;
- на главной появился сильный hero-блок с позиционированием и CTA;
- появилась отдельная страница `Available Works`;
- страница `Story` стала профессиональнее и больше похожа на artist statement + biography;
- `Contact` уже содержит сценарии обращения: покупка, реплика, комиссия, выставка, сотрудничество.

Но теперь главные проблемы не в общей структуре, а в **качестве реализации**:

1. некорректные даты и метаданные событий;
2. сломанная или нелогичная навигация между коллекциями;
3. фильтры выглядят как текст и могут быть нерабочими;
4. кнопка `Request price` не передаёт контекст конкретной работы;
5. в данных работ всё ещё есть ошибки и непоследовательность;
6. форма контакта должна быть рабочей, доступной и привязанной к сценарию покупки;
7. визуальные и UX-детали пока создают ощущение черновика.

---

## Основные URL для проверки

```text
https://alenam-art-0u7i5kpw.netlify.app/
https://alenam-art-0u7i5kpw.netlify.app/art/
https://alenam-art-0u7i5kpw.netlify.app/art/available/
https://alenam-art-0u7i5kpw.netlify.app/art/big-city-life/
https://alenam-art-0u7i5kpw.netlify.app/art/bits-and-pieces/
https://alenam-art-0u7i5kpw.netlify.app/art/little-pleasures/
https://alenam-art-0u7i5kpw.netlify.app/art/at-the-seaside/
https://alenam-art-0u7i5kpw.netlify.app/art/mind-games/
https://alenam-art-0u7i5kpw.netlify.app/art/confessions-should-be-better-planned/
https://alenam-art-0u7i5kpw.netlify.app/art/flora/
https://alenam-art-0u7i5kpw.netlify.app/story/
https://alenam-art-0u7i5kpw.netlify.app/blog/
https://alenam-art-0u7i5kpw.netlify.app/contact/
```

---

# Не откатывать уже сделанные улучшения

Перед изменениями зафиксируй, что уже работает и не должно быть сломано.

## Оставить

```text
Collections / Available / Story / Exhibitions / Contact
```

## Оставить hero-логику главной

```text
Alena Mart
ART NEVER COMES FROM HAPPINESS
Contemporary artist exploring memory, trauma, tenderness and distorted reality.
[View Collections] [Available Works] [Contact the Artist]
```

## Оставить отдельную страницу Available Works

Страница `/art/available/` нужна обязательно. Не удалять.

## Оставить структуру Story

Текущая структура `Artist Statement → Artistic Themes → Biography → Exhibitions & Recognition` лучше прежней. Её можно редактировать, но не возвращать к формату длинной личной исповеди в начале страницы.

## Оставить Contact-сценарии

На Contact уже есть правильная идея поля:

```text
I am interested in:
Buying an available artwork
Ordering a replica
Commissioning a new piece
Exhibition / collaboration
General question
```

Эту идею нужно довести до рабочего состояния, а не удалять.

---

# P0 — критические задачи

Эти задачи нужно выполнить первыми. Они напрямую влияют на доверие к сайту и готовность человека купить работу или написать художнице.

---

## P0.1. Исправить даты и метаданные в Exhibitions & Events

### Проблема

На странице `/blog/` события выглядят профессиональнее, чем раньше, но есть критичная ошибка: у старых выставок в карточках указаны даты вроде `December 2024` или `November 2024`, хотя в описаниях говорится о событиях 2019, 2018, 2014 и 2013 годов.

Примеры проблем:

```text
December 2024 · Minsk · Beetlejuice cafe
Описание: expo took place ... in December 2019
```

```text
December 2024 · Minsk
Описание: ... April 2018
```

```text
November 2024 · Minsk
Описание: ... autumn 2014
```

```text
November 2024 · Minsk
Описание: First Expo happened back in 2013
```

Это выглядит как ошибка миграции из блога: вероятно, в карточку попала дата публикации поста, а не дата события.

### Что сделать

Разделить:

```text
Event date — когда событие произошло
Published date — когда пост был опубликован, если это нужно
```

Для карточек выставок использовать именно дату события.

### Рекомендуемый формат карточки события

```text
May 2025 · Prague · SANTE
A presentation of the art collection "Confessions Should Be Better Planned"
Short professional excerpt...
[View event]
```

Для старых событий:

```text
April 2018 · Minsk
The "35" Expo
Anniversary exhibition featuring 35 artworks with live music by Stary Olsa.
[View event]
```

### Требования

- Не показывать дату публикации как дату события.
- Если точная дата неизвестна, использовать формат:

```text
2014 · Minsk
```

или

```text
Autumn 2014 · Minsk
```

- Если событие было опубликовано в 2024, но произошло в 2013, не ставить `2024` в основной metadata-line.
- В карточке события всегда должны быть:
  - дата события;
  - город;
  - venue, если известен;
  - название события;
  - короткое профессиональное описание;
  - CTA `View event` или `Read more`.

### Acceptance criteria

- На странице `/blog/` нет противоречий между датой в карточке и датой в описании.
- Все исторические события показывают реальные годы: 2013, 2014, 2018, 2019, 2025 и т.д.
- `December 2024` и `November 2024` не используются для событий, которые реально происходили в 2013–2019 годах.
- События читаются как профессиональная exhibition timeline, а не как список постов.

---

## P0.2. Исправить навигацию Previous / Next между коллекциями

### Проблема

Навигация между коллекциями сейчас местами нелогичная или сломанная.

Примеры:

```text
Big City Life:
← Previous Bits and Pieces / Next → Flora
```

```text
Bits and Pieces:
← Previous Little Pleasures / Next → Big City Life
```

```text
Mind Games:
← Previous At the Seaside / Next →
```

```text
Confessions should be better planned:
All Collections / Next → Mind Games
```

```text
Flora:
← Previous Big City Life / All Collections
```

Проблема: порядок коллекций не соответствует порядку на странице `/art/`, а у `Mind Games` `Next →` отображается без названия.

### Что сделать

Сделать единый порядок коллекций и использовать его везде.

Рекомендуемый порядок:

```text
Big City Life
Bits and Pieces
Little Pleasures
At the Seaside
Mind Games
Confessions should be better planned
Flora
```

### Правильная логика

```text
Big City Life:
All Collections / Next → Bits and Pieces
```

```text
Bits and Pieces:
← Previous Big City Life / All Collections / Next → Little Pleasures
```

```text
Little Pleasures:
← Previous Bits and Pieces / All Collections / Next → At the Seaside
```

```text
At the Seaside:
← Previous Little Pleasures / All Collections / Next → Mind Games
```

```text
Mind Games:
← Previous At the Seaside / All Collections / Next → Confessions should be better planned
```

```text
Confessions should be better planned:
← Previous Mind Games / All Collections / Next → Flora
```

```text
Flora:
← Previous Confessions should be better planned / All Collections
```

### Acceptance criteria

- Нет пустого `Next →` без названия.
- Нет пустого `Previous →` без названия.
- Порядок навигации совпадает с порядком карточек на `/art/`.
- На первой коллекции нет некорректного `Previous`.
- На последней коллекции нет некорректного `Next`.
- `All Collections` всегда ведёт на `/art/`.

---

## P0.3. Сделать фильтры настоящими интерактивными элементами

### Проблема

На страницах коллекций и Available Works фильтры выглядят как набор слов:

```text
All Available Sold Private collection
```

```text
All Paintings Drawings Small format Large format
```

Если они не являются интерактивными кнопками, это выглядит как незавершённый UI.

### Что сделать

Сделать фильтры реальными кнопками, которые фильтруют карточки на странице без перезагрузки или через query params.

### Требования для страниц коллекций

Фильтры:

```text
All
Available
Sold
Private collection
```

### Требования для Available Works

Фильтры:

```text
All
Paintings
Drawings
Small format
Large format
Big City Life
Little Pleasures
Confessions
Flora
```

Не обязательно показывать все фильтры сразу, если дизайн перегружается. Можно сделать 2 строки:

```text
Type: All / Paintings / Drawings
Format: All / Small / Large
Collection: All / Big City Life / Little Pleasures / Confessions / Flora
```

### Поведение

- Активный фильтр визуально выделен.
- При выборе фильтра список работ обновляется.
- Если результатов нет, показывать мягкое сообщение:

```text
No works in this category right now.
```

- Фильтры должны работать на mobile.
- Фильтры должны быть доступны с клавиатуры.

### Acceptance criteria

- Фильтры являются `<button>` или корректными ссылками, а не обычным текстом.
- Есть состояние active.
- Фильтры реально меняют список карточек.
- Нет ситуации, где пользователь нажимает на фильтр, а ничего не происходит.

---

## P0.4. Привязать `Request price` к конкретной работе

### Проблема

Сейчас кнопки `Request price` ведут на Contact, но не видно, что запрос связан с конкретной работой. Пользователь нажимает `Request price` у `Gone`, `Apple` или `Flora I`, а форма контакта остаётся общей.

Это снижает конверсию, потому что человеку нужно вручную писать название работы.

### Что сделать

Кнопка `Request price` должна передавать контекст работы в форму Contact.

### Вариант A — через query params

Ссылка с карточки:

```text
/contact/?interest=buy&artwork=Gone&collection=Confessions%20should%20be%20better%20planned
```

На странице Contact автоматически:

- выбрать `Buying an available artwork`;
- заполнить subject:

```text
Price request: Gone
```

- добавить в message placeholder или prefilled text:

```text
Hello, I am interested in the artwork "Gone" from the collection "Confessions should be better planned".
Please send me price and availability details.
```

### Вариант B — отдельная inquire state/modal

Если используется модальное окно, оно должно содержать:

```text
Artwork: Gone
Collection: Confessions should be better planned
[Name]
[Email]
[Message]
[Send request]
```

### Acceptance criteria

- При клике на `Request price` у конкретной работы пользователь попадает в форму с контекстом этой работы.
- Пользователю не нужно вручную копировать название картины.
- Subject или hidden field содержит название работы.
- В отправленном сообщении художница понимает, о какой работе речь.

---

## P0.5. Исправить данные работ и единый формат карточек

### Проблема

Часть данных уже исправлена, но ошибки всё ещё есть.

Текущие проблемы:

- в `Confessions should be better planned` текст `Selected works from this collection are available for purchase.` повторяется дважды;
- у работы `The tune` статус `Available` попал в строку метаданных вместо даты:

```text
Acrylic on canvas · 50×70 cm · Available
```

- у доступных работ статус и CTA иногда идут одной строкой:

```text
Available Request price
```

- `Acrylic, canvas` и `Acrylic on canvas` используются параллельно;
- `Paper, acryl, coal, pencil` лучше привести к корректному английскому: `Paper, acrylic, charcoal, pencil`;
- нужно проверить, являются ли `Rainy Eiffel` и `Rainy Eiffel II` двумя разными работами, а не дублем.

### Что сделать

Создать единый data schema для всех работ.

### Рекомендуемая структура данных

```ts
type ArtworkStatus = 'available' | 'sold' | 'private_collection';

type Artwork = {
  title: string;
  slug: string;
  collection: string;
  technique: string;
  size: string;
  date: string;
  year: number;
  status: ArtworkStatus;
  image: string;
  alt: string;
};
```

### Единый формат отображения карточки

```text
[image]
Title
Technique · Size · Date/Year
[Status badge]
[Request price] — only if available
```

### Правила

- `Available`, `Sold`, `Private collection` всегда отдельный badge.
- Дата/год не должны смешиваться со статусом.
- Кнопка `Request price` показывается только для `Available`.
- Для `Sold` и `Private collection` кнопку не показывать.
- В Available Works все карточки должны иметь ссылку на коллекцию.
- На странице коллекции все карточки должны иметь одинаковую визуальную структуру.

### Acceptance criteria

- У `The tune` есть корректная дата или год; статус вынесен отдельно.
- В `Confessions` нет повторяющейся фразы про selected works.
- Нет техники `acryl`; использовать `acrylic`.
- Нет смешения `Acrylic, canvas` и `Acrylic on canvas` без причины.
- `Request price` не появляется у sold/private works.

---

## P0.6. Проверить, что Contact-форма реально работает

### Проблема

Страница Contact выглядит лучше, но нужно убедиться, что форма не просто визуальная. На Netlify форма должна быть правильно настроена, иначе заявки не будут приходить.

### Что сделать

Если сайт на Netlify, настроить форму через Netlify Forms или другой рабочий обработчик.

### Минимальная структура для Netlify Forms

```html
<form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="contact" />
  <p hidden>
    <label>Don’t fill this out: <input name="bot-field" /></label>
  </p>

  <label>Name</label>
  <input name="name" required />

  <label>Email</label>
  <input name="email" type="email" required />

  <fieldset>
    <legend>I am interested in:</legend>
    ...
  </fieldset>

  <label>Subject</label>
  <input name="subject" />

  <label>Message</label>
  <textarea name="message" required></textarea>

  <button type="submit">Send request</button>
</form>
```

### Требования

- `Name`, `Email`, `Message` обязательны.
- `Email` должен валидироваться как email.
- `I am interested in` должен быть radio/select/checkbox, а не просто текстом.
- После отправки должен быть success-state:

```text
Thank you. Your request has been sent.
```

- При ошибке должен быть error-state:

```text
Something went wrong. Please try again or email directly at alenam.art@gmail.com.
```

### Acceptance criteria

- Тестовая заявка реально отправляется/сохраняется.
- В заявке есть выбранный интерес.
- Если пользователь пришёл с `Request price`, в заявке есть название работы.
- Поля доступны с клавиатуры.
- У полей есть label, не только placeholder.

---

# P1 — важные задачи

Эти задачи не блокируют запуск, но сильно влияют на профессиональное восприятие сайта.

---

## P1.1. Улучшить страницу Available Works как коммерческую страницу

### Проблема

Страница `/art/available/` уже есть, но пока это просто список доступных работ. Она должна работать как основной коммерческий экран сайта.

### Что сделать

Добавить верхний поясняющий блок:

```text
Available Works
Original artworks available for purchase. For price, shipping and availability details, send a request for a specific piece.
```

Добавить компактный блок доверия:

```text
Original artworks · Direct contact with the artist · Shipping details on request · Replicas and commissions available
```

### Карточки на Available

Каждая карточка должна содержать:

```text
Image
Title
Collection
Technique · Size · Year
[Available]
[Request price]
```

### Дополнительно

- Добавить сортировку или группировку по коллекциям.
- Дать возможность быстро перейти в коллекцию работы.
- Не перегружать страницу длинными текстами.

### Acceptance criteria

- Покупатель за 5 секунд понимает, какие работы можно купить.
- У каждой доступной работы есть CTA.
- CTA передаёт контекст в Contact.
- Страница не выглядит как обычная галерея — она выглядит как curated sales page.

---

## P1.2. Довести Collections до уровня профессионального каталога

### Проблема

Страница `/art/` стала лучше: есть коллекции, описания, количество работ. Но информация `Available works inside` пока выглядит как простая текстовая приписка и не всегда достаточно заметна.

### Что сделать

В карточке коллекции использовать бейджи:

```text
16 works
Available works inside
```

или:

```text
16 works · 7 available
```

Лучше показывать конкретное количество доступных работ, если данные позволяют.

### Рекомендуемый формат карточки коллекции

```text
[image]
Big City Life
Cities, memories and emotional landscapes.
11 works · 2 available
[View collection →]
```

### Acceptance criteria

- Каждая коллекция имеет изображение, название, описание, количество работ.
- Если внутри есть доступные работы, это видно как badge.
- Если доступных работ нет, не показывать ложный коммерческий намёк.
- Все карточки выглядят одинаково по структуре.

---

## P1.3. Улучшить текст и тон Exhibitions

### Проблема

Некоторые описания на `/blog/` звучат слишком как пост в соцсетях, а не как профессиональная exhibition timeline.

Пример:

```text
Thanks a million to @sante_praha...
```

Для личного поста это нормально, но в списке профессиональных событий лучше использовать более спокойный тон.

### Что сделать

На странице списка событий использовать профессиональные excerpts. Внутри отдельной страницы события можно оставить более личный текст.

### Пример

Вместо:

```text
Thanks a million to @sante_praha for hosting...
```

Лучше:

```text
A presentation of the "Confessions should be better planned" collection took place at SANTE Prague, supported by local partners and attended by the Prague art community.
```

### Acceptance criteria

- Список событий звучит как профессиональная хроника.
- Личные благодарности можно оставить внутри detail-page, но не как главный excerpt.
- Названия событий выглядят аккуратно и не слишком случайно.

---

## P1.4. Проверить detail pages для работ и событий

### Проблема

Карточки работ имеют ссылки на названия, но нужно проверить, есть ли полноценные detail pages. Если их нет, пользователь может попасть в пустую/неполную страницу или просто открыть изображение.

### Что сделать

Для каждой работы либо:

1. сделать полноценную страницу работы;
2. либо не делать название кликабельным, если detail-page не готова;
3. либо открывать fullscreen image viewer с данными работы.

### Минимальная detail-page работы

```text
Title
Large image
Collection
Technique · Size · Date/Year
Status
Description, if available
[Request price] — if available
[Back to collection]
```

### Acceptance criteria

- Кликабельные названия ведут на осмысленные страницы.
- Нет пустых страниц.
- Нет broken links.
- У доступных работ на detail-page есть `Request price`.

---

## P1.5. Улучшить Story: заменить слишком клинические формулировки

### Проблема

Страница Story стала лучше, но блок `Artistic Themes` содержит тему `Emotional Trauma`. Это честно, но может звучать слишком клинически и тяжело для первого знакомства с художницей.

### Что сделать

Заменить на более художественную формулировку:

```text
Pain & Transformation
```

или:

```text
Emotional Transformation
```

или:

```text
Inner Wounds
```

### Рекомендованная структура тем

```text
Memory
Pain & Transformation
Tenderness
Distorted Reality
Communication
City Life
Symbolic Objects
Flowers
Inner Reconstruction
```

### Acceptance criteria

- Story сохраняет эмоциональную глубину.
- Текст не звучит как медицинская карточка или терапевтический отчёт.
- Художница воспринимается профессионально, не только через травму.

---

## P1.6. Проверить дубли навигации в DOM и визуале

### Проблема

В HTML-структуре страниц навигация встречается дважды подряд. Это может быть нормой, если одна версия desktop, другая mobile и одна из них скрыта. Но если обе видны пользователю или обе доступны скринридеру, это проблема.

### Что сделать

Проверить:

- desktop viewport;
- mobile viewport;
- keyboard navigation;
- screen reader/accessibility tree, если возможно.

### Требования

- Визуально меню не должно дублироваться.
- Скринридер не должен читать одно и то же меню дважды.
- Если есть два меню, скрытое меню должно быть корректно скрыто через `aria-hidden="true"` или другой подход.

### Acceptance criteria

- Пользователь видит одно меню.
- Клавишей Tab пользователь проходит меню один раз, а не дважды.
- Нет duplicate navigation landmarks без необходимости.

---

# P2 — улучшения после исправления базы

---

## P2.1. Добавить fullscreen-просмотр работ

### Что сделать

При клике на изображение работы открывать fullscreen viewer:

```text
Large image
Title
Technique · Size · Year
Status
Close
Request price — if available
```

### Acceptance criteria

- Изображения можно рассмотреть крупно.
- Viewer работает на mobile.
- Есть закрытие по Esc и по кнопке.
- Изображение не скачет и не обрезается критично.

---

## P2.2. Добавить SEO-метаданные для ключевых страниц

### Что сделать

У каждой страницы должен быть уникальный title и description.

Примеры:

```text
Home title:
Alena Mart — Contemporary Artist
```

```text
Available title:
Available Works — Alena Mart
```

```text
Collections title:
Art Collections — Alena Mart
```

```text
Story title:
Story & Artist Statement — Alena Mart
```

```text
Exhibitions title:
Exhibitions & Events — Alena Mart
```

### Acceptance criteria

- Нет одинаковых meta title на всех страницах.
- У каждой коллекции свой title.
- Open Graph image задана для главной и коллекций.

---

## P2.3. Улучшить изображения и alt-тексты

### Что сделать

Проверить все изображения:

- изображения не должны быть слишком тяжёлыми;
- использовать responsive sizes;
- использовать lazy loading ниже первого экрана;
- alt должен описывать работу, а не быть просто `Image`.

### Пример alt

```text
Alt: "Gone, acrylic painting by Alena Mart from the Confessions should be better planned collection"
```

### Acceptance criteria

- Нет alt `Image` для ключевых работ.
- Hero image имеет осмысленный alt.
- Изображения не ломают mobile layout.
- Lazy loading включён для галерей.

---

## P2.4. Добавить мягкие empty states и loading states

### Что сделать

Если фильтр не находит работ:

```text
No works in this category right now.
```

Если форма отправляется:

```text
Sending...
```

Если форма успешно отправлена:

```text
Thank you. Your request has been sent.
```

Если ошибка:

```text
Something went wrong. Please email directly at alenam.art@gmail.com.
```

### Acceptance criteria

- Пользователь понимает, что происходит после клика.
- Нет молчаливых состояний.
- Нет кнопки, которая нажимается и визуально ничего не меняет.

---

# Постраничный план изменений

---

## 1. Главная `/`

### Статус

Страница стала намного лучше. Hero уже содержит имя, слоган, позиционирование и CTA.

### Что сделать

- Проверить, что все CTA ведут на правильные страницы.
- Проверить, что на mobile hero не занимает слишком много высоты.
- Проверить, что `Available Works` блок содержит только реально доступные работы.
- Добавить короткое пояснение перед `Available Works`, что цены и доставка уточняются по запросу.
- Проверить, что CTA `Contact the Artist` ведёт на `/contact/`.

### Acceptance criteria

- Первый экран понятен без скролла.
- Есть CTA на Collections, Available, Contact.
- На mobile кнопки удобно нажимать.
- Главная не содержит старые пункты `ART`, `MY story`, `Blog`.

---

## 2. Collections `/art/`

### Что сделать

- Превратить `Available works inside` в badge.
- По возможности заменить на точное число: `2 available`, `7 available`.
- Проверить, что количество работ совпадает с реальным количеством карточек внутри коллекции.
- Сделать всю карточку коллекции кликабельной или хотя бы изображение + название + CTA.
- Убедиться, что карточки имеют одинаковую высоту/ритм.

### Acceptance criteria

- Все 7 коллекций отображаются.
- У каждой есть название, описание, изображение, количество работ.
- Информация о доступных работах визуально отделена.
- Нет случайных текстовых приписок внутри metadata line.

---

## 3. Available Works `/art/available/`

### Что сделать

- Сделать фильтры рабочими.
- Добавить фильтр по коллекциям.
- Привязать `Request price` к конкретной работе.
- Проверить все доступные работы на соответствие статусу в исходных коллекциях.
- Добавить brief commercial note:

```text
For prices, shipping and availability details, send a request for the selected artwork.
```

### Acceptance criteria

- Все доступные работы действительно имеют статус Available в коллекциях.
- Нет sold/private works на странице Available.
- Каждая карточка содержит название коллекции.
- `Request price` передаёт artwork title в Contact.

---

## 4. Big City Life `/art/big-city-life/`

### Что сделать

- Проверить, что `Rainy Eiffel` и `Rainy Eiffel II` — действительно разные работы.
- Если это разные работы, оставить обе, но убедиться, что изображения разные.
- Если это дубль, оставить одну работу и один статус.
- Исправить Previous/Next согласно единому порядку коллекций.
- Сделать фильтры рабочими.
- Статусы `Available`, `Sold`, `Private collection` оформить бейджами.

### Acceptance criteria

- `Next → Bits and Pieces`, если Big City Life первая коллекция.
- Нет некорректного `Previous`.
- Available works имеют `Request price`.
- Sold/private works не имеют purchase CTA.

---

## 5. Bits and Pieces `/art/bits-and-pieces/`

### Что сделать

- Исправить Previous/Next.
- Если все работы `Private collection`, фильтр `Available` должен показывать empty state.
- Проверить, нужен ли CTA `Looking for a quiet emotional piece?`, если внутри нет доступных работ.

### Рекомендация

Если доступных работ нет, CTA лучше формулировать как реплику/commission:

```text
Interested in a similar work or replica?
[Contact the Artist]
```

### Acceptance criteria

- `Previous → Big City Life`.
- `Next → Little Pleasures`.
- Фильтр Available не показывает private works.
- CTA не создаёт ложное впечатление, что работы внутри доступны.

---

## 6. Little Pleasures `/art/little-pleasures/`

### Что сделать

- Исправить Previous/Next.
- Проверить, что `Little pleasure I` доступна и есть на Available Works.
- Сделать `Request price` контекстным.
- Проверить, что pastel/paper формат указан одинаково во всех работах.

### Acceptance criteria

- `Previous → Bits and Pieces`.
- `Next → At the Seaside`.
- Доступная работа есть в `/art/available/`.
- Статус и CTA не находятся в одной текстовой строке без визуального разделения.

---

## 7. At the Seaside `/art/at-the-seaside/`

### Что сделать

- Исправить Previous/Next.
- Если все работы private collection, не делать агрессивный purchase CTA.
- Фильтр Available должен показывать empty state.

### Acceptance criteria

- `Previous → Little Pleasures`.
- `Next → Mind Games`.
- Нет доступных работ, если все private.
- CTA звучит как inquiry/commission, а не покупка конкретной работы.

---

## 8. Mind Games `/art/mind-games/`

### Что сделать

- Исправить пустой `Next →`.
- Заменить `acryl` на `acrylic`.
- Заменить `coal` на `charcoal`, если имеется в виду художественный уголь.
- Проверить порядок материалов: лучше использовать единый стиль.

### Acceptance criteria

- `Previous → At the Seaside`.
- `Next → Confessions should be better planned`.
- Нет пустого next-link.
- Нет слова `acryl`.
- Нет непрофессионального `coal`, если имеется в виду `charcoal`.

---

## 9. Confessions should be better planned `/art/confessions-should-be-better-planned/`

### Что сделать

- Убрать повтор фразы:

```text
Selected works from this collection are available for purchase.
```

- Исправить `The tune`:
  - добавить год/месяц, если известен;
  - статус `Available` вынести отдельно.
- Исправить Previous/Next.
- Сделать `Ask about the collection` и `Request price` понятными разными сценариями.

### Рекомендация по CTA

Вверху коллекции:

```text
[Ask about the collection]
```

На доступных работах:

```text
[Request price]
```

Эти кнопки должны вести в Contact с разным контекстом.

### Acceptance criteria

- Нет повторяющегося текста в описании.
- У `The tune` нет строки `50×70 cm · Available`.
- `Previous → Mind Games`.
- `Next → Flora`.
- Все available works есть на `/art/available/`.

---

## 10. Flora `/art/flora/`

### Что сделать

- Исправить Previous/Next.
- Проверить, что `Flora I` и `Flora VIII` действительно доступны и есть на Available Works.
- Если `Flora` последняя коллекция, не показывать Next.
- Проверить, не слишком ли однообразно выглядят карточки, если у всех работ одинаковые размеры и год.

### Acceptance criteria

- `Previous → Confessions should be better planned`.
- Нет некорректного Next.
- Доступные работы имеют `Request price`.
- Sold/private works не имеют purchase CTA.

---

## 11. Story `/story/`

### Что сделать

- Заменить `Emotional Trauma` на более художественную формулировку.
- Проверить, что `Exhibitions & Recognition` соответствует данным из `/blog/` после исправления дат.
- Добавить 1–2 ссылки из Story:

```text
[View Collections]
[See Exhibitions]
```

- Не перегружать страницу личными подробностями в начале.

### Acceptance criteria

- Story звучит профессионально и эмоционально.
- Нет противоречий с датами exhibitions.
- Есть CTA в конце и/или после Biography.
- Текст не сводит художницу только к травме.

---

## 12. Exhibitions `/blog/`

### Что сделать

- Исправить реальные даты событий.
- Переписать excerpts в более профессиональном тоне.
- Добавить одинаковую структуру metadata:

```text
Date · City · Venue
```

- Проверить detail pages для событий.
- Если `/blog/` используется как URL, но в интерфейсе раздел называется `Exhibitions`, это допустимо. Но желательно позже сделать alias `/exhibitions/`.

### Acceptance criteria

- В UI используется название `Exhibitions & Events`.
- Слово `Blog` не видно пользователю.
- Даты событий не конфликтуют с описаниями.
- Старые события не выглядят как произошедшие в 2024 году.

---

## 13. Contact `/contact/`

### Что сделать

- Проверить рабочую отправку формы.
- Сделать `I am interested in` настоящими radio/select/checkbox.
- Добавить обработку query params от `Request price`.
- Добавить success/error states.
- Добавить direct email как fallback.
- Добавить privacy reassurance:

```text
Your message will be sent directly to the artist.
```

### Acceptance criteria

- Форма отправляется.
- Все обязательные поля валидируются.
- Заявка с конкретной работы содержит название работы.
- Direct email виден.
- Форма удобна на mobile.

---

# Общие требования к UI

## Визуальный стиль

Сохранять:

- драматичность;
- художественность;
- ощущение private gallery;
- сильный контраст;
- чёрный/белый/красный как эмоциональный акцент;
- крупные изображения;
- много воздуха.

Не делать:

- SaaS-стиль;
- агрессивные продающие баннеры;
- перегруженные анимации;
- кислотные цвета;
- generic template look.

---

## Mobile-first требования

Проверить все страницы на ширинах:

```text
375px
390px
430px
768px
1024px
1440px
```

### Acceptance criteria

- Кнопки не мельче 44px по высоте.
- Фильтры можно нажимать пальцем.
- Карточки не ломаются.
- Тексты не слипаются.
- Изображения не растягиваются некрасиво.
- Header не занимает слишком много экрана.
- Footer не выглядит как мусорный блок.

---

## Accessibility

### Требования

- У всех интерактивных элементов есть keyboard focus.
- У фильтров есть active state.
- У изображений есть alt.
- У формы есть labels.
- У radio/select/checkbox есть fieldset/legend.
- Нет duplicate menu в Tab order.
- Контраст текста достаточный.

---

## Performance

### Требования

- Использовать оптимизированные изображения.
- Не грузить все большие изображения в hero-size.
- Lazy loading для галерей.
- Минимизировать layout shift.
- Проверить Lighthouse хотя бы для Home, Available, Collection page, Contact.

### Минимальные целевые показатели

```text
Performance: 80+
Accessibility: 90+
Best Practices: 90+
SEO: 85+
```

---

# Финальный QA-чеклист

Перед завершением работы пройти чеклист.

## Навигация

- [ ] Меню одинаковое на всех страницах.
- [ ] Нет видимого дублирования меню.
- [ ] `Collections` ведёт на `/art/`.
- [ ] `Available` ведёт на `/art/available/`.
- [ ] `Story` ведёт на `/story/`.
- [ ] `Exhibitions` ведёт на `/blog/` или `/exhibitions/`.
- [ ] `Contact` ведёт на `/contact/`.

## Коллекции

- [ ] Все 7 коллекций видны на `/art/`.
- [ ] Previous/Next работает по единому порядку.
- [ ] Нет пустого `Next →`.
- [ ] Нет неправильного previous/next.
- [ ] Фильтры работают.
- [ ] Статусы оформлены бейджами.

## Данные работ

- [ ] Нет `acryl`; используется `acrylic`.
- [ ] Нет статуса внутри строки даты/размера.
- [ ] `The tune` исправлена.
- [ ] `Confessions` не содержит повторной фразы.
- [ ] `Rainy Eiffel` и `Rainy Eiffel II` проверены.
- [ ] Все available works есть на `/art/available/`.
- [ ] Sold/private works не показываются на Available.

## Available Works

- [ ] Фильтры работают.
- [ ] Есть фильтр по коллекции.
- [ ] У каждой работы есть `Request price`.
- [ ] `Request price` передаёт название работы в Contact.
- [ ] Пользователь не должен вручную писать название картины.

## Exhibitions

- [ ] Даты событий исправлены.
- [ ] Нет конфликта `2024` vs `2013/2014/2018/2019`.
- [ ] Excerpts звучат профессионально.
- [ ] Metadata имеет единый формат.
- [ ] Слово `Blog` не видно пользователю.

## Contact

- [ ] Форма реально отправляет заявки.
- [ ] Есть validation.
- [ ] Есть success state.
- [ ] Есть error state.
- [ ] Interest options интерактивны.
- [ ] Query params от Request price обрабатываются.
- [ ] Direct email виден.

## Mobile

- [ ] Проверено на 375px.
- [ ] Проверено на 390px.
- [ ] Проверено на 430px.
- [ ] Кнопки удобны.
- [ ] Фильтры не ломаются.
- [ ] Галереи читаемые.

---

# Приоритет выполнения

## Сначала сделать

```text
1. Exhibitions dates and metadata
2. Previous/Next navigation
3. Artwork data cleanup
4. Functional filters
5. Request price → Contact context
6. Working Contact form
```

## Потом сделать

```text
7. Available page improvements
8. Collections badges and counts
9. Exhibitions tone rewrite
10. Story tone polish
11. Detail pages / fullscreen viewer
```

## В конце проверить

```text
12. Mobile QA
13. Accessibility QA
14. Performance QA
15. SEO metadata
16. Broken links
```

---

# Главный критерий готовности

Сайт считается готовым к следующему ревью, когда пользователь может пройти сценарий без трения:

```text
Открыть главную
→ понять, кто художница
→ перейти в Available Works
→ выбрать конкретную работу
→ нажать Request price
→ попасть в Contact с уже заполненным контекстом работы
→ отправить заявку
```

И второй сценарий:

```text
Открыть Collections
→ выбрать коллекцию
→ отфильтровать Available/Sold/Private
→ открыть или запросить конкретную работу
→ вернуться к следующей коллекции через корректный Next/Previous
```

Если эти два сценария работают — сайт уже можно считать не просто красивой галереей, а профессиональным арт-портфолио с коммерческой логикой.
