from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.conectado = False

    def conectar(self):
        if not self._ligado:
            msg = '{} não está ligado'.format(self._nome)
            self.log_error(msg)
            return msg

        if self.conectado:
            msg = '{} já esta conectado!'.format(self._nome)
            self.log_error(msg)
            return msg

        info = 'Conectando...'
        self.conectado = True
        self.log_info(info)
        return info

    def desconectar(self):
        if not self._ligado:
            msg = 'Não está conectado!'
            self.log_error(msg)
            return msg

        self.conectado = False
        info = 'Desconectando...'
        self.log_info(info)
        return info
