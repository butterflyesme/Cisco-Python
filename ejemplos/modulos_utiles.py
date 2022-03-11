#Ejercicio 1
from random import random

for i in range(5):
    print(random())
print()

#Ejercicio 2
from random import random, seed

seed(0)

for i in range(5):
    print(random())
print()

#Ejercicio 3
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))
print()

#Ejercicio 4
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')
print()

#Ejercicio 5
from random import choice, sample

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(lst))
print(sample(lst, 5))
print(sample(lst, 10))