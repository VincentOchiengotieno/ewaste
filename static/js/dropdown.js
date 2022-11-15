document.addEventListener('DOMContentLoaded', () => {
    let btnsignup = document.querySelector('button.register');	
    let dropdown = document.getElementById('dropdown');

    btnsignup.addEventListener('click',() => {
        dropdown.click();
    })
    btnsignup.addEventListener('blur', () => {
        dropdown.checked = false;
    })
})
