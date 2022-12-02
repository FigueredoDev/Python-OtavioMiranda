# For em uma linha

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Joga cada elemento da lista para a variável 'i' e cria uma nova lista
ex1 = [i * 2 for i in l1]

l2 = ['Jhonata', 'Pedro', 'Adriana']
ex2 = [n.replace('a', '@').capitalize() for n in l2]

# Somente números pares
l3 = list(range(100))
ex3 = [v for v in l3 if v % 2 == 0]

# Usando else
ex4 = [v if v % 2 == 0 else 'Nao' for v in l3]

# Exercício
# Separar em lista de zero a nove usando list comprehension
string = '012345678901234567890123456789012345678901234567890123456789'
n = 10
list_names = [string[i: i + n] for i in range(0, len(string), n)]

# Separar os grupos por '.'
break_apart = '.'.join(list_names)
