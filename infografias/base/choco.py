import pandas as pd
import numpy as np
from datetime import date, timedelta
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go

df = pd.read_csv('/Users/andresmauriciotrianareina/Documents/GitHub/datainfografias/Propuesta_levantamiento_información_V1.csv')
#df = pd.read_csv('https://raw.githubusercontent.com/andrestrianareina/datainfografias/master/Propuesta_levantamiento_información_V1.csv')




# Se extrae los datos de la Choco

choco = df[df['Departamento'] == 'CHOCO']


# Se cambian algunos nombres de de municipios para usar en el mapa

# guajira['Municipio'].replace(
#     to_replace=['ALBANIA'],
#     value='ALBANIA_g',
#     inplace=True
# )


# guajira['Municipio'].replace(
#     to_replace=['VILLANUEVA'],
#     value='VILLA_NUEVA',
#     inplace=True
# )

# guajira['Municipio'].replace(
#     to_replace=['DISTRACCION'],
#     value='DISTRACCIÓN',
#     inplace=True
# )


##########################
###### covid
 
#Contagios

covid_contagios_choco = choco[choco['Subtema'] == 'Contagio']
covid_contagios_total_choco = "{:,.0f}".format(covid_contagios_choco['No. De personas/porcentaje/eventos'].sum())


# Fallecidos

covid_fallecidos_choco = choco[choco['Subtema'] == 'Fallecido']
covid_fallecidos_total_choco = "{:,.0f}".format(covid_fallecidos_choco['No. De personas/porcentaje/eventos'].sum())


# Recuperados

covid_recuperados_choco = choco[choco['Subtema'] == 'Recuperado']
covid_recuperados_total_choco = "{:,.0f}".format(covid_recuperados_choco['No. De personas/porcentaje/eventos'].sum())


# activos

covid_activos_choco = choco[choco['Subtema'] == 'Activo']
covid_activos_total_choco = "{:,.0f}".format(covid_activos_choco['No. De personas/porcentaje/eventos'].sum())


# Sin clasificar

covid_sinclasificar_choco= choco[choco['Subtema'] == 'Sin clasificar']
covid_sinclasificar_total_choco = "{:,.0f}".format(covid_sinclasificar_choco['No. De personas/porcentaje/eventos'].sum())


# conexión json para el mapa

import json
from urllib.request import urlopen
#with urlopen('https://raw.githubusercontent.com/caticoa3/colombia_mapa/master/co_2018_MGN_MPIO_POLITICO.geojson') as response:
with urlopen('https://raw.githubusercontent.com/andresmtr/mapa_municipios_colombia_geojonson/master/co_2018_MGN_MPIO_POLITICO_AT.geojson') as response:
    counties = json.load(response)

# Mapa covid contagios

locs = covid_contagios_choco['Municipio']


for loc in counties['features']:
    loc['id'] = loc['properties']['MPIO_CNMBR']
map_choco = go.Figure(go.Choroplethmapbox(
                    geojson=counties,
                    locations=locs,
                    z=covid_contagios_choco['No. De personas/porcentaje/eventos'],
                    colorscale='plotly3',
                    colorbar_title="Total contagios"))
map_choco.update_layout(mapbox_style="carto-positron",
                        mapbox_zoom=6.7,
                        mapbox_center = {"lat": 11.5, "lon": -73})

locs_choco = covid_contagios_choco['Municipio'].tolist()
z_choco=covid_contagios_choco['No. De personas/porcentaje/eventos'].tolist()


##########################
###### migración

# migrantes venezolanos

migracion_choco = choco[choco['Subtema'] == 'Número de Migrantes venezolanos']
migracion_choco_numero = "{:,.0f}".format(migracion_choco['No. De personas/porcentaje/eventos'].sum())

# porcentaje a nivel nacional
migracion_choco = choco[choco['Subtema'] == 'Porcentaje de Migrantes venezolanos ( comparado contra el nivel nacional)']
migracion_porcentaje_choco = "{:,.2%}".format(migracion_choco['No. De personas/porcentaje/eventos'].sum())

# primero la niñez

migracion_pn_choco = choco[choco['Subtema'] == 'Número de niños con con registro de nacimiento bajo el programa - Primero la niñez']
migracion_pn_numero_choco = "{:,.0f}".format(migracion_pn_choco['No. De personas/porcentaje/eventos'].sum())

# porcentaje primero la niñez

