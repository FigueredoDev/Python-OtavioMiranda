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

from person import Person


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Person("Jhonata", "Figueredo")

    def test_person_attr_name_has_correct_value(self):
        self.assertEqual(self.p1.name, "Jhonata")

    def test_person_attr_name_is_string(self):
        self.assertIsInstance(self.p1.name, str)

    def test_person_attr_lastname_has_correct_value(self):
        self.assertEqual(self.p1.last_name, "Figueredo")

    def test_person_attr_lastname_is_string(self):
        self.assertIsInstance(self.p1.last_name, str)

    def test_person_attr_data_obtained_start_false(self):
        self.assertFalse(self.p1.data_obtained)

    def test_get_all_data_success_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), "Conectado")
            self.assertTrue(self.p1.data_obtained)

    def test_get_all_data_fail_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), "Erro 404")
            self.assertFalse(self.p1.data_obtained)

    def test_get_all_data_success_fail_sequential(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), "Conectado")
            self.assertTrue(self.p1.data_obtained)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), "Erro 404")
            self.assertFalse(self.p1.data_obtained)


if __name__ == "__main__":
    unittest.main(verbosity=2)
