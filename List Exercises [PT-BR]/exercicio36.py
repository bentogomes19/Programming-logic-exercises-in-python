#Faça um programa que receba o salário de um funcionário e, usando a tabela a seguir, calcule e mostre
#o novo salário

print('BEM VINDO FUNCIONÁRIO AO SISTEMA DE PAGAMENTO DA EMPRESA GENERAL ELETRICS S/A')
print('-----------------------------------------------------------------------------')
print('IREMOS CALCULAR O SEU NOVO SALÁRIO DE ACORDO COM OS NOVOS PARÂMETROS DA EMRPRESA\n')
print('FAIXA SALÁRIAL\t\t\t\t% DE AUMENTO')
print('ATÉ R$ 300,00                                50%')
print('R$ 300,00 até R$ 500,00                      40%')
print('R$ 500,00 até R$ 700,00                      30%')
print('R$ 700,00 até R$ 800,00                      20%')
print('R$ 800,00 até R$ 1.000,00                    10%')
print('Acima de R$ 1.000,00                          5%')
resposta_usuário = str(input('Você gostaria de prosseguir S/N?: '))
if resposta_usuário in ['S','s']:
    print('\nVAMOS DAR SEGUIMENTO AOS CALCULOS')
    sal_funcionário = float(input('DIGITE O VALOR DO SEU SALÁRIO ATUAL (R$): '))
    if sal_funcionário <= 300:
        aumento = (sal_funcionário * 0.5)
        novo_sal = aumento + sal_funcionário
        print(f'O SEU NOVO SALÁRIO SOFRERÁ UM AUMENTO DE R$ {aumento:.2f} | LOGO TENDO UM NOVO SALÁRIO DE R$ {novo_sal}')
    elif sal_funcionário > 300 and sal_funcionário <= 500:
        aumento = (sal_funcionário * 0.40)
        novo_sal = aumento + sal_funcionário
        print(f'O SEU NOVO SALÁRIO SOFRERÁ UM AUMENTO DE R$ {aumento:.2f} | LOGO TENDO UM NOVO SALÁRIO DE R$ {novo_sal}')
    elif sal_funcionário > 500 and sal_funcionário <= 700:
        aumento = (sal_funcionário * 0.30)
        novo_sal = aumento + sal_funcionário
        print(f'O SEU NOVO SALÁRIO SOFRERÁ UM AUMENTO DE R$ {aumento:.2f} | LOGO TENDO UM NOVO SALÁRIO DE R$ {novo_sal}')
    elif sal_funcionário > 700 and sal_funcionário <= 800:
        aumento = (sal_funcionário * 0.20)
        novo_sal = aumento + sal_funcionário
        print(f'O SEU NOVO SALÁRIO SOFRERÁ UM AUMENTO DE R$ {aumento:.2f} | LOGO TENDO UM NOVO SALÁRIO DE R$ {novo_sal}')
    elif sal_funcionário > 800 and sal_funcionário <= 100:
        aumento = (sal_funcionário * 0.10)
        novo_sal = aumento + sal_funcionário
        print(f'O SEU NOVO SALÁRIO SOFRERÁ UM AUMENTO DE R$ {aumento:.2f} | LOGO TENDO UM NOVO SALÁRIO DE R$ {novo_sal}')
    elif sal_funcionário > 1000:
        aumento = (sal_funcionário * 0.05)
        novo_sal = aumento + sal_funcionário
        print(f'O SEU NOVO SALÁRIO SOFRERÁ UM AUMENTO DE R$ {aumento:.2f} | LOGO TENDO UM NOVO SALÁRIO DE R$ {novo_sal}')
elif resposta_usuário in ['n','N']:
    print('QUE PENA IREMOS ENCERRAR O PROGRAMA...')
        