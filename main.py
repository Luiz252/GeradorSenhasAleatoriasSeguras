import random

letra_maiuscula = chr(random.randint(65, 90))
letra_minuscula = chr(random.randint(97, 122))
caractere_especial = chr(33)
lista_numeros = []

for i in range(5): #até 8 digitos
    numeros = random.randrange(9)
    lista_numeros.append(numeros)

random.shuffle(lista_numeros)
lista_numeros = str(lista_numeros) [1:-1]
lista_numeros = lista_numeros.replace(",","")

print(letra_maiuscula, letra_minuscula , lista_numeros , caractere_especial)
