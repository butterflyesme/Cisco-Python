print("""Laboratorio: Leer ints de forma segura
Tu tarea es escribir una función capaz de ingresar valores enteros y verificar si están dentro de un rango especificado.
La función debe:
Aceptar tres argumentos: una entrada, un límite inferior aceptable y un límite superior aceptable.
Si el usuario ingresa una cadena que no es un valor entero, la función debe emitir el mensaje Error: entrada incorrecta, y solicitará al usuario que ingrese el valor nuevamente.
Si el usuario ingresa un número que está fuera del rango especificado, la función debe emitir el mensaje Error: el valor no está dentro del rango permitido (min..max) y solicitará al usuario que ingrese el valor nuevamente.
Si el valor de entrada es válido, será regresado como resultado.
Datos de Prueba
Prueba tu código cuidadosamente.
Así es como la función debería reaccionar ante la entrada del usuario:
Ingresa un número entre -10 a 10: 100
Error: el valor no está dentro del rango permitido (-10..10)
Ingresa un número entre -10 a 10: asd
Error: entrada incorrecta
Ingresa un número entre -10 a 10: 1
El número es: 1
""")
def readint(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: entrada incorrecta")
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print("Error: el valor no esta dentro del rango permitido (" + str(min) + ".." + str(max) + ")")
    return value;

v = readint("Ingresa un número entre -10 a 10: ", -10, 10)

print("El numero es:", v)