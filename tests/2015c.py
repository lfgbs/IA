def interpretacoes(lista):
    values=[True, False]
    atributions=[]
    final=[]
    for value in values:
        atributions+=[[(elem, value)] for elem in lista]

    
    #final = list(set([atributions]))
    return atributions


lista=["a", "b"]
print(interpretacoes(lista))