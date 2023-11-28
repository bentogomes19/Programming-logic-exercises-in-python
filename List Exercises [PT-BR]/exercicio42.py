"""
 Faça um programa que receba: 
 o código do produto comprado; e
 a quantidade comprada do produto.
Calcule e mostre: 
 o preço unitário do produto comprado, seguindo a Tabela I; 
 o preço total da nota; 
 o valor do desconto, seguindo a Tabela II e aplicado sobre o preço total da nota; e
 o preço final da nota depois do desconto.
"""

codigo_produto = float(input('Digite o código do produto: '))
qtd_comprada = int(input('Digite a quantidade comprada: '))

if codigo_produto >=1 and codigo_produto <= 10:
    preco = 10
    print(f'R$ {preco}')
    
elif codigo_produto >= 11 and codigo_produto <=20:
    preco = 15
    print(f'R$ {preco}')
    
elif codigo_produto >= 21 and codigo_produto <= 30:
    preco = 20
    print(f'R$ {preco}')
    
elif codigo_produto >= 31 and codigo_produto <= 40:
    preco = 30
    print(f'R$ {preco}')
   
preco_total = preco * qtd_comprada
print(f'R$ {preco_total}')

if preco_total <= 250:
    desconto = preco_total * 0.05
    print(f'Desconto: R$ {desconto}')
elif preco_total > 250 and preco_total <= 500:
    desconto = preco_total * 0.1
    print(f'Desconto: R$ {desconto}')
elif preco_total > 500:
    desconto = preco_total * 0.15
    print(f'Desconto: R$ {desconto}')
    
preco_final = preco_total - desconto
print(f'Preço final: R$ {preco_final}')