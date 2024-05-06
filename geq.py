exec(open('util.py').read())
def geq(ray):
	que = ""
	for a in range(0,len(ray)):
		que = que +ray[a][0]
		#if a<len(ray)-1:
		#	que = que+","
	que = que+" = "
	pic = input(que)
	return pic
inp = []
geq(inp)