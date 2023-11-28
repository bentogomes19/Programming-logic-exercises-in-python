#FAÇA UM PROGRAMA QUE RECEBA UMA TEMPERATURA EM CELSIUS, CALCULE E MOSTRE ESSA TEMPERATURA EM FAHRENHEIT.
#SABE-SE QUE F = 180*(C+32)/100 ; C/5 = F-32/9

temp_celsius = float(input("Digite a temperatura em celsius (°C): "))
fahrenheit = (160 + temp_celsius*9)/5
print(f"O valor da temperatura informada em fahrenheit (°F) é: {fahrenheit}")
#c * 9 = 5 * ( f-32 )
#c*9 = 5*f - 160
#c*9 /5 = f - 160
# (160 + c*9)/5 = f
#fahrenheit = (temp_celsius * 9/5) + 32