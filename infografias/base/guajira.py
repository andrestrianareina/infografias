import pandas as pd
import numpy as np
from datetime import date, timedelta
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go


df = pd.read_csv('/Users/andresmauriciotrianareina/Documents/GitHub/datainfografias/Propuesta_levantamiento_información_V1.csv')
#df = pd.read_csv('https://raw.githubusercontent.com/andrestrianareina/datainfografias/master/Propuesta_levantamiento_información_V1.csv')



# Se extrae los datos de la guajira

guajira = df[df['Departamento'] == 'LA GUAJIRA']


# Se cambian algunos nombres de de municipios para usar en el mapa

guajira['Municipio'].replace(
    to_replace=['ALBANIA'],
    value='ALBANIA_g',
    inplace=True
)


guajira['Municipio'].replace(
    to_replace=['VILLANUEVA'],
    value='VILLA_NUEVA',
    inplace=True
)

guajira['Municipio'].replace(
    to_replace=['DISTRACCION'],
    value='DISTRACCIÓN',
    inplace=True
)


##########################
###### covid
 
#Contagios

covid_contagios_guajira = guajira[guajira['Subtema'] == 'Contagio']
covid_contagios_total_guajira = "{:,.0f}".format(covid_contagios_guajira['No. De personas/porcentaje/eventos'].sum())


# Fallecidos

covid_fallecidos_guajira = guajira[guajira['Subtema'] == 'Fallecido']
covid_fallecidos_total_guajira = "{:,.0f}".format(covid_fallecidos_guajira['No. De personas/porcentaje/eventos'].sum())


# Recuperados

covid_recuperados_guajira = guajira[guajira['Subtema'] == 'Recuperado']
covid_recuperados_total_guajira = "{:,.0f}".format(covid_recuperados_guajira['No. De personas/porcentaje/eventos'].sum())


# activos

covid_activos_guajira = guajira[guajira['Subtema'] == 'Activo']
covid_activos_total_guajira = "{:,.0f}".format(covid_activos_guajira['No. De personas/porcentaje/eventos'].sum())


# Sin clasificar

covid_sinclasificar_guajira = guajira[guajira['Subtema'] == 'Sin clasificar']
covid_sinclasificar_total_guajira = "{:,.0f}".format(covid_sinclasificar_guajira['No. De personas/porcentaje/eventos'].sum())


# conexión json para el mapa

import json
from urllib.request import urlopen
#with urlopen('https://raw.githubusercontent.com/caticoa3/colombia_mapa/master/co_2018_MGN_MPIO_POLITICO.geojson') as response:
with urlopen('https://raw.githubusercontent.com/andresmtr/mapa_municipios_colombia_geojonson/master/co_2018_MGN_MPIO_POLITICO_AT.geojson') as response:
    counties = json.load(response)

# Mapa covid contagios

locs = covid_contagios_guajira['Municipio']


for loc in counties['features']:
    loc['id'] = loc['properties']['MPIO_CNMBR']
map_guajira = go.Figure(go.Choroplethmapbox(
                    geojson=counties,
                    locations=locs,
                    z=covid_contagios_guajira['No. De personas/porcentaje/eventos'],
                    colorscale='plotly3',
                    colorbar_title="Total contagios"))
map_guajira.update_layout(mapbox_style="carto-positron",
                        mapbox_zoom=6.7,
                        mapbox_center = {"lat": 11.5, "lon": -73})

locs_guajira = covid_contagios_guajira['Municipio'].tolist()
z_guajira=covid_contagios_guajira['No. De personas/porcentaje/eventos'].tolist()


##########################
###### migración

# migrantes venezolanos

migracion_guajira = guajira[guajira['Subtema'] == 'Número de Migrantes venezolanos']
migracion_guajira_numero = "{:,.0f}".format(migracion_guajira['No. De personas/porcentaje/eventos'].sum())

# porcentaje a nivel nacional
migracion_guajira = guajira[guajira['Subtema'] == 'Porcentaje de Migrantes venezolanos ( comparado contra el nivel nacional)']
migracion_porcentaje_guajira = "{:,.2%}".format(migracion_guajira['No. De personas/porcentaje/eventos'].sum())

# primero la niñez

migracion_pn_guajira = guajira[guajira['Subtema'] == 'Número de niños con con registro de nacimiento bajo el programa - Primero la niñez']
migracion_pn_numero_guajira = "{:,.0f}".format(migracion_pn_guajira['No. De personas/porcentaje/eventos'].sum())

# porcentaje primero la niñez

