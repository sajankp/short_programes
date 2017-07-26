def find_hcf(a,b):
	if b==0:
		return print (a)
	else:
		r=a%b
		find_hcf(b,r)

