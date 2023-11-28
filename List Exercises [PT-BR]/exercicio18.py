# FAÇA UM PROGRAMA QUE RECEBA O SALÁRIO DE UM FUNCIONÁRIO, CALCULE E MOSTRE O NOVO SALÁRIO, ACRESCIDO
# DE BONIFICAÇÃO E DE AUXÍLIO ESCOLA
#       SALÁRIO                 BONIFICAÇÃO
#   ATÉ R$ 500,00               5% DO SALÁRIO
#   R$ 500,00 E R$ 1.200,00     12% DO SALÁRIO
#   ACIMA DE R$1.200,00         SEM BONIFICAÇÃO
#-------------------------------------------------------------------------
#           SALÁRIO             AUXÍLIO ESCOLA
#        ATÉ R$ 600,00          R$ 150,000
#        MAIS QUE R$ 600,00     R$ 100,00

sal_funcionário = float(input("Digite o seu salário (R$): "))
if sal_funcionário <= 500:
    novo_salário1 = (sal_funcionário * 0.05) + sal_funcionário
    
elif sal_funcionário > 500 and sal_funcionário <= 1200:
    novo_salário1 = (sal_funcionário * 0.12) + sal_funcionário
elif sal_funcionário > 1200:
    print("SEM BONIFICAÇÃO")
    
if sal_funcionário <=600:
    novo_salário2 = novo_salário1 + 150
    print(f"O seu novo salário é de: {novo_salário2}")
else:
    novo_salário2 = novo_salário1 + 100
    print(f"O seu novo salário é de: {novo_salário2}")
    

    
        
    
    