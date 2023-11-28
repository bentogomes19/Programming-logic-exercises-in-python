import math
numero1 = float(input('Digite um número: '))
numero2 = float(input('digite um segundo número: '))
print(' A) O primeiro número elevado ao segundo número')
print(' B) Raíz quadrada de cada um dos números')
print(' C) Raíz cúbica de cada um dos números')
opcao_usuario = str(input('Escolha uma opção: '))
if opcao_usuario in ['a','A','b','B','c','C']:
    if opcao_usuario in ['a','A']:
        pot = numero1 ** numero2
        print(pot)
    elif opcao_usuario in ['b','B']:
        raiz = math.sqrt(numero1)
        raiz2 = math.sqrt(numero2)
        print(raiz)
        print(raiz2)
    elif opcao_usuario in ['c','C']:
        raiz_cubica1 = numero1 ** (1/3)
        raiz_cubica2 = numero2 ** (1/3)
        print(raiz_cubica1)
        print(raiz_cubica2)
else:
    print('OPÇÃO INVÁLIDA...')
        
        