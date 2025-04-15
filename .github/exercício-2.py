#EXERCÍCIO 2 #
N = int(input("Digite um número inteiro positivo: "))
if N > 0:
    contador = 1
    soma = 0
    while contador <= N:
        soma = soma + contador
        contador = contador + 1
    print("A soma de 1 até", N, "é:", soma)
else:
    print("Por favor, digite um número maior que zero!")