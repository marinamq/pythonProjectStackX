# ALGORITIMO: EMPRESA COM 10 FUNCIONÁRIOS
# DEV: MARINA QUEIROZ
# 19.08.2022

Laco1 = 1
Laco2 = True
Laco3 = True


while Laco1 <= 3:

    SalarioMinimo = 450
    SalarioInicial = 0
    SalarioFinal = 0
    AuxilioAlimentacao = 0

    Codigo = int(input("Digite o código: "))
    HoraTrabalhada = float(input("Digite a quantidade de horas trabalhadas no mês: "))


    while Laco2:
        Categoria = str(input("Digite a categoria: "))
        if Categoria == "O" or Categoria == "G":
            Laco2 = False
        else:
            print("As categorias possíveis são O ou G, digite novamente")
            continue
        break


    while Laco3:
       Turno = str(input("Digite o turno: "))
       if Turno == "M" or Turno == "V" or Turno == "N":
           Laco3 = False
       else:
           print("Os turnos possíveis são M, V ou N, digite novamente")
           continue
       break

    if Categoria == "G" and Turno == "N":
        ValorHora = 0.18 * SalarioMinimo
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = 0.20 * SalarioInicial
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = 0.15 * SalarioInicial
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = 0.05 * SalarioInicial
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        break

    if Categoria == "G" and Turno == "M" or Turno == "V":
        ValorHora = 0.15 * SalarioMinimo
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = 0.20 * SalarioInicial
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = 0.15 * SalarioInicial
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = 0.05 * SalarioInicial
            SalarioFinal = SalarioInicial + AuxilioAlimentacao


    if Categoria == "O" and Turno == "M" or Turno == "V":
        ValorHora = 0.10 * SalarioMinimo
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = 0.20 * SalarioInicial
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = 0.15 * SalarioInicial
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = 0.05 * SalarioInicial
            SalarioFinal = SalarioInicial + AuxilioAlimentacao


    print("Seu código é: ", Codigo, "e Trabalhou :", HoraTrabalhada, "horas e seu salario inicial é: ", SalarioInicial)
    print("O valor de auxílio alimentação é: ", AuxilioAlimentacao, "e o seu salário final é: ", SalarioFinal)

    print("Número do laço principal:", Laco1)
    Laco1 = Laco1 + 1
    Laco2 = True
    Laco3 = True
