"""
La tarea es completar el código para evaluar y mostrar el resultado de cuatro operaciones 
aritméticas básicas.
El resultado debe ser mostrado en consola.
Quizá no podrás proteger el código de un usuario que intente dividir entre cero. 
Por ahora, no hay que preocuparse por ello.
Prueba tu código - ¿Produce los resultados esperados?
"""
# ingresa un valor flotante para la variable a aquí
a = float(input("Valor de a: "))
# ingresa un valor flotante para la variable b aquí
b = float(input("Valor de b: "))
# muestra el resultado de la suma aquí
suma = a + b 
print(f"El resultado de sumas {a} + {b} es {suma}")
# muestra el resultado de la resta aquí
resta = a - b
print(f"El resultado de restar {a} - {b} es {resta}")
# muestra el resultado de la multiplicación aquí
multiplicacion = a * b
print(f"El resultado de multiplicar {a} x {b} es {multiplicacion}")
# muestra el resultado de la división aquí
division = a / b
print(f"El resultado de dividir {a} / {b} es {division}")

print("\n¡Eso es todo, amigos!")