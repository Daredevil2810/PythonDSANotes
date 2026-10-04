# Python DSA Notes — free Python & DSA tutorials

Static learning/reference site for Python, DSA, algorithms and interview preparation. The project uses HTML + CSS + vanilla JavaScript and remains deployable as a static site on GitHub Pages or Cloudflare Pages.

## Current status

- **91 Python programs** across **10 groups**
- **90 unique educational program concepts**
- Intentional canonical/alias handling for repeated concepts
- Learning walkthroughs cover all program concepts
- Problem-solving pattern library
- Coding-problem library with 30 problems
- Python, DSA and Django/Web interview libraries
- HR & behavioural interview library
- Python fundamentals currently include **17 generated lessons**
- No backend or framework is required

## Pages

`index.html` (home) · `python.html` · `programs.html` · `lesson.html` · `dsa.html` · `interview.html` · `patterns.html` · `coding-problems.html` · `dsa-interview.html` · `python-interview.html` · `django-interview.html` · `hr-interview.html` · `404.html`

## Where things live

- `assets/js/data.js` – 91 program records and 10 groups (**auto-generated; do not edit by hand**)
- `assets/js/content.js` – Python modules, DSA roadmap, interview categories
- `assets/js/app.js` – shared navigation/footer, theme, search, progress and program viewer behavior
- `assets/js/sections.js` – Python/DSA/interview section rendering
- `assets/js/lesson.js` – Python lesson-page rendering
- `assets/js/lessons-python.js` – generated Python lesson data
- `assets/js/program-lessons.js` – canonical program lessons
- `assets/js/program-lessons-stack.js` – Stack & Queue lessons
- `assets/js/program-lessons-advanced-stack.js` – Advanced Stack & Queue lessons
- `assets/js/program-lessons-linked.js` – Linked List lessons
- `assets/js/program-lessons-dp.js` – Dynamic Programming lessons
- `assets/js/program-lessons-bit.js` – Bit Manipulation lessons
- `assets/js/program-lessons-patterns.js` – Pattern Printing lessons
- `tools/source_programs/` – original Python programs; treat these as canonical source material
- `tools/build_data.py` – regenerates `assets/js/data.js` from the source-program folders
- `tools/lessons/build_lessons.py` – validates and regenerates the Python lesson registry
- `tools/audit.py` – static static project audit

## Program-learning architecture

Program metadata/code is generated separately from the educational layer. This means `data.js` can be regenerated without overwriting the hand-written structured explanations.

A repeated program concept can point to a canonical lesson instead of duplicating the same educational material. The current 91-program set therefore intentionally contains 90 unique learning concepts.

## Validation

From the project root:

```bash
python3 tools/build_data.py
python3 tools/lessons/build_lessons.py
python3 tools/audit.py
```

The expected data-generation result is:

```text
91 programs, 10 groups
missing code: []
```

The JavaScript files can also be syntax-checked with:

```bash
node --check assets/js/app.js
```

Run `node --check` against all JavaScript files when making broader JS changes.

## Add a program

Add the `.py` file to the appropriate folder in `tools/source_programs/`, add its entry to that folder's `Index.txt`, then run:

```bash
python3 tools/build_data.py
```

Do not manually edit generated `data.js`.

## Python lessons

The Python fundamentals lesson data is maintained in `tools/lessons/part1.py` and `part2.py`.

Run:

```bash
python3 tools/lessons/build_lessons.py
```

The builder executes the runnable lesson examples, checks their expected output, and writes `assets/js/lessons-python.js`.

Lesson pages use:

```text
lesson.html?id=<lesson-id>
```

## Deployment

Push this folder to a repository and deploy the repository root with GitHub Pages or Cloudflare Pages. `.nojekyll` is included for GitHub Pages compatibility.

## Maintenance principles

- Preserve the static HTML/CSS/JS architecture unless a real technical requirement says otherwise.
- Do not modify original source programs merely to improve lesson wording.
- Keep generated data generated.
- Prefer extending the existing lesson registries over creating duplicate content.
- Validate changes before packaging a release.

## SEO build (run after changing content or your domain)

The lesson/program data lives in JavaScript, so search engines would see empty pages. `tools/build_seo.js` generates real static HTML for every lesson, program and coding problem, plus the `<head>` SEO tags, `sitemap.xml` and `robots.txt`:

```bash
node tools/build_seo.js https://your-domain.com
```

- Generated folders: `python-lessons/`, `dsa-lessons/`, `python-programs/`, `dsa-implementations/`, `coding-problems/` (do not edit by hand; re-run the script).
- Old `lesson.html?id=…` style links still work: they redirect to the new static page.
- Site name is the `SITE_NAME` constant at the top of the script and the brand text in `assets/js/app.js`.
- Progress/bookmarks keep the internal `pydsa:` localStorage prefix on purpose, so existing users do not lose their progress.
- Submit `sitemap.xml` in Google Search Console and Bing Webmaster Tools.
