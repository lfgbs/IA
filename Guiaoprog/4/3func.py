def h (x,y):
	return(x+y)

def f(x,y):
	return(x-y)

def g(x,y):
	return(2*x+y)

func = lambda h,f,g,x,y,z : h(f(x,y),g(y,z))

print(func(h,f,g,1,2,3))
print(func(h,f,g, 3,6,1))