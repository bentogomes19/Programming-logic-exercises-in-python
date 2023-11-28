#FAÇA UM PROGRAMA QUE RECEBA O VALOR DOS CATETOS DE UM TRIÂNGULO, CALCULE E MOSTRE O VALOR DA HIPOTENUSA

import math
cat1 = float(input("Digite o valor do cateto1: "))
cat2 = float(input("Digite o valor do cateto2: "))
hip = math.sqrt((cat1**2) + (cat2**2))
print(f"O valor da hipotenusa é: {hip}")