# Algoritmo: 3 valores inteiros
# Dev: Marina Queiroz
# 22.08.2022

Num1 = int(input("Digite o primeiro valor: "))
Num2 = int(input("Digite o segundo valor: "))
Num3 = int(input("Digite o terceiro valor: "))

if Num1 == Num2 or Num1 == Num3 or Num2 == Num3:
    print("Os valores não podem ser iguais. Digite Novamente!")

if Num1 < Num2 and Num1 < Num3:
    Ordem1 = Num1
    if Num2 < Num3:
        Ordem2 = Num2
        Ordem3 = Num3
    else:
        Ordem2 = Num3
        Ordem3 = Num2

if Num2 < Num1 and Num2 < Num3:
    Ordem1 = Num2
    if Num1 < Num3:
        Ordem2 = Num1
        Ordem3 = Num3
    else:
        Ordem2 = Num3
        Ordem3 = Num1

if Num3 < Num1 and Num3 < Num2:
    Ordem1 = Num3
    if Num1 < Num2:
        Ordem2 = Num1
        Ordem3 = Num2
    else:
        Ordem2 = Num2
        Ordem3 = Num1

print("Os números em ordem crescente são: ", Ordem1, Ordem2, Ordem3)
