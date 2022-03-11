#AssertionError
from math import tan, radians
angle = int(input('Ingresa el angulo entero en grados: '))

# debemos estar seguros de ese angulo != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))
print()

#IndexError
# el codigo muestra una forma extravagante
# de dejar el bucle

lista = [1, 2, 3, 4, 5]
ix = 0
doit = True

while doit:
    try:
        print(lista[ix])
        ix += 1
    except IndexError:
        doit = False

print('Listo')
print()

#KeyboarInterrupt
# este código no puede ser terminado
# presionando Ctrl-C

from time import sleep
seconds = 0
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("¡No hagas eso!")
print()

#MemoryError
# este código causa la excepción MemoryError
# advertencia: ejecutar este código puede ser crucial
# para tu sistema operativo
# ¡no lo ejecutes en entornos de producción!

string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('¡Esto no es gracioso!')
print()

#OverflowError
# el código imprime los valores subsequentes 
# de exp(k), k = 1, 2, 4, 8, 16, ...

from math import exp
ex = 1
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('El número es demasiado grande.')
print()

#ImportError
# una de estas importaciones fallará, ¿cuál será?
try:
    import math
    import time
    import abracadabra

except:
    print('Una de sus importaciones ha fallado.')
print()

#KeyError
# como abusar del diccionario
# y cómo lidiar con ello

dict = { 'a' : 'b', 'b' : 'c', 'c' : 'd' }
ch = 'a'
try:
    while True:
        ch = dict[ch]
        print(ch)
except KeyError:
    print('No existe tal clave:', ch)