#SABE-SE QUE, PARA ILUMINAR DE MANEIRA CORRETA OS CÔMODOS DE UMA CASA, PARA CADA METRO**2 DEVE-SE USAR 18w 
#DE POTÊNCIA. FAÇA UM PROGRAMA QUE RECEBA AS DUAS DIMENSÕES DE UM CÔMODO ( EM METROS), CALCULE E MOSTRE A
#SUA ÁREA (EM M**2) E A POTÊNCIA DE ILUMINAÇÃO QUE DEVERÁ SER UTILIZADA.

#variáveis = vlr_comodo1, vlr_comodo2, area, pot
vlr_comodo1 = float(input("Digite o lado do cômodo em metros: "))
vlr_comodo2 = float(input("Digite o segundo lado do cômodo em metros: "))
area = vlr_comodo1 * vlr_comodo2
pot = area * 18
print(f"o valor da área do cômodo: {area}m2; o valor da potência que deverá ser utilizada: {pot}w")