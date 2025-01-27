#!/usr/bin/env python3

import pandas as pd

def load_data(ubicacion_datos):
    datos = pd.read_csv(ubicacion_datos, sep = '\t')
    return datos

#retornar la media del indice de masa corporal
def calcular_imc(serie):
    return serie.mean()

"""
datos = load_data('./data/diabetes.txt')
datos.columns
#datos.head()
calcular_imc(datos["BMI"])
datos_prueba = [1, 2, 3, 4, 5]
calcular_imc(datos_prueba)
print(sum(datos_prueba))
"""