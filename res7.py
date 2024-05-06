exec(open('util.py').read())
def res7(com):

	ray = []
	ray.append(["r",["right"]])
	ray.append(["l",["left"]])
	ray.append(["rd",["right","right","down"]])
	ray.append(["ld",["left","left","down"]])
	ray.append(["ru",["right","right","up"]])
	ray.append(["lu",["left","left","up"]])


	for a in range(0,len(ray)):
		val = ray[a][0]
		if com==val:
			loc = ray[a][1]
			#at(1,1)
			res6(loc)
			break
			"""inp = []
res7(inp)