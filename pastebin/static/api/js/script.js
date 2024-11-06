// document.getElementById('save-button').addEventListener('click', function() {
//     let textBlock = document.getElementById('text-block').value;
//     if (textBlock.trim() === "") {
//         alert("Text block cannot be empty!");
//         return;
//     }
//
//     let hash = Math.random().toString(36).substring(2, 15);
//
//     localStorage.setItem(hash, textBlock);
//
//     let link = document.createElement('div');
//     link.innerHTML = `<a href="?hash=${hash}" target="_blank">Link: ${window.location.href}?hash=${hash}</a>`;
//     document.getElementById('links-list').appendChild(link);
//
//     document.getElementById('text-block').value = "";
//
//     // Добавляем всплывающее уведомление
//     alert('Text block saved successfully!');
// });
//
// window.onload = function() {
//     let urlParams = new URLSearchParams(window.location.search);
//     let hash = urlParams.get('hash');
//     if (hash) {
//         let textBlock = localStorage.getItem(hash);
//         if (textBlock) {
//             document.body.innerHTML = `<div class="container"><pre>${textBlock}</pre></div>`;
//         } else {
//             document.body.innerHTML = `<div class="container"><p>Text block not found or has expired.</p></div>`;
//         }
//     }
// };