import math

x = 10
b = 10
a = 1
c = 1
f = 1
g = 1
h = 3
j = 5
n = 3
p = 2
q = 15

resultado = math.sqrt(2*x)
print (resultado)

delta= math.sqrt(b**2-4*a*c)
print(delta)

funcao1 = math.pow(b,2*a+c)
print(funcao1)

outro_delta = math.sqrt(math.pow(b,2)-4*a*c)
print(outro_delta)

modulo1 = math.fabs(math.pow(f,3)-10)
print(modulo1)

modulo2 = math.fabs(g-2*h)
print(modulo2)

fatorial = math.factorial(j)
print(fatorial)

fatorial1 = math.factorial(n)/(math.factorial(n-p)* math.factorial(p))
print(fatorial1)

mdc = math.gcd(b,q)
print(mdc)

print(math.ceil(9.1))
print(math.ceil(9.8))
print(math.ceil(9.5))

print(math.trunc(9.1))
print(math.trunc(9.8))
print(math.trunc(9.5))

print(math.sin(1))
print(math.sin(90))
print(math.sin(180))

print(math.cos(1))
print(math.cos(90))
print(math.cos(180))

print(math.pi)
