from electronic import Electronic
from log import LogMixin


class Smartphone(Electronic, LogMixin):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.connected = False

    def connect(self):
        if not self._switched_on:
            msg = '{} não está ligado'.format(self._name)
            self.log_error(msg)
            return msg

        if self.connected:
            msg = '{} já esta conectado!'.format(self._name)
            self.log_error(msg)
            return msg

        info = 'Conectando...'
        self.connected = True
        self.log_info(info)
        return info

    def disconnect(self):
        if not self._switched_on:
            msg = 'Não está conectado!'
            self.log_error(msg)
            return msg

        self.connected = False
        info = 'Desconectando...'
        self.log_info(info)
        return info
