#Excepcion 1
import math

x = float(input("Ingresa x: "))
y = math.sqrt(x)

print("La raíz cuadrada de", x, "es igual a", y)
print()

#Excepcion 2
primerNumero = int(input("Ingresa el primer numero: "))
segundoNumero = int(input("Ingresa el segundo numero: "))

if segundoNumero != 0:
    print(primerNumero / segundoNumero)
else:
    print("Esta operacion no puede ser realizada.")

print("FIN.")
print()

#Excepcion 3
#Este es el enfoque favorito de Python
primerNumero = int(input("Ingresa el primer numero: "))
segundoNumero = int(input("Ingresa el segundo numero: "))

if segundoNumero != 0:
    print(primerNumero / segundoNumero)
else:
    print("Esta operacion no puede ser realizada.")

print("FIN.")
print()

#Excepcion 4
try:
    print("1")
    x = 1 / 0 #El denominador no puede ser 0
    print("2")
except:
    print("Oh cielos, algo salio mal...")

print("3")
print()

#Excepcion 5
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
except:
    print("Oh cielos, algo salio mal...")

print("FIN.")
print()

#Excepcion 6
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")

print("THE END.")
print()

#Excepciones 7 
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")

print("FIN.")
print()

#Excepciones 8 
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")

print("FIN.")
print()

#Excepcion 9
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Uuuppsss...")

print("FIN.")
print()

#Excepcion 10
try:
    y = 1 / 0
except ArithmeticError:
    print("Uuuppsss...")

print("FIN.")
print()

#Excepcion 11
try:
    y = 1 / 0
except ZeroDivisionError:
    print("¡División entre Cero!")
except ArithmeticError:
    print("¡Problema aritmético!")

print("FIN.")
print()

#Excepcion 12
try:
    y = 1 / 0
except ArithmeticError:
    print("¡Problema aritmético!")
except ZeroDivisionError:
    print("¡División entre Cero!")

print("FIN.")
print()

#Excepcion 13
def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema aritmético!")
    return None

badFun(0)

print("FIN.")
print()

#Excepcion 14
def badFun(n):
    return 1 / n

try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¡Se lanzo una excepción!")

print("FIN.")
print()

#Excepcion 15
def badFun(n):
    raise ZeroDivisionError

try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")

#Excepcion 16
def badFun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise

try:
    badFun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")
print()

#Excepcion 17
import math

x = float(input("Ingresa un numero: "))
assert x >= 0.0

x = math.sqrt(x)
print(x)
print()

