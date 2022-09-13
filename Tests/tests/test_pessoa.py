'''
class Pessoa
    _init_
        nome str
        sobrenome str
        dados obtidos bool
API :
    obter_todos_os_dados - > method
            OK
            404
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
from unittest.mock import patch

from pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Pessoa("Jhonata", "Figueredo")

    def test_pessoa_attr_nome_tem_valor_correto(self):
        self.assertEqual(self.p1.nome, "Jhonata")

    def test_pessoa_attr_nome_e_string(self):
        self.assertIsInstance(self.p1.nome, str)

    def test_pessoa_attr_sobrenome_tem_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, "Figueredo")

    def test_pessoa_attr_sobrenome_e_string(self):
        self.assertIsInstance(self.p1.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), "Conectado")
            self.assertTrue(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), "Erro 404")
            self.assertFalse(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), "Conectado")
            self.assertTrue(self.p1.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), "Erro 404")
            self.assertFalse(self.p1.dados_obtidos)


if __name__ == "__main__":
    unittest.main(verbosity=2)
