from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto("Camiseta", 50)
p2 = Produto("Caneca", 15)
p3 = Produto("Bolsa", 150)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)

carrinho.lista_produto()
print(carrinho.soma())
