def F(x,y):
	return(2*x+y)

def show_aplic(list1, list2):
    final_list=[]
    if len(list1) == len(list2):    
        print(aplic_comb(list1, list2, final_list))
    else: 
        return None

def aplic_comb(list1, list2, final_list):
    if list1==[]:
        return final_list
    else:
        final_list.append(F(list1[0], list2[0]))
        return aplic_comb(list1[1:], list2[1:], final_list)

lista = [1,4,5]
lista1 = [9,0,1]

show_aplic(lista,lista1)
    