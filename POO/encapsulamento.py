"""
public, protect, private
_ protect
__ private
"""


class BaseDeDados:
    def __init__(self):
        self.__dados: dict = {}

    @property
    def dados(self) -> dict:
        return self.__dados

    def inserir_clientes(self, id: int, nome: str) -> None:
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self) -> None:
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id: int) -> None:
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_clientes(1, "Jhonata")
bd.inserir_clientes(2, "Otavio")

bd.apaga_cliente(2)
bd.lista_clientes()
print(bd.dados)
