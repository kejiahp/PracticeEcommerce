let themeControl = document.querySelector('.themeControl');
let menuControl = document.querySelector('.menuControl');
let boby = document.querySelector('body');
let menus = document.querySelector('.menus');

//register page
let register_alert = document.querySelector('.register-alert');
let alert_close = document.querySelector('.alert-close');

themeControl.onclick = function(){
    themeControl.classList.toggle('active');
    boby.classList.toggle('dark');
}
menuControl.onclick = function(){
    menuControl.classList.toggle('active');
    menus.classList.toggle('menu-slide');
}
alert_close.onclick = function(){
    register_alert.style.display="none";
    console.log("Successfully done!");
}