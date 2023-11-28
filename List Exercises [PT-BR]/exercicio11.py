#FAÇA UM PROGRAMA QUE MOSTRE O MENU DE OPÇÕES A SEGUIR, RECEBA A OPÇÃO DO USUÁRIO E OS DADOS NECESSÁRIOS
#PARA EXECUTAR CADA OPERAÇÃO
    #MENU DE OPÇÕES 1. SOMAR DOIS NÚMEROS 2. RAIZ QUADRADA DE UM NÚMERO
    #DIGITE A  OPÇÃO DESEJADA
import math
print("MENU BEM-VINDO")
print("1 - Somar dois números")
print("2 - Raiz quadrada de um número")
op = int(input("DIGITE A SUA OPÇÃO: "))
if op == 1:
    a = int(input("Digite um número: "))
    b = int(input("Digite um segundo número: "))
    c = a + b
    print(f"a soma entre os dois números é: {c}")
else:
    if op == 2:
        d = int(input("Digite um número inteiro: "))
        raiz = math.sqrt(d)
        print(f"A raíz quadrada do número informado é de: {raiz}")
