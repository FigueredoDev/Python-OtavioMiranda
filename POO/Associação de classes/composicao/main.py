from classes import Cliente, Endereco  # noqa F401


cliente1 = Cliente("Jhonata", 21)
cliente1.insere_endereco("Imperatriz", "MA")

cliente2 = Cliente("Maria", 55)
cliente2.insere_endereco("Rio de Janeiro", "RJ")

cliente1.lista_enderecos()
