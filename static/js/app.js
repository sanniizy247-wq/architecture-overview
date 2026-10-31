document.addEventListener('DOMContentLoaded', function () {
  const navToggle = document.querySelector('.nav-toggle');
  const mainNav = document.querySelector('.main-nav');
  const yearEl = document.querySelector('#year');

  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  if (navToggle && mainNav) {
    navToggle.addEventListener('click', function () {
      const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', String(!isExpanded));
      mainNav.classList.toggle('is-open');
    });
  }
});
