# Algoritmo: Três valores e o maior deles
# Dev: Marina Queiroz
# 23.08.2022

Num1 = int(input("Digite o primeiro número: "))
Num2 = int(input("Digite o segundo número: "))
Num3 = int(input("Digite o terceiro número: "))

if Num1 > Num2 and Num1 > Num3:
    Maior = Num1
    print("O maior número é: ", Maior)
elif Num2 > Num1 and Num2 > Num3:
    Maior = Num2
    print("O maior número é: ", Maior)
else:
    Maior = Num3
    print("O maior número é: ", Maior)
