#Faça um programa que receba o salário base e o tempo de serviço de um funcionário. Calcule e mostre: 
#   ■■ O imposto, conforme a tabela a seguir. 
#   sALário BAsE                                            % soBrE o sALário BAsE
#   <R$ 200,00                                                      isento
#   Entre R$ 200,00 (inclusive) e R$ 450,00 (inclusive)               3%
#   Entre R$ 450,00 e R$ 700,00                                       8%
#   >= R$ 700,00                                                      12%
#A gratificação, de acordo com a tabela a seguir.
#   Salário Base                     Tempo de Serviço            Gratificação                                    
# Superior a R$ 500,00                  Até 3 anos                      20
#                                       Mais de 3 anos                  30
# Até R$ 500,00                         Até 3 anos                      23
#                                       Entre 3 e 6 anos                35
#                                       De 6 anos para cima             33
#
#O salário líquido, ou seja, salário base menos imposto mais gratificação. 
#    ■■ A categoria, que está na tabela a seguir :
#               sALário Líquido             CLAssiFiCAção
#               Até R$ 350,00                       A 
#               Entre R$ 350,00 e R$ 600,00         B
#               De R$ 600,00 para cima              C
#variáveis = sal_base, tempo_servico, imposto, gratificacao, sal_liquido

sal_base = float(input("Digite o seu salário base (R$): "))
tempo_servico = int(input("Digite o tempo de serviço na empresa (Anos): "))
#IMPOSTO
if sal_base < 200:
    imposto = sal_base * 0 
    print("COM O SALÁRIO INFORMADO VOCÊ ESTÁ ISENTO DE IMPOSTO!!")
else:
    if sal_base <= 450:
        imposto = sal_base * 0.03
        print(f"Você irá pagar de imposto: R$ {imposto}")
    else:
        if sal_base < 700:
            imposto = sal_base * 0.08
            print(f"Você irá pagar de imposto: R$ {imposto}")
        else:
            if sal_base >= 700:
                imposto = sal_base * 0.12
                print(f"Você irá pagar de imposto: R$ {imposto}")
#GRATIFICAÇÃO
if sal_base > 500 and tempo_servico <=3:
    gratificacao = 20
    print(f"Gratificação de R$ {gratificacao}")
elif sal_base > 500 and tempo_servico > 3:
    gratificacao = 30
    print(f"Gratificação de R$ {gratificacao}")
elif sal_base <= 500 and tempo_servico <= 3:
    gratificacao = 23
    print(f"Gratificação de R$ {gratificacao}")
elif sal_base <= 500 and (tempo_servico >= 3 and tempo_servico < 6):
    gratificacao = 35 
    print(f"Gratificação de R$ {gratificacao}")
elif sal_base <= 500 and tempo_servico >= 6:
    gratificacao = 33
    print(f'Gratificação de R$ {gratificacao}')
#SALÁRIO LÍQUIDO
sal_liquido = sal_base - imposto + gratificacao
if sal_liquido < 350:
    print(f"CLASSIFICAÇÃO A | R$ {sal_liquido} ") 
elif sal_liquido >= 350 and sal_liquido < 600:
    print(f"CLASSIFICAÇÃO B | R$ {sal_liquido} ") 
elif sal_liquido >= 600:
    print(f"CLASSIFICAÇÃO C | R$ {sal_liquido} ") 