# a = 3 b = 4 c = 6
class numeros:
    def __init__(self, a, b, c):
        self.numero1 = a
        self.numero2 = b
        self.numero3 = c
        
    def comparar(self):
        if self.numero1 > self.numero2 > self.numero3:
            return self.numero1
        elif self.numero1 > self.numero3:
            return self.numero1
        elif self.numero2 > self.numero1 > self.numero3:
            return self.numero2
        elif self.numero2 > self.numero3:
            return self.numero2
        elif self.numero3 > self.numero1:
            return self.numero3
        elif self.numero3 > self.numero2 > self.numero2:
            return self.numero3
        elif self.numero1 == self.numero2 == self.numero3:
            return 'todos os números informados são iguais'
    
a = float(input('Digite um número qualquer: '))
b = float(input('Digite um segundo número qualquer: '))
c = float(input('Digite um terceiro número qualquer: '))
        
object = numeros(a,b,c)
result = object.comparar()
print(result)  
      
        
        