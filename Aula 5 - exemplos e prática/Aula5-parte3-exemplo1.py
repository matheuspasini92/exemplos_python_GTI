#Acessando caracteres individuais em uma string:

texto = "Essa é uma string"

print(texto[0]) 
print(texto[5]) 
print(texto[-1]) 
print(texto[-6]) 


#xemplo de concatenação e repetição em strings

texto = "Esta"
print(texto+" é uma string")
print(texto*3)


#combinando os dois operadores

result = texto*4 + " é uma " + "String"*3
print(result)


#exemplo simples slicing

texto = "Essa é uma string"
print(texto[0:4])
print(texto[7:10])
print(texto[-6:]) 
print(texto[:6])
print(texto[0:10:2])
print(texto[::2])
print(texto[::-1]) <- string invertida


#alterando um elemento, mesmo a string sendo imutável

texto = "Essa é uma string"
texto = texto[:3]+"e"+texto[4:]
print(texto)


#comparando strings

texto1 = "texto"
texto2 = "outro texto"
if(texto1<texto2):
  print(f"'{texto1}' vem antes de '{texto2}'")
elif(texto2<texto1):
  print(f"'{texto2}' vem antes de '{texto1}'")
else:
  print(f"'{texto2}' é igual a '{texto1}'") 


#operador de pertencimento

texto1 = input("Digite uma frase: ")
texto2 = input("Digite uma plavra: ")

if texto2 in texto1:
  print(f"{texto2} está na frase")
else:
  print(f"{texto2} não está na frase...")


#comprimento de string

texto = input("Digite uma frase: ")

print(f"O comprimento da frase é {len(texto)} caracteres")