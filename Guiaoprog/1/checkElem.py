def checkElem(list,elem):
    if list == []:
        return False
    else:
        if elem == list[0]:
            return True
        else:
            return checkElem(list[1:], elem)

lista1=[1,2,3]
lista2=[1,2]
print(checkElem(lista1, 3))
print(checkElem(lista2, 3))