func = lambda x,y: x if x<y else y

def menor(list):
    menor = list[0]
    for value in list:
        menor = func(menor, value)
    return menor

lista = [-1, 5, 7, 0, -34 ,2, -1]
lista2 = [1,3,4]

print(menor(lista))
print(menor(lista2))
