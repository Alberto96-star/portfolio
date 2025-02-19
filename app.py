from flask import Flask, render_template, redirect, url_for, request, jsonify
from decouple import config
from sendgrid.helpers.mail import *
from sendgrid import SendGridAPIClient
import sendgrid
import os


app = Flask(__name__)

# Configuración de las variables de entorno de Vercel
SENDGRID_KEY = os.environ.get('SENDGRID_KEY')
FROM_EMAIL = os.environ.get('FROM_EMAIL')

# Verifica si las variables de entorno están configuradas
if not SENDGRID_KEY or not FROM_EMAIL:
    raise ValueError("Las variables SENDGRID_KEY y FROM_EMAIL deben estar configuradas en Vercel.")

app.config.from_mapping(
        SENDGRID_KEY= 'SENDGRID_KEY'
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
        send_email(name, email, message)
        return render_template('partials/sent_mail.html')
    return render_template('partials/inicio.html') 


def send_email(name, email, message):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_KEY)
    from_email = Email(FROM_EMAIL)
    to_email = To(FROM_EMAIL, substitutions={
        "-name-": name,
        "-email-": email,
        "-message-": message,
    })

    html_content = """
        <p>Hola Alberto, tienes un nuevo contacto desde la web:</p>
        <p>Nombre: -name-</p>
        <p>Correo: -email-</p>
        <p>Mensaje: -message-</p>
    """
    email = Mail(from_email, to_email, 'Nuevo contacto desde la web', html_content=html_content)
    response = sg.send(email)

    
# la configuracion de debug debe estar al final
if __name__ == "__main__":
    app.run(debug=True)
