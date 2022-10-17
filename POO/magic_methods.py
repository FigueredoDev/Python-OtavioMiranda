# https://rszalski.github.io/magicmethods/

class A:
    def __new__(cls, *args, **kwargs):
        print('Method new was called')

        # SINGLETON
        if not hasattr(cls, '_exists'):
            cls._exists = super().__new__(cls)

        return cls._exists

    def __call__(self, *args, **kwargs):
        return f'Arguments send: {args} {kwargs}'

    def __len__(self):
        return 55

    def __init__(self, nome=None):
        print('INIT')

    def __str__(self):
        return 'Class name returned in print'

    def __del__(self):
        print('Collected object')

    def __setattr__(self, key, value):
        self.__dict__[key] = f'{value} I added this to your value'


a = A('luiz otávio')
