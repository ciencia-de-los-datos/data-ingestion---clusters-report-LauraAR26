"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():

    #Lectura Archivo
    filejob = "clusters_report.txt"
    cr1 = []
    txt = []

    #Adición primeras 2 lineas para encabezado
    clusterstxt = open(filejob, mode='r')
    cr1.append(clusterstxt.readline())
    cr1.append(clusterstxt.readline())

    #Separación de listas y reemplazo por cr1
    for id, i in enumerate(cr1):
        cr1[id] = ([i[:9], i[9:25].replace("\n",''), i[25:41].replace("\n",''), i[41:].replace("\n",'')])

    #Unión de las listas para encabezado compuesto
    cr1[0] = list(zip(cr1[0], cr1[1]))

    #Eliminación de una de las filas previamente unidas
    cr1.pop(1)

    #Unión de tuplas y limpieza de espacios en blanco
    for idx, x in enumerate(cr1[0]):
        cr1[0][idx] = '_'.join(''.join(x).split()).lower()

    #Lectura 2 líneas 'sobrantes'
    clusterstxt.readline()
    clusterstxt.readline()

    #Lectura y cierre archivo 
    cra = clusterstxt.read()
    clusterstxt.close()

    # Reemplazo espacios en blanco
    cra = ' '.join(''.join(cra).split())

    #Sepatación de  elementos de lista, partiendo por el caracter '.'
    cra = cra.split('.')

    #Eliminación fila sobrante 
    cra.pop()

    #Creación de variables para la solución fila 6 y 7 
    aux1 = []
    aux2 = []

    aux1 = re.split('([o][l][ ])+',cra[5])[0] + re.split('([o][l][ ])+',cra[5])[1]
    aux2 = re.split('([o][l][ ])+',cra[5])[2]

    cra[5] = aux1
    cra.insert(6, aux2)

    #Creación de la lista a partir de las otras y  partidas por el caracter '%'
    for i in cra:
        txt.append(i.split('%')[0].replace(',','.').split()+[i.split('%')[1].strip()])

    # Creación de dataframe con sus respectivos nombres 
    df = pd.DataFrame(txt)
    df.columns = cr1[0]
    df['cluster'] = pd.to_numeric(df['cluster'])
    df['cantidad_de_palabras_clave'] = pd.to_numeric(df['cantidad_de_palabras_clave'])
    df['porcentaje_de_palabras_clave'] = pd.to_numeric(df['porcentaje_de_palabras_clave'])

    return df
