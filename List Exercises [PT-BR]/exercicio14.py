#FAÇA UM PROGRAMA QUE RECEBA DOIS NÚMEROS E MOSTRE O MAIOR

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um segundo número: "))
if num1 > num2:
    print(num1)
elif num2 > num1:
    print(f"O segundo número é maior {num2}")
elif num1 == num2:
    print("AMBOS SÃO IGUAIS")
    
    
    