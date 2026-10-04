/* Python DSA Notes — shared behaviour: layout injection, theme, search, progress, program drawer */
(function () {
  "use strict";
  var PROGRAMS = window.PYDSA_PROGRAMS || [], GROUPS = window.PYDSA_GROUPS || [];
  var PATTERNS = window.PYDSA_PATTERNS || [], CODING = window.PYDSA_CODING_PROBLEMS || [], LESSONS = window.PYDSA_LESSONS || [], DSALE = window.PYDSA_DSA_LESSONS || [], DSP = window.PYDSA_DSA_STRUCTURE_PROGRAMS || [], PY = window.PYDSA_PYTHON || [], DSA = window.PYDSA_DSA || [], INT = window.PYDSA_INTERVIEW || [], DSAIQ = window.PYDSA_DSA_INTERVIEW || [], PYIQ = window.PYDSA_PYTHON_INTERVIEW || [], DJIQ = window.PYDSA_DJANGO_INTERVIEW || [], HRIQ = window.PYDSA_HR_INTERVIEW || [];
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s).replace(/[&<>"']/g, function (c) { return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]; }); };
  var page = document.body.getAttribute("data-page") || "home";

  /* ---------- safe storage ---------- */
  var store = {
    get: function (k, d) { try { var v = localStorage.getItem("pydsa:" + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem("pydsa:" + k, JSON.stringify(v)); } catch (e) {} }
  };
  var done = store.get("done", {});
  var bookmarks = store.get("bookmarks", {});
  var isDone = function (id) { return !!done[id]; };
  var bookmarkKey = function (type, id) { return type + ":" + id; };
  var isBookmarked = function (type, id) { return !!bookmarks[bookmarkKey(type, id)]; };
  function toggleBookmark(type, id) {
    var k = bookmarkKey(type, id);
    if (bookmarks[k]) delete bookmarks[k];
    else bookmarks[k] = Date.now();
    store.set("bookmarks", bookmarks);
    document.dispatchEvent(new CustomEvent("pydsa:bookmarks"));
  }
  function bookmarkCount() { return Object.keys(bookmarks).length; }
  function getBookmarks() { return bookmarks; }
  function toggleDone(id) { if (done[id]) delete done[id]; else done[id] = Date.now(); store.set("done", done); store.set("last", id); }
  function doneCount(group) { return PROGRAMS.filter(function (p) { return isDone(p.id) && (!group || p.group === group); }).length; }

  /* ---------- theme ---------- */
  function applyTheme(t) { document.body.classList.toggle("light", t === "light"); var b = $("#themeToggle"); if (b) { b.textContent = t === "light" ? "☾" : "☼"; b.setAttribute("aria-label", t === "light" ? "Switch to dark mode" : "Switch to light mode"); } }
  var theme = store.get("theme", "dark");
  applyTheme(theme);

  /* ---------- toast ---------- */
  var toastTimer;
  function toast(msg) { var t = $(".toast"); if (!t) return; t.textContent = msg; t.classList.add("show"); clearTimeout(toastTimer); toastTimer = setTimeout(function () { t.classList.remove("show"); }, 1700); }

  /* ---------- layout injection (one place to edit nav + footer) ---------- */
  var NAV = [
    { id: "python", label: "Python", href: "python.html", sub: LESSONS.length + " lessons" },
    { id: "programs", label: "Programs", href: "programs.html", sub: PROGRAMS.length + " interview programs" },
    { id: "dsa", label: "DSA", href: "dsa.html", sub: "The learning roadmap" },
    { id: "interview", label: "Interview", href: "interview.html", sub: "Questions & prep" }
  ];
  function buildChrome() {
    var links = NAV.map(function (n) { return '<a href="' + n.href + '"' + (page === n.id ? ' class="active" aria-current="page"' : "") + ">" + n.label + "</a>"; }).join("");
    var mlinks = NAV.map(function (n) { return '<a href="' + n.href + '"' + (page === n.id ? ' class="active"' : "") + "><span>" + n.label + "</span><small>" + n.sub + "</small></a>"; }).join("");
    $("#site-header").outerHTML =
      '<a class="skip-link" href="#main">Skip to content</a>' +
      '<header class="navbar"><a class="brand" href="index.html" aria-label="Python DSA Notes home"><img class="brand-logo" src="assets/img/site-logo.png" alt="" width="36" height="36"><span>Python <span class="accent">DSA</span> Notes</span></a>' +
      '<nav class="nav-links" aria-label="Main">' + links + "</nav>" +
      '<div class="nav-actions"><button class="search-trigger" id="openSearch" aria-label="Search"><span aria-hidden="true">⌕</span><span>Search anything…</span><kbd>Ctrl K</kbd></button>' +
      '<button class="icon-button" id="themeToggle"></button><button class="icon-button menu-button" id="menuButton" aria-label="Open menu" aria-expanded="false">☰</button></div></header>' +
      '<nav class="mobile-menu" id="mobileMenu" aria-label="Mobile">' + '<a href="index.html"><span>Home</span><small>Start here</small></a>' + mlinks + "</nav>";
    $("#site-footer").outerHTML =
      '<footer class="footer"><div class="footer-grid"><div><a class="brand" href="index.html"><img class="brand-logo" src="assets/img/site-logo.png" alt="" width="36" height="36"><span>Python <span class="accent">DSA</span> Notes</span></a><p>Python DSA Notes: a free Python and data structures & algorithms learning hub. No login, no server, no sleeping backend. Your progress stays in your own browser.</p></div>' +
      '<div><h5>Learn</h5><ul><li><a href="python.html">Python</a></li><li><a href="dsa.html">DSA roadmap</a></li><li><a href="programs.html">Programs</a></li></ul></div>' +
      '<div><h5>Prepare</h5><ul><li><a href="interview.html">Interview prep</a></li><li><a href="patterns.html">Pattern practice</a></li><li><a href="coding-problems.html">Coding problems</a></li></ul></div>' +
      '<div><h5>Project</h5><ul><li><a href="index.html#roadmap">Roadmap</a></li><li><a href="index.html#progress">Your progress</a></li></ul></div></div>' +
      '<div class="footer-bottom"><span>Built while learning. Every explanation is written in plain language.</span><span>Learn · Practice · Prepare</span></div></footer>';
    document.body.insertAdjacentHTML("beforeend",
      '<div class="palette" id="palette" role="dialog" aria-modal="true" aria-label="Search"><div class="palette-box"><div class="palette-input"><span aria-hidden="true">⌕</span><input id="paletteInput" type="text" placeholder="Search Python, programs, DSA…" autocomplete="off" aria-label="Search"><kbd>Esc</kbd></div><div class="palette-list" id="paletteList" role="listbox"></div><div class="palette-foot"><span><kbd>↑</kbd> <kbd>↓</kbd> move</span><span><kbd>Enter</kbd> open</span><span><kbd>Esc</kbd> close</span></div></div></div>' +
      '<div class="scrim" id="scrim"></div><aside class="drawer" id="drawer" aria-hidden="true" aria-label="Program"></aside><div class="toast" role="status" aria-live="polite"></div>');
    applyTheme(theme);

    $("#themeToggle").addEventListener("click", function () { theme = document.body.classList.contains("light") ? "dark" : "light"; store.set("theme", theme); applyTheme(theme); });
    var mb = $("#menuButton"), mm = $("#mobileMenu");
    mb.addEventListener("click", function () { var o = mm.classList.toggle("open"); mb.setAttribute("aria-expanded", o); mb.textContent = o ? "✕" : "☰"; document.body.classList.toggle("no-scroll", o); });
    $("#openSearch").addEventListener("click", openSearch);
  }

  /* ---------- python syntax highlighter (tiny, single-pass) ---------- */
  var KW = /^(def|return|if|elif|else|for|while|in|not|and|or|is|None|True|False|class|import|from|as|break|continue|pass|lambda|try|except|finally|raise|with|yield|global|print_)$/;
  var BI = /^(print|len|range|int|str|float|list|dict|set|tuple|input|max|min|sum|abs|sorted|enumerate|zip|map|filter|bool|type|isinstance|append|pop|insert|reversed)$/;
  function highlight(src) {
    var re = /(#[^\n]*)|("""[\s\S]*?"""|'''[\s\S]*?'''|f?"(?:\\.|[^"\\\n])*"|f?'(?:\\.|[^'\\\n])*')|(\b\d+(?:\.\d+)?\b)|(\b[A-Za-z_]\w*\b)|([\s\S])/g, out = "", m, prevDef = false;
    while ((m = re.exec(src))) {
      if (m[1]) out += '<span class="tk-cm">' + esc(m[1]) + "</span>";
      else if (m[2]) out += '<span class="tk-str">' + esc(m[2]) + "</span>";
      else if (m[3]) out += '<span class="tk-num">' + m[3] + "</span>";
      else if (m[4]) {
        var w = m[4];
        if (prevDef) { out += '<span class="tk-fn">' + w + "</span>"; prevDef = false; }
        else if (KW.test(w)) { out += '<span class="tk-kw">' + w + "</span>"; prevDef = (w === "def" || w === "class"); }
        else if (BI.test(w)) out += '<span class="tk-bi">' + w + "</span>";
        else out += w;
      } else out += esc(m[5]);
    }
    return out;
  }
  window.PyDSA = { highlight: highlight, esc: esc };

  /* ---------- program drawer ---------- */
  var openId = null;
  function renderProgramLearning(p) {
    var lessons = window.PYDSA_PROGRAM_LESSONS || {};
    var aliases = window.PYDSA_PROGRAM_LESSON_ALIASES || {};
    var L = lessons[p.id] || lessons[aliases[p.id]];
    if (!L) return '<div class="notice teal drawer-note"><div><b>Code only.</b> This program has the full Python code and expected output.</div></div>';
    var steps = '<ol class="learning-steps">' + L.approach.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ol>';
    var dry = '<div class="dry-run"><div class="dry-run-head"><span>Step</span><span>What happens</span></div>' + L.dryRun.map(function (r) { return '<div class="dry-run-row"><b>' + esc(r[0]) + '</b><span>' + esc(r[1]) + '</span></div>'; }).join('') + '</div>';
    var lines = '<div class="line-guide">' + L.lineByLine.map(function (r) { return '<div class="line-guide-row"><code>' + esc(r[0]) + '</code><span>' + esc(r[1]) + '</span></div>'; }).join('') + '</div>';
    var mistakes = '<ul class="learning-list">' + L.mistakes.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>';
    var questions = '<ul class="learning-list interview-list">' + L.interview.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>';
    var practice = '<ul class="learning-list">' + L.practice.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>';
    return '<div class="learning-content" aria-label="Learning walkthrough">' +
      '<section class="learning-section"><div class="learning-eyebrow">CONCEPT</div><h4>What are we solving?</h4><p>' + esc(L.what) + '</p><div class="learning-callout"><b>Why it matters</b><p>' + esc(L.why) + '</p></div><div class="learning-callout example"><b>Simple example</b><p>' + esc(L.example) + '</p></div></section>' +
      '<section class="learning-section"><div class="learning-eyebrow">APPROACH</div><h4>How it works</h4>' + steps + '</section>' +
      '<section class="learning-section"><div class="learning-eyebrow">CODE GUIDE</div><h4>Line-by-line meaning</h4>' + lines + '</section>' +
      '<section class="learning-section"><div class="learning-eyebrow">DRY RUN</div><h4>Walk through an example</h4>' + dry + '</section>' +
      '<section class="learning-section"><div class="learning-eyebrow">COMPLEXITY</div><h4>Time &amp; space</h4><div class="complexity-grid"><div><span>Time</span><strong>' + esc(L.complexity.time) + '</strong></div><div><span>Space</span><strong>' + esc(L.complexity.space) + '</strong></div></div></section>' +
      '<section class="learning-section"><div class="learning-eyebrow">INTERVIEW</div><h4>Common mistakes</h4>' + mistakes + '<h4 class="subheading">Questions to expect</h4>' + questions + '</section>' +
      '<section class="learning-section"><div class="learning-eyebrow">PRACTICE</div><h4>Try it yourself</h4><p><b>When to use:</b> ' + esc(L.useWhen) + '</p><p><b>When not to use:</b> ' + esc(L.avoidWhen) + '</p>' + practice + '</section>' +
      '</div>';
  }
  function openProgram(id, push) {
    var p = PROGRAMS.filter(function (x) { return x.id === id; })[0]; if (!p) return;
    var g = GROUPS.filter(function (x) { return x.slug === p.group; })[0] || {};
    var same = p.topic ? PROGRAMS.filter(function (x) { return x.topic === p.topic && x.id !== p.id; }) : [];
    var d = $("#drawer"); openId = id;
    d.innerHTML =
      '<div class="drawer-head"><div><span class="badge badge-' + g.accent + '">' + esc(g.label.toUpperCase()) + '</span> <span class="difficulty ' + p.difficulty + '">' + p.difficulty + '</span><h3>' + esc(p.title) + '</h3></div><button class="icon-button" id="closeDrawer" aria-label="Close">✕</button></div>' +
      '<div class="drawer-body"><div class="drawer-actions"><button class="button button-small button-secondary done-btn ' + (isDone(id) ? 'is-done' : '') + '" id="doneBtn">' + (isDone(id) ? '✓ Completed' : 'Mark as completed') + '</button><button class="button button-small button-ghost bookmark-btn ' + (isBookmarked("program", id) ? 'is-bookmarked' : '') + '" id="bookmarkBtn" aria-pressed="' + isBookmarked("program", id) + '">' + (isBookmarked("program", id) ? '★ Bookmarked' : '☆ Bookmark') + '</button><a class="button button-small button-ghost" href="python-programs/' + esc(id) + '.html">Full page ↗</a><button class="button button-small button-ghost" id="prevP">← Prev</button><button class="button button-small button-ghost" id="nextP">Next →</button></div>' +
      '<div class="code-box"><div class="code-header"><span>program_' + esc(p.n) + '.py</span><button class="copy-button" id="copyCode">Copy code</button></div><pre><code>' + highlight(p.code) + '</code></pre></div>' +
      renderProgramLearning(p) +
      (same.length ? '<div class="notice drawer-note"><div><b>Same idea elsewhere:</b> ' + same.map(function (s) { return '<a class="accent" href="#" data-open="' + s.id + '">' + esc(s.title) + '</a>'; }).join(', ') + '. Compare these implementations to see how one idea can be solved in different ways.</div></div>' : '') +
      '</div>';
    d.classList.add('open'); d.setAttribute('aria-hidden', 'false'); $("#scrim").classList.add('open'); document.body.classList.add('no-scroll');
    $("#closeDrawer").addEventListener('click', closeProgram);
    $("#copyCode").addEventListener('click', function (e) { var b = e.currentTarget; (navigator.clipboard ? navigator.clipboard.writeText(p.code) : Promise.reject()).then(function () { b.textContent = 'Copied ✓'; }, function () { b.textContent = 'Select & copy'; }); setTimeout(function () { b.textContent = 'Copy code'; }, 1500); });
    $("#doneBtn").addEventListener('click', function (e) { toggleDone(id); var b = e.currentTarget, y = isDone(id); b.classList.toggle('is-done', y); b.textContent = y ? '✓ Completed' : 'Mark as completed'; toast(y ? 'Marked as completed' : 'Marked as not completed'); document.dispatchEvent(new CustomEvent('pydsa:progress')); });
    $("#bookmarkBtn").addEventListener('click', function (e) { toggleBookmark('program', id); var b = e.currentTarget, y = isBookmarked('program', id); b.classList.toggle('is-bookmarked', y); b.setAttribute('aria-pressed', y); b.textContent = y ? '★ Bookmarked' : '☆ Bookmark'; toast(y ? 'Program bookmarked' : 'Bookmark removed'); });
    var i = PROGRAMS.indexOf(p);
    $("#prevP").disabled = i === 0; $("#nextP").disabled = i === PROGRAMS.length - 1;
    $("#prevP").addEventListener('click', function () { openProgram(PROGRAMS[i - 1].id, true); });
    $("#nextP").addEventListener('click', function () { openProgram(PROGRAMS[i + 1].id, true); });
    $$('[data-open]', d).forEach(function (a) { a.addEventListener('click', function (e) { e.preventDefault(); openProgram(a.getAttribute('data-open'), true); }); });
    $(".drawer-body", d).scrollTop = 0; d.querySelector('#closeDrawer').focus();
    store.set('last', id);
    if (push !== false && location.hash.slice(1) !== id) history.replaceState(null, '', '#' + id);
  }
  window.PyDSA.openProgram = openProgram;

  function closeProgram() {
    var d = $("#drawer"); if (!d) return; d.classList.remove("open"); d.setAttribute("aria-hidden", "true"); $("#scrim").classList.remove("open");
    if (!$("#palette").classList.contains("open")) document.body.classList.remove("no-scroll");
    openId = null; if (/^#[a-z]+-/.test(location.hash) && PROGRAMS.some(function (p) { return "#" + p.id === location.hash; })) history.replaceState(null, "", location.pathname + location.search);
    document.dispatchEvent(new CustomEvent("pydsa:progress"));
  }
  window.PyDSA.openProgram = openProgram;

  /* ---------- search palette ---------- */
  var INDEX = [];
  PROGRAMS.forEach(function (p) { var g = GROUPS.filter(function (x) { return x.slug === p.group; })[0]; INDEX.push({ kind: "Program", title: p.title, sub: g.label, href: "programs.html#" + p.id, id: p.id, c: g.accent, hay: (p.title + " " + g.label).toLowerCase() }); });
  PY.forEach(function (m) { INDEX.push({ kind: "Python", title: m.title, sub: "Module 1 · Section " + m.n, href: "python.html#" + m.id, c: "blue", hay: (m.title + " " + m.topics.join(" ")).toLowerCase() }); m.topics.forEach(function (t) { INDEX.push({ kind: "Python", title: t, sub: m.title, href: "python.html#" + m.id, c: "blue", hay: (t + " " + m.title).toLowerCase() }); }); });
  LESSONS.forEach(function (l) { INDEX.push({ kind: "Lesson", title: l.title, sub: "Python · " + PY[l.section - 1].title, href: "lesson.html?id=" + l.id, c: "blue", hay: (l.title + " " + l.summary + " " + l.qa.map(function (q) { return q[0]; }).join(" ")).toLowerCase() }); });
  DSA.forEach(function (l) { l.items.forEach(function (it) { INDEX.push({ kind: "DSA", title: it.t, sub: "Level " + l.level + " · " + l.title, href: it.u || "dsa.html#level-" + l.level, c: "teal", hay: (it.t + " " + l.title).toLowerCase() }); }); });
  DSALE.forEach(function (l) { INDEX.push({ kind: "DSA Lesson", title: l.title, sub: "DSA · Level " + l.level, href: "dsa-lesson.html?id=" + l.id, c: "teal", hay: (l.title + " " + l.summary + " " + l.what).toLowerCase() }); });
  DSP.forEach(function (p) { INDEX.push({ kind: "DSA Program", title: p.title, sub: p.category + " · " + p.difficulty, href: "dsa-structure-program.html?id=" + p.id, c: "purple", hay: (p.title + " " + p.category + " " + p.concept + " " + p.why).toLowerCase() }); });
  INT.forEach(function (x) { INDEX.push({ kind: "Interview", title: x.title, sub: x.status, href: "interview.html#" + x.id, c: "orange", hay: (x.title + " " + x.blurb).toLowerCase() }); });
  DSAIQ.forEach(function (x) { INDEX.push({ kind: "DSA Interview", title: x.q, sub: x.category, href: "dsa-interview.html#dsa-interview-" + x.id, c: "teal", hay: (x.q + " " + x.a + " " + x.category).toLowerCase() }); });
  PYIQ.forEach(function (x) { INDEX.push({ kind: "Python Interview", title: x.q, sub: x.category, href: "python-interview.html#python-interview-" + x.id, c: "blue", hay: (x.q + " " + x.a + " " + x.category).toLowerCase() }); });
  DJIQ.forEach(function (x) { INDEX.push({ kind: "Django Interview", title: x.q, sub: x.category, href: "django-interview.html#django-interview-" + x.id, c: "blue", hay: (x.q + " " + x.a + " " + x.category).toLowerCase() }); });
  HRIQ.forEach(function (x) { INDEX.push({ kind: "HR Interview", title: x.q, sub: x.category, href: "hr-interview.html#hr-interview-" + x.id, c: "orange", hay: (x.q + " " + x.a + " " + x.category).toLowerCase() }); });
  PATTERNS.forEach(function (x) { INDEX.push({ kind: "Pattern", title: x.title, sub: x.level + " · " + x.difficulty, href: "patterns.html#" + x.id, c: "purple", hay: (x.title + " " + x.signal + " " + x.idea + " " + x.example).toLowerCase() }); });
  CODING.forEach(function (x) { INDEX.push({ kind: "Coding Problem", title: x.title, sub: x.difficulty + " · " + x.pattern, href: "coding-problems.html#problem-" + x.id, c: "orange", hay: (x.title + " " + x.category + " " + x.pattern + " " + x.signal).toLowerCase() }); });
  
  var results = [], sel = 0;

  function runSearch(q) {
    q = q.trim().toLowerCase(); var terms = q.split(/\s+/).filter(Boolean);
    var scored = [];
    INDEX.forEach(function (it) {
      if (!terms.length) { if (it.kind === "Lesson" && scored.length < 6) scored.push({ it: it, s: 0 }); return; }
      var s = 0, ok = true;
      terms.forEach(function (t) { var tl = it.title.toLowerCase(); if (tl === t) s += 100; else if (tl.indexOf(t) === 0) s += 60; else if (tl.indexOf(" " + t) > -1) s += 40; else if (tl.indexOf(t) > -1) s += 25; else if (it.hay.indexOf(t) > -1) s += 8; else ok = false; });
      if (ok) scored.push({ it: it, s: s });
    });
    scored.sort(function (a, b) { return b.s - a.s; });
    var seen = {}, out = [];
    scored.forEach(function (r) { var k = r.it.kind + r.it.title + r.it.href; if (!seen[k]) { seen[k] = 1; out.push(r.it); } });
    return out.slice(0, 30);
  }
  function mark(text, q) { var t = esc(text); q = q.trim().split(/\s+/)[0]; if (!q) return t; var i = text.toLowerCase().indexOf(q.toLowerCase()); return i < 0 ? t : esc(text.slice(0, i)) + "<mark>" + esc(text.slice(i, i + q.length)) + "</mark>" + esc(text.slice(i + q.length)); }
  function renderResults() {
    var q = $("#paletteInput").value, list = $("#paletteList"); results = runSearch(q); sel = 0;
    if (!results.length) { list.innerHTML = '<div class="empty" style="border:0">No match for “' + esc(q) + "”. Try a topic like <b>binary</b>, <b>palindrome</b> or <b>linked list</b>.</div>"; return; }
    var html = q.trim() ? "" : '<div class="palette-label">Suggested</div>', last = "";
    results.forEach(function (r, i) {
      if (q.trim() && r.kind !== last) { html += '<div class="palette-label">' + r.kind + "s</div>"; last = r.kind; }
      html += '<button class="palette-item" role="option" data-i="' + i + '" aria-selected="' + (i === 0) + '"><span class="badge badge-' + r.c + '">' + r.kind.toUpperCase() + '</span><span class="t">' + mark(r.title, q) + '</span><small style="color:var(--text-muted);font-size:11.5px">' + esc(r.sub) + "</small></button>";
    });
    list.innerHTML = html;
    $$(".palette-item", list).forEach(function (el) { el.addEventListener("click", function () { go(+el.getAttribute("data-i")); }); el.addEventListener("mousemove", function () { setSel(+el.getAttribute("data-i")); }); });
  }
  function setSel(i) { sel = i; $$(".palette-item").forEach(function (el, k) { el.setAttribute("aria-selected", k === i); if (k === i) el.scrollIntoView({ block: "nearest" }); }); }
  function go(i) {
    var r = results[i]; if (!r) return; closeSearch();
    var target = r.href.split("#")[0], here = location.pathname.split("/").pop() || "index.html";
    if (r.kind === "Program" && r.id && target === here) { openProgram(r.id); } else location.href = r.href;
  }
  function openSearch(prefill) { var p = $("#palette"); p.classList.add("open"); document.body.classList.add("no-scroll"); var inp = $("#paletteInput"); inp.value = typeof prefill === "string" ? prefill : ""; renderResults(); inp.focus(); }
  function closeSearch() { $("#palette").classList.remove("open"); if (!openId && !$("#mobileMenu").classList.contains("open")) document.body.classList.remove("no-scroll"); }
  window.PyDSA.openSearch = openSearch;

  function bindGlobal() {
    $("#paletteInput").addEventListener("input", renderResults);
    $("#palette").addEventListener("mousedown", function (e) { if (e.target.id === "palette") closeSearch(); });
    $("#scrim").addEventListener("click", closeProgram);
    document.addEventListener("keydown", function (e) {
      var pal = $("#palette").classList.contains("open");
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") { e.preventDefault(); pal ? closeSearch() : openSearch(); return; }
      if (e.key === "/" && !pal && !/INPUT|TEXTAREA|SELECT/.test((document.activeElement || {}).tagName || "")) { e.preventDefault(); openSearch(); return; }
      if (e.key === "Escape") { if (pal) closeSearch(); else if (openId) closeProgram(); return; }
      if (pal) {
        if (e.key === "ArrowDown") { e.preventDefault(); setSel(Math.min(sel + 1, results.length - 1)); }
        else if (e.key === "ArrowUp") { e.preventDefault(); setSel(Math.max(sel - 1, 0)); }
        else if (e.key === "Enter") { e.preventDefault(); go(sel); }
      } else if (openId && (e.key === "ArrowRight" || e.key === "ArrowLeft") && !e.ctrlKey && !e.metaKey) {
        var i = PROGRAMS.map(function (p) { return p.id; }).indexOf(openId), n = i + (e.key === "ArrowRight" ? 1 : -1);
        if (PROGRAMS[n]) openProgram(PROGRAMS[n].id);
      }
    });
    $$("[data-search]").forEach(function (el) { el.addEventListener("click", function () { openSearch(el.getAttribute("data-search") || ""); }); });
    window.addEventListener("hashchange", routeHash);
    // scroll reveal
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (es) { es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } }); }, { threshold: .08 });
      $$(".reveal").forEach(function (el) { io.observe(el); });
    } else $$(".reveal").forEach(function (el) { el.classList.add("in"); });
  }
  function routeHash() {
    var h = location.hash.slice(1); if (!h) return;
    if (PROGRAMS.some(function (p) { return p.id === h; })) openProgram(h, false);
  }

  /* ---------- progress widgets (home) ---------- */
  function renderProgress() {
    var total = PROGRAMS.length, d = doneCount(), pct = total ? Math.round(d / total * 100) : 0;
    var ring = $("#progressRing"); if (ring) { ring.style.setProperty("--p", pct); $("span", ring).textContent = pct + "%"; }
    var t = $("#progressText"); if (t) t.textContent = d + " of " + total + " programs completed";
    var bars = $("#progressBars");
    var ld = LESSONS.filter(function (l) { return isDone("lesson-" + l.id); }).length;
    var lessonBar = '<div class="bar-row"><div class="meta"><span><b style="color:var(--text)">Python lessons</b></span><b>' + ld + "/" + LESSONS.length + '</b></div><div class="track"><span style="width:' + (LESSONS.length ? Math.round(ld / LESSONS.length * 100) : 0) + '%"></span></div></div>';
    if (bars) bars.innerHTML = lessonBar + GROUPS.map(function (g) { var c = doneCount(g.slug), p = g.count ? Math.round(c / g.count * 100) : 0; return '<div class="bar-row"><div class="meta"><span>' + esc(g.label) + "</span><b>" + c + "/" + g.count + '</b></div><div class="track"><span style="width:' + p + '%"></span></div></div>'; }).join("");
    var bm = $("#bookmarkList");
    if (bm) {
      var items = [];
      Object.keys(bookmarks).sort(function (a, b) { return bookmarks[b] - bookmarks[a]; }).forEach(function (k) {
        var parts = k.split(":");
        if (parts.length !== 2) return;
        var type = parts[0], id = parts[1], title = "", sub = "", href = "";
        if (type === "program") { var p = PROGRAMS.filter(function (x) { return x.id === id; })[0]; if (!p) return; title = p.title; sub = "Program · " + p.difficulty; href = "programs.html#" + p.id; }
        else if (type === "lesson") { var l = LESSONS.filter(function (x) { return x.id === id; })[0]; if (!l) return; title = l.title; sub = "Python lesson · " + l.time; href = "lesson.html?id=" + l.id; }
        else if (type === "interview") { var q = INT.filter(function (x) { return x.id === id; })[0]; if (!q) return; title = q.title; sub = "Interview · " + q.status; href = "interview.html#" + q.id; }
        else if (type === "dsa-interview") { var iq = DSAIQ.filter(function (x) { return x.id === id; })[0]; if (!iq) return; title = iq.q; sub = "DSA interview · " + iq.category; href = "interview.html#dsa-question-bank"; }
        items.push('<a class="bookmark-item" href="' + href + '"><span class="bookmark-star">★</span><span><b>' + esc(title) + '</b><small>' + esc(sub) + '</small></span></a>');
      });
      bm.innerHTML = items.length ? items.slice(0, 12).join("") : '<div class="empty bookmark-empty">No bookmarks yet. Save a program or lesson you want to revisit.</div>';
      var bc = $("#bookmarkCount"); if (bc) bc.textContent = items.length + " saved";
    }

    var cont = $("#continueBox");
    if (cont) {
      var last = store.get("last", null), p = PROGRAMS.filter(function (x) { return x.id === last; })[0];
      if (p) { var nx = PROGRAMS[PROGRAMS.indexOf(p) + (isDone(p.id) ? 1 : 0)] || p; cont.innerHTML = '<button class="button button-primary" data-continue="' + nx.id + '">Continue: ' + esc(nx.title.length > 34 ? nx.title.slice(0, 32) + "…" : nx.title) + " →</button>"; $("[data-continue]", cont).addEventListener("click", function () { location.href = "programs.html#" + nx.id; }); }
      else cont.innerHTML = '<a class="button button-primary" href="programs.html">Start with Program 01 →</a>';
      var ll = store.get("lastLesson", null), li = LESSONS.map(function (l) { return l.id; }).indexOf(ll);
      var nl = li < 0 ? LESSONS[0] : (isDone("lesson-" + ll) ? LESSONS[li + 1] || LESSONS[li] : LESSONS[li]);
      if (nl) cont.insertAdjacentHTML("afterbegin", '<a class="button button-secondary" style="margin:0 8px 8px 0" href="lesson.html?id=' + nl.id + '">' + (li < 0 ? "Start Python lesson 1" : "Continue lesson") + " →</a>");
    }
  }
  document.addEventListener("pydsa:progress", renderProgress);
  document.addEventListener("pydsa:bookmarks", renderProgress);

  /* ---------- boot ---------- */
  document.addEventListener("DOMContentLoaded", function () {
    buildChrome(); bindGlobal(); renderProgress();
    if (window.PyDSA_page) window.PyDSA_page({ store: store, isDone: isDone, doneCount: doneCount, openProgram: openProgram, toggleDone: toggleDone, isBookmarked: isBookmarked, toggleBookmark: toggleBookmark });
    routeHash();
  });
  window.PyDSA.store = store;
  window.PyDSA.bookmarks = { isBookmarked: isBookmarked, toggleBookmark: toggleBookmark, bookmarkCount: bookmarkCount, getBookmarks: getBookmarks };
})();
