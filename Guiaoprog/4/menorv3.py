#se o menor valor se repetir, os dois primeiros valores do tuplo serão esse valor

func = lambda x,y: True if x<y else False

def check(x,y,z):
    if not func(x,z):
        y=x
        x=z
    else:
        if not func(y,z):
            y=z
    return (x,y)


def menor(list):
    if len(list)>1:
        menor = list[0]
        menor2 = list[1]
        for value in list[1:]:
            tup = check(menor, menor2, value)
            menor = tup[0]
            menor2 = tup[1]

            filtered_list=[x for x in list if x!=menor and x!=menor2]

        return (menor, menor2, filtered_list)
    else:
        return None
    

lista = [4,-1, 5, 7, 0 ,2, -1]
lista1 = [4,-1, 5, 7, 0 ,2]
lista2 = [1,3,4]
lista3=[1]

print(menor(lista))
print(menor(lista1))
print(menor(lista2))
print(menor(lista3))
