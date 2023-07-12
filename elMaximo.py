import random
lista = [5,8,7,915,16,15,886,153,1565,1575,156,1535]
max = random.choice(lista)
print(max)
for i in range(len(lista)):
    if max < lista[i]:
        max = lista[i]
print(max)