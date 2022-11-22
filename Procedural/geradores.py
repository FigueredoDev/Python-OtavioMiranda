l1 = [x for x in range(10000)]   # Lista comum
l2 = (x for x in range(10000))   # Utilizando gerador

##########################

name = "Jhonata"
iterator = iter(name)
generator = (letra for letra in iterator)

# print(next(gerador))    # Consome a primeira letra do nome

# for i in nome:
#    print(nome)

###################################
#   Atividade
cart = []
cart.append(("Camisa", 30))
cart.append(("Blusa", 30))
cart.append(("Short", 50))

price = [product[1] for product in cart]
total = sum(price)  # Soma todos os valores da lista

# Formato do professor

total = sum([float(y) for x, y in cart])  # type: ignore
print(total)
