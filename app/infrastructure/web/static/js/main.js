/**
 * main.js — comportements partagés sur toutes les pages
 * - Révélation des éléments au défilement (IntersectionObserver)
 * - Disparition automatique des messages flash de notification après 3 secondes
 */

(function () {
  "use strict";

// Fonction modifiée pour cibler .flash-bar
  function initFlashMessageFadeout() {
    // Changement du sélecteur pour correspondre à votre HTML
    var notifications = document.querySelectorAll(".flash-bar");
    if (!notifications.length) return;

    notifications.forEach(function (notification) {
      setTimeout(function () {
        // Applique l'effet de transition progressif (fondu)
        notification.style.transition = "opacity 0.5s ease-out";
        notification.style.opacity = "0";

        // Supprime l'élément du DOM après la fin de la transition (500 ms)
        setTimeout(function () {
          notification.remove();
        }, 500);
        
      }, 3000); // Déclenchement de l'effet après 3 secondes
    });
  }

  function initRevealOnScroll() {
    var items = document.querySelectorAll(".reveal");
    if (!items.length) return;

    if (!("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("is-visible"); });
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );

    items.forEach(function (el) { observer.observe(el); });
  }

  function staggerReveal() {
    var groups = document.querySelectorAll("[data-stagger]");
    groups.forEach(function (group) {
      var children = group.querySelectorAll(".reveal");
      children.forEach(function (child, index) {
        child.style.transitionDelay = (index * 70) + "ms";
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    staggerReveal();
    initRevealOnScroll();
    initFlashMessageFadeout(); // Appel de la nouvelle fonctionnalité
  });
})();