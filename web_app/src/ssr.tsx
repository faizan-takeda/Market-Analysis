// Server-side render entry used only by tests/render_smoke.mjs to prove every route renders against the generated datasets.
import { renderToString } from "react-dom/server";
import { StaticRouter } from "react-router-dom/server";
import type { Bundle } from "./data";
import { Body } from "./routes";

export function renderRoute(b: Bundle, path: string): string {
  return renderToString(<StaticRouter location={path}><Body b={b} open={() => {}} /></StaticRouter>);
}
