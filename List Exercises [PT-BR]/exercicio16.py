#FAÇA UM PROGRAMA QUE RECEBA O CÓDIGO CORRESPONDENTE AO CARGO DE UM FUNCIONÁRIO E SEU SALÁRIO ATUAL
#E MOSTRE O CARGO, O VALOR DO AUMENTO E SEU NOVO SALÁRIO. OS CARGOS ESTÃO MA TABELA ABAIXO
#CÓDIGO     CARGO       PERCENTUAL
#   1   ESCRITUÁRIO         50%
#   2   SECRETÁRIO          35%
#   3   CAIXA               20%
#   4   GERENTE             10%
#   5   DIRETOR      "NÃO TEM AUMENTO"

codigo = int(input("Digite o código do cargo correspondente: "))
sal_funcionario = float(input("Digite o seu salário: "))

if codigo ==1:
    print("CARGO: ESCRITUÁRIO")
    print(f"Seu salário atual é de: R$ {sal_funcionario}")
    aumento = (sal_funcionario * 0.5)
    print(f"O valor do aumento é de: R$ {aumento}")
    novo_sal_funcionario = aumento + sal_funcionario
    print(f"O seu novo salário será de: R$ {novo_sal_funcionario}")
elif codigo ==2:
    print("CARGO: SECRETÁRIO")
    print(f"Seu salário atual é de: R$ {sal_funcionario}")
    aumento = (sal_funcionario * 0.35)
    print(f"O valor do aumento foi de: R$ {aumento}")
    novo_sal_funcionario = aumento + sal_funcionario
    print(f"O seu novo salário será de: R$ {novo_sal_funcionario}")    
elif codigo ==3:
    print("CARGO: CAIXA")
    print(f"Seu salário atual é de: R$ {sal_funcionario}")
    aumento = (sal_funcionario * 0.20)
    print(f"O valor do aumento foi de: R$ {aumento}")
    novo_sal_funcionario = aumento + sal_funcionario
    print(f"O seu novo salário será de: R$ {novo_sal_funcionario}")
elif codigo ==4:
    print("CARGO: GERENTE")
    print(f"Seu salário atual é de: R$ {sal_funcionario}")
    aumento = (sal_funcionario * 0.10)
    print(f"O valor do aumento foi de: R$ {aumento}")
    novo_sal_funcionario = aumento + sal_funcionario
    print(f"O seu novo salário será de: R$ {novo_sal_funcionario}")
elif codigo ==5:
    print("CARGO: DIRETOR")
    print(f"Seu salário atual é de: R$ {sal_funcionario}")
    aumento = (sal_funcionario * 0)
    print("NÃO TEM AUMENTO")    