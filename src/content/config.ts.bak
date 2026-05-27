import { defineCollection, z } from 'astro:content';

// Site settings — single file
const settings = defineCollection({
  type: 'data',
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

// Pages — home, story
const pages = defineCollection({
  type: 'data',
  schema: z.object({
    title: z.string().optional(),
    hero_title: z.string().optional(),
    hero_statement: z.string().optional(),
    featured_collections: z.array(z.string()).optional(),
    body: z.string().optional(),
  }),
});

// Art collections
const collections = defineCollection({
  type: 'data',
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
  type: 'data',
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
  type: 'content',
  schema: z.object({
    title: z.string(),
    event_date: z.date(),
    published_date: z.date().optional(),
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
  art_collections: collections,
  artworks,
  events,
};
