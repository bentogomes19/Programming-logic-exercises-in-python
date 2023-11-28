#FAÇA UM PROGRAMA QUE RECEBA O VALOR DO SALÁRIO MÍNIMO E O VALOR DE UM FUNCIONÁRIO, CALCULE E MOSTRE
#A QUANTIDADE DE SALÁRIOS MÍNIMOS QUE ESSE FUNCIONÁRIO GANHA.  

sal_minimo = float(input("Digite o valor do salário minimo atual (R$): "))
sal_funcionario = float(input("Digite o valor do seu salário atual (R$): "))
qtd_salmin = sal_funcionario / sal_minimo
print(f"{qtd_salmin} a quantidade de salários mínimos.")
