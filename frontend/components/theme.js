(function () {
  var storageKey = 'kaizenflow-theme';
  var root = document.documentElement;

  function applyTheme(theme) {
    if (theme === 'dark') {
      root.setAttribute('data-theme', 'dark');
    } else {
      root.removeAttribute('data-theme');
    }
  }

  try {
    applyTheme(localStorage.getItem(storageKey));
  } catch (error) {
    applyTheme('light');
  }

  document.addEventListener('click', function (event) {
    var toggle = event.target.closest('[data-theme-toggle]');
    if (!toggle) return;

    var nextTheme = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    try {
      localStorage.setItem(storageKey, nextTheme);
    } catch (error) {
      // Keep the current-page toggle working when browser storage is unavailable.
    }
    applyTheme(nextTheme);
  });
})();
