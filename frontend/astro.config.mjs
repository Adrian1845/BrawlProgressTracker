import { defineConfig } from 'astro/config';
import node from '@astrojs/node';

// Define server-side rendering output mode
export default defineConfig({
  output: 'server',
  adapter: node({ mode: 'standalone' })
});
