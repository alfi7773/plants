document.getElementById("menu-toggle").addEventListener("click", function () {
  var menu = document.getElementById("menu");
  menu.style.display = (menu.style.display === "block") ? "none" : "block";
});


function toggleFilter() {
  document.querySelector(".filter-menu").classList.toggle("active");
}

// Получаем элементы кнопки и меню
const menuToggleButton = document.getElementById('menu-toggle');
const menu = document.getElementById('menu');

// Добавляем обработчик события для кнопки
menuToggleButton.addEventListener('click', () => {
  // Переключаем класс 'active', чтобы показать или скрыть меню
  menu.classList.toggle('active');
});


const modal = document.getElementById('modal');
const openModalBtn = document.getElementById('openModalBtn');
const closeBtn = document.getElementsByClassName('close-btn')[0];

const modal1 = document.getElementById('modal1');
const openModalBtn1 = document.getElementById('openModalBtn1');
const closeBtn1 = document.getElementsByClassName('close-btn1')[0];


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
// window.onclick = function(event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// }

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
  if (event.target == modal1) {
    modal1.style.display = "none";
  }
}



openModalBtn1.onclick = function(event) {
  event.stopPropagation(); 
  modal1.style.display = "block";
}

closeBtn1.onclick = function() {
  modal1.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal1) {
    modal1.style.display = "none";
  }
}
