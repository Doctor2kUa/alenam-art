import { defineCollection, z } from 'astro:content';
import { file, glob } from 'astro/loaders';

// Site settings — single file
const settings = defineCollection({
  loader: file('src/content/settings/site.json'),
  schema: z.object({
    site_title: z.string(),
    site_description: z.string(),
    artist_name: z.string(),
    email: z.string().email(),
    instagram_url: z.string().url().optional(),
    facebook_url: z.string().url().optional(),
    linkedin_url: z.string().url().optional(),
    logo: z.string().optional(),
    og_image: z.string().optional(),
    favicon: z.string().optional(),
    media_base_url: z.string().url().default('https://media.alenam.art'),
  }),
});

// Pages — home (JSON), story (MD with frontmatter)
const pages = defineCollection({
  loader: glob({ pattern: '**/*.{json,md}', base: 'src/content/pages' }),
  schema: z.object({
    title: z.string().optional(),
    hero_title: z.string().optional(),
    hero_statement: z.string().optional(),
    featured_collections: z.array(z.string()).optional(),
  }),
});

// Art collections
const art_collections = defineCollection({
  loader: glob({ pattern: '*.json', base: 'src/content/collections' }),
  schema: z.object({
    slug: z.string(),
    title: z.string(),
    subtitle: z.string().optional(),
    description: z.string().optional(),
    cover_image: z.string().optional(),
    order: z.number().default(0),
    prev_slug: z.string().optional(),
    next_slug: z.string().optional(),
    cta: z.string().optional(),
    featured_on_home: z.boolean().default(false),
  }),
});

// Artworks
const artworks = defineCollection({
  loader: glob({ pattern: '**/*.json', base: 'src/content/artworks' }),
  schema: z.object({
    slug: z.string(),
    name: z.string(),
    collection: z.string(),
    technique: z.string(),
    size: z.string(),
    year: z.string(),
    status: z.enum(['Available', 'Sold', 'Private collection']).default('Available'),
    image: z.string().optional(),
    images: z.array(z.object({ image: z.string() })).optional(),
    description: z.string().optional(),
    order: z.number().default(0),
    featured_on_home: z.boolean().default(false),
    featured_available: z.boolean().default(false),
    cta: z.string().optional(),
  }),
});

// Events
const events = defineCollection({
  loader: glob({ pattern: '*.md', base: 'src/content/events' }),
  schema: z.object({
    title: z.string(),
    event_date: z.coerce.date(),
    published_date: z.coerce.date().optional(),
    city: z.string().optional(),
    country: z.string().optional(),
    venue: z.string().optional(),
    cover_image: z.string().optional(),
    gallery: z.array(z.object({ image: z.string() })).optional(),
    excerpt: z.string().optional(),
    related_collection: z.string().optional(),
    related_artworks: z.array(z.string()).optional(),
  }),
});

export const collections = {
  settings,
  pages,
  art_collections,
  artworks,
  events,
};
