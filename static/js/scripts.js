document.addEventListener('DOMContentLoaded', function () {
    // Código existente para el formulario
    const form = document.querySelector('.contact-form');

    if (form) {
        // Variable para rastrear si el formulario ya se envió
        let formSubmitted = false;

        // Agregar listener al evento submit
        form.addEventListener('submit', function (event) {
            // Si el formulario ya fue enviado, prevenir el envío
            if (formSubmitted) {
                event.preventDefault();
                return false;
            }

            // Marcar el formulario como enviado
            formSubmitted = true;

            // Desactivar el botón de envío
            const submitButton = form.querySelector('button');
            submitButton.disabled = true;
            submitButton.textContent = 'Enviando...';

            // Permitir que el formulario se envíe
            return true;
        });
    }

    // Código nuevo para navegación responsive
    // Crear el botón de menú hamburguesa para móvil
    const header = document.querySelector('header');
    const nav = document.querySelector('.nav-btn');

    // Solo crear el botón si no existe aún y si existe el nav
    if (nav && !document.querySelector('.menu-toggle')) {
        const menuToggle = document.createElement('button');
        menuToggle.className = 'menu-toggle';
        menuToggle.innerHTML = '☰';
        menuToggle.setAttribute('aria-label', 'Menú de navegación');

        // Insertar botón antes del nav
        header.insertBefore(menuToggle, nav);

        // Añadir clase para controlar la visibilidad inicial del menú
        nav.classList.add('nav-closed');

        // Toggle de menú
        menuToggle.addEventListener('click', function () {
            nav.classList.toggle('nav-open');
            nav.classList.toggle('nav-closed');

            // Cambiar ícono según estado
            this.innerHTML = nav.classList.contains('nav-open') ? '✕' : '☰';
        });

        // Cerrar menú al hacer clic en un link
        const navLinks = nav.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 768) {
                    nav.classList.remove('nav-open');
                    nav.classList.add('nav-closed');
                    menuToggle.innerHTML = '☰';
                }
            });
        });
    }
});