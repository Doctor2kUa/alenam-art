/// <reference types="astro/client" />

/**
 * Media helper for Alena Mart site.
 * 
 * Converts various image URL formats to the correct R2 public URL.
 * 
 * Supported input formats:
 * - Absolute URL: https://alenam.art/wp-content/uploads/2025/01/IMG_5829.avif
 * - Relative path: /uploads/2025/01/IMG_5829.avif
 * - Upload path: uploads/2025/01/IMG_5829.avif
 * 
 * Output: https://media.alenam.art/uploads/2025/01/IMG_5829.avif
 */

const MEDIA_BASE_URL = import.meta.env.PUBLIC_MEDIA_BASE_URL || 'https://media.alenam.art';
const WP_UPLOADS_PATTERN = /^https?:\/\/alenam\.art\/wp-content\/uploads\//i;

/**
 * Normalize any image URL to R2 public URL.
 */
export function normalizeImageUrl(url: string | undefined | null): string {
  if (!url) return '';
  
  // Already absolute R2 URL
  if (url.startsWith(MEDIA_BASE_URL)) {
    return url;
  }
  
  // WordPress uploads URL — extract path and prepend R2 base
  if (WP_UPLOADS_PATTERN.test(url)) {
    const path = url.replace(WP_UPLOADS_PATTERN, '');
    return `${MEDIA_BASE_URL}/uploads/${path}`;
  }
  
  // Already starts with /uploads/
  if (url.startsWith('/uploads/')) {
    return `${MEDIA_BASE_URL}${url}`;
  }
  
  // Starts with uploads/ (no leading slash)
  if (url.startsWith('uploads/')) {
    return `${MEDIA_BASE_URL}/${url}`;
  }
  
  // Any other absolute URL — return as-is
  if (url.startsWith('http')) {
    return url;
  }
  
  // Fallback: treat as relative path
  return `${MEDIA_BASE_URL}/uploads/${url}`;
}

/**
 * Get the media base URL for templates.
 */
export function getMediaBaseUrl(): string {
  return MEDIA_BASE_URL;
}
