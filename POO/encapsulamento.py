"""
public, protect, private
_ protect
__ private
"""


class DataBase:
    def __init__(self):
        self.__data: dict = {}

    @property
    def data(self) -> dict:
        return self.__data

    def insert_clients(self, id: int, name: str) -> None:
        if 'clients' not in self.__data:
            self.__data['clients'] = {id: name}
        else:
            self.__data['clients'].update({id: name})

    def list_clients(self) -> None:
        for id, nome in self.__data['clients'].items():
            print(id, nome)

    def delete_client(self, id: int) -> None:
        del self.__data['clients'][id]


bd = DataBase()
bd.insert_clients(1, "Jhonata")
bd.insert_clients(2, "Otávio")

bd.delete_client(2)
bd.list_clients()
print(bd.data)
