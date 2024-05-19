#passando diretamente por todos os caracteres de uma string

texto = input("Digite uma frase: ")

for caractere in texto:
  print(caractere)


#passando diretamente por todos os caracteres de uma string, usando o acesso por índice

texto = input("Digite uma frase: ")

for posicao in range(len(texto)):
  print(f"{posicao}: {texto[posicao]}")
