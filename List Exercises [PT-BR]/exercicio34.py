#Faça um programa que receba o salário bruto de um funcionário e, usando a tabela a seguir, calcule e
#mostre o valor a receber. Sabe-se que este é composto pelo salário bruto acrescido de gratificação e
#descontado o imposto de 7% sobre o salário.

sal_bruto = float(input('Digite o seu salário bruto (R$): '))
if sal_bruto <= 350:
    grat = 100
    print(f'Você receberá uma gratificação de: R$ {grat}')
elif sal_bruto > 350 and sal_bruto < 600:
    grat = 75
    print(f'Você receberá uma gratificação de: R$ {grat}')
elif sal_bruto >= 600 and sal_bruto <= 900:
    grat = 50
    print(f'Você receberá uma gratificação de: R$ {grat}')
elif sal_bruto > 900:
    grat = 35
    print(f'Você receberá uma gratificação de: R$ {grat}')
    
 #MODO POO

class salario:
    def __init__(self, salario):
        self.salario = salario
        self.grat = 0
        
    def gratificacao(self):
        if self.salario <= 350:
            self.grat = 100
        elif self.salario > 350 and self.salario < 600:
            self.grat = 75
        elif self.salario >= 600 and self.salario <= 900:
            self.grat = 50
        elif self.salario > 900:
            self.grat = 35
            
               
sal_bruto = float(input('Digite o seu salário bruto (R$): '))
objeto = salario(sal_bruto)
objeto.gratificacao()
grat = objeto.grat
print(f'Você receberá uma gratificação de: R$ {grat}')

        