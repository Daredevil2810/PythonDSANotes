/* Behaviour for the pre-rendered (static) lesson/program pages: syntax highlighting, copy buttons,
   "mark as completed" and bookmarks. The page content itself is plain HTML, so it works for crawlers without JS. */
window.PyDSA_page = function (api) {
  var $$ = function (s) { return Array.prototype.slice.call(document.querySelectorAll(s)); };
  // the <base> tag would send "#main" to the site root; point it at this page instead
  var skip = document.querySelector(".skip-link"); if (skip) skip.setAttribute("href", location.pathname + "#main");
  // highlight code (the raw HTML keeps plain text so search engines can read it)
  $$("[data-code]").forEach(function (el) { if (!el.hasAttribute("data-plain") && window.PyDSA) el.innerHTML = PyDSA.highlight(el.textContent); });
  $$("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var txt = b.closest(".code-box").querySelector("code").textContent;
      (navigator.clipboard ? navigator.clipboard.writeText(txt) : Promise.reject()).then(function () { b.textContent = "Copied ✓"; }, function () { b.textContent = "Select & copy"; });
      setTimeout(function () { b.textContent = "Copy code"; }, 1500);
    });
  });
  $$("[data-done]").forEach(function (b) {
    var key = b.getAttribute("data-done"), what = b.getAttribute("data-done-label") || "Item";
    function draw() { var y = api.isDone(key); b.classList.toggle("is-done", y); b.textContent = y ? "✓ " + what + " completed" : "Mark as completed"; }
    b.addEventListener("click", function () { api.toggleDone(key); draw(); document.dispatchEvent(new CustomEvent("pydsa:progress")); });
    draw();
  });
  $$("[data-bm]").forEach(function (b) {
    var parts = b.getAttribute("data-bm").split(":"), type = parts[0], id = parts.slice(1).join(":"), label = b.getAttribute("data-bm-label") || "Bookmark";
    function draw() { var y = api.isBookmarked(type, id); b.classList.toggle("is-bookmarked", y); b.setAttribute("aria-pressed", y); b.textContent = (y ? "★ Bookmarked" : "☆ " + label); }
    b.addEventListener("click", function () { api.toggleBookmark(type, id); draw(); });
    draw();
  });
  var last = document.querySelector("[data-done^='lesson-']"); if (last) api.store.set("lastLesson", last.getAttribute("data-done").slice(7));
};
