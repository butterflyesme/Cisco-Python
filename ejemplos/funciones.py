print("Ejemplo #1")
def mensaje(numero):
    print("Ingresa un número:", numero)

mensaje(1)

print("\nEjemplo 2")
def mensaje(numero):
    print("Ingresa un número:", numero)

numero = 1234
mensaje(1)
print(numero)

print("\nEjercicio #3")
def mensaje(que, numero):
    print("Ingresa", que, "número", numero)

mensaje("teléfono", 11)

print("\nEjercicio #4")
def miFuncion(a, b, c):
    print(a, b, c)

miFuncion(1, 2, 3)
          
print("\nEjercicio #5")
def presentar(primerNombre, segundoNombre):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("Luke", "Skywalker")
presentar("Jesse", "Quick")
presentar("Clark", "Kent")

print("\nEjercicio #6")
def presentar (primerNombre, segundoNombre):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar(primerNombre = "James", segundoNombre = "Bond")
presentar(segundoNombre = "Skywalker", primerNombre = "Luke")

print("\nEjercicio #7")
def suma(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
suma(9, 18, 27)

print("\nEjercicio #7.1")
def suma(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
suma(c= 9, a = 27, b= 18)

print("\nEjercicio #8")
def presentar(primerNombre, segundoNombre="González"):
    print("Hola, mi nombre es", primerNombre, segundoNombre)
presentar("Jorge", "Pérez")

print("\nEjercicio #8.1")
def presentar(primerNombre, segundoNombre="González"):
    print("Hola, mi nombre es", primerNombre, segundoNombre)
presentar("Jorge") #presentar (primerNombre="Guillermo")

print("\nEjercicio #8.2")
def presentar(primerNombre="Juan", segundoNombre="González"):
    print("Hola, mi nombre es ", primerNombre, segundoNombre)
presentar ()

print("\nEjercicio #9")
def happynewyear(deseos = True):
    print("Tres ...")
    print("Dos ...")
    print("Uno ...")
    if not deseos:
        return
    
    print("¡Feliz año nuevo!") 
happynewyear()

print("\nEjercicio #9.1")
def funcion_aburrida():
    return 123

x = funcion_aburrida()
print ("La funcion_aburrida ha devuelto su resultado. Es: ", x) 

print("\nEjercicio #9.2")
def funcion_aburrida():
        print("'Modo aburrimiento' ON.")
        return 123

print("¡Esta lección es interesante!")
funcion_aburrida()
print("Esta lección es aburrida ...") 

print("\nEjercicio #10")
def sumaDeLista(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    return sum
print(sumaDeLista([5, 4, 3]))

print("\nEjercicio #10.1")
def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    return strangeList

print(strangeListFunction(5))
