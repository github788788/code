exec(open('util.py').read())
def rta(fi):
	fi = open(fi, "r")
	lo = fi.read()
	co = lo.count("\n\n")
	st = 0
	for a in range(0,co):
		sl = lo.find("\n\n",st)
		li = lo[st:sl]
		print(li)
		st = sl+1

	#print co
	return lo

inp = []
rta(inp)