# Este código busca una palabra de un texto predeterminado u otro texto que ingrese el usuario
''' Este código se escribió usando disccionarios, el valor es la inicial 
de una palabra y la key es el indice de la posicion de la inicial en la 
cadena de texto. Esto genera el problema que no guarda todas las iniciales 
de cada palabra. Como en el diccionario el valor 'value()' es la inicial 
de la una palabra, si dos palabras diferentes tienen la misma inicial, el 
valor se va reemplazando por cada palabra nueva con la misma inicial '''
# Se desea realizar un fork donde se usen tuplas para resolver el problema

alternativeText = input("¿Deseas introducir un texto? Presiona Y/N: ")
text = "Nadie entre aquí que no sepa Geometría"
if alternativeText.lower() == "y":
    text = input("Escribe tu texto: ")
    while text[-1] == " ":
        text = text[:-1]
elif alternativeText.lower() == "n":
    print("Entonces usaremos el siguiente texto:")
    print(text)
else:
    print("No reconozco el comando que escribiste, por esa razon usaremos el siguiente texto:")
    print(text)

iniciales = [text[0]]
indiceDeLetra = [0]
for i in range(len(text)):
    letra = text[i]
    if letra == " ":
        iniciales.append(text[i+1])
        indiceDeLetra.append(i+1)
print(iniciales,indiceDeLetra)
dictLetraIndice = {iniciales[i] : indiceDeLetra[i] for i in range(len(iniciales))}
print(dictLetraIndice)

inicialChar = input("Escribe la inicial con que empieza la plabra que buscas: ")
while inicialChar not in iniciales:
    print("La letra que escribiste no es la inicial de alguna palabra del texto.")
    inicialChar = input("Por favor, escribe la inicial con que empieza la plabra que buscas: ")

inicio = 0
fin = 0
if inicialChar in iniciales:
    inicio = dictLetraIndice[inicialChar]
    for i in range(len(indiceDeLetra)):
        if indiceDeLetra[i] == inicio:
            try:
                fin = indiceDeLetra[i+1]
            except IndexError:
                fin = len(text)
print(text[inicio:fin])