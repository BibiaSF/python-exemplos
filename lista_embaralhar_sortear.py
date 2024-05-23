import random
alunos=['João','Maria','Pedro','Ana','Lucas','Mariana']
print(f"Lista: {alunos}")
# Embaralhar a lista
random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")
# Escola um aluno aleatoriamente
aluno_sorteado = random.choice(alunos)
print(f"Alunos sorteado: {aluno_sorteado}")