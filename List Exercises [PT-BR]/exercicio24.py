preco = float(input('Digite o preço do produto (R$): '))
tipo = str(input('Digite o tipo do produto A - Alimentação | L - Limpeza | V - Vestuário |: '))
refrigeracao = str(input('O produto necessita de refrigreação S/N?: '))
#VALOR ADICIONAL 
if refrigeracao in ['n','N']:
    if tipo in ['A','a','l','L','V','v']:
        if tipo in ['A','a'] and preco < 15:
            valor_add = 2
            print(f'Valor adicional de R$ {valor_add}')
        elif tipo in ['A','a'] and preco >= 15:
            valor_add = 5
            print(f'Valor adicional de R$ {valor_add}')
        elif tipo in ['l','L'] and preco < 10:
            valor_add = 1.50
            print(f'Valor adicional de R$ {valor_add}')
        elif tipo in ['l','L'] and preco >= 10:
            valor_add = 2.50
            print(f'Valor adicional de R$ {valor_add}')
        elif tipo in ['V','v'] and preco < 30:
            valor_add = 3.00
            print(f'Valor adicional de R$ {valor_add}')
        elif tipo in ['V','v'] and preco >= 30:
            valor_add = 2.50
            print(f'Valor adicional de R$ {valor_add}')
elif refrigeracao in ['S', 's']:
    if tipo in ['A','a']:
        valor_add = 8.00
        print(f'Valor adicional de R$ {valor_add}')
    elif tipo in ['l','L','V','v']:
        valor_add = 0
        print(f'Valor adicional de R$ {valor_add}')
#IMPOSTO
if preco < 25:
    imposto = preco * 0.05
    print(f'Valor do imposto | R$ {imposto:.2f}')
else:
    imposto = preco * 0.08
    print(f'Valor do imposto | R$ {imposto:.2f}')
#PREÇO DO CUSTO
preco_custo = preco + imposto
#DESCONTO
if tipo in ['A','a'] and refrigeracao in ['S', 's']:
    desconto = 0
    print(f'Não haverá desconto | seu produto é alimentação e tem refrigeração')
else:
    desconto =  preco_custo * 0.03
    print(f'O desconto será de: R$ {desconto:.3f}')
#NOVO PREÇO
novo_preco = preco_custo + valor_add - desconto
if novo_preco <= 50:
    print(f'Novo preço de R$ {novo_preco:.2f} | CLASSIFICAÇÃO --> BARATO')
elif novo_preco > 50 and novo_preco < 100: 
    print(f'Novo preço de R$ {novo_preco:.2f} | CLASSIFICAÇÃO --> NORMAL')
elif novo_preco >= 100:
    print(f'Novo preço de R$ {novo_preco:.2f} | CLASSIFICAÇÃO --> CARO')   
    
        
        

        
                    
        
