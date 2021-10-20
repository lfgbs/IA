func = lambda x : True if x > 0 else False

def check(lista):

        positives_lista = [x for x in lista if func(x)]

        if positives_lista!=[]:
            return True

        return False

lista = [-1, 0, -1]
lista2 = [1,3,4]

print(check(lista))
print(check(lista2))


