import * as path from 'path';

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

const resolvePath = (dir: string) => path.resolve(__dirname, dir);

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      src: resolvePath('src'),
    },
  },
  server: {
    port: 3000,
    open: true,
  },
});
