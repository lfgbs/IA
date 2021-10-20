def reverse(lista, listainversa):
	if lista==[]:
		return listainversa
	else:
		listainversa[0:0]=lista[0:1]
		return reverse(lista[1:], listainversa)

def checkCapicua(lista):
    listainversa = []
    if reverse(lista, listainversa) == lista:
       return True
    else:
        return False

lista=[1,2,3,2,5]
lista1=[1,2,1]
print(checkCapicua(lista))
print(checkCapicua(lista1))