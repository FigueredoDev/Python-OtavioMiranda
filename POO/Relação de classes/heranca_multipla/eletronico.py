class Eletronico:
    def __init__(self, nome) -> None:
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return 'Já esta ligado!'

        self._ligado = True
        return 'Ligando...'

    def desligar(self):
        if not self._ligado:
            return 'Está desligado!'

        self._ligado = False
        return 'Desligando...'
