#verifica qual valor é maior - if simples

num1 = int(input("Digite o primeiro valor inteiro: "))
num2 = int(input("Digite o segundo valor inteiro: "))
num3 = int(input("Digite o terceiro valor inteiro: "))

maior = num1

if(num2>maior):
  maior=num2

if(num3>maior):
  maior=num3

print("O maior valor é: ",maior)

#ler a altura de uma pessoa, em em metros, e o gênero de nascimento
#1 pra mulher e 2 pra homem. Mostrar o peso ideal
#considerar: 
#para homem: 72.7*altura-58
#pra mulher: 62.1*altura-44.7

altura = float(input("Digite a altura da pessoa, em metros: "))
genero = int(input("Digite 1 se for mulher ou 2 se for homem: "))

if(genero!=1 and genero!=2):
  print("Genero inválido")

if(genero==1):
  peso = 62.1*altura-44.7
  print("Para mulher com altura",altura,",o peso ideal é: ",peso,"kgs")

if(genero==2):
  peso = 72.7*altura-58
  print("Para homem com altura",altura,",o peso ideal é: ",peso,"kgs")