from flask import Flask, render_template, redirect, url_for, request, jsonify, flash, session
from decouple import config
from sendgrid.helpers.mail import *
from sendgrid import SendGridAPIClient
import sendgrid
import os
import uuid


app = Flask(__name__)

# Configuración de las variables de entorno de Vercel
SENDGRID_KEY = os.environ.get('SENDGRID_KEY')
FROM_EMAIL = os.environ.get('FROM_EMAIL')

# Verifica si las variables de entorno están configuradas
if not SENDGRID_KEY or not FROM_EMAIL:
    raise ValueError(
        "Las variables SENDGRID_KEY y FROM_EMAIL deben estar configuradas en Vercel.")

app.config.from_mapping(
    SENDGRID_KEY=SENDGRID_KEY
)


@app.route('/', methods=['GET'])
def index():
    return render_template('partials/inicio.html')


@app.route('/proyectos')
def proyectos():
    return render_template('proyecto/proyectos.html')


@app.route('/mail', methods=['GET', 'POST'])
def mail():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Enviar correo
        send_email(name, email, message)

        # Importante: Redireccionar después del POST para evitar reenvíos
        return redirect(url_for('mail_success'))

    # Si la solicitud es GET, redirigir a la página de inicio
    return redirect(url_for('index'))


@app.route('/mail/success')
def mail_success():
    return render_template('partials/sent_mail.html')


def send_email(name, email, message):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_KEY)
    my_mail = FROM_EMAIL
    from_email = Email(FROM_EMAIL)
    to_email = To(my_mail, substitutions={
        "-name-": name,
        "-email-": email,
        "-message-": message,
    })

    html_content = """
        <p>Hola Alberto, tienes un nuevo contacto desde el portafilios:</p>
        <p>Nombre: -name-</p>
        <p>Correo: -email-</p>
        <p>Mensaje: -message-</p>
    """
    mail = Mail(my_mail, to_email, 'Contacto desde portafolio',
                html_content=html_content)
    response = sg.client.mail.send.post(request_body=mail.get())


# la configuracion de debug debe estar al final
if __name__ == "__main__":
    app.run(debug=True)
