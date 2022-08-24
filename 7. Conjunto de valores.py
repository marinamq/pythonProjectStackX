# Algoritmo: Conjunto de valores
# Dev: Marina Queiroz
# 22.08.2022

import math

ValorLido = float(input("Digite um número: "))

while ValorLido > 0:

    Quadrado = ValorLido * ValorLido
    print("quadrado é: ", Quadrado)
    Cubo = Quadrado * ValorLido
    print("cubo é: ", Cubo)
    print("raíz quadrada é: ", math.sqrt(ValorLido))
    break

if ValorLido <= 0:
    print("Cálculo Finalizado")
