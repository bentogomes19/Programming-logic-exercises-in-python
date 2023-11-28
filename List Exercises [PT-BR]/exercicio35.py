#Faça um programa que receba o preço de um produto, calcule e mostre, de acordo com as
# tabelas a seguir, o novo preço e a classificação.

preco_produto = float(input('Digite o preço do produto (R$): '))
#PERCENTUAL DE AUMENTO
if preco_produto < 50:
    novo_preco = (preco_produto * 0.05) + preco_produto
    print(f'O novo preço do produto com o aumento é de: R$ {novo_preco:.2f}')
elif preco_produto >= 50 and preco_produto <= 100:
    novo_preco = (preco_produto * 0.1) + preco_produto 
    print(f'O novo preço do produto com o aumento é de: R$ {novo_preco:.2f}')
elif preco_produto > 100:
    novo_preco = (preco_produto * 0.15) + preco_produto
    print(f'O novo preço do produto com o aumento é de: R$ {novo_preco:.2f}')
# CLASSIFICAÇÕES
if preco_produto < 80: 
    print('CLASSIFICAÇÃO: BARATO')
elif preco_produto >= 80 and preco_produto < 120:
    print('CLASSIFICAÇÃO: NORMAL')
elif preco_produto >= 120 and preco_produto <= 200:
    print('CLASSIFICAÇÃO: CARO')
elif preco_produto > 200:
    print('CLASSIFICAÇÃO MUITO CARO')