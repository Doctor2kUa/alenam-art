# AI Agent Instruction — Alena Mart Website

## Project

Website: `https://alenam-art-0u7i5kpw.netlify.app`

Goal: bring the current website to production-quality level without changing the core visual concept.

The site already has the correct high-level structure:

```text
Home → Collections → Available Works → Artwork Detail → Contact
```

Do not redesign the website from scratch. Focus on fixing critical UX, data, navigation, form and content-quality issues.

---

## Important Restrictions

- Do not add recommendations or tasks related to additional languages, translations, multilingual support or localization.
- Do not change the artistic positioning unless required for UX clarity.
- Do not add new large sections before fixing the current bugs.
- Do not remove the emotional tone of the artist brand.
- Do not make the site look like a generic SaaS landing page.
- Keep the art as the main visual focus.

---

## Current Status

The latest version is significantly improved compared to the previous version.

Already improved:

- Unified main navigation: `Collections`, `Available`, `Story`, `Exhibitions`, `Contact`.
- Home page now has a clear hero section with artist name, statement and CTA buttons.
- `Available Works` page exists and works as a commercial entry point.
- `Story` page is more structured and professional.
- `Exhibitions & Events` has clearer dates, locations and event cards.
- Artwork detail pages exist.
- `Request price` links pass artwork and collection parameters to the contact page.

Remaining problem: the site still feels unfinished because several technical and UX issues are visible to users.

---

# P0 — Critical Fixes

These issues must be fixed before the website can be considered production-ready.

---

## P0.1 — Fix Broken Exhibition Event Links

### Problem

On the `Exhibitions & Events` page, the `View event →` links lead to 404 pages.

Example broken path:

```text
/blog/amazing-evening-amazing-place-amazing-people/
```

This damages trust because the Exhibitions section is supposed to prove the artist's professional background.

### Pages

- `/blog/`
- All event detail URLs linked from exhibition cards

### Required Action

Choose one of these two approaches:

#### Option A — Preferred

Create detail pages for every exhibition/event card.

Each event detail page should include:

```text
Event title
Date
City
Venue
Short description
Image/gallery
Related collection or artwork
Back to Exhibitions
Contact CTA
```

#### Option B — Temporary

If detail pages are not ready, remove the `View event →` links from the cards.

Do not leave clickable links that lead to 404.

### Acceptance Criteria

- Every `View event →` link opens a valid page.
- No event card leads to 404.
- If no detail page exists, the event card has no misleading clickable CTA.
- Event pages have a clear `Back to Exhibitions` link.
- Event pages keep the same site header and footer.

---

## P0.2 — Fix Incorrect Empty State Rendering

### Problem

The text:

```text
No works in this category right now.
```

appears even when artworks are visible below it.

This happens on:

- `/art/available/`
- `/art/big-city-life/`
- Possibly other collection pages

This makes the filtering logic look broken.

### Required Action

Render the empty state only when the currently selected filter returns zero items.

Default `All` view must never show empty state if works exist.

### Correct Logic

```js
if (filteredWorks.length === 0) {
  showEmptyState();
} else {
  showWorksGrid();
}
```

### Acceptance Criteria

- `/art/available/` does not show empty state in default view.
- `/art/big-city-life/` does not show empty state in default view.
- Empty state appears only after selecting a filter with no matching works.
- Empty state text is not present in visible content, hidden DOM, or accessibility tree when not needed.
- Screen readers should not announce the empty state when works exist.

---

## P0.3 — Make Filters Look and Behave Like Real Filters

### Problem

Filters currently look like plain text:

```text
All Available Sold Private collection
```

On the `Available Works` page, filters exist but the current state is not clear enough.

### Pages

- `/art/available/`
- All collection pages:
  - `/art/big-city-life/`
  - `/art/bits-and-pieces/`
  - `/art/little-pleasures/`
  - `/art/at-the-seaside/`
  - `/art/mind-games/`
  - `/art/confessions-should-be-better-planned/`
  - `/art/flora/`

### Required Action

Turn filters into actual button controls with clear visual states.

### Collection Page Filter Format

```text
All (11)
Available (2)
Sold (4)
Private collection (5)
```

### Available Works Filter Format

```text
All (12)
Paintings (11)
Drawings (1)
Small format (2)
Large format (6)
```

Collection filters:

```text
All collections
Confessions
Big City Life
Little Pleasures
Flora
```

### UX Requirements

- Active filter must be visually obvious.
- Buttons must be keyboard-focusable.
- Selected filter should update the visible artwork list immediately.
- If JavaScript is used, the page must not break if a filter has zero results.
- Filter labels must not wrap into unreadable text on mobile.

### Acceptance Criteria

