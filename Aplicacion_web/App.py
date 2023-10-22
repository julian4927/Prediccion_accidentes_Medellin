from flask import Flask , render_template, request
from Scripts.funciones import *

barrios = lista_valores_unicos('BARRIO')
tipos_accidentes = lista_valores_unicos('CLASE_ACCIDENTE')


app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('inicio.html')

@app.route("/historico", methods=["GET", "POST"])
def historico():
    # Configura las variables de selección con valores predeterminados
    selected_fecha_inicio = request.form.get("fecha-inicio")
    selected_fecha_fin = request.form.get("fecha-fin")
    selected_barrio = request.form.get("barrio")
    selected_tipo_accidente = request.form.get("tipo-accidente")
    
    mostrar_mapa = False  # Inicialmente, no se mostrará el mapa
    
    # Si se realiza una solicitud POST al presionar el botón "Filtrar datos", se generará el mapa aquí
    if request.method == "POST" and request.form.get("filtrar"):
        mapa = crear_mapa_todo()  # Reemplaza esto con la lógica para generar el mapa
        mostrar_mapa = True

    # Renderiza la plantilla historico.html
    return render_template('historico.html', barrios=barrios, tipos_accidentes=tipos_accidentes,
                           selected_fecha_inicio=selected_fecha_inicio, selected_fecha_fin=selected_fecha_fin,
                           selected_barrio=selected_barrio, selected_tipo_accidente=selected_tipo_accidente,
                           mostrar_mapa=mostrar_mapa)


@app.route("/prediccion")
def prediccion():
    return render_template('prediccion.html')

@app.route("/agrupamiento")
def agrupamiento():
    return render_template('agrupamiento.html')

@app.route("/enlaces")
def enlaces():
    return render_template('enlaces.html')


