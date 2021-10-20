def check(lista1, lista2):

    for value in lista1:
        if value not in lista2:
            return False
    
    return True

lista = [-1, 0, -1]
lista2 = [1,3,4]
lista3 = [1,5,4,7,3]

print(check(lista, lista2))
print(check(lista2, lista3))