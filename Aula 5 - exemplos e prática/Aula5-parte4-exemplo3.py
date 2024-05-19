#verifica se uma senha digitada é forte
#minimo 8 caracteres, pelo menos um dígito de 0-9 pelo menos um caractere de pontuação
import string

senha = input("Digite uma senha: ")

maiuscula = False
digito = False
pontuacao = False

if (len(senha)<8):
  print("Erro... senha muito curta")
else:
  for letra in senha:
    if (letra in string.ascii_uppercase):
      maiuscula = True
    if (letra in string.digits):
      digito = True
    if(letra in string.punctuation):
      pontuacao = True
    if (maiuscula == False or digito == False or pontuacao == False):
      if (maiuscula == False):
        print("Erro... senha não tem letra maiúscula.")
      if(digito == False):
        print("Erro... senha não tem digitos.")
      if(pontuacao == False):
        print("Erro... senha não tem caractere de pontuação.")
    else:
      print("Senha válida...")