exec(open('util.py').read())
def var(inp):
	ray = []
	for a,val in enumerate(inp):
		bac = input(val+" = ")
		ray.append(bac)
	return ray
inp = []
var(inp)