class salario:
    def __init__(self, sal_funcionário, aumento):
        self.sal_funcionario = sal_funcionário
        self.aumento = aumento
    
    def calcular(self):
        if self.sal_funcionario < 500:
             self.aumento = self.sal_funcionario * 0.3
        else:
             self.aumento = 0
           
sal_funcionário = float(input('Digite o seu salário R$: '))
aumento = 0

objeto = salario(sal_funcionário, aumento)
objeto.calcular()
novo_salario = sal_funcionário + objeto.aumento
print(novo_salario)