migracion_pn_porcentaje_choco = choco[choco['Subtema'] == 'Porcentaje de niños con con registro de nacimiento bajo el programa - Primero la niñez comparado a nivel nacional']
migracion_pn_porcentaje_choco = "{:,.2%}".format(migracion_pn_porcentaje_choco['No. De personas/porcentaje/eventos'].sum())

##########################
###### educación

# Numero de matriculados
educacion_choco = choco[choco['Subtema'] == 'Número de matriculas en el 2021']
educacion_choco_numero = "{:,.0f}".format(educacion_choco['No. De personas/porcentaje/eventos'].sum())

# porcentaje a nivel nacional
educacion_choco = choco[choco['Subtema'] == 'Porcenaje de matriculas en el 2021 ( comparado frente al nivel nacional)']
educacion_porcentaje_choco = "{:,.2%}".format(educacion_choco['No. De personas/porcentaje/eventos'].sum())

# matriculados venezolanos
educacion_migrante_choco = choco[choco['Subtema'] == 'Número de migrantes venezolanos matriculados en el 2021']
educaion_migrante_numero_choco = "{:,.0f}".format(educacion_migrante_choco['No. De personas/porcentaje/eventos'].sum())

# porcentaje matriculados venezolanos
educacion_migrante_choco = choco[choco['Subtema'] == 'Porcentaje de migrante venezolanos matriculados en 2021 (comparado frente a los migrantes matriculados a nivel nacional)']
educacion_migrante_porcentaje_choco = "{:,.2%}".format(educacion_migrante_choco['No. De personas/porcentaje/eventos'].sum())

##########################
###### servicios publicos

# porcentaje internet
internet_choco = choco[choco['Subtema'] == 'Porcentaje de Hogares con conexión a internet en el departamento']
internet_porcentaje_choco = "{:,.2%}".format(internet_choco['No. De personas/porcentaje/eventos'].sum())

# porcentaje acueducto
acueducto_choco = choco[choco['Subtema'] == 'Porcentaje de Cobertura acueducto en el departamento']
acueducto_porcentaje_choco = "{:,.2%}".format(acueducto_choco['No. De personas/porcentaje/eventos'].sum())

# porcentaje acueducto
alcantarillado_choco = choco[choco['Subtema'] == 'Porcentaje de Cobertura alcantarillado en el departamento']
alcantarillado_porcentaje_choco = "{:,.2%}".format(alcantarillado_choco['No. De personas/porcentaje/eventos'].sum())

##########################
###### desastres naturales

# Numero de inundaciones
inundaciones_choco = choco[choco['Subtema'] == 'Número de Inundaciones en 2021']
inundaciones_choco_numero = "{:,.0f}".format(inundaciones_choco['No. De personas/porcentaje/eventos'].sum())

# Numero de vendavales
vendavales_choco = choco[choco['Subtema'] == 'Número de Vendavales en 2021']
vendavales_choco_numero = "{:,.0f}".format(vendavales_choco['No. De personas/porcentaje/eventos'].sum())

# Numero de afectadas
per_afectadas_choco = choco[choco['Subtema'] == 'Número de personas afectadas por desastres naturales en 2021']
per_afectadas_choco_numero = "{:,.0f}".format(per_afectadas_choco['No. De personas/porcentaje/eventos'].sum())

# porcentaje acueducto
per_afectadas_choco = choco[choco['Subtema'] == 'Porcentaje de personas afectadas por desastres naturales en 2021']
per_afectada_porcentaje_choco = "{:,.2%}".format(per_afectadas_choco['No. De personas/porcentaje/eventos'].sum())

##########################
###### salud

# mortalidad materna
mortalidad_choco = choco[choco['Subtema'] == 'Mortalidad materna por cada 100.000 nacidos']
mortalidad_choco_numero = "{:,.1f}".format(mortalidad_choco['No. De personas/porcentaje/eventos'].sum())

# mortalidad perinatal y neonatal
perinatal_choco = choco[choco['Subtema'] == 'Mortalidad perinatal y neonatal por cada 1000 nacidos vivos']
perinatal_choco_numero = "{:,.1f}".format(perinatal_choco['No. De personas/porcentaje/eventos'].sum())

##########################
###### VBG

# numero de casos
vbg_choco = choco[choco['Subtema'] == 'Número de casos VBG en 2020']
vbg_choco_numero = "{:,.0f}".format(vbg_choco['No. De personas/porcentaje/eventos'].sum())

# porcentaje nacional
vbg_choco = choco[choco['Subtema'] == 'Porcentajes de casos VBG en 2020 comparado a nivel nacional']
vbg_porcentaje_choco = "{:,.2%}".format(vbg_choco['No. De personas/porcentaje/eventos'].sum())

