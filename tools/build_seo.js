#!/usr/bin/env node
/*
 * build_seo.js — makes the site crawlable by search engines. No dependencies, Node 14+.
 *
 *   node tools/build_seo.js https://your-domain.com
 *
 * What it does (safe to re-run any time; the output is deterministic):
 *   1. Generates one real static HTML page per lesson / program / coding problem
 *      (python-lessons/, dsa-lessons/, python-programs/, dsa-implementations/, coding-problems/).
 *   2. Rewrites the <head> SEO block (title, description, canonical, Open Graph, JSON-LD) of every root page.
 *   3. Pre-fills the listing pages with plain HTML links/content so crawlers see them without running JS.
 *   4. Writes sitemap.xml and robots.txt.
 *
 * Run it again after you change any lesson/program data, the site name, or the domain.
 */
const fs = require("fs"), path = require("path"), vm = require("vm");
const ROOT = path.resolve(__dirname, "..");
const SITE_NAME = "Python DSA Notes";
const SITE_URL = (process.argv[2] || process.env.SITE_URL || "https://YOUR-SITE-URL").replace(/\/+$/, "");
const TODAY = new Date().toISOString().slice(0, 10);
const OG = "assets/img/og-image.png";

/* ---------- load the site's data files into a sandbox ---------- */
const sb = { window: {} }; sb.window.window = sb.window; vm.createContext(sb);
const JS = ["data", "content", "lessons-python", "dsa-lessons", "dsa-structure-programs", "program-lessons", "program-lessons-stack",
  "program-lessons-advanced-stack", "program-lessons-dp", "program-lessons-bit", "program-lessons-patterns", "program-lessons-linked",
  "coding-problems", "interview-patterns", "interview-python", "interview-dsa", "interview-django", "interview-hr"];
JS.forEach(f => vm.runInContext(fs.readFileSync(path.join(ROOT, "assets/js", f + ".js"), "utf8"), sb, { filename: f }));
const W = sb.window;
const LESSONS = W.PYDSA_LESSONS, PY = W.PYDSA_PYTHON, DSAL = W.PYDSA_DSA_LESSONS, DSP = W.PYDSA_DSA_STRUCTURE_PROGRAMS;
const PROGS = W.PYDSA_PROGRAMS, GROUPS = W.PYDSA_GROUPS, PL = W.PYDSA_PROGRAM_LESSONS, ALIAS = W.PYDSA_PROGRAM_LESSON_ALIASES || {};
const CODING = W.PYDSA_CODING_PROBLEMS, PATTERNS = W.PYDSA_PATTERNS;
const IQ = { "python-interview": W.PYDSA_PYTHON_INTERVIEW, "dsa-interview": W.PYDSA_DSA_INTERVIEW, "django-interview": W.PYDSA_DJANGO_INTERVIEW, "hr-interview": W.PYDSA_HR_INTERVIEW };

/* ---------- helpers ---------- */
const esc = s => String(s == null ? "" : s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const fmt = t => esc(t).replace(/`([^`]+)`/g, "<code>$1</code>").replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>").replace(/\*([^*]+)\*/g, "<em>$1</em>").replace(/\n/g, "<br>");
const plain = t => String(t == null ? "" : t).replace(/[`*]/g, "").replace(/\s+/g, " ").trim();
const trunc = (s, n) => { s = plain(s); if (s.length <= n) return s; const cut = s.slice(0, n - 1); const sp = cut.lastIndexOf(" "); return (sp > n * 0.6 ? cut.slice(0, sp) : cut).replace(/[ ,;:.\-–—]+$/, "") + "…"; };
const writeFile = (rel, txt) => { const f = path.join(ROOT, rel); fs.mkdirSync(path.dirname(f), { recursive: true }); fs.writeFileSync(f, txt); };
const titleCase = s => s;
const pageTitle = t => (t.length > 52 ? t : t + " | " + SITE_NAME);
const abs = rel => SITE_URL + "/" + rel;
const sitemap = [];
const dirs = { py: "python-lessons", dsa: "dsa-lessons", prog: "python-programs", impl: "dsa-implementations", code: "coding-problems" };
const urlPy = id => dirs.py + "/" + id + ".html", urlDsa = id => dirs.dsa + "/" + id + ".html", urlProg = id => dirs.prog + "/" + id + ".html",
  urlImpl = id => dirs.impl + "/" + id + ".html", urlCode = id => dirs.code + "/" + id + ".html";

