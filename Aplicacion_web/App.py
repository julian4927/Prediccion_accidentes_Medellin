from flask import Flask , render_template
from Scripts.funciones import *

barrios = lista_valores_unicos('BARRIO')
tipos_accidentes = lista_valores_unicos('CLASE_ACCIDENTE')


app = Flask(__name__)

@app.route("/")
def inicio():
    for barrio in barrios:
        print(barrio)
    return render_template('inicio.html')

@app.route("/historico")
def historico():
    for tipos_accidente in tipos_accidentes:
        print(tipos_accidente)
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


