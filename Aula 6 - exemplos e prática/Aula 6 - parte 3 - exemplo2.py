#Implemente um programa que leia a idade, altura e gênero de 10 estudantes.
#Validar e criticar os dados de entrada
#O programa deve calcular e escrever:
#a)Média de idade dos estudantes
#b)Média de altura das meninas
#c)Percentual de estudantes com mais de 20 anos
#d)Altura do estudante mais velho

cont = 0
somaIdades = 0
somaAltura = 0
meninas = 0
mais20 = 0
maiorIdade = 0
maiorAltura = 0
continua = 1

while (continua == 1):
  print("Cont: ",cont)

  idade = int(input("Digite a idade: "))
  while(idade<=0 or idade>=120):
    print(">> Idade inválida... Deve estar no intervalo 0 à 120.")
    idade = int(input("Digite novamente a idade:"))
      
  altura = float(input("Digite a altura: "))
  while(altura<=0 or altura>=2.5):
    print(">> Altura inválida... Deve estar no intervalo 0 à 2.5m.")
    altura = float(input("Digite novamente a altura: "))
  
  genero = int(input("Digite '1' para feminino ou '2' para masculino: "))
  while(genero!= 1 and genero != 2):
    print(">> Gênero inválido... Deve ser 1 ou 2.")
    genero = int(input("Digite novamente '1' para feminino ou '2' para masculino: "))
  #(a)
  somaIdades = somaIdades + idade
  cont = cont + 1
  #(b)
  if(genero==1):
    somaAltura = somaAltura + altura
    meninas = meninas + 1 
  #(c)
  if(idade>20):
    mais20 = mais20 + 1
  #(d)
  if(idade>maiorIdade):
    maiorIdade = idade
    maiorAltura = altura

  continua = int(input("Deseja continuar a inclusão de informações? Digite '1' para sim ou '2' para encerrar: " ))
  if(continua!=1 and continua!=2):
    print("="*30)
    print("Verificação inválida. Programa encerrado.")
    break
  if(continua == 2):
    print("="*30)
    print("Programa encerrado!")
  
print("="*30)
print(f"Média das idades: {somaIdades/cont:.2f}")
if(meninas == 0):
  print("Não foram informados dados de meninas...")
else:
  print(f"Média de altura das meninas: {somaAltura/meninas:.2f}m")
print(f"Percentual de alunos com mais de 20 anos: {mais20*100/cont :.2f}%")
print(f"A altura do(a) mais velho(a) é {maiorAltura}m e a sua idade é de {maiorIdade}")