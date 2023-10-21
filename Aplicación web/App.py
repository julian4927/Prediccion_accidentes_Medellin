from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('inicio.html')

@app.route("/historico")
def historico():
    return render_template('historico.html')

@app.route("/prediccion")
def prediccion():
    return render_template('prediccion.html')

@app.route("/agrupamiento")
def agrupamiento():
    return render_template('agrupamiento.html')

@app.route("/enlaces")
def enlaces():
    return render_template('enlaces.html')


