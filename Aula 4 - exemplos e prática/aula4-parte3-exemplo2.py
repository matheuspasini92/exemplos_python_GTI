#numero de dias em um mês específico, sem considerar bissextos

mes = int(input("Digite o numero equivalente ao mês, ex.: 1-janeiro,2-fevereiro,...: "))

if(mes>12 ou mes<1):
  print("Número inválido")
elif (mes==2):
  print("O mês de fevereiro tem 28 dias")
elif(mes==4 or mes==6 or mes==9 or mes==11):
  print("O mês tem 30 dias")
else:
  print("O mês tem 31 dias")