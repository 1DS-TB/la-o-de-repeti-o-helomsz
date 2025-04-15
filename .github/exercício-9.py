# EXERCÍCIO 9 #
def somar_divisores(n):
    soma = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            soma += i
    return soma
for num in range(1, 10001):
    if somar_divisores(num) == num:
        print(f"Entre 1 e 1000 O número {num} é considerado perfeito" )
