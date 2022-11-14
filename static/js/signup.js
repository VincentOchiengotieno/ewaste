document.addEventListener('DOMContentLoaded', (e) =>{
    let user = document.querySelector('.container #header label[data-user]');
    let technician = document.querySelector('.container #header label[data-technician]');
    let company = document.querySelector('.container #header label[data-company]');

    user.addEventListener('click', addActive);
    technician.addEventListener('click', addActive);
    company.addEventListener('click', addActive);

})

let removeActive = () => {
    let tabs = document.querySelectorAll('.container #header > label')

    tabs.forEach((tab) => {
        tab.classList.remove('active')
    });
}

let addActive = (e) => {
    removeActive();

    e.target.classList.add('active');
}