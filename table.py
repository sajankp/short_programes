from math import *
def sq_root(a,y):
	while True:
		d= abs(y*y-a)
		e= 0.000000001
		if d<e:
			return y
			break
		else:
			x=y
			y=(x+(a/x))/2.
def table(i):
	z=1
	while z<i:
		print (i,end=' ')
		a=sq_root(z,1)
		print (a,end=' ')
		x=abs(len(str(a))-25)
		print(' '*x,end=' ')
		b=sqrt(z)
		print (b,end=' ')
		y=abs(len(str(b))-25)
		print(' '*y,end=' ')
		c=b-a
		print(c)
		z=z+1
