salario_funcionario = float(input('Digite o seu salário (R$): '))
if salario_funcionario <= 300:
    aumento = salario_funcionario * 0.35
    reajuste = aumento + salario_funcionario
    print(reajuste)
elif salario_funcionario > 300:
    aumento = salario_funcionario * 0.15
    reajuste = aumento + salario_funcionario
    print(reajuste)
    
#MODO POO

class funcionario:
    def __init__(self, salario):
        self.salario = salario 
        self.aumento = 0
        self.reajuste = 0
        
    def calcular_salario(self):
        if self.salario <= 300:
            self.aumento = self.salario * 0.35
            self.reajuste = self.salario + self.aumento
        elif self.salario > 300:
            self.aumento = self.salario * 0.15
            self.reajuste = self.salario + self.aumento

salario = float(input('Digite o seu salário (R$): '))

objeto = funcionario(salario)
objeto.calcular_salario()
reajuste_salario = objeto.aumento
print(reajuste_salario)