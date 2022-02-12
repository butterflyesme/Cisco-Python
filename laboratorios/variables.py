"""
-Crear las variables: juan, maria, y adan.
-Asignar valores a las variables. El valor debe de ser igual al numero de manzanas que cada quien tenía.
-Una vez almacenados los números en las variables, imprimir las variables en una línea, y separar cada 
 una de ellas con una coma.
-Después se debe crear una nueva variable llamada totalManzanas y se debe igualar a la suma de las tres 
  variables anteriores.
-Imprime el valor almacenado en totalManzanas en la consola.
-Experimenta con tu código: crea nuevas variables, asigna diferentes valores a ellas, y realiza varias 
 operaciones aritméticas con ellas (por ejemplo, +, -, *, /, //, etc.). Intenta poner una cadena con un 
 entero juntos en la misma línea, por ejemplo, "Numero Total de Manzanas:" y totalManzanas.
"""
maria =int(input("¿Cuantas manzanas tienes Maria? "))
juan = int(input("¿Cuantas manzanas tienes Juan? "))
adan = int(input("¿Cuantas manzanad tiene Adan? "))

print(f"{maria}, {juan}, {adan}")

totalManzanas = maria + juan + adan
print(f"Entre los tres tienen {totalManzanas} manzanas")

manzanasRegalar = int(input("¿Cuantas manzanas regalaran? "))
manzanasRegaladas= totalManzanas - manzanasRegalar
print(f"Adan le regalo {manzanasRegalar} manzanas a Max para que le lleve a su mama. Y les quedaron {manzanasRegaladas} manzanas")
total_manzanas = manzanasRegaladas // 3
print(f"Al repartirse lo que queda de manzanas, a cada uno le toca {total_manzanas}")
print("\n")
print("Por agradecimiento, Max les dijo que fueran a recolectar Naranjas!")
print(f"Maria recolecto el doble de naranjas de las manzanas que recolecto Juan")
total_naranja_maria = juan * 2
print(f"Maria tiene {total_naranja_maria} naranjas y {total_manzanas} manzanas")
print(f"Adan recolecto la mitad de naranjas de las manzanas que recolecto Maria")
total_naranja_adan = maria // 2
print(f"Maria tiene {total_naranja_adan} naranjas y {total_manzanas} manzanas")
print(f"Juan recolecto 10 naranjas mas de las manzanas que recolecto Adan")
total_naranja_adan =adan + 10
print(f"Juan tiene {total_naranja_adan} naranjas y {total_manzanas} manzanas")