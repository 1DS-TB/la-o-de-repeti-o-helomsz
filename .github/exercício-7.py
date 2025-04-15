# EXERCÍCIO 7 #
num = int(input("Digite o valor de N: "))
for i in range(1, num + 1):
    for j in range(i):
        print("*", end="")
    print()