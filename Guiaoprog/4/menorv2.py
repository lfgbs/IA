func = lambda x,y: x if x<y else y

def menor(list):
    if list!=[]:
        menor = list[0]
        for value in list:
            menor = func(menor, value)

            filtered_list=[x for x in list if x!=menor]

        return (menor, filtered_list)
    else:
        return None
    

lista = [-1, 5, 7, 0 ,2, -1]
lista2 = [1,3,4]
lista3=[1]
lista4=[]

print(menor(lista))
print(menor(lista2))
print(menor(lista3))
print(menor(lista4))