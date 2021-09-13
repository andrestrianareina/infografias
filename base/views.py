from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View, DetailView
from .models import RedesSociales
from base.guajira import *
from base.choco import *
from base.datos_nacionales import *
import pandas as pd
import json

# Create your views here.

def obtenerRedes():
    return RedesSociales.objects.filter(
        estado = True,
    ).latest('fecha_creacion')


def Inicio (request):

    context = {

        ############### Datos nacionales

        'fecha_covid':fecha_covid,
        'fecha_final_migración1':fecha_final_migración1,
        'fecha_final_migración2':fecha_final_migración2,
        'fecha_final_educacion':fecha_final_educacion,
        'fecha_final_servicios':fecha_final_servicios,
        'fecha_final_desastres':fecha_final_desastres,
        'fecha_final_salud':fecha_final_salud,
        'fecha_final_VGB':fecha_final_VGB,
        'fecha_final_eventos':fecha_final_eventos,
        'fecha_final_MAP':fecha_final_MAP,
        'Nacional_migrantes_total':Nacional_migrantes_total,
        'Nacional_migrantes_PN_total':Nacional_migrantes_PN_total,
        'Nacional_matriculados_total':Nacional_matriculados_total,
        'Nacional_matriculados_migrantes_total':Nacional_matriculados_migrantes_total,


        ############### Datos la Guajira

        #### Covid
        'covid_contagios_total_guajira':covid_contagios_total_guajira,
        'covid_fallecidos_total_guajira':covid_fallecidos_total_guajira,
        'covid_recuperados_total_guajira':covid_recuperados_total_guajira,
        'covid_activos_total_guajira':covid_activos_total_guajira,
        'covid_sinclasificar_total_guajira':covid_sinclasificar_total_guajira,
        'covid_vacunados_total_guajira':covid_vacunados_total_guajira,
        'locs_guajira':locs_guajira,
        'z_guajira':z_guajira,

        #### migración
        'migracion_guajira_numero':migracion_guajira_numero,
        'migracion_porcentaje_guajira':migracion_porcentaje_guajira,
        'migracion_pn_numero_guajira':migracion_pn_numero_guajira,
        'migracion_pn_porcentaje_guajira':migracion_pn_porcentaje_guajira,

        ### educacion
        'educacion_guajira_numero':educacion_guajira_numero,
        'educacion_porcentaje_guajira':educacion_porcentaje_guajira,
        'educaion_migrante_numero_guajira':educaion_migrante_numero_guajira,
        'educacion_migrante_porcentaje_guajira':educacion_migrante_porcentaje_guajira,

        ### servicios publicos

        'internet_porcentaje_guajira':internet_porcentaje_guajira,
        'acueducto_porcentaje_guajira':acueducto_porcentaje_guajira,
        'alcantarillado_porcentaje_guajira':alcantarillado_porcentaje_guajira,

        ### desastres naturales
        'inundaciones_guajira_numero':inundaciones_guajira_numero,
        'vendavales_guajira_numero':vendavales_guajira_numero,
        'per_afectadas_guajira_numero':per_afectadas_guajira_numero,
        'per_afectada_porcentaje_guajira':per_afectada_porcentaje_guajira,

        ### salud
        'mortalidad_guajira_numero':mortalidad_guajira_numero,
        'perinatal_guajira_numero':perinatal_guajira_numero,

        ### vbg
        'vbg_guajira_numero':vbg_guajira_numero,
        'vbg_porcentaje_guajira':vbg_porcentaje_guajira,
        'vbg_porcentaje_ninos_guajira':vbg_porcentaje_ninos_guajira,
        'vbg_porcentaje_victimario_guajira':vbg_porcentaje_victimario_guajira,
        'vbg_porcentaje_mujer_guajira':vbg_porcentaje_mujer_guajira,
        'vbg_porcentaje_rural_guajira':vbg_porcentaje_rural_guajira,

        ### conflicto armado
        'eventos_guajira_numero':eventos_guajira_numero,
        'per_afectada_guajira_numero':per_afectada_guajira_numero,
        'per_confinamiento_guajira_numero':per_confinamiento_guajira_numero,
        'ninos_reclutados_guajira_numero':ninos_reclutados_guajira_numero,
        'MAP_MUSE_guajira_numero':MAP_MUSE_guajira_numero,
        'MAP_MUSE_menores_guajira_numero':MAP_MUSE_menores_guajira_numero,

        #grafica
        'años_guajira':años_guajira,
        'fallecidos_guajira':fallecidos_guajira,
        'heridos_guajira':heridos_guajira,

        ### Respuesta y acciones UNICEF

        'kits_necesidades_guajira_total':kits_necesidades_guajira_total,
        'Mensajes_guajira_total':Mensajes_guajira_total,
        'desnutricion1_guajira_total':desnutricion1_guajira_total,
        'higiene1_guajira_total':higiene1_guajira_total,
        'desnutricion2_guajira_total':desnutricion2_guajira_total,
        'salud_guajira_total':salud_guajira_total,
        'higiene2_guajira_total':higiene2_guajira_total,
        'hidratación_guajira_total':hidratación_guajira_total,
        'telefonico1_guajira_total':telefonico1_guajira_total,
        'VBG_proteccion_guajira_total':VBG_proteccion_guajira_total,
        'Jornadas_guajira_total':Jornadas_guajira_total,
        'Mensajes_comunicacion_guajira_total':Mensajes_comunicacion_guajira_total,
        'Reuniones_comunicacion_guajira_total':Reuniones_comunicacion_guajira_total,
        'apoyo_educacion_guajira_total':apoyo_educacion_guajira_total,
        'Historia_guajira_final':Historia_guajira_final,


        
        
        ############### Datos la Choco

        #### Covid
        'covid_contagios_total_choco':covid_contagios_total_choco,
        'covid_fallecidos_total_choco':covid_fallecidos_total_choco,
        'covid_recuperados_total_choco':covid_recuperados_total_choco,
        'covid_activos_total_choco':covid_activos_total_choco,
        'covid_sinclasificar_total_choco':covid_sinclasificar_total_choco,
        'covid_vacunados_total_choco':covid_vacunados_total_choco,
        'locs_choco':locs_choco,
        'z_choco':z_choco,

        #### migración
        'migracion_choco_numero':migracion_choco_numero,
        'migracion_porcentaje_choco':migracion_porcentaje_choco,
        'migracion_pn_numero_choco':migracion_pn_numero_choco,
        'migracion_pn_porcentaje_choco':migracion_pn_porcentaje_choco,

        ### educacion
        'educacion_choco_numero':educacion_choco_numero,
        'educacion_porcentaje_choco':educacion_porcentaje_choco,
        'educaion_migrante_numero_choco':educaion_migrante_numero_choco,
        'educacion_migrante_porcentaje_choco':educacion_migrante_porcentaje_choco,

        ### servicios publicos

        'internet_porcentaje_choco':internet_porcentaje_choco,
        'acueducto_porcentaje_choco':acueducto_porcentaje_choco,
        'alcantarillado_porcentaje_choco':alcantarillado_porcentaje_choco,

        ### desastres naturales
        'inundaciones_choco_numero':inundaciones_choco_numero,
        'vendavales_choco_numero':vendavales_choco_numero,
        'per_afectadas_choco_numero':per_afectadas_choco_numero,
        'per_afectada_porcentaje_choco':per_afectada_porcentaje_choco,

        ### salud
        'mortalidad_choco_numero':mortalidad_choco_numero,
        'perinatal_choco_numero':perinatal_choco_numero,

        ### vbg
        'vbg_choco_numero':vbg_choco_numero,
        'vbg_porcentaje_choco':vbg_porcentaje_choco,
        'vbg_porcentaje_ninos_choco':vbg_porcentaje_ninos_choco,
        'vbg_porcentaje_victimario_choco':vbg_porcentaje_victimario_choco,
        'vbg_porcentaje_mujer_choco':vbg_porcentaje_mujer_choco,
        'vbg_porcentaje_rural_choco':vbg_porcentaje_rural_choco,

        ### conflicto armado
        'eventos_choco_numero':eventos_choco_numero,
        'per_afectada_choco_numero':per_afectada_choco_numero,
        'per_confinamiento_choco_numero':per_confinamiento_choco_numero,
        'ninos_reclutados_choco_numero':ninos_reclutados_choco_numero,
        'MAP_MUSE_choco_numero':MAP_MUSE_choco_numero,
        'MAP_MUSE_menores_choco_numero':MAP_MUSE_menores_choco_numero,

        #grafica
        'años_choco':años_choco,
        'fallecidos_choco':fallecidos_choco,
        'heridos_choco':heridos_choco,


        ### Respuesta y acciones UNICEF

        'kits_necesidades_choco_total':kits_necesidades_choco_total,
        'Mensajes_choco_total':Mensajes_choco_total,
        'desnutricion1_choco_total':desnutricion1_choco_total,
        'higiene1_choco_total':higiene1_choco_total,
        'desnutricion2_choco_total':desnutricion2_choco_total,
        'salud_choco_total':salud_choco_total,
        'higiene2_choco_total':higiene2_choco_total,
        'hidratación_choco_total':hidratación_choco_total,
        'telefonico1_choco_total':telefonico1_choco_total,
        'VBG_proteccion_choco_total':VBG_proteccion_choco_total,
        'Jornadas_choco_total':Jornadas_choco_total,
        'Mensajes_comunicacion_choco_total':Mensajes_comunicacion_choco_total,
        'Reuniones_comunicacion_choco_total':Reuniones_comunicacion_choco_total,
        'apoyo_educacion_choco_total':apoyo_educacion_choco_total,
        'Historia_choco_final':Historia_choco_final,
    }
    return render(request,'index.html',context)
