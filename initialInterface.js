document.addEventListener('DOMContentLoaded', () => {
    const buttonHeader = document.querySelector('.mainButton');
    buttonHeader.addEventListener('click', (e) => hideMainButton(e));
})

function hideMainButton(e) {
    const header = document.querySelector('header');
    header.remove();
    return
}