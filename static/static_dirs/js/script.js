document.getElementById("menu-toggle").addEventListener("click", function () {
  var menu = document.getElementById("menu");
  menu.style.display = (menu.style.display === "block") ? "none" : "block";
});

document.addEventListener("DOMContentLoaded", function () {
  let searchForm = document.getElementById("search-form");
  let searchInput = document.getElementById("search-input");
  let searchIcon = document.getElementById("search-icon");

  if (searchInput.value.trim() !== "") {
      searchForm.style.display = "block";
  }

  searchIcon.addEventListener("click", function () {
      searchForm.style.display = "block";
      searchInput.focus();
  });
});


function toggleFilter() {
  document.querySelector(".filter-menu").classList.toggle("active");
}

const menuToggleButton = document.getElementById('menu-toggle');
const menu = document.getElementById('menu');

menuToggleButton.addEventListener('click', () => {
  menu.classList.toggle('active');
});


const modal = document.getElementById('modal');
const openModalBtn = document.getElementById('openModalBtn');
const closeBtn = document.getElementsByClassName('close-btn')[0];

const modal1 = document.getElementById('modal1');
const openModalBtn1 = document.getElementById('openModalBtn1');
const closeBtn1 = document.getElementsByClassName('close-btn1')[0];


// модальное окно
openModalBtn.onclick = function(event) {
  event.stopPropagation(); // предотвратить всплытие события
  modal.style.display = "block";
}

closeBtn.onclick = function() {
  modal.style.display = "none";
}


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
