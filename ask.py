exec(open('util.py').read())
def ask(ray):
	for a in range(0,len(ray)):
		ray[a] = [ray[a]]
		ray[a].append(str(input(ray[a][0]+" = ")))
	return ray

inp = []
ask(inp)