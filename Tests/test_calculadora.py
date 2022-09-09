import unittest

from calculadora import soma


class TestCalculadora(unittest.TestCase):
    def test_soma_10_10_saida_20(self):
        self.assertEqual(soma(10, 10), 20)

    def test_soma_varias_saidas(self):
        x_y_saidas = (
            (10, 10, 10),
            (5, 5, 10),
            (50, 1, 51),
            (-20, 30, 10),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)


unittest.main(verbosity=2)
