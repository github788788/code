exec(open('util.py').read())
def pic(ray,ind):
	que = ""
	for a in range(0,len(ray)):
		que = que +ray[a][ind]#+" for "+ray[a][0][0]
		#if a<len(ray)-1:
		#	que = que+","
	que = que+" = "
	pic = input(que)
	return pic



inp = []
pic(inp)