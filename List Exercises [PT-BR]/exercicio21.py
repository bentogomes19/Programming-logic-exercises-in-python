#Faça um programa que receba:
# o código do estado de origem da carga de um caminhão, supondo que a digitação do código do 
# estado seja sempre válida, isto é, um número inteiro entre 1 e 5; 
# o peso da carga do caminhão em toneladas; 
# o código da carga, supondo que a digitação do código seja sempre válida, isto é, um número inteiro 
# entre 10 e 40
# Tabelas:
#       CODIGO DO ESTADO            IMPOSTO         CÓDIGO DA CARGA         PREÇO POR QUILO
#               1                     35%               10 A 20                 R$ 35
#               2                     25%               21 A 30                 R$ 70
#               3                     15%               31 A 40                 R$ 150
#               4                      5%
#               5                    ISENTO
#
#
#
# Calcule e mostre:
#   ■■ o peso da carga do caminhão convertido em quilos; 
#   ■■ o preço da carga do caminhão; 
#   ■■ o valor do imposto, sabendo que o imposto é cobrado sobre o preço da carga do caminhão e depende do estado de origem; 
#   ■■ o valor total transportado pelo caminhão, preço da carga mais imposto.

#variáveis = cod_estado, peso_ton, cod_carga | peso_kg, preco_carga, imposto, vlr_total

cod_estado = int(input("Digite o código do estado: "))
peso_ton = float(input("Digite o peso da carga em ton: "))
cod_carga = int(input("Digite o código da carga: "))
peso_kg = peso_ton * 1000
#CODIGO DA CARGA
if cod_carga >= 10 and cod_carga <= 20:
    preco_carga = peso_kg * 100
    print(f"O preço da carga é de: R$ {preco_carga}")
elif cod_carga >= 21 and cod_carga <=30:
    preco_carga = peso_kg * 250
    print(f"O preço da carga é de: R$ {preco_carga}")
elif cod_carga >= 31 and cod_carga <= 40:
    preco_carga = peso_kg * 340
    print(f"O preço da carga é de: R$ {preco_carga}")
else:
    print("Codigo inválido")
    #CODIGO DO ESTADO 
if cod_estado ==1:
    imposto = preco_carga * 0.35 # IMPOSTO DE 35%
    vlr_total = imposto + preco_carga
    print(f'Imposto a pagar = R$ {imposto} | Preço total + impostos: R$ {vlr_total}')
elif cod_estado ==2:
    imposto = preco_carga * 0.25 # IMPOSTO DE 25%
    vlr_total = imposto + preco_carga
    print(f'Imposto a pagar = R$ {imposto} | Preço total + impostos: R$ {vlr_total}')
elif cod_estado ==3:
    imposto = preco_carga * 0.15 # IMPOSTO DE 15%
    vlr_total = imposto + preco_carga
    print(f'Imposto a pagar = R$ {imposto} | Preço total + impostos: R$ {vlr_total}')
elif cod_estado ==4:
    imposto = preco_carga * 0.05 # IMPOSTO DE 05%
    vlr_total = imposto + preco_carga
    print(f'Imposto a pagar = R$ {imposto} | Preço total + impostos: R$ {vlr_total}')
elif cod_estado ==5:
    imposto = 0 # ISENTO DE IMPOSTO
    vlr_total = imposto + preco_carga
    print(f'Imposto a pagar = R$ {imposto} | Preço total + impostos: R$ {vlr_total}')
else:
    print("Código inválido")
    
    
    
    
