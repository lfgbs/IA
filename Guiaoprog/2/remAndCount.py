def remAndCount(list, remList, elem, count):
    if list==[]:
        tuple = (remList, count)
        return tuple 

    else:
        if list[0] != elem:
            remList.append(list[0])
        else:
            count+=1
        return remAndCount(list[1:], remList, elem, count)

def show(list, elem):
    remList=[]
    count=0
    print(remAndCount(list, remList, elem, count))


lista = [1,3,3,6,7,3]
lista1 = [1,3,3,6,7,3]
show(lista,3)
show(lista,7)