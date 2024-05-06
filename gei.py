exec(open('util.py').read())
def gei(ray,ind):
	for a in range(0,len(ray)):
		pro = ray[a][ind]+" = "
		ray[a].append(input(pro))
	return ray
inp = []
gei(inp)