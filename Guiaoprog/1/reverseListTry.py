def reverse(list):
    reverseList = reversedLists[lists[list]]
    if list == []:
        return reverseList
    else:
        reverseList[0:0]=list[0:1]
        return reverse(list[1:])

def saveReverse(list):

    if list not in lists.keys():
        lists[list] = count
        reversedLists[lists[list]]=[]

        reverse(list)

        """
        if list == []:
            reversedLists[list]=count
            count+=1
            return saveReverse(list)
        
        else:
            return saveReverse(list[1:])

        """

    else:
        return reversedLists[lists[list]]
    

count=0
lists={}
reversedLists={}
lista1=[1,2,3]
lista2=[1,2]
print(reverse(lista1))
print(reverse(lista2))

