
#Las listas son los arrays de java, estos son dinámicos y ueden almacenar todo tipo de datos juntos
listaPrueba = [7, "Hola que tal", True, 2.2, "Ultimo"]

print (listaPrueba[2])
print(listaPrueba[2:])
print(f"La posición 1 es {listaPrueba[1]}")
longitud = len(listaPrueba)
print(longitud)

#RECORRER LISTA
print()
for indices in listaPrueba: #usanso el foreach sencillamente
    print(indices)

#INDEXACIÓN
print (listaPrueba[2])
print(listaPrueba[1:3]) #nos da la 1 y la 2 el utlimos iempre es -1
print()
# o alrevés para obtener los últimos valores
print (listaPrueba[-1])

#COMPROBAR SI UN ELEMENTO ESTÁ EN LA LISTA

numeros = [2, 7, 9, 22, 10,78, 2, 399]

for i in numeros: #con este método recorremos el array y buscamos el numero deseado
    if i == 9:
        print("el número 9 se encuentra en la lista")
    

if 9 in numeros: #este es el metodo mas sencillo
    print(f"9 se encuentra dentro de nuestra lista")


#CON STRINGS ES IGUAL

palabras = ["Esto", "es", "una", "prueba"]    

palabraBuscar = "papaya"
palabra2 = "es"

if palabraBuscar in palabras or palabra2 in palabras:
    print(f"{palabraBuscar} y {palabra2} se encuentra en la lista")
else:
    print(f"{palabraBuscar} y {palabra2} no se encuentra en la lista")

#una forma eficiente de saber si está en lista o no es 

if "Esto" in palabras:
    print("Se encunetra en la lista")

if "EstoO" not in palabras:
     print("No se encunetra en la lista")
    
#REEMPLAZAR ELEMENTOS DE UNA LISTA

lenguajes = ["C", "Java", "Kotlin", "Java Script"]   

lenguajes[1] = "TurboPascal"
print(lenguajes)

lenguajes[0] = f"{lenguajes[0]}++"
print(lenguajes)

#esto lo he hecho yo al estilo java para mejorar mi lógica

lenguajes = ["C", "Java", "Kotlin", "Java Script"]   
    


for i in range (0, len(lenguajes)):
   
   lenguajes[i] = input("Introduce el lenguaje que más te guste")
  


print (lenguajes)

#Forma más sencilla de cambiar 
lenguajes = ["C", "Java", "Kotlin", "Java Script"]   

lenguajes[0:] = ["Java", "JavaScript", "Kotlin", "TurboPascal", "Angular"]
print(lenguajes)

lenguajes2 = ["Java", "JavaScript", "Py"]
lenguajes2 [1:2] = ["C++", "Turbo", "Angular"] #asi remmplazo java script  por tres elementos que se meten en el medio de la lista

print(lenguajes2)

lenguajes2 = ["Java", "JavaScript", "Py"]
lenguajes2 [1:2] = ["C++", "Turbo", "Angular"]


#MÉTODOS



# unir dos arrays (listas) .extend
frutas = ["pera", "manzana", "melon", "kiwi"]
frutas2 = ["melocoton", "sandia"]

# asi modificamos frutas 
frutas.extend(frutas2) #asi se modifica un array 
print (frutas)

frutasmix = frutas
print (frutasmix) #asi se crea uno nuevo diferente


#.insert
#con este método insertamos valores en la posicion que queramos, moviendo a la derecha todos los elementos

frutas3 = ["pera", "manzana", "melon", "kiwi"]

frutas3.insert(0, "papaya")
print(frutas3)

#append
#inserta al final de la lista un elemento

frutas4= ["pera", "manzana", "melon", "kiwi"]

frutas4.append("moras")
print (frutas4)

#.pop para eliminar elementos

frutas5= ["pera", "manzana", "melon", "kiwi"]

frutas5.pop() #por defecto elimina la ultima posicion del array
print(frutas5)

elementoEliminado = frutas5.pop(1) #eliminamos la posicon que queramos
print(frutas5)

#ademas de eleminarlo lo retorna y nos lo guarda 
print (elementoEliminado)

#SUMAR LOS ELEMENTOS DE UNA LISTA SUMA()

numerosRandom = [2,5,7,8]
print(sum(numerosRandom))

#ORDENAR UNA LISTA SORTED()

numeros =[ 33,22,1000,1,5]
print(sorted(numeros))