print("""
ENCRIPTANDO UN MENSAJE
El código, alimentado con este mensaje:
AVE CAESAR
Da como salida:
BWFDBFTBS
""")
# Cifrado César
text = input("Ingresa tu mensaje: ")
cifrado = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cifrado += chr(code)

print(cifrado)
print()
print("DESCIFRANDO UN MENSAJE")
print("Descifrando un mensaje")
# Cifrado César - descifrar un mensaje
cifrado = input('Ingresa tu criptograma: ')
text = ''
for char in cifrado:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)