def reverse(lista, listainversa):
	if lista==[]:
		return listainversa
	else:
		listainversa[0:0]=lista[0:1]
		return reverse(lista[1:], listainversa)

lista=[1,2,3,5]
listainversa=[]
print(reverse(lista, listainversa))