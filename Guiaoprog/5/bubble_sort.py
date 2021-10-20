#não sei o que se está a passar
comp_maior = lambda x,y: True if x>y else False

def sort(list):
    for value in list:
        i=0
        while i<len(list)-1:
            if comp_maior(list[i], list[i+1]):
                temp = list[i+1]
                list[i+1]=list[1]
                list[i]=temp
            i+=1
    return list

lista = [-1, 5, 10, 0, -34 ,2, -1,9,1,0]
print(sort(lista))
    