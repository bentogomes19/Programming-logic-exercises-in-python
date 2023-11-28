#FAÇA UM PROGRAMA QUE APRESENTE O MENU A SEGUIR, PERMITA AO USUÁRIO ESCOLHER A OPÇÃO DESEJADA, RECEBA
#OS DADOS NECESSÁRIOS PARA EXECUTAR A OPERAÇÃO E MOSTRE O RESULTADO. VERIFIQUE A POSSIBILIDADE DE
#OPÇÃO INVÁLIDA E NÃO SE PREOCUPE COM RESTRIÇÕES, COMO SALÁRIO NEGATIVO
# MENU DE OPÇÕES:
#   1.  IMPOSTO
#   2.  NOVO SALÁRIO
#   3.  CLASSIFICAÇÃO
#   DIGITE A OPÇÃO DESEJADA.

print("MENU DE OPÇÕES:")
print("------------------")
print(" 1. IMPOSTO")
print(" 2. NOVO SALÁRIO")
print(" 3. CLASSIFICAÇÃO")
op = int(input("DIGITE A OPÇÃO DESEJADA: "))
if op==1:
    sal = float(input("Informe o seu salário r$: "))
    if sal < 500:
        imp = 0.05
        vlr_imp = (sal * imp) 
        novo_sal = sal - vlr_imp
        print(f"Valor do imposto cobrado: R$ {vlr_imp} o que equivale a 5%")
        print(f"O seu novo salário com o percentual de imposto cobrado: R$ {novo_sal}")
    else:
        if sal >=500 and sal <=850:
            imp = 0.10
            vlr_imp = (sal * imp) 
            novo_sal = sal - vlr_imp
            print(f"Valor do imposto cobrado: R$ {vlr_imp} o que equivale a 10%")
            print(f"O seu novo salário com o percentual de imposto cobrado: R$ {novo_sal}")
        else:
            if sal>850:
                imp = 0.15
                vlr_imp = (sal * imp) 
                novo_sal = sal - vlr_imp
                print(f"Valor do imposto cobrado: R$ {vlr_imp} o que equivale a 15%")
                print(f"O seu novo salário com o percentual de imposto cobrado: R$ {novo_sal}")
                
if op==2:
    sal = float(input("Informe o seu salário r$: "))
    if sal >1500:
        novo_sal = sal + 25
        print(f"O valor do novo salário com o aumento é: R$ {novo_sal}")
    else:
        if sal >=750 and sal <=1500:
            novo_sal = sal + 50
            print(f"O valor do novo salário com o aumento é: R$ {novo_sal}")
        else:
            if sal >=450 and sal <=750:
                novo_sal = sal + 75
                print(f"O valor do novo salário com o aumento é: R$ {novo_sal}")
            else:
                if sal <450:
                    novo_sal = sal + 100
                    print(f"O valor do novo salário com o aumento é: R$ {novo_sal}")

if op==3:
    sal = float(input("Informe o seu salário r$: "))
    if sal <=750:
        print("CLASSIFICAÇÃO: MAL REMUNERADO")
    elif sal >700:
        print("CLASSIFICAÇÃO: BEM REMUNERADO")
        
if op < 1 or op >3:
    print("OPÇÃO INVÁLIDA!")
        
            
    
        
        
                
    
