#!/usr/bin/env python3

from ejercicio1 import load_data, calcular_imc
import unittest
import pandas as pd

#datos = pd.read_csv('./data/diabetes.txt', sep = '\t')

class TestRearrange(unittest.TestCase):
    
    """
    def test_calculo_media_imc(self):
        media_imc = datos["BMI"].mean()
        print("valor_medica: {}".format(media_imc))
        testcase = media_imc
        expected = 26.375792
        self.assertAlmostEqual(calcular_imc(testcase), expected, places=4)

        """
    
    def test_calculo_media_imc(self):
        data_prueba = [30, 20, 10, 40, 50]
        serie_prueba = pd.Series(data=data_prueba)
        #media_imc = serie_prueba.mean()
        #print("valor_medica: {}".format(media_imc))
        testcase = serie_prueba
        expected = 30
        self.assertAlmostEqual(calcular_imc(testcase), expected, places=4)
    
unittest.main()