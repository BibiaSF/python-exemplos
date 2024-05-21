alunos = ['Sofi']
alunos.append('Noah')
while True:
    nome = input ('Digite o nome do aluno: ')
    alunos.append(nome)
    resposta = input('Deseja adicionar mais um aluno? (S/N)')
    if resposta.upper() == 'N'
    break
print(F"Alunos cadastrados:{alunos}")