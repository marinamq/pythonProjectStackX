# Algoritmo: Identificar erros
# Dev: Marina Queiroz
# 23.08.2022

# a)se (idade >= 65);
# mostre ("melhor idade");

if Idade >= 65:
    print("Melhor idade")

# b)se (genero = 1)
#   mostre ("Masculino")
# senão (genero == 2)
#   mostre ("Feminino");

if Genero == 1:
    print("Masculino")
else:
    print("Feminino")

# c) se preco > 10.50
#     preco = preco * 1,2;
# senão
#     preco = preco * 1.35;

if Preco > 10.50:
    Preco = Preco * 1.20
else:
    Preco = Preco * 1.35
