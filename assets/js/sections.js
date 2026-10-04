/* Python / Programs / DSA / Interview pages */
window.PyDSA_page = function (api) {
  var page = document.body.getAttribute("data-page"), root = document.getElementById("content");
  if (!root) return;
  var P = window.PYDSA_PROGRAMS, G = window.PYDSA_GROUPS, esc = PyDSA.esc;

  function card(p) {
    var g = G.filter(function (x) { return x.slug === p.group; })[0];
    return "<button class='prog-card " + (api.isDone(p.id) ? "done" : "") + "' data-id='" + p.id + "'><div class='prog-top'><span class='prog-num'>#" + esc(p.n) + "</span><span class='check' aria-hidden='true'>✓</span></div><h4>" + esc(p.title) + "</h4><div class='prog-foot'><span class='difficulty " + p.difficulty + "'>" + p.difficulty + "</span><span>" + (p.topic ? "also in another set" : "") + "</span></div></button>";
  }

  /* ================= PROGRAMS ================= */
  if (page === "programs") {
    var state = { q: "", g: "all", d: "all", hide: false };
    root.innerHTML =
      "<div class='with-side'><aside class='side' id='side' aria-label='Categories'></aside><div>" +
      "<div class='toolbar'><label class='field grow'><span aria-hidden='true'>⌕</span><input id='q' type='search' placeholder='Filter programs…' aria-label='Filter programs'></label>" +
      "<label class='field'><select id='d' aria-label='Difficulty'><option value='all'>All levels</option><option value='easy'>Easy</option><option value='medium'>Medium</option><option value='hard'>Hard</option></select></label>" +
      "<label class='field'><input id='hide' type='checkbox' aria-label='Hide completed'><span style='font-size:13px;color:var(--text-soft)'>Hide completed</span></label></div>" +
      "<p class='result-count' id='count'></p><div id='list'></div></div></div>";

    var side = document.getElementById("side");
    function renderSide() {
      side.innerHTML = "<span class='side-title'>Categories</span><a href='#' data-g='all' class='" + (state.g === "all" ? "active" : "") + "'>All programs<span>" + api.doneCount() + "/" + P.length + "</span></a>" +
        G.map(function (g) { return "<a href='#" + g.slug + "' data-g='" + g.slug + "' class='" + (state.g === g.slug ? "active" : "") + "'>" + esc(g.label) + "<span>" + api.doneCount(g.slug) + "/" + g.count + "</span></a>"; }).join("");
    }
    function render() {
      var q = state.q.toLowerCase(), out = "", n = 0;
      G.forEach(function (g) {
        if (state.g !== "all" && state.g !== g.slug) return;
        var items = P.filter(function (p) { return p.group === g.slug && (!q || p.title.toLowerCase().indexOf(q) > -1) && (state.d === "all" || p.difficulty === state.d) && (!state.hide || !api.isDone(p.id)); });
        if (!items.length) return; n += items.length;
        out += "<section class='group-block' id='" + g.slug + "'><h2 class='group-title'><span class='badge badge-" + g.accent + "'>" + esc(g.label.toUpperCase()) + "</span><small>" + api.doneCount(g.slug) + " of " + g.count + " done</small></h2><p class='group-blurb'>" + esc(g.blurb) + "</p><div class='prog-grid' style='grid-template-columns:repeat(auto-fill,minmax(240px,1fr))'>" + items.map(card).join("") + "</div></section>";
      });
      document.getElementById("list").innerHTML = out || "<div class='empty'>No programs match these filters. Try clearing the search.</div>";
      document.getElementById("count").textContent = n + " program" + (n === 1 ? "" : "s") + " shown";
      renderSide();
    }
    document.getElementById("q").addEventListener("input", function (e) { state.q = e.target.value; render(); });
    document.getElementById("d").addEventListener("change", function (e) { state.d = e.target.value; render(); });
    document.getElementById("hide").addEventListener("change", function (e) { state.hide = e.target.checked; render(); });
    root.addEventListener("click", function (e) {
      var b = e.target.closest("[data-id]"); if (b) return api.openProgram(b.getAttribute("data-id"));
      var a = e.target.closest("[data-g]"); if (a) { e.preventDefault(); state.g = a.getAttribute("data-g"); render(); window.scrollTo({ top: 0 }); }
    });
    document.addEventListener("pydsa:progress", render);
    // deep link to a category (#patterns) or a program
    var h = location.hash.slice(1);
    if (G.some(function (g) { return g.slug === h; })) { state.g = h; }
    render();
    if (state.g !== "all") window.scrollTo({ top: 0 });
  }

  /* ================= PYTHON ================= */
  if (page === "python") {
    var LS = window.PYDSA_LESSONS, ldone = LS.filter(function (l) { return api.isDone("lesson-" + l.id); }).length;
    root.innerHTML =
      "<div class='notice teal' style='margin-bottom:28px'><div><b>" + LS.length + " lessons.</b> Core Python from the basics to OOP. Every lesson has a plain-language explanation, line-by-line code meaning, interview questions and a practice task. <b>" + ldone + " of " + LS.length + "</b> completed.</div></div>" +
      "<div class='module-grid'>" + window.PYDSA_PYTHON.map(function (m, i) {
        var ls = LS.filter(function (l) { return l.section === i + 1; });
        return "<article class='module-card' id='" + m.id + "'><header><div class='num'>" + m.n + "</div><div><span class='badge badge-blue'>PYTHON</span><h3>" + esc(m.title) + "</h3></div></header><p>" + esc(m.blurb) + "</p><div class='lesson-links'>" +
          ls.map(function (l, k) { var d = api.isDone("lesson-" + l.id); return "<a class='" + (d ? "is-done" : "") + "' href='lesson.html?id=" + l.id + "'><span>" + (d ? "✓ " : "") + esc(l.title) + "</span><small>" + esc(l.time) + "</small></a>"; }).join("") +
          "</div><footer><span class='status live'>" + ls.filter(function (l) { return api.isDone('lesson-' + l.id); }).length + "/" + ls.length + " done</span><a class='button button-small button-secondary' href='lesson.html?id=" + ls[0].id + "'>Start section →</a></footer></article>";
      }).join("") + "</div>" ;
    if (location.hash) { var el = document.getElementById(location.hash.slice(1)); if (el) setTimeout(function () { el.scrollIntoView({ behavior: "smooth", block: "center" }); el.style.borderColor = "var(--blue-bright)"; }, 150); }
  }

  /* ================= DSA ================= */
  if (page === "dsa") {
    var D = window.PYDSA_DSA, DL = window.PYDSA_DSA_LESSONS || [];
    var dsaDone = DL.filter(function (x) { return api.isDone("dsa-lesson-" + x.id); }).length;
    var dsaPct = DL.length ? Math.round(dsaDone / DL.length * 100) : 0;
    root.innerHTML =
      "<div class='notice' style='margin-bottom:28px'><div><b>Complete DSA roadmap:</b> every roadmap topic now has a full lesson. Start with Level 0, read the concept lesson, then use the linked practice programs where available.<div class='bar-row' style='margin-top:14px'><div class='meta'><span>Roadmap progress</span><b>" + dsaDone + "/" + DL.length + "</b></div><div class='track'><span style='width:" + dsaPct + "%'></span></div></div></div></div>" +
      "<div class='with-side'><aside class='side'><span class='side-title'>Levels</span>" + D.map(function (l) { return "<a href='#level-" + l.level + "'>" + esc(l.title) + "<span>L" + l.level + "</span></a>"; }).join("") + "</aside>" +
      "<div class='roadmap'>" + D.map(function (l) {
        return "<div class='level' id='level-" + l.level + "'><div class='level-num'><b>L" + l.level + "</b></div><div class='level-body'><h3>" + esc(l.title) + " <span class='status live'>Full lessons</span></h3><p>" + esc(l.blurb) + "</p><div class='tags'>" +
          l.items.map(function (i) { return i.u ? "<a class='tag done' href='" + i.u + "'>" + esc(i.t) + " →</a>" : "<span class='tag'>" + esc(i.t) + "</span>"; }).join("") + "</div></div></div>";
      }).join("") + "</div></div>";
  }

  /* ================= PATTERNS ================= */
  if (page === "patterns") {
    var PS = window.PYDSA_PATTERNS || [];
    var state = { q: "", level: "all" };
    function renderPatterns() {
      var q = state.q.toLowerCase(), items = PS.filter(function (x) {
        return (state.level === "all" || x.level === state.level) && (!q || (x.title + " " + x.signal + " " + x.idea + " " + x.example).toLowerCase().indexOf(q) > -1);
      });
      var list = document.getElementById("patternList");
      list.innerHTML = items.map(function (x) {
        var done = api.isDone("pattern-" + x.id), saved = api.isBookmarked("pattern", x.id);
        return "<article class='lesson-card " + (done ? "is-done" : "") + "'><div class='section-heading'><div><span class='badge badge-purple'>" + esc(x.level) + "</span><h2>" + esc(x.title) + "</h2><p class='section-lead'><b>Signal:</b> " + esc(x.signal) + "</p></div><div class='qa-card-actions'><button class='button button-small button-ghost bookmark-btn " + (saved ? "is-bookmarked" : "") + "' data-pattern-bookmark='" + x.id + "' aria-pressed='" + saved + "'>" + (saved ? "★" : "☆") + "</button><button class='button button-small button-ghost " + (done ? "is-done" : "") + "' data-pattern-done='" + x.id + "'>" + (done ? "✓ Practised" : "Mark practised") + "</button></div></div>" +
          "<div class='notice'><div><b>Core idea:</b> " + esc(x.idea) + "</div></div>" +
          "<h3>How to recognise and apply it</h3><ol>" + x.steps.map(function (v) { return "<li>" + esc(v) + "</li>"; }).join("") + "</ol>" +
          "<h3>Example problem</h3><p>" + esc(x.example) + "</p><pre class='code-block'><code>" + esc(x.code) + "</code></pre>" +
          "<p><b>Complexity:</b> " + esc(x.complexity) + "</p><h3>Common mistakes</h3><ul>" + x.mistakes.map(function (v) { return "<li>" + esc(v) + "</li>"; }).join("") + "</ul>" +
          "<div class='interview-tip'><b>Interview question:</b> " + esc(x.interview) + "</div><p><b>Try yourself:</b> " + esc(x.practice) + "</p></article>";
      }).join("") || "<div class='empty'>No patterns match your search.</div>";
      document.getElementById("patternCount").textContent = items.length + " pattern" + (items.length === 1 ? "" : "s") + " shown";
      list.querySelectorAll("[data-pattern-done]").forEach(function (b) { b.addEventListener("click", function () { api.toggleDone("pattern-" + b.getAttribute("data-pattern-done")); renderPatterns(); }); });
      list.querySelectorAll("[data-pattern-bookmark]").forEach(function (b) { b.addEventListener("click", function () { api.toggleBookmark("pattern", b.getAttribute("data-pattern-bookmark")); renderPatterns(); }); });
    }
    root.innerHTML = "<div class='notice purple' style='margin-bottom:28px'><div><b>Pattern recognition.</b></div><p style='margin:8px 0 0'>The goal is not to memorise solutions. For each problem, identify the signal, state the invariant, choose the pattern, then explain the trade-off before coding.</p></div><div class='toolbar'><label class='field grow'><span aria-hidden='true'>⌕</span><input id='patternQ' type='search' placeholder='Search patterns, signals, examples…' aria-label='Search patterns'></label><label class='field'><select id='patternLevel' aria-label='Pattern level'><option value='all'>All levels</option><option value='Core'>Core</option><option value='Advanced'>Advanced</option></select></label></div><p class='result-count' id='patternCount'></p><div class='qa-card-list' id='patternList'></div>";
    document.getElementById("patternQ").addEventListener("input", function (e) { state.q = e.target.value; renderPatterns(); });
    document.getElementById("patternLevel").addEventListener("change", function (e) { state.level = e.target.value; renderPatterns(); });
    document.addEventListener("pydsa:progress", renderPatterns); renderPatterns();
  }

  /* ================= CODING PROBLEMS ================= */
  if (page === "coding-problems") {
    var CP = window.PYDSA_CODING_PROBLEMS || [];
    var state = { q: "", difficulty: "all", category: "all" };
    var categories = Array.from(new Set(CP.map(function (x) { return x.category; })));
    function renderProblems() {
      var q = state.q.toLowerCase();
      var items = CP.filter(function (x) { return (state.difficulty === "all" || x.difficulty === state.difficulty) && (state.category === "all" || x.category === state.category) && (!q || (x.title + " " + x.category + " " + x.pattern + " " + x.signal + " " + x.understand).toLowerCase().indexOf(q) > -1); });
      var list = document.getElementById("codingProblemList");
      list.innerHTML = items.map(function (x, i) {
        var done = api.isDone("coding-problem-" + x.id), saved = api.isBookmarked("coding-problem", x.id);
        return "<article class='lesson-card " + (done ? "is-done" : "") + "' id='problem-" + esc(x.id) + "'><div class='section-heading'><div><span class='badge badge-orange'>" + esc(x.difficulty) + "</span><h2>" + (i + 1) + ". " + esc(x.title) + "</h2><p class='section-lead'><b>Pattern:</b> " + esc(x.pattern) + " · <b>Signal:</b> " + esc(x.signal) + "</p></div><div class='qa-card-actions'><button class='button button-small button-ghost bookmark-btn " + (saved ? "is-bookmarked" : "") + "' data-cp-bookmark='" + x.id + "' aria-pressed='" + saved + "'>" + (saved ? "★" : "☆") + "</button><button class='button button-small button-ghost " + (done ? "is-done" : "") + "' data-cp-done='" + x.id + "'>" + (done ? "✓ Solved" : "Mark solved") + "</button></div></div>" +
          "<div class='notice orange'><div><b>Understand the problem:</b> " + esc(x.understand) + "</div></div>" +
          "<h3>Core idea</h3><p>" + esc(x.idea) + "</p><h3>Approach</h3><ol>" + x.steps.map(function (v) { return "<li>" + esc(v) + "</li>"; }).join("") + "</ol>" +
          "<h3>Python implementation</h3><pre class='code-block'><code>" + esc(x.code) + "</code></pre>" +
          "<h3>Dry run</h3><p>" + esc(x.dry) + "</p><p><b>Complexity:</b> " + esc(x.complexity) + "</p>" +
          "<h3>Common mistakes</h3><ul>" + x.mistakes.map(function (v) { return "<li>" + esc(v) + "</li>"; }).join("") + "</ul>" +
          "<div class='interview-tip'><b>Interview question:</b> " + esc(x.interview) + "</div><p><b>Try yourself:</b> " + esc(x.practice) + "</p>" +
          "<footer style='display:flex;justify-content:space-between;gap:12px;align-items:center;flex-wrap:wrap;margin-top:18px'><span class='tag'>" + esc(x.category) + "</span><a class='button button-small button-secondary' href='" + x.url + "' target='_blank' rel='noopener'>Practice on LeetCode ↗</a></footer></article>";
      }).join("") || "<div class='empty'>No coding problems match these filters.</div>";
      document.getElementById("codingProblemCount").textContent = items.length + " problem" + (items.length === 1 ? "" : "s") + " shown · " + CP.length + " total";
      list.querySelectorAll("[data-cp-done]").forEach(function (b) { b.addEventListener("click", function () { api.toggleDone("coding-problem-" + b.getAttribute("data-cp-done")); renderProblems(); }); });
      list.querySelectorAll("[data-cp-bookmark]").forEach(function (b) { b.addEventListener("click", function () { api.toggleBookmark("coding-problem", b.getAttribute("data-cp-bookmark")); renderProblems(); }); });
      if (location.hash) { var target = document.getElementById(location.hash.slice(1)); if (target) setTimeout(function () { target.scrollIntoView({ behavior: "smooth", block: "center" }); }, 100); }
    }
    root.innerHTML = "<div class='notice orange' style='margin-bottom:28px'><div><b>Coding problems, Easy → Hard.</b></div><p style='margin:8px 0 0'>Turn the roadmap and patterns into interview practice. For every problem: understand the requirement, recognise the pattern, explain the approach, dry-run it, then code it yourself before checking the implementation.</p></div><div class='toolbar'><label class='field grow'><span aria-hidden='true'>⌕</span><input id='codingProblemQ' type='search' placeholder='Search problems, patterns, signals…' aria-label='Search coding problems'></label><label class='field'><select id='codingProblemDifficulty' aria-label='Difficulty'><option value='all'>All levels</option><option value='Easy'>Easy</option><option value='Medium'>Medium</option><option value='Hard'>Hard</option></select></label><label class='field'><select id='codingProblemCategory' aria-label='Category'><option value='all'>All categories</option>" + categories.map(function (c) { return "<option value='" + esc(c) + "'>" + esc(c) + "</option>"; }).join("") + "</select></label></div><p class='result-count' id='codingProblemCount'></p><div class='qa-card-list' id='codingProblemList'></div>";
    document.getElementById("codingProblemQ").addEventListener("input", function (e) { state.q = e.target.value; renderProblems(); });
    document.getElementById("codingProblemDifficulty").addEventListener("change", function (e) { state.difficulty = e.target.value; renderProblems(); });
    document.getElementById("codingProblemCategory").addEventListener("change", function (e) { state.category = e.target.value; renderProblems(); });
    document.addEventListener("pydsa:progress", renderProblems); renderProblems();
  }

  /* ================= INTERVIEW QUESTION LIBRARIES ================= */
  function renderQuestionLibrary(opts) {
    var questions = opts.questions || [], prefix = opts.prefix, accent = opts.accent || 'teal';
    var practicedKey = opts.practicedKey || prefix;
    var search = '', category = 'all';
    var categories = Array.from(new Set(questions.map(function (x) { return x.category; })));
    function done(id) { return api.isDone(practicedKey + '-' + id); }
    function render() {
      var q = search.trim().toLowerCase();
      var items = questions.filter(function (x) { return (category === 'all' || x.category === category) && (!q || (x.q + ' ' + x.a + ' ' + x.category + ' ' + (x.tip || '')).toLowerCase().indexOf(q) > -1); });
      var list = document.getElementById(opts.listId);
      if (!list) return;
      list.innerHTML = items.map(function (x, i) {
        var saved = api.isBookmarked(prefix, x.id), isDone = done(x.id);
        return "<article class='question-card " + (isDone ? "is-practiced" : "") + "' id='" + prefix + "-" + esc(x.id) + "'><header class='question-card-head'><div class='question-card-title'><span class='badge badge-" + accent + "'>" + esc(x.category) + "</span><h2>" + (i + 1) + ". " + esc(x.q) + "</h2></div><div class='question-card-actions'><button class='button button-small button-ghost bookmark-btn " + (saved ? "is-bookmarked" : "") + "' data-q-bookmark='" + x.id + "' aria-pressed='" + saved + "' title='Bookmark question'>" + (saved ? "★" : "☆") + "</button><button class='button button-small button-ghost " + (isDone ? "is-done" : "") + "' data-q-done='" + x.id + "'>" + (isDone ? "✓ Practised" : "Mark practised") + "</button></div></header><details><summary>Show answer</summary><div class='question-answer'><p>" + esc(x.a) + "</p><div class='interview-tip'><b>Interview tip:</b> " + esc(x.tip) + "</div></div></details></article>";
      }).join("") || "<div class='empty'>No questions match these filters.</div>";
      var count = document.getElementById(opts.countId);
      if (count) count.textContent = items.length + " question" + (items.length === 1 ? "" : "s") + " shown · " + questions.length + " total";
      list.querySelectorAll('[data-q-done]').forEach(function (b) { b.addEventListener('click', function () { api.toggleDone(practicedKey + '-' + b.getAttribute('data-q-done')); render(); }); });
      list.querySelectorAll('[data-q-bookmark]').forEach(function (b) { b.addEventListener('click', function () { api.toggleBookmark(prefix, b.getAttribute('data-q-bookmark')); render(); }); });
      if (location.hash) { var target = document.getElementById(location.hash.slice(1)); if (target) setTimeout(function () { target.scrollIntoView({ behavior: 'smooth', block: 'center' }); }, 80); }
    }
    var searchEl = document.getElementById(opts.searchId), catEl = document.getElementById(opts.categoryId);
    if (searchEl) searchEl.addEventListener('input', function (e) { search = e.target.value; render(); });
    if (catEl) catEl.addEventListener('change', function (e) { category = e.target.value; render(); });
    document.addEventListener('pydsa:progress', render);
    render();
  }

  if (page === "dsa-interview") {
    var DSAIQ_PAGE = window.PYDSA_DSA_INTERVIEW || [];
    var dsaCats = Array.from(new Set(DSAIQ_PAGE.map(function (x) { return x.category; })));
    root.innerHTML = "<div class='notice teal library-intro'><div><b>30 DSA interview questions.</b> Try answering before opening each answer. The goal is to explain the idea, complexity, trade-offs and edge cases clearly.</div></div><div class='toolbar'><label class='field grow'><span aria-hidden='true'>⌕</span><input id='dsaIqPage' type='search' placeholder='Search DSA interview questions…' aria-label='Search DSA interview questions'></label><label class='field'><select id='dsaCatPage' aria-label='Question category'><option value='all'>All categories</option>" + dsaCats.map(function (c) { return "<option value='" + esc(c) + "'>" + esc(c) + "</option>"; }).join("") + "</select></label></div><p class='result-count' id='dsaIqPageCount'></p><div class='question-list' id='dsaIqPageList'></div>";
    renderQuestionLibrary({ questions: DSAIQ_PAGE, prefix: 'dsa-interview', practicedKey: 'dsa-interview', accent: 'teal', searchId: 'dsaIqPage', categoryId: 'dsaCatPage', countId: 'dsaIqPageCount', listId: 'dsaIqPageList' });
  }

  if (page === "django-interview") {
    var DJIQ_PAGE = window.PYDSA_DJANGO_INTERVIEW || [];
    var djCats = Array.from(new Set(DJIQ_PAGE.map(function (x) { return x.category; })));
    root.innerHTML = "<div class='notice blue library-intro'><div><b>30 Django & Web interview questions.</b> Practice framework fundamentals, ORM behavior, security, authentication, REST APIs and production concepts.</div></div><div class='toolbar'><label class='field grow'><span aria-hidden='true'>⌕</span><input id='djIqPage' type='search' placeholder='Search Django / web interview questions…' aria-label='Search Django interview questions'></label><label class='field'><select id='djCatPage' aria-label='Question category'><option value='all'>All categories</option>" + djCats.map(function (c) { return "<option value='" + esc(c) + "'>" + esc(c) + "</option>"; }).join("") + "</select></label></div><p class='result-count' id='djIqPageCount'></p><div class='question-list' id='djIqPageList'></div>";
    renderQuestionLibrary({ questions: DJIQ_PAGE, prefix: 'django-interview', practicedKey: 'django-interview', accent: 'blue', searchId: 'djIqPage', categoryId: 'djCatPage', countId: 'djIqPageCount', listId: 'djIqPageList' });
  }

  if (page === "hr-interview") {
    var HRIQ_PAGE = window.PYDSA_HR_INTERVIEW || [];
    var hrCats = Array.from(new Set(HRIQ_PAGE.map(function (x) { return x.category; })));
    root.innerHTML = "<div class='notice orange library-intro'><div><b>30 HR & behavioural interview questions.</b> Build honest, concise answers using your own experience. Use the examples as structure, not as scripts to memorise word-for-word.</div></div><div class='toolbar'><label class='field grow'><span aria-hidden='true'>⌕</span><input id='hrIqPage' type='search' placeholder='Search HR interview questions…' aria-label='Search HR interview questions'></label><label class='field'><select id='hrCatPage' aria-label='Question category'><option value='all'>All categories</option>" + hrCats.map(function (c) { return "<option value='" + esc(c) + "'>" + esc(c) + "</option>"; }).join("") + "</select></label></div><p class='result-count' id='hrIqPageCount'></p><div class='question-list' id='hrIqPageList'></div>";
    renderQuestionLibrary({ questions: HRIQ_PAGE, prefix: 'hr-interview', practicedKey: 'hr-interview', accent: 'orange', searchId: 'hrIqPage', categoryId: 'hrCatPage', countId: 'hrIqPageCount', listId: 'hrIqPageList' });
  }

  if (page === "python-interview") {
    var PYIQ_PAGE = window.PYDSA_PYTHON_INTERVIEW || [];
    var pyCats = Array.from(new Set(PYIQ_PAGE.map(function (x) { return x.category; })));
    root.innerHTML = "<div class='notice blue library-intro'><div><b>30 Python interview questions.</b> This bank is aligned to the Python topics already taught on this site: basics, data structures, functions, OOP, exceptions, files, modules and related interview concepts.</div></div><div class='toolbar'><label class='field grow'><span aria-hidden='true'>⌕</span><input id='pyIqPage' type='search' placeholder='Search Python interview questions…' aria-label='Search Python interview questions'></label><label class='field'><select id='pyCatPage' aria-label='Question category'><option value='all'>All categories</option>" + pyCats.map(function (c) { return "<option value='" + esc(c) + "'>" + esc(c) + "</option>"; }).join("") + "</select></label></div><p class='result-count' id='pyIqPageCount'></p><div class='question-list' id='pyIqPageList'></div>";
    renderQuestionLibrary({ questions: PYIQ_PAGE, prefix: 'python-interview', practicedKey: 'python-interview', accent: 'blue', searchId: 'pyIqPage', categoryId: 'pyCatPage', countId: 'pyIqPageCount', listId: 'pyIqPageList' });
  }

  /* ================= INTERVIEW HUB ================= */
  if (page === "interview") {
    root.innerHTML = "<div class='module-grid'>" + window.PYDSA_INTERVIEW.map(function (x) {
      var ready = x.id === "python-interview" || x.id === "dsa-interview" || x.id === "patterns" || x.id === "coding-problems" || x.id === "django-interview" || x.id === "hr";
      var count = (x.id === "python-interview" || x.id === "dsa-interview" || x.id === "django-interview" || x.id === "hr") ? "30" : (x.id === "patterns" ? "9" : (x.id === "coding-problems" ? "30" : "?"));
      var href = x.u || "#";
      var status = (x.id === "python-interview" || x.id === "dsa-interview" || x.id === "django-interview" || x.id === "hr") ? "30 questions" : (x.id === "patterns" ? "9 patterns" : (x.id === "coding-problems" ? "30 problems" : esc(x.status)));
      return "<article class='module-card' id='" + x.id + "'><header><div class='num' style='color:var(--" + ({blue:"blue-bright",teal:"teal",purple:"purple",orange:"orange"})[x.c] + ")'>" + count + "</div><div><h3>" + esc(x.title) + "</h3></div></header><p>" + esc(x.blurb) + "</p><footer><span class='status " + (ready ? "live" : "soon") + "'>" + status + "</span>" + (ready ? "<a class='button button-small button-secondary' href='" + href + "'>Open library →</a>" : "") + "<button class='button button-small button-ghost bookmark-btn " + (api.isBookmarked("interview", x.id) ? "is-bookmarked" : "") + "' data-bookmark-interview='" + x.id + "' aria-pressed='" + api.isBookmarked("interview", x.id) + "'>" + (api.isBookmarked("interview", x.id) ? "★ Bookmarked" : "☆ Bookmark") + "</button></footer></article>";
    }).join("");
    root.querySelectorAll('[data-bookmark-interview]').forEach(function (b) { b.addEventListener('click', function () { var id = b.getAttribute('data-bookmark-interview'); api.toggleBookmark('interview', id); var y = api.isBookmarked('interview', id); b.classList.toggle('is-bookmarked', y); b.setAttribute('aria-pressed', y); b.textContent = y ? '★ Bookmarked' : '☆ Bookmark'; }); });
  }

};
