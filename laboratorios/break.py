"""
La instrucción break se usa para salir/terminar un ciclo.
Diseña un programa que use un ciclo while y le pida continuamente al usuario que ingrese una palabra a menos que 
ingrese "chupacabra" como la palabra de salida secreta, en cuyo caso el mensaje "¡Has dejado el ciclo con éxito". 
Debe imprimirse en la pantalla y el ciclo debe terminar.
No imprimas ninguna de las palabras ingresadas por el usuario. Utiliza el concepto de ejecución condicional y 
la declaración break.
"""
palabraSecreta = "chupacabra"


while True: 
    palabra = input("Ingresa una palabra: ") 
    if palabra == palabraSecreta: 
        break
    else: 
        palabra = input("Ingresa una palabra")
print("¡Has dejado el ciclo con éxito!")