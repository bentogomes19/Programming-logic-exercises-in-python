#FAÇA UM PROGRAMA PARA RESOLVER EQUAÇÕES DO SEGUNDO GRAU
# DADOS:
# ax**2 + bx + c = 0
# a != 0
#   delta < 0 = raiz ñ existe
#   delta = 0 = existe raiz
#   x = (-b) / 2*a
#   delta > 0 == existem duas raizes reais
#   x1 = (-b + sqrt(delta)/(2*a)
#   x2 = (-b - sqrt(delta)/(2*a)

import math
print("EQUAÇÃO DO SEGUNDO GRAU CALCULADORA")
print("EXPRESSÃO ALGÉBRICA DA EQUAÇÃO DO SEGUNDO GRAU: ax2 + bx + c = 0")
a = float(input("Insira um valor para a: "))
b = float(input("Insira um valor para b: "))
c = float(input("Insira um valor para c: "))
if a == 0:
    print("O VALOR DE (A) DEVERÁ SER DIFERENTE DE ZERO")
else:
    delta = (b*b) - (4*a*c)
    if delta < 0:
        print("NÃO EXISTE RAIZ REAL, POIS O DELTA É MENOR QUE ZERO")
    elif delta == 0:
        x = (-b) / 2*a
        print(f"o reslutado é: {x}")
    elif delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(x1, x2)
        
