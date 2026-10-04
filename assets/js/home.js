/* Homepage-only behaviour */
window.PyDSA_page = function (api) {
  var P = window.PYDSA_PROGRAMS, G = window.PYDSA_GROUPS, D = window.PYDSA_DSA, esc = PyDSA.esc;

  // syntax-highlight hero code
  document.querySelectorAll("code[data-hl]").forEach(function (c) { c.innerHTML = PyDSA.highlight(c.textContent); });

  // real numbers
  var s = document.getElementById("stats");
  s.innerHTML = [[P.length, "interview programs"], [G.length, "program categories"], [6, "DSA roadmap levels"], ["0", "servers, logins or sleeping backends"]]
    .map(function (x) { return "<div class='stat'><strong>" + x[0] + "</strong><span>" + x[1] + "</span></div>"; }).join("");
  document.getElementById("pc-programs").textContent = P.length;

  // roadmap
  document.getElementById("roadmapList").innerHTML = D.map(function (l) {
    return "<div class='level'><div class='level-num'><b>L" + l.level + "</b></div><div class='level-body'><h3>" + esc(l.title) + " <span class='status live'>Available</span></h3><p>" + esc(l.blurb) + "</p><div class='tags'>" +
      l.items.map(function (i) { return i.u ? "<a class='tag' href='" + i.u + "'>" + esc(i.t) + "</a>" : "<span class='tag'>" + esc(i.t) + "</span>"; }).join("") + "</div></div></div>";
  }).join("");

  // featured programs
  var pick = ["arrays-strings-05-1", "arrays-strings-06", "searching-sorting-02", "searching-sorting-07", "linked-list-01", "stack-queue-adv-03", "dynamic-programming-05", "dynamic-programming-03", "bit-manipulation-09"];
  document.getElementById("featuredGrid").innerHTML = pick.map(function (id) { return P.filter(function (p) { return p.id === id; })[0]; }).filter(Boolean).map(function (p) {
    var g = G.filter(function (x) { return x.slug === p.group; })[0];
    return "<button class='prog-card " + (api.isDone(p.id) ? "done" : "") + "' data-id='" + p.id + "'><div class='prog-top'><span class='badge badge-" + g.accent + "'>" + esc(g.label.toUpperCase()) + "</span><span class='check'>✓</span></div><h4>" + esc(p.title) + "</h4><div class='prog-foot'><span class='difficulty " + p.difficulty + "'>" + p.difficulty + "</span><span class='prog-num'>#" + esc(p.n) + "</span></div></button>";
  }).join("");
  document.getElementById("featuredGrid").addEventListener("click", function (e) { var b = e.target.closest("[data-id]"); if (b) api.openProgram(b.getAttribute("data-id")); });
  document.addEventListener("pydsa:progress", function () {
    document.querySelectorAll("#featuredGrid .prog-card").forEach(function (c) { c.classList.toggle("done", api.isDone(c.getAttribute("data-id"))); });
  });

  // Explain-simply binary search demo
  var arr = [5, 8, 12, 17, 23, 31, 42];
  var steps = [
    { lo: 0, hi: 6, mid: null, simple: "<p><b>The setup.</b> Imagine a sorted register of roll numbers. You want <b>23</b>. You will <b>not</b> start from page 1.</p><p>We keep two markers: <b>low</b> at the first number and <b>high</b> at the last.</p>", tech: "<p>Initialise <b>low = 0</b>, <b>high = n − 1 = 6</b>. The array must already be sorted.</p>" },
    { lo: 0, hi: 6, mid: 3, simple: "<p><b>Open the middle page.</b> It says <b>17</b>. We want 23, which is bigger than 17.</p><p>So 23 cannot be on the left. <b>Throw away the whole left half</b> in one move.</p>", tech: "<p><b>mid = (0 + 6) // 2 = 3</b>, arr[3] = 17 &lt; 23, so <b>low = mid + 1 = 4</b>. Half the range is eliminated.</p>" },
    { lo: 4, hi: 6, mid: 5, simple: "<p><b>Open the middle of what’s left.</b> It says <b>31</b>. That’s too big now.</p><p>So 23 must be to the left of 31. <b>Throw away the right side.</b></p>", tech: "<p><b>mid = (4 + 6) // 2 = 5</b>, arr[5] = 31 &gt; 23, so <b>high = mid − 1 = 4</b>.</p>" },
    { lo: 4, hi: 4, mid: 4, found: true, simple: "<p><b>Found it.</b> Only one page is left, and it says <b>23</b>.</p><p>We found it in just <b>3 looks</b>. Linear search could have needed 5.</p>", tech: "<p><b>mid = 4</b>, arr[4] == 23 → return <b>4</b>. Each step halves the range, so the time is <b>O(log n)</b>.</p>" }
  ];
  var i = 0, mode = "simple", track = document.getElementById("bsTrack"), text = document.getElementById("bsText");
  function draw() {
    var s = steps[i];
    track.innerHTML = arr.map(function (v, k) { var c = "bs-cell"; if (k < s.lo || k > s.hi) c += " out"; if (k === s.mid) c += s.found ? " found" : " mid"; return "<div class='" + c + "'>" + v + "</div>"; }).join("");
    text.innerHTML = s[mode];
    document.getElementById("bsStep").textContent = "Step " + (i + 1) + " of " + steps.length;
    document.getElementById("bsNext").disabled = i === steps.length - 1;
    document.getElementById("bsNext").style.opacity = i === steps.length - 1 ? .45 : 1;
  }
  document.getElementById("bsNext").addEventListener("click", function () { if (i < steps.length - 1) { i++; draw(); } });
  document.getElementById("bsReset").addEventListener("click", function () { i = 0; draw(); });
  document.querySelectorAll("#demo [data-mode]").forEach(function (b) {
    b.addEventListener("click", function () { mode = b.getAttribute("data-mode"); document.querySelectorAll("#demo [data-mode]").forEach(function (x) { x.classList.toggle("on", x === b); }); draw(); });
  });
  draw();
};
