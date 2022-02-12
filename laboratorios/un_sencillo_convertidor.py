"""
-Millas y kilómetros son unidades de longitud o distancia.
-Teniendo en mente que 1 equivale aproximadamente a 1.61 kilómetros, complemente el programa en el 
editor para que convierta de:
Millas a kilómetros.
Kilómetros a millas.
-No se debe cambiar el código existente. Escribe tu código en los lugares indicados con ###. Prueba tu 
programa con los datos que han sido provistos en el código fuente.
-Pon mucha atención a lo que esta ocurriendo dentro de la función print(). Analiza como es que se proveen 
múltiples argumentos para la función, y como es que se muestra el resultado.
Nota que algunos de los argumentos dentro de la función print() son cadenas (por ejemplo "millas son", 
y otros son variables (por ejemplo millas).
Resultado esperado: 
7.38 millas son 11.88 kilómetros
12.25 kilómetros son 7.61 millas
"""
print("CONVERTIDOR DE MILLAS A KILOMETROS Y KILOMETROS A MILLAS")
kilometros = 12.25
millas = 7.38

millas_a_kilometros = millas / 0.62137
kilometros_a_millas = kilometros* 0.62137

print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")
print("\nCONVERTIDOR DE USD A EUR Y DE EUR A USD")
euro = int(input("Ingresa los EUR que quieres covertir a USD: "))
dolar = int(input("Ingresa los USD que quieres convertir a EUR: "))
dolares_a_euros = 1.14039 * euro
euros_a_dolares = 0.87694435 * dolar
print(euro, " Euros son ", round(dolares_a_euros), " Dolares")
print(dolar, "Dolares son ", round(euros_a_dolares), " Euros")
print("\nCONVERTIDOR DE TEMPERATURA")
temperatura = int(input("Temperatura que quieres convertir: "))

F = temperatura * 1.8  + 32
print(f"{temperatura} °C a °F es {F}")
C = (temperatura - 32) / 1.8
print(f"{temperatura} °F a °C es {C}")
C = temperatura - 273.15
print(f"{temperatura} K a °C es {C}")
K = temperatura + 273.15
print(f"{temperatura} °C a K es {K}")
K = 5/9 * (temperatura - 32) + 273.159
print(f"{temperatura} °F a K es {K}")
F = 1.8*(temperatura - 273.15) + 32
print(f"{temperatura} °K a F es {F}")