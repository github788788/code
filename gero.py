exec(open('util.py').read())
def gero(ray):
	for a in range(0,len(ray)):
		ray[a].append(input(ray[a][0]+" = "))
	return ray
inp = []
gero(inp)