def countOccurrences(list,dict):
    if list==[]:
        return dict
    else:
        if list[0] not in dict.keys():
            dict[list[0]]=1
        else:
            dict[list[0]]+=1
        return countOccurrences(list[1:], dict)
def show(list):
    dict={}
    print(countOccurrences(list, dict))

lista = [1,3,3,6,7,3]
lista1 = [3,6,7,3]
show(lista)
show(lista1)