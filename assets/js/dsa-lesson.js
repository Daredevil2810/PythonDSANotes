/* DSA roadmap lesson renderer */
window.PyDSA_page = function (api) {
  if (document.body.getAttribute('data-page') !== 'dsa-lesson') return;
  var LS = window.PYDSA_DSA_LESSONS || [], esc = PyDSA.esc, root = document.getElementById('dsa-lesson-root');
  var id = new URLSearchParams(location.search).get('id') || (LS[0] && LS[0].id);
  var idx = LS.findIndex(function (x) { return x.id === id; }); if (idx < 0) idx = 0;
  var L = LS[idx]; if (!L) { root.innerHTML = '<div class="empty">DSA lesson not found.</div>'; return; }
  var key = 'dsa-lesson-' + L.id;
  document.title = L.title + ' — DSA · Python DSA Notes';
  function fmt(t) { return esc(t).replace(/`([^`]+)`/g, '<code>$1</code>').replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>').replace(/\n/g, '<br>'); }
  function codeBox(code) { return '<div class="code-box"><div class="code-header"><span>example.py</span><button class="copy-button" data-copy>Copy code</button></div><pre><code>' + PyDSA.highlight(code) + '</code></pre></div>'; }
  var byLevel = {};
  LS.forEach(function (x) { (byLevel[x.level] = byLevel[x.level] || []).push(x); });
  var side = Object.keys(byLevel).sort(function(a,b){return a-b;}).map(function (level) {
    return '<span class="side-title" style="margin-top:14px">LEVEL ' + level + '</span>' + byLevel[level].map(function(x){return '<a href="dsa-lesson.html?id=' + x.id + '" class="' + (x.id === L.id ? 'active' : '') + '">' + esc(x.title) + '<span>' + (api.isDone(keyFor(x.id)) ? '✓' : '') + '</span></a>';}).join('');
  }).join('');
  function keyFor(x) { return 'dsa-lesson-' + x; }
  var html = '<div class="page-head" style="padding-bottom:10px"><div class="crumbs"><a href="index.html">Home</a><span>/</span><a href="dsa.html">DSA Roadmap</a><span>/</span><span>Level ' + L.level + '</span></div></div>';
  html += '<div class="with-side"><aside class="side" aria-label="DSA lessons">' + side + '</aside><article class="lesson">';
  html += '<header class="lesson-head"><div class="demo-row" style="margin:0 0 12px"><span class="badge badge-teal">DSA</span><span class="badge badge-gray">LEVEL ' + L.level + '</span><span class="badge badge-gray">' + esc(L.difficulty.toUpperCase()) + '</span></div><h1>' + esc(L.title) + '</h1><p class="lead">' + fmt(L.summary) + '</p></header>';
  html += '<div class="drawer-actions" style="margin:18px 0"><button class="button button-small button-ghost bookmark-btn" id="bookmarkBtn" aria-pressed="' + api.isBookmarked('dsa-lesson', L.id) + '">' + (api.isBookmarked('dsa-lesson', L.id) ? '★ Bookmarked' : '☆ Bookmark lesson') + '</button></div>';
html += '<section class="ls"><h2><i>1</i>What is it?</h2><p>' + fmt(L.what) + '</p></section>';
  html += '<section class="ls"><h2><i>2</i>Why do we need it?</h2><p>' + fmt(L.why) + '</p></section>';
  html += '<section class="ls"><h2><i>3</i>How it works</h2><div class="explain"><div class="explain-tag">Everyday idea</div><p>' + fmt(L.simple) + '</p><div class="explain-tag">Technical view</div><p>' + fmt(L.tech) + '</p></div><ol class="steps-list" style="grid-template-columns:1fr;margin-top:14px">' + L.steps.map(function(s){return '<li>' + fmt(s) + '</li>';}).join('') + '</ol></section>';
  html += '<section class="ls"><h2><i>4</i>Code, step by step</h2>' + codeBox(L.code) + '<div class="out"><span>OUTPUT / RESULT</span><pre>' + esc(L.output) + '</pre></div><table class="lines"><thead><tr><th>Code</th><th>What it means</th></tr></thead><tbody>' + L.lines.map(function(r){return '<tr><td><code>' + PyDSA.highlight(r[0]) + '</code></td><td>' + fmt(r[1]) + '</td></tr>';}).join('') + '</tbody></table></section>';
  html += '<section class="ls"><h2><i>5</i>Common mistakes</h2><ul class="mist">' + L.mistakes.map(function(m){return '<li>' + fmt(m) + '</li>';}).join('') + '</ul></section>';
  html += '<section class="ls"><h2><i>6</i>When should I use it?</h2><p>' + fmt(L.use) + '</p></section>';
  html += '<section class="ls"><h2><i>7</i>Interview questions</h2><div class="qa">' + L.qa.map(function(q){return '<details><summary>' + fmt(q[0]) + '</summary><p>' + fmt(q[1]) + '</p></details>';}).join('') + '</div></section>';
  html += '<section class="ls try"><h2><i>8</i>Try it yourself</h2><div class="try-card"><p>' + fmt(L.practice) + '</p><div class="drawer-actions"><button class="button button-small button-secondary" id="hintBtn">Show hint</button><button class="button button-small button-ghost" id="solBtn">Show solution</button></div><div class="notice teal" id="hint" hidden><div><b>Hint:</b> ' + fmt(L.hint) + '</div></div><div id="sol" hidden>' + codeBox(L.solution) + '</div></div></section>';
  var related = (L.related || []).map(function(id){var p=(window.PYDSA_PROGRAMS||[]).find(function(x){return x.id===id;}); return p ? '<a class="tag done" href="programs.html#' + esc(p.id) + '">' + esc(p.title) + ' →</a>' : '';}).join('');
  if (related) html += '<section class="ls"><h2><i>9</i>Practise with real programs</h2><div class="tags">' + related + '</div></section>';
  if (L.deepPrograms && L.deepPrograms.length) {
    var deep = (window.PYDSA_DSA_STRUCTURE_PROGRAMS || []).filter(function(p){ return L.deepPrograms.indexOf(p.id) > -1; });
    html += '<section class="ls"><h2><i>10</i>Deep implementation library</h2><p>Each focused program has Python code, expected output, line-by-line explanation, dry run, complexity, common mistakes, interview questions and a practice task.</p><div class="tags">' + deep.map(function(p){return '<a class="tag done" href="dsa-structure-program.html?id=' + encodeURIComponent(p.id) + '">' + esc(p.title) + ' →</a>';}).join('') + '</div><div style="margin-top:14px"><a class="button button-small button-secondary" href="dsa-programs.html#' + encodeURIComponent((L.title.indexOf('Graph') === 0) ? 'Graphs' : 'Trees') + '">Open full program library →</a></div></section>';
  }
  var prev = LS[idx-1], next = LS[idx+1];
  html += '<footer class="lesson-foot"><button class="button done-btn button-secondary" id="lessonDone"></button><div class="pn">' + (prev ? '<a class="button button-ghost" href="dsa-lesson.html?id=' + prev.id + '">← ' + esc(prev.title) + '</a>' : '<a class="button button-ghost" href="dsa.html">← Roadmap</a>') + (next ? '<a class="button button-primary" href="dsa-lesson.html?id=' + next.id + '">' + esc(next.title) + ' →</a>' : '<a class="button button-primary" href="dsa.html">Back to roadmap →</a>') + '</div></footer></article></div>';
  root.innerHTML = html;
  root.querySelectorAll('[data-copy]').forEach(function(b){b.addEventListener('click',function(){var txt=b.closest('.code-box').querySelector('code').textContent;(navigator.clipboard ? navigator.clipboard.writeText(txt):Promise.reject()).then(function(){b.textContent='Copied ✓';},function(){b.textContent='Select & copy';});setTimeout(function(){b.textContent='Copy code';},1500);});});
  function toggle(btn, el, on, off){btn.addEventListener('click',function(){el.hidden=!el.hidden;btn.textContent=el.hidden?on:off;});}
  toggle(document.getElementById('hintBtn'),document.getElementById('hint'),'Show hint','Hide hint');
  toggle(document.getElementById('solBtn'),document.getElementById('sol'),'Show solution','Hide solution');
  var bm=document.getElementById('bookmarkBtn');
  bm.addEventListener('click',function(){api.toggleBookmark('dsa-lesson',L.id);var y=api.isBookmarked('dsa-lesson',L.id);bm.classList.toggle('is-bookmarked',y);bm.setAttribute('aria-pressed',y);bm.textContent=y?'★ Bookmarked':'☆ Bookmark lesson';});
  var db=document.getElementById('lessonDone');
  function drawDone(){var y=api.isDone(key);db.classList.toggle('is-done',y);db.textContent=y?'✓ Lesson completed':'Mark lesson as completed';}
  db.addEventListener('click',function(){api.toggleDone(key);drawDone();document.dispatchEvent(new CustomEvent('pydsa:progress'));});
  drawDone();
};
