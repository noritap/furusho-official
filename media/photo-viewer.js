const gallery = document.querySelector('#photo-gallery');
const viewer = gallery.querySelector('dialog');
const entries = [...gallery.querySelectorAll('.media-gallery-grid a[data-series]')];
const related = gallery.querySelector('template').content.querySelectorAll('a[data-series]');
const photo = viewer.querySelector('img');
const caption = viewer.querySelector('figcaption');
let opener;
let series = [];
let index = 0;
let touchStart = null;

function showPhoto(position) {
  index = (position + series.length) % series.length;
  const entry = series[index];
  const title = entry.dataset.caption || entry.closest('figure').querySelector('figcaption').textContent;
  photo.alt = entry.querySelector('img').alt;
  photo.src = entry.href;
  caption.textContent = `${title}　${index + 1} / ${series.length}`;
}

for (const entry of entries) {
  entry.addEventListener('click', event => {
    if (!viewer.showModal || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    opener = entry;
    series = [...entries, ...related].filter(item => item.dataset.series === entry.dataset.series);
    viewer.querySelector('h2').textContent = entry.dataset.series;
    showPhoto(series.indexOf(entry));
    viewer.showModal();
  });
}

for (const button of viewer.querySelectorAll('[data-direction]')) {
  button.addEventListener('click', () => showPhoto(index + Number(button.dataset.direction)));
}

viewer.querySelector('.photo-viewer-close').addEventListener('click', () => viewer.close());
viewer.addEventListener('close', () => opener?.focus());
viewer.addEventListener('keydown', event => {
  if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
  event.preventDefault();
  showPhoto(index + (event.key === 'ArrowRight' ? 1 : -1));
});

photo.addEventListener('touchstart', event => {
  touchStart = event.touches.length === 1 ? event.touches[0] : null;
}, { passive: true });
photo.addEventListener('touchend', event => {
  if (!touchStart) return;
  const end = event.changedTouches[0];
  const dx = end.clientX - touchStart.clientX;
  const dy = end.clientY - touchStart.clientY;
  touchStart = null;
  if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy)) showPhoto(index + (dx < 0 ? 1 : -1));
}, { passive: true });
photo.addEventListener('touchcancel', () => { touchStart = null; });
