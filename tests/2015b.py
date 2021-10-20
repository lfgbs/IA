#Conjunto das partes

def g(lista):
    if lista==[]:
        return [[]]
    y=g(lista[1:])
    return y + [[lista[0]]+ z for z in y]


lista = [1,2,3]
print(g(lista))