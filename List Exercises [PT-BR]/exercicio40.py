idade_nadador = int(input('Digite a sua idade: '))

if idade_nadador < 5:
    print('Sem categoria')
elif idade_nadador >= 5 and idade_nadador <= 7:
    print('Categoria - INFANTIL')
elif idade_nadador >= 8 and idade_nadador <= 10:
    print('Categoria - JUVENIL')
elif idade_nadador >= 11 and idade_nadador <= 15:
    print('Categoria - ADOLESCENTE')
elif idade_nadador >= 16 and idade_nadador <= 30:
    print('Categoria - ADULTO')
elif idade_nadador > 30:
    print('Categoria - SÊNIOR')