const codeBox = (name, src, noHl) => "<div class='code-box'><div class='code-header'><span>" + esc(name) + "</span><button class='copy-button' data-copy>Copy code</button></div><pre><code data-code" + (noHl ? " data-plain" : "") + ">" + esc(src) + "</code></pre></div>";
const outBox = (o, label) => o ? "<div class='out'><span>" + (label || "OUTPUT") + "</span><pre>" + esc(o) + "</pre></div>" : "";
const lineTable = (rows, h1, h2) => "<table class='lines'><thead><tr><th>" + h1 + "</th><th>" + h2 + "</th></tr></thead><tbody>" + rows.map(r => "<tr><td><code data-code>" + esc(r[0]) + "</code></td><td>" + fmt(r[1]) + "</td></tr>").join("") + "</tbody></table>";
const list = (a, cls) => "<ul class='" + (cls || "mist") + "'>" + a.map(x => "<li>" + fmt(x) + "</li>").join("") + "</ul>";
const qa = a => "<div class='qa'>" + a.map(q => "<details><summary>" + fmt(q[0]) + "</summary><p>" + fmt(q[1]) + "</p></details>").join("") + "</div>";
const sec = (n, h, inner, cls) => "<section class='ls" + (cls ? " " + cls : "") + "'><h2><i>" + n + "</i>" + h + "</h2>" + inner + "</section>";
const crumbs = a => "<div class='page-head' style='padding-bottom:10px'><div class='crumbs'>" + a.map((c, i) => (i ? "<span>/</span>" : "") + (c[1] ? "<a href='" + c[1] + "'>" + esc(c[0]) + "</a>" : "<span>" + esc(c[0]) + "</span>")).join("") + "</div></div>";
const btns = (doneKey, bmType, bmId, bmLabel, doneLabel) =>
  "<div class='drawer-actions' style='margin:18px 0'><button class='button button-small button-secondary done-btn' data-done='" + esc(doneKey) + "' data-done-label='" + esc(doneLabel) + "'>Mark as completed</button>" +
  "<button class='button button-small button-ghost bookmark-btn' data-bm='" + esc(bmType + ":" + bmId) + "' data-bm-label='" + esc(bmLabel) + "'>☆ " + esc(bmLabel) + "</button></div>";
const pn = (prev, next, hub) => "<footer class='lesson-foot'><div class='pn'>" +
  (prev ? "<a class='button button-ghost' href='" + prev[1] + "'>← " + esc(prev[0]) + "</a>" : "<a class='button button-ghost' href='" + hub[1] + "'>← " + esc(hub[0]) + "</a>") +
  (next ? "<a class='button button-primary' href='" + next[1] + "'>" + esc(next[0]) + " →</a>" : "<a class='button button-primary' href='" + hub[1] + "'>" + esc(hub[0]) + " →</a>") + "</div></footer>";

/* ---------- document shell ---------- */
function head(o) {
  const depth = o.path.split("/").length - 1, canon = abs(o.path === "index.html" ? "" : o.path);
  const t = o.rawTitle ? o.title : pageTitle(o.title), d = esc(trunc(o.desc, 158));
  let h = "<!--seo:head-start-->\n";
  if (depth) h += "  <base href='" + "../".repeat(depth) + "'>\n";
  h += "  <title>" + esc(t) + "</title>\n  <meta name=\"description\" content=\"" + d + "\">\n";
  h += o.noindex ? "  <meta name=\"robots\" content=\"noindex, follow\">\n" : "  <meta name=\"robots\" content=\"index, follow, max-image-preview:large\">\n  <link rel=\"canonical\" href=\"" + canon + "\">\n";
  h += "  <link rel=\"icon\" href=\"assets/img/favicon.svg\" type=\"image/svg+xml\">\n  <link rel=\"icon\" href=\"assets/img/favicon-48.png\" sizes=\"48x48\" type=\"image/png\">\n  <link rel=\"shortcut icon\" href=\"favicon.ico\">\n  <link rel=\"apple-touch-icon\" href=\"assets/img/apple-touch-icon.png\">\n";
  if (!o.noindex) {
    h += "  <meta property=\"og:type\" content=\"" + (o.ogType || "website") + "\">\n  <meta property=\"og:site_name\" content=\"" + SITE_NAME + "\">\n  <meta property=\"og:title\" content=\"" + esc(t) + "\">\n  <meta property=\"og:description\" content=\"" + d + "\">\n  <meta property=\"og:url\" content=\"" + canon + "\">\n  <meta property=\"og:image\" content=\"" + abs(OG) + "\">\n  <meta property=\"og:locale\" content=\"en\">\n";
    h += "  <meta name=\"twitter:card\" content=\"summary_large_image\">\n  <meta name=\"twitter:title\" content=\"" + esc(t) + "\">\n  <meta name=\"twitter:description\" content=\"" + d + "\">\n  <meta name=\"twitter:image\" content=\"" + abs(OG) + "\">\n";
    (o.ld || []).forEach(x => { h += "  <script type=\"application/ld+json\">" + JSON.stringify(x).replace(/</g, "\\u003c") + "</script>\n"; });
  }
  return h + "  <!--seo:head-end-->";
}
const crumbLd = (items) => ({ "@context": "https://schema.org", "@type": "BreadcrumbList", itemListElement: items.map((c, i) => ({ "@type": "ListItem", position: i + 1, name: c[0], item: abs(c[1]) })) });
const articleLd = (o) => ({ "@context": "https://schema.org", "@type": "TechArticle", headline: o.headline, description: trunc(o.desc, 158), url: abs(o.path), inLanguage: "en", isAccessibleForFree: true, image: abs(OG), dateModified: TODAY, about: o.about, publisher: { "@type": "Organization", name: SITE_NAME, url: abs("") }, mainEntityOfPage: abs(o.path) });