- Filters are real buttons or accessible controls.
- Active state is visible.
- Filter counts match actual artwork data.
- Empty state appears only when a selected filter has zero results.
- Mobile layout remains clean.

---

## P0.4 — Improve Request Price Flow

### Problem

`Request price` links pass parameters to the contact page, for example:

```text
?artwork=Gone&collection=Confessions+should+be+better+planned&interest=buy
```

But the visible contact page does not show that the form understands which artwork the user selected.

### Pages

- `/art/available/`
- Artwork detail pages
- `/contact/`

### Required Action

When the contact page receives artwork parameters, show a contextual request summary above the form.

### Required Visible Block

```text
You are requesting price for:
Gone

Collection:
Confessions should be better planned
```

### Required Form Prefill

Subject:

```text
Price request: Gone
```

Message:

```text
Hello, I am interested in the artwork “Gone” from the “Confessions should be better planned” collection. Please send me the price and shipping details.
```

Interest field:

```text
Buying an available artwork
```

### Acceptance Criteria

- Clicking `Request price` from any artwork opens Contact with the correct artwork context.
- Artwork title is visible on the contact page.
- Collection name is visible on the contact page.
- Subject is prefilled.
- Message is prefilled.
- Interest field is preselected.
- User can still edit all fields before sending.

---

## P0.5 — Fix Contact Form Honeypot Visibility

### Problem

The text:

```text
Don't fill this out:
```

appears in the contact page structure.

This is likely a honeypot anti-spam field, but it must not be visible or announced to users.

### Page

- `/contact/`

### Required Action

Hide the honeypot field correctly from visual users and assistive technologies.

### Implementation Guidance

Use a visually hidden anti-spam field that is not focusable.

Example requirements:

```text
tabindex="-1"
aria-hidden="true"
autocomplete="off"
```

Do not use `display: none` if the form provider requires the field to exist, but ensure normal users never interact with it.

### Acceptance Criteria

- The text `Don't fill this out:` is not visible.
- The honeypot field is not keyboard-focusable.
- Screen readers do not announce the honeypot as part of the form.
- The form still submits correctly.

---

# P1 — Important Improvements

These tasks are not as urgent as P0, but they are needed for a polished final version.

---

## P1.1 — Enrich Artwork Detail Pages

### Problem

Artwork detail pages exist, but they feel too empty. They currently behave like enlarged artwork cards.

### Pages

All artwork detail pages, for example:

- `/art/big-city-life/april-in-minsk/`
- `/art/confessions-should-be-better-planned/a-thought/`
- Other individual artwork pages

### Required Action

Add a stronger detail-page structure.

### Required Template

```text
Artwork image

Title
Technique · Size · Year
Status badge
Collection link

About this work
1–3 short paragraphs about the mood, story, location, symbol or emotional context.

Details
Technique
Size
Year / Month
Collection
Status

Action block
If available:
  Request price
If not available:
  Ask about similar work

Similar works
3 artworks from the same collection
```

### Acceptance Criteria

- Each artwork detail page has more value than a simple card.
- Available works show `Request price`.
- Sold/private works show `Ask about similar work`.
- Similar works are from the same collection.
- There is a clear link back to the collection.
- Layout works well on mobile.

---

## P1.2 — Improve Available Works Page as a Sales Page

### Problem

The `Available Works` page exists and is useful, but it can work harder as a buyer-focused page.

### Page

- `/art/available/`

### Required Action

Make the page more clearly commercial without making it aggressive.

### Add/Improve

```text
Intro:
Original artworks currently available for purchase.
For pricing, shipping and availability, send a request for a specific piece.

Trust line:
Original works · Direct contact with the artist · Shipping details on request · Replicas and commissions available
```

Keep this section concise.

### Card Requirements

Each available artwork card must show:

```text
Image
Title
Technique
Size
Year
Collection
Available badge
Request price button
```

### Acceptance Criteria

- Every available card has a clear CTA.
- No unavailable artwork appears on this page.
- Collection link works.
- Filters do not show wrong empty states.
- Buyer understands how to request price.

---

## P1.3 — Add Counters and Data Consistency to Collections

### Problem

Collection overview already displays useful counts like:

```text
11 works · 2 available
```

This is good, but counts must be accurate and consistent with actual data.

### Page

- `/art/`

### Required Action

Ensure collection counts are generated from the same data source used to render artworks.

### Acceptance Criteria

- Total works count matches the actual number of works in each collection page.
- Available count matches actual works marked `Available`.
- If a collection has zero available works, do not show `0 available` unless intentionally styled.
- Counts update automatically when data changes.

---

## P1.4 — Improve Exhibitions Cards

### Problem

The `Exhibitions & Events` page is much better, but event cards still need stronger consistency.

