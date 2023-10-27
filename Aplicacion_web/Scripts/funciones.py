import pandas as pd
import folium
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import geopandas as gpd
from IPython.display import IFrame
from datetime import datetime, date, timedelta
import holidays_co

def lista_valores_unicos(columna):
    datos = pd.read_csv("data/data_limpia.csv",  sep=",", decimal=".")
    valores_distintos = datos[f'{columna}'].unique()
    return valores_distintos

def style_function(feature):
    return {
        'color': 'black',  # Color de las líneas
        'weight': 0.5  # Grosor de las líneas (ajusta este valor)
    }

def crear_mapa_todo():
  barrios_med = gpd.read_file('data/Barrios de Medellín/Barrio_Vereda.dbf')
  mapa = folium.Map(width=910, height=410, zoom_start=12, location=[6.27,-75.60])
  folium.TileLayer('openstreetmap').add_to(mapa)
  folium.GeoJson(data = barrios_med,style_function=style_function,
               name = 'NOMBRE',
               popup = folium.GeoJsonPopup(
                  fields = ['CODIGO', 'NOMBRE'],
                  aliases = ['Cod.', 'Barrio']
               )
               ).add_to(mapa)
  #folium.GeoJson(data = barrios_med,style_function=style_function).add_to(mapa)
  mapa.save('templates/mapa_sincolores.html')
  return mapa

def lista_cluster(cluster):
   datos = pd.read_csv("data/final_clusters.csv",  sep=",", decimal=".")
   datos_cluster = datos[datos['cluster'] == cluster] 
   lista_cluster = datos_cluster['barrio'].tolist()
   return lista_cluster

def prediccion_modelo(fecha_inicial, fecha_final):
   df = pd.read_csv("data/validacion.csv",  sep=",", decimal=".")
   df['fecha'] = pd.to_datetime(df['fecha'])
   inicio = datetime.strptime(fecha_inicial, '%Y/%m/%d')
   fin = datetime.strptime(fecha_final, '%Y/%m/%d')
   mask = (df['fecha'] >= inicio) & (df['fecha'] <= fin)
   accidentes = df.loc[mask]['prediccion'].sum()
   accidentes_entero = int(accidentes)
   return    accidentes_entero
