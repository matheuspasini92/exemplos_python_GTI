#foram entrevistados 50 estudantes de engenharia, de cada estudante foram
#coletados: idade, semestre e curso
#o programa deve ler (sortear) os dados dos estudades, calcular e escrever:
#media de idade dos estudantes
#curso do aluno mais velho
#quantidade de alunos que estão no 5º semestre

import random

somaIdade = 0
cursoMaisVelho = ""
idadeMaisVelho = 0
qtdAlunos5semestre = 0

for cont in range (50):
  #sorteio
  idade = random.randint(18,60)
  curso = random.choice(["Civil","Mecânica","Elétrica","Química","Produção"])
  semestre = random.randint(1,10)
  print(f"{idade} {curso} {semestre}")
  #coleta de estatísticas
  #média de idades: necessário somar as idades
  somaIdade += idade
  #curso do aluno mais velho
  if(idade>idadeMaisVelho):
    idadeMaisVelho = idade
    cursoMaisVelho = curso
  #total de alunos no 5º semestre
  if(semestre == 5):
    qtdAlunos5semestre += 1

mediaIdades = somaIdade//50
print(f"Média de idades: {mediaIdades}")
print(f"Curso do aluno mais velho ({idadeMaisVelho} anos): {cursoMaisVelho}")
print(f"Total de alunos no 5º semestre: {qtdAlunos5semestre}")