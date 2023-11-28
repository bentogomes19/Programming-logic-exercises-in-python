#FAÇA UM PROGRAMA QUE DETERMINE A DATA CRONOLOGICAMENTE MAIOR ENTRE DUAS DATAS FORNECIDAS PELO USUÁRIO
# CADA DATA DEVE SER COMPOSTA POR TRÊS VALORES INTEIROS, EM QUE O PRIMEIRO REPRESENTA O DIA, O SEGUNDO, O MÊS
# E O TERCEIRO, O ANO.

#variáveis = dia1, mes1, ano1, dia2, mes2, ano2
print("Digite a primeira data")
dia1 = int(input("Digite o dia (dd): "))
mes1 = int(input("Digite o mês (mm): "))
ano1 = int(input("Digite o ano (aaaa): "))

print("Digite a segunda data")
dia2 = int(input("Digite o dia (aa): "))
mes2 = int(input("Digite o mês (mm): "))
ano2 = int(input("Digite o ano (aaaa): "))
if ano1 > ano2:
    print(f"A maior data é: {dia1}-{mes1}-{ano1}")
else:
     if ano2 > ano1:
         print(f"A maior data é: {dia2}-{mes2}-{ano2}")
     else:
         if mes1 > mes2:
             print(f"A maior data é: {dia1}-{mes1}-{ano1}")
         else:
             if mes2 > mes1:
                 print(f"A maior data é: {dia2}-{mes2}-{ano2}")
             else:
                 if dia1 > dia2:
                     print(f"A maior data é: {dia1}-{mes1}-{ano1}")
                 else:
                     if dia2 > dia1:
                         print(f"A maior data é: {dia2}-{mes2}-{ano2}")
                     else:
                         print("AS DATAS SÃO IGUAIS")
                    

         
        
