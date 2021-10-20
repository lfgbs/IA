def tail(list):
    cauda=list[1:]
    if cauda != []:
        return cauda
    else:
        return None

lista1=[1]
lista2=[2,3,4]

print(tail(lista1))
print(tail(lista2))