exec(open('util.py').read())
def med(inp):
	a = ""	

	ray = []

	ray.append(mwh2)
	ray.append(ant2)

	for a in range(0,len(ray)):
		ray[a] = [ray[a],a]
	
	for a in range(0,len(ray)):
		ray[a][0](ray[a][1])

inp = []
med(inp)