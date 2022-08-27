l1 = [x for x in range(10000)]   # Lista comum
l2 = (x for x in range(10000))   # Ultilizando gerador

##########################

nome = "Jhonata"
iterador = iter(nome)
gerador = (letra for letra in iterador)

# print(next(gerador))    # Consome a primeira letra do nome

# for i in nome:
#    print(nome)

###################################
#   Atividade
carrinho = []
carrinho.append(("Camisa", 30))
carrinho.append(("Blusa", 30))
carrinho.append(("Short", 50))

preco = [produto[1] for produto in carrinho]
total = sum(preco)  # Soma todos os valores da lista

# Formato do professor

total = sum([float(y) for x,y in carrinho])
print(total)
