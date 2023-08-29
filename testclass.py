import unittest
from romanospro import RomanNumber


class RomanosTest(unittest.TestCase):
    def test_crear_numero_romano_desde_entero(self):
        numero = RomanNumber(1745)
        self.assertEqual(numero.valor, 1745)
        self.assertEqual(numero.cadena, 'MDCCXLV')
        numero = RomanNumber(1)
        self.assertEqual(numero.valor, 1)
        self.assertEqual(numero.cadena, 'I')

    def test_crear_numero_romano_desde_cadena(self):
        numero = RomanNumber('I')
        self.assertEqual(numero.cadena, 'I')
        self.assertEqual(numero.valor, 1)
        numero = RomanNumber(1745)
        self.assertEqual(numero.valor, 1745)
        self.assertEqual(numero.cadena, 'MDCCXLV')

    def test_numero_romano_tiene_representacion_en_cadena(self):
        numero = RomanNumber(1745)
        self.assertEqual(str(numero), 'MDCCXLV')

    def test_comprobar_igualdad(self):
        numerouno = RomanNumber(1)
        otronumerouno = RomanNumber(1)
        numerodos = RomanNumber(2)
        self.assertEqual(numerouno, otronumerouno)
        self.assertNotEqual(numerouno, numerodos)
        self.assertNotEqual(otronumerouno, numerodos)

    def test_comprobar_suma(self):
        numerouno = RomanNumber(1)
        numerodos = RomanNumber(2)
        self.assertEqual(numerouno + numerodos, 3)
        self.assertEqual(numerodos + 7, 9)
        self.assertEqual(numerodos + 'XII', 14)


unittest.main()
