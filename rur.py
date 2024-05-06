exec(open('util.py').read())
def rur(ray):
	for a,val in enumerate(ray):
		val[0](val[1])
		"""
inp = []
rur(inp)