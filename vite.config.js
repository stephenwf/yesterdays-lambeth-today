import { defineConfig } from 'vite'
import { resolve } from 'path';
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  base: '/yesterdays-lambeth-today/',
  plugins: [react()],
  build: {
    rollupOptions: {
      input: {
        index: "./index.html",
        index_vite: "./index-vite.html",
        map: "./map.html",
      },
    }
  }
});
