def concLists(listOfLists, concList):
    if listOfLists == []:
        return concList

    else:
        concList[0:0]=listOfLists[-1]
        return concLists(listOfLists[:-1], concList)

def showConcLists(listOfLists):
    conclist=[]
    print(concLists(listOfLists ,conclist))

listOfLists=[[1,2], [5,67,3], [10]]
showConcLists(listOfLists)

