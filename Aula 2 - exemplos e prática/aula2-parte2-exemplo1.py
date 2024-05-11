import math

print("Digite o raio 1, em inteiro, de uma esfera: ")
raio = int(input())
volume = (4*3.14*raio**3)//3
print("O volume da esfera é: ", volume)

print("Digite o raio 2 de uma esfera: ")
r = float(input())
volume = 4/3 * math.pi * math.pow(r,3)
print("O volume da esfera é: ", volume)

raio3 = float(input("Digite o valor do raio 3 de uma esfera: "))
volume = 4/3 * math.pi * math.pow(raio3,3)
print("O volue da esfera é de: ",volume)
