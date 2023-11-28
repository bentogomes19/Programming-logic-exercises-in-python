alunos = []
médias_finais = []
recuperação = []

cont = 0
while (cont < 5):
    nome = str(input("Digite seu nome: "))
    
    nota1 = float(input("Digite sua nota1: "))
    nota2 = float(input("Digite sua nota2: "))
    
    média = (nota1 + nota2 ) / 2
    print(f"A média final de {nome} é de {média}")

    alunos.append(nome) #Adiciona o nome à lista de alunos
    médias_finais.append(média) # Adiciona a média final à lista de médias
    
    if média < 6:
        print(f"{nome} você está de recuperação")
        recuperação.append(média)
    
    cont = cont + 1
    
print("\n Lista de Alunos e Médias Finais:")    
for i in range(len(alunos)):
    print(f"{alunos[i]}: {médias_finais[i]}")

print("\n Lista de Alunos de Recuperação:")
for aluno_rec in recuperação:
    print(aluno_rec)