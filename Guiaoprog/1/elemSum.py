def elemSum(list,sum):
    if list == []:
        return sum
    else:
        sum += list[0]
        return elemSum(list[1:],sum)

sum=0
lista1=[1,2,3]
lista2=[1,2]
print( elemSum(lista1, sum))
print( elemSum(lista2, sum))
