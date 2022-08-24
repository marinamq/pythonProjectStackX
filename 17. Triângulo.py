# Algoritmo: Triângulo
# Dev: Marina Queiroz
# 23.08.2022

Lado1 = float(input("Digite a medida do primeiro lado: "))
Lado2 = float(input("Digite a medida do segundo lado: "))
Lado3 = float(input("Digite a medida do terceiro lado: "))

if Lado1 == Lado2 and Lado2 == Lado3 and Lado1 == Lado3:
    print("Este triângulo é Equilátero")
elif Lado2 == Lado1 or Lado2 == Lado3 or Lado1 == Lado3:
    print("Este triângulo é Isósceles")
else:
    print("Este triângulo é Escaleno")
