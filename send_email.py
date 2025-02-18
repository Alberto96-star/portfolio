from decouple import config
from sendgrid.helpers.mail import *
from sendgrid import SendGridAPIClient
import sendgrid
import os

def send_email(name, email, message):
    mi_email = config('FROM_EMAIL')
    sg = sendgrid.SendGridAPIClient(api_key=config('SENDGRID_KEY'))
    from_email = Email(mi_email)
    to_email = To(mi_email, substitutions={
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
    mail = Mail(mi_email, to_email, 'Nuevo contacto desde la web', html_content=html_content)
    response = sg.client.mail.send.post(request_body=mail.get())

    