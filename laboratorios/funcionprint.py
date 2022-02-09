"""
Modifica la primera línea de código en el editor, utilizando las palabras clave sep y end, 
para que coincida con el resultado esperado. Recuerda, utilizar dos funciones print().
No cambies nada en la segunda invocación de print().
datos entrada: 
print("Fundamentos","Programación","en")
print("Python")
dato salida: 
Fundamentos***Programación***en...Python
"""
print("Fundamentos","Programación","en",sep="***",end="...")
print("Python")
