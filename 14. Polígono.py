# Algoritmo: Polígono
# Dev: Marina Queiroz
# 23.08.2022

NumeroLados = int(input("Digite o número de lados: "))
MedidaLado = float(input("Digite a medida do lado em cm: "))

if NumeroLados == 3:
    Area = (MedidaLado * MedidaLado) / 2
    print("Triângulo e área de: ", Area, "cm²")
elif NumeroLados == 4:
    Area = MedidaLado * MedidaLado
    print("Quadrado e área de: ", Area, "cm²")
elif NumeroLados == 5:
    print("Pentágono")
