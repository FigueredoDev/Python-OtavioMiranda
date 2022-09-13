'''
TDD Test driven development ( Desenvolvimento dirigido a testes )

Red
Parte 1 - > Criar o teste e ver falhar

Green
Parte 2 - > Criar o código e ver o teste passar

Refactor
Parte 3 - > Melhorar meu código
'''
try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:     # noqa: E722
    raise

import unittest

from baconcomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_deve_retornar_assertion_caso_numero_nao_seja_inteiro(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos(1.2)

    def test_deve_retornar_bacon_com_ovos_caso_seja_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = "Bacon com ovos"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'{entrada} não retornou "{saida}"'
                                 )

    def test_deve_retornar_passar_fome_caso_nao_seja_multiplo_de_3_e_5(self):
        entradas = (13, 32, 41, 17)
        saida = "Passar Fome"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'{entrada} não retornou "{saida}"'
                                 )

    def test_deve_retornar_bacon_caso_seja_multiplo_de_3(self):
        entradas = (3, 6, 9, 12)
        saida = "Bacon"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'{entrada} não retornou "{saida}"'
                                 )

    def test_deve_retornar_ovos_caso_seja_multiplo_de_5(self):
        entradas = (5, 10, 20)
        saida = "Ovos"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'{entrada} não retornou "{saida}"'
                                 )


if __name__ == '__main__':
    unittest.main(verbosity=2)
