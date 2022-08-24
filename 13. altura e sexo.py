# Algoritmo: altura e sexo
# Dev: Marina Queiroz
# 22.08.2022

Altura = float(input("Digite a altura em metros: "))

Sexo = int(input("Digite o sexo 1-Feminino ou 2-Masculino: "))

if Sexo == 2:
    PesoIdeal = (Altura * 72.7) - 58
else:
    PesoIdeal = (Altura * 62.1) - 44.7

print("Seu peso ideal é: ", PesoIdeal, "kilos.")
