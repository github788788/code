exec(open('util.py').read())
def med3(inp):
	ray = []
	ray.append(mwh4(inp))
	ray.append(ant4(inp))
	nav2(ray)

inp = []
med3(inp)