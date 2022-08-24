# Algoritmo: preço de produtos
# Dev: Marina Queiroz
# 23.08.2022


PrecoProduto = float(input("Digite o preço do produto: "))
Categoria = int(input("Digite o número da categoria desejada: "))
Situacao = str(input("Digite a letra da situação desejada: "))


if PrecoProduto <= 25:
    if Categoria == 1:
        ValorAumento = PrecoProduto + PrecoProduto * 0.05
        NovoPreco = ValorAumento - ValorAumento * 0.08
        if NovoPreco <= 50:
            print("barato")
        elif NovoPreco > 50 and NovoPreco < 120:
            print("normal")
        else:
            print("caro")
    elif Categoria == 2 or Situacao == "R":
        ValorAumento = PrecoProduto + PrecoProduto * 0.08
        NovoPreco = ValorAumento - ValorAumento * 0.05
        if NovoPreco <= 50:
            print("barato")
        elif NovoPreco > 50 and NovoPreco < 120:
            print("normal")
        else:
            print("caro")
    else:
        ValorAumento = PrecoProduto + PrecoProduto * 0.10
        NovoPreco = ValorAumento - ValorAumento * 0.08
        if NovoPreco <= 50:
            print("barato")
        elif NovoPreco > 50 and NovoPreco < 120:
            print("normal")
        else:
            print("caro")

if PrecoProduto > 25:
    if Categoria == 1:
        ValorAumento = PrecoProduto + PrecoProduto * 0.12
        NovoPreco = ValorAumento - ValorAumento * 0.08
        if NovoPreco <= 50:
            print("barato")
        elif NovoPreco > 50 and NovoPreco < 120:
            print("normal")
        else:
            print("caro")
    elif Categoria == 2 or Situacao == "R":
        ValorAumento = PrecoProduto + PrecoProduto * 0.15
        NovoPreco = ValorAumento - ValorAumento * 0.05
        if NovoPreco <= 50:
            print("barato")
        elif NovoPreco > 50 and NovoPreco < 120:
            print("normal")
        else:
            print("caro")
    else:
        ValorAumento = PrecoProduto + PrecoProduto * 0.18
        NovoPreco = ValorAumento - ValorAumento * 0.08
        if NovoPreco <= 50:
            print("barato")
        elif NovoPreco > 50 and NovoPreco < 120:
            print("normal")
        else:
            print("caro")
