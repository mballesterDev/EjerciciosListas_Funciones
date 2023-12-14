

"""Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los
almacene en un array. El programa debe ser capaz de pasar todos los números pares a las
primeras posiciones del array (del 0 en adelante) y todos los números impares a las celdas
restantes. Utiliza arrays auxiliares si es necesario."""


import math
import random

""""
listaOriginal = []
listaPares = []
listaImpares = []
listaJunta = []
for i in range(20):
    numeroAleatorio = random.randint(1, 100)
    listaOriginal.append(numeroAleatorio)  #no se PUEDE usar la variable i como en java para asignar posciones ya que en py si no hay predeterminadamente un valor establecido
                                            #en la lista no lo puede sustituir y da error hay que usar append


for i in range (20):
    if listaOriginal[i] % 2 == 0:
        listaPares.append(listaOriginal[i])

listaPares.insert(0, "PARES =")
print(listaPares)

for i in range (20):
    if listaOriginal[i] % 2 != 0:
        listaImpares.append(listaOriginal[i])
listaImpares.insert(0, "IMPARES =")
print(listaImpares)  

listaJunta.extend(listaPares)
listaJunta.extend(listaImpares)
print(f"la lista de pares e impares ordenada y junta es \n{listaJunta}")  """

"""Un restaurante nos ha encargado una aplicación para colocar a los clientes en sus mesas. En
una mesa se pueden sentar de 0 (mesa vacía) a 4 comensales (mesa llena). Cuando llega un
cliente se le pregunta cuántos son. De momento el programa no está preparado para colocar a
grupos mayores a 4, por tanto, si un cliente dice por ejemplo que son un grupo de 6, el programa
dará el mensaje “Lo siento, no admitimos grupos de 6, haga grupos de 4 personas como
máximo e intente de nuevo”. Para el grupo que llega, se busca siempre la primera mesa libre
(con 0 personas). Si no quedan mesas libres, se busca donde haya un hueco para todo el grupo,
por ejemplo, si el grupo es de dos personas, se podrá colocar donde haya una o dos personas.
Inicialmente, las mesas se cargan con valores aleatorios entre 0 y 4. Cada vez que se sientan
nuevos clientes se debe mostrar el estado de las mesas. Los grupos no se pueden romper
aunque haya huecos sueltos suficientes. El funcionamiento del programa se ilustra a
continuación:"""

listaMesas = []
mesaDisponible = False

for i in range(10):  
    aleatorio = random.randint(0, 4) 
    listaMesas.append(aleatorio)

print(listaMesas)

while True:
    r1 = -1
    while r1 < 0 or r1 > 4:
        r1 = int(input("¿Cuántos son? "))
        if r1 < 0 or r1 > 4:
            print("Solo admitimos grupos de 0 a 4 personas.")

    mesaDisponible = False

    for i in range(10):
        if listaMesas[i] == 0:
            listaMesas[i] = r1
            print(f"Tenemos mesa libre para ustedes! en la posición {i + 1}")
            mesaDisponible = True
            break
        elif listaMesas[i] + r1 <= 4:
            listaMesas[i] = r1 + listaMesas[i]
            print(f"No tenemos mesa libre pero le podemos juntar con otros clientes en la posición {i + 1}")
            mesaDisponible = True
            break

    if not mesaDisponible:
        print("No tenemos mesas disponibles ahora")

    print(listaMesas)
