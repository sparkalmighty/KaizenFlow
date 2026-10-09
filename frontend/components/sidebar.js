document.addEventListener('DOMContentLoaded', function () {
  const mount = document.getElementById('sidebar-root');
  const pageName = document.body.dataset.page || 'dashboard';

  if (!mount) return;

  fetch('/components/sidebar.html')
    .then(function (response) {
      if (!response.ok) throw new Error('Sidebar file not found');
      return response.text();
    })
    .then(function (html) {
      mount.innerHTML = html;

      const activeItem = mount.querySelector('[data-page="' + pageName + '"]');
      if (activeItem) {
        activeItem.classList.add('active');
      }

      mount.querySelectorAll('[data-logout]').forEach(function (button) {
        button.addEventListener('click', function () {
          window.location.href = '/logout';
        });
      });
    })
    .catch(function (error) {
      console.error('Could not load sidebar:', error);
      mount.innerHTML = '<div class="sidebar-fallback">Sidebar unavailable</div>';
    });
});
