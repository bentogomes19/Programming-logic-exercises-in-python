nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
nota4 = float(input('Digite sua quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) /4
if media >= 7:
    print(f'media = {media:.2f} | APROVADO!')
else:
    print(f'media = {media:.2f} | REPROVADO!')