#FAÇA UM PROGRAMA QUE RECEBA O RAIO, CALCULE E MOSTRE
# A) O COMPRIMENTO DE UMA ESFERA; SABE-SE QUE C = 2* Pi * R;
# B) A ÁREA DA ESFERA; SABE-SE QUE A = Pi * R**2;
# c) O VOLUME DE UMA ESFERA; SABE-SE QUE V = 3/4 * Pi * R**3;

import math
raio = float(input("Informe o valor do raio: "))
comp = 2 * math.pi * raio
print(f"O valor do comprimento da esfera é de: {comp}")
area = math.pi * raio ** 2
print(f"O valor da área da esfera é de: {area}")
volume = 3/4 * math.pi * raio ** 3
print(f"O valor do volume da esfera é de: {volume}")
