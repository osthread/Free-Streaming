'use strict';

/**
 * navbar variables
 */

const navOpenBtn = document.querySelector("[data-menu-open-btn]");
const navCloseBtn = document.querySelector("[data-menu-close-btn]");
const navbar = document.querySelector("[data-navbar]");
const overlay = document.querySelector("[data-overlay]");

const navElemArr = [navOpenBtn, navCloseBtn, overlay];

for (let i = 0; i < navElemArr.length; i++) {

  navElemArr[i].addEventListener("click", function () {

    navbar.classList.toggle("active");
    overlay.classList.toggle("active");
    document.body.classList.toggle("active");

  });

}


/**
 * header sticky
 */

const header = document.querySelector("[data-header]");

window.addEventListener("scroll", function () {

  window.scrollY >= 10 ? header.classList.add("active") : header.classList.remove("active");

});



/**
 * go top
 */

const goTopBtn = document.querySelector("[data-go-top]");

window.addEventListener("scroll", function () {

  window.scrollY >= 500 ? goTopBtn.classList.add("active") : goTopBtn.classList.remove("active");

});

function toggleSearch() {
  var searchDropdown = document.getElementById('search-dropdown');
  if (searchDropdown.style.display === 'none') {
      searchDropdown.style.display = 'block';
  } else {
      searchDropdown.style.display = 'none';
  }
}

function toggleSearch() {
  var searchDropdown = document.getElementById('search-dropdown');
  if (searchDropdown.style.display === 'none') {
      searchDropdown.style.display = 'block';
  } else {
      searchDropdown.style.display = 'none';
  }
}

// Optional: Hide the dropdown when clicking outside of it
window.onclick = function(event) {
  if (!event.target.matches('.search-icon-container') && !event.target.matches('.search-icon-container *')) {
      var dropdowns = document.getElementsByClassName("search-dropdown");
      for (var i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.style.display === 'block') {
              openDropdown.style.display = 'none';
          }
      }
  }
}
