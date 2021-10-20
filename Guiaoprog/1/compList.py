def calcComp(list, count):
    if list == []:
        return count
    else:
        count+=1
        return(calcComp(list[1:],count)) 

count=0
lista1=[1,2,3]
lista2=[1,2]
print(calcComp(lista1,count))
print(calcComp(lista2,count))