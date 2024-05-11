#ler um valor de 1 a 7 e printar o dia da semana correspondente

dia = int(input("Digite um número de 1 à 7: "))

if(dia>7 or dia<=0):
  print("Valor inválido")
else:
  if(dia==1):
    print("Segunda-feira")
  if(dia==2):
    print("Terça-feira")
  if(dia==3):
    print("Quarta-feira")
  if(dia==4):
    print("Quinta-feira")
  if(dia==5):
    print("Sexta-feira")
  if(dia==6):
    print("Sábado")
  if(dia==7):
    print("Domingo")