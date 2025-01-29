let btnMenu = document.getElementById('btn-menu');
let menu = document.getElementById('menu-mobile');
let overley = document.getElementById('overlay-menu');

btnMenu.addEventListener('click', function() {
    menu.classList.add('abrir-menu');
});

menu.addEventListener('click', function() {
    menu.classList.remove('abrir-menu');
});

overley.addEventListener('click', function() {
    menu.classList.remove('abrir-menu');
});