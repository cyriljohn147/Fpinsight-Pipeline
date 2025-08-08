import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { resolve } from "path";

export default defineConfig({
  root: ".", // root is still current folder
  plugins: [react()],
  build: {
    rollupOptions: {
      input: resolve(__dirname, "public/index.html"), // tell Vite where HTML is
    },
  },
  server: {
    port: 5173,
    proxy: {
      "/presign": "http://localhost:8000",
      "/process": "http://localhost:8000",
      "/results": "http://localhost:8000",
      "/status": "http://localhost:8000",
    },
  },
});
