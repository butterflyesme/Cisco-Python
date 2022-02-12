"""
La tarea es completar el código para poder evaluar una expresión:
El resultado debe de ser asignado a y. Se cauteloso, observa los operadores y priorízalos.
Utiliza cuantos paréntesis sean necesarios.

Puedes utilizar variables adicionales para acortar la expresión (sin embargo, no es muy necesario).
Prueba tu código cuidadosamente.

Datos de Prueba
Entrada de muestra: 1
Salida esperada:
y = 0.6000000000000001
Entrada de muestra: 10
Salida esperada:
y = 0.09901951266867294
Entrada de muestra: 100
Salida esperada:
y = 0.009999000199950014
Entrada de muestra: -5
Salida esperada:
y = -0.19258202567760344
"""
x = float(input("Ingresa el valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("El resultado de la expresión es ", y)