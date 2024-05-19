#foram entrevistados 2000 habitantes de um planeta. De cada habitante,
#foram coletados os seguintes dados: idade, renda, gênero e nº de filhos
#O programa deve obter os dados desses habitantes, calcular e escrever:
#media de renda
#media de idade de quem tem mais de 3 filhos
#quantidades de homens com menos de 30 anos
#media do número de filhos
#renda do homem mais velho
#idade da mulher com maior renda

import random

somaRendas = 0
somaIdades = 0
qtdMais3Filhos = 0
qtdHomensMenor30 = 0
somaFilhos = 0
rendaHomemMaisVelho = 0
idadeHomemMaisVelho = 0
idadeMulherMaiorRenda = 0
mulherMaiorRenda = 0

totalHab = 2000
for cont in range(2000):
  idade = random.randint(18,80)
  renda = random.randint(1200,12000)
  genero = random.choice(["Masculino","Feminino"])
  filhos = random.randint(0,5)

  somaRendas += renda

  if(filhos>3):
    somaIdades += idade
    qtdMais3Filhos += 1
  
  if(genero == "Masculino" and idade < 30):
    qtdHomensMenor30 += 1

  somaFilhos += filhos

  if(genero == "Masculino" and idade > idadeHomemMaisVelho):
    idadeHomemMaisVelho = idade
    rendaHomemMaisVelho = renda

  if(genero == "Feminino" and renda > mulherMaiorRenda):
    mulherMaiorRenda = renda
    idadeMulherMaiorRenda = idade

mediaRenda = somaRendas / totalHab
mediaMais3Filhos = somaIdades // qtdMais3Filhos
mediaFilhos = somaFilhos // totalHab
print(f"Média de renda da população: {mediaRenda:.2f}")
print(f"Média de idade com mais de 3 filhos: {mediaMais3Filhos}")
print(f"Total de homens com menos de 30 anos: {qtdHomensMenor30}")
print(f"Média do nº de filhos: {mediaFilhos}")
print(f"Renda do homem mais velho: {rendaHomemMaisVelho:.2f}")
print(f"Idade da mulher com maior renda: {idadeMulherMaiorRenda}")