#Ejercicio 1 
import math
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14
print(sin(pi/2))
print(math.sin(math.pi/2))
print()

#Ejercicio 2
from math import sin, pi
print(sin(pi/2))
pi = 3.14
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
    
print(sin(pi/2))
print()

#Ejercicio 3
pi = 3.14	# linea 01
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None	# linea 07

print(sin(pi/2))	# linea 09
from math import sin, pi	# linea 12
print(sin(pi/2))	# linea 14
print()

#Ejercicio 4
print("Ejercicio 4")
from math import pi, radians, degrees, sin, cos, tan, asin
ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
print()

#Ejercicio 5
from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))
print()

#Ejercicio 6
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))