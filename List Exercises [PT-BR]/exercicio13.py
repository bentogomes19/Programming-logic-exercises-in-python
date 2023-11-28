#FAÇA UM PROGRAMA QUE RECEBA TRÊS NOTAS DE UM ALUNO, CALCULE E MOSTRE A MÉDIA ARITMÉTICA E A MENSAGEM
#CONSTANTE NA TABELA A SEGUIR. AOS ALUNOS QUE FICARAM PARA EXAME, CALCULE E MOSTRE A NOTA QUE DEVERÃO 
#TIRAR PARA SEREM APROVADOS, CONSIDERANDO QUE A MÉDIA EXIGIDA É 6.0
#MÉDIA ARITMÉTICA --> STATUS
#0.0 --> 3.0 --> "REPROVADO"
#3.0 --> 7.0 --> "EXAME"
#7.0 --> 10 --> "APROVADO"

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media_aritmetica = (nota1 + nota2 + nota3)/3
print(f"A média aritmética é de: {media_aritmetica}")
if media_aritmetica <= 3:
    print("REPROVADO")
else:
    if media_aritmetica <= 7:
        print("EXAME")
    else:
        if media_aritmetica <= 10:
            print("APROVADO")