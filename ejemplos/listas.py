
numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprime el contenido de la lista original

numeros[0] = 111 
print("Nuevo contenido de la lista:", numeros) # contenido de la lista actual.

print("--------------------------------------")
numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo contenido de la lista original.

numeros[0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior.

numeros[1] = numeros[4]  # copiando el valor del quinto elemento al segundo
print("Nuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual.

print("--------------------------------------")
numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo el contenido de la lista original

numeros [0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior

numeros [1] = numeros [4] # copiando el valor del quinto elemento al segundo
print("Contenido de la lista anterior:", numeros) # imprimiendo contenido de la lista anterior

print("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista

print("--------------------------------------")
numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo contenido de la lista original

numeros[0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior

numeros[1] = numeros[4] # copiando el valor del quinto elemento al segundo
print("Contenido de la lista anterior:", numeros) # imprimiendo contenido de la lista anterior

print ("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista anterior

###

del numeros[1] # eliminando el segundo elemento de la lista
print("Longitud de la nueva lista:", len(numeros)) # imprimiendo nueva longitud de la lista
print("\nNuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual

print("--------------------------------------")
numeros = [111, 7, 2, 1]
print(len(numeros))
print(numeros)
###
numeros.append(4)
print(len(numeros))
print(numeros)
###
numeros.insert(0,222)
print(len(numeros))
print(numeros)
###
numeros.insert(1,333)
print(len(numeros))
print(numeros)

#Agregar elementos a una lista 
print("append")
miLista = [] # creando una lista vacía
for i in range (5):
    miLista.append (i + 1)
print(miLista)
print("insert")
miLista = [] # creando una lista vacía

for i in range(5):
    miLista.insert(0, i + 1)
print(miLista)

print("\nEjercicio #1 suma a través de una lista")
miLista = [10, 1, 8, 3, 5]
suma = 0
for i in range(len(miLista)):
    suma += miLista[i]
print(suma)

print("\nEjercicio #2 suma a través de una lista")
miLista = [10, 1, 8, 3, 5]
suma = 0
for i in miLista:
    suma += i
print(suma)

print("\nEjercicio #3: Ordenar lista adyacentemente")
miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while
while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]
print(miLista)

print("ó")
miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?:"))

for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)

while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]
            
print("Ordenado:")
print(miLista)

print("\nEjercicio #4: Propiedad sort para ordenar la lista")
miLista = [8, 10, 6, 2, 4]
miLista.sort() 
print(miLista) 

print("\nEjercicio #5: Método burbuja - Copiar elementos de una lista")
# Copiando toda la lista
lista1 = [1]
lista2 = lista1[:] #: Permite copiar toda la lista
lista1[0] = 2
print(lista2)
print("ó")
miLista = [10, 8, 6, 4, 2]
nuevLista = miLista  [:] 
print(nuevLista)

# Copiando parte de la lista
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:3] #Le indica desde que indice quiere copiar la lista (inicio) y hasta cual ya no hacerlo (fin - 1) 
print(nuevaLista)
 
print("Rodaja: indice negativo")
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [1:-1] #rodaja
print(nuevaLista)
print("ó")
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [-1:1]
print(nuevaLista)
print("Burbuja Sin inicio")
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [:3]
print(nuevaLista)
print("Burbuja sin fin")
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[3:]
print(nuevaLista)

print("\nEjercicio #6 Eliminar rodajas con del")
miLista = [10, 8, 6, 4, 2]
del miLista[1:3] 
print(miLista)
print("Elimina todos los elementos a la vez")
miLista = [10, 8, 6, 4, 2]
del miLista[:] 
print(miLista)
print("Eliminar la lista por completo")
miLista = [10, 8, 6, 4, 2]
del miLista 
print(miLista) #Esta linea mandara error, puesto que ya no existe la lista

print("\nIn y Not en las listas")
miLista = [0, 3, 12, 8, 2]
print(5 in miLista)
print(5 not in miLista)
print(12 in miLista)

print("\nProgramas simples de listas #1")
miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista[0]
for i in range(1, len(miLista)):
   if miLista [i]> mayor:
        mayor = miLista[i]
print(mayor)
print("ó")
miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista [0]
for i in miLista [1:]:
   if i > mayor:
        mayor = i
print(mayor)

print("\nProgramas simples de listas #2")
miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 5
Encontrado = False
for i in range(len(miLista)):
    Encontrado = miLista[i] == Encontrar
    if Encontrado:
        break
if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0

for numeros in seleccionados:
    if numeros in sorteados:
        aciertos += 1

print(aciertos)