document.addEventListener('DOMContentLoaded', () => {
    let btnsignup = document.querySelector('button.register');	
    let dropdown = document.getElementById('dropdown');

    let user = document.querySelector('#user')
    let technician = document.querySelector('#technician')
    let company = document.querySelector('#company')


    btnsignup.addEventListener('click',() => {
        dropdown.click();
    })
    btnsignup.addEventListener('blur', () => {
        dropdown.checked = false;
    })
})