const SCRIPTS = ["data", "content", "lessons-python", "dsa-lessons", "dsa-structure-programs", "app", "static-page"];
function detailPage(o) {
  const html = "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n  <meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  " + head(o) +
    "\n  <meta name=\"theme-color\" content=\"#070b14\">\n  <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n  <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n  <link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap\" rel=\"stylesheet\">\n  <link rel=\"stylesheet\" href=\"assets/css/style.css\">\n</head>\n" +
    "<body data-page=\"" + o.bodyPage + "\">\n  <div id=\"site-header\"></div>\n  <main id=\"main\">\n" + o.main + "\n  </main>\n  <div id=\"site-footer\"></div>\n" +
    SCRIPTS.map(s => "  <script src=\"assets/js/" + s + ".js\"></script>").join("\n") + "\n</body>\n</html>\n";
  writeFile(o.path, html); sitemap.push(o.path);
}
const side = (title, items, activeId, mt) => "<span class='side-title'" + (mt ? " style='margin-top:14px'" : "") + ">" + esc(title) + "</span>" + items.map(x => "<a href='" + x.href + "'" + (x.id === activeId ? " class='active'" : "") + ">" + esc(x.title) + "</a>").join("");

/* ---------- 1. Python lessons ---------- */
LESSONS.forEach((L, i) => {
  const s = PY[L.section - 1], p = urlPy(L.id), prev = LESSONS[i - 1], next = LESSONS[i + 1];
  const desc = L.summary + " " + L.what, bc = [["Home", ""], ["Python", "python.html"], [L.title, p]];
  const sideHtml = PY.map((x, k) => side(x.n + " · " + x.title.split(" &")[0], LESSONS.filter(l => l.section === k + 1).map(l => ({ id: l.id, title: l.title, href: urlPy(l.id) })), L.id, k)).join("");
  let m = crumbs([["Home", "index.html"], ["Python", "python.html"], [s.title]]) + "<div class='with-side'><aside class='side' aria-label='Python lessons'>" + sideHtml + "</aside><article class='lesson'>" +
    "<header class='lesson-head'><div class='demo-row' style='margin:0 0 12px'><span class='badge badge-blue'>PYTHON</span><span class='badge badge-gray'>SECTION " + s.n + "</span><span class='badge badge-gray'>" + esc(L.time.toUpperCase()) + "</span></div><h1>" + esc(L.title) + "</h1><p class='lead'>" + fmt(L.summary) + "</p></header>" +
    btns("lesson-" + L.id, "lesson", L.id, "Bookmark lesson", "Lesson");
  m += sec(1, "What is it?", "<p>" + fmt(L.what) + "</p>") + sec(2, "Why do we need it?", "<p>" + fmt(L.why) + "</p>");
  let t = "<div class='explain'><div class='explain-tag'>Everyday example</div><p>" + fmt(L.simple) + "</p><div class='explain-tag'>Precise definition</div><p>" + fmt(L.tech) + "</p></div>";
  if (L.table) t += "<div class='table-wrap'><table class='ltable'><thead><tr>" + L.table.head.map(h => "<th>" + esc(h) + "</th>").join("") + "</tr></thead><tbody>" + L.table.rows.map(r => "<tr>" + r.map((c, k) => "<td>" + (k === 0 || /[\[\](){}=]/.test(c) ? "<code>" + esc(c) + "</code>" : esc(c)) + "</td>").join("") + "</tr>").join("") + "</tbody></table></div>";
  if (L.steps) t += "<ol class='steps-list' style='grid-template-columns:1fr;margin-top:14px'>" + L.steps.map(x => "<li>" + fmt(x) + "</li>").join("") + "</ol>";
  m += sec(3, "In plain words", t);
  m += sec(4, "Code, step by step", L.blocks.map((b, n) => "<div class='block'><h3>" + esc(b.title) + "</h3>" + codeBox(b.plain ? "structure" : (b.noRun ? "example.py" : "lesson_" + (n + 1) + ".py"), b.code, b.plain) + outBox(b.output) +
    "<table class='lines'><thead><tr><th>Line</th><th>What it means</th></tr></thead><tbody>" + b.lines.map(r => "<tr><td><code" + (b.plain ? "" : " data-code") + ">" + esc(r[0]) + "</code></td><td>" + fmt(r[1]) + "</td></tr>").join("") + "</tbody></table></div>").join(""));
  m += sec(5, "Common mistakes", list(L.mistakes)) + sec(6, "When should I use it?", "<p>" + fmt(L.use) + "</p>") + sec(7, "Interview questions", qa(L.qa));
  const tr = L.tryit;
  m += sec(8, "Try it yourself", "<div class='try-card'><p>" + fmt(tr.task) + "</p><details><summary>Show hint</summary><div class='notice teal'><div><b>Hint:</b> " + fmt(tr.hint) + "</div></div></details><details><summary>Show solution</summary>" + codeBox("solution.py", tr.solution) + outBox(tr.output) + "</details></div>", "try");
  const rel = (L.related || []).map(r => PROGS.find(x => x.id === r)).filter(Boolean);
  if (rel.length) m += sec(9, "Practise with real programs", "<div class='tags'>" + rel.map(x => "<a class='tag done' href='" + urlProg(x.id) + "'>" + esc(x.title) + " →</a>").join("") + "</div>");
  m += pn(prev && [prev.title, urlPy(prev.id)], next && [next.title, urlPy(next.id)], ["All Python lessons", "python.html"]) + "</article></div>";
  detailPage({ path: p, title: L.title + " — Python Tutorial for Beginners", desc, bodyPage: "python", main: m, ogType: "article",
    ld: [crumbLd(bc), articleLd({ path: p, headline: L.title + " — Python tutorial", desc, about: "Python programming" })] });
});

