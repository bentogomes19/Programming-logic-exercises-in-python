#FAÇA UM PROGRAMA QUE RECEBA QUATRO VALORES: I, A, B E C. DESSES VALORES, I É INTEIRO E POSITIVO
#, A, B E C SÃO REAIS. ESCREVA OS NÚMEROS A,B E C OBEDECENDO A TABELA A SEGUIR:
# VALOR DE I ----> FORMA A ESCREVER
#     1 --------> A, B E C EM ORDEM CRESCENTE 
#     2 --------> A, B E C EM ORDEM DECRESCENTE
#     3 --------> O MAIOR FICA ENTRE OS OUTROS NÚEMROS
# a = 1, b = 2, c = 3
a = int(input("Digite um número inteiro positivo para A: "))
b = float(input("Digite um valor real para B: "))
c = float(input("Digite um valor real para C: "))
i = int(input("Digite um valor para I (1, 2 e 3): "))
if i==1:
    if a<b and b<c and a<c:
        print(f"A ordem crescente dos números são: {a} / {b} / {c}")
    else:
        if a<c and a<b and b>c:
            print(f"A ordem crescente dos números são: {a} / {c} / {b}")
        else:
            if a>b and a<c and c>b:
                print(f"A ordem crescente dos números são: {b} / {a} / {c}")
            else:
                if a>b and a>c and c>b:
                    print(f"A ordem crescente dos números são: {b} / {c} / {a}")
                else:
                    if a<b and a>c and c<b:
                        print(f"A ordem crescente dos números são: {c} / {a} / {b}")
                    else:
                        if a>b and a>c and c<b:
                            print(f"A ordem crescente dos números são: {c} / {b} / {a}")


                