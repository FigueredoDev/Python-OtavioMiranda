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

from bacon_with_eggs import bacon_with_eggs


class TestBaconComOvos(unittest.TestCase):
    def test_deve_retornar_assertion_caso_numero_nao_seja_inteiro(self):
        with self.assertRaises(AssertionError):
            bacon_with_eggs(1.2)

    def test_deve_retornar_bacon_com_ovos_caso_seja_multiplo_de_3_e_5(self):
        entries = (15, 30, 45, 60)
        exit = "Bacon com ovos"

        for entry in entries:
            with self.subTest(entry=entry, exit=exit):
                self.assertEqual(bacon_with_eggs(entry),
                                 exit,
                                 msg=f'{entry} não retornou "{exit}"'
                                 )

    def test_deve_retornar_passar_fome_caso_nao_seja_multiplo_de_3_e_5(self):
        entries = (13, 32, 41, 17)
        exit = "Passar Fome"

        for entry in entries:
            with self.subTest(entry=entry, exit=exit):
                self.assertEqual(bacon_with_eggs(entry),
                                 exit,
                                 msg=f'{entry} não retornou "{exit}"'
                                 )

    def test_deve_retornar_bacon_caso_seja_multiplo_de_3(self):
        entries = (3, 6, 9, 12)
        exit = "Bacon"

        for entry in entries:
            with self.subTest(entries=entry, exit=exit):
                self.assertEqual(bacon_with_eggs(entry),
                                 exit,
                                 msg=f'{entry} não retornou "{exit}"'
                                 )

    def test_deve_retornar_ovos_caso_seja_multiplo_de_5(self):
        entries = (5, 10, 20)
        exit = "Ovos"

        for entry in entries:
            with self.subTest(entry=entry, exit=exit):
                self.assertEqual(bacon_with_eggs(entry),
                                 exit,
                                 msg=f'{entry} não retornou "{exit}"'
                                 )


if __name__ == '__main__':
    unittest.main(verbosity=2)
