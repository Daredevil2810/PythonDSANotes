/* Python lesson page: renders one lesson from window.PYDSA_LESSONS using ?id=slug */
window.PyDSA_page = function (api) {
  var LS = window.PYDSA_LESSONS, esc = PyDSA.esc, root = document.getElementById("lesson-root");
  var SECTIONS = window.PYDSA_PYTHON, store = api.store;
  var id = new URLSearchParams(location.search).get("id") || LS[0].id;
  var idx = LS.map(function (l) { return l.id; }).indexOf(id); if (idx < 0) idx = 0;
  var L = LS[idx], key = "lesson-" + L.id;
  var mode = store.get("mode", "simple");

  function fmt(t) { return esc(t).replace(/`([^`]+)`/g, "<code>$1</code>").replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>").replace(/\*([^*]+)\*/g, "<em>$1</em>").replace(/\n/g, "<br>"); }
  function codeBox(name, code, plain) { return "<div class='code-box'><div class='code-header'><span>" + esc(name) + "</span><button class='copy-button' data-copy>Copy code</button></div><pre><code>" + (plain ? esc(code) : PyDSA.highlight(code)) + "</code></pre></div>"; }
  var sec = SECTIONS[L.section - 1];
  document.title = L.title + " — Python · Python DSA Notes";

  var sideHtml = SECTIONS.map(function (s, i) {
    return "<span class='side-title' style='margin-top:" + (i ? 14 : 0) + "px'>" + s.n + " · " + esc(s.title.split(" &")[0]) + "</span>" +
      LS.filter(function (l) { return l.section === i + 1; }).map(function (l) {
        return "<a href='lesson.html?id=" + l.id + "' class='" + (l.id === L.id ? "active" : "") + "' data-lid='" + l.id + "'>" + esc(l.title) + "<span>" + (api.isDone("lesson-" + l.id) ? "✓" : "") + "</span></a>";
      }).join("");
  }).join("");

  var html = "<div class='page-head' style='padding-bottom:10px'><div class='crumbs'><a href='index.html'>Home</a><span>/</span><a href='python.html'>Python</a><span>/</span><span>" + esc(sec.title) + "</span></div></div>" +
    "<div class='with-side'><aside class='side' aria-label='Lessons'>" + sideHtml + "</aside><article class='lesson'>" +
    "<header class='lesson-head'><div class='demo-row' style='margin:0 0 12px'><span class='badge badge-blue'>PYTHON</span><span class='badge badge-gray'>SECTION " + sec.n + "</span><span class='badge badge-gray'>" + esc(L.time.toUpperCase()) + "</span></div>" +
    "<h1>" + esc(L.title) + "</h1><p class='lead'>" + fmt(L.summary) + "</p></header>";

  html += "<section class='ls'><h2><i>1</i>What is it?</h2><p>" + fmt(L.what) + "</p></section>";
  html += "<section class='ls'><h2><i>2</i>Why do we need it?</h2><p>" + fmt(L.why) + "</p></section>";
  html += "<section class='ls'><div class='ls-row'><h2><i>3</i>In plain words</h2><div class='toggle' role='group' aria-label='Explanation style'><button data-mode='simple' class='" + (mode === "simple" ? "on" : "") + "'>Explain simply</button><button data-mode='tech' class='" + (mode === "tech" ? "on" : "") + "'>Technical</button></div></div>" +
    "<div class='explain' id='explain'></div>";
  if (L.table) html += "<div class='table-wrap'><table class='ltable'><thead><tr>" + L.table.head.map(function (h) { return "<th>" + esc(h) + "</th>"; }).join("") + "</tr></thead><tbody>" + L.table.rows.map(function (r) { return "<tr>" + r.map(function (c, k) { return "<td>" + (k === 0 || /[\[\](){}=]/.test(c) ? "<code>" + esc(c) + "</code>" : esc(c)) + "</td>"; }).join("") + "</tr>"; }).join("") + "</tbody></table></div>";
  if (L.steps) html += "<ol class='steps-list' style='grid-template-columns:1fr;margin-top:14px'>" + L.steps.map(function (s) { return "<li>" + fmt(s) + "</li>"; }).join("") + "</ol>";
  html += "</section>";

  html += "<section class='ls'><h2><i>4</i>Code, step by step</h2>" + L.blocks.map(function (b, n) {
    return "<div class='block'><h3>" + esc(b.title) + "</h3>" + codeBox(b.plain ? "structure" : (b.noRun ? "example.py" : "lesson_" + (n + 1) + ".py"), b.code, b.plain) +
      (b.output ? "<div class='out'><span>OUTPUT</span><pre>" + esc(b.output) + "</pre></div>" : "") +
      "<table class='lines'><thead><tr><th>Line</th><th>What it means</th></tr></thead><tbody>" + b.lines.map(function (r) { return "<tr><td><code>" + (b.plain ? esc(r[0]) : PyDSA.highlight(r[0])) + "</code></td><td>" + fmt(r[1]) + "</td></tr>"; }).join("") + "</tbody></table></div>";
  }).join("") + "</section>";

  html += "<section class='ls'><h2><i>5</i>Common mistakes</h2><ul class='mist'>" + L.mistakes.map(function (m) { return "<li>" + fmt(m) + "</li>"; }).join("") + "</ul></section>";
  html += "<section class='ls'><h2><i>6</i>When should I use it?</h2><p>" + fmt(L.use) + "</p></section>";
  html += "<section class='ls'><h2><i>7</i>Interview questions</h2><div class='qa'>" + L.qa.map(function (q, n) { return "<details" + (n === 0 ? "" : "") + "><summary>" + fmt(q[0]) + "</summary><p>" + fmt(q[1]) + "</p></details>"; }).join("") + "</div></section>";

  var t = L.tryit;
  html += "<section class='ls try'><h2><i>8</i>Try it yourself</h2><div class='try-card'><p>" + fmt(t.task) + "</p><div class='drawer-actions'><button class='button button-small button-secondary' id='hintBtn'>Show hint</button><button class='button button-small button-ghost' id='solBtn'>Show solution</button></div>" +
    "<div class='notice teal' id='hint' hidden><div><b>Hint:</b> " + fmt(t.hint) + "</div></div><div id='sol' hidden>" + codeBox("solution.py", t.solution) + (t.output ? "<div class='out'><span>OUTPUT</span><pre>" + esc(t.output) + "</pre></div>" : "") + "</div></div></section>";

  if (L.related && L.related.length) {
    var P = window.PYDSA_PROGRAMS;
    html += "<section class='ls'><h2><i>9</i>Practise with real programs</h2><div class='tags'>" + L.related.map(function (r) { var p = P.filter(function (x) { return x.id === r; })[0]; return p ? "<a class='tag done' href='programs.html#" + p.id + "'>" + esc(p.title) + " →</a>" : ""; }).join("") + "</div></section>";
  }

  var prev = LS[idx - 1], next = LS[idx + 1];
  html += "<footer class='lesson-foot'><button class='button done-btn button-secondary' id='lessonDone'></button><div class='pn'>" +
    (prev ? "<a class='button button-ghost' href='lesson.html?id=" + prev.id + "'>← " + esc(prev.title) + "</a>" : "<span></span>") +
    (next ? "<a class='button button-primary' href='lesson.html?id=" + next.id + "'>" + esc(next.title) + " →</a>" : "<a class='button button-primary' href='programs.html'>Next: practise programs →</a>") + "</div></footer></article></div>";
  root.innerHTML = html;

  // behaviours
  function drawExplain() { document.getElementById("explain").innerHTML = "<div class='explain-tag'>" + (mode === "simple" ? "Everyday example" : "Precise definition") + "</div><p>" + fmt(mode === "simple" ? L.simple : L.tech) + "</p>"; }
  drawExplain();
  root.querySelectorAll("[data-mode]").forEach(function (b) { b.addEventListener("click", function () { mode = b.getAttribute("data-mode"); store.set("mode", mode); root.querySelectorAll("[data-mode]").forEach(function (x) { x.classList.toggle("on", x === b); }); drawExplain(); }); });
  root.querySelectorAll("[data-copy]").forEach(function (b) { b.addEventListener("click", function () { var txt = b.closest(".code-box").querySelector("code").textContent; (navigator.clipboard ? navigator.clipboard.writeText(txt) : Promise.reject()).then(function () { b.textContent = "Copied ✓"; }, function () { b.textContent = "Select & copy"; }); setTimeout(function () { b.textContent = "Copy code"; }, 1500); }); });
  function toggleEl(btn, el, on, off) { btn.addEventListener("click", function () { el.hidden = !el.hidden; btn.textContent = el.hidden ? on : off; }); }
  toggleEl(document.getElementById("hintBtn"), document.getElementById("hint"), "Show hint", "Hide hint");
  toggleEl(document.getElementById("solBtn"), document.getElementById("sol"), "Show solution", "Hide solution");
  var db = document.getElementById("lessonDone");
  function drawDone() { var y = api.isDone(key); db.classList.toggle("is-done", y); db.textContent = y ? "✓ Lesson completed" : "Mark lesson as completed"; var a = root.querySelector("[data-lid='" + L.id + "'] span"); if (a) a.textContent = y ? "✓" : ""; }
  db.addEventListener("click", function () { api.toggleDone(key); drawDone(); document.dispatchEvent(new CustomEvent("pydsa:progress")); });
  var bb = document.getElementById("lessonBookmark");
  function drawBookmark() { if (!bb) return; var y = api.isBookmarked("lesson", L.id); bb.classList.toggle("is-bookmarked", y); bb.setAttribute("aria-pressed", y); bb.textContent = y ? "★ Bookmarked" : "☆ Bookmark lesson"; }
  if (bb) bb.addEventListener("click", function () { api.toggleBookmark("lesson", L.id); drawBookmark(); });
  drawDone();
  if (bb) drawBookmark();
  store.set("lastLesson", L.id);
};
