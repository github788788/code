exec(open('util.py').read())
def mop(pic):
	ray = []
	ray.append(["m",mai,[1,""]])
	ray.append(["p",pro,[1,""]])
	if pic=="":
		pic = geq(ray)
	for a in range(0,len(ray)):
		if pic==ray[a][0]:
			ray[a][1](ray[a][2])
			break


"""inp = []
mop(inp)