### Page

- `/blog/`

### Required Event Card Format

```text
Image
Date · City · Venue
Event title
Short description
View event
```

### Required Action

Normalize all event cards:

- Date format must be consistent.
- City must be visible.
- Venue should be visible when known.
- CTA must work or be removed.
- Titles should use consistent capitalization.

### Acceptance Criteria

- All event cards use the same structure.
- Event metadata is scan-friendly.
- No event card leads to a broken page.
- Descriptions are concise and professional.

---

## P1.5 — Clean Duplicate Navigation in Accessibility Structure

### Problem

The navigation appears twice in the page text structure. This is probably desktop and mobile nav rendered together.

### Pages

All pages.

### Required Action

Ensure duplicate navigation does not create accessibility noise.

### Acceptable Solutions

Option A:

Use one responsive navigation component.

Option B:

Keep desktop and mobile menus, but hide the inactive duplicate from assistive technologies.

### Acceptance Criteria

- Screen readers do not announce the same menu twice.
- Keyboard navigation does not tab through duplicate menu items.
- Visual layout remains unchanged.
- Mobile navigation still works.

---

# P2 — Final Polish

These tasks should be done only after P0 and P1.

---

## P2.1 — Add Fullscreen Artwork Viewer

### Goal

Improve art browsing experience.

### Requirements

- Clicking artwork image opens a large viewer.
- Viewer supports close button.
- Viewer supports keyboard escape.
- Viewer works on mobile.
- Do not make the viewer visually noisy.

---

## P2.2 — Add Trust Block on Home Page

### Goal

Strengthen credibility without adding clutter.

### Suggested Block

```text
Exhibitions across Europe
Works in private collections
Original works available
Direct contact with the artist
```

### Placement

Home page, after `My Art` or before `Available Works`.

### Acceptance Criteria

- Block is short.
- It does not distract from the artworks.
- It improves trust before the user reaches the purchase CTA.

---

## P2.3 — Add Better Back/Next Navigation on Artwork Detail Pages

### Required Navigation

```text
← Previous work
Back to collection
Next work →
```

### Acceptance Criteria

- Works inside the same collection.
- No broken previous/next links.
- First and last artwork states are handled gracefully.

---

# Page-by-Page Instructions

---

## Home Page `/`

### Keep

- Artist name.
- Main slogan.
- Short positioning statement.
- CTA buttons.
- My Art block.
- Collections preview.
- Available Works preview.
- Exhibitions preview.
- Contact CTA.

### Change

- Add a small trust block if it does not make the page crowded.
- Check duplicated navigation.
- Make sure all CTA buttons lead to valid pages.
- Ensure preview artworks link to correct detail pages where possible.

### Acceptance Criteria

- First screen clearly communicates who the artist is.
- User can immediately choose:
  - View Collections
  - Available Works
  - Contact the Artist
- No broken links.
- No duplicate nav for screen readers.

---

## Collections Overview `/art/`

### Keep

- Collection cards.
- Short collection descriptions.
- Work counts.
- Available counts.

### Change

- Verify all counts.
- Ensure every collection card links to a valid collection page.
- Make card spacing and image treatment consistent.

### Acceptance Criteria

- All 7 collections are present.
- All links work.
- Counts are correct.
- Page looks like a curated gallery index, not a blog archive.

---

## Available Works `/art/available/`

### Keep

- Commercial intro.
- Trust line.
- Available artwork grid.
- Request price buttons.
- Collection filters.

### Change

- Fix empty state.
- Add active filter states.
- Add filter counts.
- Ensure `Request price` opens contextual contact form.
- Ensure only available works appear.

### Acceptance Criteria

- No incorrect empty state.
- All filters work.
- All `Request price` links work.
- Contact page receives and displays artwork context.
- Mobile layout remains clean.

---

## Collection Pages `/art/{collection}/`

### Keep

- Back to Collections link.
- Collection title.
- Short description.
- Artwork grid.
- Status labels.
- Request price for available works.
- Bottom navigation between collections.

### Change

- Fix empty state.
- Turn filters into real buttons.
- Add counts to filters.
- Ensure statuses are consistent:
  - `Available`
  - `Sold`
  - `Private collection`
- Ensure available works show CTA.
- Ensure unavailable works do not show price CTA.

### Acceptance Criteria

- Default view never shows incorrect empty state.
- Filter counts are correct.
- All artwork cards use the same data format.
- Navigation to next/previous collection works.
- No duplicate or inconsistent artwork data.

---

## Artwork Detail Pages `/art/{collection}/{artwork}/`

### Keep

- Large artwork image.
- Title.
- Technique, size, year.
- Status.
- Collection link.
- CTA.

### Change

