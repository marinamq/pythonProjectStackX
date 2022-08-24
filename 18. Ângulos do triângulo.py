# Algoritmo: Ângulos doTriângulo
# Dev: Marina Queiroz
# 23.08.2022

Angulo1 = float(input("Digite o primeiro ângulo: "))
Angulo2 = float(input("Digite o segundo ângulo: "))
Angulo3 = float(input("Digite o terceiro ângulo: "))

if Angulo1 < 90 and Angulo2 < 90 and Angulo3 < 90:
    print("Este triângulo é Acutângulo")
elif Angulo1 == 90 or Angulo2 == 90 or Angulo3 == 90:
    print("Este triângulo é Retângulo")
else:
    print("Este triângulo é Obtusângulo")
