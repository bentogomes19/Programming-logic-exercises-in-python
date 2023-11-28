#O preço ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor
# e dos impostos, ambos aplicados ao custo de fábrica. As porcentagens encontram-se na tabela a
#seguir. Faça um programa que receba o custo de fábrica de um carro e mostre o preço ao consumidor.

custo_fabrica_carro = float(input('Digite o valor do custo de fábrica do carro (R$): '))
if custo_fabrica_carro < 12000:
    preco_final = (custo_fabrica_carro * 0.05) + (custo_fabrica_carro * 0) + custo_fabrica_carro
    print(f'R$ {preco_final}')
elif custo_fabrica_carro >= 12000 and custo_fabrica_carro <= 25000:
    preco_final = (custo_fabrica_carro * 0.10) + (custo_fabrica_carro * 0.15) + custo_fabrica_carro
    print(f'R$ {preco_final}')
elif custo_fabrica_carro > 25000:
    preco_final = (custo_fabrica_carro * 0.15) + (custo_fabrica_carro * 0.20) + custo_fabrica_carro
    print(f'R$ {preco_final}')
    
#MODO POO

class consumidor:
    def __init__(self, custo):
        self.custo = custo
        self.preco_final = 0
        
    def calcular(self):
        if self.custo < 12000:
            self.preco_final = (self.custo * 0.05) + (self.custo * 0) + self.custo
        elif self.custo >= 12000 and self.custo <= 25000:
            self.preco_final = (self.custo * 0.10) + (self.custo * 0.15) + self.custo
        elif self.custo > 25000:
            self.preco_final = (self.custo * 0.15) + (self.custo * 0.20) + self.custo

custo = float(input('Digite o valor do custo de fábrica do carro (R$): '))
objeto = consumidor(custo)
objeto.calcular()
preco_final = objeto.preco_final
print(f'R$ {preco_final:.2f}')