/* ---------- 2. DSA roadmap lessons ---------- */
DSAL.forEach((L, i) => {
  const p = urlDsa(L.id), prev = DSAL[i - 1], next = DSAL[i + 1], bc = [["Home", ""], ["DSA roadmap", "dsa.html"], [L.title, p]];
  const levels = {}; DSAL.forEach(x => (levels[x.level] = levels[x.level] || []).push(x));
  const sideHtml = Object.keys(levels).sort((a, b) => a - b).map(l => side("LEVEL " + l, levels[l].map(x => ({ id: x.id, title: x.title, href: urlDsa(x.id) })), L.id, l > 0)).join("");
  let m = crumbs([["Home", "index.html"], ["DSA roadmap", "dsa.html"], ["Level " + L.level]]) + "<div class='with-side'><aside class='side' aria-label='DSA lessons'>" + sideHtml + "</aside><article class='lesson'>" +
    "<header class='lesson-head'><div class='demo-row' style='margin:0 0 12px'><span class='badge badge-teal'>DSA</span><span class='badge badge-gray'>LEVEL " + L.level + "</span><span class='badge badge-gray'>" + esc(String(L.difficulty).toUpperCase()) + "</span></div><h1>" + esc(L.title) + " in Python</h1><p class='lead'>" + fmt(L.summary) + "</p></header>" +
    btns("dsa-lesson-" + L.id, "dsa-lesson", L.id, "Bookmark lesson", "Lesson");
  m += sec(1, "What is it?", "<p>" + fmt(L.what) + "</p>") + sec(2, "Why do we need it?", "<p>" + fmt(L.why) + "</p>");
  m += sec(3, "How it works", "<div class='explain'><div class='explain-tag'>Everyday idea</div><p>" + fmt(L.simple) + "</p><div class='explain-tag'>Technical view</div><p>" + fmt(L.tech) + "</p></div><ol class='steps-list' style='grid-template-columns:1fr;margin-top:14px'>" + L.steps.map(x => "<li>" + fmt(x) + "</li>").join("") + "</ol>");
  m += sec(4, "Python code, step by step", codeBox("example.py", L.code) + outBox(L.output, "OUTPUT / RESULT") + lineTable(L.lines, "Code", "What it means"));
  m += sec(5, "Common mistakes", list(L.mistakes)) + sec(6, "When should I use it?", "<p>" + fmt(L.use) + "</p>") + sec(7, "Interview questions", qa(L.qa));
  m += sec(8, "Try it yourself", "<div class='try-card'><p>" + fmt(L.practice) + "</p><details><summary>Show hint</summary><div class='notice teal'><div><b>Hint:</b> " + fmt(L.hint) + "</div></div></details><details><summary>Show solution</summary>" + codeBox("solution.py", L.solution) + "</details></div>", "try");
  const rel = (L.related || []).map(r => PROGS.find(x => x.id === r)).filter(Boolean);
  if (rel.length) m += sec(9, "Practise with real programs", "<div class='tags'>" + rel.map(x => "<a class='tag done' href='" + urlProg(x.id) + "'>" + esc(x.title) + " →</a>").join("") + "</div>");
  const deep = DSP.filter(x => (L.deepPrograms || []).indexOf(x.id) > -1);
  if (deep.length) m += sec(10, "Deep implementation library", "<div class='tags'>" + deep.map(x => "<a class='tag done' href='" + urlImpl(x.id) + "'>" + esc(x.title) + " →</a>").join("") + "</div>");
  m += pn(prev && [prev.title, urlDsa(prev.id)], next && [next.title, urlDsa(next.id)], ["DSA roadmap", "dsa.html"]) + "</article></div>";
  detailPage({ path: p, title: L.title + " in Python — DSA Tutorial with Code", desc: L.summary + " " + L.what, bodyPage: "dsa", main: m, ogType: "article",
    ld: [crumbLd(bc), articleLd({ path: p, headline: L.title + " in Python — DSA tutorial", desc: L.summary + " " + L.what, about: "Data structures and algorithms" })] });
});

