class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__

    def falar(self):
        print(f"{self.nome_classe} está falando!")


class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nome_classe} está comprando")


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_classe} está estudando!')
