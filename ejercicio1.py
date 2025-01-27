#!/usr/bin/env python3

import pandas as pd

def load_data(diccionario):
    datos = pd.read_csv(diccionario)
    return datos

datos = load_data('./data/diabetes.txt', sep = '\t')
datos.head()