/* ---------- 3. Interview programs ---------- */
PROGS.forEach((pr, i) => {
  const p = urlProg(pr.id), g = GROUPS.find(x => x.slug === pr.group) || { label: "Programs" }, L = PL[pr.id] || PL[ALIAS[pr.id]];
  const same = PROGS.filter(x => x.group === pr.group), bc = [["Home", ""], ["Programs", "programs.html"], [pr.title, p]];
  const sameIdea = pr.topic ? PROGS.filter(x => x.topic === pr.topic && x.id !== pr.id) : [];
  const prev = PROGS[i - 1], next = PROGS[i + 1];
  let m = crumbs([["Home", "index.html"], ["Programs", "programs.html"], [g.label]]) + "<div class='with-side'><aside class='side' aria-label='" + esc(g.label) + "'>" + side(g.label, same.map(x => ({ id: x.id, title: x.title, href: urlProg(x.id) })), pr.id) + "</aside><article class='lesson'>" +
    "<header class='lesson-head'><div class='demo-row' style='margin:0 0 12px'><span class='badge badge-" + (g.accent || "blue") + "'>" + esc(g.label.toUpperCase()) + "</span><span class='badge badge-gray'>" + esc(String(pr.difficulty).toUpperCase()) + "</span></div><h1>" + esc(pr.title) + " in Python</h1>" +
    "<p class='lead'>" + (L ? fmt(L.what) : "A complete Python program with code and expected output.") + "</p></header>" + btns(pr.id, "program", pr.id, "Bookmark", "Program");
  m += sec(1, "Python program", codeBox("program_" + pr.n + ".py", pr.code));
  if (L) {
    m += sec(2, "Why it matters", "<p>" + fmt(L.why) + "</p><div class='explain'><div class='explain-tag'>Simple example</div><p>" + fmt(L.example) + "</p></div>");
    m += sec(3, "How it works", "<ol class='steps-list' style='grid-template-columns:1fr;margin-top:6px'>" + L.approach.map(x => "<li>" + fmt(x) + "</li>").join("") + "</ol>");
    m += sec(4, "Line-by-line meaning", lineTable(L.lineByLine, "Code", "What it means"));
    m += sec(5, "Dry run", lineTable(L.dryRun, "Step", "What happens").replace(/<code data-code>/g, "<code>"));
    m += sec(6, "Time and space complexity", "<p><strong>Time:</strong> " + fmt(L.complexity.time) + "</p><p><strong>Space:</strong> " + fmt(L.complexity.space) + "</p>");
    m += sec(7, "Common mistakes", list(L.mistakes)) + sec(8, "When to use it (and when not to)", "<p><strong>Use it when:</strong> " + fmt(L.useWhen) + "</p><p><strong>Avoid it when:</strong> " + fmt(L.avoidWhen) + "</p>");
    m += sec(9, "Interview questions to expect", list(L.interview, "mist")) + sec(10, "Try it yourself", list(L.practice), "try");
  }
  if (sameIdea.length) m += sec(L ? 11 : 2, "Same idea, different implementation", "<div class='tags'>" + sameIdea.map(x => "<a class='tag done' href='" + urlProg(x.id) + "'>" + esc(x.title) + " →</a>").join("") + "</div>");
  m += pn(prev && [prev.title, urlProg(prev.id)], next && [next.title, urlProg(next.id)], ["All programs", "programs.html"]) + "</article></div>";
  const desc = L ? "Python program to " + pr.title.charAt(0).toLowerCase() + pr.title.slice(1) + ". " + L.what : "Python program: " + pr.title + ". Full code with expected output.";
  detailPage({ path: p, title: pr.title + " in Python — Program, Explanation & Dry Run", desc, bodyPage: "programs", main: m, ogType: "article",
    ld: [crumbLd(bc), articleLd({ path: p, headline: pr.title + " in Python", desc, about: g.label })] });
});

