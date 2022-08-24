# Algoritmo: compra de produtos
# Dev: Marina Queiroz
# 23.08.2022

CodigoProduto = int(input("Digite o código do produto: "))
Quantidade = int(input(("Digite a quantidade comprada do produto: ")))

if CodigoProduto >= 1 and CodigoProduto <= 10:
    PrecoUnit = 10
    PrecoTotal = Quantidade * 10
    if PrecoTotal <= 250:
        PrecoFinal = PrecoTotal * 0.95
        print("O valor final da compra é: ", PrecoFinal)
    else:
        PrecoFinal = PrecoTotal
        print("O valor final da compra é: ", PrecoFinal)
if CodigoProduto > 10 and CodigoProduto <= 20:
    PrecoUnit = 15
    PrecoTotal = Quantidade * 15
    if PrecoTotal > 250 and PrecoTotal <= 500:
        PrecoFinal = PrecoTotal * 0.90
        print("O valor final da compra é: ", PrecoFinal)
    else:
        PrecoFinal = PrecoTotal
        print("O valor final da compra é: ", PrecoFinal)
if CodigoProduto > 20 and CodigoProduto <= 30:
    PrecoUnit = 20
    PrecoTotal = Quantidade * 20
    if PrecoTotal > 50:
        PrecoFinal = PrecoTotal * 0.85
        print("O valor final da compra é: ", PrecoFinal)
    else:
        PrecoFinal = PrecoTotal
        print("O valor final da compra é: ", PrecoFinal)
if CodigoProduto > 30 and CodigoProduto <= 40:
    PrecoUnit = 30
    PrecoTotal = Quantidade * 30
    print("O valor final da compra é: ", PrecoTotal)


