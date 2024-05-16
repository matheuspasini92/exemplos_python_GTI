#calcular a data da páscoa no intervalo de anos de 1900 e 2099

ano = int(input("Digite o ano: "))

if(ano>2099 or ano<1900):
  print("Impossível calcular")
else:
  a = ano%19
  b = ano%4
  c = ano%7
  d = (19*a+24)%30
  e = (2*b+4*c+6*d+5)%7
  dia = 22+d+e
  if(ano== 1954 or ano==1981 or ano==2049 or ano==2076):
    dia = dia-7
    if(dia>31):
      dia = dia - 31
      print("Data da páscoa é: ",dia," de abril")
    else:
      print("Data da páscoa é: ",dia," de março")