/* ---------- 4. Tree & graph implementations ---------- */
DSP.forEach((P, i) => {
  const p = urlImpl(P.id), same = DSP.filter(x => x.category === P.category), prev = DSP[i - 1], next = DSP[i + 1], bc = [["Home", ""], ["DSA roadmap", "dsa.html"], ["Tree & graph programs", "dsa-programs.html"], [P.title, p]];
  let m = crumbs([["Home", "index.html"], ["DSA roadmap", "dsa.html"], ["Tree & graph programs", "dsa-programs.html"], [P.category]]) + "<div class='with-side'><aside class='side' aria-label='" + esc(P.category) + "'>" + side(P.category, same.map(x => ({ id: x.id, title: x.title, href: urlImpl(x.id) })), P.id) + "</aside><article class='lesson'>" +
    "<header class='lesson-head'><div class='demo-row' style='margin:0 0 12px'><span class='badge badge-teal'>" + esc(P.category.toUpperCase()) + "</span><span class='badge badge-gray'>" + esc(String(P.difficulty).toUpperCase()) + "</span></div><h1>" + esc(P.title) + " in Python</h1><p class='lead'>" + fmt(P.concept) + "</p></header>" +
    btns("dsa-structure-program-" + P.id, "dsa-structure-program", P.id, "Bookmark program", "Program");
  m += sec(1, "Why this matters", "<p>" + fmt(P.why) + "</p><div class='explain'><div class='explain-tag'>Approach</div><p>" + fmt(P.approach) + "</p></div>");
  m += sec(2, "Python implementation", codeBox("Python", P.code)) + sec(3, "Expected output", outBox(P.output, "OUTPUT / RESULT"));
  m += sec(4, "Line by line", lineTable(P.lines, "Code", "Meaning")) + sec(5, "Dry run", "<div class='explain'><p>" + fmt(P.dryRun) + "</p></div>");
  m += sec(6, "Complexity", "<p>" + fmt(P.complexity) + "</p>") + sec(7, "Common mistakes", list(P.mistakes)) + sec(8, "When to use it", "<p>" + fmt(P.useWhen) + "</p>");
  m += sec(9, "Interview questions", qa(P.interview)) + sec(10, "Try it yourself", "<div class='try-card'><p>" + fmt(P.practice) + "</p></div>", "try");
  m += pn(prev && [prev.title, urlImpl(prev.id)], next && [next.title, urlImpl(next.id)], ["Tree & graph programs", "dsa-programs.html"]) + "</article></div>";
  const desc = P.title + " in Python: " + P.concept + " " + P.why;
  detailPage({ path: p, title: P.title + " in Python — Code, Output & Complexity", desc, bodyPage: "dsa", main: m, ogType: "article",
    ld: [crumbLd(bc), articleLd({ path: p, headline: P.title + " in Python", desc, about: P.category })] });
});

/* ---------- 5. Coding problems (generic renderer: fields vary in shape) ---------- */
function val(x) {
  if (x == null || x === "") return "";
  if (typeof x === "string") return "<p>" + fmt(x) + "</p>";
  if (Array.isArray(x)) {
    if (x.length && Array.isArray(x[0])) return lineTable(x, "Step", "What happens").replace(/<code data-code>/g, "<code>");
    return list(x.map(String));
  }
  return "<dl>" + Object.keys(x).map(k => "<dt><strong>" + esc(k) + "</strong></dt><dd>" + fmt(typeof x[k] === "string" ? x[k] : JSON.stringify(x[k])) + "</dd>").join("") + "</dl>";
}
CODING.forEach((c, i) => {
  const p = urlCode(c.id), prev = CODING[i - 1], next = CODING[i + 1], bc = [["Home", ""], ["Coding problems", "coding-problems.html"], [c.title, p]];
  let m = crumbs([["Home", "index.html"], ["Interview prep", "interview.html"], ["Coding problems", "coding-problems.html"], [c.title]]) + "<div class='with-side'><aside class='side' aria-label='Coding problems'>" + side("Problems", CODING.map(x => ({ id: x.id, title: x.title, href: urlCode(x.id) })), c.id) + "</aside><article class='lesson'>" +
    "<header class='lesson-head'><div class='demo-row' style='margin:0 0 12px'><span class='badge badge-orange'>" + esc(c.category.toUpperCase()) + "</span><span class='badge badge-gray'>" + esc(String(c.difficulty).toUpperCase()) + "</span><span class='badge badge-gray'>" + esc(c.pattern.toUpperCase()) + "</span></div><h1>" + esc(c.title) + " — Python Solution</h1><p class='lead'>" + fmt(c.understand) + "</p></header>" +
    btns("coding-" + c.id, "coding", c.id, "Bookmark problem", "Problem");
  let n = 0; const add = (h, inner) => { if (inner) m += sec(++n, h, inner); };
  add("How to recognise it", val(c.signal)); add("Key idea", val(c.idea)); add("Approach, step by step", Array.isArray(c.steps) ? "<ol class='steps-list' style='grid-template-columns:1fr;margin-top:6px'>" + c.steps.map(x => "<li>" + fmt(x) + "</li>").join("") + "</ol>" : val(c.steps));
  add("Python solution", c.code ? codeBox("solution.py", c.code) : ""); add("Dry run", val(c.dry)); add("Time and space complexity", val(c.complexity));
  add("Common mistakes", val(c.mistakes)); add("Interview follow-ups", val(c.interview)); add("Practice", val(c.practice));
  m += pn(prev && [prev.title, urlCode(prev.id)], next && [next.title, urlCode(next.id)], ["All coding problems", "coding-problems.html"]) + "</article></div>";
  const desc = c.title + " Python solution (" + c.difficulty + "): " + c.understand + " " + c.idea;
  detailPage({ path: p, title: c.title + " — Python Solution, Approach & Complexity", desc, bodyPage: "interview", main: m, ogType: "article",
    ld: [crumbLd(bc), articleLd({ path: p, headline: c.title + " Python solution", desc, about: c.category })] });
});

