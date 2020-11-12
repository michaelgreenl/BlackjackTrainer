let navAccountBtn = document.getElementById('nav-account-btn');
let navDropdown = document.getElementById('navbar-dropdown');

navDropdown.style.display = 'none';

document.body.addEventListener('click', function () {
    if (navDropdown.style.display === 'flex') {
        navDropdown.style.display = 'none';
    }
}, false);

navAccountBtn.addEventListener('click', function (ev) {
    if (navDropdown.style.display === 'none') {
        navDropdown.style.display = 'flex';
    } else if (navDropdown.style.display === 'flex') {
        navDropdown.style.display = 'none';
    }
    ev.stopPropagation();
}, false);


let alert = document.getElementById('alert');

if (alert !== null) {
    document.body.addEventListener('click', function () {
        alert.style.display = 'none';
    });
    navAccountBtn.addEventListener('click', function () {
        alert.style.display = 'none';
    });
}

let playBtn = document.getElementById('play-btn');
let rulesBtn = document.getElementById('rules-btn');


