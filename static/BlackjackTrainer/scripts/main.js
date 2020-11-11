import mainScene from "./mainScene.js";

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

// let playBtn = document.getElementById('play-btn');
// let rulesBtn = document.getElementById('rules-btn');
//
// const config = {
//     type: Phaser.AUTO,
//     width: '100%',
//     height: '100%',
//     backgroundColor: '#FDFEF6',
//     physics: {
//         default: 'arcade',
//         arcade: {
//             debug: false,
//         }
//     },
//     scene: [mainScene],
// };
//
// playBtn.addEventListener('click', function () {
//     const game = new Phaser.Game(config);
//     game.scene.start('mainScene');
// });
//
// let canvas = document.getElementsByTagName("canvas");


