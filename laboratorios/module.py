"""
Se creara un experimento, donde se creara un paquete, Uno de ellos sera el modulo en si, que es "module.py
, el segundo archivo contiene el código usando el nuevo módulo. Su nombre es main.py
"""
__counter = 0

def suml(list):
	global __counter
	__counter += 1
	sum = 0
	for el in list:
		sum += el
	return sum

def prodl(list):
	global __counter	
	__counter += 1
	prod = 1
	for el in list:
		prod *= el
	return prod

if __name__ == "__main__":
	print("I prefer to be a module, but I can do some tests for you")
	l = [i+1 for i in range(5)]
	print(suml(l) == 15)
	print(prodl(l) == 120)