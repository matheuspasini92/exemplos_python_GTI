import math

raio = float(input("Digite o valor do raio da esfera: "))

area = 4 * math.pi * math.pow(raio,2)

print("A área da esfera é: ",area)

n = float(input("Digite um valor qualquer: "))
print("O valor de n^2 é ",math.pow(n,2),", n^3 é ",math.pow(n,3)," e n^4 é ",math.pow(n,4))

#valor positivo da bhaskara
a=2
b=3
c=4
(-b+math.sqrt(math.pow(b,2)-4*a*c))/(2*a)

#exemplo de sobreposição de valores

num = 5
num = 13
num = num +1
num = 3 + num * 2
num = num // 2
num = num +num % 14
print(math.sqrt(num))
