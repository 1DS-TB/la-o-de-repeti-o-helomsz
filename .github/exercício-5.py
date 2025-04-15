# EXERCÍCIO 5 #
num = int(input("Digite um número: "))
mult=0
for count in range(2,num):
    if (num % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Tem",mult," múltiplos acima de 2 e abaixo de",num)
