exec(open('util.py').read())
def exc(ray,ind):
	for a in range(0,len(ray)):
		coi = ray[a][ind]
		if int(coi)==1:
			ray[a][1]()

	
inp = []
exc(inp)