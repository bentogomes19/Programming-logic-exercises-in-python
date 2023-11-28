#FAÇA UM PROGRAMA QUE MOSTRE A DATA E A HORA DO SISTEMA NOS SEGUINTES FORMATOS: DD/MM/AAAA - MÊS POR EXTENSO
## E HORA:MINUTO.

from datetime import datetime #IMPORTANDO MODULO DE TEMPO 
data_atual = datetime.now() #ATRIBUIR A DATA ATUAL COM O HORÁRIO DO COMPUTADOR
day = data_atual.day # EXTRAINDO SOMENTE O DIA DO DATETIME.NOW
month = data_atual.month # EXTRAINDO SOMENTE O MÊS DO DATETIME.NOW
year = data_atual.year # EXTRAINDO SOMENTE O ANO DO DATETIME.NOW
print(f"Data atual: {day}/{month}/{year}") 
if month == 1:
    print("JANEIRO")
if month == 2:
    print("FEVEREIRO")
if month == 3:
    print("MARÇO")
if month == 4:
    print("ABRIL")
if month == 5:
    print("MAIO")
if month == 6:
    print("JUNHO")
if month == 7:
    print("JULHO")
if month == 8:
    print("AGOSTO")   
if month == 9:
    print("SETEMBRO")
if month == 10:
    print("OUTUBRO")
if month == 11: 
    print("NOVEMBRO")
if month == 12:
    print("DEZEMBRO")

hora_atual = datetime.now()
hora = hora_atual.hour
min = hora_atual.minute
print(f"Hora atual: {hora}:{min}")