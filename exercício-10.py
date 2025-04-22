# EXERCÍCIO 10 #
def eh_kaprekar(n):
    if n == 1:
        return True
    quadrado = str(n ** 2)
    for i in range(1, len(quadrado)):
        esquerda = int(quadrado[:i])
        direita = int(quadrado[i:])
        if direita != 0 and esquerda + direita == n:
            return True
    return False

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

print(f"Números de Kaprekar entre {inicio} e {fim}:")
for num in range(inicio, fim + 1):
    if eh_kaprekar(num):
        print(num)

