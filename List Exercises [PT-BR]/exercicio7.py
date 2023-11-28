#FAÇA UM PROGRAMA QUE RECEBA A QUANTIDADE DE DINHEIRO EM REAIS QUE UMA PESSOA QUE VAI VIAJAR POSSUI.
#ELA VAI PASSAR POR VÁRIOS PAÍSES E PRECISA CONVERTER SEU DINHEIRO EM DÓLARES, MARCO ALEMÃO E LIBRA ESTERLINA.
#SABE-SE QUE A COTAÇÃO DO DÓLAR É DE R$1,80, DO MARCO ALEMÃO É DE R$2,00 E DA LIBRA ESTERLINA É DE R$1,57.
#O PROGRAMA DEVE FAZER AS CONVERSÕES E MOSTRÁ-LAS

#variáveis = real, dolar, marco_alemao, libra
real = float(input("Digite a quantidade de dinheiro em reais (R$): "))
dolar = real * 1.80
marco_alemao = real * 2.00
libra = real * 1.57
print(f"A conversão da quantidade de moedas é de: dolar: US$ {dolar}; marco alemão: DE$ {marco_alemao} libras: £ {libra}")