# porcentaje niños
vbg_choco = choco[choco['Subtema'] == 'Porcentaje de casos contra niños y niñas']
vbg_porcentaje_ninos_choco = "{:,.2%}".format(vbg_choco['No. De personas/porcentaje/eventos'].sum())

# porcentaje victimario
vbg_choco = choco[choco['Subtema'] == 'Porcentajes de casos donde el victimario es familiar']
vbg_porcentaje_victimario_choco = "{:,.2%}".format(vbg_choco['No. De personas/porcentaje/eventos'].sum())

# porcentaje mujer
vbg_choco = choco[choco['Subtema'] == 'Porcentaje de casos donde la Victima fue mujer']
vbg_porcentaje_mujer_choco = "{:,.2%}".format(vbg_choco['No. De personas/porcentaje/eventos'].sum())

# porcentaje rural
vbg_choco = choco[choco['Subtema'] == 'Porcentaje de casos ocurridos en zona rural']
vbg_porcentaje_rural_choco = "{:,.2%}".format(vbg_choco['No. De personas/porcentaje/eventos'].sum())


##########################
###### Conflicto armado

# numero de eventos
eventos_choco = choco[choco['Subtema'] == 'Número de Eventos de violecia']
eventos_choco_numero = "{:,.0f}".format(eventos_choco['No. De personas/porcentaje/eventos'].sum())

# numero de personas afectadas
per_afectadas_choco = choco[choco['Subtema'] == 'Personas afectadas por el conflicto armado']
per_afectada_choco_numero = "{:,.0f}".format(per_afectadas_choco['No. De personas/porcentaje/eventos'].sum())

# numero de personas confinamiento
per_confinamiento_choco = choco[choco['Subtema'] == 'Número de personas afectados por confinamiento y/o desplazamiento']
per_confinamiento_choco_numero = "{:,.0f}".format(per_confinamiento_choco['No. De personas/porcentaje/eventos'].sum())

# numero de niños reclutados
ninos_reclutados_choco = choco[choco['Subtema'] == 'Número de niños con Reclutamiento o desvinculación']
ninos_reclutados_choco_numero = "{:,.0f}".format(ninos_reclutados_choco['No. De personas/porcentaje/eventos'].sum())

# numero de MAP-MUSE
MAP_MUSE_choco = choco[choco['Subtema'] == 'Número de Eventos MAP-MUSE']
MAP_MUSE_choco_numero = "{:,.0f}".format(MAP_MUSE_choco['No. De personas/porcentaje/eventos'].sum())

# numero de MAP-MUSE
MAP_MUSE_menores_choco = choco[choco['Subtema'] == 'Número de Eventos MAP-MUSE que involucran menores de edad']
MAP_MUSE_menores_choco_numero = "{:,.0f}".format(MAP_MUSE_menores_choco['No. De personas/porcentaje/eventos'].sum())

# Grafica

grafica = pd.read_csv('https://raw.githubusercontent.com/andrestrianareina/datainfografias/master/Situaci_n_V_ctimas_Minas_Antipersonal_en_Colombia.csv')
choco_mins = grafica[grafica['departamento'] == 'CHOCO']
choco_mins['Cantidad'] = 1
Estado_años_choco = choco_mins.groupby(['ano','estado']).sum().reset_index()

choco_heridos = Estado_años_choco[Estado_años_choco['estado']=='Herido']
choco_heridos_final = pd.concat([choco_heridos['ano'], choco_heridos['Cantidad']], axis=1)
choco_heridos_final.columns = ['Año', 'Heridos']

choco_fallecidos = Estado_años_choco[Estado_años_choco['estado']=='Muerto']
choco_fallecidos_final = pd.concat([choco_fallecidos['ano'], choco_fallecidos['Cantidad']], axis=1)
choco_fallecidos_final.columns = ['Año', 'Fallecidos']

lista_años = list(range(1990,2022))
lista_años_df = pd.DataFrame(lista_años, columns=['Año'])

choco_datos_union1 = pd.merge(lista_años_df, choco_heridos_final,on='Año',how='outer')
choco_datos_final_grafica = pd.merge(choco_datos_union1, choco_fallecidos_final,on='Año',how='outer')
choco_datos_final_grafica = choco_datos_final_grafica.fillna(0)

años_choco = lista_años_df['Año'].tolist()
fallecidos_choco = choco_datos_final_grafica['Fallecidos'].tolist()
heridos_choco = choco_datos_final_grafica['Heridos'].tolist()





