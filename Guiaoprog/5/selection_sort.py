comp_menor = lambda x,y: True if x<y else False

def sort(list, sorted_list):
    pos=0
    menor_pos=0
    menor = list[0]
    if len(list)>2:
        for value in list[1:]: #skips the first element cause its already stored 
            pos+=1
            if  not comp_menor(menor, value):
                menor_pos=pos
                menor = value
        sorted_list.append(menor)  
        list.pop(menor_pos)
        return(sort(list, sorted_list))
    else:
        if comp_menor(list[0], list[1]):
            sorted_list.append(list[0])
            sorted_list.append(list[1])
        else:
            sorted_list.append(list[1])
            sorted_list.append(list[0])
        return sorted_list

def show_sort(list):
    sorted_list=[]
    print(sort(list, sorted_list))

lista = [-1, 5, 10, 0, -34 ,2, -1,9,1,0]
show_sort(lista)