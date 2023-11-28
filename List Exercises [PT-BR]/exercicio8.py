#FAÇA UM PROGRAMA QUE RECEBA UMA HORA (UMA VARIÁVEL PARA HORAS E OUTRA PARA MINUTOS), CALCULE E MOSTRE:
# A) A HORA DIGITADA CONVERTIDA EM MINUTOS;
# B) O TOTAL DE MINUTOS, OU SEJA, OS MINUTOS DIGITADOS MAIS A CONVERSÃO ANTERIOR;
# C) O TOTAL DE MINUTOS CONVERTIDOS EM SEGUNDOS;

horas = float(input("Digite um tempo qualquer em horas: "))
min = float(input("Digite um tempo qualquer em minutos: "))
convert_min = horas * 60
total_min = min + convert_min
total_minsec = total_min * 60
print(f"A hora digitada convertida em minutos: {convert_min}")
print(f"Os minutos digitados mais a conversão anterior: {total_min}")
print(f"O total de minutos convertidos em segundos: {total_minsec}")

