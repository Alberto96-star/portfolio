from flask import Flask, render_template, redirect, url_for, request
from decouple import config
from send_email import send_email


app = Flask(__name__)

app.config.from_mapping(
        SENDGRID_KEY=config('SENDGRID_KEY')
    )

@app.route('/')
def index():
    return render_template('partials/inicio.html')


@app.route('/proyectos')
def proyectos():
    return render_template('proyecto/proyectos.html')

@app.route('/mail', methods=['GET', 'POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if request.method == 'POST':
        send_email(name, email, message)
        return render_template('partials/sent_mail.html')
    
    return render_template('partials/inicio.html') 

# la configuracion de debug debe estar al final
if __name__ == "__main__":
    app.run(debug=True)
