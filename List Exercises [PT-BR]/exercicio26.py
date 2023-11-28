nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 3:
    print(media)
    print('Reprovado')
elif media >=3 and media < 7:
    print(media)
    print('Exame')
elif media >= 7:
    print(media)
    print('Aprovado')
    