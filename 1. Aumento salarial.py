# Algoritmo: Aumento Salarial
# Dev: Marina Queiroz
# 23.08.2022

PercentualAumento = 0.015

for i in range(2000, 2017):
    if i == 2000:
        SalarioInicial = 1000
    elif i == 2001:
        ReajusteSalarioAnual = SalarioInicial * PercentualAumento
        SalarioAcumulado = SalarioInicial + ReajusteSalarioAnual
        print("O salario em 2001 é de : ", SalarioAcumulado)
    else:
        ReajusteSalarioAnual = SalarioAcumulado * (PercentualAumento * 2)
        SalarioAcumulado = SalarioAcumulado + ReajusteSalarioAnual
        print("O salario final é de : ", SalarioAcumulado)
