class LogMixin:
    @staticmethod
    def write(msg):
        with open(r'Relação de classes\heranca_multipla\logs.log', 'a+',
                  encoding='UTF-8') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')

    def log_warning(self, msg):
        self.write(f'WARNING: {msg}')
