#Ejercicio 1
print("Ejercicio 1")
for i in range(1, 11):
    if i % 2 != 0:
        print(f"{i} es impar")

print("\nEjercicio 2")
x = 1
while x < 11:
    if x % 2 != 0:
        print(f"{x} es impar")
    x += 1

print("\nEjercicio 3")
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end= "")

print("\nEjercicio 4")
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

print("\nEjercicio 5")
n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)
print("\nEjercicio 6")
n = range(4)
for num in n:
    print(num - 1)
else:
    print(num)

print("\nEjercicio 7")
for i in range(0, 6, 3):
    print(i)