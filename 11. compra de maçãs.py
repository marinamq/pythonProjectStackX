# Algoritmo: Compra de maçãs
# Dev: Marina Queiroz
# 22.08.2022

NumMaca = int(input("Digite a quantidade de maçãs compradas: "))

if NumMaca < 12:
    ValorCompra = NumMaca * 0.30
else:
    ValorCompra = NumMaca * 0.25

print("O valor total da compra é de: ", ValorCompra)

