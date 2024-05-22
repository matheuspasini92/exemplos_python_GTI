#Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de 
#idade, gênero(1-masculino e 2-feminino) e salário. Faça um programa que leia os dados necessários e informe
#a)a média de salários do grupo
#b)maior e menor idade do grupo
#c)quantidade de mulheres com salário até R$ 3.500,00
#Encerra a entrada de dados quando for digitada uma idade negativa


somaSalario = 0
pessoas = 0
maiorIdade = 0
menorIdade = 120
qtdMulheres = 0

while(True):
  print("Digite uma idade negativa para encerrar o programa")
  idade = int(input("Digite a idade da pessoa:"))
  if (idade<0):
      print("="*30)
      print("Fim do programa")
      print("="*30)
      break
  while(idade<=0 or idade>=120):
    print("> Idade inválida. Deve estar em um intervalo de 0 à 120.")
    idade = int(input(">> Digite novamente a idade da pessoa:"))
    
  genero = int(input("Digite 1 para Masculino ou 2 para feminino: "))
  while(genero!=1 and genero!=2):
    print("> Genero inválido.")
    genero = int(input(">> Digite novamente 1 para Masculino ou 2 para feminino: "))

  salario = float(input("Digite o salário dessa pessoa: R$ "))
  while(salario<0):
    print("> Salário inválido, deve ser um valor maior ou igual a zero.")
    salario = float(input(">> Digite novamente o salário dessa pessoa: R$ "))

  print("="*30)
  #(a)
  somaSalario = somaSalario + salario
  pessoas = pessoas + 1
  #(b)
  if(idade>maiorIdade):
    maiorIdade = idade
  #(c)
  if(idade<menorIdade):
    menorIdade = idade
  #(d)
  if(genero==2 and salario<=3500):
    qtdMulheres = qtdMulheres + 1

#a)a média de salários do grupo
if(pessoas==0):
  print("Dados não informados")
else:
  print(f"A média de salários do grupo é de R$ {somaSalario/pessoas}")
  #b)maior e menor idade do grupo
  print(f"A maior idade é de {maiorIdade} e a menor idade é de {menorIdade}")
  #c)quantidade de mulheres com salário até R$ 3.500,00
  print(f"A quantidade de mulheres que recebem um salário de até R$ 3.500,00 é de {qtdMulheres}")