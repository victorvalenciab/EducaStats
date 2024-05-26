function Click(url)
{

    window.location.href = url;
        
}

// Obtenemos el header
const header = document.querySelector('header');

// Guardamos la altura del header
const headerHeight = header.offsetHeight;

// Posición del último scroll
let lastScrollTop = 0;

// Al hacer scroll
window.addEventListener('scroll', () => {
    // Posición actual del scroll
    let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    // Si el scroll es hacia abajo y no estamos en la parte superior de la página
    if (currentScroll > lastScrollTop && currentScroll > headerHeight) {
        // Ocultamos el header
        header.classList.add('hidden');
    } else {
        // Mostramos el header
        header.classList.remove('hidden');
    }

    // Guardamos la posición actual del scroll para comparar en el siguiente evento de scroll
    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
});

