#determinar o total de dias em um mês e ano, consideranod bissexto

mes = int(input("Digite o numero equivalente ao mês, ex.: 1-janeiro,2-fevereiro,...: "))
ano = int(input("Digite o ano: "))

if (mes==2):
  if(ano%4==0 and ano%100!=0) or (ano%400==0):
    dia = 29
  else:
    dia = 28
elif(mes==4 or mes==6 or mes==9 or mes==11):
  dia = 30
else:
  dia = 31

print("Total de dias: ",dia)