#ejercicio 1 Crea un programa que calcule la media de los alumnos de las clases de un colegio


def puntuacionMedia(alumnos):
    suma = sum(alumnos)
    media = suma / len(alumnos)
    return media

clase1 = []
clase2 = []
clase3 = []

r1 = int(input("¿Cuantos alumnos hay en la clase 1? "))

for i in range(r1):
    notaAlumno = -1
    while notaAlumno < 0 or notaAlumno > 10:
        notaAlumno = int(input(f"Escribe la nota media del alumno {i+1} (debe estar entre 0 y 10)"))
    clase1.append(notaAlumno)

notaMedia1 = puntuacionMedia(clase1)
print(notaMedia1)  

r2 = int(input("¿Cuantos alumnos hay en la clase 2? "))

for i in range (r2):
    notaAlumno = -1
    while notaAlumno < 0 or notaAlumno > 10:
        notaAlumno = int(input(f"Escribe la nota media del alumno {i+1} (debe estar entre 0 y 10)"))
    clase2.append(notaAlumno)

notaMedia2 = puntuacionMedia(clase2) 
print(notaMedia2)

r3 = int(input("¿Cuantos alumno hay en la clase 3? "))

for i in range (r3):
    notaAlumno = -1
    while notaAlumno < 0 or notaAlumno > 10:
        notaAlumno = int(input(f"Escribe la nota media del alumno {i+1} (debe estar entre 0 y 10)"))
    clase3.append(notaAlumno)

notaMedia3 = puntuacionMedia(clase3)
print(notaMedia3)


#crea un programa que creee y ordena listas

def OrdenarLista(lista):
    listaOrdenada = sorted(lista)
    return listaOrdenada


lista1 = []

r1 = int(input("Cuantos elementos quieres que tenga la lista?"))

for i in range (r1):
    r2 = int(input(f"Introduce el número{i+1}"))
    lista1.append(r2)


print(OrdenarLista(lista1))


#crea una funcion para hacer un cuadrado

def HacerCuadrado(alto, ancho):
    for filas in range (alto):
        for columnas in range (ancho):
            print ("*", end= " ")
        print()


r1 = int(input("Introduce el alto: "))
r2 = int(input("Introduce el ancho: "))
print(HacerCuadrado(r1, r2))


#CREA UN TRIANGULO CON UNA FUNCION
def triangulo (altura):
    i =altura
    columnasI =0
    columnasFinal =1
    cantidad = "*"
    for filas in range (altura):
        for columnas in range(columnasI, columnasFinal):
            print ("* ", end="")
            
        print()
        i= i-1
        columnas= columnas +1
        columnasFinal = columnasFinal+1
    i = altura
    for filas in range (altura):
        for columnas in range (i-1,0,-1):
            print ("* ", end="")
            
        print()
        i= i -1
   
   

r1 = int(input("introduce la altura del triangulo")) 


#CREADOR DE LISTAS

def CrearLista(cantidadLista):
    listaNombres = []
    for i in range (cantidadLista):
        r1 = input(f"Introduce un nombre {i+1}")
        listaNombres.append(r1)

    return print(listaNombres)   


CrearLista (4)