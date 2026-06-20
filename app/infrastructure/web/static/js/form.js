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
        clearAuthorError();
      } else if (authorInput.dataset.previousValue) {
        authorInput.value = authorInput.dataset.previousValue;
      }
    }

    checkbox.addEventListener("change", sync);
    sync();
  }

  function clearAuthorError() {
    var authorInput = document.querySelector("[data-author-input]");
    var hint = document.querySelector("[data-author-hint]");
    if (authorInput) authorInput.classList.remove("has-error");
    if (hint) hint.hidden = true;
  }

  function initPublishValidation() {
    var form = document.querySelector("[data-publish-form]");
    var authorInput = document.querySelector("[data-author-input]");
    var checkbox = document.querySelector("[data-anonymous-toggle]");
    var hint = document.querySelector("[data-author-hint]");
    var submitBtn = document.querySelector("[data-submit-btn]");
    if (!form || !authorInput || !checkbox || !hint) return;

    form.addEventListener("submit", function (event) {
      var nameMissing = authorInput.value.trim().length === 0;
      var notAnonymous = !checkbox.checked;

      if (nameMissing && notAnonymous) {
        event.preventDefault();
        authorInput.classList.add("has-error");
        hint.hidden = false;
        authorInput.focus();
        return;
      }

      clearAuthorError();
      setSubmitLoading(submitBtn);
    });

    authorInput.addEventListener("input", function () {
      if (authorInput.value.trim().length > 0) clearAuthorError();
    });
  }

  function setSubmitLoading(button) {
    if (!button || button.classList.contains("is-loading")) return;

    var label = button.querySelector("span");
    var loadingText = button.getAttribute("data-loading-text") || "Envoi en cours…";

    if (label) {
      button.dataset.originalText = label.textContent;
      label.textContent = loadingText;
    }

    button.classList.add("is-loading");
    button.disabled = true;
    button.setAttribute("aria-busy", "true");
  }

  document.addEventListener("DOMContentLoaded", function () {
    initCharCounter();
    initAnonymousToggle();
    initPublishValidation();
  });
})();