/* ---------- 6. Root pages: head block + crawlable pre-fill ---------- */
const mapOld = u => { // old dynamic URLs -> new static URLs
  let m;
  if ((m = u.match(/^dsa-lesson\.html\?id=([\w-]+)$/))) return urlDsa(m[1]);
  if ((m = u.match(/^dsa-structure-program\.html\?id=([\w-]+)$/))) return urlImpl(m[1]);
  return u;
};
const ul = items => "<ul>" + items.map(x => "<li><a href='" + x[0] + "'>" + esc(x[1]) + "</a>" + (x[2] ? " — " + esc(x[2]) : "") + "</li>").join("") + "</ul>";
const wrap = (intro, body) => "<!--seo:start--><section class='seo-static' id='seo-static'>" + (intro ? "<p>" + esc(intro) + "</p>" : "") + body + "</section><!--seo:end-->";
const faq = (arr) => arr.map(x => "<h3>" + esc(x.q) + "</h3><p>" + fmt(x.a) + "</p>" + (x.tip ? "<p><em>Tip:</em> " + fmt(x.tip) + "</p>" : "")).join("");

const ROOT_PAGES = {
  "index.html": { title: "Python DSA Notes — Free Python & DSA Tutorials with Interview Programs", rawTitle: true,
    desc: "Learn Python and data structures & algorithms (DSA) for free: plain-language lessons, " + PROGS.length + " interview programs with dry runs, a roadmap and interview questions. No login.",
    ld: [{ "@context": "https://schema.org", "@type": "WebSite", name: SITE_NAME, url: abs(""), inLanguage: "en", description: "Free Python and DSA tutorials, interview programs and practice." }] },
  "python.html": { title: "Python Tutorial for Beginners — " + LESSONS.length + " Lessons from Basics to OOP",
    desc: "Free Python tutorial: data types, loops, functions, lambda, OOP, file handling, exceptions and modules. Every lesson has line-by-line code, output and interview questions.",
    fill: () => wrap("", PY.map((s, k) => "<h2>" + esc(s.title) + "</h2><p>" + esc(s.blurb) + "</p>" + ul(LESSONS.filter(l => l.section === k + 1).map(l => [urlPy(l.id), l.title, l.summary]))).join("")) },
  "programs.html": { title: "Python Interview Programs — " + PROGS.length + " Programs with Code & Dry Run",
    desc: "Most-asked Python interview programs with code, output and dry run: arrays, strings, recursion, sorting, linked lists, stack, queue, dynamic programming, bit manipulation and patterns.",
    fill: () => wrap("", GROUPS.map(g => "<h2>" + esc(g.label) + "</h2><p>" + esc(g.blurb) + "</p>" + ul(PROGS.filter(p => p.group === g.slug).map(p => [urlProg(p.id), p.title + " in Python"]))).join("")) },
  "dsa.html": { title: "DSA Roadmap in Python — Data Structures & Algorithms Learning Path",
    desc: "A step-by-step data structures and algorithms roadmap in Python: arrays, linked lists, stack, queue, trees, graphs, recursion, sorting, searching and dynamic programming.",
    fill: () => wrap("", W.PYDSA_DSA.map(l => "<h2>Level " + l.level + ": " + esc(l.title) + "</h2><p>" + esc(l.blurb) + "</p>" + ul(l.items.map(it => [mapOld(it.u), it.t]))).join("")) },
  "dsa-programs.html": { title: "Tree & Graph Programs in Python — BST, AVL, BFS, DFS, Dijkstra",
    desc: "Python implementations of trees and graphs: traversals, BST, AVL rotation, BFS, DFS, Dijkstra, Kruskal, Prim, topological sort. Code, output, dry run and complexity.",
    fill: () => wrap("", [...new Set(DSP.map(x => x.category))].map(c => "<h2>" + esc(c) + "</h2>" + ul(DSP.filter(x => x.category === c).map(x => [urlImpl(x.id), x.title + " in Python", x.concept]))).join("")) },
  "interview.html": { title: "Python & DSA Interview Preparation — Questions, Patterns & Coding Problems",
    desc: "Interview prep hub: Python, DSA, Django and HR questions with model answers, problem-solving patterns and coding problems with Python solutions.",
    fill: () => wrap("", "<h2>Question banks</h2>" + ul(W.PYDSA_INTERVIEW.map(x => [x.u, x.title, x.blurb])) + "<h2>Practice</h2>" + ul([["patterns.html", "Problem-solving patterns"], ["coding-problems.html", "Coding problems with Python solutions"]])) },
  "patterns.html": { title: "Problem-Solving Patterns for Coding Interviews — Two Pointers, Sliding Window",
    desc: "Learn the coding-interview patterns that solve most problems: two pointers, sliding window, prefix sum, binary search, DFS/BFS and more, with Python code.",
    fill: () => wrap("", PATTERNS.map(x => "<h2>" + esc(x.title) + "</h2><p><strong>When to use:</strong> " + fmt(x.signal) + "</p><p>" + fmt(x.idea) + "</p>").join("")) },
  "coding-problems.html": { title: "Coding Interview Problems with Python Solutions — Easy to Hard",
    desc: "Classic coding interview problems (Two Sum, Valid Parentheses and more) with approach, Python solution, dry run and complexity.",
    fill: () => wrap("", ul(CODING.map(c => [urlCode(c.id), c.title + " — Python solution", c.difficulty + " · " + c.category]))) },
  "python-interview.html": { title: "Python Interview Questions and Answers (" + IQ["python-interview"].length + " Questions)", desc: "Common Python interview questions with clear model answers and tips: data types, functions, OOP, exceptions, files and more.", fill: () => wrap("", faq(IQ["python-interview"])) },
  "dsa-interview.html": { title: "DSA Interview Questions and Answers (" + IQ["dsa-interview"].length + " Questions)", desc: "Data structures and algorithms interview questions with model answers: Big O, arrays, linked lists, stacks, trees, graphs, sorting and dynamic programming.", fill: () => wrap("", faq(IQ["dsa-interview"])) },
  "django-interview.html": { title: "Django & Web Interview Questions and Answers (" + IQ["django-interview"].length + " Questions)", desc: "Django and web development interview questions with answers: MVT, ORM, models, forms, authentication, REST and deployment basics.", fill: () => wrap("", faq(IQ["django-interview"])) },
  "hr-interview.html": { title: "HR & Behavioural Interview Questions with Sample Answers", desc: "Common HR and behavioural interview questions with answer frameworks and tips: tell me about yourself, strengths, weaknesses, conflict and teamwork.", fill: () => wrap("", faq(IQ["hr-interview"])) },
};
const DYNAMIC = { "lesson.html": { ids: LESSONS.map(l => l.id), to: dirs.py }, "dsa-lesson.html": { ids: DSAL.map(l => l.id), to: dirs.dsa }, "dsa-structure-program.html": { ids: DSP.map(l => l.id), to: dirs.impl } };

