# Algoritmo: Gratificacao de Natal
# Dev: Marina Queiroz
# 16.08.2022

HorasExtras = float(input("Digite o número de horas extras: "))
HorasFaltas = float(input("Digite o número de horas faltantes: "))

SaldoHoras = (HorasExtras - (2/3*HorasFaltas)) * 60

if SaldoHoras < 600:
    print("Saldo horas: ", SaldoHoras, "O prêmio a receber é de R$ 100.00")
elif SaldoHoras >= 600 and SaldoHoras <= 1200:
    print("Saldo horas: ", SaldoHoras, "O prêmio a receber é de R$ 200.00")
elif SaldoHoras >= 1201 and SaldoHoras <= 1800:
    print("Saldo horas: ", SaldoHoras, "O prêmio a receber é de R$ 300.00")
elif SaldoHoras >= 1801 and SaldoHoras <= 2400:
    print("Saldo horas: ", SaldoHoras, "O prêmio a receber é de R$ 400.00")
elif SaldoHoras >= 2401:
    print("Saldo horas: ", SaldoHoras, "O prêmio a receber é de R$ 500.00")

