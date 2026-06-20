/**
 * form.js — comportements de la page de dépôt
 * - Compteur de caractères sur le message
 * - Désactive/efface le champ nom quand "anonyme" est coché
 */

(function () {
  "use strict";

  function initCharCounter() {
    var textarea = document.querySelector("[data-counter-target]");
    var counter = document.querySelector("[data-counter]");
    if (!textarea || !counter) return;

    var min = parseInt(textarea.getAttribute("minlength") || "0", 10);

    function update() {
      var len = textarea.value.length;
      counter.textContent = len + " caractère" + (len > 1 ? "s" : "");
      counter.classList.toggle("has-text-grey-light", len < min);
    }

    textarea.addEventListener("input", update);
    update();
  }

  function initAnonymousToggle() {
    var checkbox = document.querySelector("[data-anonymous-toggle]");
    var authorInput = document.querySelector("[data-author-input]");
    if (!checkbox || !authorInput) return;

    function sync() {
      authorInput.disabled = checkbox.checked;
      if (checkbox.checked) {
        authorInput.dataset.previousValue = authorInput.value;
        authorInput.value = "";
      } else if (authorInput.dataset.previousValue) {
        authorInput.value = authorInput.dataset.previousValue;
      }
    }

    checkbox.addEventListener("change", sync);
    sync();
  }

  document.addEventListener("DOMContentLoaded", function () {
    initCharCounter();
    initAnonymousToggle();
  });
})();