document.addEventListener('DOMContentLoaded', () => {
    let content = document.querySelector('.col-lg-4');
    let right = document.querySelector('.row #right');
    let left = document.querySelector('.row #left');

    right.addEventListener('click', () => {
        content.style.transform = "translateX('-120px')";
    })
    left.addEventListener('click', () => {
        content.style.transform = "translateX('-120px')";
    })
})