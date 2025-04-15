# EXERCÍCIO 3 #
numero =int(input("Digite o número inteiro que você deseja obter a tabuada:"))
tabuada = 1
for x in range (1,11):
    tabuada = numero * x
    print(numero, "x", x, "=", tabuada)