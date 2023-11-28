#FAÇA UM PROGRAMA QUE RECEBA O VALOR DO SALÁRIO MÍNIMO, O NÚMERO DE HORAS TRABALHADAS, O NÚMERO DE
#DEPENDENTES DO FUNCIONÁRIO E A QUANTIDADE DE HORAS EXTRAS TRABALHADAS. CALCULE E MOSTRE O SALÁRIO A RECEBER
#DO FUNCIONÁRIO DE ACORDO COM AS REGRAS A SEGUIR:
#   O VALOR DA HORA TRABALHADA É IGUAL A 1/5 DO SALÁRIO MÍNIMO
#   O SALÁRIO DO MÊS É IGUAL AO NÚMERO DE HORAS TRABALHADAS MULTIPLICADO PELO VALOR DA HORA TRABALHADA
#   PARA CADA DEPENDENTE, ACRESCENTAR R$ 32,00
#   PARA CADA HORA EXTRA TRABALHADA, CALCULAR O VALOR DA HORA TRABALHADA ACRESCIDA DE 50%
#   O SALÁRIO BRUTO É IGUAL AO SALÁRIO DO MÊS MAIS O VALOR DOS DEPENDENTES MAIS O VALOR DAS HORAS EXTRAS
#   CALCULAR O VALOR DO IRRF RETIDO NA FONTE DE ACORDO COM A TABELA A SEGUIR.
#
#       IRRF                SALÁRIO BRUTO
#       ISENTO          INFERIOR A R$ 200,00
#       10%             DE R$ 200,00 ATÉ R$ 500,00
#       20%             SUPERIOR A R$ 500,00
#   O SALÁRIO LÍQUIDO É IGUAL AO SALÁRIO BRUTO MENOS O IRRF
#   A GRATIFICAÇÃO DE ACORDO COM A TABELA A SEGUIR:
#           SALÁRIO LÍQUIDO                 GRATIFICAÇÃO
#            ATÉ R$ 350,00                  R$ 100,00
#           SUPERIOR A R$ 350,00            R$ 50,00
#   O SALÁRIO A RECEBER DO FUNCIONÁRIO É IGUAL AO SALÁRIO LÍQUIDO MAIS A GRATIFICAÇÃO

print("Bem-vindo FUNCIONÁRIO")
nome_funcionário = str(input("Insira seu nome: "))
print(f"BEM-VINDO FUNCIONÁRIO: {nome_funcionário}")
print("Iremos coletar algumas informações ao seu respeito para calcular seu salário bruto e a receber")
resposta_funcionário = input("Você concorda seguir em frente Sim|Não: ").lower()

if resposta_funcionário in ['sim', 'Sim', 's']:
    salario_minimo = float(input("Por gentileza insira o valor do salário mínimo (R$): "))
    horas_trabalhadas = int(input("Digite o número de horas trabalhadas na empresa: "))
    dependentes = int(input("Insira a quantidade de dependentes: "))
    horas_extras = int(input("Digite a quantidade de horas extras trabalhadas: "))
    vlr_hrtrab = salario_minimo / 20
    sal_mes = horas_trabalhadas * vlr_hrtrab
    qtd_dependentes = dependentes * 32
    vlr_hrextra = ((vlr_hrtrab * 0.5) + vlr_hrtrab) * horas_extras
    sal_bruto = sal_mes + qtd_dependentes + vlr_hrextra
    if sal_bruto < 1700:
        print("VOCÊ ESTA ISENTO DE IRRF")
        print(f"Seu salário líquido é de: R$ {sal_bruto}")
    elif sal_bruto >= 1700 and sal_bruto <= 2500:
        irrf = sal_bruto * 0.1
        sal_liq = sal_bruto - irrf
        print(f"Seu salário líquido é de: R$ {sal_liq}")
    elif sal_bruto > 2500:
        irrf = sal_bruto * 0.2
        sal_liq = sal_bruto - irrf
        print(f"Seu salário líquido é de: R$ {sal_liq}")
        
    if sal_liq <= 950:
        gratificação = 350
        print(f"Seu salário líquido com a gratificação é de: R$ {sal_liq + gratificação}")
    else:
        gratificação = 150
        print(f"Seu salário líquido com a gratificação é de: R$ {sal_liq + gratificação}")      
    
else:
    print("Que pena! iremos terminar o processo...")


                        


