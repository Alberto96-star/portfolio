from flask import Flask, render_template, redirect, url_for

import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyecto/proyectos.html')


# la configuracion de debug debe estar al final
if __name__ == "__main__":
    app.run(debug=True)
