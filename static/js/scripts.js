document.addEventListener('DOMContentLoaded', function () {
    // Obtener el formulario
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
});