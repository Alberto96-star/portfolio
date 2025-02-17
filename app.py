from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('inicio.html')


# la configuracion de debug debe estar al final
if __name__ == "__main__":
    app.run(debug=True)
