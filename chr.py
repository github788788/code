exec(open('util.py').read())
def chr(ray):
	cha = 1
	if cha==1:
		for a in range(0,len(ray)):
			val = ray[a]
			val = val[val.find("\n")+1:val.find("\n\n")]
			fn1 = val.find("\n")
			fn2 = val.find("\n",fn1+1)
			fn3 = val.find("\n",fn2)
			#fn4 = val.find("\n",fn3)
			val = val[0:fn3]
			qui=0
			while(qui<1):
				if val[0]==" ":
					val = val[1:len(val)]
				if val[0]!=" ":
					qui = 1
			ray[a]=val
	return ray 
inp = []
chr(inp)