migracion_pn_porcentaje_guajira = guajira[guajira['Subtema'] == 'Porcentaje de niños con con registro de nacimiento bajo el programa - Primero la niñez comparado a nivel nacional']
migracion_pn_porcentaje_guajira = "{:,.2%}".format(migracion_pn_porcentaje_guajira['No. De personas/porcentaje/eventos'].sum())

##########################
###### educación

# Numero de matriculados
educacion_guajira = guajira[guajira['Subtema'] == 'Número de matriculas en el 2021']
educacion_guajira_numero = "{:,.0f}".format(educacion_guajira['No. De personas/porcentaje/eventos'].sum())

# porcentaje a nivel nacional
educacion_guajira = guajira[guajira['Subtema'] == 'Porcenaje de matriculas en el 2021 ( comparado frente al nivel nacional)']
educacion_porcentaje_guajira = "{:,.2%}".format(educacion_guajira['No. De personas/porcentaje/eventos'].sum())

# matriculados venezolanos
educacion_migrante_guajira = guajira[guajira['Subtema'] == 'Número de migrantes venezolanos matriculados en el 2021']
educaion_migrante_numero_guajira = "{:,.0f}".format(educacion_migrante_guajira['No. De personas/porcentaje/eventos'].sum())

# porcentaje matriculados venezolanos
educacion_migrante_guajira = guajira[guajira['Subtema'] == 'Porcentaje de migrante venezolanos matriculados en 2021 (comparado frente a los migrantes matriculados a nivel nacional)']
educacion_migrante_porcentaje_guajira = "{:,.2%}".format(educacion_migrante_guajira['No. De personas/porcentaje/eventos'].sum())

##########################
###### servicios publicos

# porcentaje internet
internet_guajira = guajira[guajira['Subtema'] == 'Porcentaje de Hogares con conexión a internet en el departamento']
internet_porcentaje_guajira = "{:,.2%}".format(internet_guajira['No. De personas/porcentaje/eventos'].sum())

# porcentaje acueducto
acueducto_guajira = guajira[guajira['Subtema'] == 'Porcentaje de Cobertura acueducto en el departamento']
acueducto_porcentaje_guajira = "{:,.2%}".format(acueducto_guajira['No. De personas/porcentaje/eventos'].sum())

# porcentaje acueducto
alcantarillado_guajira = guajira[guajira['Subtema'] == 'Porcentaje de Cobertura alcantarillado en el departamento']
alcantarillado_porcentaje_guajira = "{:,.2%}".format(alcantarillado_guajira['No. De personas/porcentaje/eventos'].sum())

##########################
###### desastres naturales

# Numero de inundaciones
inundaciones_guajira = guajira[guajira['Subtema'] == 'Número de Inundaciones en 2021']
inundaciones_guajira_numero = "{:,.0f}".format(inundaciones_guajira['No. De personas/porcentaje/eventos'].sum())

# Numero de vendavales
vendavales_guajira = guajira[guajira['Subtema'] == 'Número de Vendavales en 2021']
vendavales_guajira_numero = "{:,.0f}".format(vendavales_guajira['No. De personas/porcentaje/eventos'].sum())

# Numero de afectadas
per_afectadas_guajira = guajira[guajira['Subtema'] == 'Número de personas afectadas por desastres naturales en 2021']
per_afectadas_guajira_numero = "{:,.0f}".format(per_afectadas_guajira['No. De personas/porcentaje/eventos'].sum())

# porcentaje acueducto
per_afectadas_guajira = guajira[guajira['Subtema'] == 'Porcentaje de personas afectadas por desastres naturales en 2021']
per_afectada_porcentaje_guajira = "{:,.2%}".format(per_afectadas_guajira['No. De personas/porcentaje/eventos'].sum())

##########################
###### salud

# mortalidad materna
mortalidad_guajira = guajira[guajira['Subtema'] == 'Mortalidad materna por cada 100.000 nacidos']
mortalidad_guajira_numero = "{:,.1f}".format(mortalidad_guajira['No. De personas/porcentaje/eventos'].sum())

# mortalidad perinatal y neonatal
perinatal_guajira = guajira[guajira['Subtema'] == 'Mortalidad perinatal y neonatal por cada 1000 nacidos vivos']
perinatal_guajira_numero = "{:,.1f}".format(perinatal_guajira['No. De personas/porcentaje/eventos'].sum())

##########################
###### VBG

# numero de casos
vbg_guajira = guajira[guajira['Subtema'] == 'Número de casos VBG en 2020']
vbg_guajira_numero = "{:,.0f}".format(vbg_guajira['No. De personas/porcentaje/eventos'].sum())

# porcentaje nacional
vbg_guajira = guajira[guajira['Subtema'] == 'Porcentajes de casos VBG en 2020 comparado a nivel nacional']
vbg_porcentaje_guajira = "{:,.2%}".format(vbg_guajira['No. De personas/porcentaje/eventos'].sum())

