import pandas as pd
import numpy as np
from datetime import date, timedelta

df = pd.read_csv('/Users/andresmauriciotrianareina/Documents/GitHub/datainfografias/Propuesta_levantamiento_información_V1.csv')

# Covid

covid = df[df['Tema'] == 'COVID 19']
covid.reset_index(drop=True, inplace=True)

covid_fecha_inicial = covid['Fecha inicial corte'].loc[0]
covid_fecha_final = covid['Fecha final corte'].loc[0]
fecha_covid = covid_fecha_inicial +" al " + covid_fecha_final

# migración

migracion1 = df[df['Subtema'] == 'Número de Migrantes venezolanos']
migracion1.reset_index(drop=True, inplace=True)

migracion1inicial = migracion1['Fecha inicial corte'][0]
migracion1final = migracion1['Fecha final corte'][0]

fecha_final_migración1 = migracion1inicial +" al " + migracion1final

migracion2 = df[df['Subtema'] == 'Número de niños con con registro de nacimiento bajo el programa - Primero la niñez']
migracion2.reset_index(drop=True, inplace=True)

migracion2inicial = migracion2['Fecha inicial corte'][0]
migracion2final = migracion2['Fecha final corte'][0]
fecha_final_migración2 = migracion2inicial +" al " + migracion2final

# Educacion
educacion = df[df['Tema'] == 'Educación']
educacion.reset_index(drop=True, inplace=True)

educacion2inicial = educacion['Fecha inicial corte'][0]
educacion2final = educacion['Fecha final corte'][0]
fecha_final_educacion = educacion2inicial +" al " + educacion2final

# Servicios

servicios = df[df['Tema'] == 'Servicios publicos']
servicios.reset_index(drop=True, inplace=True)

Servicios_inicial = servicios['Fecha inicial corte'][0]
Servicios_final = servicios['Fecha final corte'][0]
fecha_final_servicios = Servicios_inicial +" al " + Servicios_final

# desastres

desastres = df[df['Tema'] == 'Desastres naturales']
desastres.reset_index(drop=True, inplace=True)

desastres_inicial = desastres['Fecha inicial corte'][0]
desastres_final = desastres['Fecha final corte'][0]
fecha_final_desastres = desastres_inicial +" al " + desastres_final

# salud

salud = df[df['Tema'] == 'Salud']
salud.reset_index(drop=True, inplace=True)

salud_inicial = salud['Fecha inicial corte'][0]
salud_final = salud['Fecha final corte'][0]
fecha_final_salud = salud_inicial +" al " + salud_final

# VBG

VGB = df[df['Tema'] == 'Violencia basada en genero']
VGB.reset_index(drop=True, inplace=True)

VGB_inicial = VGB['Fecha inicial corte'][0]
VGB_final = VGB['Fecha final corte'][0]
fecha_final_VGB = VGB_inicial +" al " + VGB_final

# conflicto armado

eventos = df[df['Subtema'] == 'Número de Eventos de violecia']
eventos.reset_index(drop=True, inplace=True)

eventos_inicial = eventos['Fecha inicial corte'][0]
eventos_final = eventos['Fecha final corte'][0]
fecha_final_eventos = eventos_inicial +" al " + eventos_final

MAP = df[df['Subtema'] == 'Número de Eventos MAP-MUSE']
MAP.reset_index(drop=True, inplace=True)

MAP_inicial = MAP['Fecha inicial corte'][0]
MAP_final = MAP['Fecha final corte'][0]
fecha_final_MAP = MAP_inicial +" al " + MAP_final
 
# Nacional

Nacional = df[df['Departamento'] == 'NACIONAL']
Nacional.reset_index(drop=True, inplace=True)

#Migrantes

Nacional_migrantes = Nacional[Nacional['Subtema'] == 'Número de Migrantes venezolanos']
Nacional_migrantes_total = "{:,.0f}".format(Nacional_migrantes['No. De personas/porcentaje/eventos'].sum())

# Primero la ninez

Nacional_migrantes_PN = Nacional[Nacional['Subtema'] == 'Número de niños con con registro de nacimiento bajo el programa - Primero la niñez']
Nacional_migrantes_PN_total = "{:,.0f}".format(Nacional_migrantes_PN['No. De personas/porcentaje/eventos'].sum())

# matriculados

Nacional_matriculados = Nacional[Nacional['Subtema'] == 'Número de matriculas en el 2021']
Nacional_matriculados_total = "{:,.0f}".format(Nacional_matriculados['No. De personas/porcentaje/eventos'].sum())

# matriculados migrantes

Nacional_matriculados_migrantes = Nacional[Nacional['Subtema'] == 'Número de migrantes venezolanos matriculados en el 2021']
Nacional_matriculados_migrantes_total = "{:,.0f}".format(Nacional_matriculados_migrantes['No. De personas/porcentaje/eventos'].sum())