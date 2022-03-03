from statistics import variance
from turtle import update


print("Ejercicio #1")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
numerosTelefono = {'jefe' : 5551234567, 'Suzy' : 22657854310}
diccionarioVacio = {}

print(dict)
print(numerosTelefono)
print(diccionarioVacio)

print("\nEjercicio #2")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'leon', 'caballo']

for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "no está en el diccionario")

print("\nEjercicio #3")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in dict.keys():
    print(key, "->", dict[key])

print("\nEjercicio #4")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
for key in sorted(dict.keys()):
    print(key, "->", dict[key])
          
print("\nEjercicio #5")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
for spanish, french in dict.items():
    print(spanish, "->", french)
    
print("\nEjercicio #6")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
for french in dict.values():
    print(french)
    
print("\nEjercicio #7")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict['cisne'] = 'cygne'
print(dict)

print("\nEjercicio #8")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
dict.update({"pato" : "canard"})
print(dict)

print("\nEjercico #9")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

del dict['perro']
print(dict)

print("\nEjercicio #10")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict.popitem()
print(dict)    # outputs: {'gato' : 'chat', 'perro' : 'chien'}


print("----")
tup = (1, 2, 4, 8)
tup = tup[1: -1]
tup = tup[0]
print(tup)