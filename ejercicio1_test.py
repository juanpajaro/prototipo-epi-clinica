#!/usr/bin/env python3

from ejercicio1 import load_data, calcular_imc
import unittest
import pandas as pd

datos = pd.read_csv('./data/diabetes.txt', sep = '\t')

class TestRearrange(unittest.TestCase):
    
    def test_calculo_media_imc(self):
        media_imc = datos["BMI"].mean()
        print("valor_medica: {}".format(media_imc))
        testcase = media_imc
        expected = 26.375792
        self.assertAlmostEqual(calcular_imc(testcase), expected, places=4)

unittest.main()