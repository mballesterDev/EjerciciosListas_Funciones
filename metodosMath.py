import math
import random
#operaciones básicas

print(3+1)
print(3-1)
print(10/3) #dividir normal
print(10//3)#dividir pero solo nos da el entero(sin decimales)
print(10%3) #residuo
print(10*2)
print(2**3)#elevado a 


#metodos.math #los que llevan #math son los importados

print (round(1.5)) #redonde normal (si es 5 redondea arriba)
print(math.ceil(1.2)) #redondea siempre arriba
decimales = math.pow(2, 3) # obtiene el resultado con decimales
sinDecmales = int (decimales)
print(sinDecmales)

print (abs(-22)) #redonde al valor absoluto (es decir a positivo)  
print(math.sqrt(10))

numero_entero = random.randint(1, 10)#random.randint para generar números entre 1y 10 (sin decimales)
print(numero_entero)


numero_flotante = random.uniform(0.0, 1.0) #random pero con decimales
print(numero_flotante)