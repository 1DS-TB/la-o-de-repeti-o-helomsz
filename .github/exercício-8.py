# EXERCÍCIO 8 #
num = int(input("Digite o valor de N: "))
soma = 0
for i in range(1, num + 1):
    soma += 1 / i
soma_arredondada = round(soma, 2)
print(f"A soma da série harmônica até {num} termos é: {soma_arredondada}")