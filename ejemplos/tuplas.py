print("Ejercicio #1")
miTupla = (1, 10, 100, 1000)

print(miTupla[0])
print(miTupla[-1])
print(miTupla[1:])
print(miTupla[:-2])

for elem in miTupla:
    print(elem)
    
print("\nEjercicio #2")
miTupla = (1, 10, 100)

t1 = miTupla + (1000, 10000)
t2 = miTupla * 3

print(len(t2))
print(t1)
print(t2)
print(10 in miTupla)
print(-10 not in miTupla)