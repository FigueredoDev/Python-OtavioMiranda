def main():
    print("""
1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.

2 - Faça um Programa que peça um número e então mostre a mensagem:
número informado foi [número].

3 - Faça um programa que receba um número inteiro e verifique se este número é
maior que 20, em caso afirmativo o programa deverá multiplicar o valor por 2 e
após o cálculo imprimir a mensagem: "Resultado: <valor do resultado>", em que
<valor do resultado> deve ser substituído pelo resultado do cálculo.

4 - Segundo uma tabela médica, o peso ideal está relacionado com a altura e o sexo.
Faça um programa que receba a altura e o sexo de uma pessoa, após isso calcule
e imprima o seu peso ideal, utilizando as seguintes fórmulas:
• Para homens: (72,7 * A) – 58
• Para mulheres: (62,1 * A) – 44,7
Em que: A = Altura

5 - Faça um programa que leia 5 números e informe a soma e a média dos números.

6 - Faça um programa que leia "n" valores. O programa deve inicialmente solicitar ao
usuário que informe a quantidade desejada de valores a ser informada, depois ler
os "n" valores e ao final imprimir a média aritmética dos valores lidos.

7 - Sair
    """)


def questao1():
    print("Alo Mundo.")


def questao2():
    numero = input("Digite seu numero: ")
    print("O numero digitado foi", numero)


def questao3():
    numero = int(input("Digite um número: "))

    if numero > 20:
        numero *= 2
        print(f"Resultado: {numero}")
    else:
        print(f"Numero digitado: {numero}")


def questao4():
    print("Digite 'M' para MASCULINO ou 'F' para FEMININO")

    sexo = str(input("Digite seu sexo:"))
    alt = float(input("Digite sua altura:"))

    if sexo == 'M':
        p_ideal = (72.7 * al
    main()
    valor = int(input("Digite o valor correspondente a atividade: "))

    if valor == 1:
        questao1()
    elif valor == 2:
        questao2()
    elif valor == 3:
        questao3()
    elif valor == 4:
        questao4()
    elif valor == 5:
        questao5()
    elif valor == 6:
        questao6()
    elif valor == 7:
        ...
    else:
        print("Valor incorreto")
t) - 58
        print("Seu peso ideal é: %.2fkg" % p_ideal)

    if sexo == 'F':
        p_ideal = (62.1 * alt) - 44.7
        print("Seu peso ideal é: %.2fkg " % p_ideal)


def questao5():
    soma = 0
    for i in range(5):
        num = int(input("Digite um numero:"))
        soma = soma + num
        media = soma / 5

    print("Soma :", soma)
    print(f"Média({soma}/5): {media}")


def questao6():
    i = 1
    soma = 0
    n = int(input("Digite a quantidade desejada de valores:"))
    print("Quantidade informada: ",  n)

    for i in range(n):
        num = int(input("Informe o numero:"))
        soma = soma+num
        media = soma / n

    print(f"Média({soma}/{n}): {media} ")


def sair():
    valor = input("Fechar sistema? S para sim e N para nao")
    if valor == "S" or valor == "s":
        exit()
    else:
        ...


main()
valor = int(input("Digite o valor correspondente a atividade: "))

if valor == 1:
    questao1()
elif valor == 2:
    questao2()
elif valor == 3:
    questao3()
elif valor == 4:
    questao4()
elif valor == 5:
    questao5()
elif valor == 6:
    questao6()
elif valor == 7:
    ...
else:
    print("Valor incorreto")
