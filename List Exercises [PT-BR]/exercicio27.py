# a = 2, b = 3
a = int(input("Digite um número inteiro: "))
b = int(input('Digite um segundo número inteiro: '))
if a > b: 
    print(a)
if b > a:
     print(b)
if a == b:
    print('os números são iguais')

#MODO POO
class numeros:
    def __init__(self, a,b):
        self.numero1 = a
        self.numero2 = b
        
    def comparar(self):
        if self.numero1 > self.numero2:
            return self.numero1
        elif self.numero2 > self.numero2:
            return self.numero2
        else:
            return 'os números são iguais'
        
a = int(input('Digite um número inteiro: '))
b = int(input('Digite um segundo número inteiro: '))

object = numeros(a,b)
result = object.comparar()
print(result)
    
    