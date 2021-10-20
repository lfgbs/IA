def sepPares(list, first, second):
    if list == []:
        second[0:0] = first[:]
        return second

    else:
        first.append(list[0][0])
        second.append(list[0][1])
        return sepPares(list[1:], first, second)

def show(list):
    first=[]
    second=[]
    print(sepPares(list,first,second))

lista=[(1,3),(2,4)]
show(lista)