def listConc(head,tail):
    tail[0:0]=head
    return tail

lista1=[1,2,3]
lista2=[1,2]

print(listConc(lista1,lista2))