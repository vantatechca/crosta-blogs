/* Crosta motion layer. No-op (everything stays visible) if JS is off or the
   visitor prefers reduced motion. */
(function () {
  var mq = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)');
  if (mq && mq.matches) return;
  var root = document.documentElement;
  root.classList.add('anim');

  function ready(fn){ document.readyState !== 'loading' ? fn() : document.addEventListener('DOMContentLoaded', fn); }

  ready(function () {
    var targets = Array.prototype.slice.call(
      document.querySelectorAll('main.wrap > *:not([data-no-reveal])')
    );
    targets.forEach(function (el) { el.classList.add('reveal'); });

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          var el = e.target;
          el.style.transitionDelay = ((+el.dataset.crI || 0) * 70) + 'ms';
          el.classList.add('in');
          io.unobserve(el);
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
      targets.forEach(function (el, i) { el.dataset.crI = i % 5; io.observe(el); });
    } else {
      targets.forEach(function (el) { el.classList.add('in'); });
    }

    var bi = document.querySelector('.cr-banner__inner');
    if (bi) requestAnimationFrame(function () { bi.classList.add('in'); });

    var fab = document.querySelector('.cr-fab');
    if (fab) setTimeout(function () { fab.classList.add('show'); }, 400);

    var media = document.querySelector('.cr-banner__media');
    if (media) {
      var ticking = false;
      window.addEventListener('scroll', function () {
        if (ticking) return; ticking = true;
        requestAnimationFrame(function () {
          var y = window.pageYOffset || 0;
          media.style.transform = 'translateY(' + Math.min(y * 0.22, 70) + 'px)';
          ticking = false;
        });
      }, { passive: true });
    }
  });
})();