# porcentaje niños
vbg_guajira = guajira[guajira['Subtema'] == 'Porcentaje de casos contra niños y niñas']
vbg_porcentaje_ninos_guajira = "{:,.2%}".format(vbg_guajira['No. De personas/porcentaje/eventos'].sum())

# porcentaje victimario
vbg_guajira = guajira[guajira['Subtema'] == 'Porcentajes de casos donde el victimario es familiar']
vbg_porcentaje_victimario_guajira = "{:,.2%}".format(vbg_guajira['No. De personas/porcentaje/eventos'].sum())

# porcentaje mujer
vbg_guajira = guajira[guajira['Subtema'] == 'Porcentaje de casos donde la Victima fue mujer']
vbg_porcentaje_mujer_guajira = "{:,.2%}".format(vbg_guajira['No. De personas/porcentaje/eventos'].sum())

# porcentaje rural
vbg_guajira = guajira[guajira['Subtema'] == 'Porcentaje de casos ocurridos en zona rural']
vbg_porcentaje_rural_guajira = "{:,.2%}".format(vbg_guajira['No. De personas/porcentaje/eventos'].sum())


##########################
###### Conflicto armado

# numero de eventos
eventos_guajira = guajira[guajira['Subtema'] == 'Número de Eventos de violecia']
eventos_guajira_numero = "{:,.0f}".format(eventos_guajira['No. De personas/porcentaje/eventos'].sum())

# numero de personas afectadas
per_afectadas_guajira = guajira[guajira['Subtema'] == 'Personas afectadas por el conflicto armado']
per_afectada_guajira_numero = "{:,.0f}".format(per_afectadas_guajira['No. De personas/porcentaje/eventos'].sum())

# numero de personas confinamiento
per_confinamiento_guajira = guajira[guajira['Subtema'] == 'Número de personas afectados por confinamiento y/o desplazamiento']
per_confinamiento_guajira_numero = "{:,.0f}".format(per_confinamiento_guajira['No. De personas/porcentaje/eventos'].sum())

# numero de niños reclutados
ninos_reclutados_guajira = guajira[guajira['Subtema'] == 'Número de niños con Reclutamiento o desvinculación']
ninos_reclutados_guajira_numero = "{:,.0f}".format(ninos_reclutados_guajira['No. De personas/porcentaje/eventos'].sum())

# numero de MAP-MUSE
MAP_MUSE_guajira = guajira[guajira['Subtema'] == 'Número de Eventos MAP-MUSE']
MAP_MUSE_guajira_numero = "{:,.0f}".format(MAP_MUSE_guajira['No. De personas/porcentaje/eventos'].sum())

# numero de MAP-MUSE
MAP_MUSE_menores_guajira = guajira[guajira['Subtema'] == 'Número de Eventos MAP-MUSE que involucran menores de edad']
MAP_MUSE_menores_guajira_numero = "{:,.0f}".format(MAP_MUSE_menores_guajira['No. De personas/porcentaje/eventos'].sum())

# Grafica

grafica = pd.read_csv('https://raw.githubusercontent.com/andrestrianareina/datainfografias/master/Situaci_n_V_ctimas_Minas_Antipersonal_en_Colombia.csv')
guaira_mins = grafica[grafica['departamento'] == 'LA GUAJIRA']
guaira_mins['Cantidad'] = 1
Estado_años = guaira_mins.groupby(['ano','estado']).sum().reset_index()

Guajira_heridos = Estado_años[Estado_años['estado']=='Herido']
Guajira_heridos_final = pd.concat([Guajira_heridos['ano'], Guajira_heridos['Cantidad']], axis=1)
Guajira_heridos_final.columns = ['Año', 'Heridos']

Guajira_fallecidos = Estado_años[Estado_años['estado']=='Muerto']
Guajira_fallecidos_final = pd.concat([Guajira_fallecidos['ano'], Guajira_fallecidos['Cantidad']], axis=1)
Guajira_fallecidos_final.columns = ['Año', 'Fallecidos']

lista_años = list(range(1990,2022))
lista_años_df = pd.DataFrame(lista_años, columns=['Año'])

datos_union1 = pd.merge(lista_años_df, Guajira_heridos_final,on='Año',how='outer')
datos_final_grafica = pd.merge(datos_union1, Guajira_fallecidos_final,on='Año',how='outer')
datos_final_grafica = datos_final_grafica.fillna(0)

años_guajira = lista_años_df['Año'].tolist()
fallecidos_guajira = datos_final_grafica['Fallecidos'].tolist()
heridos_guajira = datos_final_grafica['Heridos'].tolist()



