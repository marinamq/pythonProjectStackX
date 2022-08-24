# Algoritmo: Idade e Peso (IF)
# Dev: Marina Queiroz
# 16.08.2022

Idade = int(input("Qual a sua idade: "))

Peso = float(input("Qual o seu peso: "))

if Idade < 20 and Peso <= 60:
    print("Sua idade é",Idade, "anos e o seu peso é",Peso, "kilos e o seu grupo de risco é 9")
elif Idade < 20 and Peso > 60 and Peso <= 90:
    print("Sua idade é", Idade, "anos e o seu peso é", Peso, "kilos e o seu grupo de risco é 8")
elif Idade < 20 and Peso > 90:
    print("Sua idade é", Idade, "anos e o seu peso é", Peso, "kilos e o seu grupo de risco é 7")
elif Idade >= 20 and Idade <= 50 and Peso <= 60:
    print("Sua idade é", Idade, "anos e o seu peso é", Peso, "kilos e o seu grupo de risco é 6")
elif Idade >= 20 and Idade <= 50 and Peso > 60 and Peso <= 90:
    print("Sua idade é", Idade, "anos e o seu peso é", Peso, "kilos e o seu grupo de risco é 5")
elif Idade >= 20 and Idade <= 50 and Peso > 90:
    print("Sua idade é", Idade, "anos e o seu peso é", Peso, "kilos e o seu grupo de risco é 4")
elif Idade > 50 and Peso <= 60:
    print("Sua idade é", Idade, "anos e o seu peso é", Peso, "kilos e o seu grupo de risco é 3")
elif Idade > 50 and Peso > 60 and Peso <= 90:
    print("Sua idade é", Idade, "anos e o seu peso é", Peso, "kilos e o seu grupo de risco é 2")
elif Idade > 50 and Peso > 90:
    print("Sua idade é", Idade, "anos e o seu peso é", Peso, "kilos e o seu grupo de risco é 1")