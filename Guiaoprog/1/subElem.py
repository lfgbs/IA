def sub(list, subList,x,y):
    if list == []:
        return subList

    else:
        subList.append(list[0])
        if subList[-1] == x:
            subList[-1]=y
        return sub(list[1:], subList, x, y)


def showSub(list,x,y):
    subList=[]
    print(sub(list, subList, x, y))

lista1 = [5,67,3]
lista2 = [1, 4, 5, 5]

showSub(lista1,67,2)
showSub(lista2, 5, 1)