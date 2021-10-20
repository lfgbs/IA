def impar(value):
    return value%2

func = lambda x : True if impar(value)==0 else False

lista=[1,2,3,4,6,7]

for value in lista: 
    print(func(value))


