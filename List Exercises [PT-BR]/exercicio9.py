#A NOTA FINAL DE UM ESTUDANTE É CALCULADA A PARTIR DE TRÊS NOTAS ATRIBUÍDAS, RESPECTIVAMENTE, A UM TRABALHO
#DE LABORATÓRIO, A UMA AVALIAÇÃO SEMESTRAL E A UM EXAME FINAL. A MÉDIA DAS TRÊS NOTAS MENCIONADAS OBEDECE
#AOS PESOS A SEGUIR:
#TRABALHO DE LABORATÓRIO --> PESO = 2
#AVALIAÇÃO SEMESTRAL --> PESO 3
#EXAME FINAL --> PESO 5
#FAÇA UM PROGRAMA QUE RECEBA AS TRÊS NOTAS, CALCULE E MOSTRE A MÉDIA PONDERADA E O CONCEITO A SEGUIR
#MÉDIA PONDERADA = 8 E 10 --> CONCEITO A
#MÉDIA PONDERADA = 7 E 8 --> CONCEITO B
#MÉDIA PONDERADA = 6 E 7 --> CONCEITO C
#MÉDIA PONDERADA = 5 E 6 --> CONCEITO D
#MÉDIA PONDERADA = 0 E 5 --> CONCEITO E

#variáveis = lab, av_semestral, examefinal, media_ponderada
lab = float(input("Digite a nota do trabalho do laboratório: "))
av_semestral = float(input("Digite a nota da avaliação semestral: "))
examefinal = float(input("Digite a nota do exame final: "))

media_ponderada = ((lab * 2) + (av_semestral * 3) + (examefinal * 5)) / 10

print(f"A média ponderada final é: {media_ponderada}")
#ESTRUTURA CONDICIONAL SIMPLES
if media_ponderada >= 8 and media_ponderada <= 10: # (V) E (F) = (F); (V) E (V) = (V)
    print("CONCEITO A")
if media_ponderada >= 7 and media_ponderada <= 8:  
    print("CONCEITO B")
if media_ponderada >=6 and media_ponderada <=7: 
    print("CONCEITO C")
if media_ponderada >=5 and media_ponderada <=6: 
    print("CONCEITO D")
if media_ponderada >=0 and media_ponderada <=5: 
    print("CONCEITO E")
    

lab = float(input("Digite a nota do trabalho do laboratório: "))
av_semestral = float(input("Digite a nota da avaliação semestral: "))
examefinal = float(input("Digite a nota do exame final: "))
print(f"A média ponderada final é: {media_ponderada}")
#ESTRUTURA CONDICIONAL COMPOSTA
if media_ponderada >= 8:
    print("CONCEITO A")
else:
    if media_ponderada >=7:
        print("CONCEITO B")
    else:
        if media_ponderada >=6:
            print("CONCEITO C")
        else:
            if media_ponderada >=5:
                print("CONCEITO D")
            else:
                print("CONCEITO E")