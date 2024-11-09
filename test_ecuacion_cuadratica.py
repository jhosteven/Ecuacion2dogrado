import unittest
from resolver_ecuacion_cuadratica import resolver_ecuacion_cuadratica

class TestEcuacionCuadratica(unittest.TestCase):
    def test_dos_soluciones(self):

        self.assertEqual(resolver_ecuacion_cuadratica(1, -3, 2), (2.0, 1.0))

    def test_una_solucion(self):

        self.assertEqual(resolver_ecuacion_cuadratica(1, -2, 1), (1.0,))

    def test_sin_soluciones_reales(self):

        self.assertEqual(resolver_ecuacion_cuadratica(1, 0, 1), "No tiene soluciones reales")

if __name__ == '__main__':
    unittest.main()
