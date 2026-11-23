import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
// base "./" lets the built dist be served from any sub-path (e.g. python http.server on 127.0.0.1)
export default defineConfig({ plugins: [react()], base: "./", build: { outDir: "dist", sourcemap: false } });
