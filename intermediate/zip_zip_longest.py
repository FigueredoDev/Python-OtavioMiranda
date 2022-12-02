
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
list_a     = [1, 2, 3, 4, 5, 6, 7]
list_b     = [1, 2, 3, 4]
=== resultado ===
list_sum  = [2, 4, 6, 8]
"""
list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]

list_sum = zip(list_a, list_b)
total = [(x + y) for x, y in list_sum]
# Resultado = 2,4,6,8

print(total)

# Código do professor
list_a = [10, 2, 3, 40, 5, 6, 7]
list_b = [1, 2, 3, 4]
list_sum = [x + y for x, y in zip(list_a, list_b)]  # type: ignore
print(list_sum)
