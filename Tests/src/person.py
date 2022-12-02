import requests


class Person:
    def __init__(self, nome, last_name):
        self.name = nome
        self.last_name = last_name
        self.data_obtained = False

    def get_all_data(self):
        response = requests.get('')

        if response.ok:
            self.data_obtained = True
            return 'Conectado'
        else:
            self.data_obtained = False
            return 'Erro 404'
