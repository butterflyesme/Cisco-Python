"""
Usando uno de los operadores de comparación en Python, escribe un programa simple de dos líneas que 
tome el parámetro n como entrada, que es un entero, e imprime False si n es menor que 100, y True si 
n es mayor o igual que 100.
Ejemplo de entrada: 55
Resultado esperado: False
Ejemplo de entrada: 99
Resultado esperado: False
Ejemplo de entrada: 100
Resultado esperado: True
Ejemplo de entrada: 101
Resultado esperado: True
Ejemplo de entrada: -5
Resultado esperado: False
Ejemplo de entrada: +123
Resultado esperado: True
"""
n = 55
print(n >= 100)
n = 99
print(n  >= 100)
n = 100
print (n >= 100)
n = 101
print(n >= 100)
n = -5
print(n >= 100)
n = +123
print(n >= 100)