exec(open('util.py').read())
def mwt(inp):
	ray = []
	ray.append(mwh3(inp))
	ray.append(ant3(inp))
	for a in range(0,len(ray)):
		for b in range(0,len(ray[a])):
			print (a,b,ray[a][b])
	#sys.exit()
	
	for a in range(0,len(ray)):
		if a==0:
			at(1,1)
		spe = ray[a]
		raf5(spe)
	print (ray)
inp = []
mwt(inp)