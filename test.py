import unittest
from romanos2 import romano_a_entero


class romanpstest(unittest.TestCase):

    def test_unidades(self):
        self.assertEqual(romano_a_entero('I'), 1)
        self.assertEqual(romano_a_entero('V'), 5)
        self.assertEqual(romano_a_entero('X'), 10)
        self.assertEqual(romano_a_entero('L'), 50)
        self.assertEqual(romano_a_entero('C'), 100)
        self.assertEqual(romano_a_entero('D'), 500)
        self.assertEqual(romano_a_entero('M'), 1000)

    def test_numeros_basicos(self):
        self.assertEqual(romano_a_entero('II'), 2)
        self.assertEqual(romano_a_entero('IV'), 4)
        self.assertEqual(romano_a_entero('IX'), 9)
        self.assertEqual(romano_a_entero('CCV'), 205)
        self.assertEqual(romano_a_entero('MCXXIII'), 1123)

    def test_no_resta_mas_un_orden_magnitud(self):
        self.assertRaises(ValueError, romano_a_entero, 'IC')

    def test_no_restas_consecutivas(self):
        self.assertRaises(ValueError, romano_a_entero, ('IIV'))
        self.assertRaises(ValueError, romano_a_entero, ('IVX'))


unittest.main()
