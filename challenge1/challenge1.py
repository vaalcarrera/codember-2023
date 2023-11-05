with open('message_01.txt', 'r') as archivo:
    contenido = archivo.read()

palabras = contenido.split()
conteo_palabras = {}

for palabra in palabras:
    palabra = palabra.lower()
    
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

resultado = ''

for palabra, recuento in conteo_palabras.items():
    resultado +=  f'{palabra}{recuento}'

print(resultado)