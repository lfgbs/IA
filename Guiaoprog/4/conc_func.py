func = lambda x: x**2

def conc(list1, list2):
    list1 = [func(x) for x in list1]
    list2 = [func(x) for x in list2]

    list_return = list2

    list_return[0:0]=list1[:]

    return list2

lista = [1,4,5]
lista1 = [9,0,1]

print(conc(lista,lista1))