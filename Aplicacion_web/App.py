from flask import Flask , render_template, request
from Scripts.funciones import *

barrios = lista_valores_unicos('BARRIO')
tipos_accidentes = lista_valores_unicos('CLASE_ACCIDENTE')


app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('inicio.html')

@app.route("/historico",methods=['GET', 'POST'])
def historico():
    fecha_inicio = ""
    fecha_fin = ""
    barrio = ""
    tipo_accidente = ""
    mostrar_mapa = False
    diccionario = {'barrios':barrios,'tipos_accidentes':tipos_accidentes}
    if request.method == 'POST':
        if 'Filtrar' in request.form['submit_button']:
            fecha_inicio = request.form.get("fecha-inicio")
            fecha_fin = request.form.get("fecha-fin")
            barrio = request.form.get("barrio")
            tipo_accidente = request.form.get("tipo-accidente")
            mapa = crear_mapa_todo()
            mostrar_mapa = True
        elif 'Borrar filtros' in request.form['submit_button']:
            fecha_inicio = ""
            fecha_fin = ""
            barrio = ""
            tipo_accidente = ""
            mostrar_mapa = False
    diccionario['fecha_inicio'] = fecha_inicio
    diccionario['fecha_fin'] = fecha_fin
    diccionario['barrio'] = barrio
    diccionario['tipo_accidente'] = tipo_accidente
    diccionario['mostrar_mapa'] = mostrar_mapa

    return render_template('historico.html',datos = diccionario)



@app.route("/prediccion")
def prediccion():
    return render_template('prediccion.html')

@app.route("/agrupamiento")
def agrupamiento():
    return render_template('agrupamiento.html')

@app.route("/enlaces")
def enlaces():
    return render_template('enlaces.html')


