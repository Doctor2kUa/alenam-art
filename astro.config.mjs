import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://alenam.art',
  vite: {
    plugins: [tailwindcss()],
  },
  output: 'static',
});
