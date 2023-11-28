print('1 - Poupança')
print('2 - Fundos de Renda Fixa')
tipo_investimento = int(input("Digite o tipo de investimento: "))
vlr_investimento = float(input("Digite o valor do seu investimento (R$): "))
if tipo_investimento == 1:
    rend_mensal = (vlr_investimento * 0.03) + vlr_investimento
    print(f'O valor corrigido após um mês de investimento é de : R$ {rend_mensal:.0f}')
if tipo_investimento == 2:
    rend_mensal = (vlr_investimento * 0.04) + vlr_investimento
    print(f"O valor corrigido após um mês de investimento é de : R$ {rend_mensal:.0f}")
    
#MODO POO   
class investimento:
    def __init__(self, tipo_investimento):
        self.tipo_invest = tipo_investimento
        self.vlr_invest = 0
        self.rend_mensal = 0
        
    def calcular_rendimento(self, vlr_investimento):
        self.vlr_invest = vlr_investimento
        if self.tipo_invest == 1:
            self.rend_mensal = (self.vlr_invest * 0.03) + self.vlr_invest
        elif self.tipo_invest == 2:
            self.rend_mensal = (self.vlr_invest * 0.04) + self.vlr_invest

print('1 - Poupança')
print('2 - Fundo de Renda Fixa')
tipo_investimento = int(input(" Digite o tipo de investimento: "))
vlr_investimento = float(input("Digite o valor do seu investimento (R$): "))
objeto = investimento(tipo_investimento)
objeto.calcular_rendimento(vlr_investimento)
rend_mensal = objeto.rend_mensal
print(rend_mensal)



    
    