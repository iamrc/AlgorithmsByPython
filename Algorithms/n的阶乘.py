def factor(n):
	return reduce(lambda x,y: x*y, range(1, n+1))
    
fact = lambda n: 1 if n==0 else n*fact(n-1)
