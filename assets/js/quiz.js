/* Lightweight, dependency-free revision quizzes.
 *
 * Each quiz lives in a `<div class="quiz" data-quiz>` containing a
 * `<script type="application/json">` payload (emitted by build.py from a YAML
 * file). Questions and options are reshuffled on every run, an optional `pick`
 * shows a random subset, and a best score is kept in localStorage. */
(function () {
  "use strict";

  function shuffle(array) {
    for (var i = array.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = array[i];
      array[i] = array[j];
      array[j] = tmp;
    }
    return array;
  }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }

  function typeset(node) {
    if (window.MathJax && MathJax.typesetPromise) {
      MathJax.typesetPromise([node]).catch(function () {});
    }
  }

  function initQuiz(root) {
    var dataEl = root.querySelector('script[type="application/json"]');
    if (!dataEl) return;
    var data;
    try {
      data = JSON.parse(dataEl.textContent);
    } catch (e) {
      return;
    }
    var pool = data.questions || [];
    if (!pool.length) return;
    var pick = data.pick && data.pick < pool.length ? data.pick : pool.length;
    var storeKey = "gtquiz:" + (data.title || document.title);

    var questions = [];
    var index = 0;
    var score = 0;

    function start() {
      questions = shuffle(pool.slice())
        .slice(0, pick)
        .map(function (q) {
          return {
            q: q.q,
            explain: q.explain,
            options: shuffle((q.options || []).slice()),
          };
        });
      index = 0;
      score = 0;
      renderQuestion();
    }

    function renderQuestion() {
      var q = questions[index];
      root.innerHTML = "";
      var card = el("div", "quiz-card");
      card.appendChild(
        el("p", "quiz-progress", "Question " + (index + 1) + " of " + questions.length)
      );

      var prompt = el("p", "quiz-question");
      prompt.innerHTML = q.q;
      card.appendChild(prompt);

      var form = el("form", "quiz-options");
      q.options.forEach(function (opt, i) {
        var label = el("label", "quiz-option");
        var input = document.createElement("input");
        input.type = "radio";
        input.name = "opt";
        input.value = i;
        var span = document.createElement("span");
        span.innerHTML = opt.text;
        label.appendChild(input);
        label.appendChild(span);
        form.appendChild(label);
      });
      card.appendChild(form);

      var btn = el("button", "quiz-btn", "Check");
      btn.type = "button";
      btn.disabled = true;
      card.appendChild(btn);

      form.addEventListener("change", function () {
        btn.disabled = false;
      });

      btn.onclick = function () {
        var chosen = form.querySelector('input[name="opt"]:checked');
        if (!chosen) return;
        var choice = parseInt(chosen.value, 10);
        var labels = form.querySelectorAll(".quiz-option");
        form.querySelectorAll("input").forEach(function (i) {
          i.disabled = true;
        });
        q.options.forEach(function (opt, i) {
          if (opt.correct) labels[i].classList.add("quiz-correct");
          else if (i === choice) labels[i].classList.add("quiz-incorrect");
        });
        if (q.options[choice].correct) score++;

        if (q.explain) {
          var ex = el("p", "quiz-explain");
          ex.innerHTML = q.explain;
          card.insertBefore(ex, btn);
          typeset(ex);
        }

        btn.textContent =
          index < questions.length - 1 ? "Next question" : "See score";
        btn.onclick = function () {
          index++;
          if (index < questions.length) renderQuestion();
          else renderScore();
        };
      };

      root.appendChild(card);
      typeset(card);
    }

    function renderScore() {
      var total = questions.length;
      var pct = Math.round((100 * score) / total);
      var best = pct;
      try {
        best = Math.max(pct, parseInt(localStorage.getItem(storeKey) || "0", 10));
        localStorage.setItem(storeKey, String(best));
      } catch (e) {}

      root.innerHTML = "";
      var card = el("div", "quiz-card");
      card.appendChild(
        el(
          "p",
          "quiz-score",
          "You scored " + score + " out of " + total + " (" + pct + "%). Best so far: " + best + "%."
        )
      );
      var btn = el("button", "quiz-btn", "Try again");
      btn.type = "button";
      btn.onclick = start;
      card.appendChild(btn);
      root.appendChild(card);
    }

    start();
  }

  document.querySelectorAll("[data-quiz]").forEach(initQuiz);
})();
