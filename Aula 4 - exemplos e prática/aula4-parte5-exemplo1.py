#verifica se ano é bissexto (divisível por 4, não divisível por 100, a menos que seja por 400)

ano = int(input("Digite o ano: "))

if(ano%4==0 and ano%100!=0) or (ano%400==0):
  print("É bissexto")
else:
  print("Não é bissexto")