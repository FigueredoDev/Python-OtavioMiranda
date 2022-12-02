class Electronic:
    def __init__(self, name) -> None:
        self._name = name
        self._switched_on = False

    def turn_on(self):
        if self._switched_on:
            return 'Já esta ligado!'

        self._switched_on = True
        return 'Ligando...'

    def turn_off(self):
        if not self._switched_on:
            return 'Está desligado!'

        self._switched_on = False
        return 'Desligando...'
