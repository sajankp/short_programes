def A(m,n):
	if m<0 or n<0:
		return 'not possible'
	elif m==0:
		return n+1
	elif n==0:
		a=A(m-1,1)
		return a
	else:
		x=A(m,n-1)
		y=A(m-1,x)
		return y 


