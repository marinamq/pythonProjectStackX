# Algoritmo: Idade para voto
# Dev: Marina Queiroz
# 22.08.2022

AnoNascimento = int(input("Digite o ano que você nasceu: "))
print("Você nasceu em ", AnoNascimento)

if AnoNascimento > 2006:
    print("Você não poderá votar este ano!")
else:
    print("Você poderá votar este ano!")
