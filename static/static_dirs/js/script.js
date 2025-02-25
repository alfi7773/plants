document.getElementById("menu-toggle").addEventListener("click", function () {
  var menu = document.getElementById("menu");
  menu.style.display = (menu.style.display === "block") ? "none" : "block";
});
const modal = document.getElementById('modal');
const openModalBtn = document.getElementById('openModalBtn');
const closeBtn = document.getElementsByClassName('close-btn')[0];

// Открыть модальное окно
openModalBtn.onclick = function(event) {
  event.stopPropagation(); // предотвратить всплытие события
  modal.style.display = "block";
}

// Закрыть модальное окно
closeBtn.onclick = function() {
  modal.style.display = "none";
}

// Закрыть модальное окно, если кликнуть за пределами модального окна
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
