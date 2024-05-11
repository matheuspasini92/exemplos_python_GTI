import math
#conversão de graus fahrenheit para celsius

far = float(input("Digite uma temperatura, em Fahrenheit: "))

c = (5/9)*(far-32)

print("A temperatura ",far," em graus Celsius é: ",c)

#ler dois valores inteiros e escreve soma, diferença, média, a distância (valor absoluto da diferença)
#o maior dos dois e o menor dos dois

a = int(input("Digite um primeiro valor inteiro: "))
b = int(input("Digite um segundo valor inteiro: "))

soma = a+b
subt = a-b
media = (a+b)/2
dist = math.fabs(a-b)
maior = (a+b+math.fabs(a-b))/2
menor = (a+b-math.fabs(a-b))/2

print("A soma dos valor é: ",soma)
print("A subtração dos valores é: ",subt)
print("A média dos valores é: ",media)
print("A variação entre os valores é: ",dist)
print("O maior valor é: ",maior)
print("O menor valor é: ",menor)

#lê o tempo em segundos e decompõe em hora, minuto e segundo

tempo = int(input("Digite um tempo em segundos: "))

hora = tempo//3600
restoHora = tempo%3600
minuto = restoHora//59
segundo = restoHora%59 

print("O tempo ",tempo,", em segundos, tem: ",hora,"h",minuto,"min",segundo,"segundos")

#le um valor e devolve invertido

numero = int(input("Digite um valor inteiro de 4 dígitos: "))

num1 = numero//1000
resto1 = numero%1000
num2 = resto1//100
resto2 = resto1%100
num3 = resto2//10
num4 = resto2%10

print("O valor ",numero," invertido é: ",num4,num3,num2,num1)