Object.keys(ROOT_PAGES).concat(Object.keys(DYNAMIC), ["404.html"]).forEach(file => {
  let src = fs.readFileSync(path.join(ROOT, file), "utf8");
  const cfg = ROOT_PAGES[file], dyn = DYNAMIC[file];
  let block;
  if (cfg) block = head({ path: file, title: cfg.title, rawTitle: cfg.rawTitle, desc: cfg.desc, ld: (cfg.ld || []).concat(file === "index.html" ? [] : [crumbLd([["Home", ""], [cfg.title.split(" — ")[0], file]])]) });
  else block = head({ path: file, title: file === "404.html" ? "Page not found — " + SITE_NAME : "Loading… — " + SITE_NAME, rawTitle: true, desc: "Free Python and DSA tutorials, interview programs and practice.", noindex: true });
  // remove old head items, then insert the block (idempotent)
  src = src.replace(/<!--seo:head-start-->[\s\S]*?<!--seo:head-end-->\s*/g, "")
    .replace(/<title>[\s\S]*?<\/title>\s*/g, "").replace(/<meta name="description"[^>]*>\s*/g, "")
    .replace(/<link rel="icon"[^>]*>\s*/g, "").replace(/<link rel="apple-touch-icon"[^>]*>\s*/g, "");
  if (/<meta name="viewport"[^>]*>/.test(src)) src = src.replace(/(<meta name="viewport"[^>]*>)/, "$1\n  " + block.replace(/\$/g, "$$$$"));
  else throw new Error("no viewport meta in " + file);
  if (cfg && cfg.fill) src = src.replace(/<div id="content">(?:<!--seo:start-->[\s\S]*?<!--seo:end-->)?<\/div>/, () => "<div id=\"content\">" + cfg.fill() + "</div>");
  if (dyn) { // old ?id= URLs forward to the static page
    src = src.replace(/<script>\/\*seo-redirect\*\/[\s\S]*?<\/script>\s*/g, "");
    const r = "<script>/*seo-redirect*/(function(){var ok=" + JSON.stringify(dyn.ids.reduce((o, k) => (o[k] = 1, o), {})) + ",id=new URLSearchParams(location.search).get('id');if(id&&ok[id])location.replace('" + dyn.to + "/'+id+'.html');})();</script>\n";
    src = src.replace(/<\/head>/, r + "</head>");
  }
  if (file !== "404.html" && file !== "index.html" && !cfg === false) sitemap.push(file);
  if (file === "index.html") sitemap.unshift("");
  writeFile(file, src);
});

/* ---------- 7. sitemap.xml + robots.txt ---------- */
const uniq = [...new Set(sitemap)];
writeFile("sitemap.xml", "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n" +
  uniq.map(u => "  <url><loc>" + abs(u) + "</loc><lastmod>" + TODAY + "</lastmod></url>").join("\n") + "\n</urlset>\n");
writeFile("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: " + abs("sitemap.xml") + "\n");
console.log("Site:", SITE_URL, "\nStatic pages generated:", uniq.length, "(sitemap entries)");
if (/YOUR-SITE-URL/.test(SITE_URL)) console.log("\nNOTE: SITE_URL is still the placeholder. Re-run with your real address:\n  node tools/build_seo.js https://your-domain.com");
