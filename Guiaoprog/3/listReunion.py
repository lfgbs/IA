def reunion(list1, list2, common):
    if list1 == []:
        if common == []:
            return None
        return common
    
    else:
        if list1[0]==list2[0]:
            

def checkLen(list1,list2):
    if len(list1) != len(list2):
        return False
    return True

def show(list1, list2):
    common=[]
    if checkLen:
        print(reunion(list, common))
    else:
        print("As listas não têm o mesmo comprimento")