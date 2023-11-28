sal_min = float(input("Digite o valor do salário mínimo atual (R$): "))
turno_trab = str(input("Digite o turno de trabalho | M - Matuino | V - Vespertino | N - Notruno: "))
categoria = str(input("Digite a Categoria | O - Operário | G - Gerente : "))
nr_hr_trab = int(input("Digite o número de horas trabalhadas no mês: "))

#COEFICIENTE DE SALÁRIO 
if turno_trab in ['M','m','V','v','n','N']:
    if turno_trab in ['M', 'm']:
        coef_sal = sal_min * 0.1
        print(f'O coeficiente de salário será de R$ {coef_sal}')
    elif turno_trab in ['V','v']:
        coef_sal =  sal_min * 0.15
        print(f'O coeficiente de salário será de R$ {coef_sal}')
    elif turno_trab in ['n', 'N']:
        coef_sal = sal_min * 0.12
        print(f'O coeficiente de salário será de R$ {coef_sal}')
#SALÁRIO BRUTO
sal_bruto = nr_hr_trab * coef_sal
print(f'O SEU SALÁRIO BRUTO É DE: R$ {sal_bruto}')
#IMPOSTO
if categoria in ['O','o','G','g']:
    if categoria in ['O','o'] and sal_bruto >= 300:
        imposto = sal_bruto * 0.05
        print(f"Imposto sobre o salário de R$ {imposto}")
    elif categoria in ['O','o'] and sal_bruto < 300:
        imposto = sal_bruto * 0.03
        print(f"Imposto sobre o salário de R$ {imposto}")
    elif categoria in ['G','g'] and sal_bruto >= 400:
        imposto = sal_bruto * 0.06
        print(f"Imposto sobre o salário de R$ {imposto}")
    elif categoria in ['G','g'] and sal_bruto < 400:
        imposto = sal_bruto * 0.04
        print(f"Imposto sobre o salário de R$ {imposto}")
#GRATIFICAÇÃO
#REQUISITOS --> TURNO == NOTURNO | NÚMERO DE HORAS TRABALHADAS == SUPERIOR A 80 HORAS
if turno_trab in ['n', 'N'] and nr_hr_trab > 80:
    gratificacao = 50
    print(f'VOCÊ RECEBERÁ UMA GRATIFICAÇÃO DE R$ {gratificacao}')
else:
    gratificacao = 30
    print(f'VOCÊ RECEBERÁ UMA GRATIFICAÇÃO DE R$ {gratificacao}')
# AUX ALIMENTAÇÃO 
# REQUISITOS --> CATEGORIA == OPERÁRIO | COEFICIENTE DE SALÁRIO <= 25
if categoria in ['O','o'] and coef_sal <= 80:
    aux_alimentacao = sal_bruto / 3
    print(f'VOCÊ RECEBERÁ UM AUXILÍO ALIMENTAÇÃO DE R$ {aux_alimentacao}')
else:
    aux_alimentacao = sal_bruto / 2
    print(f'VOCÊ RECEBERÁ UM AUXILÍO ALIMENTAÇÃO DE R$ {aux_alimentacao}')
#SALÁRIO LÍQUIDO = SALÁRIO BRUTO - IMPOSTO + GRATIFICAÇÃO + AUXÍLIO ALIMENTAÇÃO
sal_liquido = sal_bruto - imposto + gratificacao + aux_alimentacao
if sal_liquido < 350:
    print(f' SALÁRIO LÍQUIDO: R$ {sal_liquido} | MAL REMUNERADO')
elif sal_liquido >= 350 and sal_liquido < 600:
    print(f' SALÁRIO LÍQUIDO: R$ {sal_liquido} |NORMAL')
elif sal_liquido > 600:
    print(f' SALÁRIO LÍQUIDO: R$ {sal_liquido} | BEM REMUNERADO')
    