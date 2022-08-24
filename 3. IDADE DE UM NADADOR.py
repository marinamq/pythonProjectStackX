# ALGORITIMO: IDADE DE UM NADADOR
# DEV: MARINA QUEIROZ
# 16.08.2022

Idade = int(input("Digite a sua idade: "))

if Idade < 5:
    print("Esta categoria é inexistente, digite novamente.")
elif Idade >= 5 and Idade <= 7:
    print("A sua idade é", Idade, "anos e você está na categoria Infantil")
elif Idade >= 8 and Idade <= 10:
    print("A sua idade é", Idade, "anos e você está na categoria Juvenil")
elif Idade >= 11 and Idade <= 15:
    print("A sua idade é", Idade, "anos e você está na categoria Adolescente")
elif Idade >= 16 and Idade <= 30:
    print("A sua idade é", Idade, "anos e você está na categoria Adulto")
elif Idade > 30:
    print("A sua idade é", Idade, "anos e você está na categoria Sênior")