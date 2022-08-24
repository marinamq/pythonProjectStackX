# ALGORITIMO: SALARIO BRUTO
# DEV: MARINA QUEIROZ
# 19.08.2022

SalarioBruto = float(input("Digite o salário bruto: "))

Imposto = 0.07

if SalarioBruto <= 350:
    SalarioLiquido = (SalarioBruto + 100) - (SalarioBruto * Imposto)
    print("Salário líquido é: ", SalarioLiquido)
elif SalarioBruto >= 351 and SalarioBruto <= 600:
    SalarioLiquido = (SalarioBruto + 75) - (SalarioBruto * Imposto)
    print("Salário líquido é: ", SalarioLiquido)
elif SalarioBruto >= 601 and SalarioBruto <= 900:
    SalarioLiquido = (SalarioBruto + 50) - (SalarioBruto * Imposto)
    print("Salário líquido é: ", SalarioLiquido)
elif SalarioBruto >= 901:
    SalarioLiquido = (SalarioBruto + 35) - (SalarioBruto * Imposto)
    print("Salário líquido é: ", SalarioLiquido)
