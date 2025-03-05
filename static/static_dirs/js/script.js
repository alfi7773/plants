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



document.addEventListener("DOMContentLoaded", function () {
  let index = 0;
  const slides = document.querySelectorAll(".slide");
  const totalSlides = slides.length;
  const slidesContainer = document.querySelector(".slides");

  function showSlide(n) {
      index = (n + totalSlides) % totalSlides;
      slidesContainer.style.transform = `translateX(-${index * 100}%)`;
  }

  document.querySelector(".prev").addEventListener("click", function () {
      showSlide(index - 1);
  });

  document.querySelector(".next").addEventListener("click", function () {
      showSlide(index + 1);
  });

  setInterval(() => {
      showSlide(index + 1);
  }, 5000); 
});



document.addEventListener("DOMContentLoaded", function () {
  let minPrice = document.getElementById("price_min");
  let maxPrice = document.getElementById("price_max");
  let priceDisplay = document.getElementById("price_display");

  function updatePrice() {
      priceDisplay.textContent = `$${minPrice.value} - $${maxPrice.value}`;
  }

  minPrice.addEventListener("input", updatePrice);
  maxPrice.addEventListener("input", updatePrice);
});



document.querySelectorAll('.links a').forEach(link => {
  link.addEventListener('click', function () {
      document.querySelectorAll('.links a').forEach(el => el.classList.remove('active'));
      this.classList.add('active');
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


// const modal = document.getElementById('modal');
// const openModalBtn = document.getElementById('openModalBtn');
// const closeBtn = document.getElementsByClassName('close-btn')[0];

// const modal1 = document.getElementById('modal1');
// const openModalBtn1 = document.getElementById('openModalBtn1');
// const closeBtn1 = document.getElementsByClassName('close-btn1')[0];


// // модальное окно
// openModalBtn.onclick = function(event) {
//   event.stopPropagation(); 
//   modal.style.display = "block";
// }

// closeBtn.onclick = function() {
//   modal.style.display = "none";
// }


// window.onclick = function(event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
//   if (event.target == modal1) {
//     modal1.style.display = "none";
//   }
// }



// openModalBtn1.onclick = function(event) {
//   event.stopPropagation(); 
//   modal1.style.display = "block";
// }

// closeBtn1.onclick = function() {
//   modal1.style.display = "none";
// }

// window.onclick = function(event) {
//   if (event.target == modal1) {
//     modal1.style.display = "none";
//   }
// }




document.addEventListener("DOMContentLoaded", function () {  
  const loginModal = document.getElementById("loginModal");  
  const registerModal = document.getElementById("registerModal");  
  const openLoginModalBtn = document.getElementById("openLoginModal");  
  const openRegisterFromLoginBtn = document.getElementById("openRegisterFromLogin");  
  const closeLoginModalBtn = document.getElementById("closeLoginModal");  
  const closeRegisterModalBtn = document.getElementById("closeRegisterModal");  

  // Открыть модальное окно логина  
  openLoginModalBtn.addEventListener("click", () => {  
      loginModal.style.display = "block";  
  });  

  // Открыть модальное окно регистрации из модального окна логина  
  openRegisterFromLoginBtn.addEventListener("click", (event) => {  
      event.preventDefault(); // Предотвратить переход по ссылке  
      loginModal.style.display = "none"; // Скрыть модальное окно логина  
      registerModal.style.display = "block"; // Показать модальное окно регистрации  
  });  

  // Закрыть модальное окно логина  
  closeLoginModalBtn.addEventListener("click", () => {  
      loginModal.style.display = "none";  
  });  

  // Закрыть модальное окно регистрации  
  closeRegisterModalBtn.addEventListener("click", () => {  
      registerModal.style.display = "none";  
  });  

  // Закрыть модальные окна при клике вне модального окна  
  window.addEventListener("click", (event) => {  
      if (event.target === loginModal) {  
          loginModal.style.display = "none";  
      }  
      if (event.target === registerModal) {  
          registerModal.style.display = "none";  
      }  
  });  
});  



// document.addEventListener("DOMContentLoaded", function () {
//   const loginModal = document.getElementById("loginModal");
//   const registerModal = document.getElementById("registerModal");

//   document.getElementById("openLoginModal").addEventListener("click", function () {
//       loginModal.style.display = "block";
//   });

//   document.getElementById("openRegisterModal").addEventListener("click", function () {
//       registerModal.style.display = "block";
//   });

//   document.querySelectorAll(".close-btn").forEach(btn => {
//       btn.addEventListener("click", function () {
//           loginModal.style.display = "none";
//           registerModal.style.display = "none";
//       });
//   });

//   window.addEventListener("click", function (event) {
//       if (event.target === loginModal) loginModal.style.display = "none";
//       if (event.target === registerModal) registerModal.style.display = "none";
//   });
// });




// document.addEventListener("DOMContentLoaded", function () {
//   const loginModal = document.getElementById("loginModal1");
//   const registerModal = document.getElementById("registerModal1");

//   document.getElementById("openLoginModal1").addEventListener("click", function () {
//       loginModal.style.display = "block";
//   });

//   document.getElementById("openRegisterModal1").addEventListener("click", function () {
//       registerModal.style.display = "block";
//   });

//   document.querySelectorAll(".close-btn").forEach(btn => {
//       btn.addEventListener("click", function () {
//           loginModal.style.display = "none";
//           registerModal.style.display = "none";
//       });
//   });

//   window.addEventListener("click", function (event) {
//       if (event.target === loginModal1) loginModal.style.display = "none";
//       if (event.target === registerModal1) registerModal.style.display = "none";
//   });
// });



function changeImage(element) {
  document.getElementById('mainImage').src = element.src;
}

function selectSize(element) {
  document.querySelectorAll('.circle').forEach(el => el.classList.remove('selected'));
  element.classList.add('selected');
  document.getElementById('selectedSize').value = element.innerText;
}

function changeQuantity(amount) {
  let quantityInput = document.getElementById('quantity');
  let currentValue = parseInt(quantityInput.value, 10);
  if (currentValue + amount >= 1) {
    quantityInput.value = currentValue + amount;
  }
}