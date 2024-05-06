exec(open('util.py').read())
def opw(ray):
	for a in range(0,len(ray)):
		#print (a)
		print (a,ray[a])
	qui = 0
	while(qui<1):
		opu = input("url to open?e to end = ")
		if opu=="e":
			break
		neu(ray[int(opu)],2,1)
inp = []
opw(inp)