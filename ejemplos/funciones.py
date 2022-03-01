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

print("\nEjercicio #11")
def imc(peso, altura):
    return peso / altura ** 2
print(imc(52.5, 1.65))

print("\nEjercicio #11.1")
def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    return peso / altura ** 2
print(imc(352.5, 1.65))

print("\nEjercicio #11.2") #Pulgadas
def lbakg(lb):
    return lb * 0.45359237
print(lbakg(1))

print("\nEjercicio #11.3") #pies y pulgadas
def piepulgam(pie, pulgada):
    return pie * 0.3048 + pulgada * 0.0254

print("\n",piepulgam(1, 1))

def piepulgam(pie, pulgada = 0.0):
    return pie * 0.3048 + pulgada * 0.0254
print(piepulgam(6))

print("\nEjercicio #11.4")
print("¿Cual es el IMC de una persona que tiene 5'7' de altura y un peso de 176 lbs?")
def piespulgam(pies, pulgadas = 0.0):
    return pies * 0.3048 + pulgadas * 0.0254


def lbsakg(lb):
    return lb * 0.45359237


def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    
    return peso / altura ** 2


print(imc(peso = lbsakg(176), altura = piespulgam(5, 7)))

print("\nEjercicio #12")
print("Formando triangulos con tres parámetros")
def esUnTriangulo(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(esUnTriangulo (1, 1, 1))
print(esUnTriangulo (1, 1, 3))

print("\nEjercicio #13")
print("Triangulo y teorema de pitagoras")
def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

if esUnTriangulo(a, b, c):
    print("Felicidades, puede ser un triángulo.")
else:
    print("Lo siento, no puede ser un triángulo.")
    
print("\nEjercicio #14")
print("Campo de una función")
def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def campoTriangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return None
    return heron(a, b, c)

print(campoTriangulo(1., 1., 2. ** .5))