- Add `About this work`.
- Add structured details.
- Add similar works.
- Add previous/back/next navigation.
- Improve CTA depending on artwork status.

### Acceptance Criteria

- Detail page feels intentional, not empty.
- Available works lead to contextual price request.
- Sold/private works lead to similar-work inquiry.
- Related works are relevant.
- No broken links.

---

## Story `/story/`

### Keep

- Artist Statement.
- Biography.
- Themes.
- Collections context.
- Exhibitions & Recognition.

### Change

- Keep the story professional and emotionally honest.
- Avoid making the first section too heavy or traumatic.
- Ensure links to collections/exhibitions work.

### Acceptance Criteria

- Page reads like a professional artist biography.
- Emotional background supports the art instead of overwhelming the reader.
- No broken internal links.
- Layout is readable on mobile.

---

## Exhibitions `/blog/`

### Keep

- Page title `Exhibitions & Events`.
- Chronological event cards.
- Dates, cities and venues.
- Collaboration CTA.

### Change

- Fix or remove all broken `View event` links.
- Normalize card structure.
- Create event detail pages if CTAs remain.
- Ensure event dates and venues are accurate.
- Avoid blog-style language.

### Acceptance Criteria

- No 404 from event links.
- Every card has consistent metadata.
- Event detail pages have useful content.
- Page supports trust and credibility.

---

## Contact `/contact/`

### Keep

- Form.
- Interest selector.
- Direct email.
- Form status messages.
- Contact purpose text.

### Change

- Hide honeypot properly.
- Add contextual request summary when URL contains artwork parameters.
- Prefill subject/message/interest when user clicks `Request price`.
- Check all form states:
  - idle
  - sending
  - success
  - error

### Acceptance Criteria

- User sees which artwork they are asking about.
- User does not see technical anti-spam fields.
- Form is easy to use.
- Error message includes direct email fallback.
- Success message is clear.

---

# Data Cleanup Rules

Use one consistent format across all artworks.

## Artwork Data Schema

```js
{
  title: string,
  slug: string,
  collection: string,
  technique: string,
  size: string,
  year: string,
  status: "Available" | "Sold" | "Private collection",
  image: string,
  description?: string
}
```

## Status Rules

Use only these values:

```text
Available
Sold
Private collection
```

Do not use mixed variants such as:

```text
Private
In private collection
private collection
available
SOLD
```

## Technique Rules

Use consistent terms:

```text
Acrylic on canvas
Oil on canvas
Pastel, paper
Mixed media
Grattage
```

Do not mix:

```text
Acryl
Acrylics
acrylic
```

unless it is intentionally part of the artwork data.

## CTA Rules

```text
Available → Request price
Sold → Ask about similar work
Private collection → Ask about similar work
```

---

# QA Checklist

Before marking the task complete, test the following manually.

## Navigation

- [ ] Header menu works on every page.
- [ ] Header menu is not duplicated for screen readers.
- [ ] Footer links work.
- [ ] Collection next/previous links work.
- [ ] Artwork previous/back/next links work.

## Broken Links

- [ ] No 404 from exhibition cards.
- [ ] No 404 from collection cards.
- [ ] No 404 from artwork cards.
- [ ] No 404 from CTAs.
- [ ] Social links work.

## Filters

- [ ] Available Works filters work.
- [ ] Collection filters work.
- [ ] Active state is visible.
- [ ] Counts are correct.
- [ ] Empty state appears only when correct.

## Contact Flow

- [ ] `Request price` passes artwork title.
- [ ] `Request price` passes collection name.
- [ ] Contact page displays artwork context.
- [ ] Subject is prefilled.
- [ ] Message is prefilled.
- [ ] Interest is preselected.
- [ ] Honeypot is hidden.
- [ ] Success and error states work.

## Content

- [ ] Artwork statuses are consistent.
- [ ] Techniques are consistent.
- [ ] Sizes are consistent.
- [ ] Dates are consistent.
- [ ] Exhibition dates are correct.
- [ ] No placeholder text remains.

## Mobile

- [ ] Home hero works on mobile.
- [ ] Filters do not break layout.
- [ ] Cards are readable.
- [ ] Contact form is easy to fill.
- [ ] Artwork detail pages are usable.
- [ ] No horizontal scroll.

---

# Final Delivery Requirements

The task is complete only when:

1. No visible 404 links remain.
2. Empty state logic is fixed.
3. Filters are visually and functionally clear.
4. Contact form shows artwork context from `Request price`.
5. Honeypot is hidden properly.
6. Artwork detail pages have enough content to feel intentional.
7. Collection and artwork data are consistent.
8. Mobile version is clean.
9. No recommendations or functionality related to additional languages are added.
