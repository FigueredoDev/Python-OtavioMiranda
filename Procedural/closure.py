def criar_saudação(saudação, nome):
    def saudar():
        return f"{saudação}, {nome}"

    return saudar()


s1 = criar_saudação("Bom dia", "Luiz")
s2 = criar_saudação("Boa noite", "Jhonata")

print(s1)
print(s2)
